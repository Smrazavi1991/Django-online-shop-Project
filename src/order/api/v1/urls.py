from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import AddToCartView
from user.views import *

urlpatterns = [
    path("add_to_cart/", AddToCartView.as_view(), name="Add to cart"),
    # path("", Home.as_view(), name="Home-page"),
    # path("register/", Register.as_view(), name="Register"),
    # path("verification/", Verification.as_view(), name="Verification"),
    # path("login/", Login.as_view(), name="Login"),
    # path("profile/", Profile.as_view(), name="Profile"),
    # path("category/<int:pk>/", CategoryProducts.as_view(), name="Category-page"),
    # path("product/<int:pk>/", ProductDetails.as_view(), name="Product-page"),
    # path("api/v1/user/", include('user.api.v1.urls')),
    # path("/api/v1/cart", include('order.api.v1.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)