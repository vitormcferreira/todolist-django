from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class IsNotAuthenticatedUser(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('todolist:home')


class LoginView(IsNotAuthenticatedUser, auth_views.LoginView):
    next_page = 'todolist:home'


class RegisterView(IsNotAuthenticatedUser, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/register.html'
