from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
# Create your views here.

# def List_post(request):
# 	print(Post.objects.all())
# 	# thêm dấu trừ vào date để sắp xếp ngược lại
# 	data = {
# 		# 'Post':Post.objects.all().order_by("-date"),
# 		'Post':Post.objects.all(),
# 	}
# 	return render(request,"blog/blog.html",data)

# thay List_post bằng class

class PostListView(ListView):
	queryset = Post.objects.all().order_by("-date")
	template_name = "blog/blog.html"
	context_object_name = "Post"
	paginate_by = 1

# def PostDetail(request,id):
# 	post = Post.objects.get(id=id)
# 	data = {
# 		'post':post,
# 	}
# 	return render(request,'blog/post.html',data)

# thay PostDetail bằng class

class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post.html"


def post(request,pk):
	post = get_object_or_404(Post,pk=pk)
	form = CommentForm()
	if(request.method=="POST"):
		form = CommentForm(request.POST,author=request.user,post=post)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(request.path)

	return render(request,'blog/post.html',{'post':post,'form':form})

