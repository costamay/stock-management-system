from django.shortcuts import render, redirect
from .models import *
from sales.forms import *


def sales(request):
    sales = Sale.objects.all()

    return render(request, 'sales/all_sales.html', locals())


def sales_report(request):
    sales = Sale.objects.all()
    total = [i.product.product_price * i.quantity for i in sales]
    final_total = sum(total)
    return render(request, 'reports/sales_report.html', locals())


def add_item(request, cls):

    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sales')

    else:
        form = cls()

        return render(request, 'sales/add_sell.html', locals())


def add_sell(request):
    return add_item(request, SalesForm)


def filter(request):
    sales = Sale.objects.filter(date__range=(
        request.POST['start_date'],
        request.POST['end_date']
    ))
    
    total = [i.product.product_price * i.quantity for i in sales]
    final_total = sum(total)
    
    return render(request, 'reports/sales_report.html',locals())