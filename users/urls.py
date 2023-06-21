from .views import SingupView, ProfileView, UpdateProfileView, AddRemoveSavedView, SavedView, RecentlyViewedView

from django.urls import path

app_name ='users'
urlpatterns = [
    path('singup', SingupView.as_view(),  name = 'singup'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('addremovesaved/<int:product_id>', AddRemoveSavedView.as_view(), name = 'addremovesaved'),
    path('saveds', SavedView.as_view(), name = 'saveds'),
    path('recently_viewed', RecentlyViewedView.as_view(), name = 'recently_viewed'),

]