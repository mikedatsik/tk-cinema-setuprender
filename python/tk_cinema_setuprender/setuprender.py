import traceback

from contextlib import contextmanager

import c4d
import os
import tank
from tank.platform.qt import QtCore, QtGui
from .setuprender_dialog import SetupRenderDialog


class SetupRenderManager(object):
    __uploadToShotgun = True

    """
    Main Setup Render functionality
    """
    def __init__(self, app, context=None):
        """
        Construction
        """
        self._app = app
        self._context = context if context else self._app.context

    def showDialog(self):
        try:
            self._app.engine.show_dialog("Setup Render %s" % self._app.version,
                                         self._app, SetupRenderDialog, self._app, self)
        except:
            traceback.print_exc()
    
    def doSetup(self, **overridePlayblastParams):
        doc = c4d.documents.GetActiveDocument()

        if overridePlayblastParams.get('multilayer'):
            destination = "../images/$prj/$take/Main/$take_$prj_Main_"
            multilayer = 1
        else:
            destination = "../images/$prj/$take/$take_$prj"
            multilayer = 0

        rdata = doc.GetFirstRenderData()
        listOfRs = []
        while rdata:
            rdata = rdata.GetNext()
            if rdata:
                listOfRs.append(rdata.GetName())

        if 'Octane' in overridePlayblastParams.get('engine'):
            if 'shotgun_render' not in listOfRs:
                rd = c4d.documents.RenderData()
                rd_bc = rd.GetDataInstance()
                
                rd_bc[c4d.RDATA_RENDERENGINE] = 1029525
                
                octane_vp = c4d.BaseList2D(1029525)
                
                rd.InsertVideoPost(octane_vp)
                
                c4d.StopAllThreads()
                doc.InsertRenderDataLast(rd)
                rd.SetName('shotgun_render')
                rd[c4d.RDATA_SAVEIMAGE] = 0
                doc.SetActiveRenderData(rd)

                OctaneRenderer = rd.GetFirstVideoPost()
                OctaneRenderer[c4d.SET_PASSES_ENABLED] = 1
                OctaneRenderer[c4d.SET_PASSES_SAVE_MAINPASS] = 1
                OctaneRenderer[c4d.SET_PASSES_SAVEPATH] = destination
                OctaneRenderer[c4d.SET_PASSES_MULTILAYER] = multilayer
                OctaneRenderer[c4d.SET_PASSES_MAKEFOLDER] = 1
                OctaneRenderer[c4d.SET_PASSES_EXR_COMPR] = 3
                
                c4d.EventAdd()
        
        # self._app.log_info("Render Setup for %s succesful" % scenename)
