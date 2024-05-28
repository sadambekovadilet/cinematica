from django.contrib import admin

from cinematica.models import *


admin.site.register(Movie)
admin.site.register(Janr)
admin.site.register(Author)
admin.site.register(ReviewToMovie)
admin.site.register(View)
