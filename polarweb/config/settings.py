PAGES = {
    "A1": {
        "width": 450,
        "height": 550,
        "x": 125,
        "y": 150},
    "A4": {
        "width": 450,
        "height": 550,
        "x": 125,
        "y": 150}
}

DEFAULT_PAGE = "A1"

MACHINES = [
    {"name": "left",
     "spec": {
        "width": 725,
        "height": 980,
        "comm_port": "COM8",
        "baud_rate": 57600,
        "default_page": "A1"}
    }
    # ,
    # {"name": "right",
    #  "spec": {
    #     "width": 725,
    #     "height": 980,
    #     "comm_port": "COM39",
    #     "baud_rate": 57600,
    #     "default_page": "A1"}
    # }
]

ARTWORK_ACQUIRE_METHOD = {
    "method_name": "acquire_face_track",
    "module": "polarweb.models.acquire"
}

CAMERA_NUM = 0

# Values are 'none' or 'rotate cw'
CAMERA_ORIENTATION = 'rotate cw'

# Camera will ignore faces below this size
MIN_FACE_SIZE = 100

# Face must stay in the same place for this many cycles before a lock happens.
FACE_LOCK_VALUE = 15

# Some tracing settings
POSTERIZE_LEVELS = 3
MIN_PATH_LENGTH = 20
MAX_PATH_COUNT = 200
PATH_SMOOTHING_LEVELS = 2
BLUR = 4

# Some debugging settings
PATHFINDER_MINIMUM_TIME = 0
SHOW_PATHS_DURING_VIZ = False