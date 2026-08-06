from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from .models import Order


def home(request):
    return render(request, "home.html")


# -------------------------------
# Task 1 : My Orders
# -------------------------------
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )


# -------------------------------
# Task 2 : Post Product
# -------------------------------
@permission_required(
    'accounts.add_product',
    raise_exception=True
)
def post_product(request):

    return render(
        request,
        "post_product.html"
    )


# -------------------------------
# Task 4 : Login
# -------------------------------
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            if user.groups.filter(name="Seller").exists():
                return redirect("seller_dashboard")

            elif user.groups.filter(name="Buyer").exists():
                return redirect("buyer_dashboard")

            elif user.groups.filter(name="Admin").exists():
                return redirect("admin_dashboard")

            else:
             return redirect("home")

            

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(
        request,
        "login.html"
    )


# -------------------------------
# Seller Dashboard
# -------------------------------
@login_required
def seller_dashboard(request):

    return render(
        request,
        "seller_dashboard.html"
    )


# -------------------------------
# Buyer Dashboard
# -------------------------------
@login_required
def buyer_dashboard(request):

    return render(
        request,
        "buyer_dashboard.html"
    )


# -------------------------------
# Logout
# -------------------------------
@login_required
def user_logout(request):

    logout(request)

    return redirect("login")

@login_required
def admin_dashboard(request):

    return render(
        request,
        "admin_dashboard.html"
    )