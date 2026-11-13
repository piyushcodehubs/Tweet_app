from django.contrib import admin
from .models import Tweet
# Register your models here.

@admin.register(Tweet)
class User_Tweet(admin.ModelAdmin):
  list_display = ('id','user','text','photo','created_at','updated_at')
  list_filter = ('created_at', 'updated_at')
  ordering = ('-created_at',)
  search_fields = ('user__username', 'text')
  