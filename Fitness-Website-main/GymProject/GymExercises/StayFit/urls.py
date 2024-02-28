from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from StayFit import views
from .views import exercise_create
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('products',views.product_list, name='product_list'),
    path('gexercises/', views.Gym_exercise, name='gym_exercises'),
    path('hexercises/', views.Home_exercises, name='Home_exercises'),
    path('yexercises/', views.yoga, name='yoga'),
    path('s_exercises/', views.stretch, name='stretch'),
    path('pt_exercises/', views.pt, name='pt'),
    #path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    #path('exercise/create/', views.exercise_create, name='exercise_create'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('create/', views.exercise_create, name='exercise_create'),
    path('contact/', views.contact, name='contact'),
     path('membership/', views.membership, name='membership'),
    #path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



