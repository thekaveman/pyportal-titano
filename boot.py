import supervisor

from app.util import get_env

supervisor.runtime.autoreload = get_env("RELOAD", default=False, cast=bool)
