from django.shortcuts import render, redirect
from ExtendsUserModel.models import User
from Thoughts.models import Post, Comment
from .forms import PostForm, CommentForm

from django.shortcuts import get_object_or_404, get_list_or_404, resolve_url
from django.urls import reverse

def profile(request, pk):
    posts = Post.objects.filter(connected_to = get_object_or_404(User, username=pk))
    friends = [fr for fr in User.objects.all() if fr in request.user.friends.all()]
    req_to = [req for req in User.objects.all() if req in request.user.friend_requests_to.all()]
    req_from = [req for req in User.objects.all() if req in request.user.friend_requests_from.all()]
    return render(request, 'profile.html', {
        'title':get_object_or_404(User, username=pk).first_name + ' ' + get_object_or_404(User, username=pk).last_name + ' (' + get_object_or_404(User, username=pk).username + ')' if (get_object_or_404(User, username=pk).first_name and get_object_or_404(User, username=pk).last_name) else 'Profile', 
        'login_user':request.user, 
        'now_at_user':get_object_or_404(User, username=pk), 
        'posts':posts,
        'friends':friends,
        'req_to':req_to,
        'req_from':req_from,
        })        


def add_comment(request, pk_user, pk_post):
    user = get_object_or_404(User, pk=pk_user)
    post = get_object_or_404(Post, pk=pk_post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(
                connected_to_post = post,
                connected_to = user,
                text = form.cleaned_data.get('text'),
            )
            new_comment.save()
            post.comments.add(new_comment)
            return redirect('{}#posts'.format(reverse('profile', kwargs={'pk':post.connected_to.username})))
            

def my_profile_redirect(request):
    return redirect('profile', request.user.username)

def edit(request):
    if request.method=='POST':
        return redirect('my_profile_redirect')
    return redirect('my_profile_redirect')