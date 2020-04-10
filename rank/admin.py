from django.contrib import admin
from .models import Rank


class RankModelAdmin(admin.ModelAdmin):
    list_display = ["user", "movie", "number", "slug"]


admin.site.register(Rank, RankModelAdmin)
