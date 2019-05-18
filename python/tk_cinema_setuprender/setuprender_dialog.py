
import tank
import os
import sys
import threading

from tank.platform.qt import QtCore, QtGui
from .ui.setuprender_dialog import Ui_setuprenderDialog

ENGINES_OPTIONS = ['Octane', 'Standart']

class SetupRenderDialog(QtGui.QWidget):
    """
    Main application dialog window
    """
    
    def __init__(self, app, handler, parent=None):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self, parent)

        self._app = app
        self._handler = handler
        
        # now load in the UI that was created in the UI designer
        self._ui = Ui_setuprenderDialog() 
        self._ui.setupUi(self)
        self.__initComponents()
        
        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        # self._app = tank.platform.current_bundle()
        
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - A tk API instance, via self._app.tk 
        
        # lastly, set up our very basic UI
        # self._ui.context.setText("Current Shot: %s" % self._app.context)
        self._ui.btnSetupRender.clicked.connect(self.doSetup)

    def __initComponents(self):
        # Setting up playblast resolution percentage. Customizable through
        # optional "engine_options" field in app settings.
        engines = self._app.get_setting("engine_options", ENGINES_OPTIONS)
        for engine in engines:
            self._ui.cmbRenderEngine.addItem( "%s" % engine, userData=engine )

    def doSetup(self):
        overrideSettingsParams = {}

        chbMultiLayer = self._ui.chbMultiLayer.isChecked()
        overrideSettingsParams["multilayer"] = chbMultiLayer

        engine = self._ui.cmbRenderEngine.itemData( self._ui.cmbRenderEngine.currentIndex() )
        overrideSettingsParams["engine"] = engine
        self._handler.doSetup(**overrideSettingsParams)