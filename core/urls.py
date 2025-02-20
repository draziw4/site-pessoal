from django.urls import path
from .views import HomeView, login_view, logout_view, VlogView,RegistroView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('vlogs/', VlogView.as_view(), name='vlog'),
    path("registro/", RegistroView.as_view(), name="registro"),  # Nova rota para registro
]
