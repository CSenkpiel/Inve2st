# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:51:34 2019

@author:  Charlotte Senkpiel
"""
import os
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots


#--------------------------DATABASE SETTINGS-----------------------------------

# Specification if data base connection exists 
databaseconnection = True  # False no connection; True connection to database

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

#--------------------------USER VARIABLES-------------------------------------- 

# New scenario name can be chosen, if connection to database exists
# if not please use Scenario name 'Default_Data'
Scenario_name = 'Default_Data'

if os.path.exists(os.path.join(os.getcwd(),'inputs',Scenario_name)) == False:  # Creation of folder if database connection exists
    os.mkdir(os.path.join(os.getcwd(),'inputs',Scenario_name))


#____Iterables____________________________________________________________

# If iterables are true more than one parameter combination can be calculated. 
#Iterables are(demand, regions, PV_orientation, ratio PV-to demand, ratio PV to battery, year,  WACC, CAPEX PV, CAPEX battery,FIT, EEX price, household electrity price;
#TRUE/FALSES only changes the plotting)

#iterables_on = True
iterables_on = False                                                           # used for plotting options so if iterables specicified use True else False 

#demand_scenarios = ['Row_house_Family_4P','single_family_house_2_persons']    # available demand scenarios    (multiple can be chosen) 
demand_scenarios = ['single_family_house_2_persons']

#regions =['DE731','DEF01','DE131']                                            # available regions for PV generation #DE731 (Kassel), DEF01 (Flensburg), DE131 (Freiburg), (multiple can be chosen) 
regions =['DE131']

#PV_orientations= ['S1_pv_eastwest','S2_pv_renewable_ninja_south']             # available PV orientations, (multiple can be chosen) 
PV_orientations= ['S2_pv_renewable_ninja_south']

# Dimensioning of PV-battery system 
#ratio PV-size to electricity demand
#ratio_PV_demands = [0.8, 1, 1.2, 1.4]                                         # suggestions of ratios Figgener.2018, (multiple can be chosen) 
ratio_PV_demands = [1]

# PV size to Battery capacity
#ratio_PV_Batterys = [0.8,1,1.5,2]                                             # suggestions of ratios (between 0.8 and 5 / around 1/ 1.5), (multiple can be chosen) 
ratio_PV_Batterys = [1]                                                      

ratio_storage_energy_power = 2                                                      

roundtrip_efficiency_bat = 0.85                                                # Figgener.2018 (0.75 - 0.95), (multiple can be chosen) 

#____GENERAL___________________________________________________________________
#investment_option = 'homestorage'
investment_option = 'PV_homestorage' 
#start_years = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2040,2050] #(multiple years  can be chosen) 
start_years = [2020]

#____economic calculations_____________________________________________________
technical_lifetime_PV = 20 # fix (don´t change)
technical_lifetime_battery = 10 # fix (don´t change)

degradation_rate = 0.0025 # per year
Subsidy_Invest_PV = 0.0 # Percent of CAPEX
Subsidy_Invest_Bat =  0.0 # Percent of CAPEX 
OPEX_fix_PV = 0.025 #percent of CAPEX
FIT_duration = 20 
VAT = 0.19 


WACCs = [0.018] # (multiple can be chosen) 

#['S1_PV_high_3_to10kW', 'S1_PV_high_less_3kW', 'S1_PV_low_3_to10kW', 'S1_PV_low_less_3kW'] # (multiple can be chosen) 
scenario_CAPEX_PVs = ['S1_PV_low_3_to10kW']

#scenario_CAPEX_bats = ['S2_battery_high_path_6to12kWh', 'S2_battery_high_path_upto6kWh', 'S2_battery_low_path_6to12kWh', 'S2_battery_low_path_upto6kWh']  # (multiple can be chosen) 
scenario_CAPEX_bats = ['S2_battery_low_path_6to12kWh']

#scenario_FITs = ['S_0_percent_degression','S_05_percent_monthly_degression','S_1_percent_monthly_degression','S_2_percent_monthly_degression','S_2_8_percent_monthly_degression']  # (multiple can be chosen) 
scenario_FITs = ['S_0_percent_degression']

#scenario_eex_prices = ['EEX_low','EEX_high']  # (multiple can be chosen) 
scenario_eex_prices = ['EEX_high'] 

#scenario_consumption_prices = ['S3_high_price_hh', 'S1_low_price_hh','S2_medium_price_hh']  # (multiple can be chosen) 
scenario_consumption_prices = ['S3_high_price_hh']


installation_costs = 1500 


#---------------------------Result MultiIndex----------------------------------


iterables = [start_years,demand_scenarios,regions,PV_orientations,ratio_PV_demands,ratio_PV_Batterys,WACCs,scenario_CAPEX_PVs,scenario_CAPEX_bats,scenario_FITs,scenario_eex_prices, scenario_consumption_prices]

result_df = pd.DataFrame(columns=['degree_autarky_wo_storage','degree_autarky_w_storage','own_consumption_wo_stor','own_consumption_w_stor','pay_back','NPV','IRR'],index=pd.MultiIndex.from_product(iterables))


#--------------------------SIMULATION------------------------------------------

#____PV-battery USE____________________________________________________________

# CALCULATE THE DEGREE OF AUTARKY and OWN CONSUMPTION
# Battery usage to maximize degree of autarky 

def calculate_PV_battery_use(demand_scenario,region, PV_orientation):
    """
    Calculation of the PV battery operation on the basis of a specified load profile and the PV feed-in time series to determine the degree of self-sufficiency and the share of own consumption 
    
    Parameters
    ----------
    demand_scenario: str
        Input for query to get hourly loadprofile (if database is enables) e.g. 'Row_house_Family_4P'; 
        csv file containing hourly load data 
    region: str
        NUTS3 code for Germany used to filter generation tiemseries from database for query_generation_profile(region, PV_orientation)
        e.g. 'DE131'
        (w.o. database used to write csv file with generation data from database)
    PV_orientation: str 
        Identifier to filter generation tiemseries from database for query_generation_profile(region, PV_orientation)
        e.g. 'S1_pv_eastwest','S2_pv_renewable_ninja_south'
        (w.o. database used to write csv file with generation data from database)
    Returns
    -------
    Own_consumption_wo_stor: float degree of own consumption without storage system
    Own_consumption_w_stor: float degree of own consumption with storage system
    Degree_autarky_wo_stor: float degree of autarky without storage system
    Degree_autarky_w_stor: float degree of autarky with storage system
    load_sum: float sum of electricity demand
    gen_PV_wo_stor_sum: float sum of PV generation without storage
    gen_PV_w_stor_sum: float sum of PV generation with storage
    df_PV_use : Pandas.DataFrame() containing the columns [Datetime, load_kw, units, gen_scaled, residual_load_wo_stor, Feed_in_wo_stor, curtailment_wo_stor,SOC,charge, discharge, Feed_in_w_stor, curtailment_w_stor]
    """
    # Reading in data 

    if db_on:
        # Query household load [kW] 
        load = pd.DataFrame(DB.execute_query(Query().query_demand(demand_scenario))) 
        load.columns = ['Datetime','load_kW','units']

    if write_data:
        load.to_csv(os.path.join(os.getcwd(),'inputs',Scenario_name, demand_scenario+'load.csv'),sep=';', index = False)

    if read_data:
        path = os.path.join(os.getcwd(),'inputs',Scenario_name,demand_scenario+'load.csv')
        load = pd.read_csv(path,sep=';')
 
    load.load_kW = load.load_kW.astype(float)
    load_sum = sum(load.load_kW)

    PV_cap = ratio_PV_demand * load_sum/1000
    battery_cap = ratio_PV_Battery * PV_cap
    charge_cap = battery_cap / ratio_storage_energy_power
    discharge_cap = battery_cap / ratio_storage_energy_power

    # Query generation timeseries (normalized to 1 kW) 
    if db_on:
        gen_norm = pd.DataFrame(DB.execute_query(Query().query_generation_profile(region, PV_orientation)))
        gen_norm.columns = ['Datetime','generation_norm_kW','units']
        
    if write_data:
        gen_norm.to_csv(os.path.join(os.getcwd(),'inputs',Scenario_name,region+"_"+PV_orientation+'_generation.csv'),sep=';', index = False)

    if read_data:
        path = os.path.join(os.getcwd(),'inputs',Scenario_name,region+"_"+PV_orientation+'_generation.csv')
        gen_norm = pd.read_csv(path,sep=';')

    gen_norm.generation_norm_kW = gen_norm.generation_norm_kW.astype(float)

    df_PV_use = pd.merge(load, gen_norm, on='Datetime')
    df_PV_use['gen_scaled'] = df_PV_use['generation_norm_kW'] * PV_cap                                          # generation according to PV-size in kW 
    df_PV_use['residual_load_wo_stor'] = df_PV_use['load_kW'] - df_PV_use['gen_scaled']                         # residual load without storage in kW
    
    # iteration over each hour without storage 
    for i in range(len(df_PV_use)):
        if df_PV_use.loc[i,'residual_load_wo_stor'] >= 0:                                                       # if residual load (without storage) is positive electricity can be self-consumed (no grid feed-in)
            df_PV_use.loc[i,'Feed_in_wo_stor'] = 0
            df_PV_use.loc[i,'curtailment_wo_stor'] = 0 
        else: 
            df_PV_use.loc[i,'Feed_in_wo_stor'] = df_PV_use.loc[i,'residual_load_wo_stor'] *(-1)                 # if residual load (without storage) is negative electricity need to be drawn from the grid 
            df_PV_use.loc[i,'curtailment_wo_stor'] = 0
            if df_PV_use.loc[i,'Feed_in_wo_stor'] >= 0.7 * PV_cap:                                              # curtailment of electricity > 70% of installed capacity (EEG 2014 $9)
                df_PV_use.loc[i,'curtailment_wo_stor'] = df_PV_use.loc[i,'Feed_in_wo_stor'] - 0.7 * PV_cap     
                df_PV_use.loc[i,'Feed_in_wo_stor'] = 0.7 * PV_cap
                
    # initialisation
    df_PV_use['SOC'] = 0
    df_PV_use['charge'] = 0
    df_PV_use['discharge'] = 0
    
    # calculating battery charge 
    for i in range(2, len(df_PV_use)):
        if df_PV_use.loc[i,'Feed_in_wo_stor'] > 0 and df_PV_use.loc[i-1,'SOC'] <= battery_cap:                                  # check if PV excess energy exists and battery is not full 
            if df_PV_use.loc[i,'residual_load_wo_stor'] *(-1) <= charge_cap:
                df_PV_use.loc[i,'charge'] = df_PV_use.loc[i,'Feed_in_wo_stor'] + df_PV_use.loc[i,'curtailment_wo_stor']         # if execss energy is smaller than charging capacity all excess energy can be charged      
            else: df_PV_use.loc[i,'charge'] = charge_cap                                                                        # if execss energy is bigger or equal than charging capacity is charged
            if (df_PV_use.loc[i-1,'SOC'] + df_PV_use.loc[i,'charge']) > battery_cap:                                            # charge only to remaining storage capacity         
                df_PV_use.loc[i,'charge'] = battery_cap - df_PV_use.loc[i-1,'SOC']
            
        # calculating battery discharge
        if df_PV_use.loc[i,'residual_load_wo_stor'] > 0 and df_PV_use.loc[i-1,'SOC'] > 0:                                       # discharge when residual load bigger 0 and storage is not empty
            if df_PV_use.loc[i-1,'SOC'] > discharge_cap:
                df_PV_use.loc[i,'discharge'] = discharge_cap * roundtrip_efficiency_bat
            else: df_PV_use.loc[i,'discharge'] = df_PV_use.loc[i-1,'SOC'] * roundtrip_efficiency_bat
            
        #Calculating SOC
        df_PV_use.loc[i,'SOC'] = df_PV_use.loc[i-1,'SOC'] + df_PV_use.loc[i,'charge'] - df_PV_use.loc[i,'discharge']    
    
    #Calculate residual load with storage
    df_PV_use['residual_load_w_stor'] = df_PV_use['load_kW'] - df_PV_use['gen_scaled'] -  df_PV_use['discharge'] +df_PV_use['charge']
    
    for i in range(len(df_PV_use)):
        if df_PV_use.loc[i,'residual_load_w_stor'] >= 0:                                                                # not Feed in with positive Residual load 
            df_PV_use.loc[i,'Feed_in_w_stor'] = 0
            df_PV_use.loc[i,'curtailment_w_stor'] = 0
        else: 
            df_PV_use.loc[i,'Feed_in_w_stor'] = df_PV_use.loc[i,'residual_load_w_stor'] *(-1)
            df_PV_use.loc[i,'curtailment_w_stor'] = 0                                                                   # if residual load (with storage) is negative electricity need to be drawn from the grid 
            if df_PV_use.loc[i,'Feed_in_w_stor'] >= 0.7 * PV_cap:                                                       # curtailment of electricity > 70% of installed capacity (EEG 2014 $9)
                df_PV_use.loc[i,'curtailment_w_stor'] = df_PV_use.loc[i,'Feed_in_w_stor'] - 0.7 * PV_cap     
                df_PV_use.loc[i,'Feed_in_w_stor'] = 0.7 * PV_cap
    

    load_sum = sum(df_PV_use.load_kW)
    
    
    # Own consumption and autarky without storage
    gen_PV_wo_stor_sum = sum(df_PV_use.gen_scaled) - sum(df_PV_use.curtailment_wo_stor)
    Feed_in_wo_stor_sum = sum(df_PV_use.Feed_in_wo_stor)

    Own_consumption_wo_stor = (gen_PV_wo_stor_sum - Feed_in_wo_stor_sum)/gen_PV_wo_stor_sum
    Degree_autarky_wo_stor = (gen_PV_wo_stor_sum - Feed_in_wo_stor_sum)/load_sum 
    
    # Own consumption and autarky with storage  
    gen_PV_w_stor_sum = sum(df_PV_use.gen_scaled) - sum(df_PV_use.curtailment_w_stor)
    Feed_in_w_stor_sum = sum(df_PV_use.Feed_in_w_stor)  
    
    Own_consumption_w_stor = (gen_PV_w_stor_sum - Feed_in_w_stor_sum)/gen_PV_w_stor_sum
    Degree_autarky_w_stor = (gen_PV_w_stor_sum - Feed_in_w_stor_sum)/load_sum 
    
    df_PV_use.to_csv(os.path.join(os.getcwd(),'inputs',Scenario_name, demand_scenario+'df_PV_use.csv'),sep=';', index = False)
     
    return Own_consumption_wo_stor, Own_consumption_w_stor, Degree_autarky_wo_stor , Degree_autarky_w_stor , load_sum , gen_PV_wo_stor_sum, gen_PV_w_stor_sum, df_PV_use


    
#CALCULATE THE Cash-flow
#Two different equations for PV_bat and only bat 
def calculate_cashflow(technical_lifetime_PV, technical_lifetime_battery, start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC, load_sum,gen_PV_w_stor_sum,Own_consumption_wo_stor, Own_consumption_w_stor):
    """
    Calculation of the cash flow of a home storage system 
    
    Parameters
    ----------
    technical_lifetime_PV: integer [years] e.g 20
    technical_lifetime_battery: integer [years]  e.g 10
    start_year: integer e.g 2020 
    investment_option: string e.g. 'PV_hiom
    scenario_CAPEX_PV: string Scenario ID to filter from database or input data 
    scenario_CAPEX_bat: string Scenario ID to filter from database or input data 
    scenario_FIT: string Scenario ID to filter from database or input data 
    scenario_eex_price: string Scenario ID to filter from database or input data 
    scenario_consumption_price: string Scenario ID to filter from database or input data
    WACC: float e.g. 0.018
    load_sum: float e.g. 4200 kWh (Output from calculate_PV_battery_use)
    gen_PV_w_stor_sum: float e.g. 4410 kWh (Output from calculate_PV_battery_use)
    Degree_autarky_wo_stor: float e.g  0.35(Output from calculate_PV_battery_use)
    Degree_autarky_w_stor: float e.g. 0.55 (Output from calculate_PV_battery_use)
    
    Returns
    -------
    df_cashflow: dataframe containing ['year, Capital_cost','net_annual_cash_flow', 'OPEX','revenue_PV_self_consumption','revenue_battery_self_consumption','Feed_in_tarif','net_annual cash_flow_discounted', 'net_annual_casg_flow_cummulated']
    
    """
    # Input from Database or input folder     
    if db_on:
        CAPEX_PV_df = pd.DataFrame(DB.execute_query(Query().query_capex_pv_r(year=start_year, scenario = scenario_CAPEX_PV))) 
        CAPEX_PV = CAPEX_PV_df[0].astype(float).values[0] #Euro per kWp query_investment_costs
    
    if read_data:
        path = os.path.join(os.getcwd(),'inputs',Scenario_name, 'CAPEX_PV.csv')
        CAPEX_PV_all = pd.read_csv(path,sep=';')
        CAPEX_PV = CAPEX_PV_all.loc[(CAPEX_PV_all['c_economic_parameter_validity_time'] == start_year) & (CAPEX_PV_all['c_economic_parameter_scenario_pk'] == scenario_CAPEX_PV) ,'c_economic_parameter_value'].astype(float).values[0]
    
    PV_cap = ratio_PV_demand * load_sum/1000
    
    if db_on:
        CAPEX_bat_df = pd.DataFrame(DB.execute_query(Query().query_capex_battery(year=start_year, scenario =scenario_CAPEX_bat)))
        CAPEX_bat = CAPEX_bat_df[0].astype(float).values[0] # Euro per kWh query_investment_costs
    
    if read_data: 
        path = os.path.join(os.getcwd(),'inputs',Scenario_name, 'CAPEX_battery.csv')
        CAPEX_battery_all = pd.read_csv(path,sep=';')
        CAPEX_bat = CAPEX_battery_all.loc[(CAPEX_battery_all['c_economic_parameter_validity_time'] == start_year) & (CAPEX_battery_all['c_economic_parameter_scenario_pk'] == scenario_CAPEX_bat) ,'c_economic_parameter_value'].astype(float).values[0]
    battery_cap = ratio_PV_Battery * PV_cap

    if db_on:
        CAPEX_bat_replace = pd.DataFrame(DB.execute_query(Query().query_capex_battery(start_year + technical_lifetime_battery,scenario=scenario_CAPEX_bat)))
        CAPEX_bat_replace = CAPEX_bat_replace[0].astype(float).values[0]
        
    if read_data:
        if (start_year + technical_lifetime_battery)<= 2050:
            CAPEX_bat_replace = CAPEX_battery_all.loc[(CAPEX_battery_all['c_economic_parameter_validity_time'] == start_year + technical_lifetime_battery) & (CAPEX_battery_all['c_economic_parameter_scenario_pk'] == scenario_CAPEX_bat) ,'c_economic_parameter_value'].astype(float).values[0]
        else: CAPEX_bat_replace = CAPEX_battery_all.loc[(CAPEX_battery_all['c_economic_parameter_validity_time'] == 2050) & (CAPEX_battery_all['c_economic_parameter_scenario_pk'] == scenario_CAPEX_bat) ,'c_economic_parameter_value'].astype(float).values[0]
    
    # ELCTRICITY Price
    if db_on:    
        hh_electricity_price = pd.DataFrame(DB.execute_query(Query().query_consumer_prices(c_investment_options_description='PV_homestorage', c_consumertype_description='household',
                              c_consumption_prices_scenario= scenario_consumption_price, start_year=start_year, end_year=technical_lifetime_PV+start_year)))
        hh_electricity_price[3] = pd.to_datetime(hh_electricity_price[3])
        hh_electricity_price['year'] = hh_electricity_price[3].dt.year
        hh_electricity_price[0] = hh_electricity_price[0].astype(float)  
        hh_electricity_price = hh_electricity_price[[0,'year']].groupby(['year']).mean()
        if technical_lifetime_PV+start_year > 2050:
            for yr in range(2051,technical_lifetime_PV+start_year+1):
                hh_electricity_price.loc[yr,0 ] = hh_electricity_price.loc[2050,0]
        hh_electricity_price.columns = ['c_consumer_prices_value']
        
            
    if read_data:        
        path = os.path.join(os.getcwd(),'inputs',Scenario_name, 'electricity_prices.csv')
        hh_electricity_price = pd.read_csv(path,sep=';')
        hh_electricity_price = hh_electricity_price.loc[(hh_electricity_price['year'] >= start_year) & (hh_electricity_price['year'] <= (technical_lifetime_PV+start_year)) & (hh_electricity_price['c_consumption_prices_scenario'] == scenario_consumption_price)]
        hh_electricity_price = hh_electricity_price.set_index('year')

    
    if db_on:  
        fit = float(DB.execute_query(Query().query_political_incentives( c_investment_options_pk='tec_pv', scenario = scenario_FIT ,
                                       tb_political_instrument_types='pol_fit',start_year =start_year))[0][0])/100
    
    if read_data:
       path = os.path.join(os.getcwd(),'inputs',Scenario_name, 'FIT.csv')
       fit = pd.DataFrame(pd.read_csv(path,sep=';'))
       fit = fit.loc[((fit['year'] == start_year) & (fit['c_FIT_scenario'] == scenario_FIT)), 'c_FIT_value'].astype(float).values[0]/100
     
    if db_on:
        end_year = start_year + technical_lifetime_PV
        eex_df = pd.DataFrame(DB.execute_query(Query().query_eex_price(scenario_eex_price,start_year,end_year))) 
        eex_df.columns = ['year','c_EEX_value'] 
        eex =  eex_df.loc[(eex_df['year'] == start_year), 'c_EEX_value'].astype(float).values[0] 
    
    if read_data:
       path = os.path.join(os.getcwd(),'inputs',Scenario_name, 'EEX.csv')
       eex_df = pd.DataFrame(pd.read_csv(path,sep=';'))
       eex = eex_df.loc[((eex_df['year'] == start_year) & (eex_df['c_EEX_scenario'] == scenario_eex_price)), 'c_EEX_value'].astype(float).values[0]

    df_energy_balance = pd.DataFrame()
    df_energy_balance['year'] = 0
    if investment_option == 'PV_homestorage':  
        temp_tec_lifetime=technical_lifetime_PV
    elif investment_option == 'homestorage':
        temp_tec_lifetime=technical_lifetime_battery
    for i in range(1, temp_tec_lifetime+1):
        df_energy_balance.loc[i,'year'] = i
        df_energy_balance.loc[i,'net_generation'] = gen_PV_w_stor_sum * (1-degradation_rate)**i
        df_energy_balance.loc[i,'self_consumption_PV'] = df_energy_balance.loc[i,'net_generation'] * Own_consumption_wo_stor
        df_energy_balance.loc[i,'self_consumption_batt'] = df_energy_balance.loc[i,'net_generation'] * (Own_consumption_w_stor - Own_consumption_wo_stor)
        df_energy_balance.loc[i,'grid'] = df_energy_balance.loc[i,'net_generation'] * (1-Own_consumption_wo_stor - Own_consumption_w_stor)

    df_cashflow = pd.DataFrame()
    df_cashflow['year'] = 0
    for i in range(0, temp_tec_lifetime +1):
        df_cashflow.loc[i,'year'] = i
   
    # Calculate expenses
    df_cashflow['Capital_cost'] = 0
    if investment_option == 'PV_homestorage':  
        df_cashflow.loc[0,'Capital_cost'] = ((CAPEX_PV * PV_cap) * (1-Subsidy_Invest_PV) + installation_costs + (CAPEX_bat * battery_cap) * (1-Subsidy_Invest_Bat))*(-1)       
        df_cashflow.loc[technical_lifetime_battery,'Capital_cost'] =   (CAPEX_bat_replace * battery_cap) * (1-Subsidy_Invest_Bat)*(-1) 
    elif investment_option == 'homestorage':
        df_cashflow.loc[0,'Capital_cost'] = ((CAPEX_bat * battery_cap) * (1-Subsidy_Invest_Bat))*(-1)       
    df_cashflow['net_annual_cash_flow']=0
    df_cashflow['OPEX'] =0
    df_cashflow['rev_PV_self_consumption'] =0
    df_cashflow['rev_battery_self_consumption'] =0
    df_cashflow['compensation_feed_in'] =0
    df_cashflow['rev_Feed_in'] =0
    df_cashflow['net_annual_cash_flow'] =0
    df_cashflow.loc[0,'net_annual_cash_flow'] = df_cashflow.loc[0,'Capital_cost']
    df_cashflow.loc[0,'net_annual_cash_flow_disc'] = df_cashflow.loc[0,'Capital_cost']
    df_cashflow.loc[0,'net_annual_cash_flow_disc_cum'] = df_cashflow.loc[0,'Capital_cost']

    for i in range(1, temp_tec_lifetime +1):
        df_cashflow.loc[i,'OPEX'] = OPEX_fix_PV * CAPEX_bat * battery_cap *(-1)
        df_cashflow.loc[i,'rev_PV_self_consumption'] = df_energy_balance.loc[i,'self_consumption_PV'] * hh_electricity_price.loc[start_year+i,'c_consumer_prices_value'] * (1-VAT)
        df_cashflow.loc[i,'rev_battery_self_consumption'] = df_energy_balance.loc[i,'self_consumption_batt'] * hh_electricity_price.loc[start_year+i,'c_consumer_prices_value'] * (1-VAT)
        
        if eex <= fit: 
            df_cashflow.loc[:,'compensation_feed_in'] = fit
        else:
            if db_on == False:
                df_cashflow.loc[i,'compensation_feed_in'] = eex_df.loc[((eex_df['year'] ==start_year+i) & (eex_df['c_EEX_scenario'] == scenario_eex_price)), 'c_EEX_value'].astype(float).values[0]
            else: 
                df_cashflow.loc[i,'compensation_feed_in'] = eex_df.loc[((eex_df['year'] ==start_year+i)), 'c_EEX_value'].astype(float).values[0]
        
        if df_cashflow.loc[i,'year'] <= FIT_duration:
            df_cashflow.loc[i,'rev_Feed_in'] = df_energy_balance.loc[i,'grid'] * df_cashflow.loc[i,'compensation_feed_in']
        else: 
            df_cashflow.loc[i,'rev_Feed_in'] = 0
        if investment_option == 'PV_homestorage':
            df_cashflow.loc[i,'net_annual_cash_flow'] = df_cashflow.loc[i,'Capital_cost'] + df_cashflow.loc[i,'OPEX'] + df_cashflow.loc[i,'rev_PV_self_consumption'] + df_cashflow.loc[i,'rev_battery_self_consumption'] + df_cashflow.loc[i,'rev_Feed_in'] 
        elif investment_option == 'homestorage':
            df_cashflow.loc[i,'net_annual_cash_flow'] = df_cashflow.loc[i,'Capital_cost'] + df_cashflow.loc[i,'OPEX'] +  df_cashflow.loc[i,'rev_battery_self_consumption'] 
        df_cashflow.loc[i,'net_annual_cash_flow_disc'] = df_cashflow.loc[i,'net_annual_cash_flow']/((1+WACC)**df_cashflow.loc[i,'year'])
        df_cashflow.loc[i,'net_annual_cash_flow_disc_cum'] = df_cashflow.loc[i-1,'net_annual_cash_flow_disc_cum'] + df_cashflow.loc[i,'net_annual_cash_flow_disc'] 
    return df_cashflow


# Calculate Payback 
def calculate_payback(df_cashflow):
    idx = df_cashflow.loc[1:].net_annual_cash_flow_disc_cum.gt(0).apply(abs).idxmax()  
    payback = df_cashflow.loc[idx,"year"]
    
    if df_cashflow.loc[1:].net_annual_cash_flow_disc_cum.gt(0).apply(abs).sum() == 0:
        payback = 99
    return payback


# Calculate Payback    
def calculate_npv(technical_lifetime_PV, technical_lifetime_battery,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor):
    df_cashflow = calculate_cashflow(technical_lifetime_PV, technical_lifetime_battery,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)# Calculate NPV 
    npv = df_cashflow.loc[(len(df_cashflow)-1),'net_annual_cash_flow_disc_cum']
    return npv
    
     

start_i1 = 0.02

step_size = 0.01


def calculate_IRR(technical_lifetime_PV, technical_lifetime_battery,start_i1,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor):
    
    npv_i1 = calculate_npv(technical_lifetime_PV, technical_lifetime_battery,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT, scenario_eex_price,scenario_consumption_price, start_i1,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
    
    list_i = []
    list_npv = []

    if npv_i1 < 0:
        print("LOOP 1")
        start_i2 = start_i1
        list_i.append(start_i1)
        list_npv.append(npv_i1)
        while True:
            start_i2 -= step_size
            npv_i2 = calculate_npv(technical_lifetime_PV, technical_lifetime_battery,start_year,investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, start_i2,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
            list_i.append(start_i2)
            list_npv.append(npv_i2)
        
            if npv_i2 > 0:
                break
          
        C1 = list_npv[-1]
        C2 = list_npv[-2]
        i1 = list_i[-1]
        i2 = list_i[-2]
    else:
        print("LOOP 2")
        start_i2 = start_i1
        list_i.append(start_i1)
        list_npv.append(npv_i1)
        while True:
            start_i2 += step_size
            npv_i2 = calculate_npv(technical_lifetime_PV, technical_lifetime_battery,start_year,investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, start_i2,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
            list_i.append(start_i2)
            list_npv.append(npv_i2)
            if npv_i2 < 0:
                break    
        C1 = list_npv[-2]
        C2 = list_npv[-1]
        i1 = list_i[-2]
        i2 = list_i[-1]
    
    #print((list_i,list_npv))    
    r = i1 - C1 * (i2-i1)/(C1-C2)
    return r

# Iteration 
for start_year in start_years:
    for demand_scenario in demand_scenarios:
        for region in regions:
            for PV_orientation in PV_orientations:
                for ratio_PV_demand in ratio_PV_demands:
                    for ratio_PV_Battery in ratio_PV_Batterys:
                        for WACC in WACCs:
                            for scenario_CAPEX_PV in scenario_CAPEX_PVs:
                                for scenario_CAPEX_bat in scenario_CAPEX_bats:
                                    for scenario_FIT in scenario_FITs:
                                        for scenario_eex_price in scenario_eex_prices:
                                            for scenario_consumption_price in scenario_consumption_prices:
                                             
                                                Own_consumption_wo_stor, Own_consumption_w_stor, Degree_autarky_wo_stor , Degree_autarky_w_stor , load_sum , gen_PV_wo_stor_sum, gen_PV_w_stor_sum, df_PV_use = calculate_PV_battery_use(demand_scenario,region, PV_orientation)
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'degree_autarky_wo_storage'] = Degree_autarky_wo_stor 
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'degree_autarky_w_storage'] = Degree_autarky_w_stor
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'own_consumption_wo_stor'] = Own_consumption_wo_stor 
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'own_consumption_w_stor'] = Own_consumption_w_stor
                                                
                                                df_cashflow = calculate_cashflow(technical_lifetime_PV, technical_lifetime_battery,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT, scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'pay_back'] = calculate_payback(df_cashflow)
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'NPV'] = calculate_npv(technical_lifetime_PV, technical_lifetime_battery,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
                                                result_df.loc[(start_year,demand_scenario,region,PV_orientation,ratio_PV_demand,ratio_PV_Battery,WACC,scenario_CAPEX_PV,scenario_CAPEX_bat,scenario_FIT,scenario_eex_price, scenario_consumption_price),'IRR'] = calculate_IRR(technical_lifetime_PV, technical_lifetime_battery,start_i1,start_year, investment_option, scenario_CAPEX_PV,scenario_CAPEX_bat, scenario_FIT,scenario_eex_price, scenario_consumption_price, WACC,load_sum,gen_PV_w_stor_sum,Degree_autarky_wo_stor, Degree_autarky_w_stor)
                                                

result_df.to_csv(os.path.join(os.getcwd(),'results',Scenario_name+ 'results_econ.csv'),index=True)

#--------------------------------------------------------------------------------------------------------------------------
# Plots without input variatinon 
if iterables_on == False: 
    
    # Plot timeseries    
    data = df_PV_use
    # add a new column of indices, which serves as x axis
    x_col=list(range(1,8761))
    data["x_col"]=x_col

    # opens an interactive plot in a browser
    pio.renderers.default = 'browser'
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.load_kW),name="load_kW",marker=dict(color="black")))
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.gen_scaled),name="gen_scaled"))
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.Feed_in_w_stor),name="Feed_in_w_stor"))
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.curtailment_w_stor),name="curtailment_w_stor"))
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.charge),name="charge"))
    fig.add_trace(
        go.Scatter(x=list(data.x_col), y=list(data.discharge),name="discharge"))                                                                                                                                                          
    
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                
            ),
            rangeslider=dict(
                visible=True
            ),
            title="Hours"
            
        ),
        yaxis=dict(
        title="Power el in kW")
    )
    # Set title
    fig.update_layout(
        title_text="Time series plot"
        
    )
    fig.write_html('tmp.html', auto_open=True)

    # plot cash flow
    pio.renderers.default = 'browser'
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=df_cashflow['year'], y=df_cashflow['Capital_cost'],offsetgroup=0,name="CAPEX"))
    fig.add_trace(    
      go.Bar(x=df_cashflow['year'], y=df_cashflow['OPEX'],offsetgroup=0,base=df_cashflow["Capital_cost"],name="OPEX"))
    fig.add_trace(    
      go.Bar(x=df_cashflow['year'], y=df_cashflow['rev_PV_self_consumption'],offsetgroup=0,name="revenue PV self consumption"))
    fig.add_trace(    
      go.Bar(x=df_cashflow['year'], y=df_cashflow['rev_battery_self_consumption'],offsetgroup=0,base=df_cashflow["rev_PV_self_consumption"],name="revenue battery self consumption"))
    fig.add_trace(    
      go.Bar(x=df_cashflow['year'], y=df_cashflow['rev_Feed_in'],offsetgroup=1,name="revenue feed_in"))
    fig.update_layout(
        yaxis=dict(title="Euro"),
        xaxis=dict(title="Year"), 
        title_text="Cash flow of investment")   
    fig.write_html('tmp.html', auto_open=True)
    
    # plot cumulated cash flow
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=df_cashflow['year'], y=df_cashflow['net_annual_cash_flow_disc'],name="net annual cash flow discounted"))
    fig.add_trace(
        go.Bar(x=df_cashflow['year'], y=df_cashflow['net_annual_cash_flow_disc_cum'],name="cumulatednet annual cash flow discounted"))
    fig.update_layout(
        yaxis=dict(title="Euro"),
        xaxis=dict(title="Year"), 
        title_text="Cumulated cash flow of investment")       
    fig.write_html('tmp.html', auto_open=True)
    
    
    # plot techno-economic benchmarks
    pio.renderers.default = 'browser'
    result_df.rename(columns={'degree_autarky_wo_storage':'Degree aut. wo/stor',
                          'degree_autarky_w_storage':'Degree aut. w/stor',
                          'own_consumption_wo_stor':'Own cons. wo/stor',
                          'own_consumption_w_stor':'Own cons. w/stor'},inplace=True)    
    fig = make_subplots(rows=2, cols=2)

    fig.add_trace(go.Bar(x=['Degree aut. wo/stor'], y=result_df['Degree aut. wo/stor'],name='Degree aut. wo/stor'),
              row=1, col=1)
    fig.add_trace(go.Bar(x=['Degree aut. w/stor'], y=result_df['Degree aut. w/stor'],name='Degree aut. w/stor'),
              row=1, col=1)
    fig.add_trace(go.Bar(x=['Own cons. wo/stor'], y=result_df['Own cons. wo/stor'],name='Own cons. wo/stor'),
              row=1, col=1)
    fig.add_trace(go.Bar(x=['Own cons. w/stor'], y=result_df['Own cons. w/stor'],name='Own cons. w/stor'),
              row=1, col=1)

    fig.add_trace(go.Bar(x=['Payback period'], y=result_df['pay_back'],name='Payback period',width=0.5),
              row=1, col=2)
    fig.add_trace(go.Bar(x=['NPV'], y=result_df['NPV'],name='NPV',width=0.5),
              row=2, col=1)
    fig.add_trace(go.Bar(x=['IRR'], y=result_df['IRR'],name='IRR',width=0.5),
              row=2, col=2)
    fig.update_yaxes(title='share',row=1,col=1)
    fig.update_yaxes(title='years',row=1,col=2)
    fig.update_yaxes(title='euros',row=2,col=1)
    fig.update_yaxes(title='%',row=2,col=2)
    fig.update_layout(showlegend=False, title_text="Economic performance")
    fig.write_html('tmp.html', auto_open=True)
    


if iterables_on == True: 
   
    #scatter
    pio.renderers.default = 'browser'
    names=('<br>start year: ','<br>demand scenario: ','<br>region: ','<br>PV orientation: ',
           '<br>ratio PV demand: ',
           '<br>ratio PV Battery: ','<br>WACC: ','<br>scenario CAPEX PV: ','<br>scenario CAPEX bat: ',
           '<br>scenario FIT: ',
           '<br>scenario eex price: ', '<br>scenario consumption price: ')
    if not 'text_col' in result_df.columns:
        result_df['text_col']=''
    for i in range(0,len(result_df.index)):
        for j in range(0,len(names)):
            result_df['text_col'].values[i]+=names[j]+str(result_df.index[i][j])
        
    fig = make_subplots(rows=2,cols=4,
                        specs=[[{}, {}, {'colspan':2},None],
                               [{'colspan':2},None, {'colspan':2},None]])
    fig.add_trace(go.Scatter(y=result_df['degree_autarky_wo_storage'],mode='markers',name='Degree aut. wo/stor',
                         #hovertext=(result_df['text_col'],result_df['NPV']), 
                         
                         #hoverlabel=dict(namelength=0),
                         #hovertemplate='%{y}<br>year: <br>demand: %{hovertext} <br>Avg. Playtime: %{hovertext}'),
                         text=result_df['text_col']),
                  row=1, col=1)
    fig.add_trace(go.Scatter(y=result_df['degree_autarky_w_storage'],mode='markers',name='Degree aut. w/stor',
                         text=result_df['text_col']),
                  row=1, col=1)
    fig.add_trace(go.Scatter(y=result_df['own_consumption_wo_stor'],mode='markers',name='Own cons. wo/stor',
                  text=result_df['text_col']),
                  row=1, col=2)
    fig.add_trace(go.Scatter(y=result_df['own_consumption_w_stor'],mode='markers',name='Own cons. w/stor',
                  text=result_df['text_col']),
                  row=1, col=2)
    
    fig.add_trace(go.Scatter(y=result_df['pay_back'],mode='markers',name='Payback period',
                         text=result_df['text_col']),
                  row=1, col=3)
    fig.add_trace(go.Scatter(y=result_df['NPV'],mode='markers',name='NPV',
                  text=result_df['text_col']),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=result_df['IRR'],mode='markers',name='IRR',
                  text=result_df['text_col']),
                  row=2, col=3)

 

    fig.update_xaxes(title="Degree autarky",range=[-0.5,(len(result_df) -0.5)],showgrid=True,tickvals=[],row=1,col=1)
    fig.update_xaxes(title="Own consumption",range=[-0.5,(len(result_df) -0.5)],tickvals=[],row=1,col=2)
    fig.update_xaxes(title="Payback period",range=[-0.5,(len(result_df) -0.5)],tickvals=[],row=1,col=3)
    fig.update_xaxes(title="NPV",range=[-0.5,(len(result_df) -0.5)],tickvals=[],row=2,col=1)
    fig.update_xaxes(title="IRR",range=[-0.5,(len(result_df) -0.5)],tickvals=[],row=2,col=3)
    fig.update_yaxes(title='share',row=1,col=1)
    fig.update_yaxes(title='years',row=1,col=3)
    fig.update_yaxes(title='euros',row=2,col=1)
    fig.update_yaxes(title='%',row=2,col=3)
    fig.update_layout(showlegend=True, title_text="Economic performance")
    fig.write_html('tmp.html', auto_open=True)
