from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.login_page, name='login_page'),
    path('dashboard/<str:unique_id>/', views.dashboard, name='dashboard_page'),
    path('events/<str:unique_id>/', views.events_page, name='events_page'),
    path('events/create/<str:unique_id>/', views.create_event, name='create_event'),
    
    path('events/view/<str:event_id>/', views.view_event, name='view_event'),
    path('api/events/delete-event/<str:event_id>/', views.delete_event, name='delete_event'),
    path('api/events/update-event/<str:event_id>/', views.update_event, name='update_event'),


    path('circular/<str:unique_id>/', views.circulars_page, name='circulars_page'),
    path('delete_circular/<str:id>/', views.delete_circular, name='delete_circular'),
    path('get_circular/<str:id>/', views.get_circular, name='get_circular'),
    path('edit_circular/<str:id>/', views.edit_circular, name='edit_circular'),
    path('add_circular/', views.create_circular, name='add_circular'),
    path('view_circular/<str:circular_id>/', views.view_circular, name='view_circular'),

    path('signout/', views.sign_out, name='sign_out'),
    path('debug/', views.debug_view, name='debug_view'),
]
