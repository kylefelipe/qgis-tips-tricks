# -*- coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='String')
def wrap_delimiter(text, delimiter, feature, parent):
	"""<p>Returns a string wrapped to a delimiter</p>
	<p><h4>Syntax </h4> wrap_delimiter(string, delimiter)</p>
	<p><h4>Arguments</h4></p>
	<p>string = string to be wrapped</p>
	<p>delimiter = the delimiter string to wrap to a new line</p>
	<p><h4>Example</h4> wrap-delimiter('don't panic, it will be wrapped', ',')</p>
	<p><h4>Result</h4></p>
	<p>don't panic</p>
	<p>it will be wrapped</p>
	"""
	t = str(text).replace(delimiter+' ', delimiter)
	return str(t).replace(delimiter, "\n")
