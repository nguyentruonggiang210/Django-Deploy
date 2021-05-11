from django.test import TestCase
from .models import Post
# Create your tests here.
class BockTest(TestCase):
	def setUp(self):
		Post.objects.create(
			title="Hello title",
			body="Simple love",
			)

	# test xem có title = Giang trong csdl k
	# def test_string_representation(self):
	# 	post = Post(title="GIang")
	# 	self.assertEqual(str(post.title),post.title)

	# test trang blog có trả về code 200 k (code = 200 => chạy được)
	def test_post_list_view(self):
		reponse = self.client.get('/blog/')
		self.assertEqual(reponse.status_code,200)
		self.assertContains(reponse,"First title")
		self.assertTemplateUsed(reponse,"blog/blog.html")

	def test_post_detail_view(self):
		reponse = self.client.get('/blog/1/')
		self.assertEqual(reponse.status_code,200)
		self.assertContains(reponse,"First title")
		self.assertTemplateUsed(reponse,"blog/post.html")

