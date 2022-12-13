from otree.api import *


class Constants(BaseConstants):  # des constantes https://otree.readthedocs.io/en/master/models.html#constants
    name_in_url = 'intro'
    num_rounds = 1;
    players_per_group = 2  # participant par groupe



# https://otree.readthedocs.io/en/latest/rounds.html

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):  # group model pour quand les résultats impactent le groupe
  pass


class Player(BasePlayer):  # player model
 pass



def creating_session(subsession):
   pass


# PAGES


class pintro(Page):
    form_model = 'player'



page_sequence = [pintro]
