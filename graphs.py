import matplotlib.pyplot as plt
import numpy as np
import csv


def ps_curve(a, res):
    return 1.0/(1+np.exp(2-4*((-res[3] + a * res[1])/((res[2]-res[3])-a *(res[0] - res[1])))))

resources = []
name = ""
a_values = np.linspace(0, 2500000, 1000)

with open('data.csv', mode='r', newline='') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row and row[0].startswith("#R"):
                continue 
            if row and row[0].startswith("#"):
                 name = "".join(row[0][1:] )
                 continue
            res = list(map(float, row))
            w_values = ps_curve(a_values,res)
            plt.plot(a_values,w_values)
            plt.plot(a_values, w_values)
            plt.xlabel("Population")
            plt.ylabel("P-S Value")
            plt.title("P-S Curve for " + name)
            plt.ticklabel_format(axis='x', style='plain')
            plt.show()
            
