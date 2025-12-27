from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_card, contacts, products_list  # index, home,

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    path("catalog/<int:pk>/", product_card, name="product_card"),
    # path("contacts/", contacts, name="contacts"),
    # path("", index),
    path("", products_list, name="products_list")
]
