#!/usr/bin/env python3

#iperf3 -c 212.33.230.200 -P5 -t10 -J > upload.json
#iperf3 -c 212.33.230.200 -P5 -t10 -R -J > download.json

import json
import numpy as np
import matplotlib.pyplot as plt

def parse_pbs(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f) # загружаем словарь
    intervals = data['intervals']
    bps_list = list()
    bps = 0
    for i in intervals:
        bps = i['sum']['bits_per_second']
        bps =  round(bps / 10**6, 2)
        bps_list.append(bps)
    return bps_list

def parse_sec(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f) # загружаем словарь
    intervals = data['intervals']
    sec_list = list()
    sec = 0
    for i in intervals:
        sec = i['sum']['end']
        sec = round(sec, 1)
        sec_list.append(sec)
    return sec_list

y = parse_pbs('upload.json')
x = parse_sec('upload.json')
y1 = parse_pbs('download.json')
x1 = parse_sec('download.json')

print(x, y, x1, y1, sep = '\n')

mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']
columns = ['Upload, Mbit/s', 'Download, Mbit/s']

# Draw Plot

#plt.plot(sec_list, bps_list)
fig, ax = plt.subplots(1, 1, figsize=(16,9), dpi= 80)
plt.axis([x[0], x[-1], 0, 110])
ax.fill_between(x, y, label=columns[0], alpha=0.2, color=mycolors[0], linewidth=2)
ax.fill_between(x1, y1, label=columns[1], alpha=0.2, color=mycolors[1], linewidth=2)

#approximation
"""
linear_model=np.polyfit(x,y,50)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,60)
plt.plot(x_s,linear_model_fn(x_s),color="green")

linear_model=np.polyfit(x1,y1,50)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,60)
plt.plot(x_s,linear_model_fn(x_s),color="red")
"""



# Decorations
ax.set_title('Iperf WLAN-WAN', fontsize=18)
#ax.set(ylim=[0, 100])
#ax.set(xlim=[1, 60])
ax.legend(loc='best', fontsize=14)
#plt.xticks(x[::50], fontsize=10, horizontalalignment='center')
plt.yticks(np.arange(2.5, 100.0, 2.5), fontsize=10)
#plt.xlim(-10, x[-1])


# Draw Tick lines  
for y in np.arange(2.5, 110.0, 2.5):
    plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.3, linestyles="--", lw=0.5)

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
plt.show()

