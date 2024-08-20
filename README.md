# Multi-Access Edge Fog CrowdSensing Simulator
A python multi-access (edge) fog mobile crowdsensing simulator. The current version, from a given place creates a user movements list of events and a series of tasks. Subsequently, it computes how many users are able to perform each task on the basis of their distance from the latter. This is what the simulator does, in a nutshell.

## Why?
A MCS campaign involves collecting data through unconventional methods and analyzing it to enhance the areas where it was gathered, such as cities or rural regions. However, planning these campaigns is resource-intensive and costly, requiring significant user recruitment. To mitigate these challenges, running campaigns in a simulated environment that mirrors real-world conditions can be advantageous. To meet this need, we developed a software that simulates the assignment of sensing tasks by an MCS server and their execution by one or multiple users within a chosen real-world scenario.

## Abstract (tentative)
Set up a living-lab project as a Mobile CrowdSensing (MCS) campaign  for real-world data collection and processing is a costly task both in terms of resources to be allocated and people to be recruited. Consequently, it is often advisable to use simulators that accurately replicate real-world scenarios, as they can offer reliable insights into the system's effectiveness and efficiency, particularly when evaluating the theoretical system's practical functionality. Considering this, we introduce a task execution simulator for MCS, that can generate user mobility patterns and evaluate their effectiveness in performing sensing tasks within a specified transceiver range in a given urban environment. This article explains how the simulator works, including the user interface, settings, execution and interpretation of results.

## What the code does
The execution of the main code enables the user to perform the following:
1. run a saved simulation;
2. create a new list of events (i.e., running a new experiment);
3. delete saved simulations;
4. change the default simulation parameters;
5. exit without prompt.

# Run
To run the code is advised to create a conda environment and install all the required dependencies by executing the following steps:

```
cd Multi-Access-Edge-Fog-Crowd-Sensing-Simulator
conda create --name=mcsim python=3.8 networkx osmnx haversine tqdm
conda activate mcsim
```

Note that some libraries (e.g., osmnx and haversine) could not be retrieved by "conda install". Alternatively it is possible to install them manually using 'pip' once activated the mcsim environment.

## Configuration
No further action required.

## Launch!
To launch the program under Linux use the launcher.sh as follows
```
sh ./launcher.sh
```
To launch the program under Windows use the launcher.bat as follows
```
launcher.bat
```

To run an experiment, select option 2 of the main mnu, then enter the name of the city where you want the simulation to run and press return.  

Before running a new simulation you can modify parameters as the duration (in days), the number of users and tasks, the data transmission range and the kind of platform through option 4 of the main menu.

## Results
The program retrieves data and saves new files from and within the following nested folders:

```
Multi-Access-Edge-Fog-Crowd-Sensing-Simulator
├── Inputs
│   │   ├── Mobility
│   │   │   ├── Users
│   │   │   └── Tasks
├── Outputs
└── saved
```   

Specifically, the main results are temporarily stored into the `Outputs` folder, and are moved into the `saved` folder at the end of the simulation under request.

All the information about the users' movement list of events and tasks are respectively stored in the `Users` folder and in the `Tasks` folder.

# Contributing
If you find something missing, wrong or you want to suggest an improvement you are welcome to notify it by writing an email to the corresponding author: dimitri.belli@isti.cnr.it.

# Authors
Dimitri Belli, Paolo Barsocchi, Antonino Crivello, Michele Girolami and Davide La Rosa
