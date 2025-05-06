from django.shortcuts import render,get_object_or_404
from.models import Post

# Create your views here.
def post_list_view(request):
    posts=Post.objects.order_by('date')
    return render(request,'Blog/post.html',{'post':posts})
def post_details(request):
    post_detail=get_object_or_404(Post,pk=Post.pk)
    return render(request,'Blog/details.html',{'post_detail':post_detail})