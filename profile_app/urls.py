from django.urls import path 
from . import views

app_name = 'profile_app'

urlpatterns = [
	path('profile_page/<int:profile_id>', views.profile_page, name='profile_page'),
	path('write_new_post/', views.write_new_post, name='write_new_post'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('follow_user/<username>/', views.follow_user, name='follow_user'),
	path('unfollow_user/<username>/', views.unfollow_user, name='unfollow_user'),
	path('like_post/<int:post_id>/', views.like_post, name='like_post'),
	path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
