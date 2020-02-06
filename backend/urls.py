from django.contrib import admin
from django.urls import path, include
from backend.app.wallets.urls import router as wallet_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(
        wallet_router.urls,
    )),
]
