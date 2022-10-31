from django.db import models
from api.players.models import *

# Create your models here.
class Season(models.Model):
    season = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return self.season

class TournamentType(models.Model):
    name = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return self.name

class Tournament(models.Model):
    tmt_name = models.CharField(
        max_length = 50
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    added_field = models.DateTimeField(
        auto_now_add = True
    )
    type = models.ForeignKey(
        TournamentType,
        on_delete=models.CASCADE
    )
    max_players = models.IntegerField()

    def __str__(self):
        return str(self.tmt_name) + str(self.season.season)

class Champion(models.Model):
    tmt = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE
    )
    winner = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "tmt_winners"

    )
    runners = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "tmt_finalist"
    )
    score = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return str(self.tmt.tmt_name) + " " + str(self.season.season)


class ScoreBoard(models.Model):
    tmt = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE
    )
    team1 = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "team1"
    )
    team2 = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "team2"
    )
    team1goals = models.IntegerField()
    team2goals = models.IntegerField(default=0)
    result = models.CharField(
        max_length = 50,
        null = True,
        blank = True
    )

    def save(self, *args, **kwargs):
        if self.team1goals > self.team2goals:
            self.result = str(self.team1.team_name) +" "+"wins"
        elif self.team2goals > self.team1goals:
            self.result = str(self.team2.team_name) +" "+"wins"
        else:
            self.result = "draw"

        super(ScoreBoard, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.tmt.tmt_name) + str(self.season.season)


class PlayerRegister(models.Model):
    tmt = models.ForeignKey(
        Tournament,
        on_delete = models.CASCADE
    )
    player = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE
    )
    registration_time = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return str(self.player.team_name) + " " + str(self.tmt.tmt_name) + " "+ str(self.season.season)

    


