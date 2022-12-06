from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from helpers import match_utility_code

def pretty_plot(x,y):
    _, ax = plt.subplots(figsize=(12,8))
    ax.tick_params(axis='both', labelsize=15)
    y_ticks = [0.605,0.606,0.607,0.608,0.609]
    x_ticks = [2020,2021,2022,2023]
    for yt in y_ticks:
        ax.plot([2019,2024],[yt,yt], color="#a4a4a4", alpha=0.5)
    for xt in x_ticks:
        ax.plot([xt,xt],[0.60,0.61], color="#a4a4a4", alpha=0.5)
    ax.plot(x,y, color="#ffffff")
    ax.set_facecolor("#112299")
    ax.set_xlabel('year', fontsize=20)
    ax.set_ylabel('fraction of residental area', fontsize=20)
    ax.set_ylim(0.605,0.610)
    ax.set_xlim(2019.9,2023.1)
    ax.set_yticks(y_ticks)
    ax.set_xticks(x_ticks)
    ax.set_title('Fraction of residental houses in terms of floor area', fontsize=25)

    
def plot_locations(data):
    _,ax = plt.subplots(figsize=[12,12])
    types = data['utility'].unique()
    handles, labels = [], []
    for i,tp in enumerate(types):
        l = match_utility_code(tp)
        if l == 'Toimistorakennukset': c = '#00aa11'
        else: c = '#' + str(i)*2 + '11' + str(9-i)*2
        subset = data.loc[data['utility']==tp]
        ax.scatter( 
            x = subset['east_coordinate'].to_numpy()/(10**6), 
            y = subset['north_coordinate'].to_numpy()/(10**5), 
            s = subset['floor_area'].to_numpy()/100,
            color = c
        )
        handles.append(mpatches.Patch(color=c, label=l))
        labels.append(l)
    ax.legend(handles=handles, loc='lower left', labels=labels)
    ax.set_xticks([])
    ax.set_yticks([])