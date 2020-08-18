.. _data_and_data_base:

Data and Database
=================

Database
------------------------------

The foundation for the Inve2st Framework is a PostgreSQL Database. Queries have been defined to be able to use the framework as flexible as possible, e.g. for choosing different scenario_IDs for different kinds of data. All queries can be found in the modules.Queries *Link Einfügen API*

If the database is installed locally by the user, the database needs to be set as TRUE (self.db_on = True) within the module investment_options.

If the data from the database should be written into the input folder the function needs to be set as True (self.write_data = True)


Equipment Data
------------------------------


To be able to use the framework without the database, equipment data is provided for different scenarios and aggregation levels. 

The data provided are the results of the database queries for specific settings. The provided data can be found in …\sozio_e2s_model\Inve2st_Passenger_car\inputs. 


The names of the folders are a combination of the settings for the queries:
investment_option _ aggregation_level _ (tec_none) _ttribute_sceanrio _ probability_calc_type_main_sub


One exemplary set of input files (as csv) is described here:


.. toctree::
   :maxdepth: 2
   :glob:

   data_inputs/*


Database Credentials
------------------------------
To be able to connect to database, the login credentials should be set in credentials.json.

.. code-block:: JSON

	{
		"dbname": "sozio_e2s",
		"host": "db_host", 
		"user": "my_user", 
		"password" : "mypassword"
	}

Data of Power-to-Gas
------------------------------

All required Data is located in the "inputs" folder.
