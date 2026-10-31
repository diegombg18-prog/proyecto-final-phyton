from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, UserUpdateForm, PerfilUpdateForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada con éxito! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'usuarios/editar_perfil.html', context)