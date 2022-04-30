from django.urls import path
from django.views.generic import TemplateView

from portfolio.views import PortfolioView, PortfolioDetailView, AboutDetailView

urlpatterns = [
    path('post/<int:pk>/', PortfolioDetailView.as_view(), name='post_detail'),
    path('', PortfolioView.as_view(), name='home'),
    path('about/', AboutDetailView.as_view(), name='about'),
    path('success/', TemplateView.as_view(template_name='success.html'))
]