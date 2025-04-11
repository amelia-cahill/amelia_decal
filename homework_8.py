#HW 8

#1 Introduction to Matplotlib
#Your goal is to use matplotlib.pyplot and NumPy to plot several sine waves
#by looping through amplitude and frequency values.

import numpy as np
import matplotlib as plt

#1. Write a function make sine wave(x, A, w) that returns:
#y = A · sin(w · x)
#where x is an array, A is amplitude, and w is angular frequency.
def make_sine_wave(x, A, w):
    y= A * np.sin(w * x)
    return y

# 2. Create an array x using NumPy that goes from 0 to 2π with 1000 points.
x = np.linspace(0, 2 * np.pi, 1000)

# 3. Amplitude and frequency arrays with the given values 
amplitudes = [0.5, 1, 1.5, 2, 2.5]
frequencies = [1, 2, 3, 4, 5]

# different line styles
line_styles = ['-', '--', '-.', ':', 'solid']  

#4. Create a figure using plt.figure(). Give an appropriate value for the
#figsize argument.
plt.figure(figsize=(10, 6))

# 5. Loop through amplitude and frequency values
for A, w, linesty in zip(amplitudes, frequencies, line_styles):
    y = make_sine_wave(x, A, w) #Call your sine wave function to get y.
    plt.plot(x, y, linestyle = linesty, label=f"A={A}, w={w}")

# 6. Add plot labels and show the figure
plt.title("Sine Waves with Different Amplitude and Frequency Values")
plt.xlabel("x")
plt.ylabel("y = A · sin(w · x)")
plt.legend()
plt.grid(True)
plt.show()

#2 Data with Pandas
#Use pandas to explore a dataset of nearby stars and their properties. You’ll
#load the data, inspect it, and answer questions about different types of stars.
#1. Load the data from stars.csv into a pandas DataFrame using pandas.read csv().
#2. Print:
#• The first 5 rows.
#• The number of rows and columns.
#• The column names and data types.
#3. Calculate:
#• The average mass and temperature of the stars.
#• The star with the largest radius.
#• How many stars have a spectral type starting with ‘‘M" (M-type
#stars).
#4. Sort the stars by distance and show the 3 closest ones.
#5. Save a filtered DataFrame of only M-type stars to a new file called m type stars.csv.
import pandas

stars = pandas.read_csv('stars.csv')
print(stars.head(5))
rows, columns = stars.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
for col in stars.columns:
    print(f"Column Name: {col}, Data Type: {stars[col].dtype}")
average_mass = stars['Mass (M☉)'].mean()
print(f"Avg mass of stars: {average_mass}")
average_temp = stars['Temperature (K)'].mean()
print(f"Avg temperature of stars: {average_temp}")

max_radius = stars['Radius (R☉)'].max()
print(f"max radius: {max_radius}")
max_index = stars['Radius (R☉)'].idxmax()
max_star = stars.loc[max_index, 'Name']
print(max_star)

m_type_stars = stars[stars['Spectral_Type'].str.startswith('M')]
m_count = m_type_stars.sum()
print(f"Number of M-type stars: {m_count}")

closest_stars = stars.sort_values(by='Distance (ly)').head(3)
print(closest_stars)

m_type_stars.to_csv('m_type_stars.csv', index=False)

#3 Seaborn!
#Use seaborn to explore the penguins dataset, which includes measurements of
#different penguin species from the Palmer Archipelago in Antarctica.
#1. Load the dataset using:
#import seaborn as sns
#penguins = sns.load_dataset("penguins")
#Make sure matplotlib.pyplot is imported as well.
#2. Create a figure with 2 side-by-side subplots.
#3. For the leftmost plot, make a scatter plot using sns.scatterplot() and
#add a title, axis labels and a legend.
#4. For the leftmost plot, make a scatter plot using sns.scatterplot() and
#add a title, axis labels and a legend. For the rightmost plot, make a
#histogram using sns.histplot() to show the distribution of body mass
#for all the penguins.

import seaborn as sns
penguins = sns.load_dataset("penguins")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Bill Length vs Bill Depth (scatter plot)
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax1)
ax1.set_title("Bill Length vs Bill Depth")
ax1.set_xlabel("Bill Length (mm)")
ax1.set_ylabel("Bill Depth (mm)")

# Body Mass Distribution (histogram)
sns.histplot(data=penguins, x='body_mass_g', kde=True, ax=ax2, hue='species', bins=20)
ax2.set_title("Distribution of Body Mass")
ax2.set_xlabel("Body Mass (g)")
ax2.set_ylabel("Frequency")

plt.show()


