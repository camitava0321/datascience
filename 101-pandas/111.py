# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Options and Customization
"""

#Pandas provide API to customize some aspects of its behavior, display is being mostly used.
"""
The API is composed of five relevant functions. They are −

    get_option()
    set_option()
    reset_option()
    describe_option()
    option_context()
"""
#Let us now understand how the functions operate.
#get_option(param)
#get_option takes a single parameter and returns the value as given in the output below −
display.max_rows

Displays the default number of value. Interpreter reads this value and displays the rows with this value as upper limit to display.

import pandas as pd
print pd.get_option("display.max_rows")

Its output is as follows −

60

display.max_columns

Displays the default number of value. Interpreter reads this value and displays the rows with this value as upper limit to display.

import pandas as pd
print pd.get_option("display.max_columns")

Its output is as follows −

20

Here, 60 and 20 are the default configuration parameter values.
set_option(param,value)

set_option takes two arguments and sets the value to the parameter as shown below −
display.max_rows

Using set_option(), we can change the default number of rows to be displayed.

import pandas as pd

pd.set_option("display.max_rows",80)

print pd.get_option("display.max_rows")

Its output is as follows −

80

display.max_rows

Using set_option(), we can change the default number of rows to be displayed.

import pandas as pd

pd.set_option("display.max_columns",30)

print pd.get_option("display.max_columns")

Its output is as follows −

30

reset_option(param)

reset_option takes an argument and sets the value back to the default value.
display.max_rows

Using reset_option(), we can change the value back to the default number of rows to be displayed.

import pandas as pd

pd.reset_option("display.max_rows")
print pd.get_option("display.max_rows")

Its output is as follows −

60

describe_option(param)

describe_option prints the description of the argument.
display.max_rows

Using reset_option(), we can change the value back to the default number of rows to be displayed.

import pandas as pd
pd.describe_option("display.max_rows")

Its output is as follows −

display.max_rows : int
   If max_rows is exceeded, switch to truncate view. Depending on
   'large_repr', objects are either centrally truncated or printed as
   a summary view. 'None' value means unlimited.

   In case python/IPython is running in a terminal and `large_repr`
   equals 'truncate' this can be set to 0 and pandas will auto-detect
   the height of the terminal and print a truncated object which fits
   the screen height. The IPython notebook, IPython qtconsole, or
   IDLE do not run in a terminal and hence it is not possible to do
   correct auto-detection.
   [default: 60] [currently: 60]

option_context()

option_context context manager is used to set the option in with statement temporarily. Option values are restored automatically when you exit the with block −
display.max_rows

Using option_context(), we can set the value temporarily.

import pandas as pd
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))

Its output is as follows −

10
10

See, the difference between the first and the second print statements. The first statement prints the value set by option_context() which is temporary within the with context itself. After the with context, the second print statement prints the configured value.
Frequently used Parameters
S.No 	Parameter 	Description
1 	display.max_rows 	Displays maximum number of rows to display
2 	2 display.max_columns 	Displays maximum number of columns to display
3 	display.expand_frame_repr 	Displays DataFrames to Stretch Pages
4 	display.max_colwidth 	Displays maximum column width
5 	display.precision 	Displays precision for decimal numbers