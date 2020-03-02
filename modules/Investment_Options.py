import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from modules.Queries import Query
from scipy import interpolate
import matplotlib.patches as mpatches
from scipy.optimize import curve_fit
from scipy import integrate
from sklearn.metrics import r2_score

class Investment_Options():
    """Base class for Investment Options"""

    def __init__(self, folder_name, investment_option, starting_year, DB,db_on,write_data,read_data):

        """
        Investment Options Class constructor

        Parameters
        ----------
        investment_option: str
            Investment Option
        starting_year: str
            Start Year
        DB: DataBase Object
        """
        self.investment_option = investment_option
        self.starting_year = starting_year
        self.DB = DB
        
        self.attribute_sceanrio = None # Default Value
        self.folder_name = folder_name # Comes from test data 

        self.db_on = db_on
        self.write_data = write_data # control variable to write data from DB to csv

        self.read_data = read_data # control variable to read data from csv        

    ##################################################################################################################################
    #-------Utilities----------------------------------------------------------------------------------------------------

    def calculate_utility(self, value_resolution,attribute_sceanrio,aggregation_level,tec_none=True):
        """
        Given the input parameters, it calculates the total annual utility from partial utilities for the given value resolution (average/individual) for the chosen scenario.
        
        Parameters
        ----------
        value_resolution: str
            e.g. average_raw, individual_raw
        attribute_sceanrio: str
            e.g. S1_contra_afv, S1_moderate_afv, S1_pro_afv
        aggregation_level: str
            e.g. average or individual 
        tec_none: Boolean
            True if tec_none option should be considered, otherwise False
        
        Returns
        -------
        utility_alternatives: Pandas.DataFrame() containing the columns [year, alternative, respondend_ID, utility]
        """
        # Reading in data 
        
        if self.db_on:
            alternatives = self.DB.execute_query(Query().query_investment_option_alternatives(self.investment_option)) 
        
        if self.write_data:
            pd.DataFrame(alternatives).to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_investment_option_alternatives.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_investment_option_alternatives.csv')
            alternatives = list(zip(pd.read_csv(path,sep=';')['0']))
            
        
        self.attribute_sceanrio = attribute_sceanrio
        if tec_none == False and 'Class' in self.investment_option:
            idx = alternatives.index(('tec_none',))
            alternatives.pop(idx)
            utility_none_option = None
        print(alternatives)    
        for alternative in alternatives:
            print(alternative)
 
            if 'tec_none' == alternative[0]:
                if self.db_on:
                    utility_none_option = pd.DataFrame(self.DB.execute_query(Query().query_utility_none_option(self.investment_option, value_resolution)))
                    utility_none_option.columns=['attribute','attribute_level','utility_value','respondend','value_resolution']
                
                if self.write_data:
                    utility_none_option.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_utility_none_option.csv'),index=False,sep=';')
                
                if self.read_data:
                    path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_utility_none_option.csv')
                    utility_none_option = pd.read_csv(path,sep=';')
                    
                
            else:
                if self.db_on:
                    attributes = self.DB.execute_query(Query().query_attributes(self.investment_option))
                    attribute_levels = pd.DataFrame(self.DB.execute_query(Query().query_attribute_level_per_year(self.investment_option, attribute_sceanrio)))
                    attribute_levels.columns= ['alternative','year','attribute','attribute_level']
                
                if self.write_data:
                    attribute_levels.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_per_year.csv'),index=False,sep=';')
                
                if self.read_data:
                    path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_per_year.csv')
                    attribute_levels = pd.read_csv(path,sep=';')
                    
                    
                if self.db_on:    
                    attribute_level_putility = pd.DataFrame(self.DB.execute_query(Query().query_attribute_level_putility(self.investment_option, value_resolution)))
                    attribute_level_putility.columns=['attribute','attribute_level','partial_utility_value','respondend','value_resolution']
                
                if self.write_data:
                    attribute_level_putility.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_putility.csv'),index=False,sep=';')
                    
                if self.read_data:
                    path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_putility.csv')
                    attribute_level_putility = pd.read_csv(path,sep=';')
                
                # list of discrete attributes
          
                if self.db_on:
                    discrete_att_list = pd.DataFrame(self.DB.execute_query(Query().query_discrete_attributes(self.investment_option)))
                
                if self.write_data:
                    discrete_att_list.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_discrete_attributes.csv'),index=False,sep=';')
                
                if self.read_data:
                    path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_discrete_attributes.csv')
                    discrete_att_list = pd.read_csv(path,sep=';',header=0)                
                    discrete_att_list.columns = discrete_att_list.columns.astype(int)
                
                discrete_df = attribute_level_putility[attribute_level_putility.attribute.isin(discrete_att_list[0].drop_duplicates())]

                # get dataframe of discrete attribute levels               
                attribute_levels_putility_comb_discrete = pd.merge(attribute_levels,discrete_df,how='inner',on=['attribute','attribute_level'])  
                
                
                
                # Based on investment option (cars, PV-battery), separate continuous attributes from discrete ones.
                continuous_df = attribute_level_putility[~attribute_level_putility.attribute.isin(discrete_att_list[0].drop_duplicates())]
                
                # get dataframe of continuous attribute levels with specific attribute levels to be interpolated.
                attribute_levels_putility_comb_cont = pd.merge(attribute_levels,attribute_levels_putility_comb_discrete,how='left',indicator=True,on=['year','alternative','attribute','attribute_level'])  
                attribute_levels_putility_comb_cont = attribute_levels_putility_comb_cont[attribute_levels_putility_comb_cont['partial_utility_value'].isnull()]
                attribute_levels_putility_comb_cont = attribute_levels_putility_comb_cont.drop(['_merge'],axis=1)
                attribute_levels_putility_comb_cont.reset_index(inplace=True,drop=True)
                
                attribute_levels_putility_comb_cont_dummy = attribute_levels_putility_comb_cont.copy(deep=True)
                
                print("interpolating...")
                cont_att_functions = {}
                attribute_levels_putility_comb_cont_df_list = []
                attributes = continuous_df['attribute'].drop_duplicates().values
                for i, respondend in enumerate(attribute_level_putility.respondend.drop_duplicates().values):

                    if respondend not in cont_att_functions:
                        cont_att_functions[respondend]={}
                    for attribute in attributes:
                        x = continuous_df[(continuous_df['attribute']==attribute)&(continuous_df['respondend']==respondend)]['attribute_level'].values
                        if attribute != 'att_pp_IRR':
                            x = [float(i) for i in x]

                        else: 
                            x = [5,10,15,20]
                        y = continuous_df[(continuous_df['attribute']==attribute)&(continuous_df['respondend']==respondend)]['partial_utility_value'].values
    
                        # fit an interpolating function to continuous attributes
                        cont_att_functions[respondend][attribute] = interpolate.interp1d(x, y)

               

                    # interpolate using the fitted interpolated functions
                    for index in range(0,len(attribute_levels_putility_comb_cont_dummy)):                        
                        y = cont_att_functions[respondend][attribute_levels_putility_comb_cont_dummy.iloc[index]['attribute']](attribute_levels_putility_comb_cont_dummy.iloc[index]['attribute_level'])
                        attribute_levels_putility_comb_cont_dummy.loc[index,'partial_utility_value'] = y
                        attribute_levels_putility_comb_cont_dummy.loc[index,'respondend'] = respondend
                        attribute_levels_putility_comb_cont_dummy.loc[index,'value_resolution'] = value_resolution
                    
                    attribute_levels_putility_comb_cont_df_list.append(attribute_levels_putility_comb_cont_dummy.copy(deep=True))

                attribute_levels_putility_comb_cont = pd.concat(attribute_levels_putility_comb_cont_df_list)

        
        # combining the data to get a joint data frame 
        attribute_levels_putility_comb = pd.concat([attribute_levels_putility_comb_cont,attribute_levels_putility_comb_discrete])

        print("Calculating utilities...")
        
        # total utility is the sum of all partial utilities. 
        
        attribute_levels_putility_comb.partial_utility_value = attribute_levels_putility_comb.partial_utility_value.apply(pd.to_numeric,errors='ignore')
        grouped = attribute_levels_putility_comb.groupby(['year','alternative','respondend'])

        utility_alternatives = grouped['partial_utility_value'].agg(np.sum).reset_index()
        utility_alternatives.columns  = ['year', 'alternative', 'respondend', 'utility']
        utility_alternatives["probability"] = -1
        
        if tec_none:
            xx = utility_none_option.assign(foo=1).merge(utility_alternatives['year'].drop_duplicates().to_frame().assign(foo=1)).drop(['attribute_level','attribute','value_resolution','foo'],axis=1)
            xx['probability'] = -1
            xx['alternative'] = 'tec_none'
            xx.columns = ['utility', 'respondend', 'year', 'probability', 'alternative']
            xx.reindex(columns=['year', 'alternative', 'respondend', 'utility','probability'])
            utility_alternatives = pd.concat([xx,utility_alternatives])
        utility_alternatives = utility_alternatives.sort_values(by=['year','alternative','respondend']).reset_index(drop=True)


        
        utility_alternatives.to_csv(os.path.join(os.getcwd() , 'results',self.folder_name,'utility_alternatives.csv'),index=False)
        
        return utility_alternatives
    
    ##################################################################################################################################
    #-------DECISION PROBABILITIES----------------------------------------------------------------------------------------------------         

    def calculate_logit_probabilities(self,utility_alternativesl,main_sub):
        """
        euqation to calculate logit probabilities 
        
        Parameters
        ----------
        utility_alternativesl: pandas.DataFrame()
            Pandas dataframe containing columns [year, alternative, respondend_ID, utility, 'probability'] from calculate_utility()
        
        main_sub: dict
            defined sub-groups of respondends accoring to individual data (e.g. main_sub = {'gender':'female','gr_coll_eff_median':'high'})
            
        Returns
        -------
            tb_probabilities_alternatives: pandas.DataFrame() containing the columns [year, alternative, respondend_ID, utility, probability] 
            preference_share.png: graph of probabilities for each alternative per year
        """
        utility_alternatives = utility_alternativesl.copy(deep=True)
        
        # individual respondends can be categorised into main and sub categories. e.g. gender is a main and female is a sub-category.
        
        df_filter = pd.DataFrame()
        for main,sub in main_sub.items():
            
            if self.db_on:
                df_sub = pd.DataFrame(self.DB.execute_query(Query().query_sub_group(main,sub,self.investment_option)))
            
            if self.write_data:
                    df_sub.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_group.csv'),index=False,sep=';')
                    
            if self.read_data:
                path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_group.csv')
                df_sub = pd.read_csv(path,sep=';')
            
            
            if df_filter.empty:
                df_filter = df_sub.copy(deep=True)
            df_filter = pd.merge(df_filter,df_sub,how='inner')
        if len(main_sub) != 0:
            utility_alternatives = utility_alternatives[utility_alternatives.respondend.isin(list(np.ravel(df_filter.values)))].dropna().reset_index(drop=True)
        
        print('Number of Sample = {0}'.format(utility_alternatives.respondend.drop_duplicates().count()))
        
        print("Calculating logit probabilities...")
        
        
        # Calculating logit probabilities
        
        # probability for alternative x = np.exp(x) / sum of all N alternatives i.e. np.exp(alternative 1) +np.exp(alternative 2) + ...+ np.exp(alternative N)
        
        grouped = utility_alternatives.groupby(['year','respondend'])
        utility_alternatives['num'] = utility_alternatives['utility'].astype(float).apply(np.exp)
        x = grouped['num'].agg(np.sum).reset_index()
        y = utility_alternatives.merge(x,how='left',on= ['year','respondend'])
        utility_alternatives['probability'] = y['num_x'] / y['num_y'] 
        ua = utility_alternatives.apply(pd.to_numeric,errors='ignore')
        tb_prob_alternatives = ua.groupby(['year','alternative'],as_index=False).mean()[['year','alternative','probability']]
        
        x = pd.pivot_table(tb_prob_alternatives,values=['probability'],index='year',columns=['alternative'])
        x = x[x.columns[::-1]]
        
        if self.investment_option != 'photovoltaik and battery storage sysem on single familiy and row houses ':
            tuples = [('probability', 'tec_cv'), ('probability', 'tec_bev'),('probability', 'tec_fcev')]
            x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
        
        color_dict = {'tec_fcev':'#1c86ee','tec_cv':'#a1a1a1','tec_bev':'#ffb90f','tec_pv_plus_battery':'#ffb90f','tec_none':'#a1a1a1'}
        colors = []
        for c in x:
            if c[1] in color_dict:
                colors.append(color_dict[c[1]])
            else:
                colors.append('black')

        ax2 = x.plot.area(y='probability', stacked=True,fontsize=30,title='Logit Probabilities {0}'.format(main_sub),color=colors)
        ax2.set_xlabel('Time [Years]', fontsize=30)
        ax2.title.set_size(30)
        ax2.figure.set_size_inches(18.5, 10.5)
        
        if self.investment_option == 'photovoltaik and battery storage sysem on single familiy and row houses ':
            colors =['#a1a1a1','#ffb90f']
            texts = ['No Investment', 'PV and battery system on single family and row houses']
            patches = []
            patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
            patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1])) )
        else:
            colors =['#a1a1a1','#ffb90f','#1c86ee']
            texts = ['diesel/gasoline', 'battery electric vehicles', 'fuel cell electric vehicel']
            patches = []
            patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
            patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1])) )
            patches.append(mpatches.Patch(color=colors[2], label="{:s}".format(texts[2])) )

        
        plt.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        ax2.figure.savefig(os.path.join(os.getcwd(),'results',self.folder_name,'preference_share.png'))
        tb_prob_alternatives.to_csv(os.path.join(os.getcwd(),'results',self.folder_name, r'tb_prob_alternatives.csv'),index=False)

        return tb_prob_alternatives, df_filter
        
    def calculate_first_choice(self,utility_alternatives,main_sub):
        """
        euqation to calculate first choice probabilities 
        
        Parameters
        ----------
        utility_alternativesl: pandas.DataFrame()
            Pandas dataframe containing columns [year, alternative, respondend_ID, utility, 'probability'] from calculate_utility()
        
        main_sub: dict
            defined sub-groups of respondends accoring to individual data (e.g. main_sub = {'gender':'female','gr_coll_eff_median':'high'})

        Returns
        -------
        tb_probabilities_alternatives: pandas.DataFrame() containing the columns [year, alternative, respondend_ID, utility, probability] 
        
        preference_share.png: graph of probabilities for each alternative per year
        """
        print("Calculating first choice probabilities...")
        
        # First choice probability is calculated the following way
        # 1. for each respondend, maximum utility of all of its alternatives is set to 1 and other alternatives are set to zero.
        # 2. probability for the alternative = sum of all 1's / number of respondend.
        # 
        
        # Example: given following utilities for each alternative
        
        #   Respondend  alternative#1   alternative#2   alternative#3
        #   1           2.5             2               1.5 
        #   2           1               1.5             0.7
        #   3           0               1               0.7
        
        #   convert the above table to following
        
        #   Respondend  alternative#1   alternative#2   alternative#3
        #   1           1               0               0 
        #   2           0               1               0
        #   3           0               1               0
        
        # Probability:  1/3             2/3             0/3
        
        utility_alternatives = utility_alternatives.copy(deep=True)
        
        df_filter = pd.DataFrame()
        for main,sub in main_sub.items():
            if self.db_on:
                df_sub = pd.DataFrame(self.DB.execute_query(Query().query_sub_group(main,sub)))
            if self.write_data:
                    df_sub.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_group.csv'),index=False,sep=';')
                    
            if self.read_data:
                path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_group.csv')
                df_sub = pd.read_csv(path,sep=';')
                
            if df_filter.empty:
                df_filter = df_sub.copy(deep=True)
            df_filter = pd.merge(df_filter,df_sub,how='inner')
        if len(main_sub) != 0:
            utility_alternatives = utility_alternatives[utility_alternatives.respondend.isin(list(np.ravel(df_filter.values)))].dropna().reset_index(drop=True)
        
        print('Number of Sample = {0}'.format(utility_alternatives.respondend.drop_duplicates().count()))
        
        
        years = utility_alternatives.year.drop_duplicates().values
        alternatives = utility_alternatives.alternative.drop_duplicates()  
        
        df_rearranged = pd.pivot_table(utility_alternatives, values='utility', index=['year', 'respondend'],columns=['alternative'], aggfunc=np.sum).reset_index()
        tb_prob_alternatives = pd.DataFrame(columns=['year'] + list(alternatives.values ))
        
        for year in years:
            temp = df_rearranged[df_rearranged.year==year]
            if len(temp) == 1:
                x = temp.iloc[:,2:len(alternatives)+2].astype(float).idxmax(axis=1).value_counts()
                x = x/x.sum(axis=0)
                for alt in alternatives:
                    if alt not in x:
                        x[alt] = 0
            else:
                x = temp.iloc[:,2:len(alternatives)+2].astype(float).idxmax(axis=1).value_counts()
                x = x/x.sum(axis=0)
            t = {'year':str(year)}
            t.update(dict(x))
            tb_prob_alternatives = tb_prob_alternatives.append(t,ignore_index=True)
        
        first_choice_prob  = pd.DataFrame(columns=['year','alternative','probability'])   

        for year in years:
            for alternative in alternatives:
                first_choice_prob = first_choice_prob.append({'year':year,'alternative':alternative,'probability':tb_prob_alternatives[(tb_prob_alternatives.year==str(year))][alternative].values[0]},ignore_index=True)

        x = pd.pivot_table(first_choice_prob,values=['probability'],index='year',columns=['alternative'])
        x = x[x.columns[::-1]]
        
        tuples = x.columns.tolist()
        for item in tuples:
            if ('probability', 'tec_cv') == item:
                old_index = tuples.index(('probability', 'tec_cv')) 
                tuples.insert(0, tuples.pop(old_index))

        x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
        
        color_dict = {'tec_fcev':'#1c86ee','tec_cv':'#a1a1a1','tec_bev':'#ffb90f'}
        colors = []
        for c in x:
            if c[1] in color_dict:
                colors.append(color_dict[c[1]])
            else:
                colors.append('black')
                
        if self.db_on:
            labels = []        
            for tec in x.columns.levels[1]:
                
                labl = self.DB.execute_query(Query().query_technologies_name(tec))[0][0]
                labels.append(labl)
        if self.write_data:
            pd.DataFrame(labels).to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'labels.csv'),index=False,sep=';')   
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'labels.csv')
            labels = list(pd.read_csv(path,sep=';')['0'])
            
        ax2 = x.plot.area(y='probability', stacked=True,fontsize=30,title='First Choice Probabilities',color=colors)
        ax2.set_ylabel('Preference Share [%]', fontsize=30)
        ax2.set_xlabel('Time [Years]', fontsize=30)
        ax2.title.set_size(30)
        ax2.legend(labels, fontsize=30)
        ax2.figure.set_size_inches(18.5, 10.5)
        ax2.figure.savefig(os.path.join(os.getcwd(),'results',self.folder_name,'preference_share.png'))

        first_choice_prob.to_csv(os.path.join(os.getcwd(),'results',self.folder_name,r'first_choice_prob.csv'),index=False)
        
        return first_choice_prob,utility_alternatives

             
    ##################################################################################################################################
    #-------WEIBULL FUNCTIONS--------------------------------------------------------------------------------------------------------- 
    
    # Definition of Weibull density and distribution function
    

    def pdf_weibull(self,t,T,b):
        """
        Weibull Density function
        
        Parameters
        ----------        
        t: random parameter (car age)
        
        T: location parameter
            
        b: form parameter
        
        Returns
        -------
        Outage probability
        """
        return (b / T) * (t / T)**(b - 1) * np.exp(-(t / T)**b)
    
            
    def cdf_weibull(self,t,T,b):
        """
        Weibull Distribution function
        
        Parameters
        ----------        
        t: random parameter (car age)
        
        T: location parameter
            
        b: form parameter
        
        Returns
        -------
        Cumulated outages
        """
        return np.exp(-((t/T)**b))  

    
    def pdf_weibull_fit(self,t,T,b):
        """
        Weibull Density function adapted 
        
        Parameters
        ----------        
        t: random parameter (car age)
        
        T: location parameter
            
        b: form parameter
        
        Returns
        -------
        Outage probability with a cut at 30 years 
        """
        
        if t > 29: 
            return 0
        else:
            return (b / T) * (t / T)**(b - 1) * np.exp(-(t / T)**b)
          
    
  
    ##################################################################################################################################
    #-------STOCK CALCULATION---------------------------------------------------------------------------------------------------------  
    def stock_model(self, probabilities,growth_scenario,average_passenger_kilometers,specific_consumption_scenario,specific_emissions_electricity_mix_scenario,specific_emissions_scenario):
        """
        function to calculate change in stock from 2018 to 2050 and estimates CO2-emissions; valid for passenger cars
        
        Parameters
        ----------
        tb_prob_alternatives: Pandas DataFrame()
            tb_probabilities_alternatives: pandas.DataFrame() containing the columns [year, alternative, respondend_ID, utility, probability] (result from robability calculation)
            
        growth_scenario: str (for query)
            growth_scenario = 'S_constant' result in query_car_stock_scenario -> assumption on percentage car stock change (e.g. 0.01 - 1% growth per year; -0.01 - 1% decrease per year)
        
        average_passenger_kilometers: numeric
            specified in test.py
        
        specific_consumption_scenario: str (for query)
            (e.g specific_consumption_scenario = 'S_base') 
        
        specific_emissions_electricity_mix_scenario: str (for query)
            (e.g. specific_emissions_electricity_mix_scenario = 'S_95_Reduction')
            
        specific_emissions_scenario
            (e.g. specific_emissions_scenario = 'S_emissions_calibrated_low')
        
        Returns
        -------
        car_stock: Pandas DataFrame() 
            Dataframe containing following columns [reg_year, stock_year,num_cars, age, prob_out, total_outages, share_tec_bev, share_tec_cv, share_tec_fcev, tec_bev, tec_cv, tec_fcev,
            outage_tec_bev, outage_tec_cv,outage_fcev, emission_tec_cv, sp_emissions_tec_cv, consumption_tec_bev, consumption_tec_fcev, emissions_el_mix, emissions_BEV, emissions_FCEV]
        
        stock_sum: Pandas DataFrame() 
            Dataframe containing following columns [year, tec_bev, tec_cv, tec_fcev, total_number_of_cars, share_tec_bev, share_tec_cv, share_tec_fcev, stock_next_year, 
            outage_tec_bev, outage_tec_cv,outage_fcev, sum_outages, sum_new_cars_next_year, new_cars_ny_tec_bev,  new_cars_ny_tec_cv,new_cars_ny_tec_fcev]
            
        CO2_emissions: Pandas DataFrame() 
            Dataframe containing following columns [year,emissions_CV, emissions_BEV, emissions_FCEV]
            
            
        """

        # 1) Calculation of the outage probability to pass out Weibull 
        #####################################

        # data input 
        if self.db_on:
            x = pd.DataFrame(self.DB.execute_query("""SELECT * FROM public.tb_cars_stock where c_technology_pk = 'tec_car'"""))
            x.columns = ['technology','registeration_year','stock_year','num_cars','sources','quality','date','modifier']

        if self.write_data:
            x.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_stock.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_stock.csv')
            x = pd.read_csv(path,sep=';')
        
        
        x_pivot = pd.pivot_table(x, values='num_cars', index=['registeration_year'],columns=['stock_year']).reset_index()
        
        prob_tb = pd.DataFrame()
        for ind, column in enumerate(x_pivot.columns[::-1]):
            #y[column] =x_pivot[column]
            col_name = x_pivot.columns[-ind]
            if ind == 0:
                prob_tb[col_name] = x_pivot[col_name]
            elif ind < len(x_pivot.columns)-1:
                prob_tb[col_name] = x_pivot[col_name] / x_pivot[x_pivot.columns[-ind-1]] 
                
        prob_tb = prob_tb.drop('registeration_year',axis=1)
        
        na_idx = prob_tb.isnull().sum(axis = 0).values
        
        for idx, col in enumerate(prob_tb):
            prob_tb[col]= prob_tb[col].shift(na_idx[idx])
            
        pdf = 1- prob_tb.mean(axis=1)#/prob_tb.sum(axis=1).sum()
        pdf = pdf.dropna()
        pdf = pd.DataFrame(pdf)
        t = x_pivot['registeration_year'].values[-1] - x_pivot['registeration_year'] + 1
        pdf['alter'] = pd.DataFrame(t.astype(int))
        
        pdf=pdf[pdf.alter<30]
        t = pd.DataFrame(pdf.alter.copy())
        
        pdf=pdf.drop(['alter'],axis=1)
        pdf = pdf / pdf.sum()
        cdf = pdf.cumsum().dropna()
        
        
        t = np.ravel(t.values)
        pdf = np.ravel(pdf.values)
        cdf = np.ravel(cdf.values)
        ym=pdf

        # Random guess of starting parameters
        p0= [5,4]
        
        # Fit of curve
        c,cov=curve_fit(self.pdf_weibull,t,ym,p0)
        
        # Predict values using the coefficients of the fit above
        yp=self.pdf_weibull(t, c[0],c[1])

        # Print the R2
        print('R^2 = '+ str(r2_score(ym,yp)))

        plt.figure()
        #Plot the results
        plt.plot(t,ym, 'ro')
        plt.plot(t,yp)
        plt.ylabel('outage probability', fontsize=30)
        plt.xlabel('years after initial registration', fontsize=30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.show()
        
        plt.figure()
        #Plot the results
        plt.plot(t,self.cdf_weibull(t,c[0],c[1]))
        plt.plot(t,cdf, 'ro')
        plt.ylabel('probability to survive', fontsize=30)
        plt.xlabel('years after initial registration', fontsize=30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.show()
        
        #####################################

        ###### Calculation for the first year 
        
        # Reduction of the total car stock according to the shares (class share, investor share and ) 
        # Shares of the different car classes         
        if self.db_on:
            car_class_share = pd.DataFrame(self.DB.execute_query(Query().query_car_class_share(self.investment_option)))
            print(car_class_share)
        if self.write_data:
            car_class_share.to_csv(os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_car_class_share.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_car_class_share.csv')
            car_class_share = pd.read_csv(path,sep=';',header=0)
            car_class_share.columns = car_class_share.columns.astype(int)     
        
        # Shares of the investor
        if self.db_on:
            investor_stock_share = pd.DataFrame(self.DB.execute_query(Query().query_investor_stock_share(self.investment_option)))
        if self.write_data:
            investor_stock_share.to_csv(os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_investor_stock_share.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_investor_stock_share.csv')
            investor_stock_share = pd.read_csv(path,sep=';',header=0)
            investor_stock_share.columns = investor_stock_share.columns.astype(int)
            
        # Total number of cars per sub-technology
        if self.db_on:
            stock_sum = pd.DataFrame(self.DB.execute_query(Query().query_sub_technology_share(self.investment_option)))                    
            stock_sum.columns = ['year','stock','alternative']
        
        if self.write_data:
            stock_sum.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_technology_share.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_sub_technology_share.csv')
            stock_sum = pd.read_csv(path,sep=';')
            
        # Reduction by car class and investor
        stock_sum['stock'] = stock_sum['stock'].astype(float) * float(investor_stock_share[0][0]) * float(car_class_share[0][0])
        
        # Identification of vehicle types (BEV, FCEV and CV)
        alternatives = stock_sum.alternative.drop_duplicates()
        # Create data table with year, alternative, total number of cars, outages, new car stock and total number of new cars and number of cars per vehicle type
        stock_sum = pd.pivot_table(stock_sum, values='stock', index=['year'],columns=['alternative'], aggfunc=np.sum)
        stock_sum['total_number_of_cars'] = stock_sum[alternatives].sum(axis=1)
        #print(stock_sum)
        
        # append columns for share per type
        col = []
        for alternative in alternatives:
            col.append('share_' + alternative)
        for co in col:
            stock_sum[co] = 0
            
        for alternative in alternatives:
            stock_sum.loc[:,'share_' + alternative] =  stock_sum.loc[:,alternative].astype(float) / stock_sum.loc[:,'total_number_of_cars'].astype(float)
            
        # append columns for number of cars in the next year 
        stock_sum["stock_next_year"] = 0
        
        col = []
        for alternative in alternatives:
            col.append('outage_' + alternative)
        
        # Create second data table for the car stock containing the registration year (starting with the oldest car year)
        init_year = stock_sum.index.max()
        if self.db_on:
            car_stock = pd.DataFrame(self.DB.execute_query(Query().query_stoc_init_year(self.investment_option,init_year)))
            car_stock.columns=['reg_year','stock_year','num_cars']
        
        if self.write_data:
            car_stock.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_stoc_init_year.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_stoc_init_year.csv')
            car_stock = pd.read_csv(path,sep=';')
            
            
        # Reduction according to the investor share and car class share 
        car_stock['num_cars'] = car_stock['num_cars'].astype(float) * float(investor_stock_share[0][0]) * float(car_class_share[0][0])
        # Calculate the age of the car (t)
        car_stock["age"] = car_stock["stock_year"] - car_stock["reg_year"]
              
        # make copy of stock sum to take values for 2018 
        stock_sum_copy = stock_sum.copy()
        
        # Calculate the outage probability in dependence of the age of the cars, according to Weibull (when cart is older than 30 years the outage probability is 1)        
        p = []        
        car_stock["prob_out"] = 0       
        for x in car_stock["age"]:
            temp = self.pdf_weibull_fit(x, c[0],c[1])
            p.append(temp)
        car_stock["prob_out"] = p 
        car_stock.loc[car_stock["age"] >= 30,'prob_out'] = 1
      
        # Calculation of the outages as the product of of outage probability * number of cars 
        car_stock["total_outages"] = car_stock["prob_out"] * car_stock["num_cars"]

        # append columns for stock shares per vehicle type    
        col = []
        for alternative in alternatives:
            col.append('share_' + alternative)
        for co in col:
            car_stock[co] = 0
            
        #  if registration year < 2009 (is the min Index of sub_technology share) the share for CV is 100%
        #  for registration year >= 2009 it is the share based on tb_stock_sums 
     
        for alternative in alternatives:
            if alternative == 'tec_cv':
                car_stock.loc[car_stock.reg_year < stock_sum.index.min(),'share_' + alternative] = 1
            car_stock.loc[(stock_sum.index.min() <= car_stock.reg_year) & (car_stock.reg_year <= stock_sum.index.max()) ,'share_' + alternative] = stock_sum.loc[stock_sum.index.min():stock_sum.index.max()-1 ,'share_' + alternative].values

        # append columns for total number of cars per type
        col = []
        for alternative in alternatives:
            col.append(alternative)
        for alternative in alternatives:
            car_stock.loc[:,alternative] = car_stock.loc[:,'share_' + alternative] * car_stock.loc[:,'num_cars']
        
        # append columns for outage per type
        col = []
        for alternative in alternatives:
            col.append('outage_' + alternative)
        for co in col:
            car_stock[co] = 0   

        # calculate for all alternatives the number of outages_alternative (based on the alternative shares)
        for alternative in alternatives:
            car_stock.loc[:,'outage_'+alternative] = car_stock.loc[:,'share_'+alternative] * car_stock.loc[:,'total_outages']

            car_stock.loc[car_stock['outage_'+alternative]>car_stock[alternative],'outage_'+alternative] = car_stock.loc[car_stock['outage_'+alternative]>car_stock[alternative],alternative]

        # integrate value from database as new stock value 
        stock_sum.loc[init_year,'stock_next_year'] = stock_sum_copy.loc[init_year,'total_number_of_cars']
        
        
        # add sum per vehicle type from car stock into stock_sums 
        for alternative in alternatives:
            stock_sum.loc[init_year,alternative] = car_stock.loc[car_stock["stock_year"] == init_year,'num_cars'].sum() * stock_sum.loc[init_year,'share_'+alternative]
      
        # calculate total number of cars as the sum       
        temp_sum = 0
        for alternative in alternatives:
            temp_sum += stock_sum.loc[init_year,alternative]
            stock_sum.loc[init_year,'total_number_of_cars'] = temp_sum
            
        # append columns for outage per type in stock_sum table
        col = []
        for alternative in alternatives:
            col.append('outage_' + alternative)
        for co in col:
            stock_sum[co] = 0   
        
        for alternative in alternatives:
            stock_sum.loc[stock_sum['outage_'+alternative]>stock_sum[alternative],'outage_'+alternative] = stock_sum.loc[stock_sum['outage_'+alternative]>stock_sum[alternative],alternative]
        # integrate the outages for the init_year into the stock_sum_table
        for alternative in alternatives:
            stock_sum.loc[init_year,'outage_' + alternative] = car_stock.loc[car_stock["stock_year"] == init_year,'outage_' + alternative].sum() 
        
        # calculate sum of outages 
        stock_sum["sum_outages"] = 0
        temp_sum = 0
        for alternative in alternatives:
            temp_sum += stock_sum.loc[init_year,'outage_' + alternative]
            stock_sum.loc[init_year,'sum_outages'] = temp_sum
        
        stock_sum["sum_new_cars_next_year"] = 0
        # append columns for new cars per type
        
        stock_sum.loc[init_year,"sum_new_cars_next_year"] = stock_sum.loc[init_year,'stock_next_year'] - stock_sum.loc[init_year,'total_number_of_cars'] + stock_sum.loc[init_year,'sum_outages']
        
        col = []
        for alternative in alternatives:
            col.append('new_cars_ny_' + alternative)
        for co in col:
            stock_sum[co] = 0
        
        for alternative in alternatives:
            stock_sum.loc[:,'new_cars_ny_' + alternative]=0
            stock_sum.loc[init_year,'new_cars_ny_' + alternative] = float(stock_sum_copy.loc[init_year,alternative])  - stock_sum.loc[init_year,alternative] + stock_sum.loc[init_year,'outage_' + alternative]
            
        ####### Calculation loop for the following years 

        for y in range(init_year+1, 2051):
            #copy car stock table from previous year subset, only previous year for copy
            car_stock_2 = car_stock.copy()
            car_stock_2 = car_stock_2.loc[car_stock.stock_year == y-1] 

            car_stock_2.loc[:,'stock_year']= y
            # substract outages from previous year 
            car_stock_2.loc[:,'num_cars'] = car_stock_2.loc[:,'num_cars'] - car_stock_2.loc[:,'total_outages']
            # Integrate the new cars from previous year 
            car_stock_2.loc[car_stock_2.index.max()+1,'reg_year'] = y-1 
            car_stock_2.loc[car_stock_2.index.max(),'stock_year'] = y
            car_stock_2.loc[car_stock_2.index.max(),'num_cars'] = stock_sum.loc[stock_sum.index.max(),'sum_new_cars_next_year']
            for alternative in alternatives:
                car_stock_2.loc[car_stock_2.index.max(),'share_' + alternative]= stock_sum.loc[stock_sum.index.max(),'share_' + alternative]
            
            # append columns for total umber of cars per type
            col = []
            for alternative in alternatives:
                col.append(alternative)
            for alternative in alternatives:
                car_stock_2.loc[:,alternative] = car_stock_2.loc[:,'share_' + alternative] * car_stock_2.loc[:,'num_cars']
            
            # calculate age 
            car_stock_2["age"] = car_stock_2["stock_year"] - car_stock_2['reg_year']
            
            p = []        
            car_stock_2["prob_out"] = 0       
            for x in car_stock_2["age"]:
                temp = self.pdf_weibull_fit(x, c[0],c[1])
                p.append(temp)
            car_stock_2["prob_out"] = p 
            car_stock_2.loc[car_stock_2["age"] >= 30,'prob_out'] = 1
                   
            # Calculation of the outages as the product of of outage probability * number of cars 
            car_stock_2["total_outages"] = car_stock_2["prob_out"] * car_stock_2["num_cars"]
            
            # calculate for all alternatives the number of outages_alternative (based on the alternative shares)
            for alternative in alternatives:
                car_stock_2.loc[:,'outage_'+alternative] = np.floor(car_stock_2.loc[:,'share_'+alternative] * car_stock_2.loc[:,'total_outages'])
                car_stock_2.loc[car_stock_2['outage_'+alternative]>car_stock_2[alternative],'outage_'+alternative] = car_stock_2.loc[car_stock_2['outage_'+alternative]>car_stock_2[alternative],alternative]
            # append car_stock and car_stock 2 
            car_stock = car_stock.append(car_stock_2,ignore_index=True)
    
            # Calculate the stock sums 
            for alternative in alternatives:
                stock_sum.loc[y,alternative] = float(stock_sum.loc[y-1,alternative]) - float(stock_sum.loc[y-1,'outage_' +alternative]) + float(stock_sum.loc[y-1,'new_cars_ny_' + alternative])
    
            # Calculate the total number of cars 
            temp_sum = 0
            for alternative in alternatives:
                temp_sum += stock_sum.loc[y,alternative]
            stock_sum.loc[y,'total_number_of_cars'] = temp_sum
            
            # calculate the shares 
            for alternative in alternatives:
                stock_sum.loc[y,'share_' + alternative] =  stock_sum.loc[y,alternative] / stock_sum.loc[y,'total_number_of_cars']
    
            # calculate new car share 
            if self.db_on:
                growth_rate = pd.DataFrame(self.DB.execute_query(Query().query_car_stock_scenario(self.investment_option,growth_scenario)))
            
            if self.write_data:
                growth_rate.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_car_stock_scenario.csv'),index=False,sep=';')
        
            if self.read_data:
                path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_car_stock_scenario.csv')
                growth_rate = pd.read_csv(path,sep=';')
                growth_rate.columns = growth_rate.columns.astype(int)

            stock_sum.loc[y ,"stock_next_year"] = float(1.0 +float(growth_rate[0][0])) * float(stock_sum.loc[y ,"total_number_of_cars"])
            
            # calculate outages per type as sum of the car_stock table 
            for alternative in alternatives:
                stock_sum.loc[y ,"outage_" + alternative]  = car_stock_2.loc[:,'outage_' + alternative].sum()    
            
            for alternative in alternatives:
                stock_sum.loc[stock_sum['outage_'+alternative]>stock_sum[alternative],'outage_'+alternative] = stock_sum.loc[stock_sum['outage_'+alternative]>stock_sum[alternative],alternative]
        
            
            # calculate sum of outages 
            temp_sum = 0
            for alternative in alternatives:
                temp_sum += stock_sum.loc[y,'outage_' + alternative]
            stock_sum.loc[y,'sum_outages'] = temp_sum
            
            # calculate sum of new cars for next year 
            stock_sum.loc[y,"sum_new_cars_next_year"] = stock_sum.loc[y,'stock_next_year'] - stock_sum.loc[y,'total_number_of_cars'] + stock_sum.loc[y,'sum_outages']
            
            # calculate shares for new cars 
            for alternative in alternatives:
                stock_sum.loc[y,"new_cars_ny_" + alternative] = probabilities[(probabilities.year==y)&(probabilities.alternative==alternative)].probability.values[0] * stock_sum.loc[y ,"sum_new_cars_next_year"]


        alternatives = list(alternatives)
        
        if 'tec_cv' in alternatives:
            old_index = alternatives.index('tec_cv') 
            alternatives.insert(0, alternatives.pop(old_index))
        x = stock_sum[alternatives].astype(float)# angabe in millionen
        print(list(alternatives))
        #plt.figure(figsize=(20,20))
           
        for cc in x:
            x[cc] = x[cc]/1000000
        ax2 = x.plot.area(y=alternatives, fontsize=30, color=['#a1a1a1','#ffb90f','#1c86ee'],linewidth=0, title='Total car stock')
        ax2.title.set_size(30)
        colors =['#a1a1a1','#ffb90f','#1c86ee','#7A7A7A','#CD950C','#104E8B']
        texts = ['diesel/gasoline', 'battery electric vehicles', 'fuel cell electric vehicel','target diesel/gasoline', 'target battery electric vehicles', 'target fuel cell electric vehicel']
        
        patches = []
        
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1]) ) )
        patches.append(mpatches.Patch(color=colors[2], label="{:s}".format(texts[2]) ) )
        ax2.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        
        
        ax2 = x.plot.area(y=alternatives,title='Market share of private passenger cars ({0})'.format(self.investment_option), fontsize=30, color=['#a1a1a1','#ffb90f','#1c86ee'],linewidth=0)                  
        ax2.title.set_size(30)
        
        colors =['#a1a1a1','#ffb90f','#1c86ee','#7A7A7A','#CD950C','#104E8B']
        texts = ['diesel/gasoline', 'battery electric vehicles', 'fuel cell electric vehicel','target diesel/gasoline', 'target battery electric vehicles', 'target fuel cell electric vehicel']
        
        patches = []
        
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1]) ) )
        patches.append(mpatches.Patch(color=colors[2], label="{:s}".format(texts[2]) ) )
        plt.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        ax2.set_ylabel('Number of Cars (millions)', fontsize=30)
        ax2.set_xlabel('Time [Years]', fontsize=30)
       
        
        stock_sum.to_csv(os.path.join(os.getcwd(),'results',self.folder_name, 'stock_sum.csv'),sep=';')
        ax2.figure.set_size_inches(18.5, 10.5)
        
        
        
        ax2.figure.savefig(os.path.join(os.getcwd(),'results', self.folder_name, 'stock.png'))
        if self.db_on:
            car_target = pd.DataFrame(self.DB.execute_query(Query().query_car_target_value(self.investment_option,'S1b90_IEK_frei_v71')))
        
        if self.write_data:
            car_target.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_car_target_value.csv'),index=False,sep=';')
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_car_target_value.csv')
            car_target = pd.read_csv(path,sep=';',header=None)
            
        car_target[[0]]= car_target[[0]].astype(float)
        car_target[[1]]= car_target[[1]].astype(float)
        
        car_target = pd.pivot_table(car_target, values=0, index=[1],columns=[2], aggfunc=np.sum)
        car_target = car_target.div( car_target.sum(axis=1),axis=0)
        car_target = car_target[alternatives]#.cumsum(axis=1)
        
        x_normalised = x.copy()
        
        for cc in x_normalised:
            x_normalised[cc] = x_normalised[cc] / x.sum(axis=1)
        plt.figure()
        ax2 = plt.gca()
        
        
        x_normalised.plot.area(ax=ax2,y=alternatives, fontsize=30, color=['#a1a1a1','#ffb90f','#1c86ee'],linewidth=0)
        x_normalised.plot.area(ax=ax2,y=alternatives,title='Market share of private passenger cars ({0})'.format(self.investment_option), fontsize=30, color=['#a1a1a1','#ffb90f','#1c86ee'],linewidth=0)
        ax2.title.set_size(30)
        
        ax2.set_ylabel('%age of cars', fontsize=30)
        ax2.set_xlabel('Time [Years]', fontsize=30)
        
        
        colors=['#7A7A7A','#CD950C','#104E8B']
        for index, row in car_target.iterrows():
            bottom = 0
            for indx,alt in enumerate(alternatives):
                plt.bar(index,row[alt],bottom=bottom,color=colors[indx],edgecolor='w', width=0.7,linestyle='--')
                bottom += row[alt]
            plt.legend()        
        ax2.figure.set_size_inches(18.5, 10.5)
        
        colors =['#a1a1a1','#ffb90f','#1c86ee','#7A7A7A','#CD950C','#104E8B']
        texts = ['diesel/gasoline', 'battery electric vehicles', 'fuel cell electric vehicel','target diesel/gasoline', 'target battery electric vehicles', 'target fuel cell electric vehicel']
        
        patches = []
        
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1])) )
        patches.append(mpatches.Patch(color=colors[2], label="{:s}".format(texts[2]) ) )
        patches.append(mpatches.Patch(color=colors[3], label="{:s}".format(texts[3]),linestyle='--' ) )
        patches.append(mpatches.Patch(color=colors[4], label="{:s}".format(texts[4]),linestyle='--' ) )
        patches.append(mpatches.Patch(color=colors[5], label="{:s}".format(texts[5]),linestyle='--' ) )
        plt.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        ax2.figure.savefig(os.path.join(os.getcwd(),'results',self.folder_name, 'share.png'))        
        plt.show()
       
        for yr in [2030,2050]:
            if x_normalised.loc[yr,'tec_bev'] >= car_target.loc[yr,'tec_bev']:
                print("In {0}, the market share of battery electric vehicles (BV) is {1:.2f} %. The target of {2:.2f} % is achieved".format(yr,x_normalised.loc[yr,'tec_bev']*100,car_target.loc[yr,'tec_bev']*100))
            else:
                print("In {0}, the market share of battery electric vehicles (BV) is {1:.2f} %. The target of {2:.2f} % is not achieved".format(yr,x_normalised.loc[yr,'tec_bev']*100,car_target.loc[yr,'tec_bev']*100))
            
            if x_normalised.loc[yr,'tec_fcev'] >= car_target.loc[yr,'tec_fcev']:
                print("In {0}, the market share of fuel cell electric vehicles (FCEV) is {1:.2f} %. The target of {2:.2f} % is achieved".format(yr,x_normalised.loc[yr,'tec_fcev']*100,car_target.loc[yr,'tec_fcev']*100))
            else:
                print("In {0}, the market share of fuel cell electric vehicles (FCEV) is {1:.2f} %. The target of {2:.2f} % is not achieved".format(yr,x_normalised.loc[yr,'tec_fcev']*100,car_target.loc[yr,'tec_fcev']*100))
            
                
        # calculating CO2-emissions 
        
        # Consumption of BEV an FCEV [kWh/100km]
        if self.db_on:
            specific_consumption = pd.DataFrame(self.DB.execute_query(Query().query_specific_consumption(self.investment_option,specific_consumption_scenario)))
            specific_consumption.columns = ['c_specific_consumption_construction_year','c_specific_consumption_technology','c_specific_consumption_value']
            specific_consumption.c_specific_consumption_value = specific_consumption.c_specific_consumption_value.astype(float)
        
        if self.write_data:
            specific_consumption.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_specific_consumption.csv'),index=False,sep=';')
        
        
        if self.read_data:
            path = os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_specific_consumption.csv')
            specific_consumption = pd.read_csv(path,sep=';',header=0)

            
        # CO2-emissions of the electricity mix [kgCO2/kWh]
        if self.read_data:    
            path = os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_spec_emissions_electricity_mix.csv')
            spec_emissions_electricity_mix = pd.read_csv(path,sep=';',header=0)           

        if self.db_on:
            spec_emissions_electricity_mix = pd.DataFrame(self.DB.execute_query(Query().query_emissions_electricity_mix(specific_emissions_electricity_mix_scenario)))
            spec_emissions_electricity_mix.columns = ['c_specific_emissions_electricity_mix_year','c_specific_emissions_value']
            spec_emissions_electricity_mix.c_specific_emissions_electricity_mix_year = spec_emissions_electricity_mix.c_specific_emissions_electricity_mix_year.astype(int)
            spec_emissions_electricity_mix.c_specific_emissions_value = spec_emissions_electricity_mix.c_specific_emissions_value.astype(float)
            
        
        if self.write_data:
            spec_emissions_electricity_mix.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_spec_emissions_electricity_mix.csv'),index=False,sep=';')
        

           
        # CO2-emissions of conventional vehicles in dependence of building year [gCO2/km]
        if self.read_data:
            pass
            path = os.path.join(os.getcwd() , 'inputs', self.folder_name,'query_spec_emissions_cv.csv')
            spec_emissions_cv = pd.read_csv(path,sep=';',header=0)

        if self.db_on:
            spec_emissions_cv = pd.DataFrame(self.DB.execute_query(Query().query_specific_emissions(self.investment_option,specific_emissions_scenario)))
            spec_emissions_cv.columns = ['c_specific_emissions_construction_year','c_specific_emissions_value']
            spec_emissions_cv.c_specific_emissions_electricity_mix_year = spec_emissions_cv.c_specific_emissions_construction_year.astype(int)
            spec_emissions_cv.c_specific_emissions_value = spec_emissions_cv.c_specific_emissions_value.astype(int)
                   
        if self.write_data:
            spec_emissions_cv.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_spec_emissions_cv.csv'),index=False,sep=';')
        

        #calculate the total emissions of conventional vehicles 
        car_stock['emissions_tec_cv'] = 0
        for i in range(len(car_stock)):
            emissions_temp = spec_emissions_cv.loc[spec_emissions_cv['c_specific_emissions_construction_year'] == car_stock.loc[i,"reg_year"].item(),  'c_specific_emissions_value'].item()
            car_stock.loc[i,'sp_emissions_tec_cv'] = emissions_temp
            emissions_temp_total = car_stock.loc[i,"tec_cv"].item() * average_passenger_kilometers * car_stock.loc[i,'sp_emissions_tec_cv'].item()
            car_stock.loc[i,'emissions_tec_cv_Mio_t'] = emissions_temp_total  /1000000000

        #Calculation of the total emissions of BEV and FCEV
        car_stock['consump_tec_bev'] = 0
        for i in range(len(car_stock)):
            temp_reg_year = car_stock.loc[i,"reg_year"].item()
            
            # as a constraint because there are no BEV and FCEV in the stock 
            if temp_reg_year >2018: 
                consumption_temp_bev = specific_consumption.loc[(specific_consumption['c_specific_consumption_construction_year']== temp_reg_year)& (specific_consumption['c_specific_consumption_technology']== 'tec_bev' ), 'c_specific_consumption_value'].item()
                consumption_temp_fcev = specific_consumption.loc[(specific_consumption['c_specific_consumption_construction_year']== temp_reg_year)& (specific_consumption['c_specific_consumption_technology']== 'tec_fcev' ), 'c_specific_consumption_value'].item()
            else: 
                  consumption_temp_bev=0
                  consumption_temp_fcev=0
                  
            car_stock.loc[i,'consump_tec_bev'] = consumption_temp_bev
            car_stock.loc[i,'consump_tec_fcev'] = consumption_temp_fcev

            temp_stock_year = car_stock.loc[i,"stock_year"].item()
            temp_emission_factor = spec_emissions_electricity_mix.loc[spec_emissions_electricity_mix['c_specific_emissions_electricity_mix_year'] == temp_stock_year, 'c_specific_emissions_value'].item() 
            car_stock.loc[i,'emission_el_mix'] = temp_emission_factor
            
            emissions_temp_bev_total = car_stock.loc[i,"tec_bev"].item() * average_passenger_kilometers * car_stock.loc[i,'consump_tec_bev'].item()/100 * car_stock.loc[i,'emission_el_mix'].item()/1000000
            car_stock.loc[i,'emissions_BEV'] = emissions_temp_bev_total
            
            emissions_temp_fcev_total = car_stock.loc[i,"tec_fcev"].item() * average_passenger_kilometers * car_stock.loc[i,'consump_tec_fcev'].item()/100 * car_stock.loc[i,'emission_el_mix'].item()/1000000
            car_stock.loc[i,'emissions_FCEV'] = emissions_temp_fcev_total
            
        # Adding emissions to stock_sum table 
  
        col_names = ['year','emissions_CV','emissions_BEV','emissions_FCEV' ]
        CO2_emissions = pd.DataFrame(columns = col_names )
        CO2_emissions.set_index('year', inplace=True)
        colors =['#a1a1a1','#ffb90f','#1c86ee']
        texts = ['diesel/gasoline', 'battery electric vehicles', 'fuel cell electric vehicel']
        
        patches = []
        
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1])) )
        patches.append(mpatches.Patch(color=colors[2], label="{:s}".format(texts[2]) ) )
        
        for y in range(car_stock.stock_year.min().astype(int),car_stock.stock_year.max().astype(int)+1,1):
            CO2_emissions.loc[y,'emissions_CV'] = car_stock.loc[car_stock.stock_year==y,'emissions_tec_cv_Mio_t'].sum()
            CO2_emissions.loc[y,'emissions_BEV'] = car_stock.loc[car_stock.stock_year==y,'emissions_BEV'].sum()
            CO2_emissions.loc[y,'emissions_FCEV'] = car_stock.loc[car_stock.stock_year==y,'emissions_FCEV'].sum()

        
        ax2 = CO2_emissions.plot.area(fontsize=30, color=['#a1a1a1','#ffb90f','#1c86ee'],linewidth=0,title='Total CO2-emissions')
        ax2.set_ylabel('Million Tonnes CO2', fontsize=30)
        ax2.set_xlabel('Time [Years]', fontsize=30)
        ax2.title.set_size(30)
        ax2.figure.set_size_inches(18.5, 10.5)
        ax2.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        
        
        ax2.figure.savefig(os.path.join(os.getcwd(),'results',self.folder_name, 'Co2_emissions.png'))                                                      
        
        
        v2030 = (CO2_emissions.loc[2030].sum() / (106316 * float(car_class_share[0][0]))) *100
        v2050 = (CO2_emissions.loc[2050].sum() / (106316 * float(car_class_share[0][0]))) *100       
        
        if v2030 > 42:
            print("The proportional CO2-emission reduction target of 40-42% in 2030 compared to 1990 in the transport sector is not achieved, as a remaining share of {0:.2f}% is estimated for 2030 and {1:.2f}% for 2050.".format(v2030,v2050))
        else:
            print("The proportional CO2-emission reduction target of 40-42% in 2030 compared to 1990 in the transport sector is achieved, as a remaining share of {0:.2f}% is estimated for 2030 and {1:.2f}% for 2050.".format(v2030,v2050))
            
        return stock_sum, car_stock, CO2_emissions
             
    # Can be deleted for the model        
    def query_importances(self,main_sub):
        
        query_importances = pd.DataFrame(self.DB.execute_query(Query().query_importances(list(main_sub.items())[0][0],list(main_sub.items())[0][1],self.investment_option,)))
        
        query_importances.to_csv(os.path.join(os.getcwd() , 'results',self.folder_name,'query_importances.csv'),index=False)