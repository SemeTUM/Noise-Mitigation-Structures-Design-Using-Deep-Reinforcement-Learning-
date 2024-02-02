import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import pandas as pd
import matplotlib.font_manager as fm
#Figure 4c
#ddqncnnrule>> np.load('Results/DDQNCNNabsorption.npy')
fig = plt.figure(figsize=(50,30), dpi=300)
ax = fig.add_subplot(111)
plt.plot(freq, ddqncnnrule[3], linewidth=20, label='#3')# 
plt.plot(freq, ddqncnnrule[391], linewidth=20, label='#391')#
plt.plot(freq, ddqncnnrule[403], linewidth=20,label='#403')#
plt.plot(freq, ddqncnnrule[1725], linewidth=20,label='#1725')#

font_properties = {'family': 'serif', 'weight': 'bold', 'size': 90}
font = fm.FontProperties(family=font_properties['family'], weight=font_properties['weight'], size=font_properties['size'])
plt.xticks(fontproperties=font, weight='bold')
plt.yticks(fontproperties=font, weight='bold')
plt.xlabel("Frequency (Hz)", fontproperties=font)
plt.ylabel(r"$\alpha$", fontproperties=font)

ax.spines['top'].set_linewidth(4)
ax.spines['right'].set_linewidth(4)
ax.spines['bottom'].set_linewidth(4)
ax.spines['left'].set_linewidth(4)

# Show the plot
legend_font = {'family': 'serif', 'weight': 'bold', 'size': 80}
plt.legend(prop=fm.FontProperties(**legend_font), loc='lower right')
plt.show()