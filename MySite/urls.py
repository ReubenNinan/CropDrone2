from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('HomePage.urls')),
    path('DataPage/', include('LoginScreen.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls'))

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)