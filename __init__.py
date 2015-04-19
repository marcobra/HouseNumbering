# --------------------------------------------------------
#    __init__ - HouseNumbering init file
#
#    begin                : June 5, 2014
#    copyright            : (c) 2014 by Marco Braida
#    email                : See marcobra.ubuntu at gmail.com
#
#   HouseNumbering is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------

from HouseNumbering_menu import HouseNumbering_menu

def name():
	return "HouseNumbering"

def description():
	return "Edit and assign an increasing value for the input elements"

def version():
	return "0.0.2"

def qgisMinimumVersion():
	return "2.0"

def authorName():
	return "Marco Braida"

def icon():
    return "icons/housenumbering.png"
	
def classFactory(iface):
	return HouseNumbering_menu(iface)
