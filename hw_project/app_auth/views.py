from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

class RegisterViews(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Congratulations {username}! Registration was successful!')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, context={'form': form})

# @login_required
def logoutuser(request):
    logout(request)
    return render(request, 'app_auth/logout.html', {})
