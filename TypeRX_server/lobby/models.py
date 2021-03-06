from django.db import models

GAME_STATUS = (
    ('LI', 'Log In'),
    ('L', 'Lobby'),
    ('P', 'Playing'),
    ('O', 'Offline'),

)
# Player
# Identification
#   player_id
# Login
#   username
#   password
# Profile
#   global_rank
#   matches_won
#   type_speed
#   letters_typed
# Game
#   status (Playing, Lobby, Offline)
#   local_rank
# region Player Model


class Player(models.Model):

    # Login fields
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    # Profile fields
    global_rank = models.IntegerField(unique=True)
    matches_won = models.IntegerField(default=0)
    type_speed = models.IntegerField(default=0)
    letters_typed = models.IntegerField(default=0)

    # Game fields
    status = models.CharField(max_length=10, choices=GAME_STATUS)
    local_rank = models.IntegerField(null=True)

    def __str__(self):
        return "{} : {}".format(self.username, self.global_rank)

# endregion
