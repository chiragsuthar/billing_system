from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Bill
from .forms import ItemForm, BillForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def accounts(request):
    return render(request, 'account.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'billing/item_list.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'billing/item_form.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'billing/item_form.html', {'form': form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'billing/item_confirm_delete.html', {'item': item})

@login_required
def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.save()  # Save the bill to get an ID
            form.save_m2m()  # Save the many-to-many relationships
            bill.total_cost = bill.calculate_total_cost()
            bill.save()  # Save the bill again with updated total cost
            return redirect('bill_detail', pk=bill.pk)
    else:
        form = BillForm()
    return render(request, 'billing/bill_form.html', {'form': form})

@login_required
def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'billing/bill_detail.html', {'bill': bill})
