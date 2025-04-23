#Curve fitting is a super important skill. These problems should help you get
#more comfortable with:
#• curve fitting (using scipy.optimize.curve fit, pandas, and matplotlib)
#(you’ll need this for your final project!)
#• covariance matrices and error
#• data cleaning, processing, and visualization
#1 Curve Fitting Guided Problem
#The following problem will walk you through how to fit a tricky curve to a set
#of data.
#This problem looks super long, but it’s not :)
#1.1
#Use pandas to do the following:
#1. Read in the file “GlobalLandTemperaturesByState.csv”.
#2. Filter the table to include only the columns for the date, temperature,
#and state.
#3. Filter the table to include only years after 2000.
#4. Filter the table to include only the rows corresponding to Wyoming, Ne-
#braska, or South Dakota. Check: your table should be 495 rows and 3
#columns.

import pandas as pd

#1
global_land_temps_by_state = pd.read_csv("GlobalLandTemperaturesByState.csv")

#2
global_land_temps_by_state = global_land_temps_by_state[['dt', 'AverageTemperature', 'State']]

#3
global_land_temps_by_state = global_land_temps_by_state[global_land_temps_by_state['dt'].str[:4].astype(int) >= 2000]

#4
states = ['Wyoming', 'Nebraska', 'South Dakota']
global_land_temps_by_state = global_land_temps_by_state[global_land_temps_by_state['State'].isin(states)]

#check
print(global_land_temps_by_state.shape)



#Modify the table such that it contains the average temperature over all three
#states for each date. It should have two columns: date and average temperature.
avg_temp_by_date = global_land_temps_by_state.groupby('dt')['AverageTemperature'].mean().reset_index()
avg_temp_by_date.columns = ['Date', 'AverageTemperature']

print(avg_temp_by_date.head())

#Use matplotlib.pyplot to plot the data from the table you created above. You
#can pass pandas columns directly into matplotlib.pyplot without needing to
#turn them into arrays.
#1. Date on the x axis, average temperature on the y axis.
#2. Label the axis and give the graph a title

import matplotlib.pyplot as plt

# Plotting the data
plt.figure(figsize=(12, 3))
plt.plot(avg_temp_by_date['Date'], avg_temp_by_date['AverageTemperature'])

# Labels and title
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature Over Time (Wyoming, Nebraska, South Dakota)')

# Optional: improve date formatting
plt.xticks(rotation=45)
plt.tight_layout()

#plt.show()

#The function scipy.optimize, unsurprisingly, can only do math with numbers.
#The date column of the table is currently composed of strings.
#• Fix this and convert the string date into numerical values however you
#see fit, and make it a column in the dataframe. Your numerical values
#should capture all parts of the date provided in the string (don’t use just
#the year, etc)

 # Convert the 'Date' column to datetime (if not already)
avg_temp_by_date['Date'] = pd.to_datetime(avg_temp_by_date['Date'])

# Add a column with numerical date values (ordinal)
# Convert the 'Date' column to string (if it's datetime) and remove dashes
avg_temp_by_date['Date_Numeric'] = avg_temp_by_date['Date'].astype(str).str.replace('-', '').astype(int)

print(avg_temp_by_date.head())

#The function scipy.optimize requires: a model equation, and an initial guess
#of parameters. For this section:
#1. Define an appropriate model equation. Use a generic form like mx + b:
#there should be four parameters.
#2. Make an initial guess at the parameters and save them in an array.
#• This part is really important. A dataset with a non polynomial pat-
#tern was chosen for a reason: your initial guesses matter, particularly
#the period.
#• If you’re stuck, eyeball the length of the period (it should make phys-
#ical sense, and remember that the units are in years) and keep this
#in mind: cos(2x) means the function covers two periods in the space
#of 2π.2 ∗ period = 2π, so each period is π long.

import numpy as np

# Model function
def temp_model(x, a, b, c, d):
    return a * np.cos(b * x + c) + d

# Initial guess: [amplitude, frequency, phase shift, vertical shift]
new_guess = [10, 0.0002, 0, 5]

#1.6
#Run scipy.optimize’s curve fit function! Remember that it outputs a tuple
#containing two arrays: the parameter array and the covariance matrix.
#• If while attempting this, you get one of the following errors:
#– Something about maximum depth
#– Something about not being able to estimate the covariance
#– A line that does not fit the data at all
#You may need to re-examine your guesses for the initial parameters (par-
#ticularly the period). This is why plotting the data before fitting it is
#critical.

from scipy.optimize import curve_fit
import numpy as np

# Convert Date to numeric: as years + fraction (so no have huge values like 20010101)
avg_temp_by_date['Date_Years'] = avg_temp_by_date['Date'].apply(lambda x: x.year + x.month / 12 + x.day / 365)
x_data = avg_temp_by_date['Date_Years'].values
y_data = avg_temp_by_date['AverageTemperature'].values

new_guess = [10, 2 * np.pi, 0, 5]

params, covariance = curve_fit(temp_model, x_data, y_data, p0=new_guess)

print("Fitted parameters:", params)

plt.figure(figsize=(12,6))
plt.plot(x_data, y_data, label="Actual Data")
plt.plot(x_data, temp_model(x_data, *params), label="Fitted Model", color='red')
plt.xlabel("Years")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Fit with Cosine Model")
plt.legend()
plt.show()
