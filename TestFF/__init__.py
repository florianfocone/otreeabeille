from otree.api import *


class Constants(BaseConstants):  # des constantes https://otree.readthedocs.io/en/master/models.html#constants
    name_in_url = 'TestFF'
    num_rounds = 5;
    players_per_group = 2  # participant par groupe
    payoff_both_defect = 50;
    payoff_high = 150;
    payoff_low = 0;
    payoff_both_cooperate = 100;


# https://otree.readthedocs.io/en/latest/rounds.html

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):  # group model pour quand les résultats impactent le groupe
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):  # player model

    pr1 = models.CurrencyField(initial=0)
    pr2 = models.CurrencyField(initial=0)
    pr3 = models.CurrencyField(initial=0)
    pr4 = models.CurrencyField(initial=0)
    pr5 = models.CurrencyField(initial=0)
    Gains = models.CurrencyField(initial=0)

    defect = models.BooleanField(
        label='Une seule réponse possible.',
        choices=[[True, 'Garder les 50€'], [False, 'Donner les 50€']],
        widget=widgets.RadioSelect,
        blank=False,
        initial=None
    )

    pensee = models.StringField(
    choices=[['garde', 'Il garde les 50€'], ['donne', 'Il donne les 50€']],
    label='Une seule réponse possible.',
    widget=widgets.RadioSelect,
    blank=False,
   # initial='garde'
    )

    # FUNCTIONS


def resultatcoop(group):
    player_Lists = group.get_players()
    player1 = player_Lists[0]
    player2 = player_Lists[1]
    if player1.defect:
        if player2.defect:
            player1.payoff = Constants.payoff_both_defect
            player2.payoff = Constants.payoff_both_defect
        else:
            player1.payoff = Constants.payoff_high
            player2.payoff = Constants.payoff_low
    else:
        if player2.defect:
            player2.payoff = Constants.payoff_high
            player1.payoff = Constants.payoff_low
        else:
            player1.payoff = Constants.payoff_both_cooperate
            player2.payoff = Constants.payoff_both_cooperate


    player1.pr1 = player1.in_round(1).payoff
    player2.pr1 = player2.in_round(1).payoff
    player1.pr2 = player1.in_round(2).payoff
    player2.pr2 = player2.in_round(2).payoff
    player1.pr3 = player1.in_round(3).payoff
    player2.pr3 = player2.in_round(3).payoff
    player1.pr4 = player1.in_round(4).payoff
    player2.pr4 = player2.in_round(4).payoff
    player1.pr5 = player1.in_round(5).payoff
    player2.pr5 = player2.in_round(5).payoff
    player1.Gains = player1.in_round(1).payoff + player1.in_round(2).payoff + player1.in_round(3).payoff + player1.in_round(4).payoff + player1.in_round(5).payoff
    player2.Gains = player2.in_round(1).payoff + player2.in_round(2).payoff + player2.in_round(3).payoff + player2.in_round(4).payoff + player2.in_round(5).payoff
    #print (player.Gains)


def creating_session(subsession):
    labels = ['bob1', 'alice1', 'bob2', 'alice2']
    for player, label in zip(subsession.get_players(), labels):
        player.participant.label = label


# PAGES


class pjeu1(Page):
    form_model = 'player'
    form_fields = ['defect','pensee']



class ResultsWaitPage(WaitPage):
    after_all_players_arrive = resultatcoop  # condition pour lancer la fonction set_payoffs et passer à la page suivante
    body_text = "Attente des réponses des autres participants avant de continuer."


class presult1(Page):
    form_model = 'player'


class pfinal(Page):
    form_model = 'player'


page_sequence = [pjeu1, ResultsWaitPage, presult1]
