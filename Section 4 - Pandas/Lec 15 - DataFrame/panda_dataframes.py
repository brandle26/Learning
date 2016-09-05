import numpy as np

import pandas as pd

from pandas import Series, DataFrame

import webbrowser

website="https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records"

webbrowser.open(website)

nfl_frame=pd.read_clipboard()
print(nfl_frame)


