from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('clubs/', clubs),
    path('club/<int:son>/', club),

    path('latest_transfers/', latest_transfers),
    path('players/', players),
    path('stats/record_transfers/', record_transfers),
    path('u20players/', u20players),
    path('seasons/', seasons),
    path('seasons/<str:mavsum>/', seasons),
    path('countries/<str:country>/', countries_country),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)