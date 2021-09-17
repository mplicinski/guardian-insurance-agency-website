from typing import ContextManager
from django.shortcuts import render
from django.views.generic import TemplateView

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


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
    