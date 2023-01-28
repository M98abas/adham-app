from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.get,name='Indexing'),
    path('register/',views.register,name='registeration'),
    path('login/',views.login_view, name="login_user"),
    path('get-request/',views.get_all_requested, name="get_reqiest"),
    path('get-users/',views.get_all_users, name="get_users"),
    path('accepted/<str:email>',views.update, name="accepted"),
    path('rejected/<str:email>',views.reject, name="rejected"),
    path('logout/',views.user_logout, name="logout_admin_user"),
]
