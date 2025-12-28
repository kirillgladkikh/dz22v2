from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductCardView, ContactsView


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductCardView.as_view(), name='product_card'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]





# from django.urls import path
# from catalog.apps import CatalogConfig
# from catalog.views import product_card, contacts, products_list  # index, home,
#
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path("", products_list, name="products_list"),
#     path("catalog/<int:pk>/", product_card, name="product_card"),
#     path("contacts/", contacts, name="contacts"),
# ]
