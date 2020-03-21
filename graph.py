#! /usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime as dt
import numpy as np
import pandas as pd

with open('log', 'r') as f:
    log = f.readlines()

data = {'t': [], 'u': [], 'g': []}

for line in log:
    line = line[:-1].split()
    line[0] = dt.datetime.fromtimestamp(int(line[0]))
    data['t'].append(line[0])
    data['u'].append(int(line[1]))
    data['g'].append(int(line[2]))

df = pd.DataFrame(data=data)


fig, ax = plt.subplots()
plt.plot( 't', 'u', data=df, linewidth=2, label='Users')
plt.plot( 't', 'g', data=df, linewidth=2, label='Games')
plt.legend()

ax.set(xlabel='Time', ylabel='Count',
       title='Chess.com Activity')

plt.ylim(0,80000)


xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.25))


fig.savefig("test.png")

plt.show()
