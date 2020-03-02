from modules.Investment_Options import Investment_Options
from modules.DataBase import DataBase
import json
import os




db_on = False
write_data = False # control variable to write data from DB to csv

read_data = True

if read_data == False:        
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
    DB = DataBase(dbname=credentials['dbname'], host=credentials['host'], user=credentials['user'],password=credentials['password'])



######################################################################################################################
#-------USER INPUT----------------------------------------------------------------------------------------------------

#------Car class---------------------------------------------------------------
    
#'Class1_small'  -  passenger car containing minis, small cars and compact class 
#'Class2_medium' -  passenger car containing mid-sized cars
#'Class3_upper'  -  passenger car containg upper mid-sized cars and luxury cars  

investment_option='Class3_upper'

#------Value resolution for utilities------------------------------------------

#'individual_raw'   - individual values (containing the full sample)
#'average_raw'      - average values (average of full sample)
value_resolution = 'average_raw'

# Value resolution for utilities 

#------Aggregation level-------------------------------------------------------

#'individual'  - individual values (containing the full sample) (Same as value resolution)
#'average'     - average values (containing the full sample) (Same as value resolution)
aggregation_level = 'average'


#------Attribute scenario development -----------------------------------------
#Defines a scenario in which the attributes (CAPEX, fuel price, range, CO2-tax, CO2-emissions and infrastructure are...) 

#'S1_contra_afv'   - in favor of conventional vehicles (CV) and against alternative vehicles (AV) ( battery electric (BEV) and fuel cell cars (FCEV))
#'S1_moderate_afv' - moderate for CV and AV  
#'S1_pro_afv'      - in favor of AV
attribute_sceanrio ='S1_moderate_afv'

#------None option ------------------------------------------------------------
# additional choice for the investment decision tec_none = True means that also no car can be prefered/ option 
#tec_none = True   -  not suggested for stock calculation as exchange rate is given by growth factor (for calculation of preference shares only it can be considered)
tec_none = False

#------Method to calculated preferences ---------------------------------------
#'first_choice'  - always choice for alternative with highes utility
#'logit'         - Assumes logit distribution for choices 

probability_calc_type = 'logit'

#------Assumption for growth rate of car stock  -------------------------------
#'S_decreasing_1' - 1% degrease per year
#'S_constant'     - constant car stock
#'S_decreasing_05'- decrease by 0.5% per year
growth_scenario = 'S_constant'

#------Assumptions for CO2-calculation-----------------------------------------
# assumption of average passenger kilometers for calculating CO2-emissions [Pkm/car]
average_passenger_kilometers = 20900
specific_consumption_scenario = 'S_base'  #average consumption of cars [kWh/100km]

#'S_95_Reduction'   - primary energy factor of grid electricity mix with 95% CO2 emission reduction until 2050 (provided in extra file - can be exchanged in input file)
#'S_85_Reduction'   - primary energy factor of grid electricity mix with 85% CO2 emission reduction until 2050 (default)
specific_emissions_electricity_mix_scenario = 'S_85_Reduction'


specific_emissions_scenario = 'S_emissions_calibrated_average'  # co2-emissions of CV [g/km] (real)

######################################################################################################################

# settings only possible with database connection to separate the sample according to personal-related factors (e.g. only part of sample where degree of information is high)
if value_resolution == 'average_raw' and aggregation_level == 'average':
    main_sub = {}
else:
    main_sub = {}  

#-------CALLING FUNCTIONS----------------------------------------------------------------------------------------------------

folder_name = investment_option + '_' + aggregation_level + '_' +'_'+str(tec_none)+ '_'+attribute_sceanrio + '_' + probability_calc_type + '_' +  json.dumps(main_sub).replace(':','_').replace('"','')

io = Investment_Options(folder_name,investment_option=investment_option,starting_year=2018,DB=False,db_on=db_on,write_data=write_data,read_data=read_data)



#Creates folder for results 
directory = os.path.join(os.getcwd() ,'results', io.folder_name)
if not os.path.exists(directory):
    os.makedirs(directory)

#Creates folder for inputs
directory = os.path.join(os.getcwd() ,'inputs',io.folder_name)
if not os.path.exists(directory):
    os.makedirs(directory)

# Calls ulitity calculation 
utility_alternatives = io.calculate_utility(value_resolution,attribute_sceanrio,aggregation_level,tec_none=tec_none)

# Calls preference share calculation
if probability_calc_type=='logit':
    probabilities,df_filter = io.calculate_logit_probabilities(utility_alternatives,main_sub)
elif probability_calc_type=='first_choice':
    probabilities,utility_alternatives2 = io.calculate_first_choice(utility_alternatives,main_sub)

if not tec_none:
    # Calls stock model calculation 
    stock_sum, car_stock,CO2_emissions = io.stock_model(probabilities,growth_scenario,average_passenger_kilometers,specific_consumption_scenario, specific_emissions_electricity_mix_scenario,specific_emissions_scenario )


