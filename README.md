Auralise
========
Transforming time series data to sound. An attempt was made.

Turns out, using data to make music is a lot harder than it sounds (no pun intended), especially without an intimate understanding of what makes a Sine wave special. Still, it does something and doesn't sound too terrible, though it doesn't show a trend in quite the same way as I had hoped.

To run:
* Uses Pyo to [Pyo](http://ajaxsoundstudio.com/software/pyo/) to make the sweet music. Annoyingly, they don't have a ready made binary for Python 3.7, so you need to [compile manually](http://ajaxsoundstudio.com/pyodoc/compiling.html).
* requirements.txt holds the rest of the dependencies.
* All a lot easier if you do it within a [Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* Run auralise.py (don't blame me if you have to manually kill the process if it decides to keep singing at you once its finished) 