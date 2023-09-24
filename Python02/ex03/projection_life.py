import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def handleData(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts and processes data from the dataframe.

    @param df: dataframe
    @return processed_df: dataframe after processing
    """

    # get dataframe containing all rows with column
    processed_df = df.loc[:, ["country", "1900"]]

    # dict for storing conversion factors
    tens = dict(k=1000, M=1000000)

    # process dataframe by converting values with suffixes to int repr
    processed_df = (processed_df.iloc[:, 1]
                    .apply((lambda x: int(float(x[0:-1]) * tens[x[-1]])
                            if isinstance(x, (int, float)) is False else x))
                    )

    return processed_df


def main():
    """
    Program that plots a scatter graph on Gross Domestic Product vs
    life expectancy of each country based on the data in the csvs'.
    """

    # data frames
    gdp_df = load("../income_per_person_gdppercapita_ppp_inflation_adjusted\
.csv")
    life_df = load("../life_expectancy_years.csv")

    gdp_df = handleData(gdp_df)
    life_df = handleData(life_df)

    gdp = gdp_df.values.flatten()
    life = life_df.values.flatten()

    # new figure object
    fig = plt.figure()

    # new subplot object
    ax = fig.add_subplot(111)

    ax.scatter(gdp, life, color='r')

    # labels
    ax.set_title("1900")
    ax.set_xlabel('Gross Domestic Product')
    ax.set_ylabel('Life Expectancy')

    # ticks
    ax.set_xticks([300, 1000, 10000])
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=1.05, numticks=15))

    plt.show()


if __name__ == "__main__":
    main()
