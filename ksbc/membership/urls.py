from django.urls import path

from .views import MembershipSelectView, product_page, payment_successful, payment_cancelled, stripe_webhook, profile

app_name = 'membership'


urlpatterns = [
    path(
        'membership/',
        MembershipSelectView.as_view(),
        name='membership-list'
    ),
    path('payment', product_page, name='payment'),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment_cancelled/', payment_cancelled, name='payment_cancelled'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('profile/', profile, name='profile')
]
