# HouseNumbering

This is a Qgis plugin to auto generate civic house numbers with auto increment values rules.

Was designed with italian based address numbering rules.

It can also be used to enumerate elements, upgrading result values into a desired field.

It can enumerate elements starting by start value, increased by step and then stored
into the field selected from fields listbox, the destination field must be a character field type.

If there is a letter in start value ( 1a or 2A ...) it keep fixed the numeric part and only the letter parts 
will be increased: 1a,1b,1c... or 2A,2B,2C... 

To keep letter fixed and to increase, by step amount, the number part:

start value (1a or 2A ...)  step = 1 
with checkbox option "keep letter fixed..." flagged
result: 1a,2a,3a or 1A,2A,3A  

