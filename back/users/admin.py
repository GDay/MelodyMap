from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2' )}
         ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('email', 'name', 'is_superuser')
    search_fields = ('name', 'email')
    ordering = ('id',)
    list_filter = ('name', 'email')
    filter_horizontal = ()
    readonly_fields = ('last_login', 'date_joined',)

admin.site.register(User, UserAdmin)