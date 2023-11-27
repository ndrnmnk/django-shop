from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.search, name='search'),
    path("search", views.search),
    path("create", views.create, name='create'),
    path('<int:pk>', views.GoodsDetailView.as_view(), name='goods-detail'),
    path('<int:pk>/update', views.GoodsUpdateView.as_view(), name='goods-update'),
    path('<int:pk>/delete', views.GoodsDeleteView.as_view(), name='goods-delete')
]