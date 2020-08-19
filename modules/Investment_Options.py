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
from scipy.optimize import leastsq


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
        self.DB = DB # if DB connection = True
        
        #self.attribute_sceanrio = None # Default Value
        self.folder_name = folder_name # Comes from test data 
        self.db_on = db_on
        self.write_data = write_data # control variable to write data from DB to csv

        self.read_data = read_data # control variable to read data from csv        

    ##################################################################################################################################
    #-------Utilities----------------------------------------------------------------------------------------------------

    def calculate_utility(self, value_resolution,attribute_sceanrio,aggregation_level,tec_none):
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
            #path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_investment_option_alternatives.csv')
            path = os.path.join(os.getcwd() , 'inputs',self.investment_option + '_'+ aggregation_level,'query_investment_option_alternatives.csv')
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
                    #path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_utility_none_option.csv')
                    path = os.path.join(os.getcwd() , 'inputs',self.investment_option + '_'+ aggregation_level,'query_utility_none_option.csv')
                    utility_none_option = pd.read_csv(path,sep=';')
                    
                
            else:
                if self.db_on:
                    attributes = self.DB.execute_query(Query().query_attributes(self.investment_option))
                    attribute_levels = pd.DataFrame(self.DB.execute_query(Query().query_attribute_level_per_year(self.investment_option, attribute_sceanrio)))
                    attribute_levels.columns= ['alternative','year','attribute','attribute_level']
                
                if self.write_data:
                    attribute_levels.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_per_year.csv'),index=False,sep=';')
                
                if self.read_data:
                    #path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_per_year.csv')
                    path = os.path.join(os.getcwd() , 'inputs',self.investment_option +'_scenarios',attribute_sceanrio + '_attribute_level_per_year.csv')
                    attribute_levels = pd.read_csv(path,sep=';')
                    
                    
                if self.db_on:    
                    attribute_level_putility = pd.DataFrame(self.DB.execute_query(Query().query_attribute_level_putility(self.investment_option, value_resolution)))
                    attribute_level_putility.columns=['attribute','attribute_level','partial_utility_value','respondend','value_resolution']
                
                if self.write_data:
                    attribute_level_putility.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_putility.csv'),index=False,sep=';')
                    
                if self.read_data:
                    #path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_attribute_level_putility.csv')
                    path = os.path.join(os.getcwd() , 'inputs',self.investment_option+ '_'+ aggregation_level,'query_attribute_level_putility.csv')
                    attribute_level_putility = pd.read_csv(path,sep=';')
                
                # list of discrete attributes
          
                if self.db_on:
                    discrete_att_list = pd.DataFrame(self.DB.execute_query(Query().query_discrete_attributes(self.investment_option)))
                
                if self.write_data:
                    discrete_att_list.to_csv(os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_discrete_attributes.csv'),index=False,sep=';')
                
                if self.read_data:
                    #path = os.path.join(os.getcwd() , 'inputs',self.folder_name,'query_discrete_attributes.csv')
                    path = os.path.join(os.getcwd() , 'inputs',self.investment_option+ '_'+ aggregation_level,'query_discrete_attributes.csv')
                    discrete_att_list = pd.read_csv(path,sep=';',header=0)                
                    discrete_att_list.columns = discrete_att_list.columns.astype(int)
                
                discrete_df = attribute_level_putility[attribute_level_putility.attribute.isin(discrete_att_list[0].drop_duplicates())]

                # get dataframe of discrete attribute levels               
                attribute_levels_putility_comb_discrete = pd.merge(attribute_levels,discrete_df,how='inner',on=['attribute','attribute_level'])  
                
                
                
                # Based on investment option (PV-battery), separate continuous attributes from discrete ones.
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
                        #if attribute != 'att_pp_IRR':
                        x = [float(i) for i in x]
                                                     
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

                attribute_levels_putility_comb_cont = pd.concat(attribute_levels_putility_comb_cont_df_list,sort=True)

        
        # combining the data to get a joint data frame 
        attribute_levels_putility_comb = pd.concat([attribute_levels_putility_comb_cont,attribute_levels_putility_comb_discrete],sort=True)

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
            utility_alternatives = pd.concat([xx,utility_alternatives],sort=True)
        utility_alternatives = utility_alternatives.sort_values(by=['year','alternative','respondend']).reset_index(drop=True)


        
        utility_alternatives.to_csv(os.path.join(os.getcwd() , 'results',self.folder_name,'utility_alternatives.csv'),index=False)
        
      #  return utility_alternatives
        return utility_alternatives, attribute_levels_putility_comb,attribute_levels_putility_comb_cont,continuous_df
    
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
        
        if self.investment_option == 'homestorage':
            tuples = [('probability', 'tec_bat_li'), ('probability', 'tec_none')]
            x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
            color_dict = {'tec_bat_li':'#ffb90f','tec_none':'#a1a1a1'}

        if self.investment_option == 'PV_homestorage':
            tuples = [('probability', 'tec_pv_plus_battery'), ('probability', 'tec_none')]
            x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
            color_dict = {'tec_pv_plus_battery':'#ffb90f','tec_none':'#a1a1a1'}
        
        colors = []
        for c in x:
            if c[1] in color_dict:
                colors.append(color_dict[c[1]])
            else:
                colors.append('black')

        ax2 = x.plot.bar(y='probability', stacked=True,fontsize=30,title='Logit Probabilities',color=colors)
        ax2.set_xlabel('Year', fontsize=30)
        ax2.set_ylabel('Probability', fontsize=30)
        ax2.title.set_size(30)
        ax2.figure.set_size_inches(18.5, 10.5)
        
        colors =['#a1a1a1','#ffb90f']
        texts = ['No Investment', self.investment_option]
        patches = []
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[0]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[1])) )
        
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
        
        """
        tuples = x.columns.tolist()
        for item in tuples:
            if ('probability', 'tec_cv') == item:
                old_index = tuples.index(('probability', 'tec_cv')) 
                tuples.insert(0, tuples.pop(old_index))

        x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
        """
                
        if self.investment_option == 'PV_homestorage':
            tuples = [('probability', 'tec_pv_plus_battery'), ('probability', 'tec_none')]
            x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
            texts = ['No Investment', 'PV and battery system in single family or row house']
            
        if self.investment_option == 'homestorage':
            tuples = [('probability', 'tec_bat_li'), ('probability', 'tec_none')]
            x = x.reindex(columns=pd.MultiIndex.from_tuples(tuples))
            texts = ['No Investment', 'battery system in single family or row house']
        
        colors =['#a1a1a1','#ffb90f'][::-1]

        patches = []
        patches.append(mpatches.Patch(color=colors[0], label="{:s}".format(texts[1]) ) )
        patches.append(mpatches.Patch(color=colors[1], label="{:s}".format(texts[0])) )
        
        ax2 = x.plot.bar(y='probability', stacked=True,fontsize=30,title='First Choice Probabilities',color=colors)
        ax2.set_ylabel('Preference Share [%]', fontsize=30)
        ax2.set_xlabel('Time [Years]', fontsize=30)
        ax2.title.set_size(30)
        #ax2.legend(labels, fontsize=30)
        ax2.figure.set_size_inches(18.5, 10.5)
        ax2.figure.savefig(os.path.join(os.getcwd(),'results',self.folder_name,'preference_share.png'))
        ax2.legend(handles=patches,loc='lower left', bbox_to_anchor=(0.0, 0.0),prop={'size': 30})
        first_choice_prob.to_csv(os.path.join(os.getcwd(),'results',self.folder_name,r'first_choice_prob.csv'),index=False)
        
        return first_choice_prob,utility_alternatives

             
