import numpy as np


class HistoricDiffusion:
    """
    Class to calculate the historic diffusion rate for a logistic function matching the historical data and the maximum
    capacity
    """
    def __init__(self, hist_data, sector, duration, cap_max_sector):
        """
        by initializing this class, the arguments are written to the class
        :param hist_data: historic data
        :param sector: sector under consideration
        :param duration: analysed period
        :param cap_max_sector: maximum installed capacity in sector in GWel
        """
        self.hist_data = hist_data
        self.sector = sector
        self.duration = duration
        self.cap_max_sector = cap_max_sector

    def function_to_minimize(self, rate):
        """
        This is the function to minimize to determine the historic diffusion rate
        :param rate: float growth rate of logistic function
        :return: sum of the quadratic deviation of historic data to model data
        """
        data = self.hist_data
        r = rate
        deviation_list = []
        for i in range(len(data)):
            a = (data.iloc[i] - self.cap_max_sector / (1 + np.exp(-r * (i - self.duration/2))))**2
            deviation_list.append(a)
        s = sum(deviation_list)
        return s

# Alternative approach by curve fitting
    # def function_to_fit(self, year, rate):
    #     """
    #     Function to fit to data to get historic rate if alternative computation needed
    #     code for fitting is stored below
    #     :param year: year
    #     :param rate: rate
    #     :return: model data
    #     """
    #     cap = self.cap_max/(1 + np.exp(-rate * (year - self.duration/2)))
    #     return cap

# code for minimization by curve-fitting
# ydata = ptg_data.hist[sector]
# xdata = ydata.index
# r, s = opt.curve_fit(HD.function_to_fit, xdata, ydata)
