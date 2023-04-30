import sys
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType
from block import block_module, Block
import keyboard

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
            keyboard.add_hotkey('a', self.NextBlock)
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
engine.load('main.qml')
sys.exit(app.exec())
