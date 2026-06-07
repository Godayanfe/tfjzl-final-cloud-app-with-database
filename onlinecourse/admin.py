from django.contrib import admin

# Import all models including the new ones
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline class for Lesson (used inside CourseAdmin)
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Inline class for Choice (used inside QuestionAdmin)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Inline class for Question (used inside CourseAdmin if needed)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# CourseAdmin - manages Course with Lessons inline
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# QuestionAdmin - manages Question with Choices inline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


# LessonAdmin - manages Lesson model
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register all models with the admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
