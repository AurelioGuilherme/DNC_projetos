import seaborn as sns

def set_theme():
    # https://matplotlib.org/stable/tutorials/introductory/customizing.html
    sns.set_theme(
        context='talk',
        style='ticks',
        font_scale=.8,
        palette='pastel',
        rc={
            'figure.figsize': (12,8),
            'axes.grid': True,
            'grid.alpha': .2,
            'axes.titlesize': 'x-large',
            'axes.titleweight': 'bold',
            'axes.titlepad': 20,
        }
    )

scatter_kwargs = dict(palette='viridis', alpha=0.8, linewidth=0)

def valuesPlot(plot):

  for i in plot.patches:
    plot.annotate(i.get_height(),
                  (i.get_x() + i.get_width() / 2, i.get_height()),
                  ha='center',
                  va='baseline',
                  fontsize=12,
                  color='black',
                  xytext=(0, 1),
                  textcoords='offset points');

if __name__ == "__main__":
    set_theme()
    main()