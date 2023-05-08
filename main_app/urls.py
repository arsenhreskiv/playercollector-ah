from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('players/', views.PlayerList.as_view(), name='player_index'),
    # path('players/<int:player_id>/', views.player_detail, name='detail'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('players/create/', views.PlayerCreateView.as_view(), name='player_create'),
    path('players/<int:pk>/update/', views.PlayerUpdateView.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name='player_delete'),
    path('players/<int:player_id>/add_training/', views.add_training, name='add_training'),
    path('players/<int:player_id>/assoc_boot/<int:boot_id>/', views.assoc_boot, name='assoc_boot'),
    path('players/<int:player_id>/unassoc_boot/<int:boot_id>/', views.unassoc_boot, name='unassoc_boot'),
    path('boots/', views.BootList.as_view(), name='boots_index'),
    path('boots/<int:pk>/', views.BootDetail.as_view(), name='boots_detail'),
    path('boots/create/', views.BootCreate.as_view(), name='boots_create'),
    path('boots/<int:pk>/update/', views.BootUpdate.as_view(), name='boots_update'),
    path('boots/<int:pk>/delete/', views.BootDelete.as_view(), name='boots_delete'),
]