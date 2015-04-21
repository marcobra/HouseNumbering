# HouseNumbering

This is a Qgis plugin to auto generate civic house numbers with auto increment values rules.

Was designed with italian based address numbering rules.

It can also be used to enumerate elements, upgrading result values into a desired field.

It can enumerate elements starting by start value, increased by step and then stored
into the field selected from fields listbox, the destination field must be a character field type.

If there is a letter in start value ( 1a or 2A ...) it keep fixed the numeric part and only the letter parts 
will be increased: 1a,1b,1c... or 2A,2B,2C... 

To keep letter fixed and to increase, by step amount, the number part only, set:<br>
start value (1a or 2A ...)<br>
step = 1<br>
flag the checkbox option "based on... keep letter fixed..."<br>
result will be: 1a,2a,3a or 1A,2A,3A<br>

The selected elements are processed with same sequence as they were inserted.

To get ordered increasing numbers on singles points, on geometrical position that differ from inserting sequence, select desired point press "F10" and then enter, the numbering rule will generate correct value for that point.

