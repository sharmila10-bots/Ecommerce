from django.shortcuts import render,redirect
from testapp.models import Ecommerce
from testapp.forms import ConfirmationForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def welcome_data(request):
    return render(request,'testapp/welcome.html')

def fetch_data(request):
    ecommerce=Ecommerce.objects.all()
    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        ecommerce=ecommerce.filter(category__contains=item_name)
    my_dict={'ecommerce':ecommerce}
    return render(request,'testapp/home.html',my_dict)


class EcommerceDetailView(DetailView):
    model=Ecommerce


@login_required
def login_form(request):
    return render(request,'registeration/login.html')

@login_required
def confirm_view(request):
    if request.method=='POST':
        order_amount = 5000000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client=razorpay.Client(auth=('rzp_test_3WcdY7UpiOvxim','A0UNw9coiX5uEKgAmDFEdEnF'))
        payment=client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    ecommerce=Ecommerce.objects.all()
    my_dict={'ecommerce':ecommerce}
    return render(request,"testapp/checkout.html",my_dict)


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('/home')

    return render(request, 'testapp/signup.html', {'form': form})

def logout(request):
    return redirect('/welcome')

def about(request):
    return render(request,"testapp/about.html")
