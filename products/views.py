from django.shortcuts import render,redirect,HttpResponse
from products.forms import *
import json
from django.core import serializers

def product_list(request):
    # products =  Product.objects.all()
    products = serializers.serialize('json', Product.objects.all())
    # json_data=json.dumps(industry)
    return HttpResponse(products,content_type='application/json')    

def product_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk,id) 
            print(product)
            form = ProductForm(instance=product)
        return render(request,"products/product_form.html",{'form':form})
    else:
        if id == 0:
            form = ProductForm(request.POST,request.FILES)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance=product) 
        if form.is_valid():
            form.save()
        return redirect('/store')

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/products/list')
