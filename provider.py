import pandas as pd

WORLD_HAPPINESS_REPORT_FILENAME = "world-happiness-report.csv"
WORLD_HAPPINESS_REPORT_2021_FILENAME = "world-happiness-report-2021.csv"

def read_and_prepare_old_data():
    # Read data
    df = pd.read_csv("Datasets/" + WORLD_HAPPINESS_REPORT_FILENAME)

    # Drop useless columns
    df = df.drop(
        ['Positive affect', 'Negative affect'],
        axis=1)

    # Check for null values in data
    # print(df.columns.isnull().sum())
    # there are no null values in the dataset so we can continue

    # Fill NaN data with 0
    df = df.fillna(0)

    return df


def read_and_prepare_2021_data():
    # Read data
    df = pd.read_csv("Datasets/" + WORLD_HAPPINESS_REPORT_2021_FILENAME)

    # Drop useless columns
    df = df.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Dystopia + residual', 'Regional indicator',
                   'Explained by: Log GDP per capita', 'Explained by: Social support',
                   'Explained by: Healthy life expectancy',
                   'Explained by: Freedom to make life choices',
                   'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Ladder score in Dystopia'],
                  axis=1)

    # Check for null values
    # print(df.columns.isnull().sum())
    # there are no null values in the dataset so we can continue

    # Rename columns to become similar to old data
    df = df.rename(columns={'Ladder score': 'Life Ladder',
                       'Logged GDP per capita': 'Log GDP per capita',
                       'Healthy life expectancy': 'Healthy life expectancy at birth'})

    # Fill NaN data with 0
    df = df.fillna(0)

    # Insert 2021 year column in data
    df.insert(1, "year", [element * 2021 for element in [1] * df.shape[0]])

    return df


def read_and_prepare_2021_data_with_region_indicator():
    # Read data
    df = pd.read_csv("Datasets/" + WORLD_HAPPINESS_REPORT_2021_FILENAME)

    # Drop useless columns
    df = df.drop(['Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Dystopia + residual',
                   'Explained by: Log GDP per capita', 'Explained by: Social support',
                   'Explained by: Healthy life expectancy',
                   'Explained by: Freedom to make life choices',
                   'Explained by: Generosity', 'Explained by: Perceptions of corruption', 'Ladder score in Dystopia'],
                  axis=1)

    # Check for null values
    # print(df.columns.isnull().sum())
    # there are no null values in the dataset so we can continue

    # Rename columns to become similar to old data
    df = df.rename(columns={'Ladder score': 'Life Ladder',
                       'Logged GDP per capita': 'Log GDP per capita',
                       'Healthy life expectancy': 'Healthy life expectancy at birth'})

    # Fill NaN data with 0
    df = df.fillna(0)

    # Insert 2021 year column in data
    df.insert(1, "year", [element * 2021 for element in [1] * df.shape[0]])

    return df
