# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
pandas Cookbook
"""
A quick tour of IPython Notebook
This tour will work a little better in interactive mode, so it'll be better if you get IPython notebook installed and running. You can start it from a terminal by running

ipython notebook

First, we need to explain how to run cells. Try to run the cell below!

import pandas as pd

print "Hi! This is a cell. Press the ▶ button above to run it"
You can also run a cell with Ctrl+Enter or Shift+Enter. Experiment a bit with that.

One of the most useful things about IPython notebook is its tab completion.

Try this: click just after read_csv( in the cell below and press Shift+Tab (or Tab if you're using IPython 1.x) 4 times, slowly

pd.read_csv(
After the first time, you should see this:


After the second time:


After the fourth time, a big help box should pop up at the bottom of the screen, with the full documentation for the read_csv function:


I find this amazingly useful. I think of this as "the more confused I am, the more times I should press Shift+Tab". Nothing bad will happen if you tab complete 12 times.

Okay, let's try tab completion for function names!

pd.r
You should see this:


Writing code
Writing code in the notebook is pretty normal.

def print_10_nums():
    for i in range(10):
        print i,
print_10_nums()
0 1 2 3 4 5 6 7 8 9
Saving
As of the latest stable version, the notebook autosaves. You should use the latest stable version. Really.

Magic functions
IPython has all kinds of magic functions. Here's an example of comparing sum() with a list comprehension to a generator comprehension using the %time magic.

%time sum([x for x in range(100000)])
CPU times: user 24 ms, sys: 4 ms, total: 28 ms
Wall time: 27.4 ms
4999950000
%time sum(x for x in range(100000))
CPU times: user 8 ms, sys: 0 ns, total: 8 ms
Wall time: 8.11 ms
4999950000
The magics I use most are %time and %prun for profiling. You can run %magic to get a list of all of them, and %quickref for a reference sheet.

%quickref
You can also do nutty things like run Perl code in the notebook with cell magics. This is especially cool for things like Cython code, where you can try out Cython really fast with the %%cython magic (you'll need to install it).

%%perl

$_ = "whoa, python!";
s/python/perl/;
print
whoa, perl!