from django.shortcuts import render, redirect
from profile_app.models import ProfileInfo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from profile_app.forms import FormNewPost, UserEditForm, ProfileEditForm 
from main_app.models import NewPost


# Create your views here.

@login_required
def profile_page(request, profile_id):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user=connected_user)
	user_profile = ProfileInfo.objects.get(id=profile_id)
	
	check_own_profile = False
	
	if profile_id == profile_connected_user.id: #est ce que le profile que je veux voir est le mien ?
		check_own_profile = True

	return render(request, 'profile_page.html', 
		{
		'check_own_profile': check_own_profile,
		'user_profile': user_profile,
		'logged_in':True, 
		'user': request.user,
		'profile_connected_user': profile_connected_user
		})

@login_required
def edit_profile(request):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user=connected_user)

	if request.method == 'POST':
		profile_connected_user.user.first_name = request.POST.get('first_name')
		profile_connected_user.user.last_name = request.POST.get('last_name')
		profile_connected_user.bio = request.POST.get('bio')
		profile_connected_user.facebook_link = request.POST.get('facebook_link')
		
		if 'profile_pic' in request.FILES:
			profile_connected_user.profile_pic = request.FILES['profile_pic']
	
		profile_connected_user.user.save()
		profile_connected_user.save()

	user_edit_form = UserEditForm(initial={
	'first_name': profile_connected_user.user.first_name,
	'last_name': profile_connected_user.user.last_name,
	})

	profile_edit_form = ProfileEditForm(initial={
	'bio': profile_connected_user.bio,
	'facebook_link': profile_connected_user.facebook_link,
	'profile_pic': profile_connected_user.profile_pic.url,
	})

	return render(request, 'edit_profile.html', context={
	'user_edit_form': user_edit_form,
	'profile_edit_form': profile_edit_form,
	'profile_connected_user': profile_connected_user,
	'logged_in': True,
	})

@login_required
def write_new_post(request):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user= connected_user)

	if request.method=='POST':
		
		description = request.POST.get('description')
		
		if 'picture' in request.FILES:
			picture = request.FILES['picture']
		
		new_post = NewPost(user_info=profile_connected_user, description=description, picture=picture)

		new_post.save()
			
		return redirect('/main_app/feed_page/', permanent=False)

	else: 
		new_post_form = FormNewPost()


	return render(request, 'write_new_post.html', context={
		'new_post_form': FormNewPost(),
		'logged_in':True,
		'profile_connected_user': profile_connected_user,
		})




@login_required
def follow_user(request, username):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user= connected_user)
	user_to_follow = ProfileInfo.objects.get(user__username= username)
	profile_connected_user.follows.add(user_to_follow)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow_user(request, username):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user= connected_user)
	user_to_unfollow = ProfileInfo.objects.get(user__username= username)
	profile_connected_user.follows.remove(user_to_unfollow)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def like_post(request, post_id):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user= connected_user)
	post_to_like = NewPost.objects.get(id = post_id)
	post_to_like.liked_by.add(profile_connected_user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def dislike_post(request, post_id):
	connected_user = request.user
	profile_connected_user = ProfileInfo.objects.get(user= connected_user)
	post_to_like = NewPost.objects.get(id = post_id)
	post_to_like.liked_by.remove(profile_connected_user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

