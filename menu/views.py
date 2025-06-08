from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Product
from .forms import ProductForm, CustomUserCreationForm

# Login va Logout View'lari
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Prefikssiz URL nomi
        else:
            return render(request, 'login.html', {'error': 'Нотўғри фойдаланувчи номи ёки парол!'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Home View
class HomeView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

# Taomlar View
class TaomlarView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Product.objects.filter(category__slug=category_slug, is_available=True)
        return Product.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            try:
                context['category'] = Category.objects.get(slug=category_slug)
            except Category.DoesNotExist:
                context['category'] = None
        context['is_admin'] = self.request.user.is_authenticated and getattr(self.request.user, 'is_admin', False)
        return context

    def test_func(self):
        return True  # Har kimga ruxsat, lekin adminlik tekshiruvi templateda bo'ladi

    def handle_no_permission(self):
        return self.render_to_response(self.get_context_data())  # Ruxsat bo'lmasa ham sahifani ko'rsat


# Product Create va Update View'lari
class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_admin', False)

    def handle_no_permission(self):
        return redirect('login')  # Adminga ruxsat bo‘lmasa asosiy sahifaga qaytarish

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

    def handle_no_permission(self):
        return redirect('login')  # Prefikssiz URL nomi

# Register View
class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        user.is_admin = False
        user.save()
        return super().form_valid(form)
    


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    template_name = 'product_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_admin', False)

    def handle_no_permission(self):
        return redirect('login')

