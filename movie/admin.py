from django.contrib import admin
from .models import Movie


class MovieModelAdmin(admin.ModelAdmin):
    list_display = ["title", "phase",
                    "release_date", "active"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Movie


admin.site.register(Movie, MovieModelAdmin)
