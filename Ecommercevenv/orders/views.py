from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='account')
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    context = {'cart':cart_obj}
    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj,created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item,created = OrderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj,
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')

def remove(request,pk):
    product = OrderedItem.objects.get(pk=pk)
    if product:
        product.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        total = request.POST.get('total')
        print(total)
        order_obj = Order.objects.get(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        if order_obj:
           order_obj.order_status=Order.ORDER_CONFIRMED
           order_obj.total_price=total
           order_obj.save()
           status_message = "Your Oder is Processed. Your item will be delivered soon"
           messages.success(request,status_message)
        else:
            status_message = "Unable to Processed. No items in Cart"
            messages.error(request,status_message)
    return redirect('cart')

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {'all_orders':all_orders}
    return render(request,'orders.html',context)