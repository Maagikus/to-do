from django.urls import path
from .views import ToDoView, add_el, del_el, del_el_all, RegUser, LogUser, LogoutUser

urlpatterns = [
    path('', ToDoView.as_view(), name='todo'),
    path('add_el/<int:user_id>/', add_el, name='add_el'),
    path('del_el/<int:user_id>/<int:item_id>/', del_el, name='del_el'),
    path('del_el/<int:user_id>/', del_el_all, name='del_el_all'),
    path('reg_user/', RegUser, name='RegUser'),
    path('log_user/', LogUser, name='LogUser'),
    path('logout_user/', LogoutUser, name='Logout'),
]