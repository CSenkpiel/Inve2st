class Query():
    """
    This Class contains methods which help in generating SQL queries for various purposes in the Investment_Options Class.
    """
    def __init__(self):
        """
        Query Class constructor
        """
        pass
    
    def query_investment_option_alternatives(self,investment_option):
        return """SELECT 
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sub_technology_pfk
FROM 
  public.tb_relation_investment_option_alternatives, 
  public.tb_investment_options
WHERE 
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}';
""".format(investment_option)
    
    def query_utility_none_option(self,investment_option,value_resolution):
        return """--query to get the utility values according to the attribute level 
-- it can be chosen according to investment option or the aggregation level ('individual_raw', 'individual_zero_centered','average_raw', 'average_zero_centered')
SELECT 
  tb_utilities.c_utilities_attribute_pfk, 
  tb_utilities.c_utilities_attribute_level_pfk, 
  tb_utilities.c_utilities_value,
  tb_utilities.c_utilities_respondend_pfk,
  tb_utilities.c_utilities_level_pk
FROM 
  public.tb_utilities, 
  public.tb_investment_options
WHERE 
  tb_utilities.c_utilities_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_utilities.c_utilities_investment_options_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_utilities.c_utilities_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_utilities.c_utilities_level_pk = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_utilities.c_utilities_attribute_pfk = 'att_none'
  ;
""".format(investment_option,value_resolution)

    def query_attributes(self,investment_option):
        return """SELECT 
  DISTINCT tb_attribute_level.c_attribute_level_attribute_pfk
FROM 
  public.tb_attribute_level, 
  public.tb_investment_options
WHERE 
  tb_attribute_level.c_attribute_level_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_attribute_level.c_attribute_level_investment_options_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_attribute_level.c_attribute_level_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_attribute_level.c_attribute_level_attribute_pfk != 'att_none';
""".format(investment_option)

    def query_attribute_level_per_year(self,investment_option,attribute_sceanrio):
        return """-- query to get the the attribute developments according to a chosen scenario and an investment option 

SELECT 
  tb_attribute_scenarios.c_attribute_scenario_sub_technology_pfk, 
  tb_attribute_scenarios.c_attribute_scenario_year_pk, 
  tb_attribute_scenarios.c_attribute_development_attributes_pfk,
  tb_attribute_scenarios.c_attribute_development_value
FROM 
  public.tb_attribute_scenarios, 
  public.tb_investment_options
WHERE 
  tb_attribute_scenarios.c_attribute_scenarios_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_attribute_scenarios.c_attribute_development_investment_option_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_attribute_scenarios.c_attribute_development_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_attribute_scenarios.c_attribute_development_scenario_pk = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{0}';""".format(investment_option,attribute_sceanrio)


    def query_attribute_level_putility(self,investment_option,value_resolution):
      return """--query to get the utility values according to the attribute level 
-- it can be chosen according to investment option or the aggregation level ('individual_raw', 'individual_zero_centered','average_raw', 'average_zero_centered')
SELECT 
  tb_utilities.c_utilities_attribute_pfk, 
  tb_utilities.c_utilities_attribute_level_pfk, 
  tb_utilities.c_utilities_value,
  tb_utilities.c_utilities_respondend_pfk,
  tb_utilities.c_utilities_level_pk
FROM 
  public.tb_utilities, 
  public.tb_investment_options
WHERE 
  tb_utilities.c_utilities_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_utilities.c_utilities_investment_options_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_utilities.c_utilities_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_utilities.c_utilities_level_pk = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_utilities.c_utilities_attribute_pfk != 'att_none'
  ;
""".format(investment_option,value_resolution)
  
#-------------------------CAR Stock----------------------------------------------------------------------------------------------- 
    def query_stoc_init_year(self,investment_option,year):
      return """

SELECT 
  tb_cars_stock.c_registration_year, 
  tb_cars_stock.c_stock_year, 
  tb_cars_stock.c_number_of_cars
FROM 
  public.tb_cars_stock, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_cars_stock.c_technology_pk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_cars_stock.c_stock_year = {1};
""".format(investment_option,year)
  
  
    def query_car_class_share(self,investment_option):
        return """
  SELECT 
  tb_car_class_shares.c_car_class_shares_stock_share
FROM 
  public.tb_car_class_shares, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_car_class_shares.c_car_class_shares_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_car_class_shares.c_car_class_shares_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_car_class_shares.c_car_class_shares_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}';""".format(investment_option)
  
  
    def query_investor_stock_share(self,investment_option):
      return"""
      SELECT 
  tb_investor_stock_share.c_investor_stock_share_stock_share
FROM 
  public.tb_relation_investor_investment_option, 
  public.tb_investment_options, 
  public.tb_investor_stock_share
WHERE 
  tb_relation_investor_investment_option.c_investment_options_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investor_investment_option.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_relation_investor_investment_option.c_investors_pfk = tb_investor_stock_share.c_investor_stock_share_investors_pk AND
  tb_investment_options.c_technology_pfk = tb_relation_investor_investment_option.c_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}';
""".format(investment_option)
  
  # query for vehivle type 
    def query_sub_technology_share(self,investment_option):
        return"""
  SELECT 
  tb_sub_technology_shares.c_sub_tec_shares_validity_year, 
  tb_sub_technology_shares.c_sub_tec_shares_value, 
  tb_sub_technology_shares.c_sub_tec_shares_technology_pfk
FROM 
  public.tb_sub_technology_shares, 
  public.tb_investment_options, 
  public.tb_relation_technologies
WHERE 
  tb_investment_options.c_technology_pfk = tb_relation_technologies.c_technology_main_pfk AND
  tb_relation_technologies.c_technology_sub_pfk = tb_sub_technology_shares.c_sub_tec_shares_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}';""".format(investment_option)

