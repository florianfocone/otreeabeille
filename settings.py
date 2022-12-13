from os import environ
import os

DEBUG = os.getenv('DEBUG', False) == 'True'  #get rid of debug panel

OTREE_PRODUCTION = 1;
AUTH_LEVEL = 'STUDY'
ADMIN_USERNAME = 'p2ac'
ADMIN_PASSWORD = 'p2ac'
DEMO_PAGE_INTRO_HTML = 'test'

SECRET_KEY = '1785114498942'
INSTALLED_APPS = ['otree']


SESSION_CONFIGS = [
        dict(
         name='Abeille',
         app_sequence=['intro','TestFF', 'payment_info'],
         num_demo_participants=4 #participant en tout
            )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'fr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    dict(
        name='Abeille',
        display_name='Abeille',
        participant_label_file='_rooms/label_p.txt',
        use_secure_urls=False  #obligé de passer par les urls spécifique si true sinon false et entre le label http://localhost:8001/room/room_salon_vegetal
    ),
  #  dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]




# info
# admin interface login : p2ac -- mdp : p2ac