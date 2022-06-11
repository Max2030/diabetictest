import datetime
import numpy as np
import random
import decimal
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from numpy.random import rand

for i in range(10):
  print(random.randint(60, 190)/10)

# get number of days in period:
date1 = date(2021, 1, 1)
date2 = date(2021, 8, 14)
days = (date2 - date1).days +1

# Create dates:
dates = pd.date_range(date1, periods=days).tolist()

# Create the an Glucose levels:
morning = []
lunchTime = []
evening = []

for i in range(days):
  morning.append(random.randint(56, 190)/10)
  lunchTime.append(random.randint(70, 200)/10)
  evening.append(random.randint(45, 150)/10)

data = pd.DataFrame({'date':dates,'morning': morning, 'lunchTime':lunchTime, 
'evening':evening})
print(data)

# averages:
m_average = round(np.average(data['morning']),0)
l_average = round(np.average(data['lunchTime']),0)
e_average = round(np.average(data['evening']),0)

# plot data:
plt.plot(data['date'], data['morning'], linewidth=1, label='Morning')
plt.plot(data['date'], data['lunchTime'], linewidth=1, label='lunchTime')
plt.plot(data['date'], data['evening'], linewidth=1, label='evening')

plt.axhline(m_average, color='red', linewidth=1, linestyle='dashed', label='Morning average')
plt.axhline(l_average, color='blue', linewidth=1, linestyle='dashed', label='Lunch time average')
plt.axhline(e_average, color='green', linewidth=1, linestyle='dashed', label='Evening average')

plt.title( 'glucose levels')
plt.xlabel('Data')
plt.ylabel('Level')
plt.legend()
plt.tight_layout()
plt.show()


# Save the data:
# plt.spngavefig('data/glucose2021.png')
data.to_csv('data/glucose2021.csv')






