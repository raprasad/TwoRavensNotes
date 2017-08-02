from os.path import dirname, isdir, isfile, join, realpath
import json

CURRENT_DIR = dirname(realpath(__file__))

INPUT_DIR = join(CURRENT_DIR, 'input')
OUTPUT_DIR = join(CURRENT_DIR, 'output')

R_DEV_SERVER_BASE = 'http://0.0.0.0:8000/custom/'

URL_ZELIG_APP = R_DEV_SERVER_BASE + 'zeligapp'

try:
    from local_settings import *
except:
    pass


def get_input_file(fname):

    return get_file_contents(fname)

def get_file_contents(fname, input_dir=True):

    if input_dir:
        fpath = join(INPUT_DIR, fname)
    else:
        fpath = join(OUTPUT_DIR, fname)

    if not isfile(fpath):
        print ('file not found: %s' % fpath)
        return None

    return open(fpath, 'r').read()


def get_file_contents_as_json(fname, input_dir=True):

    content = get_file_contents(fname, input_dir)

    return json.loads(content)
