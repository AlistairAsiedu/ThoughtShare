from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post


# Create views that handle the CRUD functionality.
def Thoughtshare(request):
    return render(request, 'ThoughtShare/homepage.html', {})


# Welcome page view
def welcome(request):
    name = request.GET['name']
    email = request.GET['email']
    birthday = request.GET['birthday']
    text_data = {
        'name': name,
        'email': email,
        'birthday': birthday,
    }
    return render(request, 'ThoughtShare/welcome.html', context=text_data)


# List of post view
@login_required
def list(request):
    all_post = Post.objects.all()
    return render(request, 'ThoughtShare/post_page.html',
                  {'all_post': all_post})


# View to add post
@permission_required('ThoughtShare.add_post', login_url='list')
def add_post(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        context = request.POST.get('context')
        # Below is the ORM to create a new post in the ThoughtShare table
        Post.objects.create(author=author, title=title, context=context)
        # When done, return to the post_page.html page
        return redirect('list')
    return render(request, 'ThoughtShare/add_post.html')


# View to examine a post
@login_required
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'ThoughtShare/view_post.html', {'post': post})


# View to edit a post
@permission_required('ThoughtShare/edit_post', login_url='list')
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        context = request.POST.get('context')
        # Update the ThoughtShare record
        post.author = author
        post.title = title
        post.context = context
        post.save()
        # Redirect to the view_post page
        return redirect('view_post', post_id=post.id)
    return render(request, 'ThoughtShare/edit_post.html', {'post': post})


# View to delete a post
@permission_required('ThoughtShare/delete_post', login_url='list')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    return render(request, 'ThoughtShare/delete_post.html', {'post': post})
