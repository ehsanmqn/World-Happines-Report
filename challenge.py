from __future__ import print_function
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


from provider import read_and_prepare_old_data, read_and_prepare_2021_data_with_region_indicator
from analysis import extract_yearly_variations_of_happiness, generate_data_heat_map, calculate_average_happiness_score, \
    plot_factor_responsibility_for_happiness_rate_over_years, plot_factor_responsibility_for_happiness_region


# Initialize jinja
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/report.html")

# Read old and 2021 data
df_old = read_and_prepare_old_data()
df_2021 = read_and_prepare_2021_data_with_region_indicator()

# Merge old and 2021 data frames together
frames = [df_old, df_2021]
df = pd.concat(frames)
df = df.fillna(0)

# Create Country to Region map
region_map = dict(df_2021[['Country name', 'Regional indicator']].values)

# Fill old data Region indicator based on 2021 values
for index, row in df.iterrows():
    if row['Regional indicator'] == 0:
        try:
            df.at[index, 'Regional indicator'] = region_map[row['Country name']]
        except:
            # If it does not find, place 'Not determined'
            df.at[index, 'Regional indicator'] = 'Not determined'

df = df.reset_index()
# print(df.to_string())


# Generate heat map to explore co-relation between indices
generate_data_heat_map(df)
# From the heat map, it is pretty evident that most of the data fields have a strong relation between them.


# Generate yearly happiness variation report according to a selected index (In this example Life Ladder)
interested_data = extract_yearly_variations_of_happiness(df,
                                     country="Yemen",           # Coment this and uncomment region if you want calculate report for a region
                                     # region="South Asia",
                                     factor="Life Ladder",
                                     print_result=False)

# Let's calculate the mean of factors provided for the rate of happiness.
calculate_average_happiness_score(df,
                                  from_column="Life Ladder",
                                  till_column="Regional indicator",
                                  # country="Yemen",            # Coment this and uncomment region if you want calculate report for a region
                                  region="South Asia",
                                  print_result=False)


# Let's calculate the each factor responsibility for the rates of happiness over years
plot_factor_responsibility_for_happiness_rate_over_years(df)

# Let's calculate the each factor responsibility for the rates of happiness for each region
plot_factor_responsibility_for_happiness_region(df)

# Generate PDF report from variation of happiness over years
template_vars = {"title" : "Happiness report",
                 "interested_data": interested_data.to_html()}
html_out = template.render(template_vars)
HTML(string=html_out).write_pdf("report.pdf")


