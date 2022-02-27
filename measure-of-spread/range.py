"""
Mesaure of spread simulation

Range (max - min)
"""

# import packages
import numpy as np
import matplotlib.pyplot as plt

# variables
np.random.seed(101)
mean_height_netherlands = 180
std_height_netherlands = 10
mean_height_world = 165
std_height_world = 20
n_people = 20000
text_x_netherlands  = mean_height_netherlands * 1.3
text_x_world = mean_height_world * 1.3
text_y = int(0.2 * n_people)
text_y_offset = int(0.05 * n_people)
text_font_size = 12

# generate random dataset
netherlands = np.random.normal(
    loc=mean_height_netherlands,
    scale=std_height_netherlands,
    size=n_people,
    )
world = np.random.normal(
    loc=mean_height_world,
    scale=std_height_world,
    size=n_people,
    )

# create figure
fig, ax = plt.subplots(nrows=2, ncols=1,figsize=(10,8))

# add histogram
_ = ax[0].set_xlim(80, 300)
_ = ax[0].hist(
    netherlands,
    bins=10,
    rwidth=1,
    alpha=0.8,
    color='orange',
    label='Netherlands',
)
_ = ax[1].set_xlim(80, 300)
_ = ax[1].hist(
    world,
    bins=10,
    rwidth=1,
    alpha=0.8,
    color='navy',
    label='World',
)

# add texts to plot (to show mean, median and mode)
_ = ax[0].annotate(
    f'range = {int(np.max(netherlands) - np.min(world))}',
    (text_x_netherlands, text_y - 1 * text_y_offset),
    fontsize=text_font_size,
)
_ = ax[1].annotate(
    f'range = {int(np.max(world) - np.min(world))}',
    (text_x_netherlands, text_y - 1 * text_y_offset),
    fontsize=text_font_size,
)


# set titles
_ = ax[0].set_title("Height Distibution of Fake Netherlands in Fake World")
_ = ax[0].set_xlabel("Height (cm)")
_ = ax[0].set_ylabel("# of observations")
_ = ax[1].set_title("Height Distibution of Fake World")
_ = ax[1].set_xlabel("Height (cm)")
_ = ax[1].set_ylabel("# of observations")

# add legends
_ = ax[0].legend()
_ = ax[1].legend()

# tigh
_ = plt.tight_layout()

# show the plot
_ = plt.show()

# save the plot
fig.savefig('range.svg')
