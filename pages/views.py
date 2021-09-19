from typing import ContextManager
from django import forms
from django.contrib.messages.api import MessageFailure
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'header_title': "Personal",
            'header_subtitle': "Insurance for your personal assets",

            # triple small card header section
            # card 1 - home
            'card_title1': "Home Insurance",
            'card_text1': "Insurance for your home or living space as well as your belongings.",
            'card_img1': 'images/home-solid.png',
            'card_alt1': "Home graphic",

            # card 2 - auto
            'card_title2': "Auto Insurance",
            'card_text2': "Insurance for your car or any other vehicles you own.",
            'card_img2': 'images/car-solid.png',
            'card_alt2': "Car graphic",

            # card 3 - life
            'card_title3': "Life Insurance",
            'card_text3': "Insurance to protect and secure your family’s future.",
            'card_img3': 'images/star-of-life-solid.png',
            'card_alt3': "Home graphic",

            # features
            # feature 1 - home
            'feature_title1': "Home Insurance",
            'feature_text1': "Home insurance protects your home and your belongings kept inside the home. Whatever your living situation is we can help ensure that you have the best policies for your assets. Our policies offer the best and more comprehensive coverage for your belongings at the most competitive prices. Why not save some money and combine your home and auto insurance as a bundle?",
            'feature_img1': "images/home2.jpg",
            'feature_alt1': "Suburban home",

            # feature 2 - auto
            'feature_title2': "Auto Insurance",
            'feature_text2':"Auto insurance can protect your cars, trucks, motorcycles and other road vehicles. With the proper auto insurance, you’ll be protecting yourself from bodily injury and damage to your car. If you do need to make a claim, we’ll help you call it in and make sure you receive all the benefits and protections from your policy. Feel confident on the road after we help you choose the best auto insurance plan.",
            'feature_img2': "images/auto.jpg",
            'feature_alt2': "Chevrolet Camaro driving on the road",

            # feature 3 - life
            'feature_title3': "Life Insurance",
            'feature_text3': "Life insurance ensures that your family’s future is protected in case you become unable to provide for them anymore. Sometimes disaster strikes but we can ensure that you have peace of mind for your family’s security no matter what happens. Help us find the best life insurance policy for you so that you never have to worry what would happen if you couldn’t be there for your family.",
            'feature_img3': "images/life.jpg",
            'feature_alt3': "Family walking together on a trail",
        })
        return context


class CommercialView(TemplateView):
    template_name = 'pages/commercial.html'


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
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
        recipient_list = ['mplicinski@gmail.com']
        
        if 'cert' in full_message.lower() or 'cert' in subject.lower():  # checking for possible certificate request
            recipient_list.append('erzinsurance@gmail.com') # add commercial email 

        send_mail(subject, full_message, email_from, recipient_list)
        messages.success(self.request, "Contact form submission successful. We'll get back to you soon!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Error submitting form")
        redirect(reverse_lazy('contact'))
        return super().form_invalid(form)

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
    