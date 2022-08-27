from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

output_file('plot.html')

df["Start_Formatted"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_Formatted"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", height = 100, width = 500, sizing_mode="scale_both", title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1



hover = HoverTool(tooltips=[("Start: ", "@Start_Formatted"), ("End: ", "@End_Formatted")])
p.add_tools(hover)

#Without Data Source
#q = p.quad(top=1, bottom=0, left=df["Start"], right=df["End"], color="green")

#With DataSource, Column name should come from datasource
q = p.quad(top=1, bottom=0, left="Start", right="End", color="green", source = cds)
show(p)