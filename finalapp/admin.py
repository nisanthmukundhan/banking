from django.contrib import admin

# Register your models here.
from finalapp.models import District, Branch, Registerr


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(District, DistrictAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Branch, BranchAdmin)


class RegisterrAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Registerr, RegisterrAdmin)
