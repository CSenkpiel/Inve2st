.. _Class1_small_average__False_S1_moderate_afv_logit_{}:

Class1_small_average__False_S1_moderate_afv_logit_{}
====================================================

**Description of the folder name**

investment_option = Class1_small 
aggregation_level = average
tec_none = False
growth_scenario = S1_moderate_afv
probability_calc_type = logit
main_sub = {}

A subset of each input csv files is shown below: 

List of investment option alternatives **(query_investment_option_alternatives)**
   
.. csv-table:: query_investment_option_alternatives
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_investment_option_alternatives.csv
   :delim: ;
   :header-rows: 1
   :widths: 1
   :stub-columns: 0

Description of the alternatives:

List of all alternatives related to the car type **alternatives**:
	1. tec_bev (battery electric vehicles)
	2. tec_cv (conventional vehicles, diesel/gasoline)
	3. tec_fecv (fuel cell electric vehicle)
	4. tec_none (no car/optional)

Following are the options that the table columns could contain;

The attribute scenarios are in  **(query_attribute_level_per_year)**

where: 
year: integer range between [2018,2050]

The cars have a list of **attributes** which have different **attribute_level** s (which are part of the discrete choice experiment)
	1. att_CAPEX (investment cost)
		a. numeric range []
	2. att_Co2_tax (additional CO2-tax on gazoline and diesel)
		a. co2_tax
		b. no_co2_tax
	3. att_v_type (vehicle type)
		a. BEV (battery electric vehicle)
		b. CV (conventional vehicle)
		c. FCEV (fuel cell electric vehicle)
	4. att_fuel_cost (fuel cost per 100 km)
		a. numeric range []
	5. att_infrast (charging infrastructure)
		a. strong_res (with strong restrictions)
		b. with_res (with restrictions)
		c. no_res (without restrictions)
	6. att_range (average maximum range for the vehicle)
		a. numeric range []
	7. att_w2w (Weel2well CO2-emissions)
		a. low_co2
		b. medium_co2
		c. high_co2
		
The query_attribute_level_per_year delivers the following table


.. csv-table:: query_attribute_level_per_year
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_attribute_level_per_year.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1, 1
   :stub-columns: 0
  
The attribute and attribute_level should be same as defined above, whereas the attribute levels for the continuous values need to stay within the limits of the discrete chocie experiment.

List of discrete attributes **(query_discrete_attributes)**

.. csv-table:: query_discrete_attributes
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_discrete_attributes.csv
   :delim: ;
   :header-rows: 1
   :widths: 1
   :stub-columns: 0

The **query_attribute_level_putility**

Data source is the discrete chocice experiment data. The average values are the average from individual values. 
In this case the respondend_ID equals a numeric value. Note that individual values are prefered because the uncertainty with average values is high.

 
.. csv-table:: query_attribute_level_putility
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_attribute_level_putility.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1, 1, 1
   :stub-columns: 0


The **query_utility_none_option** is separated from the other alternatives, as it is optional


.. csv-table:: query_utility_none_option
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_utility_none_option.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1, 1, 1
   :stub-columns: 0


The query **query_stock** delivers the historical stock, containing the registration year of the cars. 
  
.. csv-table:: query_stock
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_stock.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1, 1, 1, 1, 1, 1
   :stub-columns: 0


The **query_stoc_init_year** delivers the actual stock (2018), containing the registration year of the cars. 

.. csv-table:: query_stoc_init_year
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_stoc_init_year.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1
   :stub-columns: 0


The **query_car_class_share** delivers percentage of the chosen car classes (small, medium or upper and luxury on the basis of the investment-option)


.. csv-table:: query_car_class_share
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_car_class_share.csv
   :delim: ;
   :header-rows: 1
   :widths: 1
   :stub-columns: 0


The **query_sub_technology_share** delivers total number of cars by vehicle type (tec_bev, tec_fcev, tec_cv)

.. csv-table:: query_sub_technology_share
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_sub_technology_share.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1
   :stub-columns: 0
 
The **query_investor_stock_share** delivers percentage of the investor (private owners) of the total car stock

.. csv-table:: query_investor_stock_share
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_investor_stock_share.csv
   :delim: ;
   :header-rows: 1
   :widths: 1
   :stub-columns: 0


The **query_car_stock_scenario** delivers the annual percentage increase or decrease of the total car stock (e.g. 0.01,0, -0.01 )


.. csv-table:: query_car_stock_scenario
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_car_stock_scenario.csv
   :delim: ;
   :header-rows: 1
   :widths: 1
   :stub-columns: 0


The **query_car_target_value** defines the total number of cars per vehicle type as a target value 

.. csv-table:: query_car_target_value
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_car_target_value.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1
   :stub-columns: 0


The **query_spec_emissions_cv** gives values for the specific emissions of conventional vehicles for the car size of the investment option per registration year  [gCO2/km]

.. csv-table:: query_spec_emissions_cv
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_spec_emissions_cv.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1
   :stub-columns: 0

The **query_spec_emissions_electricity_mix** gives values for the specific emissions of the electricty mix for a choosen scenario  per year  [kgCO2/kWh]

.. csv-table:: query_spec_emissions_electricity_mix
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_spec_emissions_electricity_mix.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1
   :stub-columns: 0
   

The **query_specific_consumption** gives values for the specific consumption pf BEV and FCEV per construction year and choosen car size [kWh/100km]

.. csv-table:: query_specific_consumption
   :file: Class1_small_average__False_S1_moderate_afv_logit_{}/query_specific_consumption.csv
   :delim: ;
   :header-rows: 1
   :widths: 1, 1, 1
   :stub-columns: 0



   



   



   



   

   