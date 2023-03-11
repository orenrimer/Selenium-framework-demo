from os.path import join, dirname

DIRS = dict(
    ROOT=dirname(__file__),
    TEST=join(dirname(__file__), "test"),
    RESOURCES=join(dirname(__file__), "test", "resources")
)
