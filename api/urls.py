from django.urls import path

from book_management_app.views import *

urlpatterns = [
    path('add_book/', add_book),
    path('sell_book/', sell),
    path('get_book/<int:id>', get_book)
]