import matplotlib.pyplot as plt
import numpy as np
import csv

def ps_curve(a, res):
    return 1.0/(1+np.exp(2-4*((-res[3] + a * res[1])/((res[2]-res[3])-a *(res[0] - res[1])))))

a_values = np.linspace(200000, 1250000, 1000)
cc = []
names = []
curves = []

with open('data.csv', mode='r', newline='') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row and row[0].startswith("#R"):
            continue
        if row and row[0].startswith("#"):
            name = "".join(row[0][1:]).strip()
            names.append(name)
            continue
        
        res = list(map(float, row))
        w_values = ps_curve(a_values,res)
        curves.append(w_values)
        idx_cc = np.argmin(np.abs(w_values - 0.6))
        cc_value = a_values[idx_cc]
        cc.append(cc_value)
        plt.plot(a_values,w_values)
        plt.xlabel("Population")
        plt.ylabel("P-S Value")
        plt.title("P-S Curve for " + name)
        plt.ticklabel_format(axis='x', style='plain')
        plt.show()

cc_total = sum(cc)/len(cc)
print("Carrying capacity (unweighted) with 0.6 threshold")
print(cc_total)

weights = np.array([0.3,0.1,0.2,0.1,0.3])
curves_array = np.array(curves)
weighted_curve = np.sum(weights[:,None]*curves_array, axis=0)
idx_weighted = np.argmin(np.abs(weighted_curve - 0.6))
weighted_cc = a_values[idx_weighted]

print("Weighted carrying capacity (threshold 0.6)")
print(weighted_cc)

plt.plot(a_values, weighted_curve)
plt.xlabel("Population")
plt.ylabel("Weighted P-S Value")
plt.title("Weighted P-S Curve")
plt.ticklabel_format(axis='x', style='plain')
plt.show()
