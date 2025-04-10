from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, EditUserProfileForm  # Importa los formularios
from .models import Profile

@login_required
def edit_profile(request):
    user = request.user
    profile = None
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile(user=user) # Crea un perfil si no existe

    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=user)
        profile_form = EditUserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profiles:profile_view')
    else:
        user_form = EditProfileForm(instance=user)
        profile_form = EditUserProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })