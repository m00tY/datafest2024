import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p_data = pd.read_csv('Full Data/page_views.csv')
for i in range(len(p_data['chapter_number'])):
    if np.isnan(p_data.loc[i, 'chapter_number']) == False:
        p_data.loc[i, 'chapter_number'] = int(p_data.loc[i, 'chapter_number'])

peen_data = p_data.iloc[:,[4,13,14,15]]
grouped = peen_data.groupby('chapter_number').mean()
grouped = grouped.loc[0:12]

print(grouped)
plot = grouped.plot(title='Average Engament Per Chapter', kind='bar',xlabel='Chapter', ylabel='Time (ms)')
plt.show()


v_data = pd.read_csv('Full Data/media_views.csv')
for i in range(len(v_data['chapter_number'])) == False:
    if np.isnan(v_data.loc[i, 'chapter_number']):
        v_data.loc[i, 'chapter_number'] = int(v_data.loc[i, 'chapter_number'])
        
for i in range(len(v_data['proportion_video'])):
    v_data.loc[i, 'proportion_video'] = v_data.loc[i, 'proportion_video'] * 100
for i in range(len(v_data['proportion_video'])):
    v_data.loc[i, 'proportion_time'] = v_data.loc[i, 'proportion_time'] * 100

taint_data = v_data.iloc[:,[4,13,14]]
grouper = taint_data.groupby('chapter_number').mean()

#grouper = grouper.loc[0:12]
#percentiles == .describes()

print(grouper)
plot = grouper.plot(title='Average Percent of Videos Watched Per Chapter', kind='bar', xlabel='Chapter', ylabel='Percent (%)')
plt.show()
