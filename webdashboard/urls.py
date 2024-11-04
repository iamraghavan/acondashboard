from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.login_page, name='login_page'),
    path('dashboard/<str:unique_id>/', views.dashboard, name='dashboard_page'),
    path('events/<str:unique_id>/', views.events_page, name='events_page'),
    path('events/create/<str:unique_id>/', views.create_event, name='create_event'),
    
    path('events/view/<str:event_id>/', views.view_event, name='view_event'),
    path('api/events/get/', views.get_events_api, name='getEventsApi'),
    path('api/circulars/get/', views.get_circulars_api, name='getCircularsApi'),
    path('api/events/delete-event/<str:event_id>/', views.delete_event, name='delete_event'),
    path('api/events/update-event/<str:event_id>/', views.update_event, name='update_event'),


    path('circular/<str:unique_id>/', views.circulars_page, name='circulars_page'),
    path('delete_circular/<str:id>/', views.delete_circular, name='delete_circular'),
    path('get_circular/<str:id>/', views.get_circular, name='get_circular'),
    path('edit_circular/<str:id>/', views.edit_circular, name='edit_circular'),
    path('add_circular/', views.create_circular, name='add_circular'),
    path('view_circular/<str:circular_id>/', views.view_circular, name='view_circular'),


    path('gallerys/<str:unique_id>/', views.gallery, name="gallerys_page"),
    path('gallerys/create/<str:unique_id>/', views.create_folder, name='create_folder'),
    path('folders/', views.list_folders, name='list_folders'),
    path('upload/<int:folder_id>/', views.upload_modal, name='upload_modal'),
    path('folder/<int:folder_id>/gallery/<str:unique_id>/', views.folder_gallery, name='folder_gallery'),

    path('folder/<int:folder_id>/delete/', views.delete_folder, name='delete_folder'),
    path('folder/<int:folder_id>/gallery/', views.folder_gallery, name='folder_gallery'),
    path('folder/<int:folder_id>/gallery/<str:unique_id>/', views.folder_gallery, name='folder_gallery_with_unique_id'),

    path('gallery/d/kuppai-thotti/delete-image/<str:unique_id>/kuppa-thottila-podu/<int:image_id>/', views.delete_image, name='delete_image'),

    path('api/events/get/', views.get_events_api, name='getEventsApi'),
    path('api/circulars/get/', views.get_circulars_api, name='getCircularsApi'),

    path('signout/', views.sign_out, name='sign_out'),
    path('debug/', views.debug_view, name='debug_view'),
]
