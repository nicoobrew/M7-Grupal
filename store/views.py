from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from .models import Product


# Create your views here.
class Index(generic.ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_login"] = AuthenticationForm
        return context


class Details(generic.DetailView):
    model = Product
    template_name = 'store/product_details.html'


def welcome_page(request):
    return render(request, 'store/welcome.html')
