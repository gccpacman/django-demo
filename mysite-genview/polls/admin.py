from django.contrib import admin
from .models import Question, Choice

# Register your models here.


#class ChoiceInline(admin.StackedInline):
    #model = Choice
    #extra = 3
   
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date infomation', {'fields':['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]
    #fieldsets = [(None, {'fields':['question_text']}), ('Date infomation', {'fields':['pub_date'], 'classes':['collapse']}),]
    #fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']

# admin.site.register(Choice)
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin) 


