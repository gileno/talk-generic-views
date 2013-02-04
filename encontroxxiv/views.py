#encoding: utf-8

import random

from django.views.generic import TemplateView, DetailView

from blog.models import Post

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['random_number'] = random.randint(1, 10)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = '_home.html'
        return super(HomeView, self).dispatch(request, *args, **kwargs)

class PostView(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'