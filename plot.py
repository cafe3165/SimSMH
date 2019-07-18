# 3、堆叠图

from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure,show
# 导入value模块

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
colors = ["#254e7b", "#85c1e5", "#cde6f4"]
data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}
# df = pd.DataFrame(data)
# print(df)
# source = ColumnDataSource(data = df) #也可以使用DataFrame
source = ColumnDataSource(data=data)


# 创建数据

p = figure(x_range=fruits, plot_height=350, title="Fruit Counts by Year",tools="")
renderers = p.vbar_stack(["2015", "2016", "2017"], #可以用years代替，就是上边设置的变量 # 设置堆叠值，这里source中包含了不同年份的值，years变量用于识别不同堆叠层
                         x='fruits',     # 设置x坐标
                         source=source, #包含了2015/2016/2017的数据的；  主要设置的就是这3个参数
                         width=0.9, color=colors,
                         legend=[value(x) for x in years], name=years) #对整个数据做一个分组集合变成一个列表
# 绘制堆叠图
# 注意第一个参数需要放years

p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
# 设置其他参数

show(p)
[value(x) for x in years]