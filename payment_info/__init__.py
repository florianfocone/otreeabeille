from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = 2  # participant par groupe
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    free_text = models.StringField(
        label='''optionnel''',
        blank=True)

    recevoirinfo = models.BooleanField(blank=True, initial=True)


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['free_text','recevoirinfo']


    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(redemption_code=participant.label or participant.code)


class merci(Page):
    form_model = 'player'

page_sequence = [PaymentInfo,merci]
