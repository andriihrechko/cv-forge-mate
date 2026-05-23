from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignInForm


class SignInView(CreateView):
    model = get_user_model()
    form_class = SignInForm
    template_name = "users/signin.html"
    success_url = reverse_lazy("users:login")
