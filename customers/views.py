from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()  # Tüm müşterileri veritabanından al
        return render(request, 'customer_list.html', {'customers': customers})
        