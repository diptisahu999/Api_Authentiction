from django.contrib import admin
from api.models import User,Electric_Product,Home_Kitchen_Product,Role
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserModelAdmin(BaseUserAdmin):
   
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'id','password', 'tc','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credencials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','tc')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','tc', 'password', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Electric_Product)
admin.site.register(Home_Kitchen_Product)
admin.site.register(Role)
