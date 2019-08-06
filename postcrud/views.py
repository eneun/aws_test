from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from .models import Post, Scrap

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def postshow(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    scrap = Scrap.objects.filter(user=request.user, post=post) # 추가
    return render(request, 'postshow.html', {'post': post, 'scrap': scrap}) # 추가

def postnew(request):
    return render(request, 'postnew.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
        else:
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'postnew.html', {'form': form})

def scrap(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)
    if not scrapped:
        scrap = Scrap(user = request.user, post = post)
        # scrap.user = request.user
        # scrap.post = post
        scrap.save
        Scrap.objects.create(user=request.user, post=post)
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
