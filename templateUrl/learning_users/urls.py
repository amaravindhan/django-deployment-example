from django.urls import path
from learning_users import views

#Template Tagging
app_name = "learning_users"

urlpatterns = [
    path('signup/', views.signup, name = "register"),
    path('login/', views.user_login, name = "user_login"),
    path('logout/', views.user_logout, name = "user_logout"),
    path('special/', views.special, name = "special"),
]
