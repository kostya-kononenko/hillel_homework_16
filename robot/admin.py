from django.contrib import admin

from robot.models import Robot_Author, Robot_Quotes


class QuotesInline(admin.StackedInline):
    model = Robot_Quotes
    extra = 1


@admin.register(Robot_Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('text', 'authors')
    list_filter = ['text', 'authors']
    search_fields = ['text', 'authors']


@admin.register(Robot_Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
    list_filter = ['name']
    search_fields = ['name']
    inlines = [QuotesInline]
