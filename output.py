##################################################################################
# Module: output.py
# Description: The module provides definitions to manage the simulator's input/ 
#              output
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

import os

from utility import *


def save_simulation_data(cn, u, t, d, p):
   """
      Save generated data in a separate folder named as the selected city, the number of users and tasks
      :param cn:        city name
      :param u:         number of users
      :param t:         number of tasks
      :param d:         number of days
      :param p:         type of platform
      
      :return:          a copy of all simulation files in a new folder
   """
   plat = ""
   
   # utility module
   param = read_parameters("Setup.txt")
   
   plt = param[7]
   
   if(plt == 1):
      plat = "MCS"
   elif(plt == 2):
      plat = "FOG-MCS"
   else:
      plat = "MEC-MCS"

   output_candidates_for_task('./Inputs/Mobility/Users', './Inputs/Tasks/Tasks.txt', "Outputs/tasks_with_candidates.txt")
   
   os.makedirs("./saved/{}_{}_{}_{}_{}/Users".format(cn,u,t,d,p), exist_ok=True)
   os.makedirs("./saved/{}_{}_{}_{}_{}/Tasks".format(cn,u,t,d,p), exist_ok=True)
   os.makedirs("./saved/{}_{}_{}_{}_{}/Outputs".format(cn,u,t,d,p), exist_ok=True)

   file_copy("./Inputs/Mobility/Users", "./saved/{}_{}_{}_{}_{}/Users".format(cn,u,t,d,p))
   file_copy("./Inputs/Tasks", "./saved/{}_{}_{}_{}_{}/Tasks".format(cn,u,t,d,p))
   file_copy("./Outputs", "./saved/{}_{}_{}_{}_{}/Outputs".format(cn,u,t,d,p))
   
def output_candidates_for_task(path_users, path_tasks, destination):
   """   
      Compute the number of candidates for each single task
      
      :return:       file made up of records [task_id number_of_candidates]
   """
   
   # utility module
   c = candidates_for_task(path_users, path_tasks)
   key = list(c.keys())

   file = open(destination, 'w')
   file.write("task_id candidates\n")

   for i in key:
      if(i >= 10):
         file.write("{} {}\n".format(i, len(c[i])))
      else:
         file.write("{}  {}\n".format(i, len(c[i])))
   
   # print before termination
   for i in key:
      if(i >= 10):
         print("{} {}".format(i, len(c[i])))
      else:
         print("{}  {}".format(i, len(c[i])))
      
   file.close()
