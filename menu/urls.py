from django.urls import path
from .views import HomeView, TaomlarView, ProductCreateView, ProductUpdateView, ProductDeleteView, login_view, logout_view, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<slug:category_slug>/', TaomlarView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),  # Tekshirish
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]