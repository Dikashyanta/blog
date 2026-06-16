from django.contrib import admin
from .models import category, Blog, comment

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'is_featured', 'created_at', 'category') 
    search_fields = ('title', 'author__username','id', 'category__category_name', 'status')
    list_editable = ('status', 'is_featured') 
    


# Register your models here.
admin.site.register(category)

admin.site.register(Blog, blogAdmin)

admin.site.register(comment)

