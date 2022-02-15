# import packages
import numpy as np
import matplotlib.pyplot as plt

# variables
np.random.seed(101)
mean_wealth = 20000
n_people = 100000
text_x = mean_wealth*5
text_y = int(0.3 * n_people)
text_y_offset = int(0.04 * n_people)
verical_height = int(0.47 * n_people)
text_font_size = 12

# generate random dataset
dataset = np.random.exponential(scale=mean_wealth, size=n_people)

# create figure
fig, ax = plt.subplots(figsize=(10,5))

# add histogram
_ = ax.hist(
    dataset,
    bins=20,
    rwidth=0.8,
    alpha=0.3,
    color='blue',
)

# add vertical lines in mean and median values
_ = ax.vlines(
    np.mean(dataset),
    0,
    verical_height,
    color='red',
    label='mean',
)
_ = ax.vlines(
    np.median(dataset),
    0,
    verical_height,
    color='black',
    label='median',
)

# add texts to plot (to show mean, median and mode)
_ = ax.annotate(
    f'mean = {int(np.mean(dataset))}',
    (text_x,text_y + text_y_offset),
    fontsize=text_font_size,
)
_ = ax.annotate(
    f'median = {int(np.median(dataset))}',
    (text_x,text_y),
    fontsize=text_font_size,
)
_ = ax.annotate(
    f'mode = first bin',
    (text_x,text_y - text_y_offset),
    fontsize=text_font_size,
)

# set titles
_ = ax.set_title("Wealth Distibution of Fake Earth in Fake Galaxy")
_ = ax.set_xlabel("Welath (USD)")
_ = ax.set_ylabel("# of observations")

# add legends
_ = ax.legend()

# show the plot
_ = plt.show()

# save the plot
fig.savefig('wealth.svg')
