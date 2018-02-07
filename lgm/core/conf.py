from .utils.settings import Settings

MIN_PLAYERS = 1
MAX_PLAYERS = 16

MIN_NAME_LEN = 1
MAX_NAME_LEN = 16

MIN_GAME_TIME = 1
MAX_GAME_TIME = 30

MIN_DEATH_TIME = 1
MAX_DEATH_TIME = 30

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
