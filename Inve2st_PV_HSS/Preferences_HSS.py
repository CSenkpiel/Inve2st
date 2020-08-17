import os
import json
from modules.Investment_Options import Investment_Options

#--------------------------DATABASE SETTINGS-----------------------------------

# Specification if data base connection exists 
databaseconnection = False  # False no connection; True connection to database

# Fixed settings 
if databaseconnection == True:
    from modules.DataBase import DataBase
    from modules.Queries import Query
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
    DB = DataBase(dbname=credentials['dbname'], host=credentials['host'], user=credentials['user'],password=credentials['password'])
    db_on=True
    write_data=True
    read_data=False
else: 
    db_on=False
    write_data=False
    read_data=True
    DB = 'not defined'
    
######################################################################################################################
#-------USER INPUT----------------------------------------------------------------------------------------------------
#CHOICES 
investment_option='PV_homestorage' 

#CHOICES    
# individual_raw
# average_raw
value_resolution = 'individual_raw'

if value_resolution == 'individual_raw':
    aggregation_level = 'individual'
else: aggregation_level = 'average'




# 'Conservative', 'Progressive' # can be specified in input folder also for different years 
attribute_sceanrio ='Conservative'


tec_none = True #need to be true for Homestoragesystems

probability_calc_type = 'logit' #Choices: first_choice; logit

# if respondend data is clustered to specific groups it ca be specified here
main_sub = {}

folder_name = investment_option + '_' + aggregation_level + '_' +'_'+str(tec_none)+ '_'+attribute_sceanrio + '_' + probability_calc_type + '_' +  json.dumps(main_sub).replace(':','_').replace('"','')


######################################################################################################################
#-------CALLING FUNCTIONS----------------------------------------------------------------------------------------------------

io = Investment_Options(folder_name=folder_name,investment_option=investment_option,starting_year=2018,DB=DB,db_on=db_on,write_data=write_data,read_data=read_data)


#Creates folder for results 
directory = os.path.join(os.getcwd() ,'results', io.folder_name)
if not os.path.exists(directory):
    os.makedirs(directory)

#Creates folder for inputs
if databaseconnection == True:
    directory = os.path.join(os.getcwd() ,'inputs',io.folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)


# Calls ulitity calculation 
#utility_alternatives = io.calculate_utility(value_resolution,attribute_sceanrio,aggregation_level,tec_none=tec_none)
utility_alternatives,attribute_levels_putility_comb,attribute_levels_putility_comb_cont,continuous_df = io.calculate_utility(value_resolution,attribute_sceanrio,aggregation_level,tec_none=tec_none)

# Calls preference share calculation
if probability_calc_type=='logit':
    probabilities,df_filter = io.calculate_logit_probabilities(utility_alternatives,main_sub)
elif probability_calc_type=='first_choice':
    probabilities,utility_alternatives = io.calculate_first_choice(utility_alternatives,main_sub)
    