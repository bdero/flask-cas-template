from os import environ
import yaml


ENVIRONMENT_PREFIX = 'APP'
FLATFILE_CONFIG = {}

def resolve_setting(key, default=None):
    return FLATFILE_CONFIG.get(
        key.lower(),
        environ.get(
            '{0}_{1}'.format(ENVIRONMENT_PREFIX, key.upper()),
            default
        )
    )

def load_yaml_config(filename):
    contents = None
    try:
        with open(CONFIG_FILENAME) as f:
            contents = yaml.load(f)
    except:
        # Unable to load config, this should be logged.
        pass
    return contents if contents else {}

CONFIG_FILENAME = resolve_setting('CONFIG_FILENAME', 'config.yml')
FLATFILE_CONFIG = load_yaml_config(CONFIG_FILENAME)

#DEBUG = resolve_setting('DEBUG', False)
