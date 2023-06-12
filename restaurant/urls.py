from django.urls import path
from restaurant.views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path("", index, name='home'),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
]
