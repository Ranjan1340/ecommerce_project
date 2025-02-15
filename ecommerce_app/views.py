from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart,Order, OrderItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect


def custom_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Get email from form
        password = request.POST.get("password")

        user = User.objects.filter(username=email).first()
        if user:  
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect("product_list") 
            else:pass
        
        return render(request, "login.html", {"error": "Invalid email or password"})

    return render(request, "login.html")

@login_required
def add_to_cart(request, product_id):
    quantity = int(request.GET.get("quantity", 1)) 
    print(quantity, "Selected Quantity")

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += quantity 
    else:
        cart_item.quantity = quantity  

    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return redirect('view_cart')

    if request.method == 'POST':
        delivery_address = request.POST.get('address')
        total_amount = sum(item.total_price() for item in cart_items)

        # Create an order with "Cash on Delivery"
        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount,
            delivery_address=delivery_address,
            payment_method="Cash on Delivery",
            status="Pending"
        )

        # Move cart items to order items
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)

        # Clear the cart
        cart_items.delete()

        return redirect('order_history')

    return render(request, 'checkout.html', {'cart_items': cart_items})

@login_required
def order_history(request):
    # orders = Order.objects.filter(user=request.user).order_by('-order_date')
    orders = Order.objects.filter(user=request.user).prefetch_related("items__product__category", "items__product__brand").order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def user_logout(request):
    logout(request)
    return redirect('login') 
