from django.urls import path
from . import views
from django.views.generic import ListView,DetailView
from .models import Post

# đặt tên để tranh hashcode url
urlpatterns = [
	# path("",views.List_post,name="blog"),
	# path("",views.PostListView.as_view(),name="blog"),
	path("",views.PostListView.as_view(
		queryset = Post.objects.all().order_by("-date"),
		template_name = "blog/blog.html",
		context_object_name = "Post",
		paginate_by = 1),name="blog"),

	# path("<int:id>/", views.PostDetail ,name="post"),
	# path("<int:pk>/", views.PostDetailView.as_view() ,name="post"),
	path("<int:pk>/", views.post ,name="post"),
]
