from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'mysite/index.html')

def creditcard(request):
    form = CreditCardForm()
    context = {'form': form }
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['error'] = form.errors
    return render(request,'mysite/creditcard.html', context=context)


def personalloan(request):
    form = PersonalLoanForm()
    context = {'form': form }
    if request.method == 'POST':
        form = PersonalLoanForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['error'] = form.errors
    return render(request,'mysite/personal_loan.html', context=context)

def investment(request):
    return render(request,'mysite/investment.html')

def creditscore(request):
    return render(request,'mysite/creditscore.html')

def homeloan(request):
    form = homeloanForm()
    context = {'form': form }
    if request.method == 'POST':
        form = homeloanForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['error'] = form.errors
    return render(request,'mysite/homeloan.html', context=context)

def businessloan(request):
    form = businessloanForm()
    context = {'form': form }
    if request.method == 'POST':
        form = businessloanForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'mysite/business_loan.html', context=context)

def educationloan(request):
    form = educationloanForm()
    context = {'form': form }
    if request.method == 'POST':
        form = educationloanForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'mysite/educationloan.html', context=context)

def carloan(request):
    form = carloanForm()
    context = {'form': form }
    if request.method == 'POST':
        form = carloanForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'mysite/carloan.html', context=context)

def contact(request):
    form = ContactForm()
    context = {'form': form }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'mysite/contact.html', context=context)


@csrf_exempt
def save_email(request):
    email = request.POST.get('email')
    print(request.POST, 'request posttttt', email)
    try:
        EmailRecord.objects.get(email=email)
    except EmailRecord.DoesNotExist:
        EmailRecord.objects.create(email=email)
    return HttpResponse('Saved Successfully')

def CreditCard(request):
    form = CreditCardForm()
    context = {'form': form }
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'mysite/creditcard.html', context=context)


def loanservices(request):
    return render(request,'mysite/services.html')

def blogs(request):
    return render(request,'mysite/blog.html')

def blogdetails(request):
    return render(request,'mysite/blog-details.html')

def team(request):
    return render(request,'mysite/team.html')

def testimonial(request):
    return render(request,'mysite/testimonial.html')

def howitwork(request):
    return render(request,'mysite/how-it-work.html')

def faq(request):
    return render(request,'mysite/faq.html')

def aboutus(request):
    return render(request,'mysite/about.html')



