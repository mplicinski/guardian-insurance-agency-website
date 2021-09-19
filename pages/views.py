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
            'card_title1': "Personal Insurance",
            'card_text1': "We can guard your personal assets like your car and home with more than 15 of the best companies available. Learn more about our services in Home, Auto, and Life Insurance.",
            'img_src1': 'images/home.png',
            'img_alt1': "Picture of home",
            'button_link1':"personal",

            # card 2 - commerical
            'card_title2': "Commercial Insurance",
            'card_text2': "We can help protect the most important things to keep your business running smoothly. We offer a variety of policies for all types of businesses. Learn about our services, dump trucks, long distance hauling, contracting, and more.",
            'img_src2': 'images/trucks.png',
            'img_alt2': "Picture of truck parking lot",
            'button_link2':"commercial",

            # card 3 - about us
            'card_title3': "About Us",
            'card_text3': "Learn more about who we are and our experience in the insurance industry.",
            'img_src3': 'images/header_bg.png',
            'img_alt3': "Picture of home",
            'button_link3':"about"
        })
        return context

class PersonalView(TemplateView):
    template_name = 'pages/personal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'header_title': "Personal",
            'header_subtitle': "Insurance for your personal assets",
            'header_img' : "images/personal_header.png",

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'header_title': "Commercial",
            'header_subtitle': "Insurance for your business and commercial assets",
            'header_img' : "images/commercial_header.png",

            # triple small card header section
            # card 1 - dump truck
            'card_title1': "Dump Truck Insurance",
            'card_text1': "Insurance for local dump haulers.",
            'card_img1': 'images/truck-monster-solid.png',
            'card_alt1': "Truck graphic",

            # card 2 - long distance transport
            'card_title2': "Long Distance Insurance",
            'card_text2': "Insurance for long distance hauling & transport",
            'card_img2': 'images/truck-moving-solid.png',
            'card_alt2': "Semi-truck graphic",

            # card 3 - contractor / business
            'card_title3': "Contractor Insurance",
            'card_text3': "Insurance for contractors and businesses.",
            'card_img3': 'images/tools-solid.png',
            'card_alt3': "Tools graphic",

            # features
            # feature 1 - dump truck
            'feature_title1': "Dump Truck Insurance",
            'feature_text1': "Dump truck insurance could include liability insurance, physical damage insurance, and workers compensation insurance. This all depends on whether you’d be working as an independent owner operator or for another trucking company. Whatever your dump truck needs are our agents will ensure you have all the coverages you need for whatever your personal situation is. ",
            'feature_img1': "images/dump.jpg",
            'feature_alt1': "Dump hauler on a construction site.",

            # feature 2 - long distance transport
            'feature_title2': "Long Distance Transport Insurance",
            'feature_text2':"We offer a great variety of trucking insurance. This includes coverage for anything from cargo haulers to auto haulers. We also offer cargo coverage, so we’ll make sure that you have right amount to completely cover whatever you’re hauling. Contact us and help us get you the perfect trucking policy so that you can have peace of mind when you’re out on the road.",
            'feature_img2': "images/long_distance.jpg",
            'feature_alt2': "Semi-truck driving down thte road.",

            # feature 3 - contractor / business
            'feature_title3': "Contractor & Business Insurance",
            'feature_text3': "Whatever your unique business policy needs are we can help you get the perfect policy to make sure all your bases are covered. This could include bodily injury, property damage, medical expenses, and defense costs, etc. When you get a policy with us you won’t have to worry about what could go wrong on the job and instead you can focus on providing the best service for your clients.",
            'feature_img3': "images/contractor.jpg",
            'feature_alt3': "A contractor working outside a home.",
        })
        return context


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
        recipient_list = ['mzp.devtesting@gmail.com']
        
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
    
    