from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm


# Create your views here.


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('project_list')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})
