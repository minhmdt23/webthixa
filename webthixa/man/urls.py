from django.urls import path
from . import views

app_name = 'man'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('conference/<int:conference_id>/', views.conference, name='conference'),
    path('nameplate/<int:nameplate_id>/', views.nameplate, name='nameplate'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('conference/<int:conference_id>/edit/', views.edit_conference, name='edit_conference'),
    path('conference/<int:conference_id>/edit/view_location', views.edit_conference_view_location, name='view_location'),
    path('completed/', views.completed, name='completed'),
]
