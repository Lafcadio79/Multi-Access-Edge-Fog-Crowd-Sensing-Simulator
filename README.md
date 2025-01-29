# Multi-Access Edge Fog CrowdSensing Simulator
A python multi-access (edge) fog mobile crowdsensing simulator. The current version, from a given place creates a user movements list of events and a series of tasks. Subsequently, it computes how many users are able to perform each task on the basis of their distance from the latter. This is what the simulator does, in a nutshell.

## Why?
A MCS campaign involves collecting data through unconventional methods and analyzing it to enhance the areas where it was gathered, such as cities or rural regions. However, planning these campaigns is resource-intensive and costly, requiring significant user recruitment. To mitigate these challenges, running campaigns in a simulated environment that mirrors real-world conditions can be advantageous. To meet this need, we developed a software that simulates the assignment of sensing tasks by an MCS server and their execution by one or multiple users within a chosen real-world scenario.

## Abstract
This work presents MCSim, a task execution simulator for Mobile CrowdSensing (MCS) campaigns that uniquely combines the generation of realistic user mobility patterns with the evaluation of sensing task effectiveness within specified transceiver ranges in urban environments. Unlike previous simulators, MCSim provides a comprehensive yet easy-to-use platform that integrates detailed customization, intuitive execution, and robust results analysis. This makes it an indispensable tool for optimizing MCS strategies while reducing costs and deployment risks.

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
conda create --name=mcsim python=3.8 networkx osmnx haversine tqdm jupyter folium numpy pandas seaborn
conda activate mcsim
```

Note that some libraries (e.g., osmnx and haversine) could not be retrieved by "conda install". Alternatively it is possible to install them using 'pip' once activated the mcsim environment.

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

To run an experiment, select option 2 of the main menu, then enter the name of the city where you want the simulation to run and press return.  

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

Specifically, the main results are temporarily stored into the `Outputs` folder, and are moved into the `saved` folder at the end of the simulation, if requested.

All the information about the users' movement list of events and tasks are respectively stored in the `Users` folder and in the `Tasks` folder.

## Plot Renderer
We have added a Jupyter notebook that demonstrates the generation of figures from the data produced by the simulator. Specifically, the notebook processes the user movement list, task deployment, and task assignment to generate a sample user trajectory over a map and a bar plot showing the number of users able to contribute to the execution of each task.
To run the code is advised to activate the previously created conda environment and launch the notebook by executing the following steps:

```
conda activate MCSim
jupyter notebook plots.ipynb
```

Alternatively, it is possible to run the notebook using the sole Jupyter Lab, just remember to include the following dependencies: numpy, pandas, and seaborn.

# Contributing
If you find something missing, wrong or you want to suggest an improvement you are welcome to notify it by writing an email to the corresponding author: dimitri.belli@isti.cnr.it.

# Authors
Dimitri Belli, Paolo Barsocchi, Antonino Crivello, Michele Girolami and Davide La Rosa
