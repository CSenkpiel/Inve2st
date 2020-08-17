.. _api:

API
===

Settings
--------

The following variables can be set in ptg.py, note that some of them have to match the inices in the input csv files.

- **year_start**, the year when the first facility was constructed in germany
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
.. automodule:: modules.Investment_Options
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:
  
.. automodule:: modules.DataBase
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
  
.. automodule:: modules.Queries
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:  
  
.. automodule:: calc_UCM_economics
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:   
 
