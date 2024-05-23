from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def admin(request):
    return render(request, 'admin.html')

def user_login(request):
    return render(request, 'user_login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html') 

# user

# admin
def create_item(request):
    return render(request, 'createItem.html')

def create_subscription(request):
    return render(request, 'createSubscription.html')

def edit_item(request):
    return render(request, 'editItem.html')

def edit_subscription(request):
    return render(request, 'editSubscription.html')

def view_item(request):
    return render(request, 'viewItem.html')

def view_subscription(request):
    return render(request, 'viewSubscription.html')

def delete_item(request):
    return render(request, 'deleteItem.html')

def delete_subscription(request):
    return render(request, 'deleteSubscription.html')

def view_all_items(request):
    return render(request, 'viewAllItems.html')

def view_all_subscriptions(request):
    return render(request, 'viewAllSubscriptions.html')

# subscription

# rating
