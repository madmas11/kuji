from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Comment, Favorite


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'is_staff', 'is_active')
    list_display_links = ('username',)
    list_editable = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'text', 'post_date')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Comment, CommentAdmin)