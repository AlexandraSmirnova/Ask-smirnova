from django.contrib import admin

# Register your models here.


from .models import Question
from .models import Profile
from .models import Answer
from .models import Tag
#from .models import Like
from .models import VoteForPosts

admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Tag)
#admin.site.register(Like)
admin.site.register(VoteForPosts)
