
from django.views.generic import ListView
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Membership, UserMembership, Subscription
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import stripe
import time
from django.utils.decorators import method_decorator


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request)
    )
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
            membership_type=membership_type
        )
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


@method_decorator(login_required, name='dispatch')
class MembershipSelectView(ListView):
    model = Membership

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership_type = request.POST.get('membership_type')

        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)

        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type
        )
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()
        else:
            selected_membership = None

        if user_membership.membership == selected_membership:
            if user_subscription is not None:
                messages.info(
                    request, 'You already have this membership. Your \
                    next payment is due {}'.format(
                        'get this value from stripe'
                    )
                )
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        request.session['selected_membership_type'] = (
            selected_membership.membership_type if selected_membership else None
        )
        return HttpResponseRedirect(reverse('membership:payment'))


@login_required(login_url='users:login')
def product_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    selected_membership = None
    if request.method == 'POST':
        selected_membership = get_selected_membership(request)
        price = selected_membership.stripe_plan_id
        customer = stripe.Customer.create(email=request.user.email)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            customer=customer['id'],
            success_url=settings.REDIRECT_DOMAIN + (
                '/payment_successful?session_id={CHECKOUT_SESSION_ID}'
            ),
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        user_membership = get_user_membership(request)
        user_membership.stripe_checkout_id = checkout_session['id']
        user_membership.save()
        return redirect(checkout_session.url, code=303)
    context = {
        'selected_membership': selected_membership
    }
    return render(request, 'membership/membership_payment.html', context)


# use Stripe dummy card: 4242 4242 4242 4242
@login_required(login_url='users:lo')
def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_membership = get_object_or_404(UserMembership, user=request.user)
    selected_membership = get_selected_membership(request)
    user_membership.payment_successful = True
    user_membership.membership = selected_membership
    user_membership.save()
    new_subscription = Subscription.objects.create(
        user_membership=user_membership,
        stripe_subscription_id=session.subscription,
        active=True
    )
    return render(request, 'membership/payment_successful.html', {
        'customer': customer,
        'subscription': new_subscription,
        'username': user_membership.user.get_full_name(),
    })


def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    return render(request, 'membership/payment_cancelled.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_KEY
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        user_membership = UserMembership.objects.get(
            stripe_checkout_id=session_id
        )
        user_membership.payment_successful = True
        user_membership.save()
    return HttpResponse(status=200)


def profile(request):
    user_membership = UserMembership.objects.get(user=request.user)

    return render(request, 'users/profile.html', {
        'user': request.user,
        'user_membership': user_membership,
    })
