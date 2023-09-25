from app import wifi
from app.board import print_pins
from app.util import get_env

debug_mode = get_env("DEBUG", True, bool)
if debug_mode:
    print_pins()
    print("=" * 40)
    wifi.info()

should_scan = get_env("WIFI_SCAN", False, bool)
if should_scan:
    wifi.scan()

wifi.connect()
