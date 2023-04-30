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
        self.update_zone("clicked")
        lst = [{"taunter": "lr", "word": "truth"},{"taunter": "loo", "word": "listen"}]
        self.block_change.emit(lst)

qmlRegisterType(MyApp, "MyApp", 1, 0, "MyApp")
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

class Action:
    taunter: str
    word: str
    me: bool

    def __init__(self, taunter, word) -> None:
        self.taunter = taunter
        self.word = word

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
    __index: int

    def __init__(self, block_lst) -> None:
        self.block_list = block_lst

    def NextBlock(self) -> Block:
        block = self.block_list[self.__index]
        self.__index += 1
        if(self.__index == self.block_list.count()):
            self.__index = 1
        return block

    def __PrepareBlocks(self):
        for block in self.block_list:
            block.PrepareBlock
        self.__index = 0

start = Block(zone_holder="SC", 
              action_list = [Action(taunter="LR", word="Truth"),
                              Action(taunter="LOO", word="Listen")])
block1 = Block(zone_holder="LR", 
              action_list = [Action(taunter="AP", word="Truth"),
                              Action(taunter="SC", word="Listen"),
                              Action(taunter="SC", word="Truth")])
block2 = Block(zone_holder="AP", 
              action_list = [Action(taunter="LR", word="Listen"),
                              Action(taunter="LR", word="Truth"),
                              Action(taunter="LOO", word="Truth"),
                              Action(taunter="LOO", word="Listen")])
block3 = Block(zone_holder="LOO", 
              action_list = [Action(taunter="AP", word="Truth"),
                              Action(taunter="SC", word="Listen"),
                              Action(taunter="SC", word="Truth")])
block4 = Block(zone_holder="SC", 
              action_list = [Action(taunter="LR", word="Listen"),
                              Action(taunter="LR", word="Truth"),
                              Action(taunter="LOO", word="Truth"),
                              Action(taunter="LOO", word="Listen")])

block_lst = [start, block1, block2, block3, block4]
block_chain = BlockChain(block_lst = block_lst)

mouse.on_button_event(block_chain.NextBlock, buttons=mouse.X2, types=mouse.DOWN)


sys.exit(app.exec())
