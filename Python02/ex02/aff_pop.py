import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load

def handleData(df: pd.DataFrame, country: str, range: tuple[int, int]) -> pd.DataFrame:
    """
    Extracts and processes data from the dataframe.
    """
    country_df = df.loc[df['country'] == country]

    tens = dict(k=1000, M=1000000)
    
    country_df = country_df.iloc[:, range[0]:range[1]].applymap(lambda x : int(float(x[0:-1]) * tens[x[-1]]))

    return country_df

def tickFormatterMillions(x, pos):
    """Formatter for ticks"""
    return '%1.1fM' % (x*1e-6)

def main():

    # data frames
    df = load("../population_total.csv")

    start = df.columns.get_loc("1800")
    end = df.columns.get_loc("2050") + 1
    df_my = handleData(df, 'Malaysia', (start, end))
    df_th = handleData(df, 'France', (start, end))

    x_axis_vals = df_my.columns.values.flatten()

    my_vals = df_my.values.flatten()
    th_vals = df_th.values.flatten()

    # new figure object
    fig = plt.figure()

    # new subplot object
    ax = fig.add_subplot(111)

    # lines
    my_line = ax.plot(x_axis_vals, my_vals, 'r-', label='Malaysia')
    fr_line = ax.plot(x_axis_vals, th_vals, 'b-', label='France')

    # labels
    ax.set_title("Population Projections")
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    # legend
    ax.legend(loc='lower right')

    # ticks
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(tickFormatterMillions))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20000000))
    ax.xaxis.set_major_locator(ticker.MaxNLocator(9))

    plt.show()


if __name__ == "__main__":
    main()
