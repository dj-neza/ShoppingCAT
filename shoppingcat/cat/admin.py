from django.contrib import admin
from .models import MyClothing, Inspiration, Recommendation

# Register your models here.
admin.site.register(MyClothing)
admin.site.register(Inspiration)
admin.site.register(Recommendation)