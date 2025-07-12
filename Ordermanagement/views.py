from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required

@login_required(login_url='') 
def Customerpage(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerForm()  # Reinitialize the form after saving
            return render(request, 'customers_add.html', {'customer_form': form, 'success': True})
    else:
        form = CustomerForm()

    context = {'customer_form': form}
    return render(request, 'customers_add.html', context)

def AllCustomers(request):
    all_customers = Customer.objects.all()  # Fetch all customers
    context = {'all_customers': all_customers}  # Pass customers to template
    return render(request, 'customers.html', context)  # Ensure template name is correct

def DeleteCustomer(request, id):
    try:
        selected_customer = Customer.objects.get(id=id)
        selected_customer.delete()
    except Customer.DoesNotExist:
        pass  # Handle non-existent customer

    return redirect('/order/Customers/')  # Correct redirect path

def UpdateCustomer(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return redirect('/order/Customers/')  # Redirect if customer doesn't exist

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/order/Customers/')
    else:
        form = CustomerForm(instance=customer)

    context = {'customer_form': form}
    return render(request, 'customers_add.html', context)


def OrdersAdd(request):
    context = { 'order_form': Order_Form()}
    if request.method == 'POST':
        selected_product = Product.objects.get(id= request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = ( amount * selected_product.gst) / 100
        bill_amount = amount + gst_amount
        new_order = Orders(customer_reference_id = request.POST['customer_reference'] , 
        product_reference_id = request.POST['product_reference'], order_number = request.POST['order_number'], 
        order_date = request.POST['order_date'] , quantity = request.POST['quantity'] , 
        amount= amount , gst_amount =gst_amount, bill_amount = bill_amount)
        
        new_order.save()
        return redirect('/order/orders/')
    return render(request,'orders_add.html', context)


def Orderlist(request):
    context = { 'all_orders': Orders.objects.all() }
    return render(request, 'orders.html', context)


def OrdersDelete(request,id):
    order= Orders.objects.get(id=id)
    order.delete()
    return redirect('/order/orders/')

def OrdersUpdate(request,id):
    order=Orders.objects.get(id=id)
    context = { 'order_form' : Order_Form(instance= order)}
    
    if request.method ==  'POST' :
        
        selected_product = Product.objects.get(id= request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = ( amount * selected_product.gst) / 100
        bill_amount = amount + gst_amount
        
        order_filter =Orders.objects.filter(id=id)
        order_filter.update(customer_reference_id = request.POST['customer_reference'] , 
        product_reference_id = request.POST['product_reference'], order_number = request.POST['order_number'], 
        order_date = request.POST['order_date'] , quantity = request.POST['quantity'] , 
        amount= amount , gst_amount =gst_amount, bill_amount = bill_amount)
        
        return redirect('/order/orders/')
    return render(request,'orders_add.html', context)
