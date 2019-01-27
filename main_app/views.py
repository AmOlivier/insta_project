from django.shortcuts import render, redirect
from profile_app.models import ProfileInfo
from main_app.models import NewPost, Comment
from django.contrib.auth.decorators import login_required
from profile_app.forms import FormNewComment
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
def get_all_user_and_last_post(profile_connected_user):
	
	all_users_profile = ProfileInfo.objects.all()
	list_of_informations = []
	
	for user_profile in all_users_profile:
		in_follows = False
		last_post = user_profile.posts.order_by('-date')[:1]
		
		if not last_post:
			continue
		
		if user_profile in profile_connected_user.follows.all():
			in_follows = True
		
		list_of_informations.append({
			'user_profile': user_profile,
			'in_follows': in_follows,
			'last_post':last_post[0],
			})

		

	return list_of_informations

def get_all_post_of_all_follows(profile_connected_user):
	
	all_follows = profile_connected_user.follows.all()
	all_post = NewPost.objects.all().order_by('-date')
	feed_post = []
	for post in all_post:
		if post.user_info in all_follows:
			feed_post.append(post)

	
	return feed_post


@login_required
def discover(request):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user=connected_user)
	informations_of_users = get_all_user_and_last_post(profile_connected_user)

	return render(request, 'discover.html', context={
		'informations_of_users': informations_of_users,
		'logged_in': True,
		'profile_connected_user':profile_connected_user,
		})

@login_required
def feed_page(request):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user=connected_user)
	feed_posts = get_all_post_of_all_follows(profile_connected_user)
	print(feed_posts)

	return render(request, 'feed_page.html', context={
		'feed_posts': feed_posts,
		'logged_in': True,
		'profile_connected_user':profile_connected_user,
		})

@login_required
def write_comment(request, post_id):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user=connected_user)
	comment_form = FormNewComment()

	if request.method == 'POST':

		comment = Comment(
			user_info=profile_connected_user, 
			text=request.POST.get('text'), 
			post_id=post_id
			)

		comment.save()
		
		return redirect('/main_app/feed_page/')
		
	return render(request, 'write_comment.html', context= {
		'comment_form': FormNewComment(),
		'logged_in': True,
		'profile_connected_user': profile_connected_user, 
		})












