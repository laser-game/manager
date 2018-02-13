from .utils.settings import Settings

MIN_PLAYERS = 1
MAX_PLAYERS = 16

MIN_NAME_LEN = 1
MAX_NAME_LEN = 16

MIN_GAME_DURATION = 1 * 60
MAX_GAME_DURATION = 30 * 60

MIN_DEATH_DURATION = 1
MAX_DEATH_DURATION = 30

MIN_SHOTS_IN_BATCH = 1
MAX_SHOTS_IN_BATCH = 30

MIN_FN = 0
MAX_FN = 3

MAX_EVENTS = 16

DEFAULT_TEAM_NAMES = (
    'Red team',
    'Orange team',
    'Yellow team',
    'Green team',
    'Aqua team',
    'Blue team',
    'Purple team',
    'Pink team'
)

DEFAULT_COLORS = (
    {
        'index': 0,
        'name': 'black',
        'css': '#000000',
        'hw': '#000000',
    },
    {
        'index': 1,
        'name': 'red',
        'css': '#FF0000',
        'hw': '#FF0000',
    },
    {
        'index': 2,
        'name': 'orange',
        'css': '#FFA500',
        'hw': '#FFA500',
    },
    {
        'index': 3,
        'name': 'yellow',
        'css': '#FFFF00',
        'hw': '#FFFF00',
    },
    {
        'index': 4,
        'name': 'green',
        'css': '#00FF00',
        'hw': '#00FF00',
    },
    {
        'index': 5,
        'name': 'aqua',
        'css': '#00FFFF',
        'hw': '#00FFFF',
    },
    {
        'index': 6,
        'name': 'blue',
        'css': '#0000FF',
        'hw': '#0000FF',
    },
    {
        'index': 7,
        'name': 'purple',
        'css': '#FF00FF',
        'hw': '#FF00FF',
    },
    {
        'index': 8,
        'name': 'pink',
        'css': '#FFC0CB',
        'hw': '#FFC0CB',
    },
)

COLOR = (
    '#000000',  # black
    '#FF0000',  # red
    '#FFA500',  # orange
    '#FFFF00',  # yellow
    '#00FF00',  # green
    '#00FFFF',  # aqua
    '#0000FF',  # blue
    '#FF00FF',  # purple
    '#FFC0CB',  # pink
)

# bodování hry
SCORE_KILL_OPPONENTS = 100
SCORE_KILL_PLAYMATE = -50

core_settings = Settings(__name__, 'CORE')
