from django.contrib import admin

from .models import Post, Profile, User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio')
    list_filter = ('created_at',)

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
