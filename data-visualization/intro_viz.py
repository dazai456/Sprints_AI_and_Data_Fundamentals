# ------------------------------------------------------------------------------
# Install all required libraries and verify each import works in a single script
# ------------------------------------------------------------------------------
import matplotlib
import seaborn as sns
import plotly
import bokeh

print("Matplotlib version:", matplotlib.__version__)
print("Seaborn version:", sns.__version__)
print("Plotly version:", plotly.__version__)
print("Bokeh version:", bokeh.__version__)

# ------------------------------
# Why Data Visualization Matters
# ------------------------------
'''
When you look at a raw Pandas DataFrame of 10,000 rows, 
your brain has to work hard to compute averages, spot outliers, or recognize trends. 
A well-designed chart turns numbers into instant insights, allowing you to spot anomalies, clusters, and directions in milliseconds.

'''

# -----------------------
# most common chart types
# -----------------------
'''
Line Chart: A continuous line connecting data points, ideal for tracking changes over time (time-series).

Bar Chart: Rectangular bars (vertical or horizontal) representing discrete categories, where the length or height corresponds to a value.

Scatter Plot: Individual dots plotted on an X-Y Cartesian plane to show the relationship between two numerical variables.

Histogram: A specialized bar chart that groups continuous numerical data into bins to show its frequency distribution.

Pie Chart: A circular graphic divided into slices to illustrate numerical proportions (best kept to 5 or fewer categories).

Box Plot: A standardized way of displaying the statistical distribution of data based on a five-number summary 
    (minimum, first quartile, median, third quartile, maximum, and outliers).

Heatmap: A 2D grid where individual values are represented by colors, excellent for correlation matrices or density maps.

Area Chart: Similar to a line chart, but the area below the line is filled with color to emphasize volume or cumulative totals over time.

'''

# -----------------------
# when to use which chart
# -----------------------
'''

'''

# ------------------------------
# Basic Colour Theory for Charts
# ------------------------------
'''
Qualitative (Categorical) Palettes: Used for distinct, unrelated groups (e.g., different directors, genres, or departments). 
    Colors should be visually distinct from one another.

Sequential Palettes: Uses variations of a single hue (light to dark) to represent ordered numerical data 
    where values increase from low to high (e.g., low votes to high votes).
    
Diverging Palettes: Uses two contrasting hues meeting at a neutral midpoint (e.g., blue for negative, white for zero, red for positive). 
    Perfect for correlation matrices, profit/loss, or deviations from an average.

Colour-Blind Safety: Approximately 8% of men and 0.5% of women have color vision deficiencies (most commonly red-green).
    Always rely on color-blind-friendly palettes
'''

# --------------------------------------
# Describe common visualisation pitfalls
# --------------------------------------
'''
Truncated Axes: Starting a bar chart axis above zero exaggerates differences between categories, making small variations look massive.

Misleading Scales: Using dual axes with mismatched scales or uneven intervals, which can force two unrelated trends to look artificially correlated.

3-D Distortion: Adding 3-D depth to bar or pie charts distorts visual proportions, making it nearly impossible to accurately read data values.

Chart Junk: Overloading a graphic with unnecessary gridlines, distracting background images, heavy borders, or redundant text that clutters the message.
'''

# ----------------------------------
# the Python visualisation ecosystem
# ----------------------------------

'''
Matplotlib: The foundational plotting library in Python.
    Strengths: Ultimate, pixel-level control over every aspect of a figure; highly customizable.
    Trade-offs: Verbose syntax; requires a lot of boilerplate code for clean-looking plots.

Seaborn: Built on top of Matplotlib, specifically designed for statistical graphics.
    Strengths: Beautiful default aesthetics; handles Pandas DataFrames natively with minimal code.
    Trade-offs: Less flexible when you need completely non-standard layouts outside its statistical scope.

Plotly: A library built for interactive, web-ready visualizations.
    Strengths: Interactive tooltips, zoom, and pan capabilities; perfect for dashboards.
    Trade-offs: Generates heavier file sizes and can render slowly on massive datasets.

Bokeh: Focuses on interactive visualizations for modern web browsers.
    Strengths: Great for streaming data and building complex interactive web applications.
    Trade-offs: Steeper learning curve compared to Plotly and Seaborn.
'''

# ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# ------------------------------
# Exercise: given a small dataset, decide which chart type is best for 4 different questions and justify your choice in comments.
# ------------------------------
# ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
