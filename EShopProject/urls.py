"""EShopProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from store.views.home import Index, store
from store.views.saveBuy import SaveBuy
from store.views.signup import Signup
from store.views.login import Login, logout
from store.views.cart import Cart
from store.views.checkout import CheckOut
from store.views.orders import OrderView
from store.auth import auth_middleware
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='check-out'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('orders', OrderView.as_view(), name='orders'),
    path('accounts/', include('allauth.urls')),
    path('saveorder/', SaveBuy.as_view(), name='update_user_after'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('accounts/', include('allauth.urls')),
)