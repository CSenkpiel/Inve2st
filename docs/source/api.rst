.. _api:

API
===

Settings
--------

The following variables can be set in ptg.py, note that some of them have to match the indices in the input csv files.

- **year_start**, the year when the first facility was constructed in Germany
- **duration**, time until maximum capacity is installed
- **cap_max**, target maximum installed capacity in GWel
- **share_sector**, dictionary with the shares of cap_max per sector
- **sector_sizes**, dictionary with the sizes of the facilities in different sectors in MWel
- **debt_share**, share of debts in financing
- **debt_interest_rate**, interest rate for debts
- **debt_term**, runtime of debts
- **income_tax**, income tax rate
- **upper_bound** upper bound for investors expectation
- **lower_bound**, lowewr bound for investors expectations
- **supportive**, whether the political decisions are supportive
- **det_weigt**, dictionary for the determinants weights
- **lower_bound_rate**, lower growth rate (without political support)


Modules
-------
.. automodule:: Inve2st_cars.modules.Investment_Options
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:
  
.. automodule:: Inve2st_cars.modules.DataBase
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.Queries
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance: 

.. automodule:: Inve2st_PV_HSS.modules.calc_UCM_economics
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:   
  
.. automodule:: Inve2st_ptg.modules.calc_annual_diffusion
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:
  
.. automodule:: Inve2st_ptg.modules.calc_hist_diffusion
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
  
.. automodule:: modules.calc_installed_cap_from_hist
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
 
.. automodule:: modules.calc_modified_capacity
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.generate_sector_classes
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance: 

.. automodule:: modules.loop
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.plot_cap
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.plot_irr
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.read_and_generate_data
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
  
.. automodule:: Inve2st_ptg.modules.save_data
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.IRR.calc_cashflow
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.IRR.calc_financial_expenses
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
 
.. automodule:: modules.IRR.calc_income_statement
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  

.. automodule:: modules.IRR.calc_investment
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
  
.. automodule:: modules.IRR.calc_operational_cost
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance: 

