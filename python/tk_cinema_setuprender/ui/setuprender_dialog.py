# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setuprender_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_setuprenderDialog(object):
    def setupUi(self, setuprenderDialog):
        setuprenderDialog.setObjectName("setuprenderDialog")
        setuprenderDialog.resize(521, 67)
        self.gridLayout = QtGui.QGridLayout(setuprenderDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetupRender = QtGui.QPushButton(setuprenderDialog)
        self.btnSetupRender.setMinimumSize(QtCore.QSize(450, 0))
        self.btnSetupRender.setObjectName("btnSetupRender")
        self.gridLayout.addWidget(self.btnSetupRender, 2, 0, 1, 3)
        self.chbMultiLayer = QtGui.QCheckBox(setuprenderDialog)
        self.chbMultiLayer.setChecked(False)
        self.chbMultiLayer.setObjectName("chbMultiLayer")
        self.gridLayout.addWidget(self.chbMultiLayer, 0, 2, 1, 1)
        self.cmbRenderEngine = QtGui.QComboBox(setuprenderDialog)
        self.cmbRenderEngine.setEditable(False)
        self.cmbRenderEngine.setObjectName("cmbRenderEngine")
        self.gridLayout.addWidget(self.cmbRenderEngine, 0, 0, 1, 1)
        self.label = QtGui.QLabel(setuprenderDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(setuprenderDialog)
        QtCore.QMetaObject.connectSlotsByName(setuprenderDialog)

    def retranslateUi(self, setuprenderDialog):
        setuprenderDialog.setWindowTitle(QtGui.QApplication.translate("setuprenderDialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSetupRender.setText(QtGui.QApplication.translate("setuprenderDialog", "Setup Render", None, QtGui.QApplication.UnicodeUTF8))
        self.chbMultiLayer.setText(QtGui.QApplication.translate("setuprenderDialog", "Single EXR Pipeline", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("setuprenderDialog", "Render Engine", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
