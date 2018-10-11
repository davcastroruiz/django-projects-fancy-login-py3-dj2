
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from principal.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', include('principal.urls')),
    path('login/', auth_views.LoginView, {'next_page': '/'}, name='login'),
    #ctrl+d copy and past the line
    path('logout/', logout_view, name='logout'),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)