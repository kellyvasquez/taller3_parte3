from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'telefono', 'website', 'foto')
	list_display_links = ('pk', 'user',)
	list_editable = ('telefono', 'website', 'foto')
	search_fields = ('user__email', 'user__first_name', 'user__last_name', 'telefono')

	list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

	fieldsets = (
		('Profile', {
			'fields': ('user', 'foto'),
		}),
		('Extra Info', {
			'fields': (('telefono', 'website'), ('biografia')),
		}),
		('Metadata', {
			'fields': ('created', 'modified'),
		}),
	)

	readonly_fields = ('created', 'modified')
#admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)