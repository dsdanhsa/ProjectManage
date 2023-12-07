# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserProfileForm

def user_list(request):
    users = UserProfile.objects.all()

    # Sorting by name
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        users = users.order_by('name')
    elif sort_by == 'dob':
        users = users.order_by('dob')
    elif sort_by == 'role':
        users = users.order_by('role')

    return render(request, 'user_list.html', {'users': users, 'sort_by': sort_by})

def user_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('username:user_list')
    else:
        form = UserProfileForm()

    return render(request, 'user_form.html', {'form': form, 'action': 'Create'})

def user_update(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('username:user_list')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'user_form.html', {'form': form, 'action': 'Update'})

def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('username:user_list')

    return render(request, 'user_confirm_delete.html', {'user': user})
