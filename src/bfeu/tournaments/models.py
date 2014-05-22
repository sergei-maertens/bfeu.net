from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tournament(models.Model):
    """
    Model to contain an entire tournament.

    All teams, matches etc. will be linked to a tournament object.
    """
    name = models.CharField(_('name'), max_length=254)
    start = models.DateTimeField(_('start'), null=True, blank=True)
    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'tournament')
        verbose_name_plural = _(u'tournaments')

    def __unicode__(self):
        return self.name


class Team(models.Model):
    tournament = models.ForeignKey(Tournament)
    name = models.CharField(_('name'), max_length=100)
    members = models.TextField(_('members'), help_text=_('Add each member on a new line'))

    class Meta:
        verbose_name = _(u'team')
        verbose_name_plural = _(u'teams')

    def __unicode__(self):
        return self.name


class Match(models.Model):
    """ Matches between two teams. """
    tournament = models.ForeignKey(Tournament)
    team1 = models.ForeignKey(Team, related_name='+')
    team2 = models.ForeignKey(Team, related_name='+')
    map_name = models.CharField(_('map name'), max_length=100, blank=True)
    start = models.DateTimeField(_('start date and time'))

    points_team1 = models.SmallIntegerField(_('points for team 1'), blank=True, null=True)
    points_team2 = models.SmallIntegerField(_('points for team 2'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'match')
        verbose_name_plural = _(u'matches')

    def __unicode__(self):
        return _('{team1} versus {team2}').format(team1=self.team1.name, team2=self.team2.name)

    @property
    def is_played(self):
        """ Determine if the match has been played, based on the points entered """
        return self.points_team1 is not None and self.points_team2 is not None

    @property
    def winner(self):
        if self.points_team2 > self.points_team1:
            return self.team2
        elif self.points_team1 > self.points_team2:
            return self.team1
        return None
