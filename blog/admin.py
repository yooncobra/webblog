from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_title_length']
    list_display_links = ['title']
    
    def get_title_length(self, post):
        return len(post.title)

admin.site.register(Post, PostAdmin)

