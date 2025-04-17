from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_transparente_view, name='checkout_transparente'),
    path('processar-pagamento/', views.processar_pagamento, name='processar_pagamento'),
    path('checkout/sucesso/', views.success_view, name='checkout_success'),
    path('checkout/erro/', views.failure_view, name='checkout_failure'),
    path('checkout/pendente/', views.pending_view, name='checkout_pending'),    
]