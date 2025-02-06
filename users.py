##################################################################################
# Module: users.py
# Description: The module provides definitions for creating and reading of user
#              movements list of events files
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

import networkx as nx
import random as rd
import osmnx as ox
import os.path
import time
import os

from haversine import haversine as hv
from random import randrange as rdg
from tqdm import tqdm

ox.config(log_console=True, use_cache=True)

def walking_time(g, p, min_s, max_s):
    """
        Computing the walking time from point a to point b (in seconds)
        for all user's movements through the haversine distance
        (fair method currently in disuse because it increases the complexity 
        of the user movements list of events generator algorithm from O(n^2) to O(n^3))

        :param g:     networkx multidigraph
        :param p:     networkx shortest path
        :param min_s: walker's minimum speed
        :param max_s: walker's maximum speed

        :return:      dictionary made up of {[(a coordinates), (b coordinates)] : time}
    """

    seconds = {}

    # we assume different speed for each sub-path
    for i in range(1, len(p)):

        speed = rd.uniform(min_s, max_s)
        t1 = (g.nodes[p[i-1]]['y'], g.nodes[p[i-1]]['x'])
        t2 = (g.nodes[p[i]]['y'], g.nodes[p[i]]['x'])
        dist = hv(t1, t2, 'm')
        seconds[dist / speed] = [t1, t2]

    return seconds

def time_update(tm, et):
    """
        Update the simuation timestamp

        :param tm:    current simulation timestamp
        :param et:    elapsed walking time (in seconds)

        :return:      list made up of [new_timestamp, [day, hour, minute, second]]
    """
    nt = tm + et

    return nt

    
def list_of_events_generator(g, u, d, k, st, et):
    """
        User movements list of events generator

        :param g:      networkx multidigraph
        :param u:      number of users
        :param d:      simulation duration (days)
        :param k:      kind of network
        :param st:     simulation starting time
        :param et:     simulation ending time
        
        :return:       file - all users' movements with the following information
                       [user_id latitude longitude day hour minute second]
    """

    path = []
    
    if(k == 1):
      # between 3.6 Km/h and 5.4 Km/h  (walk)
      min_speed = 1      # m/s
      max_speed = 1.5    # m/s
    elif(k == 2):
      # between 10 Km/h and 20 Km/h    (bike)
      min_speed = 2.7    # m/s
      max_speed = 5.5    # m/s
    elif(k == 3):
      # between 20 Km/h and 50 Km/h    (drive)
      min_speed = 5.5    # m/s
      max_speed = 13.8   # m/s
    else:
      # between 3.6 Km/h and 50 Km/h   (all)
      min_speed = 1    # m/s
      max_speed = 13.8   # m/s

    file_number = 0
    record_counter = 0
       

    file = open("./Inputs/Mobility/Users/UserMovementsListEvents_{}.txt".format(file_number), 'w')
    file.write("user_id lat lon timestamp\n")	
    print("Generating user movements list of events")
    


    #################################################
    #                   Main Cycle                  #
    #################################################
    for i in tqdm(range(u)):

        lst = list(g.nodes())
        rorg = rd.randint(0, len(lst)-1)
        rdst = rd.randint(0, len(lst)-1)

        org = lst[rorg]
        dst = lst[rdst]

        path = nx.shortest_path(g, org, dst, weight='length')
        
        r_start = rd.uniform(st,et)
        
        wt = walking_time(g, path, min_speed, max_speed)
        
        w = wt.keys()

        nl = []
        et0 = 0
        nl.append(time_update(r_start, et0))

        for m in w:
            ct = nl[len(nl)-1]
            nl.append(time_update(ct, m))

        for j in range(len(path)):
            file.write("{} {} {} {}\n".format(i+1, g.nodes[path[j]]['y'], g.nodes[path[j]]['x'], nl[j]))
            record_counter += 1
            if(record_counter % 99999 == 0):
                file_number += 1
                file.close()
                file = open("./Inputs/Mobility/Users/UserMovementsListEvents_{}.txt".format(file_number), 'w')
                file.write("user_id lat lon timestamp\n")

        time.sleep(0.01)
    print("Records generated:", record_counter, "\nFiles generated:", file_number+1)


    
    file.close()

    
def read_user_movements_list_events(path):
   """
      Read data from file
      
      :return:    list of lists made up of user movements (time and space information)
                  [user_id latitude longitude day hour minute second]
   """

   n_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

   setup_data = []
   l = []

   for i in range(n_files):
      with open("{}/UserMovementsListEvents_{}.txt".format(path,i)) as f:
         data = f.readlines()
      setup_data = setup_data + data[1:len(data)]
   
   for k in range(1, len(setup_data)):
      try:
         sd = setup_data[k].split()
         l.append([int(sd[0]), float(sd[1]), float(sd[2]), float(sd[3])])
      except:
         print("header ", end=" ")
      
   return l
