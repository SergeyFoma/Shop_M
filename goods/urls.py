from django.urls import path
from . import views

app_name="goods_name"

urlpatterns=[
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="catalog"),
    path("products/<slug:prod_slug>/", views.products, name="products"),
]