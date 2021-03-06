from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stores', views.StoreViewSet, basename='store')
router.register('carts', views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls))
]
