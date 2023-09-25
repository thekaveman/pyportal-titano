# SPDX-FileCopyrightText: 2019 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import board
import busio
from digitalio import DigitalInOut

from app.util import bytes_str, get_env, mac_str


esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

requests.set_socket(socket, esp)


def info():
    """Get information about the wifi co-processor."""
    if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
        print("ESP32 found and in idle mode")
    print("Firmware:", bytes_str(esp.firmware_version))
    print("MAC:", mac_str(esp.MAC_address))


def connect():
    """Connect to a configured Wifi access point.

    WIFI_SSID and WIFI_PASSWORD should be configured in settings.toml.
    """
    print("ESP32 SPI connect")

    ssid = get_env("WIFI_SSID")
    password = get_env("WIFI_PASSWORD")
    assert ssid and password, "Missing wifi credentials in settings.toml"

    print("Connecting to configured AP...")
    count = 0
    while not esp.is_connected:
        try:
            count += 1
            print(f"Connection attempt: {count}")
            esp.connect_AP(ssid, password)
        except OSError as e:
            print("Could not connect, retrying: ", e)
            continue

    assert esp.is_connected, "Connection failed!"

    print("Connected to:", bytes_str(esp.ssid), f"({esp.rssi})")
    print("IP:", esp.pretty_ip(esp.ip_address))
    print("Ping github.com:", f"{esp.ping('github.com')}ms")

    print("Connection successful!")


def scan():
    """Scan for visible APs."""
    print("Scanning for visible APs...")
    for ap in esp.scan_networks():
        ssid, rssi = bytes_str(ap["ssid"]), ap["rssi"]
        print(f"  {ssid} ({rssi})")
