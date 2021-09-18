from typing import ContextManager
from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # card 1 - home
            'card_title1': "Context title",
            'card_text1': "With supporting text below as a natural lead-in to additional content.",
            'img_src1': 'images/home.jpg',
            'img_alt1': "Picture of home",

            # card 2 - commerical
            'card_title2': "Context title",
            'card_text2': "With supporting text below as a natural lead-in to additional content.",
            'img_src2': 'images/trucks.jpg',
            'img_alt2': "Picture of truck parking lot",

            # card 3 - about us
            'card_title3': "Context title",
            'card_text3': "With supporting text below as a natural lead-in to additional content.",
            'img_src3': 'images/header_bg.png',
            'img_alt3': "Picture of home",
        })
        return context

class PersonalView(TemplateView):
    template_name = 'pages/personal.html'


class CommercialView(TemplateView):
    template_name = 'pages/commercial.html'


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    # success_message = 'Form submission succesful'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        if phone_number == '':
            phone_number = "Not provided"
        full_message = f"Name: {name}\n\n Email: {email}\n\n Phone number: {phone_number}\n\n {message}" # constructing a full message including the sender name & email
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mzp.devtesting@gmail.com']
        
        if 'cert' in full_message.lower() or 'cert' in subject.lower():  # checking for possible certificate request
            recipient_list.append('erzinsurance@gmail.com') # add commercial email 

        send_mail(subject, full_message, email_from, recipient_list)
        messages.success(self.request, "Contact form submission successful. We'll get back to you soon!")
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
    