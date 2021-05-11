from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	def __init__(self,*args,**kargs):
		self.author = kargs.pop('author',None)
		self.post = kargs.pop('post',None)
		super().__init__(*args,**kargs)

	def save(self,commit=True):
		comment = super().save(commit=False)
		comment.author = self.author
		comment.post = self.post
		comment.save()

	class Meta:
		model = Comment
		fields = ["body"]

