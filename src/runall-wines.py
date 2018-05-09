
import sys
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import importlib


"""
Import modules.
"""
subset = importlib.import_module('.data.01_subset-data-GBP','src')
plotwines = importlib.import_module('.visualization.02_visualize-wines','src')
country_sub = importlib.import_module('.data.03_country-subset','src')



"""
Initialize variables.
"""
file = r'data/raw/winemag-data-130k-v2.csv'
country = 'Chile'


"""
For running from command line/shell.
"""
if __name__ == '__main__':
    filename = subset.process_data_GBP(file)
    print(filename)
    plotwines.create_plots(filename)
    country_file = country_sub.get_country(filename, country)
    print(country_file)

   

"""
Generate interim data.
"""
filename = subset.process_data_GBP(file)



"""
Create plots.
"""
plotwines.create_plots(filename)



"""
Do analysis of specified country.
"""
country_sub.get_country(filename, country)