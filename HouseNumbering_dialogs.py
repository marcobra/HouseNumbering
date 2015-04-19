# --------------------------------------------------------
#    HouseNumbering_dialogs - Dialog classes for HouseNumbering
#
#    begin                : 01 Sep 2014
#    copyright            : (c) 2014 by Marco Braida
#    email                : See marcobra.ubuntu@gmail.com
#
#   HouseNumbering is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------

#import os.path
import operator
import tempfile
import datetime
import codecs

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import QgsMessageBar

from HouseNumbering_library import *


from os import path, access, R_OK

import sys
import re
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")

# --------------------------------------------------------
#    HouseNumbering_update_selected - Update selected feature field
# --------------------------------------------------------

from HouseNumbering_update_selected_form import *


class HouseNumbering_update_selected_dialog(QDialog, Ui_HouseNumbering_update_selected_form):
   def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)
        layer = self.iface.mapCanvas().currentLayer()
        delimchars = "#"
        if (layer) and layer.type() == QgsMapLayer.VectorLayer:
            if layer.type() == QgsMapLayer.VectorLayer:
                provider = layer.dataProvider()
                fields = provider.fields()
                self.QLEvalore.setText("")
                self.CBfields.clear()
                for f in fields:
                    self.CBfields.addItem(f.name(), f.name() )
                    nF = layer.selectedFeatureCount()
                    if (nF > 0):        
                        self.label.setText("<font color='green'>For <b>" + str(nF) +  "</b> selected elements in <b>" + layer.name() + "</b> set value of field</font>" )
                        self.CBfields.setFocus(True)
                        rm_if_too_old_settings_file(tempfile.gettempdir() + "/HouseNumbering_tmp")
                        if os.path.exists( tempfile.gettempdir() + "/HouseNumbering_tmp"):
                            #in_file = open(tempfile.gettempdir() + '/HouseNumbering_tmp', 'r')
                            in_file = codecs.open(tempfile.gettempdir() + '/HouseNumbering_tmp', encoding='utf8')
                            file_cont = in_file.read()
                            in_file.close()
                            file_cont_splitted = file_cont.split(delimchars)
                            lastlayer = file_cont_splitted[0]
                            lastfield = file_cont_splitted[1]
                            lastvalue = file_cont_splitted[2]
                            lkeepLatestValue = file_cont_splitted[3]
                            lastnsteps = file_cont_splitted[4]
                            lastcBsetLabel = file_cont_splitted[5]
                            lastcBkeepCharFixed = file_cont_splitted[6]
                            if ( self.CBfields.findText(lastfield) > -1 ): # se esiste il nome del campo nel combobox
                                self.CBfields.setCurrentIndex(self.CBfields.findText(lastfield))
                                self.cBkeepLatestValue.setChecked(str2bool(lkeepLatestValue)) # read thevalue from settings
                                if ( self.cBkeepLatestValue.isChecked() ): # if true to keep latest input value
                                    self.QLEnsteps.setText(lastnsteps)
                                    self.QLEvalore.setText(lastvalue)
                                    self.cBsetLabel.setChecked(str2bool(lastcBsetLabel))
                                    self.cBkeepCharFixed.setChecked(str2bool(lastcBkeepCharFixed))
                                    self.QLEvalore.setFocus()
                    if (nF == 0):
                        infoString = unicode("<font color='red'> Please select some elements into current <b>" + layer.name() + "</b> layer</font>")
                        self.label.setText(infoString)
                        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
                        self.QLEvalore.setEnabled(False)
                        self.CBfields.setEnabled(False)
        elif (layer) and layer.type() != QgsMapLayer.VectorLayer:
            infoString = unicode("<font color='red'> Layer <b>" + layer.name() + "</b> is not a vector layer</font>")
            self.iface.messageBar().pushMessage("Message", infoString, level=QgsMessageBar.INFO, duration=3)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            self.QLEvalore.setEnabled(False)
            self.CBfields.setEnabled(False)
        else:
            infoString = unicode("<font color='red'> <b>No layer selected... Select a layer from the layer list...</b></font>")
            self.iface.messageBar().pushMessage("Message", infoString, level=QgsMessageBar.INFO, duration=3)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            self.QLEvalore.setEnabled(False)
            self.CBfields.setEnabled(False)

   # lascio ma non funziona essendo la selezione effettuata prima del richiamo della dialog bisognerebbe far diventare la dialog non modale
   # e catturare l'evento di selezione per poter avere poi un ordine di click degli elementi utile per ordine di numerazione
   def onSelectionChanged( self, added, removed, cleared ): 
      self.iface.messageBar().pushMessage("Message", "added", level=QgsMessageBar.INFO,duration=1)
      self.iface.activeLayer().selectionChanged.connect( onSelectionChanged )

   def run(self):
     delimchars = "#" # delim char to write file to backup dialog user settings
     letter='' # define an empty var then fill it with dialog values or defaults 
     layer = self.iface.mapCanvas().currentLayer()
     if (layer == None):
        infoString = unicode("<font color='red'> <b>No layer selected... Select a layer from the layer list...</b></font>")
        self.iface.messageBar().pushMessage("Message", infoString, level=QgsMessageBar.INFO, duration=3)
        #self.label.setText(infoString)
        return
     layer.startEditing() if not layer.isEditable() else 1 # il valore 1 e' solo per tenere la if su una sola riga coerente con la sintassi
   
     if (len(unicode(self.QLEvalore.displayText()))!=0):
        value = unicode(self.QLEvalore.displayText())
        letter= re.sub('[0-9 ]','',value) # keep the letter of the value
        value= re.sub('[a-zA-Z ]','',value) # keep the number of the value
     else:    
        value = unicode(int('2'))
     #value_when_true if condition else value_when_false   
     nsteps = int(self.QLEnsteps.displayText()) if (len(unicode(self.QLEnsteps.displayText()))!=0) else 2
     nPosField = self.CBfields.currentIndex()
     f_index = self.CBfields.itemData( nPosField )[0]
     f_name = self.CBfields.itemData( nPosField )
     if len(value) == 0:
        infoString = unicode("Warning <b> please input a value... </b>")
        self.iface.messageBar().pushMessage("Message", infoString, level=QgsMessageBar.INFO, duration=3)
        return
     layer = self.iface.mapCanvas().currentLayer()
     if(layer):     
        nF = layer.selectedFeatureCount() # numero delle features selezionate
     else:
       self.iface.messageBar().pushMessage("Error", "Please select a layer", level=QgsMessageBar.ERROR)
       return
     if (nF == 0):
        self.iface.messageBar().pushMessage("Error", "Please select at least one feature from <b> " + layer.name() + "</b> current layer", level=QgsMessageBar.ERROR)                       
     else:
        if ( self.cBsetLabel.isChecked() ):
			layer.setCustomProperty("labeling", "pal")
			layer.setCustomProperty("labeling/enabled", True)
			layer.setCustomProperty("labeling/fieldName", f_name )
        else:
			layer.setCustomProperty("labeling/enabled", False)
			#layer.setCustomProperty("labeling/fontSize","8" )
        oFeaIterator = layer.selectedFeatures() # give the selected features new in api2
        #for index, item in enumerate(oFeaIterator): # since we have not a select order we can use x and y to set udate direction of incremental values
           #print index, item['civ']
           #x = item.geometry().asPoint().x()
           #y = item.geometry().asPoint().y()
           #featid = item.id
           #infoString = unicode(id.row())
           #oFeaIterator = sorted(oFeatures)
           #value=unicode(int(value)-nsteps)
           
        for feature in oFeaIterator: # in oFea2 there is an iterator object (api2)
           if ((letter != "") and not self.cBkeepCharFixed.isChecked()) :
              value = re.sub('[a-zA-Z ]','',value) # keep the number of the value
              layer.changeAttributeValue(feature.id(),nPosField,value+letter,True) 
              letter = checkletter(letter) # to not go over "z" or "Z"
              value=unicode(int(value)) + unichr(ord(letter) + 1)
              letter = re.sub('[0-9 ]','',value) # keep the letter of the value

              
           else:   
                if ((letter != "") and self.cBkeepCharFixed.isChecked()) :
                   value = re.sub('[a-zA-Z ]','',value)
                   layer.changeAttributeValue(feature.id(),nPosField,value+letter,True)
                   value=unicode(str(int(value)+nsteps))+letter

                else:
                   layer.changeAttributeValue(feature.id(),nPosField,value,True) 
                   value=unicode(int(value)+nsteps)

              
        if not os.path.exists( tempfile.gettempdir() + "/HouseNumbering_tmp"):
           out_file = open(tempfile.gettempdir() + '/HouseNumbering_tmp', 'w')
           out_file.write( (layer.name() + delimchars +  self.CBfields.currentText() + delimchars + value +  delimchars + bool2str(self.cBkeepLatestValue.isChecked()) + delimchars + str(nsteps)  ).encode('UTF-8') + delimchars + bool2str(self.cBsetLabel.isChecked()) + delimchars + bool2str(self.cBkeepCharFixed.isChecked()) )
           out_file.close()
           infoString = unicode("<font color='green'> <b>You can save or abort changes at the end of sessions. Press the Save icon to save or disable the edit mode of layer without save changes to abort...</b></font>")
           self.iface.messageBar().pushMessage("Message", infoString, level=QgsMessageBar.INFO)
        else:
           in_file = open(tempfile.gettempdir() + '/HouseNumbering_tmp', 'r')
           file_cont = in_file.read()
           in_file.close()
           file_cont_splitted = file_cont.split(delimchars)
           lastlayer = file_cont_splitted[0]
           lastfield = file_cont_splitted[1]
           lastvalue = file_cont_splitted[2]
           lkeepLatestValue = file_cont_splitted[3]
           lastnsteps = file_cont_splitted[4]
           lastcBsetLabel = file_cont_splitted[5]
           lastcBkeepCharFixed = file_cont_splitted[6]
           #if ( lastlayer != layer.name() ):
           out_file = open(tempfile.gettempdir() +  '/HouseNumbering_tmp', 'w')
           out_file.write( (layer.name() + delimchars +  self.CBfields.currentText() + delimchars + value +  delimchars + bool2str(self.cBkeepLatestValue.isChecked()) + delimchars + str(nsteps)  ).encode('UTF-8') + delimchars + bool2str(self.cBsetLabel.isChecked()) + delimchars + bool2str(self.cBkeepCharFixed.isChecked()) )
           out_file.close()
           self.iface.mapCanvas().refresh()  
           # layer.commitChanges() # questo salva il file immediatamente e non da modo di undo

def checkletter(cLett):
	nOrd=ord(cLett)
	if  (( nOrd == ord('z') ) or (nOrd == ord('Z')) ):
		if (nOrd == ord('z')): # per non andare oltre le z
			return unichr(ord('a')-1)
		if (nOrd == ord('Z')): # per non andare oltre le Z
			return unichr(ord('A')-1)
	return	cLett
   


def bool2str(bVar):
    if bVar:
        return 'True'
    else:
        return 'False'

def str2bool(bVar):
    if ( bVar == 'True'):
        return True
    else:
        return False

def rm_if_too_old_settings_file(myPath_and_File):
    if os.path.exists(myPath_and_File) and os.path.isfile(myPath_and_File) and os.access(myPath_and_File, R_OK):
        now = time.time()
        tmpfileSectime = os.stat(myPath_and_File)[7] #get last modified time,[8] would be last creation time
        if( now - tmpfileSectime > 60 * 60 * 12 ): # if settings file is older than 12 hour
            os.remove( myPath_and_File )



