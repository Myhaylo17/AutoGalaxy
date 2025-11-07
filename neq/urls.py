from django.contrib import admin
from django.urls import path
from main import views  # Імпортуємо views з додатку main
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bmw/', views.bmw_page, name='bmw'),
    path('bmw/reserve/', views.reserve_bmw, name='reserve_bmw'),
    path('audi/', views.audi_page, name='audi'),
    path('mercedes/', views.mercedes_page, name='mercedes'),
    path('ford/', views.ford_page, name='ford'),
    path('porsche/', views.porsche_page, name='porsche'),
    path('tesla/', views.tesla_page, name='tesla'),
    path('volswagen/', views.volswagen_page, name='volswagen'),
    path('about_us/', views.about_us_page, name='about_us'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    path('car-enter/', views.car_enter, name='car_enter'),
    path('ford/rent/', views.ford_rent_car, name='ford_rental'),
    path('login/', views.login_s, name='login'),
    path('register/', views.register, name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)