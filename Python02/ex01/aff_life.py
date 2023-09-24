import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Program that plots a single line graph on years vs life expectancy
    for Malaysia, based on the data in the csv.
    """

    # data frames
    df = load("../life_expectancy_years.csv")
    df_my = df.loc[df['country'] == 'Malaysia']

    headers = df_my.columns.values.flatten()
    vals = df_my.values.flatten()

    x_axis_vals = np.delete(headers, 0)
    y_axis_vals = np.delete(vals, 0)

    # new figure object
    fig = plt.figure()

    # new subplot object
    ax = fig.add_subplot(111)
    ax.plot(x_axis_vals, y_axis_vals, 'y-')

    ax.set_title("Malaysia life expectancy Projections")
    ax.set_xlabel('Year')
    ax.set_ylabel('Life Expectancy')

    # set x axis ticks
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    plt.show()


if __name__ == "__main__":
    main()
