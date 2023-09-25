import board
import microcontroller


def print_pins():
    # SPDX-FileCopyrightText: 2020 anecdata for Adafruit Industries
    # SPDX-FileCopyrightText: 2021 Neradoc for Adafruit Industries
    # SPDX-FileCopyrightText: 2021-2023 Kattni Rembor for Adafruit Industries
    # SPDX-FileCopyrightText: 2023 Dan Halbert for Adafruit Industries
    #
    # SPDX-License-Identifier: MIT
    """CircuitPython Essentials Pin Map Script"""
    board_pins = []
    for pin in dir(microcontroller.pin):
        if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
            pins = []
            for alias in dir(board):
                if getattr(board, alias) is getattr(microcontroller.pin, pin):
                    pins.append(f"board.{alias}")
            # Add the original GPIO name, in parentheses.
            if pins:
                # Only include pins that are in board.
                pins.append(f"({str(pin)})")
                board_pins.append(" ".join(pins))

    if len(board_pins) > 0:
        print("Board pins:")
        for pins in sorted(board_pins):
            print(" ", pins)
    else:
        print("No board pins found!")
