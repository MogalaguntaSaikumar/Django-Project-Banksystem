from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Admin, Customer, Transaction

# ---------- ADMIN LOGIN ----------
def admin_login(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        admin = Admin.objects.filter(Username=Username, Password=Password).first()

        if admin:
            request.session['admin'] = admin.Username
            request.session['role'] = admin.Role
            return redirect('admin_menu')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# ---------- ADMIN MENU ----------
def admin_menu(request):
    if 'admin' not in request.session:
        return redirect('login')

    return render(request, 'admin_menu.html', {
        'role': request.session['role']
    })


# ---------- CREATE ACCOUNT ----------
def create_account(request):
    if request.method == "POST":
        Customer.objects.create(
            Custid=request.POST.get('Custid'),
            Accno=request.POST.get('Accno'),
            Name=request.POST.get('Name'),
            Password=request.POST.get('Password'),
            Dob=request.POST.get('Dob'),
            Phno=request.POST.get('Phno'),
            Amount=request.POST.get('Amount')
        )
        return redirect('admin_menu')

    return render(request, 'create_account.html')


# ---------- DEPOSIT ----------
def deposit(request):
    if request.method == "POST":
        Accno = request.POST.get('Accno')
        Amount = float(request.POST.get('Amount'))

        customer = Customer.objects.filter(Accno=Accno).first()
        if customer:
            customer.Amount += Amount
            customer.save()

            Transaction.objects.create(
                Date=timezone.now(),
                Accno=Accno,
                Type='d',
                Amount=Amount
            )
            return redirect('admin_menu')

    return render(request, 'deposit.html')


# ---------- WITHDRAW ----------
def withdraw(request):
    if request.method == "POST":
        Accno = request.POST.get('Accno')
        Amount = float(request.POST.get('Amount'))

        customer = Customer.objects.filter(Accno=Accno).first()
        if customer and customer.Amount >= Amount:
            customer.Amount -= Amount
            customer.save()

            Transaction.objects.create(
                Date=timezone.now(),
                Accno=Accno,
                Type='w',
                Amount=Amount
            )
            return redirect('admin_menu')

    return render(request, 'withdraw.html')


# ---------- BALANCE ----------
def balance(request):
    balance = None
    if request.method == "POST":
        Accno = request.POST.get('Accno')
        customer = Customer.objects.filter(Accno=Accno).first()
        if customer:
            balance = customer.Amount

    return render(request, 'balance.html', {'balance': balance})


# ---------- STATEMENT ----------
def statement(request):
    transactions = []
    if request.method == "POST":
        Accno = request.POST.get('Accno')
        transactions = Transaction.objects.filter(Accno=Accno)

    return render(request, 'statement.html', {'transactions': transactions})


# ---------- LOGOUT ----------
def logout(request):
    request.session.flush()
    return redirect('login')
