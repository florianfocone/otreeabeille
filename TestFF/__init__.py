from otree.api import *


class Constants(BaseConstants):  # des constantes https://otree.readthedocs.io/en/master/models.html#constants
    name_in_url = 'TestFF'
    num_rounds=5;
    players_per_group = 2  # participant par groupe
    payoff_both_defect = 10000;
    payoff_high = 30000;
    payoff_low = 0;
    payoff_both_cooperate = 20000;

# https://otree.readthedocs.io/en/latest/rounds.html

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):  # group model pour quand les résultats impactent le groupe
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):  # player model

    defect1 = models.BooleanField(
        label='Une seule réponse possible.',
        choices=[[True, 'Garder les 10000€'], [False, 'Donner les 10000€']],
        widget=widgets.RadioSelect,
        blank=False,
        initial=None
    )

    # FUNCTIONS
def resultatcoop(group):
        player_Lists = group.get_players()
        player1 = player_Lists[0]
        player2 = player_Lists[1]
        if player1.defect1:
            if player2.defect1:
                player1.payoff = Constants.payoff_both_defect
                player2.payoff = Constants.payoff_both_defect
            else:
                player1.payoff = Constants.payoff_high
                player2.payoff = Constants.payoff_low
        else:
            if player2.defect1:
                player2.payoff = Constants.payoff_high
                player1.payoff = Constants.payoff_low
            else:
                player1.payoff = Constants.payoff_both_cooperate
                player2.payoff = Constants.payoff_both_cooperate

def creating_session(subsession):
    labels = ['bob1', 'alice1', 'bob2','alice2']
    for player, label in zip(subsession.get_players(), labels):
        player.participant.label = label

# PAGES


class pjeu1(Page):
    form_model = 'player'
    form_fields = ['defect1']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = resultatcoop  # condition pour lancer la fonction set_payoffs et passer à la page suivante
    body_text = "Attente des réponses des autres participants avant de continuer."


class presult1(Page):
    form_model = 'player'


page_sequence = [pjeu1, ResultsWaitPage, presult1]
