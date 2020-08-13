# In this file classes for each sector are generated where the specific data is stored
import pandas as pd


class Mobility:
    """
    Data frames for sector mobility
    """
    def __init__(self, year_start, duration):

        self.rate_hist = 0.
        self.cap_installed_hist = pd.DataFrame(index=range(year_start, year_start + duration))
        self.annual_rate = pd.DataFrame(index=range(year_start, year_start + duration))
        self.irr = pd.DataFrame(index=range(2019, 2051))


class Industry:
    """
    Data frames for sector industry
    """
    def __init__(self, year_start, duration):
        self.rate_hist = 0.
        self.cap_installed_hist = pd.DataFrame(index=range(year_start, year_start + duration))
        self.annual_rate = pd.DataFrame(index=range(year_start, year_start + duration))
        self.irr = pd.DataFrame(index=range(2019, 2051))


class Injection:
    """
    Data frames for sector injection
    """
    def __init__(self, year_start, duration):
        self.rate_hist = 0.
        self.cap_installed_hist = pd.DataFrame(index=range(year_start, year_start + duration))
        self.annual_rate = pd.DataFrame(index=range(year_start, year_start + duration))
        self.irr = pd.DataFrame(index=range(2019, 2051))


class ReElectrification:
    """
    Data frames for sector re-electrification
    """
    def __init__(self, year_start, duration):
        self.rate_hist = 0.
        self.cap_installed_hist = pd.DataFrame(index=range(year_start, year_start + duration))
        self.annual_rate = pd.DataFrame(index=range(year_start, year_start + duration))
        self.irr = pd.DataFrame(index=range(2019, 2051))
