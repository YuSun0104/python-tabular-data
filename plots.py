#! /usr/bin/ env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def get_all_species():
    species_list = dataframe.species.unique()
    return species_list
def get_regression_plots():
    i = 0
    for i in range(0,len(dataframe.species.unique())):
        df = dataframe[dataframe.species == species[i]]
        x = df.petal_length_cm
        y = df.sepal_length_cm
        regression = stats.linregress(x,y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x,y,label=species[i])
        plt.plot(x,slope * x + intercept,color="red",label="Our Fitting Line")
        plt.xlabel("Petal length(cm)")
        plt.ylabel("Sepal length(cm)")
        plt.legend()

        plt.savefig(species[i] + ".png")
        plt.close()
        i += 1


if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
    species = dataframe.species.unique()
    print("the Regression plots for " + species)
    get_regression_plots()
