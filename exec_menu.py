##################################################################################
# Module: exec_menu.py
# Description: The module manages the user's communication interface through a  
#              series of command line menus (execution)
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

from output import *
from utility import *
from users import *
from tasks import *


#################################################
#                   Main Menu                   #
#################################################

def run_a_saved_simulation():
   """
      Option 1. of the main menu, it allows to run a saved simulation through a dynamic sub-menu 
   """
   cls()
   
   lst = []
   opt = []
   todel = {}
   counter = 1
   print("Existing simulations list:\n\n")
   
   for root, dirs, files in os.walk("./saved", topdown=False):
      for names in dirs:
         lst.append(names)
         
   lst = list(set(lst))
   lst = [x for x in lst if x not in ['Users', 'Tasks', 'Outputs']]
   
   print("-------------------------------")
   for i in lst:
      s = i.split("_")
      todel[counter] = "{}_{}_{}_{}_{}".format(s[0], s[1], s[2], s[3], s[4])
      print("{}. City: {}, Users: {}, Tasks: {}, Days: {}, Platform: {}".format(counter, s[0], s[1], s[2], s[3], s[4]))
      counter = counter + 1
      
   print("{}. Back to the main menu".format(counter))

   choice = int(input(" >> "))

   opt = [x for x in range(1, counter)]
   
   if(choice in opt):
      folder = todel[choice]
      print("Processing data . . .")
      output_candidates_for_task("./saved/{}/Users".format(folder), "./saved/{}/Tasks/Tasks.txt".format(folder), "./saved/{}/Outputs/tasks_with_candidates.txt".format(folder))
   else:
      main_menu()
      
def create_a_new_list_of_events():
   """
      Option 2. of the main menu, it runs a new simulation creating all necessary files      
   """

   # all possible network types: ‘walk’, ‘bike’, ‘drive’, ‘drive_service’, ‘all’, ‘all_private’, ‘none’
   nt = ['walk', 'bike', 'drive', 'all']

   filename = "Setup.txt"
   end_time = time.time()
   param = read_parameters(filename)
   starting_time = end_time - 60 *60 *24 * int(param[0])

   cls()
   
   while(True):
      try:
         city = input("Insert the name of the city: ")
         print("Download the map of {} . . .".format(city))
         G = ox.graph_from_place(city, network_type='walk')
         break
      except:
         print("Wrong city name!")
         continue
      else:
         break      
   list_of_events_generator(G, param[1], param[0], param[2], starting_time, end_time)
   task_generator(G, param[3], param[0], param[5], param[4], param[6], starting_time, end_time)
   
   
   s = input("Do you want to save the data?[y/n] ")
   
   while(True):
      s = s.lower()
      if(s != 'y' and s != 'n'):
         print("Wrong selection, please insert [y/n]")
      else:
         if(s == 'y'):
            plt = param[7]
   
            if(plt == 1):
               plat = "MCS"
            elif(plt == 2):
               plat = "FOG-MCS"
            else:
               plat = "MEC-MCS"
            # output module
            save_simulation_data(city, param[1], param[3], param[0], plat)
            break
         else:
            # output module
            output_candidates_for_task('./Inputs/Mobility/Users', './Inputs/Tasks/Tasks.txt', "Outputs/tasks_with_candidates.txt")
            break
            

   
   # remove all the temporary files generated
   shutil.rmtree('./Inputs/Mobility/Users/', ignore_errors=True)
   os.makedirs('./Inputs/Mobility/Users/')
   shutil.rmtree('./Inputs/Tasks/', ignore_errors=True)
   os.makedirs('./Inputs/Tasks/')
   shutil.rmtree('./Outputs/', ignore_errors=True)
   os.makedirs('./Outputs/')
   
def delete_saved_simulations():
   """
      Option 3. of the main menu, it allows to delete saved simulations through a dynamic sub-menu 
   """
   cls()
   
   lst = []
   opt = []
   todel = {}
   counter = 1
   print("Saved simulations list:\n\n")
   
   for root, dirs, files in os.walk("./saved", topdown=False):
      for names in dirs:
         lst.append(names)
         
   lst = list(set(lst))
   lst = [x for x in lst if x not in ['Users', 'Tasks', 'Outputs']]
   
   print("-------------------------------")
   for i in lst:
      s = i.split("_")
      todel[counter] = "{}_{}_{}_{}_{}".format(s[0], s[1], s[2], s[3], s[4])
      print("{}. City: {}, Users: {}, Tasks: {}, Days: {}, Platform: {}".format(counter, s[0], s[1], s[2], s[3], s[4]))
      counter = counter + 1
      
   print("{}. Back to the main menu".format(counter))

   choice = int(input(" >> "))

   opt = [x for x in range(1, counter)]

   if(choice in opt):
      shutil.rmtree('./saved/{}'.format(todel[choice]), ignore_errors=True)
   
   main_menu()

   
def exit_without_prompt():
   print("No other action required ... ")

#################################################
#             Change Parameters Menu            #
#################################################

def change_number_of_days():
   """
      Option 1. of the change parameters menu, it allows to modify the number of days   
   """

   cls()

   setup_data = read_setup_data("Setup.txt")
   
   while(True):
      try:
         days = int(input("How many days? "))
         break
      except:
         print("Wrong input!")
         
   replace("Setup.txt", setup_data[7], "|Days of simulation| = {}\n".format(days))

def change_number_of_users():
   """
      Option 2. of the change parameters menu, it allows to modify the number of users   
   """

   cls()

   setup_data = read_setup_data("Setup.txt")
   
   while(True):
      try:
         users = int(input("How many users? "))
         break
      except:
         print("Wrong input!")
         
   replace("Setup.txt", setup_data[10], "|Number of users|    = {}\n".format(users))
   
def change_number_of_tasks():
   """
      Option 3. of the change parameters menu, it allows to modify the number of tasks   
   """

   cls()

   setup_data = read_setup_data("Setup.txt")
   
   while(True):
      try:
         tasks = int(input("How many tasks? "))
         break
      except:
         print("Wrong input!")
         
   replace("Setup.txt", setup_data[13], "|Number of tasks|    = {}\n".format(tasks))

def change_data_transmission_range():
   """
      Option 4. of the change parameters menu, it allows to modify the data transmission range   
   """

   cls()

   setup_data = read_setup_data("Setup.txt")
   
   while(True):
      try:
         range = int(input("How many meters? "))
         break
      except:
         print("Wrong input!")
         
   replace("Setup.txt", setup_data[14], "|Range of execution| = {}\n".format(range))
   
def change_platform():
   """
      Option 5. of the change parameters menu, it allows to modify the type of platform   
   """

   cls()

   setup_data = read_setup_data("Setup.txt")
   
   while(True):
      try:
         sim = int(input("Choose the platform:\n1) MCS \n2) FOG-MCS \n3) MEC-MCS\n >> "))
         break
      except:
         print("Wrong input!")

   replace("Setup.txt", setup_data[22], "|Type of platform|   = {}\n".format(sim))
   
def memo_parameters():
   """
      Print information about settings (days, users, tasks, platform) on the upper side of each menu
   """
   plat = ""
   
   param = read_parameters("Setup.txt")
   
   plt = param[7]
   
   if(plt == 1):
      plat = "MCS"
   elif(plt == 2):
      plat = "FOG-MCS"
   else:
      plat = "MEC-MCS"
   
   print("Days:     ", param[0])
   print("Users:    ", param[1])
   print("Tasks:    ", param[3])
   print("Range:    ", param[4])
   print("Platform: ", plat)
