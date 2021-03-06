# -*- coding: utf-8 -*-

""" THIS COMMENT MUST NOT REMAIN INTACT

GNU GENERAL PUBLIC LICENSE

Copyright (c) 2015 geometalab HSR

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import utils

from vtr_dialog import Dialog
from vtr_dialog import Model


class Plugin:
    _dialog = None
    _model = None
    vtr_action = None

    def __init__(self, iface):
        self._iface = iface
        self.settings = QSettings("Vector Tile Reader","vectortilereader")

    def initGui(self):
        vtr_layer_icon = QIcon(':/plugins/vectortilereader/icon.png')
        self.vtr_action = QAction(vtr_layer_icon, "Add Vector Tiles Layer", self._iface.mainWindow())
        self._iface.addToolBarIcon(self.vtr_action)
        self._iface.addPluginToMenu("&Add Vector Tiles Layer", self.vtr_action)
        self._iface.addPluginToVectorMenu("&Add Vector Tiles Layer", self.vtr_action)
        self.vtr_action.triggered.connect(
            lambda: Dialog(self._iface, self.settings).create_dialog()
        )

    def unload(self):
        # Remove the plugin menu item and icon
        self._iface.removeToolBarIcon(self.vtr_action)
        self._iface.removePluginMenu("&Add Vector Tiles Layer", self.vtr_action)
        self._iface.removePluginVectorMenu("&Add Vector Tiles Layer", self.vtr_action)
