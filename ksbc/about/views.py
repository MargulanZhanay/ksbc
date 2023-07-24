from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutUsView(TemplateView):
    template_name = 'about/index.html'


class WhatWeDoView(TemplateView):
    template_name = 'about/what-we-do.html'


class OurStructureView(TemplateView):
    template_name = 'about/our-structure.html'


def ContactUsView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        from_email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        message = request.POST['message']
        name = first_name + ' ' + last_name
        email_body = f'{name}\n\n {phone_number} - {from_email} - {subject} \n\n {message}'
        send_mail(
            subject,
            email_body,
            from_email,
            ['mcmrkr@gmail.com'],
        )
        return render(request, 'about/contact-us.html', {
            'first_name': first_name,
            'last_name': last_name
        })
    else:
        return render(request, 'about/contact-us.html', {})