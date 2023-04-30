import sys
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType
import mouse

class MyApp(QObject):
    zone_change = pyqtSignal(str)
    block_change = pyqtSignal(list)

    @pyqtSlot(str)
    def update_zone(self, zone_taker):
        self.zone_change.emit(zone_taker)

    @pyqtSlot()
    def on_button_clicked(self):
        block_chain.NextBlock()
        self.update_zone(block_chain.current_block.zone_holder)
        self.block_change.emit(block_chain.current_block.action_list)

qmlRegisterType(MyApp, "MyApp", 1, 0, "MyApp")
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

class Block:
    action_list: list
    zone_holder: str

    def __init__(self, action_list, zone_holder) -> None:
        self.action_list = action_list
        self.zone_holder = zone_holder

    def PrepareBlock(self, lr, loo, ap, sc):
        for action in self.action_list:
            if(action.taunter == "lr" and lr == True):
                action.me = True
            if(action.taunter == "ap" and ap == True):
                action.me = True
            if(action.taunter == "sc" and sc == True):
                action.me = True
            if(action.taunter == "loo" and loo == True):
                action.me = True

class BlockChain:
    block_list: list
    __index: int = 0
    current_block: Block

    def __init__(self, block_lst) -> None:
        self.block_list = block_lst

    def NextBlock(self):
        self.current_block = self.block_list[self.__index]
        self.__index += 1
        if(self.__index == self.block_list.__len__):
            self.__index = 1

    def __PrepareBlocks(self):
        for block in self.block_list:
            block.PrepareBlock
        self.__index = 0

start = Block(zone_holder="SC", 
              action_list = [{"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])
block1 = Block(zone_holder="LR", 
              action_list = [{"taunter":"AP", "word":"Truth"},
                              {"taunter":"SC", "word":"Listen"},
                              {"taunter":"SC", "word":"Truth"}])
block2 = Block(zone_holder="AP", 
              action_list = [{"taunter":"LR", "word":"Listen"},
                              {"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])
block3 = Block(zone_holder="LOO", 
              action_list = [{"taunter":"AP", "word":"Truth"},
                              {"taunter":"SC", "word":"Listen"},
                              {"taunter":"SC", "word":"Truth"}])
block4 = Block(zone_holder="SC", 
              action_list = [{"taunter":"LR", "word":"Listen"},
                              {"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])

block_lst = [start, block1, block2, block3, block4]
block_chain = BlockChain(block_lst = block_lst)

myApp = engine.rootObjects()[0].findChild(QObject, "myApp")

mouse.on_button(block_chain.NextBlock, buttons=mouse.X2, types=mouse.DOWN)

sys.exit(app.exec())
