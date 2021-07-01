import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None  # default='warn'

#
# Calculate yearly variations of happiness for determined country or region
#
# INPUTS:
# df: pandas dataframe [Mandatory]
# factor: happiness factor [Mandatory]
# country: country name [determine this or region only]
# region: region name [determine this or country only]
#  print_result: print resulting data
#
def extract_yearly_variations_of_happiness(df, factor, country=None, region=None, print_result=False):

    ordering = [*range(2005, 2022)]

    if country is None:
        dataframe = df[df['Regional indicator'] == region]
        dataframe = dataframe.groupby(by="year")[[factor]].mean()
        dataframe = dataframe.reindex(index=ordering)

        label = region

    else:
        dataframe = df[df['Country name'] == country]
        dataframe = dataframe.groupby(by="year")[[factor]].sum()
        dataframe = dataframe.reindex(index=ordering)

        label = country

    # Plot result data
    # plt.figure()
    ax = dataframe.plot.bar(stacked=False, title=label + " happiness score over time")
    ax.set_ylabel(factor + " score")
    ax.set_xlabel("Year")
    plt.show()

    # Print result data
    if print_result:
        print("-------------------- REPORT ----------------------")
        print(label + "happiness report according " + factor)
        print(dataframe.to_string())

    return dataframe


#
# Generate heat map from data
#
# INPUTS:
# df: pandas dataframe [Mandatory]
#
def generate_data_heat_map(df):
    fig_dims = (20, 8)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.heatmap(df[['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth',
                    'Freedom to make life choices', 'Generosity',
                    'Perceptions of corruption']].corr(), annot=True, cmap="YlGnBu")
    plt.show()


#
# Calculate average of happiness scores over each year for determied country or region
#
# INPUTS:
# df: pandas dataframe [Mandatory]
# from_column: starting column name [Mandatory]
# from_column: ending column name [Mandatory]
# country: country name [determine this or region only]
# region: region name [determine this or country only]
#  print_result: print resulting data
#
def calculate_average_happiness_score(df, from_column, till_column, country=None, region=None, print_result=False):

    # Define ordering list
    ordering = [*range(2005, 2022)]

    # Calculate row-wise mean and add it as a new column to data
    col = df.loc[:, from_column:till_column]
    df['HDI'] = col.mean(axis=1)

    # Query data by region or country
    if country is None:
        df = df[df['Regional indicator'] == region]
        df = df.groupby(by="year")[['HDI']].mean()
        df = df.reindex(index=ordering)

        label = region
    else:
        df = df[df['Country name'] == country]
        df = df.groupby(by="year")[['HDI']].mean()
        df = df.reindex(index=ordering)

        label = country

    # Print result
    if print_result:
        print(df.to_string())

    # Plot result data
    ax = df.plot.bar(stacked=False, title=label + " mean of factors over time")
    ax.set_ylabel("HDI score")
    ax.set_xlabel("Year")
    plt.show()


#
# Determine each factor impact and plot result over years
#
# INPUTS:
# df: pandas dataframe [Mandatory]
# print_result: print resulting data
#
def plot_factor_responsibility_for_happiness_rate_over_years(df, print_result=False):
    # The 6 major factors that determine the
    # happiness rates of a country are: Ladder score, Log GDP per capita, Social support, Healthy life expectancy at birth,
    # Freedom to make life choices, Generosity, Perceptions of corruption

    # Define ordering list
    ordering = [*range(2005, 2022)]

    # Select interested data
    Exp = df[["year", "Life Ladder", "Log GDP per capita", "Social support", "Healthy life expectancy at birth",
               "Freedom to make life choices", "Generosity", "Perceptions of corruption"]]

    # Group data according to year
    Exp_mean = Exp.groupby(by="year")[["Life Ladder", "Log GDP per capita", "Social support",
                                       "Healthy life expectancy at birth",
                                       "Freedom to make life choices", "Generosity",
                                       "Perceptions of corruption"]].mean()
    # Print data
    if print_result:
        print(Exp_mean.to_string())

    # Plot results
    Exp_mean.reindex(index=ordering).plot.barh(stacked=True, colormap='Spectral')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.title("How each factor contributed to happiness score (Year)", fontsize="10")
    plt.show()


#
# Determine each factor impact and plot result for every regions
#
# INPUTS:
# df: pandas dataframe [Mandatory]
# print_result: print resulting data
#
def plot_factor_responsibility_for_happiness_region(df, print_result=False):
    # The 6 major factors that determine the
    # happiness rates of a country are: Ladder score, Log GDP per capita, Social support, Healthy life expectancy at birth,
    # Freedom to make life choices, Generosity, Perceptions of corruption

    # Define ordering list
    ordering = ['North America and ANZ',
                'Western Europe', 'Central and Eastern Europe',
                'Latin America and Caribbean', 'East Asia',
                'Commonwealth of Independent States', 'Southeast Asia',
                'Middle East and North Africa',
                'Sub-Saharan Africa', 'South Asia']

    # Select interested columns
    Exp = df[["Country name", "Regional indicator", "Life Ladder", "Log GDP per capita", "Social support",
              "Healthy life expectancy at birth", "Freedom to make life choices", "Generosity",
              "Perceptions of corruption"]]

    # Group data and calculate row-wise mean
    Exp_mean = Exp.groupby(by="Regional indicator")[["Log GDP per capita", "Social support",
                                       "Healthy life expectancy at birth",
                                       "Freedom to make life choices", "Generosity",
                                       "Perceptions of corruption"]].mean()

    # If determined, prent data
    if print_result:
        print(Exp_mean.to_string())

    # Plot result
    Exp_mean.reindex(index=ordering).plot.barh(stacked=True, colormap='Spectral')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.title("How each factor contributed to happiness score (Region)", fontsize="12")
    plt.show()
