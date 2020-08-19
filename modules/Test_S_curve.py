# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:52:04 2020

@author: csenkpie
"""

def calculate_S_curve(pv_stock_battery,t_mid=None):
        plt.figure(figsize=(12.0, 12.0))
        #K = 60 #pv_potential_germany[0].astype(float).values[0]
        K = 16700
        def model(t, coeffs):
            return K/(1+np.exp(-coeffs[0]*(t-coeffs[1])))
        
        x0 = np.array([0.4,28], dtype=float)
        
        def residuals(coeffs, y, t):
            return y - model(t, coeffs)
               
        df = pv_stock_battery.copy(deep=True)
        df = df.sort_values(by =['operation_year'])
    
        df['historic'] = df['stock'].cumsum().astype(float)/1000
        df['t'] = df['operation_year']-df['operation_year'].min()
        df.set_index(keys=['t'],inplace=True)
        
        
        r_optim, flag = leastsq(residuals, x0, args=(df.historic.values, df.index.values))
        
        if not t_mid:
            t_mid = r_optim[1]
        else:
            t_mid = t_mid
        r_optim = r_optim[0]
        t_end = 100
      
        PV_install_S_Curve = pd.DataFrame(index=range(1,t_end+1),columns=range(1))
        PV_install_S_Curve.columns = ["cumulated_installations"]
        
        for t in range(1,t_end+1):
            PV_install_S_Curve.loc[t,"cumulated_installations"] = model(t,(r_optim,t_mid))
       
        
        PV_install_S_Curve['installations'] = PV_install_S_Curve.cumulated_installations -  PV_install_S_Curve.cumulated_installations.shift(1)
        PV_install_S_Curve['installations'] = PV_install_S_Curve['installations'].fillna(PV_install_S_Curve.cumulated_installations)    
        PV_install_S_Curve['year'] = PV_install_S_Curve.index + pv_stock_battery.operation_year.min()
        PV_install_S_Curve['index'] = PV_install_S_Curve['year']
        PV_install_S_Curve.set_index(['index'],inplace=True)
        
        plt.plot(PV_install_S_Curve['year'],PV_install_S_Curve["cumulated_installations"],color='#104E8B',label='Cumulated Installations')
        plt.bar(df.operation_year,df.historic,color='#CD950C',label='Historic Installations')
        plt.ylabel('Cumulated Stock Sum [MW]', fontsize=30)
        plt.xlabel('Time [years]', fontsize=30)
        plt.title('{}'.format(self.investment_option), fontsize=30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        plt.legend(fontsize=30)
        
        plt.savefig(os.path.join(os.getcwd(),'results',self.folder_name,'Stock.png'))
        plt.show()
        
        return PV_install_S_Curve, df