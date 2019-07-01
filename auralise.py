import pandas as pd
from pyo import *
import time

df = pd.read_csv('resources/GlobalLandTemperaturesByCountry.csv',
                 usecols=[0, 1, 3], index_col=False)
df = df.fillna(method='ffill')
df['year'] = pd.to_numeric(df['dt'].apply(lambda dt: dt[:4]))
df = df[df['year'] > 1799]
df['month'] = pd.to_numeric(df['dt'].apply(lambda dt: dt[5:7]))
df = df[['year', 'month', 'AverageTemperature']]
df.columns = ['year', 'month', 'min_temp']
df = df.sort_values(['year', 'month', 'min_temp'])
df['max_temp'] = df['min_temp']
df = df.groupby(['year', 'month'], as_index=False).agg(
    {'min_temp': 'min', 'max_temp': 'max'})


def calc_freq(num):
    freq = num + 40 * 15
    return int(freq - freq % 10)


s = Server(nchnls=1).boot()
s.amp = .1
s.start()

y_beat = Sine(freq=100, mul=.3)
m_beat = Sine(freq=200, mul=.3)
low = Sine(mul=.2)
lh = Harmonizer(low).out()
high = Sine(mul=.2)
hh = Harmonizer(high).out()

for index, row in df.iterrows():
    if row['month'] == 1:
        if row['year'] % 10 == 0:
            y_beat.out(dur=.2)
        else:
            m_beat.out(dur=.1)

    low.freq = calc_freq(row['min_temp'])
    high.freq = calc_freq(row['max_temp'])
    time.sleep(.2)

s.stop()
