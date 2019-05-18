# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sys
import os
import traceback

from tank.platform import Application
from tank.platform.qt import QtCore, QtGui
import tank

class RenderSetup(Application):
    SetupRenderManager = None

    def init_app(self):
        """
        Called as the application is being initialized
        """
        self.engine.register_command("Render Setup...", self.run_app)

    def destroy_app(self):
        """
        App teardown
        """
        self.log_debug("Destroying rendersetup app")
        
    # def run_app(self):
    #     """
    #     Start doing rendersetup
    #     """
    #     template_work = self.get_template("template_work")
    #     template_shot = self.get_template("template_shot")

    #     doc = c4d.documents.GetActiveDocument()
    #     scenename = os.path.join(doc.GetDocumentPath(), doc.GetDocumentName())

    #     fields = template_work.get_fields(scenename)
    #     fields['layer'] = 'Main'
    #     destination = template_shot.apply_fields(fields)

    #     destination = os.path.join(
    #         os.path.dirname(os.path.dirname(destination)),
    #         '_'.join(os.path.basename(destination).split('_')[:-1])
    #         )

    #     rd = c4d.documents.RenderData()
    #     rd_bc = rd.GetDataInstance()
        
    #     rd_bc[c4d.RDATA_RENDERENGINE] = 1029525
        
    #     octane_vp = c4d.BaseList2D(1029525)
    #     rd.InsertVideoPost(octane_vp)
        
    #     c4d.StopAllThreads()
    #     doc.InsertRenderDataLast(rd)
    #     rd.SetName('shotgun_render')
    #     rd[c4d.RDATA_SAVEIMAGE] = 0
    #     doc.SetActiveRenderData(rd)

    #     OctaneRenderer = rd.GetFirstVideoPost()
    #     OctaneRenderer[c4d.SET_PASSES_ENABLED] = 1
    #     OctaneRenderer[c4d.SET_PASSES_SAVE_MAINPASS] = 1
    #     OctaneRenderer[c4d.SET_PASSES_SAVEPATH] = destination
    #     OctaneRenderer[c4d.SET_PASSES_MULTILAYER] = 0
    #     OctaneRenderer[c4d.SET_PASSES_MAKEFOLDER] = 1
    #     OctaneRenderer[c4d.SET_PASSES_EXR_COMPR] = 3
        
    #     c4d.EventAdd()
        
    #     QtGui.QMessageBox.information(None, "No data in Shotgun!", destination)
    
    def run_app(self):
        """
        Start doing playblast
        """
        try:
            SetupRenderManager = self.get_setuprender_manager()
            SetupRenderManager.showDialog()
        except:
            traceback.print_exc()

    def get_setuprender_manager(self):
        """
        Create a singleton SetupRenderManager object to be used by any app.
        """
        if self.SetupRenderManager is None:
            tk_cinema_setuprender = self.import_module("tk_cinema_setuprender")            
            self.SetupRenderManager = tk_cinema_setuprender.SetupRenderManager(self)
        return self.SetupRenderManager