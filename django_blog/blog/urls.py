from django.views.generic import ListView
from django_blog.blog.models import Post

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            return Post.objects.filter(tags__slug=tag_slug).distinct().order_by('-created_at')
        return Post.objects.all().order_by('-created_at')
