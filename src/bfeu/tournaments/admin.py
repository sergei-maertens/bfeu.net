from django.contrib import admin
from .models import Tournament, Team, Match


class InlineTeam(admin.TabularInline):
    model = Team
    extra = 1


class MatchInline(admin.TabularInline):
    model = Match
    fields = ('team1', 'points_team1', 'points_team2', 'team2', 'map_name', 'start',)


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')
    list_editable = ('start', 'end')

    inlines = [InlineTeam, MatchInline]


admin.site.register(Tournament, TournamentAdmin)
