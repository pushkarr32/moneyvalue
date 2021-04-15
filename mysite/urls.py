
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('creditcard.html',views.creditcard),
    path('personal_loan.html', views.personalloan),
    path('business_loan.html', views.businessloan),
    path('educationloan.html', views.educationloan),
    path('carloan.html', views.carloan),
    path('homeloan.html', views.homeloan),
    path('investment.html', views.investment),
    path('creditscore.html', views.creditscore),
    path('contact.html', views.contact),
    path('save-email', views.save_email),
    path('services.html', views.loanservices),
    path('blog.html', views.blogs),
    path('blog-details.html', views.blogdetails),
    path('team.html', views.team),
    path('testimonial.html', views.testimonial),
    path('how-it-work.html', views.howitwork),
    path('faq.html', views.faq),
    path('about.html', views.aboutus),
]