.. _quick_start:

Quick Start
=============

Installation
------------------------------
Download the code from https://www.github.com

Hint: If working in Spyder IDE, please set the working directory to the root folder (Inve2st_Passenger_car).

Prerequisites
------------------------------
Please use Python 3.7. 
Following python modules are required and should be installed before running the framework.
 

	- numpy 
	- scipy
	- pandas
	- scikit-learn 
	- psycopg2 

Minimum working example Passenger Cars
------------------------------
To run the simulation for passenger cars car_simulation.py needs to be executed. 
If no own PostgreSQL Database – according to the Inve2st schema is set up, the model can be run without database – reading in csv data from the Input folder. Within the car_simulation.py the following settings need to be put to work with csv files:

.. figure:: images/setting_db_off.png
   :align: center
   :scale: 70%
   
.. figure:: images/setting_db_off2.png
   :align: center
   :scale: 70%

The csv files are provided for different cases:

.. figure:: images/Input_folder.PNG
   :align: center
   :scale: 70% 

The options (scenarios) that are available are put as comments in the car_simulation.py  and can be replaced by the other available options(e.g. investment_option = ‘Class1_small’ can be replaced by investment_option = ‘Class2_medium’). The folder name in the input order shows which scenarios are available by default. A detailed description of the data can be found under "Data and Database". A short description of the options is provided in the code. 
In the folder inputs/scenario_data an excel sheet is provided containing attribute developments for 4 different scenarios, which can be filtered an replaced in the input/query_attribute_level_per_year.csv - if the scenario is not supplied by default. 
Ensure that the folder name is build according to the "folder_name" specification  

All user settings can be made in the car_simulation.py 

.. figure:: images/test_py.PNG
   :align: center
   :scale: 70%
