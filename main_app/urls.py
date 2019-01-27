from django.urls import path 
from . import views

app_name = 'main_app'

urlpatterns = [
	path('feed_page/', views.feed_page, name='feed_page'),
	path('discover/', views.discover, name='discover'),
	path('write_comment/<int:post_id>', views.write_comment, name='write_comment'),
]
