
import random
import functools
from itertools import zip_longest

import matplotlib.pyplot as plt
import matplotlib.animation as animation



def run_animation(*sort_functions, n_numbers = 16):
    
    # set bins and numbers
    hist_bins = list(range(n_numbers+1))  # NOTE: edges = bins + 1
    num_min = 40
    num_max = 100
    numbers = [random.randint(num_min, num_max) for _ in range(n_numbers)]

    # set frames for animation
    frame_generators = [g(numbers=numbers) for g in sort_functions]
    sort_func_names = [f.name() for f in frame_generators]
    frames = zip_longest(*frame_generators, fillvalue=sorted(numbers))  # some sort faster than others

    # set figure 
    n_funcs = len(sort_functions)
    fig, axs = plt.subplots(1, n_funcs, sharey=True)
    fig.set_size_inches(16, 9)

    # following code assume axs is a list of ax(s)
    axs = [axs] if n_funcs == 1 else axs
    
    # set plots
    plt.setp(axs, xticks=[], yticks=[],             # remove ticks and labels for a clean look
             ylim=(num_min * 0.5, num_max * 1.02))  
    for ax, name in zip(axs, sort_func_names):
        ax.set_title(name)

    # set histograms
    default_color = "green"
    hightlight_color = "pink"
    edge_color = "yellow"

    bar_containers = []
    for ax in axs:
        _, _, bar_container  = ax.hist(x=[], bins=hist_bins, lw=1, ec=edge_color, fc=default_color, alpha=0.5)
        bar_containers.append(bar_container)

    # for a cleaner look
    plt.tick_params(left=False, bottom=False,
                    labelleft=False, labelbottom=False)

    def animate(new_heights, bar_containers):
        for heights, bar_container in zip(new_heights, bar_containers):
            for height, patch in zip(heights, bar_container.patches):
                current_height = patch.get_height()
                if current_height == 0:  # first frame
                    patch.set_height(height)
                elif current_height != height:
                    patch.set_height(height)
                    patch.set_facecolor(hightlight_color)  
                else:
                    patch.set_facecolor(default_color)  # default color
        return bar_containers

    func = functools.partial(animate, bar_containers=bar_containers)  # NOTE: new_heights will be supplied later as frames

    func_animation = animation.FuncAnimation(fig=fig, 
                                             func=func,
                                             interval=400,           
                                             frames=frames,
                                             blit=True, 
                                             repeat=False,
                                             cache_frame_data=False)  # to suppress warning
    plt.show() 
    return func_animation  # NOTE: must keep a reference to this returned animaton to keep it alive 