# query growth rate of car stock
    def query_car_stock_scenario(self,investment_option,car_stock_scenario_ID):
        return"""  
  SELECT 
  tb_car_stock_scenario.c_stock_scenario_annual_growth_rate
FROM 
  public.tb_car_stock_scenario, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_car_stock_scenario.c_stock_scenario_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_car_stock_scenario.c_stock_scenario_scenario_pk = '{1}';""".format(investment_option,car_stock_scenario_ID)

    def query_car_target_value(self,investment_option,car_target_scenario):
        return""" 
        SELECT 
  tb_car_target_system.c_car_target_value, 
  tb_car_target_system.c_car_target_year_pk, 
  tb_car_target_system.c_car_target_system_sub_technology_pfk
FROM 
  public.tb_car_target_system, 
  public.tb_investment_options, 
  public.tb_relation_technologies
WHERE 
  tb_investment_options.c_technology_pfk = tb_relation_technologies.c_technology_main_pfk AND
  tb_relation_technologies.c_technology_sub_pfk = tb_car_target_system.c_car_target_system_sub_technology_pfk AND
  tb_car_target_system.c_car_target_scenario_pk = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{0}';
""".format(investment_option,car_target_scenario)

    def query_sub_group(self,main,sub,investment_option):
        return """SELECT 
  tb_respondends_sub_groups.c_respondends_sub_groups_respondend_pfk
FROM 
  public.tb_respondends_sub_groups, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_respondends_sub_groups.c_respondends_sub_groups_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{2}' AND 
  tb_respondends_sub_groups.c_respondends_sub_groups_main_group_pk = '{0}' AND 
  tb_respondends_sub_groups.c_respondends_sub_groups_sub_group_pk = '{1}';""".format(main,sub,investment_option)

    def query_technologies_name(self,tec_pk):
        return """select c_technologies_name from tb_technologies where c_technology_pk='{0}'""".format(tec_pk)

    def query_discrete_attributes(self,investment_option):
        return """SELECT 
  distinct tb_attributes.c_attributes_pk
FROM 
  public.tb_investment_options, 
  public.tb_attribute_level, 
  public.tb_attributes
WHERE 
  tb_investment_options.c_technology_pfk = tb_attribute_level.c_attribute_level_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_attribute_level.c_attribute_level_investment_options_size_pfk AND
  tb_attribute_level.c_attribute_level_attribute_pfk = tb_attributes.c_attributes_pk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_attributes.c_attribute_type = 'discrete';""".format(investment_option)
  

    def query_importances(self,main,sub,inv_opt):
        return """SELECT 
  tb_importances.c_importance_attribute_pfk, 
  avg(tb_importances.c_importance_value)
FROM 
  public.tb_importances, 
  public.tb_respondends_sub_groups, 
  public.tb_investment_options
WHERE 
  tb_respondends_sub_groups.c_respondends_sub_groups_respondend_pfk = tb_importances.c_importance_respondend_pfk AND
  tb_investment_options.c_technology_pfk = tb_importances.c_importances_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_importances.c_importances_investment_options_size_pfk AND
  tb_investment_options.c_investment_options_units_pfk = tb_importances.c_importances_investment_options_units_pfk AND
  tb_respondends_sub_groups.c_respondends_sub_groups_main_group_pk = '{0}' AND 
  tb_respondends_sub_groups.c_respondends_sub_groups_sub_group_pk = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{2}'
Group by
tb_importances.c_importance_attribute_pfk;""".format(main,sub,inv_opt)

    
    def query_specific_consumption(self,investment_option,specific_consumption_scenario):
        return """SELECT 
  tb_specific_consumption.c_specific_consumption_year, 
  tb_specific_consumption.c_specific_consumption_technology_pfk, 
  tb_specific_consumption.c_specific_consumption_value
FROM 
  public.tb_specific_consumption, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_specific_consumption.c_specific_consumption_sub_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_specific_consumption.c_specific_consumption_investment_options_size_pfk AND
  tb_investment_options.c_investment_options_units_pfk = tb_specific_consumption.c_specific_consumption_investment_options_units_pfk AND
  tb_specific_consumption.c_specific_consumption_scenario = '{1}' AND 
  tb_investment_options.c_investment_options_description = '{0}';""".format(investment_option,specific_consumption_scenario)

    def query_emissions_electricity_mix(self,specific_emissions_electricity_mix_scenario):
        return """SELECT 
  tb_specific_emissions_electricity_mix.c_specific_emissions_electricity_mix_year, 
  tb_specific_emissions_electricity_mix.c_specific_emissions_electricity_mix_value
FROM 
  public.tb_specific_emissions_electricity_mix
WHERE 
  tb_specific_emissions_electricity_mix.c_specific_emissions_electricity_mix_scenario = '{0}';""".format(specific_emissions_electricity_mix_scenario)


    def query_specific_emissions(self,investment_option,specific_emissions_scenario):
        return """SELECT 
  tb_specific_emissions_cv.c_specific_emissions_construction_year_pk, 
  tb_specific_emissions_cv.c_specific_emissions_value
FROM 
  public.tb_specific_emissions_cv, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_specific_emissions_cv.c_specific_emissions_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_specific_emissions_cv.c_specific_emissions_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_specific_emissions_cv.c_specific_emissions_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_specific_emissions_cv.c_specific_emissions_scenario_pk = '{1}';""".format(investment_option,specific_emissions_scenario)

 ######################################################################## PV BATTERY #########################################################

    def query_capex_pv_r(self,year,scenario):
        return """SELECT 
  
Avg (tb_economic_parameter.c_economic_parameter_value)
FROM 
  public.tb_economic_parameter
WHERE 
  tb_economic_parameter.c_technology_pfk = 'tec_pv_r' AND 
  tb_economic_parameter.c_economic_parameter_scenario_pk = '{2}' AND 
  tb_economic_parameter.c_economic_parameter_types_pfk = 'ep_capex' AND 
  tb_economic_parameter.c_economic_parameter_validity_time <@ '[{0}-01-01,{1}-01-01)' """.format(year,year+1, scenario)
  
  
    def query_capex_battery(self,year,scenario):
        return """SELECT 
  
Avg (tb_economic_parameter.c_economic_parameter_value)
FROM 
  public.tb_economic_parameter
WHERE 
  tb_economic_parameter.c_technology_pfk = 'tec_bat_li' AND 
  tb_economic_parameter.c_economic_parameter_scenario_pk = '{2}' AND 
  tb_economic_parameter.c_economic_parameter_types_pfk = 'ep_capex' AND 
  tb_economic_parameter.c_economic_parameter_validity_time <@ '[{0}-01-01,{1}-01-01)' """.format(year,year+1,scenario)
    
 
  
  
    def query_applications(self, c_investment_options_description, c_application_characteristics_validity_time_pk,
                           c_application_description, c_application_characteristics_scenario_pk, c_regions_name):
        """
        Query applications 
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment option description
        c_application_characteristics_validity_time_pk: str
            Application characteristics validity time
        c_application_description: str
            Application Description
        c_application_characteristics_scenario_pk: str
            application characteristics scenario
        c_regions_name: str
            Regions Name
            
        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_investment_options.c_investment_options_description, 
  tb_application_characteristics.c_application_characteristics_value, 
  tb_application_characteristics.c_application_characteristics_units_fk, 
  tb_application.c_application_description, 
  tb_application_characteristics.c_application_characteristics_scenario_pk, 
  tb_regions.c_regions_name, 
  tb_application_characteristics_types.tb_application_characteristic_types_description
FROM 
  public.tb_investment_options, 
  public.tb_application_characteristics, 
  public.tb_application, 
  public.tb_regions, 
  public.tb_application_characteristics_types, 
  public.tb_relation_investment_option_application
WHERE 
  tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
  tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
  tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
  tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
  tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
  tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{}' AND 
  tb_application_characteristics.c_application_characteristics_validity_time_pk = '{}' AND 
  tb_application.c_application_description = '{}' AND 
  tb_application_characteristics.c_application_characteristics_scenario_pk = '{}' AND 
  tb_regions.c_regions_name = '{}';""".format(c_investment_options_description,
                                              c_application_characteristics_validity_time_pk,
                                              c_application_description,
                                              c_application_characteristics_scenario_pk,
                                              c_regions_name)

    def query_applications_characteristics(self, c_investment_options_description,
                                           start_year,
                                           end_year,
                                           c_application_description, c_application_characteristics_scenario_pk,
                                           c_regions_name,
                                           tb_application_characteristic_types_description):
        """
        Query Application Characteristics
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        start_year: str
            Start year
        end_year: str
            End year
        c_application_description: str
            Application description
        c_application_characteristics_scenario_pk: str
            Application characteristic scenario
        c_regions_name: str
            Regions Name
        tb_application_characteristic_types_description: str
            Application characteristic types description

        Returns
        -------
        SQL string
        """
        return """SELECT 
      tb_investment_options.c_investment_options_description, 
      tb_application_characteristics.c_application_characteristics_value, 
      tb_application_characteristics.c_application_characteristics_units_fk, 
      tb_application.c_application_description, 
      tb_application_characteristics.c_application_characteristics_scenario_pk, 
      tb_regions.c_regions_name, 
      tb_application_characteristics_types.tb_application_characteristic_types_description
    FROM 
      public.tb_investment_options, 
      public.tb_application_characteristics, 
      public.tb_application, 
      public.tb_regions, 
      public.tb_application_characteristics_types, 
      public.tb_relation_investment_option_application
    WHERE 
      tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
      tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
      tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
      tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
      tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
      tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
      tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
      tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      daterange('{1}-01-01', '{2}-12-31') && tb_application_characteristics.c_application_characteristics_validity_time_pk AND 
      tb_application.c_application_description = '{3}' AND 
      tb_application_characteristics.c_application_characteristics_scenario_pk = '{4}' AND 
      tb_regions.c_regions_name = '{5}' AND
      tb_application_characteristics_types.tb_application_characteristic_types_description='{6}';""".format(
            c_investment_options_description,
            start_year,
            end_year,
            c_application_description,
            c_application_characteristics_scenario_pk,
            c_regions_name,
            tb_application_characteristic_types_description)
      
      
      
    def query_applications_characteristics_opts(self, c_investment_options_description,
                                                start_year,
                                                end_year,
                                                c_application_description,
                                                c_regions_name,
                                                tb_application_characteristic_types_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        start_year: str
            Start year
        end_year: str
            End year
        c_application_description: str
            Application description
        c_regions_name: str
            Regions name
        tb_application_characteristic_types_description: str
            Application characteristic types description

        Returns
        -------
        SQL string
        """
        return """SELECT 
      tb_application_characteristics.c_application_characteristics_scenario_pk
    FROM 
      public.tb_investment_options, 
      public.tb_application_characteristics, 
      public.tb_application, 
      public.tb_regions, 
      public.tb_application_characteristics_types, 
      public.tb_relation_investment_option_application
    WHERE 
      tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
      tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
      tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
      tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
      tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
      tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
      tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
      tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      daterange('{1}-01-01', '{2}-12-31') && tb_application_characteristics.c_application_characteristics_validity_time_pk AND 
      tb_application.c_application_description = '{3}' AND 
      tb_regions.c_regions_name = '{4}' AND
      tb_application_characteristics_types.tb_application_characteristic_types_description='{5}';""".format(
            c_investment_options_description,
            start_year,
            end_year,
            c_application_description,
            c_regions_name,
            tb_application_characteristic_types_description)

    def query_applications_demand(self, c_investment_options_description,
                                  start_year,
                                  end_year,
                                  c_application_description, c_application_characteristics_scenario_pk, c_regions_name,
                                  tb_application_characteristic_types_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        start_year: str
            Start year
        end_year: str
            End year
        c_application_description: str
            Application description
        c_application_characteristics_scenario_pk: str
            Application characteristics scenario
        c_regions_name: str
            Regions name
        tb_application_characteristic_types_description: str
            Application characteristic types description

        Returns
        -------
        SQL string
        """
        return """SELECT 
      tb_investment_options.c_investment_options_description, 
      tb_application_characteristics.c_application_characteristics_value, 
      tb_application_characteristics.c_application_characteristics_units_fk, 
      tb_application.c_application_description, 
      tb_application_characteristics.c_application_characteristics_scenario_pk, 
      tb_regions.c_regions_name

    FROM 
      public.tb_investment_options, 
      public.tb_application_characteristics, 
      public.tb_application, 
      public.tb_regions, 
      public.tb_application_characteristics_types, 
      public.tb_relation_investment_option_application
    WHERE 
      tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
      tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
      tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
      tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
      tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
      tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
      tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
      tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      daterange('{1}-01-01', '{2}-12-31') && tb_application_characteristics.c_application_characteristics_validity_time_pk AND 
      tb_application.c_application_description = '{3}' AND 
      tb_application_characteristics.c_application_characteristics_scenario_pk = '{4}' AND 
      tb_regions.c_regions_name = '{5}' AND
      tb_application_characteristics_types.tb_application_characteristic_types_description='{6}';""".format(
            c_investment_options_description,
            start_year,
            end_year,
            c_application_description,
            c_application_characteristics_scenario_pk,
            c_regions_name,
            tb_application_characteristic_types_description)


    def query_applications_demand_opts(self, c_investment_options_description,
                                       start_year,
                                       end_year,
                                       c_application_description, c_regions_name,
                                       tb_application_characteristic_types_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        start_year: str
            Start year
        end_year: str
            End year
        c_application_description: str
            Application description
        c_regions_name: str
            Regions name
        tb_application_characteristic_types_description: str
            Application characteristic types description

        Returns
        -------
        SQL string
        """
        return """SELECT 
      DISTINCT tb_application_characteristics.c_application_characteristics_scenario_pk 
    FROM 
      public.tb_investment_options, 
      public.tb_application_characteristics, 
      public.tb_application, 
      public.tb_regions, 
      public.tb_application_characteristics_types, 
      public.tb_relation_investment_option_application
    WHERE 
      tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
      tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
      tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
      tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
      tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
      tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
      tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
      tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      daterange('{1}-01-01', '{2}-12-31') && tb_application_characteristics.c_application_characteristics_validity_time_pk AND 
      tb_application.c_application_description = '{3}' AND 
      tb_regions.c_regions_name = '{4}' AND
      tb_application_characteristics_types.tb_application_characteristic_types_description='{5}';""".format(
            c_investment_options_description,
            start_year,
            end_year,
            c_application_description,
            c_regions_name,
            tb_application_characteristic_types_description)


    def query_applications_size(self, c_investment_options_description, starting_year,
                                c_application_description, c_application_characteristics_scenario_pk, c_regions_name,
                                tb_application_characteristic_types_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        starting_year: str
            Starting year
        c_application_description: str
            Application description
        c_application_characteristics_scenario_pk: str
            Application characteristic scenario
        c_regions_name: str
            Regions name
        tb_application_characteristic_types_description: str
            Application characteristic types

        Returns
        -------
        SQL string
        """
        return """SELECT 
      tb_investment_options.c_investment_options_description, 
      tb_application_characteristics.c_application_characteristics_value, 
      tb_application_characteristics.c_application_characteristics_units_fk, 
      tb_application.c_application_description, 
      tb_application_characteristics.c_application_characteristics_scenario_pk, 
      tb_regions.c_regions_name 

    FROM 
      public.tb_investment_options, 
      public.tb_application_characteristics, 
      public.tb_application, 
      public.tb_regions, 
      public.tb_application_characteristics_types, 
      public.tb_relation_investment_option_application
    WHERE 
      tb_investment_options.c_technology_pfk = tb_application_characteristics.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_application_characteristics.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_application_characteristics.c_investment_options_units_pfk AND
      tb_application_characteristics.c_application_characteristics_regions_fk = tb_regions.c_regions_pk AND
      tb_application.c_application_pk = tb_application_characteristics.c_application_pfk AND
      tb_application_characteristics_types.c_application_characteristic_types_pk = tb_application_characteristics.c_application_characteristic_types_pk AND
      tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
      tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
      tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
      tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      daterange('{1}-01-01', '{1}-12-31') && tb_application_characteristics.c_application_characteristics_validity_time_pk AND 
      tb_application.c_application_description = '{2}' AND 
      tb_application_characteristics.c_application_characteristics_scenario_pk = '{3}' AND 
      tb_regions.c_regions_name = '{4}' AND
      tb_application_characteristics_types.tb_application_characteristic_types_description = '{5}';
    """.format(c_investment_options_description, starting_year,
               c_application_description, c_application_characteristics_scenario_pk, c_regions_name,
               tb_application_characteristic_types_description)



    def query_consumer_prices(self, c_investment_options_description, c_consumertype_description,
                              c_consumption_prices_scenario, start_year, end_year):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_consumertype_description: str
            Consumer type desciption
        c_consumption_prices_scenario: str
            Consumer prices scenario
        start_year: str
            Start year  
        end_year: str
            End year

        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_consumer_prices.c_consumer_prices_value, 
  tb_consumer_prices.c_consumer_prices_units_fk, 
  tb_consumertype.c_consumertype_description, 
  lower(tb_consumer_prices.c_consumption_prices_validity_time)
FROM 
  public.tb_consumertype, 
  public.tb_consumption_good, 
  public.tb_consumer_prices, 
  public.tb_fuels, 
  public.tb_relation_fuels_technologies, 
  public.tb_investment_options
WHERE 
  tb_consumertype.c_consumertype_pk = tb_consumer_prices.c_consumertype_pfk AND
  tb_consumption_good.c_consumption_good_pk = tb_consumer_prices.c_consumption_good_pfk AND
  tb_fuels.c_fuels_pk = tb_consumer_prices.c_consumer_prices_fuels_fk AND
  tb_relation_fuels_technologies.c_fuels_pfk = tb_fuels.c_fuels_pk AND
  tb_investment_options.c_technology_pfk = tb_relation_fuels_technologies.c_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_consumertype.c_consumertype_description = '{1}' AND 
  tb_consumer_prices.c_consumption_prices_scenario = '{2}' AND 
  daterange('{3}-01-01', '{4}-12-31') && tb_consumer_prices.c_consumption_prices_validity_time;""".format(
            c_investment_options_description, c_consumertype_description, c_consumption_prices_scenario, start_year,
            end_year)
  

    def query_consumer_prices_opts(self, c_investment_options_description, c_consumertype_description,
                                   start_year, end_year):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_consumertype_description: str
            Consumer type description
        start_year: str
            Start year
        end_year: str
            End year

        Returns
        -------
        SQL string
        """
        return """SELECT 
  DISTINCT tb_consumer_prices.c_consumption_prices_scenario 
FROM 
  public.tb_consumertype, 
  public.tb_consumption_good, 
  public.tb_consumer_prices, 
  public.tb_fuels, 
  public.tb_relation_fuels_technologies, 
  public.tb_investment_options
WHERE 
  tb_consumertype.c_consumertype_pk = tb_consumer_prices.c_consumertype_pfk AND
  tb_consumption_good.c_consumption_good_pk = tb_consumer_prices.c_consumption_good_pfk AND
  tb_fuels.c_fuels_pk = tb_consumer_prices.c_consumer_prices_fuels_fk AND
  tb_relation_fuels_technologies.c_fuels_pfk = tb_fuels.c_fuels_pk AND
  tb_investment_options.c_technology_pfk = tb_relation_fuels_technologies.c_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_consumertype.c_consumertype_description = '{1}' AND 
  daterange('{2}-01-01', '{3}-12-31') && tb_consumer_prices.c_consumption_prices_validity_time;""".format(
            c_investment_options_description, c_consumertype_description, start_year,
            end_year)


    def query_consumer_prices_yearly_avg(self, c_investment_options_description, c_consumertype_description,
                                         c_consumption_prices_scenario, start_year, end_year):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_consumertype_description: str
            Consumer type description
        c_consumption_prices_scenario: str
            Consumption prices scenario
        start_year: str
            Start year
        end_year: str
            End year

        Returns
        -------
        SQL string
        """
        return """SELECT 
  avg(tb_consumer_prices.c_consumer_prices_value),
  extract(year from lower(tb_consumer_prices.c_consumption_prices_validity_time)) yr
    FROM 
      public.tb_consumertype, 
      public.tb_consumption_good, 
      public.tb_consumer_prices, 
      public.tb_fuels, 
      public.tb_relation_fuels_technologies, 
      public.tb_investment_options
    WHERE 
      tb_consumertype.c_consumertype_pk = tb_consumer_prices.c_consumertype_pfk AND
      tb_consumption_good.c_consumption_good_pk = tb_consumer_prices.c_consumption_good_pfk AND
      tb_fuels.c_fuels_pk = tb_consumer_prices.c_consumer_prices_fuels_fk AND
      tb_relation_fuels_technologies.c_fuels_pfk = tb_fuels.c_fuels_pk AND
      tb_investment_options.c_technology_pfk = tb_relation_fuels_technologies.c_technology_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      tb_consumertype.c_consumertype_description = '{1}' AND 
      tb_consumer_prices.c_consumption_prices_scenario = '{2}' AND 
      daterange('{3}-01-01', '{4}-12-31') && tb_consumer_prices.c_consumption_prices_validity_time
    GROUP by yr;""".format(
            c_investment_options_description, c_consumertype_description, c_consumption_prices_scenario, start_year,
            end_year)
    
    
    def query_eex_price(self,scenario_eex_price,start_year,end_year):
        """
        Query string for annual EEX price from Database  
         
        Parameters
        ----------
        scenario_eex_prices: str
            Scenario name
        start_year: integer
            start year of investment
        end_year: integer
            start year of cash flow
        Returns
        -------
        SQL string
        """
        return """SELECT 
  extract(year from lower(tb_consumer_prices.c_consumption_prices_validity_time)) as year ,
  avg(tb_consumer_prices.c_consumer_prices_value) as c_EEX_value 
FROM 
  public.tb_consumer_prices
WHERE 
  tb_consumer_prices.c_consumption_prices_scenario = '{0}' AND 
  daterange('{1}-01-01', '{2}-12-31') && tb_consumer_prices.c_consumption_prices_validity_time
GROUP by 
  year
ORDER BY year ASC;""".format(scenario_eex_price,start_year, end_year)



    def query_investment_costs(self, c_economic_parameter_description, c_investment_options_description, c_regions_name,
                               c_economic_parameter_validity_time, c_economic_parameter_scenario_pk):
        """
        
        Parameters
        ----------
        c_economic_parameter_description: str
            Economic parameter description
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            Regions name
        c_economic_parameter_validity_time: str
            Economic parameter validity time
        c_economic_parameter_scenario_pk: str
            Economic parameter scenario
        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_economic_parameter.c_economic_parameter_unit_fk, 
  tb_economic_parameter.c_economic_parameter_value, 
FROM 
  public.tb_economic_parameter, 
  public.tb_investment_options, 
  public.tb_regions, 
  public.tb_economic_parameter_type
WHERE 
  tb_investment_options.c_technology_pfk = tb_economic_parameter.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_economic_parameter.c_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_economic_parameter.c_investment_options_units_pfk AND
  tb_regions.c_regions_pk = tb_economic_parameter.c_regions_pfk AND
  tb_economic_parameter_type.c_economic_parameter_types_pk = tb_economic_parameter.c_economic_parameter_types_pfk AND
  tb_economic_parameter_type.c_economic_parameter_description= '{}' AND
  tb_investment_options.c_investment_options_description = '{}' AND 
  tb_regions.c_regions_name = '{}' AND 
  tb_economic_parameter.c_economic_parameter_validity_time = '{}' AND 
  tb_economic_parameter.c_economic_parameter_scenario_pk = '{}';"""
  


    def query_economic_parameters(self, c_investment_options_description, c_regions_name,
                                  c_economic_parameter_validity_time, c_economic_parameter_scenario_pk):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            Regions name
        c_economic_parameter_validity_time: str
            Economic parameter validity time
        c_economic_parameter_scenario_pk: str
            Economic parameter scenario

        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_economic_parameter.c_economic_parameter_unit_fk, 
  tb_economic_parameter.c_economic_parameter_value, 
  tb_economic_parameter_type.c_economic_parameter_description
FROM 
  public.tb_economic_parameter, 
  public.tb_investment_options, 
  public.tb_regions, 
  public.tb_economic_parameter_type
WHERE 
  tb_investment_options.c_technology_pfk = tb_economic_parameter.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_economic_parameter.c_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_economic_parameter.c_investment_options_units_pfk AND
  tb_regions.c_regions_pk = tb_economic_parameter.c_regions_pfk AND
  tb_economic_parameter_type.c_economic_parameter_types_pk = tb_economic_parameter.c_economic_parameter_types_pfk AND
  tb_investment_options.c_investment_options_description = '{}' AND 
  tb_regions.c_regions_name = '{}' AND 
  tb_economic_parameter.c_economic_parameter_validity_time = '{}' AND 
  tb_economic_parameter.c_economic_parameter_scenario_pk = '{}';
""".format(c_investment_options_description, c_regions_name, c_economic_parameter_validity_time,
           c_economic_parameter_scenario_pk)


    def query_economic_parameters_2(self, c_investment_options_description, c_regions_name,
                                    starting_year, c_economic_parameter_scenario_pk,
                                    c_economic_parameter_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            Regions name
        starting_year: str
            Starting year
        c_economic_parameter_scenario_pk: str
            Economic parameter scenario
        c_economic_parameter_description: str
            Economic parameter description
        Returns
        -------
        SQL string
        """
        return """SELECT 
      tb_economic_parameter.c_economic_parameter_unit_fk, 
      tb_economic_parameter.c_economic_parameter_value
    FROM 
      public.tb_economic_parameter, 
      public.tb_investment_options, 
      public.tb_regions, 
      public.tb_economic_parameter_type
    WHERE 
      tb_investment_options.c_technology_pfk = tb_economic_parameter.c_technology_pfk AND
      tb_investment_options.c_investment_options_size_pk = tb_economic_parameter.c_investment_options_size_pk AND
      tb_investment_options.c_investment_options_units_pfk = tb_economic_parameter.c_investment_options_units_pfk AND
      tb_regions.c_regions_pk = tb_economic_parameter.c_regions_pfk AND
      tb_economic_parameter_type.c_economic_parameter_types_pk = tb_economic_parameter.c_economic_parameter_types_pfk AND
      tb_investment_options.c_investment_options_description = '{0}' AND 
      tb_regions.c_regions_name = '{1}' AND 
      daterange('{2}-01-01', '{2}-12-31') && tb_economic_parameter.c_economic_parameter_validity_time  AND 
      tb_economic_parameter.c_economic_parameter_scenario_pk = '{3}' AND
      tb_economic_parameter_type.c_economic_parameter_description = '{4}';
    """.format(c_investment_options_description, c_regions_name, starting_year,
               c_economic_parameter_scenario_pk, c_economic_parameter_description)
    
    
    def query_economic_parameters_economic_lifetime(self, c_investment_options_description, c_regions_name,
                                                    starting_year, c_economic_parameter_scenario_pk,
                                                    c_economic_parameter_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            regions name
        starting_year: str
            starting year
        c_economic_parameter_scenario_pk: str
            Economic parameter scenario 
        c_economic_parameter_description: str
            Economic parameter description

        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_economic_parameter.c_economic_parameter_unit_fk, 
  tb_economic_parameter.c_economic_parameter_value 

FROM 
  public.tb_economic_parameter, 
  public.tb_investment_options, 
  public.tb_regions, 
  public.tb_economic_parameter_type
WHERE 
  tb_investment_options.c_technology_pfk = tb_economic_parameter.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_economic_parameter.c_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_economic_parameter.c_investment_options_units_pfk AND
  tb_regions.c_regions_pk = tb_economic_parameter.c_regions_pfk AND
  tb_economic_parameter_type.c_economic_parameter_types_pk = tb_economic_parameter.c_economic_parameter_types_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_regions.c_regions_name = '{1}' AND 
  daterange('{2}-01-01', '{2}-12-31')  && tb_economic_parameter.c_economic_parameter_validity_time  AND --add range
  tb_economic_parameter.c_economic_parameter_scenario_pk = '{3}' AND
  tb_economic_parameter_type.c_economic_parameter_description = '{4}' ;""".format(c_investment_options_description,
                                                                                  c_regions_name, starting_year,
                                                                                  c_economic_parameter_scenario_pk,
                                                                                  c_economic_parameter_description)
  

    def query_economic_parameters_economic_lifetime_opts(self, c_investment_options_description, c_regions_name,
                                                         starting_year, c_economic_parameter_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            Regions name
        starting_year: str
            Starting year
        c_economic_parameter_description: str
            economic parameter description

        Returns
        -------
        SQL string
        """
        return """SELECT 
DISTINCT  tb_economic_parameter.c_economic_parameter_scenario_pk 

FROM 
  public.tb_economic_parameter, 
  public.tb_investment_options, 
  public.tb_regions, 
  public.tb_economic_parameter_type
WHERE 
  tb_investment_options.c_technology_pfk = tb_economic_parameter.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_economic_parameter.c_investment_options_size_pk AND
  tb_investment_options.c_investment_options_units_pfk = tb_economic_parameter.c_investment_options_units_pfk AND
  tb_regions.c_regions_pk = tb_economic_parameter.c_regions_pfk AND
  tb_economic_parameter_type.c_economic_parameter_types_pk = tb_economic_parameter.c_economic_parameter_types_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_regions.c_regions_name = '{1}' AND 
  daterange('{2}-01-01', '{2}-12-31')  && tb_economic_parameter.c_economic_parameter_validity_time  AND --add range
  tb_economic_parameter_type.c_economic_parameter_description = '{3}' ;""".format(c_investment_options_description,
                                                                                  c_regions_name, starting_year,
                                                                                  c_economic_parameter_description)
  


    
    def query_financial_parameters(self, c_investors_description, c_financial_parameter_scenario_pk, c_regions_name,
                                   c_financial_parameter_types_description, starting_year):
        """
        
        Parameters
        ----------
        c_investors_description: str
            Investors description
        c_financial_parameter_scenario_pk: str
            Financial parameter scenario
        c_regions_name: str
            Regions name
        c_financial_parameter_types_description: str
            Financial parameter types description
        starting_year: str
            Starting year
        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_financial_parameter.c_financial_parameter_value, 
  tb_financial_parameter.c_financial_parameter_units_fk
FROM 
  public.tb_financial_parameter_types, 
  public.tb_financial_parameter, 
  public.tb_relation_investor_investment_option, 
  public.tb_investors, 
  public.tb_regions
WHERE 
  tb_financial_parameter_types.c_financial_parameter_types_pk = tb_financial_parameter.c_financial_parameter_types_pk AND
  tb_relation_investor_investment_option.c_technology_pfk = tb_financial_parameter.c_technology_pfk AND
  tb_relation_investor_investment_option.c_investment_options_size_pfk = tb_financial_parameter.c_investment_options_size_pk AND
  tb_relation_investor_investment_option.c_investment_options_units_pfk = tb_financial_parameter.c_investment_options_units_pfk AND
  tb_investors.c_investors_pk = tb_financial_parameter.c_investors_pfk AND
  tb_regions.c_regions_pk = tb_financial_parameter.c_financial_parameter_regions_fk AND
  tb_relation_investor_investment_option.c_technology_pfk = tb_relation_investor_investment_option.c_technology_pfk AND
  tb_relation_investor_investment_option.c_investment_options_size_pfk = tb_relation_investor_investment_option.c_investment_options_size_pfk AND
  tb_relation_investor_investment_option.c_investment_options_units_pfk = tb_relation_investor_investment_option.c_investment_options_units_pfk AND
  tb_relation_investor_investment_option.c_investors_pfk = tb_investors.c_investors_pk AND
  tb_investors.c_investors_description = '{0}' AND 
  tb_financial_parameter.c_financial_parameter_scenario_pk = '{1}' AND 
  tb_regions.c_regions_name = '{2}' AND 
  tb_financial_parameter_types.c_financial_parameter_types_description = '{3}' AND 
    daterange('{4}-01-01', '{4}-12-31') && tb_financial_parameter.c_financial_parameter_validity_time_pk ;""".format(
            c_investors_description,
            c_financial_parameter_scenario_pk,
            c_regions_name,
            c_financial_parameter_types_description,
            starting_year)
 
    
    def query_demand(self,c_profiles_profile_scenario_pfk):
        return """    SELECT 
  tb_profiles.c_profiles_timestamp_pk, 
  tb_profiles.c_profiles_value, 
  tb_profiles.c_profiles_units_fk
FROM 
  public.tb_profiles
WHERE 
  tb_profiles.c_profiles_profile_scenario_pfk = '{0}';""".format (c_profiles_profile_scenario_pfk)
  
    def query_generation_profile(self, region, PV_scenario):
        return """
SELECT 
  tb_profiles.c_profiles_timestamp_pk, 
  tb_profiles.c_profiles_value, 
  tb_profiles.c_profiles_units_fk
FROM 
  public.tb_profiles
WHERE 
  tb_profiles.c_profiles_profile_pfk = (SELECT 
  mapping_profile_region.c_map_profile_reg_profile_pfk
FROM 
  public.mapping_profile_region
WHERE 
  mapping_profile_region.c_map_profile_reg_regions_pfk = '{0}' AND 
  mapping_profile_region.c_map_profile_reg_scenario_pfk = '{1}');""".format(region, PV_scenario)
  
  
    def query_financial_parameters_opts(self, c_investors_description, c_regions_name,
                                        c_financial_parameter_types_description, starting_year):
        """
        
        Parameters
        ----------
        c_investors_description: str
            Investors description
        c_regions_name: str
            Regions name
        c_financial_parameter_types_description: str
            Financial parameter types description
        starting_year: str
            Starting year
        Returns
        -------
        SQL string
        """
        return """SELECT 
  DISTINCT tb_financial_parameter.c_financial_parameter_scenario_pk
FROM 
  public.tb_financial_parameter_types, 
  public.tb_financial_parameter, 
  public.tb_relation_investor_investment_option, 
  public.tb_investors, 
  public.tb_regions
WHERE 
  tb_financial_parameter_types.c_financial_parameter_types_pk = tb_financial_parameter.c_financial_parameter_types_pk AND
  tb_relation_investor_investment_option.c_technology_pfk = tb_financial_parameter.c_technology_pfk AND
  tb_relation_investor_investment_option.c_investment_options_size_pfk = tb_financial_parameter.c_investment_options_size_pk AND
  tb_relation_investor_investment_option.c_investment_options_units_pfk = tb_financial_parameter.c_investment_options_units_pfk AND
  tb_investors.c_investors_pk = tb_financial_parameter.c_investors_pfk AND
  tb_regions.c_regions_pk = tb_financial_parameter.c_financial_parameter_regions_fk AND
  tb_relation_investor_investment_option.c_technology_pfk = tb_relation_investor_investment_option.c_technology_pfk AND
  tb_relation_investor_investment_option.c_investment_options_size_pfk = tb_relation_investor_investment_option.c_investment_options_size_pfk AND
  tb_relation_investor_investment_option.c_investment_options_units_pfk = tb_relation_investor_investment_option.c_investment_options_units_pfk AND
  tb_relation_investor_investment_option.c_investors_pfk = tb_investors.c_investors_pk AND
  tb_investors.c_investors_description = '{0}' AND 
  tb_regions.c_regions_name = '{1}' AND 
  tb_financial_parameter_types.c_financial_parameter_types_description = '{2}' AND 
    daterange('{3}-01-01', '{3}-12-31') && tb_financial_parameter.c_financial_parameter_validity_time_pk ;""".format(
            c_investors_description,
            c_regions_name,
            c_financial_parameter_types_description,
            starting_year)
    
    
    def query_meteological_data(self):
        pass

    def query_political_incentives(self, c_investment_options_pk, scenario, tb_political_instrument_types,start_year):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_application_description: str
            Application description
        tb_political_instrument_types_description: str
            Political instrument types description
        Returns
        -------
        SQL string
        """
        return """SELECT 
avg (tb_political_incentives.c_political_incentive_value) 
FROM 
  public.tb_political_incentives
WHERE 
  tb_political_incentives.c_technology_pfk = '{0}' AND 
  tb_political_incentives.c_political_instrument_scenario = '{1}' AND 
  tb_political_incentives.c_political_instrument_type_fk = '{2}' AND
  tb_political_incentives.c_political_incentive_validity_time <@ '[{3}-01-01,{4}-01-01)';
""".format(c_investment_options_pk, scenario, tb_political_instrument_types,start_year,start_year+1)
  
    def query_political_incentives_opt(self, c_investment_options_description, c_application_description,
                                       tb_political_instrument_types_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_application_description: str
            Application description
        tb_political_instrument_types_description: str
            Political instrument types description
        Returns
        -------
        SQL string
        """
        return """SELECT 
 DISTINCT tb_political_incentives.c_political_instrument_scenario
FROM 
  public.tb_political_incentives, 
  public.tb_political_instrument_types, 
  public.tb_investment_options, 
  public.tb_application, 
  public.tb_relation_investment_option_application
WHERE 
  tb_political_instrument_types.c_political_instrument_type_pk = tb_political_incentives.c_political_instrument_type_fk AND
  tb_investment_options.c_technology_pfk = tb_political_incentives.c_technology_pfk AND
  tb_investment_options.c_investment_options_size_pk = tb_political_incentives.c_investment_options_size_pfk AND
  tb_investment_options.c_investment_options_units_pfk = tb_political_incentives.c_investment_options_units_pfk AND
  tb_application.c_application_pk = tb_political_incentives.c_political_incentive_application_fk AND
  tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
  tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_application.c_application_description = '{1}' AND 
  tb_political_instrument_types.tb_political_instrument_types_description = '{2}';""".format(
            c_investment_options_description, c_application_description, tb_political_instrument_types_description)
  
  

    def query_stock_scenario(self, c_application_description, c_investment_options_description, c_regions_name):
        """
        
        Parameters
        ----------
        c_application_description: str
            Application description
        c_investment_options_description: str
            Investment options description
        c_regions_name: str
            Regions name
        Returns
        -------
        SQL string
        """
        return """SELECT 
  DISTINCT tb_stock.c_stock_scenario
FROM 
  public.tb_application, 
  public.tb_investment_options, 
  public.tb_regions, 
  public.tb_stock
WHERE 
  tb_application.c_application_pk = tb_stock.c_stock_application_fk AND
  tb_investment_options.c_technology_pfk = tb_stock.c_stock_technology_pfk AND
  tb_regions.c_regions_pk = tb_stock.c_stock_regions_pfk AND
  tb_application.c_application_description =  '{0}' AND 
  tb_investment_options.c_investment_options_description =  '{1}' AND 
  tb_regions.c_regions_name =  '{2}';
""".format(c_application_description, c_investment_options_description, c_regions_name)



    def query_nominal_rate(self, start_year):
        """
        
        Parameters
        ----------
        start_year: str
            Start year

        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_economic_basic_parameter.c_economic_basic_parameter_value, 
  tb_economic_basic_parameter.c_economic_basic_parameter_validity_time
FROM 
  public.tb_economic_basics_types, 
  public.tb_economic_basic_parameter
WHERE 
  tb_economic_basics_types.c_economic_basics_types_pk = tb_economic_basic_parameter.c_economic_basic_parameter_type_pk AND
  daterange('{}-01-01', '2018-12-31') && tb_economic_basic_parameter.c_economic_basic_parameter_validity_time AND 
  tb_economic_basic_parameter.c_economic_basic_parameter_scenario = 'S0_historical_data' AND 
  tb_economic_basics_types.c_economic_basics_types_description = 'inflation rate';""".format(int(start_year) + 1)
  
  
    def query_historical_annual_installations(self):
        """
        
        Returns
        -------
        SQL string
        """
        return "SELECT DISTINCT DATE_part('Year', c_stock_initial_operation) , sum(c_stock_parameter_value)  FROM tb_stock2 GROUP BY DATE_part('Year', c_stock_initial_operation) ORDER BY DATE_part('Year', c_stock_initial_operation) "
    
    
    def query_historical_annual_installations_main(self, c_investment_options_description, c_application_description,
                                                   c_regions_name):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_application_description: str
            Application description
        c_regions_name: str
            Regions name

        Returns
        -------
        SQL string
        """
        return """-- Valid for stock parameter equals 'number of annual installations'
SELECT 
  tb_stock.c_stock_value, 
  tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_scenario, 
  tb_stock.c_stock_initial_operation
FROM 
  public.tb_application, 
  public.tb_investment_options, 
  public.tb_relation_investment_option_application, 
  public.tb_stock, 
  public.tb_stock_parameter, 
  public.tb_regions
WHERE 
  tb_application.c_application_pk = tb_stock.c_stock_application_fk AND
  tb_investment_options.c_technology_pfk = tb_stock.c_stock_technology_pfk AND
  tb_relation_investment_option_application.c_application_pfk = tb_application.c_application_pk AND
  tb_relation_investment_option_application.c_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_relation_investment_option_application.c_investment_options_size_pk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investment_option_application.c_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_stock_parameter.c_stock_parameter_pk = tb_stock.c_stock_paramter_pfk AND
  tb_regions.c_regions_pk = tb_stock.c_stock_regions_pfk AND
  tb_stock_parameter.c_stock_parameter_description = 'number of annual installations' AND

-- USER INPUT as variables
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_application.c_application_description = '{1}' AND 
  tb_regions.c_regions_name = '{2}';
""".format(c_investment_options_description, c_application_description, c_regions_name)



    def query_technology_relation(self, c_investment_options_description):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_investment_options.c_technology_pfk, 
  tb_relation_technologies.c_technology_main_pfk, 
  tb_relation_technologies.c_technology_sub_pfk
FROM 
  public.tb_investment_options, 
  public.tb_relation_technologies
WHERE 
  (tb_relation_technologies.c_technology_main_pfk = tb_investment_options.c_technology_pfk OR
  tb_relation_technologies.c_technology_sub_pfk = tb_investment_options.c_technology_pfk )AND
  tb_investment_options.c_investment_options_description = '{0}';""".format(c_investment_options_description)


    def query_historical_annual_installations_sub(self, c_regions_name, c_application_description, tec):
        """
        
        Parameters
        ----------
        c_regions_name: str
            Regions name
        c_application_description: str
            Application description
        tec: str
            technology
        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_stock.c_stock_initial_operation, 
  tb_stock.c_stock_value, 
  tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_paramter_pfk, 
  tb_stock.c_stock_scenario, 
  tb_stock.c_stock_decommissioning
FROM 
  public.tb_stock, 
  public.tb_regions, 
  public.tb_application
WHERE 
  tb_regions.c_regions_pk = tb_stock.c_stock_regions_pfk AND
  tb_application.c_application_pk = tb_stock.c_stock_application_fk AND
-- Variables from the code 
  tb_regions.c_regions_name = '{0}' AND 
  tb_application.c_application_description = '{1}' AND 
  tb_stock.c_stock_technology_pfk = '{2}';""".format(c_regions_name, c_application_description, tec)



    def query_historical_annual_installations_pv(self):
        """
        
        Returns
        -------
        SQL string
        """
        return """-- Valid for stock parameter equals 'installed capacity' 
-- Only valid for scenario 'Germany- installed based on 'Kreisebene' data 
-- Sums up the data for Germany 
-- considers only power plants in operation 
-- queries single power plant data - each power plant accounts for 1 power plant independend on the size 


SELECT 

 DISTINCT (tb_stock.c_stock_initial_operation),
 count(tb_stock.c_stock_value)

FROM 
  public.tb_stock, 
  public.tb_investment_options, 
  public.tb_stock_parameter, 
  public.tb_regions
WHERE 
  tb_investment_options.c_technology_pfk = tb_stock.c_stock_technology_pfk AND
  tb_stock_parameter.c_stock_parameter_pk = tb_stock.c_stock_paramter_pfk AND
  tb_regions.c_regions_pk = tb_stock.c_stock_regions_pfk AND
  tb_investment_options.c_investment_options_description = 'pv' AND 
  tb_stock_parameter.c_stock_parameter_description = 'installed capacity ' AND
  tb_stock.c_stock_scenario = 'Germany_inst' AND
  cast (tb_stock.c_stock_value*1000 as integer)  <@ tb_investment_options.c_investment_options_size_pk AND 
  tb_stock.c_stock_status_fk in ('pp_stat_planned' , 'pp_stat_op') AND
  tb_stock.c_stock_regions_pfk in (Select c_regions_pk from tb_regions where c_regions_pk in (

WITH RECURSIVE source(main ,sub ) AS (
	SELECT character varying '', character varying 'DE1'
	UNION ALL
	SELECT tb_relation_regions.c_regions_main_pfk, tb_relation_regions.c_regions_sub_pfk
	FROM source JOIN tb_relation_regions ON (source.sub=tb_relation_regions.c_regions_main_pfk)
	
)
-- SELECT * from source
SELECT distinct main as combine from source UNION ALL SELECT sub from source ORDER BY combine
)
AND c_regions_level = 'Kreisebene')

GROUP BY 
  tb_stock.c_stock_initial_operation

ORDER BY tb_stock.c_stock_initial_operation"""



    def query_potential(self, c_technology_pfk):
        """
        
        Parameters
        ----------
        c_technology_pfk: str
            technology primary key
        Returns
        -------
        SQL string
        """
        return "SELECT c_potential_value from tb_potential where c_technology_pfk='{}'".format(c_technology_pfk)
    
    
    def query_market_phases(self):
        """
        
        Returns
        -------
        SQL string
        """
        return "SELECT c_market_phase_description, c_market_phase_value from tb_market_phase Order By c_market_phase_pk"
    
    
    def query_technical_lifetime(self, c_investment_options_description, c_technical_characteristics_types_description,
                                 c_technology_characteristics_validity_period_pk):
        """
        
        Parameters
        ----------
        c_investment_options_description: str
            Investment options description
        c_technical_characteristics_types_description: str
            Technical characteristics types description
        c_technology_characteristics_validity_period_pk: str
            Technology characteristics validity period

        Returns
        -------
        SQL string
        """
        return """SELECT 
  tb_technology_characteristics.c_technology_characteristics_value, 
  tb_technology_characteristics.c_technology_characteristics_units_fk
FROM 
  public.tb_technology_characteristics, 
  public.tb_investment_options, 
  public.tb_technical_characteristics_types
WHERE 
  tb_investment_options.c_technology_pfk = tb_technology_characteristics.c_technology_pfk AND
  tb_technical_characteristics_types.c_technical_characteristics_types_pk = tb_technology_characteristics.c_technology_characteristics_types_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_technical_characteristics_types.c_technical_characteristics_types_description = '{1}' AND 
  tb_technology_characteristics.c_technology_characteristics_validity_period_pk = '{2}';""".format(
            c_investment_options_description, c_technical_characteristics_types_description,
            c_technology_characteristics_validity_period_pk)
  
  
    def query_utility_energy_transition(self):
        pass

    def query_utility_grid_independence(self):
        pass
    
    def query_investment_option_alternatives(self,investment_option):
        return """SELECT 
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sub_technology_pfk
FROM 
  public.tb_relation_investment_option_alternatives, 
  public.tb_investment_options
WHERE 
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}';
""".format(investment_option)
    



    def query_importances(self,investment_option,aggregation_level):
        return """-- Query to get the individual or the average importances 
-- options to chose: "individual" or "average" 

SELECT 
  tb_importances.c_importance_respondend_pfk, 
  tb_importances.c_importance_attribute_pfk,
  tb_importances.c_importance_value
FROM 
  public.tb_importances, 
  public.tb_investment_options
WHERE 
  tb_importances.c_importances_technology_pfk = tb_investment_options.c_technology_pfk AND
  tb_importances.c_importances_investment_options_size_pfk = tb_investment_options.c_investment_options_size_pk AND
  tb_importances.c_importances_investment_options_units_pfk = tb_investment_options.c_investment_options_units_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_importances.c_importance_level = '{1}';""".format(investment_option,aggregation_level)
  
  
  
    def query_total_car_stock_w_registration_year(self,investment_option):
      return """
SELECT 
  tb_cars_stock.c_registration_year, 
  tb_cars_stock.c_stock_year, 
  tb_cars_stock.c_number_of_cars
FROM 
  public.tb_cars_stock, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_cars_stock.c_technology_pk AND
  tb_investment_options.c_investment_options_description = '{0}';""".format(investment_option)
  
  
    def query_total_car_stock(self,investment_option):
      return """
  SELECT 
  tb_cars_stock.c_stock_year, 
  sum(tb_cars_stock.c_number_of_cars)
FROM 
  public.tb_cars_stock, 
  public.tb_investment_options
WHERE 
  tb_investment_options.c_technology_pfk = tb_cars_stock.c_technology_pk AND
  tb_investment_options.c_investment_options_description = 'passenger car containing minis, small cars and compact class'
Group by
tb_cars_stock.c_stock_year
ORDER BY tb_cars_stock.c_stock_year ASC
;""" .format(investment_option)


    def query_car_target_system(self,investment_option,car_target_system_scenario):
        return""" 
 SELECT 
  tb_car_target_system.c_car_target_year_pk, 
  tb_car_target_system.c_car_target_value, 
  tb_car_target_system.c_car_target_system_sub_technology_pfk
FROM 
  public.tb_car_target_system, 
  public.tb_investment_options, 
  public.tb_relation_technologies
WHERE 
  tb_investment_options.c_technology_pfk = tb_relation_technologies.c_technology_main_pfk AND
  tb_relation_technologies.c_technology_sub_pfk = tb_car_target_system.c_car_target_system_sub_technology_pfk AND
  tb_investment_options.c_investment_options_description = '{0}' AND 
  tb_car_target_system.c_car_target_scenario_pk = '{1}';""".format(investment_option,car_target_system_scenario)
  

    def query_battery_stock(self,region):
        return  """
    SELECT 
  sum(tb_stock_bat.c_stock_bat_value), 
  tb_stock_bat.c_stock_bat_units_fk,
  tb_stock_bat.c_stock_bat_initial_operation_pk

FROM 
  public.tb_stock_bat
WHERE 
  tb_stock_bat.c_stock_bat_regions_pfk like '{0}%' AND 
  tb_stock_bat.c_stock_bat_scenario_pk = 'S_1_Figgener'
 Group by 
   tb_stock_bat.c_stock_bat_initial_operation_pk, 
   tb_stock_bat.c_stock_bat_units_fk
    """.format(region)


    def query_pv_stock_federal(self,region,size):
        return """
  SELECT 
  sum(tb_stock_pv.c_stock_pv_value), 
  tb_stock_pv.c_stock_pv_units_fk,
  tb_stock_pv.c_stock_pv_initial_operation 

FROM 
  public.tb_stock_pv
WHERE 
  tb_stock_pv.c_stock_pv_status_fk = 'pp_stat_op' AND 
  --tb_stock_pv.c_stock_pv_value <= {1} AND 
  tb_stock_pv.c_stock_pv_regions_federal_pfk = '{0}' AND 
  tb_stock_pv.c_stock_pv_scenario = 'Germany_inst'
 Group by 
   tb_stock_pv.c_stock_pv_initial_operation, 
   tb_stock_pv.c_stock_pv_units_fk;""".format(region,size)
   
    def query_pv_potential_federal(self,region, potential_orientation):
         return """SELECT 
  sum(tb_potential_pv_bat.c_potential_value), 
  tb_potential_pv_bat.c_potential_units_fk
FROM 
  public.tb_potential_pv_bat
WHERE 
  tb_potential_pv_bat.c_potential_scenario_pk = '{1}' AND
  tb_potential_pv_bat.c_potential_regions_federal_fk = '{0}'	
Group by
  tb_potential_pv_bat.c_potential_units_fk;""".format(region, potential_orientation)
  
    def query_pv_stock_germany(self,size):
        return """SELECT 
  sum (tb_stock.c_stock_value), 
  tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_initial_operation
FROM 
  public.tb_stock
WHERE 
  tb_stock.c_stock_status_fk = 'pp_stat_op' AND 
  --tb_stock.c_stock_value <= {0}  AND
  tb_stock.c_stock_scenario='Germany_inst'
Group by
  (tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_initial_operation);""".format(size)
  
    def query_pv_stock_region(self,region,size):
        return """SELECT 
  sum(tb_stock.c_stock_value), 
  tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_initial_operation
FROM 
  public.tb_stock
WHERE 
  tb_stock.c_stock_status_fk = 'pp_stat_op' AND 
  --tb_stock.c_stock_value <= {1} AND 
  tb_stock.c_stock_regions_pfk = '{0}' AND
  tb_stock.c_stock_scenario='Germany_inst'
Group by
  (tb_stock.c_stock_units_fk, 
  tb_stock.c_stock_initial_operation);""".format(region,size)
  
    def query_pv_potential_germany(self):
        return """SELECT 
  sum(tb_potential_pv_bat.c_potential_value),  
  tb_potential_pv_bat.c_potential_units_fk
FROM 
  public.tb_potential_pv_bat
WHERE 
  tb_potential_pv_bat.c_potential_scenario_pk = 'S1_class1_Taumann'
Group by
  tb_potential_pv_bat.c_potential_units_fk;"""
  
  
    def query_pv_potential_region(self,region):
        return """SELECT 
  sum(tb_potential_pv_bat.c_potential_value), 
  tb_potential_pv_bat.c_potential_units_fk
FROM 
  public.tb_potential_pv_bat
WHERE 
  tb_potential_pv_bat.c_potential_scenario_pk = 'S1_class1_Taumann' AND
  tb_potential_pv_bat.c_potantial_regions_pfk = '{0}'	
Group by
  tb_potential_pv_bat.c_potential_units_fk; """.format(region)