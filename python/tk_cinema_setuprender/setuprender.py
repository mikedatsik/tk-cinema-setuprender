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
        # template_work = self._app.get_template("template_work")
        # template_shot = self._app.get_template("template_shot")

        # self._app.log_info(" %s" % overridePlayblastParams)

        doc = c4d.documents.GetActiveDocument()
        # scenename = os.path.join(doc.GetDocumentPath(), doc.GetDocumentName())

        # fields = template_work.get_fields(scenename)
        # fields['layer'] = 'Main'
        # destination = template_shot.apply_fields(fields)

        if overridePlayblastParams.get('multilayer'):
            destination = "../images/$prj/$take/Main/$take_$prj_Main"
        else:
            destination = "../images/$prj/$take/$take_$prj"
            # destination = os.path.join(
            #     os.path.dirname(os.path.dirname(destination)),
            #     '_'.join(os.path.basename(destination).split('_')[:-1])
            #     )
        if 'Octane' in overridePlayblastParams.get('engine'):
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
            OctaneRenderer[c4d.SET_PASSES_MULTILAYER] = 0
            OctaneRenderer[c4d.SET_PASSES_MAKEFOLDER] = 1
            OctaneRenderer[c4d.SET_PASSES_EXR_COMPR] = 3
            
            c4d.EventAdd()

        # self._app.log_info("Render Setup for %s succesful" % scenename)
