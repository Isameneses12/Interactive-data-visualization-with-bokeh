'''You can create Bokeh plots from Pandas DataFrames by passing column selections to the glyph functions.
Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read 
a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.
The CSV file is provided for you as 'auto.csv'.
Your job is to plot miles-per-gallon (mpg) vs horsepower (hp) by passing Pandas column selections into the
p.circle() function. Additionally, each glyph will be colored according to values in the color column.'''


# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv("auto.csv")

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(df["hp"], df["mpg"], color= df["color"], size= 10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle("Year", "Time", source= source, color= "color", size= 8)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label= "Year", y_axis_label="Time", tools= "box_select")

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle("Year", "Time", source= source, selection_color= "red", nonselection_alpha= 0.1)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color="grey", alpha=0.1, line_color=None,
         hover_fill_color="firebrick", hover_alpha=0.5,
         hover_line_color="white")

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode= "vline")

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle("weight", 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)
