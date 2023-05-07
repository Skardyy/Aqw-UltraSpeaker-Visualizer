import sys
import os
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType
from block import block_module
import mouse

class MyApp(QObject):
    zone_change = pyqtSignal(str)
    block_change = pyqtSignal(list)
    started = False

    def update_zone(self, zone_taker):
        self.zone_change.emit(zone_taker)

    def block_change_ui(self, lst):
        self.block_change.emit(lst)

    @pyqtSlot(bool, bool, bool, bool)
    def apply(self, lr, loo, ap, sc):
        block_module.Init(lr, loo, ap, sc)
        if(self.started == False):
            mouse.on_button(buttons = mouse.X2, types= mouse.UP, callback=self.NextBlock)
            self.started = True
        self.NextBlock()
        
    def NextBlock(self):
        block_module.NextBlock()
        self.update_zone(block_module.current_block.zone_holder)
        self.block_change_ui(block_module.current_block.action_list)
        
qmlRegisterType(MyApp, "MyApp", 1, 0, "MyApp")
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
engine.load(QUrl.fromLocalFile(os.path.abspath(qml_file)))
sys.exit(app.exec())
