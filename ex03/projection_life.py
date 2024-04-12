from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def process_data(data_to_process: str) -> float:
    if data_to_process.endswith('k'):
        print('nani')
        return float(data_to_process.replace('k', ''))*1e3
    else:
        return float(data_to_process)


def filter_year_data(df: pd.DataFrame, year: str) -> any:
    return [process_data(str(data_to_process)) for data_to_process in df[year]]


def plt_plot(df1: pd.DataFrame, df2: pd.DataFrame, year: str) -> None:

    year_data_df1 = df1[year]
    year_data_df2 = df2[year]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(year_data_df1, year_data_df2)
    ax.set_xlabel('Gross domestic product')
    ax.set_ylabel('Life Expectancy')
    ax.set_xscale("log")
    ax.set_title(year)
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def main():
    life_expect_df = load("life_expectancy_years.csv")
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    plt_plot(gdp_df, life_expect_df, '1900')
    plt_plot(gdp_df, life_expect_df, '2020')
    plt_plot(gdp_df, life_expect_df, '1850')
    plt_plot(gdp_df, life_expect_df, '1994')


if __name__ == "__main__":
    main()
