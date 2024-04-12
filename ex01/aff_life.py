from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plt_plot(df: pd.DataFrame, country: str) -> None:

    # Filter data for the given country
    country_data = df.loc[df['country'] == country]
    country_data = country_data.iloc[:, 1:].to_numpy().flatten()
    years = [int(year) for year in df.columns[1:]]

    # Plot the data
    plt.plot(years, country_data)

    plt.title(f'{country} Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()


def seaborn_plot(df: pd.DataFrame, country: str) -> None:
    # Filter data for the given country
    country_data = df.loc[df['country'] == country]
    country_data = country_data.iloc[:, 1:].to_numpy().flatten()
    years = [int(year) for year in df.columns[1:]]

    # Create dataframe to give seaborn
    data = pd.DataFrame({
        'Year': years,
        'Life Expectancy': country_data
    })

    sns.lineplot(x='Year', y='Life Expectancy', data=data)

    plt.title(f'{country} Life expectancy Projections')
    plt.show()



def main():
    population_df = load("life_expectancy_years.csv")
    plt_plot(population_df, "France")
    seaborn_plot(population_df, "France")


if __name__ == "__main__":
    main()
