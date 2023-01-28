from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.get,name='index_page'),
    path('logout/',views.user_logout,name='logout'),
    path('request/',views.make_request,name='make_request'),
    path('success/',views.final_view,name='successs'),
    path('files/',views.get_files,name='files_form'),
    path('get_element/',views.get_my_request,name='getElement'),
    path('accounts/register/',views.register,name='registeration'),
    path('accounts/login/', views.login_view,name="login_local"),  
]
