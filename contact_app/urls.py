from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('xabarlar/', views.MessagesListView.as_view(), name='messages_list'),
]