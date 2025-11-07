from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('purchase/', views.purchase_car, name='purchase_car'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Додаємо обробку медіафайлів
