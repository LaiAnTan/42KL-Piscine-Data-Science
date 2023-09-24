import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def handleData(df: pd.DataFrame, country: str, range: tuple[int, int]) \
                -> pd.DataFrame:
    """
    Extracts and processes data from the dataframe.

    @param df: dataframe
    @param country: country to access data of
    @param range: range of data to get in the form of (start, stop)
    @return country_df: dataframe of the country with data within range of
    start and stop
    """
    # get dataframe containing row with country = country
    country_df = df.loc[df['country'] == country]

    # dict for storing conversion factors
    tens = dict(k=1000, M=1000000)

    # process dataframe by only extracting values within range
    # values extracted are string values with suffixes and need to be converted
    # to ints
    country_df = (country_df.iloc[:, range[0]:range[1]]
                  .applymap(lambda x: int(float(x[0:-1]) * tens[x[-1]])))

    return country_df


def main():
    """
    Program that plots a double line graph on years vs life expectancy
    for Malaysia and France, based on the data in the csv.
    """

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
    ax.plot(x_axis_vals, my_vals, 'r-', label='Malaysia')
    ax.plot(x_axis_vals, th_vals, 'b-', label='France')

    # labels
    ax.set_title("Population Projections")
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    # legend
    ax.legend(loc='lower right')

    # ticks

    # format ticks to show million with suffix
    ax.yaxis.set_major_formatter(ticker.FuncFormatter((lambda x, _: '%1.0fM' %
                                                       (x*1e-6))))

    # set tick locations at intervals of 20 million
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20000000))
    ax.xaxis.set_major_locator(ticker.MaxNLocator(9))

    plt.show()


if __name__ == "__main__":
    main()
