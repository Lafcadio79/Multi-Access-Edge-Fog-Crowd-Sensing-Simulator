##################################################################################
# Module: text_menu.py
# Description: The module manages the user's communication interface through a  
#              series of command line menus (text)
# 
# Updated on Feb/07/2025
# @authors: Dimitri Belli, Paolo Barsocchi, Antonino Crivello, Michele Girolami, 
#           Davide La Rosa          
# @License: GPLv3
# Web: https://github.com/Lafcadio79/Multi-Access-Edge-Fog-Crowd-Sensing-Simulator
##################################################################################
# This program is free software; you can redistribuite it and/or modify it under
# the terms of the GNU/General Pubblic License as published the Free software
# Foundation; either version 3 of the License, or (at your opinion) any later 
# version
##################################################################################

import os
import sys
import shutil

from exec_menu import *
from utility import *


def main_menu():
   cls()

   while(True):
      try:
         print("Main menu:\n")
   
         memo_parameters()
   
         print("-------------------------------")
         print("1. Run a saved simulation")
         print("2. Create a new list of events")
         print("3. Delete saved simulations")
         print("4. Change simulation parameters")
         print("5. Exit without prompt")
   
         choice = int(input(" >> "))
         execution_main_menu(choice)
         break
      except:
         cls()
         
   
def change_parameters_menu():
   """
      Option 4. of the main menu, it allows to change parameters as days, users, tasks, platform of the Setup.txt file      
   """

   cls()

   while(True):
      try:
         print("Change parameters menu:\n")

         memo_parameters()
         print("-------------------------------")
         print("1. Days")
         print("2. Number of users")
         print("3. Number of tasks")
         print("4. Data transimission range")         
         print("5. Type of platform")
         print("6. Back to main menu")
   
         choice = int(input(" >> "))
         execution_change_parameters_menu(choice)
         break
      except:
         cls()
         
def execution_main_menu(c):
   """
      Manage the main menu options      
   """

   if(c in [1,2,3,4,5]):
      options1[c]()
   else:
      main_menu()
   
def execution_change_parameters_menu(c):
   """
      Manage the change parameters menu options      
   """

   if(c in [1,2,3,4,5]):
      options2[c]()
      change_parameters_menu()
   elif(c == 6):
      main_menu()
   else:
      change_parameters_menu()
      
# main menu options   
options1 = {1 : run_a_saved_simulation, 2 : create_a_new_list_of_events, 3: delete_saved_simulations, 4: change_parameters_menu, 5: exit_without_prompt}
# change parameters menu options
options2 = {1 : change_number_of_days,2 : change_number_of_users, 3 : change_number_of_tasks, 4 : change_data_transmission_range, 5 : change_platform}
