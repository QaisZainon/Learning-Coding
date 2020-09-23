# use bokeh to start visualising the data that you gathered
# you need to use two seperate lists
'''
from bokeh.plotting import figure, show, output_file
# we specify the HTML file for output
output_file('plot.html')
# load x and y data
x = [10, 20, 30]
y = [4, 5, 6]
# create a figure
p = figure()
# create a histogram
p.vbar(x = x, top = y, width = 0.5)
# render (show) the plot
show(p)
'''

from bokeh.plotting import figure, show, output_file
import json
from collections import Counter
def date_extracter():
    with open('Practice Python/Birthdaynames.json','r') as f:
        birthday_dict = json.load(f)
    month = ['January', 'Febuary', 'March', 'April', 'May', 'June',
    'July', 'August','September', 'October', 'November', 'December']
    birthday_counter = []
    for i in birthday_dict:
        load = birthday_dict[i].split('/')
        birthday_counter.append(month[int(load[1]) - 1])
    load = Counter(birthday_counter)
    x = list(load.keys())
    y = list(load.values())
    output_file('plot.html')
    p = figure(x_range = month)
    p.vbar(x = x, top = y, width = 0.5)
    show(p)
date_extracter()