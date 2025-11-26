from django.shortcuts import render
from django.contrib.urlresolvers import reverse_lazy
# Create your views here.

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin
from . import models
from . import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
  model = models.Post
  select_group = ('user', 'group')

class UserPost(generic.ListVIew):
  model = model.Post
  template_name = 'posts/user_post_list.html'

  def get_queryset(self):
    try:
      self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
    except User.DoesNotExist:
      raise Http404
    else:
      return self.post_user.post.all()
    
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    const['post_user'] = self.post_user
    return context
