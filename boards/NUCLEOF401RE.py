#!/bin/false
# -*- coding: utf8 -*-
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
# Copyright (C) 2014 Alain Sézille for NucleoF401RE specific lines of this file
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
info = {
  'name' : "NUCLEOF401RE",
  'link' :  [ "http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1847/PF260000#tab-3"],
  'default_console' : "EV_SERIAL2", # USART2 par défaut USART2_TX sur PA2, USART2_RX sur PA3
  'variables' : 5376, # (96-12)*1024/16-1
  'binary_name' : 'espruino_%v_nucleof401re.bin',
};
chip = {
  'part' : "STM32F401RET6",
  'family' : "STM32F4",
  'package' : "LQFP64",
  'ram' : 96, # 0x0001 8000 long, from 0x2000 0000 to 0x2001 7FFF
  'flash' : 512, # 0x0008 0000 long, from 0x0800 0000 to 0x0807 FFFF
  'speed' : 84,
  'usart' : 3,
  'spi' : 4,
  'i2c' : 3,
  'adc' : 1,
  'dac' : 0,
  'saved_code' : {
    # code size 225248 = 0x36FE0 starts at 0x0800 0000 ends at 0x0803 6FE0
    # so we have some left room for Espruino firmware and no risk to clear it while saving
    'address' : 0x08060000, # flash_saved_code_start 0x0806 0000 to 0x807 5000
    # we have enough flash space in this single flash page to save all of the ram
    'page_size' :  131072, # size of pages : on STM32F401, last 2 pages are 128 Kbytes
    # we use the last flash page only, furthermore it persists after a firmware flash of the board
    'page_number' : 7, # number of the flash page we save at (0 based, must be coherent with address)
    'pages' : 1, # count of pages we're using to save RAM to Flash,
    'flash_available' : 512 # binary will have a hole in it, so we just want to test against full size
  },
  'place_text_section' : 0x08010000, # note flash_available above # TODO A VERIFIER
};
# left-right, or top-bottom order
# TODO add Arduino. prefix to the pins concerned in left3 and right3
board = {
  'left' :   [ 'C10', 'C12', 'VDD', 'BOOT0', 'NC', 'NC', 'A13', 'A14', 'A15', 'GND', 'B7', 'C13', 'C14', 'C15', 'H0', 'H1', 'VBAT', 'C2', 'C3'],
  'left2' :  [ 'C11', 'D2', 'E5V', 'GND', 'NC', 'IOREF', 'RESET', '3V3', '5V', 'GND', 'GND', 'VIN', 'NC', 'A0', 'A1', 'A4', 'B0', 'C1', 'C0'],
  'left3' :  [ 'NC', 'IOREF', 'RESET', '3V3', '5V', 'GND', 'GND', 'VIN', 'A0', 'A1', 'A4', 'B0', 'C1', 'C0'],
  'right3' : [ 'B8', 'B9', 'AVDD', 'GND', 'A5', 'A6', 'A7', 'B6','C7','A9','A8','B10','B4','B5','B3','A10','A2','A3'],
  'right2' : [ 'C9', 'B8', 'B9', 'AVDD', 'GND', 'A5', 'A6', 'A7', 'B6','C7','A9','A8','B10','B4','B5','B3','A10','A2','A3'],
  'right' :  [ 'C8', 'C6', 'C5', 'U5V', 'NC', 'A12', 'A11', 'B12', 'NC', 'GND', 'B2', 'B1', 'B15', 'B14', 'B13', 'AGND', 'C4', 'NC', 'NC'],
};
devices = {
  'OSC' : { 'pin_1' : 'H0', # MCO from ST-LINK fixed at 8 Mhz, boards rev MB1136 C-02
            'pin_2' : 'H1' },
  'OSC_RTC' : { 'pin_1' : 'C14', # MB1136 C-02 corresponds to a board configured with on-board 32kHz oscillator
                'pin_2' : 'C15' },
  'LED1' : { 'pin' : 'A5' },
  # TODO make it work with setWatch
  'BTN1' : { 'pin' : 'C13',
             'inverted' : True, # 1 when unpressed, 0 when pressed! (Espruino board is 1 when pressed)
             'pinstate': 'IN_PULLUP', # to specify INPUT, OUPUT PULL_UP PULL_DOWN..
           },
#  'USB' : { 'pin_otg_pwr' : 'C0',
#            'pin_dm' : 'A11',
#            'pin_dp' : 'A12',
#            'pin_vbus' : 'A9',
#            'pin_id' : 'A10', },
};


board_css = """
#board {
  width: 680px;
  height: 1020px;
  left: 200px;
  background-image: url(img/NUCLEOF401RE.jpg);
}
#boardcontainer {
  height: 1020px;
}
#left {
  top: 375px;
  right: 590px;
}
#left2 {
  top: 375px;
  left: 105px;
}

#right  {
  top: 375px;
  left: 550px;
}
#right2  {
  top: 375px;
  right: 145px;
}
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f401.csv', 5, 8, 9)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
