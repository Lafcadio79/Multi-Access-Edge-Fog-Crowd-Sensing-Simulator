##################################################################################
# Module: utility.py
# Description: The module provides utility functions for configuration, computing, 
#              writing and reading to and from file, and simulation data saving
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
import sys
import pip
import shutil

from haversine import haversine as hv
from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
from tqdm import tqdm
from users import *
from tasks import *


#################################################
#                Main MCS procedures            #
#################################################
   
def candidates_for_task_timeslots(t, ul):
   """
      Compute the candidates for each timeslot
      
      :param t:      list, a task deployed into the territory
      :param ul:     user movements list of events
      
      :return:       list of the number of users involved in each timeslot of the task
   """
   
   lt = []
   ls = []
   
   ts = t[4] / t[6] * 60
   
   # time
   for i in ul:
      if(i[3] >= t[3] and i[3] <= (t[3] + ts)):
            lt.append(i)
            
   # space
   for j in lt:
      t1 = (t[1], t[2])
      t2 = (j[1], j[2])
      distance = hv(t1, t2, 'm')
      # distance factor of user-i for task-j
      dMax = 1 - (distance / t[5])
      if(distance >= 0):
         ls.append(j)
   
   return ls
   
def candidates_for_task(path_users, path_tasks):
   """
       Compute the candidates for each task
      
      :return:       dictionary made up of {task_id : [candidates per each timeslot]}
   """

   tt = {}

   ulist = read_user_movements_list_events(path_users)
   tlist = read_task_list(path_tasks)
   
   print("\nComputing task candidates")
   for i in tqdm(range(len(tlist))):
      cand = candidates_for_task_timeslots(tlist[i], ulist)
      tt[tlist[i][0]] = cand
      
   return tt

#################################################
#            Main MEC-MCS procedures            #
#################################################

#################################################
#            Main FOG-MCS procedures            #
#################################################



def cls():
   """
      Clean screen
   """
   plt = sys.platform.lower()
   if(plt == 'win32'):
      os.system('cls')
   else:
      os.system('clear')
      
def read_parameters(filename):
   """
      Read data from file
      :param filename:     name of the file to be read
      
      :return:             list of simulation parameters
                           [days, users, number of tasks, communication radius, task duration]
   """
   
   setup_data = read_setup_data(filename)
   
   days    = int(setup_data[7][23:])    # simulation days
   users   = int(setup_data[10][23:])   # number of users
   locom   = int(setup_data[11][23:])   # mean of locomotion
   num_t   = int(setup_data[13][23:])   # number of tasks
   dist    = int(setup_data[14][23:])   # coverage radius of the task (in metres)
   dur_tsk = int(setup_data[15][23:])   # task duration (in minutes)
   dur_tsl = int(setup_data[16][23:])   # timeslot duration
   plt     = int(setup_data[22][23:])   # platform

   return [days, users, locom, num_t, dist, dur_tsk, dur_tsl, plt]

   
def replace(file_path, pattern, subst):
   """
       Replace a line in a file
      
      :return:       file modified
   """
   #Create temp file
   fh, abs_path = mkstemp()
   with fdopen(fh,'w') as new_file:
      with open(file_path) as old_file:
         for line in old_file:
            new_file.write(line.replace(pattern, subst))
   #Remove original file
   remove(file_path)
   #Move new file
   move(abs_path, file_path)
   
def file_copy(orig, dest):
   """
       Copy all files from one directory to one another
      
      :return:       copied files
   """

   for root, dirs, files in os.walk(orig):  
      for file in files:
         path_file = os.path.join(root, file)
         shutil.copy(path_file, dest)

def read_setup_data(f):
   """
       Read all lines of a file
       
       :param f:     filename
       
      :return:       list of strings
   """
   sd = []
   
   with open(f) as fl:
      sd = fl.readlines()
   
   return sd

def import_or_install(p):
   """
       Check if all auxiliary modules are already installed,
       if not, it provides to install them
       
       :param p:     list of packages
       
      :return:       copied files
   """
      
   for i in p:
      try:
         __import__(p)
      except ImportError:
         pip.main(['install', p])
