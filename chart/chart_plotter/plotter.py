import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import plotly.offline as pyo 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#welcome
""" welcome = input('Do you want to proceed? Y/n\n')
if welcome == 'n':
    exit()
else:
    pass """

#here you can choose the period to show in the chart 

end = dt.datetime.now()

""" start_year = int(input('Start year:\n'))
start_month = int(input('Start month:\n'))
start_day = int(input('Start day:\n'))
start = dt.datetime(start_year,start_month,start_day) """

start = ''

#get data and print it to see if it works
df = pdr.get_data_yahoo('ETH-USD',start,end)
 
#create moving average
df['MA50'] = df['Close'].rolling(window=50, min_periods=0).mean()
df['MA200'] = df['Close'].rolling(window=200, min_periods=0).mean()

#create plotly fig / subplot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('ETH', 'Volume'), row_width=[0.2, 0.7])

#add open high low close candlestick graph
fig.add_trace(
    go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='OHLC'), row=1, col=1
)
#add moving average
fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], marker_color='blue', name='MA50'), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df['MA200'], marker_color='cyan', name='MA200'), row=1, col=1)

#volume bar chart
fig.add_trace(go.Bar(x=df.index, y=df['Volume'], marker_color='red',showlegend=False), row=2, col=1)

#update layout
fig.update_layout(
    title = 'Ethereum price',
    xaxis_tickfont_size = 12,
    yaxis = dict(
        title = 'Price ($/share)',
        titlefont_size = 14,
        tickfont_size = 12
    ),
    autosize = False,
    width=800,
    height=500,
    margin=dict(l=50,r=50,b=100,t=100,pad=5),
    paper_bgcolor = 'LightSteelBlue'
)

#remove rangeslider from subplot
fig.update(layout_xaxis_rangeslider_visible=False)

#show chart to user
fig.show()