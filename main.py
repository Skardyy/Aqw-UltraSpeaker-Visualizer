import sys
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType

class MyApp(QObject):
    zone_change = pyqtSignal(str)

    @pyqtSlot(str)
    def update_title(self, zone_taker):
        self.zone_change.emit(zone_taker)

    @pyqtSlot()
    def on_button_clicked(self):
        self.update_title("clicked")

qmlRegisterType(MyApp, "MyApp", 1, 0, "MyApp")

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
sys.exit(app.exec())
