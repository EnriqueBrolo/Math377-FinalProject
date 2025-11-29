import matplotlib.pyplot as plt
import numpy as np
import csv


def ps_curve(a, res):
    return 1.0/(1+np.exp(2-4*((-res[3] + a * res[1]) /
            ((res[2]-res[3]) - a*(res[0] - res[1])))))


cc = []
cc_total = 0
name = ""
a_values = np.linspace(200000, 1250000, 1000)
plt.figure()
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

curve_index = 0

with open('data.csv', mode='r', newline='') as file:
    csvFile = csv.reader(file)

    for row in csvFile:
        if row and row[0].startswith("#R"):
            continue
        if row and row[0].startswith("#"):
            name = "".join(row[0][1:])
            continue


        res = list(map(float, row))
        w_values = ps_curve(a_values, res)
        cc.append(a_values[np.argmin(np.abs(w_values - 0.6))])
        color = color_cycle[curve_index % len(color_cycle)]
        plt.plot(a_values, w_values, color=color, alpha=0.9, label=name)

        curve_index += 1



plt.xlabel("Population")
plt.ylabel("P-S Value")
plt.title("Unweighted P-S Curves")
plt.ticklabel_format(axis='x', style='plain')
plt.legend(loc="best")
plt.show()

for value in cc:
    cc_total += value

cc_total /= len(cc)

print("Carrying capacity calculated (unweighted) with 0.6 threshold:")
print(cc_total)