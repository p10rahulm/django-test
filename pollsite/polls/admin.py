from django.contrib import admin

from .models import Question,Choice

# You can either use TabularInline or StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Decide what is to be displayed when questions are shown in a list
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Give users option to filter
    list_filter = ['pub_date']

    # Add search field
    search_fields = ['question_text']

    # Make the choice set for the question within the admin module for question itself
    inlines = [ChoiceInline]

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]



admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)