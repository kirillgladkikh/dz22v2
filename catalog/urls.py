from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    ProductsListView,
    ProductCardView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>/", ProductCardView.as_view(), name="product_card"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
