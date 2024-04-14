import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p_data = pd.read_csv('Full Data/media_views.csv')
r_data = pd.read_csv('Full Data/responses.csv')
c_data = pd.read_csv('Full Data/checkpoints_eoc.csv')

prop_data = p_data.iloc[:,[13,14]]
vid_data = p_data.loc[:, 'proportion_video']
# prop_data = prop_data.dropna()
# plot = prop_data.plot(linestyle=':', title='proportions', ylabel='y', xlabel='x')
# plt.show()

resp_data = r_data.iloc[:,[15,16]]
check_data = c_data.loc[:,'EOC']

# prop_corr = prop_data.corr(method='pearson')
# print(prop_corr)

corr_data = check_data.join(vid_data)
eoc_corr = corr_data.corr(method='pearson')
print(eoc_corr)

