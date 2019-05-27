# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation.ui'
#
# Created: Wed Feb 06 01:24:05 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SimulationWindow(object):
    def setupUi(self, SimulationWindow):
        SimulationWindow.setObjectName("SimulationWindow")
        SimulationWindow.resize(1106, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(SimulationWindow.sizePolicy().hasHeightForWidth())
        SimulationWindow.setSizePolicy(sizePolicy)
        SimulationWindow.setMinimumSize(QtCore.QSize(1096, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pymote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimulationWindow.setWindowIcon(icon)
        SimulationWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(SimulationWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.controlGroupBox = QtWidgets.QGroupBox(self.leftWidget)
        self.controlGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.controlGroupBox.setObjectName("controlGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.controlGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.controlGroupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.stepSize = QtWidgets.QSpinBox(self.widget)
        self.stepSize.setAccelerated(True)
        self.stepSize.setMaximum(999)
        self.stepSize.setProperty("value", 1)
        self.stepSize.setObjectName("stepSize")
        self.horizontalLayout_2.addWidget(self.stepSize)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.controlGroupBox)
        self.viewGroupBox = QtWidgets.QGroupBox(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewGroupBox.sizePolicy().hasHeightForWidth())
        self.viewGroupBox.setSizePolicy(sizePolicy)
        self.viewGroupBox.setObjectName("viewGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.viewGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.networkViewGroup = QtWidgets.QGroupBox(self.viewGroupBox)
        self.networkViewGroup.setObjectName("networkViewGroup")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.networkViewGroup)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.showNodes = QtWidgets.QCheckBox(self.networkViewGroup)
        self.showNodes.setChecked(True)
        self.showNodes.setObjectName("showNodes")
        self.verticalLayout_6.addWidget(self.showNodes)
        self.showEdges = QtWidgets.QCheckBox(self.networkViewGroup)
        self.showEdges.setChecked(True)
        self.showEdges.setObjectName("showEdges")
        self.verticalLayout_6.addWidget(self.showEdges)
        self.showMessages = QtWidgets.QCheckBox(self.networkViewGroup)
        self.showMessages.setChecked(True)
        self.showMessages.setObjectName("showMessages")
        self.verticalLayout_6.addWidget(self.showMessages)
        self.showLabels = QtWidgets.QCheckBox(self.networkViewGroup)
        self.showLabels.setChecked(True)
        self.showLabels.setObjectName("showLabels")
        self.verticalLayout_6.addWidget(self.showLabels)
        self.redrawNetworkButton = QtWidgets.QPushButton(self.networkViewGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redrawNetworkButton.sizePolicy().hasHeightForWidth())
        self.redrawNetworkButton.setSizePolicy(sizePolicy)
        self.redrawNetworkButton.setObjectName("redrawNetworkButton")
        self.verticalLayout_6.addWidget(self.redrawNetworkButton)
        self.verticalLayout_2.addWidget(self.networkViewGroup)
        self.treeGroupBox = QtWidgets.QGroupBox(self.viewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeGroupBox.sizePolicy().hasHeightForWidth())
        self.treeGroupBox.setSizePolicy(sizePolicy)
        self.treeGroupBox.setMinimumSize(QtCore.QSize(132, 60))
        self.treeGroupBox.setFlat(False)
        self.treeGroupBox.setCheckable(True)
        self.treeGroupBox.setChecked(True)
        self.treeGroupBox.setObjectName("treeGroupBox")
        self.treeKey = QtWidgets.QLineEdit(self.treeGroupBox)
        self.treeKey.setGeometry(QtCore.QRect(42, 20, 71, 20))
        self.treeKey.setFrame(True)
        self.treeKey.setObjectName("treeKey")
        self.label = QtWidgets.QLabel(self.treeGroupBox)
        self.label.setGeometry(QtCore.QRect(10, 22, 31, 16))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.treeGroupBox)
        self.propagationError = QtWidgets.QGroupBox(self.viewGroupBox)
        self.propagationError.setMinimumSize(QtCore.QSize(132, 70))
        self.propagationError.setCheckable(True)
        self.propagationError.setChecked(False)
        self.propagationError.setObjectName("propagationError")
        self.locKey = QtWidgets.QLineEdit(self.propagationError)
        self.locKey.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.locKey.setObjectName("locKey")
        self.label2 = QtWidgets.QLabel(self.propagationError)
        self.label2.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.propagationError)
        self.verticalLayout_3.addWidget(self.viewGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.leftWidget)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.networkDisplayWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkDisplayWidget.sizePolicy().hasHeightForWidth())
        self.networkDisplayWidget.setSizePolicy(sizePolicy)
        self.networkDisplayWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.networkDisplayWidget.setObjectName("networkDisplayWidget")
        self.horizontalLayout.addWidget(self.networkDisplayWidget)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        SimulationWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(SimulationWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setObjectName("toolBar")
        SimulationWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(SimulationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimulation = QtWidgets.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        SimulationWindow.setMenuBar(self.menubar)
        self.dockWidget = QtWidgets.QDockWidget(SimulationWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(87, 109))
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.networkInspector = QtWidgets.QTreeView(self.dockWidgetContents)
        self.networkInspector.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.networkInspector.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.networkInspector.setProperty("showDropIndicator", False)
        self.networkInspector.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.networkInspector.setAnimated(True)
        self.networkInspector.setWordWrap(True)
        self.networkInspector.setHeaderHidden(True)
        self.networkInspector.setObjectName("networkInspector")
        self.horizontalLayout_3.addWidget(self.networkInspector)
        self.dockWidget.setWidget(self.dockWidgetContents)
        SimulationWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(SimulationWindow)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(105, 377))
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nodeInspector = QtWidgets.QTreeView(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeInspector.sizePolicy().hasHeightForWidth())
        self.nodeInspector.setSizePolicy(sizePolicy)
        self.nodeInspector.setMinimumSize(QtCore.QSize(87, 337))
        self.nodeInspector.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.nodeInspector.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nodeInspector.setProperty("showDropIndicator", False)
        self.nodeInspector.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.nodeInspector.setAnimated(True)
        self.nodeInspector.setWordWrap(True)
        self.nodeInspector.setHeaderHidden(True)
        self.nodeInspector.setObjectName("nodeInspector")
        self.horizontalLayout_4.addWidget(self.nodeInspector)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        SimulationWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(SimulationWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(87, 109))
        self.dockWidget_3.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logListWidget = QtWidgets.QListWidget(self.dockWidgetContents_3)
        self.logListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.logListWidget.setLineWidth(0)
        self.logListWidget.setObjectName("logListWidget")
        self.horizontalLayout_5.addWidget(self.logListWidget)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        SimulationWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
        self.actionRun = QtWidgets.QAction(SimulationWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/player_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionRun.setObjectName("actionRun")
        self.actionStep = QtWidgets.QAction(SimulationWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/player_fwd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStep.setIcon(icon2)
        self.actionStep.setObjectName("actionStep")
        self.actionReset = QtWidgets.QAction(SimulationWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/player_start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon3)
        self.actionReset.setObjectName("actionReset")
        self.actionCopyInspectorData = QtWidgets.QAction(SimulationWindow)
        self.actionCopyInspectorData.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionCopyInspectorData.setObjectName("actionCopyInspectorData")
        self.actionSaveNetwork = QtWidgets.QAction(SimulationWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveNetwork.setIcon(icon4)
        self.actionSaveNetwork.setObjectName("actionSaveNetwork")
        self.actionOpenNetwork = QtWidgets.QAction(SimulationWindow)
        self.actionOpenNetwork.setCheckable(False)
        self.actionOpenNetwork.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenNetwork.setIcon(icon5)
        self.actionOpenNetwork.setObjectName("actionOpenNetwork")
        self.actionShowLocalizedSubclusters = QtWidgets.QAction(SimulationWindow)
        self.actionShowLocalizedSubclusters.setObjectName("actionShowLocalizedSubclusters")
        self.toolBar.addAction(self.actionOpenNetwork)
        self.toolBar.addAction(self.actionSaveNetwork)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionStep)
        self.toolBar.addAction(self.actionReset)
        self.menuFile.addAction(self.actionOpenNetwork)
        self.menuFile.addAction(self.actionSaveNetwork)
        self.menuSimulation.addAction(self.actionRun)
        self.menuSimulation.addAction(self.actionStep)
        self.menuSimulation.addAction(self.actionReset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())

        self.retranslateUi(SimulationWindow)
        QtCore.QMetaObject.connectSlotsByName(SimulationWindow)
        SimulationWindow.setTabOrder(self.stepSize, self.treeKey)

    def retranslateUi(self, SimulationWindow):
        SimulationWindow.setWindowTitle(QtWidgets.QApplication.translate("SimulationWindow", "Pymote Simulation", None))
        self.controlGroupBox.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "Control", None))
        self.label_2.setText(QtWidgets.QApplication.translate("SimulationWindow", "Step size:", None))
        self.stepSize.setSpecialValueText(QtWidgets.QApplication.translate("SimulationWindow", "All", None))
        self.viewGroupBox.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "View", None))
        self.networkViewGroup.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "Network", None))
        self.showNodes.setText(QtWidgets.QApplication.translate("SimulationWindow", "Nodes", None))
        self.showEdges.setText(QtWidgets.QApplication.translate("SimulationWindow", "Edges", None))
        self.showMessages.setText(QtWidgets.QApplication.translate("SimulationWindow", "Messages", None))
        self.showLabels.setText(QtWidgets.QApplication.translate("SimulationWindow", "Labels", None))
        self.redrawNetworkButton.setText(QtWidgets.QApplication.translate("SimulationWindow", "Redraw", None))
        self.treeGroupBox.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Enter memory key that has parent and child items.", None))
        self.treeGroupBox.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "Tree", None))
        self.treeKey.setText(QtWidgets.QApplication.translate("SimulationWindow", "treeNeighbors", None))
        self.label.setText(QtWidgets.QApplication.translate("SimulationWindow", "Key:", None))
        self.propagationError.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Enter memory key that has stitch location data.", None))
        self.propagationError.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "Propagation error", None))
        self.locKey.setText(QtWidgets.QApplication.translate("SimulationWindow", "convergecastLoc", None))
        self.label2.setText(QtWidgets.QApplication.translate("SimulationWindow", "LocKey:", None))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("SimulationWindow", "toolBar", None))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "File", None))
        self.menuSimulation.setTitle(QtWidgets.QApplication.translate("SimulationWindow", "Simulation", None))
        self.dockWidget.setWindowTitle(QtWidgets.QApplication.translate("SimulationWindow", "Network inspector", None))
        self.dockWidget_2.setWindowTitle(QtWidgets.QApplication.translate("SimulationWindow", "Node inspector", None))
        self.dockWidget_3.setWindowTitle(QtWidgets.QApplication.translate("SimulationWindow", "Log", None))
        self.actionRun.setText(QtWidgets.QApplication.translate("SimulationWindow", "Run", None))
        self.actionRun.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Run simulation from beginning", None))
        self.actionRun.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+R", None))
        self.actionStep.setText(QtWidgets.QApplication.translate("SimulationWindow", "Step", None))
        self.actionStep.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Run next step", None))
        self.actionStep.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+Space", None))
        self.actionReset.setText(QtWidgets.QApplication.translate("SimulationWindow", "Reset", None))
        self.actionReset.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Reset simulation", None))
        self.actionReset.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+W", None))
        self.actionCopyInspectorData.setText(QtWidgets.QApplication.translate("SimulationWindow", "Copy", None))
        self.actionCopyInspectorData.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+C", None))
        self.actionSaveNetwork.setText(QtWidgets.QApplication.translate("SimulationWindow", "Save", None))
        self.actionSaveNetwork.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Save network in npickle format", None))
        self.actionSaveNetwork.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+S", None))
        self.actionOpenNetwork.setText(QtWidgets.QApplication.translate("SimulationWindow", "Open", None))
        self.actionOpenNetwork.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Open network from npickle", None))
        self.actionOpenNetwork.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+O", None))
        self.actionShowLocalizedSubclusters.setText(QtWidgets.QApplication.translate("SimulationWindow", "Show localized subclusters", None))
        self.actionShowLocalizedSubclusters.setToolTip(QtWidgets.QApplication.translate("SimulationWindow", "Show localized subclusters based on memory field that has positions and subclusters items.", None))
        self.actionShowLocalizedSubclusters.setShortcut(QtWidgets.QApplication.translate("SimulationWindow", "Ctrl+L", None))

from . import icons_rc
