##################################################################################
# Module: tasks.py
# Description: The module provides definitions for creating and reading of a
#              task list of events files
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

import random as rd
import time

def task_generator(g, n, d, dur, dist, tsl, st, et):
    """
        Generator of tasks

        :param g:     networkx multidigraph
        :param n:     number of tasks to be generated
        :param d:     simulation days
        :param dur:   task duration (in minutes)
        :param dist:  coverage radius (in metres)
        :param tsl:   number of timeslots per task
        :param st:    simulation starting time
        :param et:    simulation ending time
        
        :return:    file made up of records as follows
                    [id_task, latitude, longitude, timestamp, duration, distance, timeslots]
    """

    l = list(g.nodes())
    file = open('./Inputs/Tasks/Tasks.txt', 'w')
    file.write("id_task lat lon timestamp duration distance timeslots\n")
    for i in range(n):
        timestamp = rd.uniform(st, et)
        file.write("{} {} {} {} {} {} {}\n".format(i+1, float(g.nodes[rd.choice(l)]['y']), float(g.nodes[rd.choice(l)]['x']), timestamp, dur, dist, tsl))

    print("Tasks generated:", n)

    file.close()

def read_task_list(path):
   """
       Read data from file
      
      :return:    list of lists made up of tasks (time and space information)
                  [task_id latitude longitude day hour minute second duration distance]
   """

   setup_data = []
   l = []

   with open(path) as f:
      setup_data = f.readlines() 
      
   for k in range(1, len(setup_data)):
      sd = setup_data[k].split()
      l.append([int(sd[0]), float(sd[1]), float(sd[2]), float(sd[3]), int(sd[4]), int(sd[5]), int(sd[6])])
      
   return l
   
