from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


def process_population(population: str) -> float:
    if population.endswith('M'):
        return float(population.replace('M', ''))*1e6
    elif population.endswith('k'):
        return float(population.replace('k', ''))*1e3
    else:
        return float(population)


def custom_formatter(x, pos):
    if x >= 1e6:
        return f'{int(x*1e-6)}M'
    elif x >= 1e3:
        return f'{int(x*1e-3)}K'
    else:
        return str(int(x))


def filter_country_data(df: pd.DataFrame, country: str, num_years: int) -> any:
    country_data = df.loc[df['country'] == country]
    country_data = country_data.iloc[:, 1:num_years + 1].to_numpy().flatten()
    country_data = [process_population(pop) for pop in country_data]
    return country_data


def plt_plot(df: pd.DataFrame, country_one: str, country_two: str) -> None:

    years = list(range(1800, 2051))

    num_years = len(years)

    # Filter data for the first given countries
    country_one_data = filter_country_data(df, country_one, num_years)
    country_two_data = filter_country_data(df, country_two, num_years)

    # Plot the data
    plt.plot(years, country_one_data)
    plt.plot(years, country_two_data)

    # Using FuncFormatter to create a formatter that multiplies the tick value by 1e-6
    formatter = ticker.FuncFormatter(custom_formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend([country_one, country_two], loc=2)
    plt.show()


def seaborn_plot(df: pd.DataFrame, country_one: str, country_two: str) -> None:
    years = list(range(1800, 2051))
    num_years = len(years)

    # Filter data for the first given countries
    country_one_data = filter_country_data(df, country_one, num_years)
    country_two_data = filter_country_data(df, country_two, num_years)


    # Create dataframe to give seaborn
    data_country_one = pd.DataFrame({
        'Year': years,
        'Population': country_one_data
    })
    data_country_two = pd.DataFrame({
        'Year': years,
        'Population': country_two_data
    })

    sns.lineplot(x='Year', y='Population', data=data_country_one)
    sns.lineplot(x='Year', y='Population', data=data_country_two)

    formatter = ticker.FuncFormatter(custom_formatter)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.title('Population Projections')
    plt.legend([country_one, country_two], loc=2)
    plt.show()


def main():
    # Load dataset into a dataframe
    population_df = load("population_total.csv")

    # Matplotlib plotting
    plt_plot(population_df, "Belgium", "France")
    plt_plot(population_df, "South Africa", "Moldova")
    plt_plot(population_df, "Singapore", "Venezuela")
    plt_plot(population_df, "Samoa", "Andorra")

    # Searborn plotting
    seaborn_plot(population_df, "Belgium", "France")
    seaborn_plot(population_df, "Belgium", "France")
    seaborn_plot(population_df, "South Africa", "Moldova")
    seaborn_plot(population_df, "Singapore", "Venezuela")
    seaborn_plot(population_df, "Samoa", "Andorra")

if __name__ == "__main__":
    main()
