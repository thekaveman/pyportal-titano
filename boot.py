import supervisor

from app.util import get_env

auto_reload = get_env("AUTO_RELOAD", default=False, cast=bool)
supervisor.runtime.autoreload = auto_reload

print("Booting up with auto_reload:", auto_reload)
