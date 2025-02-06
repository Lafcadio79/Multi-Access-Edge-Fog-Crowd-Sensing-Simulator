##################################################################################
# Module: main.py
# Description: The main module manages the execution of all simulator's functions 
# 
# Updated on Feb/07/2025
# @authors: Dimitri Belli, Paolo Barsocchi, Antonino Crivello, Michele Girolami, 
#           Davide La Rosa         
# License: GPLv3
# Web: https://github.com/Lafcadio79/Multi-Access-Edge-Fog-Crowd-Sensing-Simulator
##################################################################################
# This program is free software; you can redistribuite it and/or modify it under
# the terms of the GNU/General Pubblic License as published the Free software
# Foundation; either version 3 of the License, or (at your opinion) any later 
# version
##################################################################################

import time
import os

from users import *
from tasks import *
from text_menu import *
from utility import *
from output import *


__author__  = "Dimitri Belli"
__contact__ = "dimitri.belli@isti.cnr.it"
__website__ = "still under construction"
__license__ = "GPL3"


def run():
   # text_menu module
   main_menu()


# execution            
run()
