from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from .forms import ProductForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# def Productpage(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = ProductForm()  # Reinitialize the form to blank after saving
#             return render(request, 'products_add.html', {'product_form': form, 'success': True})
#     else:
#         form = ProductForm()

#     context = {'product_form': form}
#     return render(request, 'products_add.html', context)

# def AllProducts(request):
#     all_products = Product.objects.all()  # Fetch all products from the database
#     context = {'all_products': all_products}  # Pass the products to the template
#     return render(request, 'products.html', context)

# def DeleteProducts(request,id):
#     selected_product= Product.objects.get(id=id)
#     selected_product.delete()
#     return redirect('/inventory/Products/')

# def UpdateProducts(request,id):
#     select_product= Product.objects.get(id=id)
#     context={"product_form" :ProductForm(instance=select_product)}
#     if request.method == "POST":
#         product_form = ProductForm(request.POST, instance=select_product)
#         if product_form.is_valid():
#             product_form.save()
#             return redirect('/inventory/Products/')
#     return render(request,'products_add.html', context)


class ProductsAddView(LoginRequiredMixin,View):
    login_url =''
    def get(self,request):
        print(" from class based get")
        form = ProductForm()
        context = {'product_form': form}
        return render(request, 'products_add.html', context)
    
    def post(self,request):
        print(" from post based save")
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/inventory/Products/')
        
# Class-Based View for listing all products
class ProductsListView(LoginRequiredMixin,View):
    login_url =''
    def get(self, request):
        all_products = Product.objects.all()  # Fetch all products from the database
        context = {'all_products': all_products}  # Pass the products to the template
        return render(request, 'products.html', context)

# Class-Based View for deleting a product
class ProductsDeleteView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)  # Safely fetch the product or return 404
        product.delete()  # Delete the product
        return redirect(reverse_lazy('all_products'))  # Redirect after deletion

# Class-Based View for updating a product
class ProductsUpdateView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)  # Fetch the product or return 404
        form = ProductForm(instance=product)  # Pre-populate the form with existing data
        context = {"product_form": form}
        return render(request, 'products_add.html', context)

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('all_products'))  # Redirect to the products list after update
        context = {"product_form": form}
        return render(request, 'products_add.html', context)

      