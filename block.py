class Block:
    action_list: list
    zone_holder: str

    def __init__(self, action_list, zone_holder) -> None:
        self.action_list = action_list
        self.zone_holder = zone_holder

    def PrepareBlock(self, lr, loo, ap, sc):
        for action in self.action_list:
            if(action["taunter"] == "LR" and lr == True):
                action["me"] = True
            else:
                action["me"] = False
            if(action["taunter"] == "AP" and ap == True):
                action["me"] = True
            else:
                action["me"] = False
            if(action["taunter"] == "SC" and sc == True):
                action["me"] = True
            else:
                action["me"] = False
            if(action["taunter"] == "LOO" and loo == True):
                action['me'] = True
            else:
                action["me"] = False

class BlockModule:
    block_list: list
    __index: int = 0
    current_block: Block

    def __init__(self, block_lst) -> None:
        self.block_list = block_lst

    def Init(self, lr, loo, ap, sc):
        self.__index = 0
        self.__PrepareBlocks(lr, loo, ap, sc)

    def NextBlock(self):
        self.current_block = self.block_list[self.__index]
        self.__index += 1
        if(self.__index == self.block_list.__len__):
            self.__index = 1

    def __PrepareBlocks(self, lr, loo, ap, sc):
        for block in self.block_list:
            block.PrepareBlock(lr, loo, ap, sc)

__start = Block(zone_holder="SC", 
              action_list = [{"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])
__block1 = Block(zone_holder="LR", 
              action_list = [{"taunter":"AP", "word":"Truth"},
                              {"taunter":"SC", "word":"Listen"},
                              {"taunter":"SC", "word":"Truth"}])
__block2 = Block(zone_holder="AP", 
              action_list = [{"taunter":"LR", "word":"Listen"},
                              {"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])
__block3 = Block(zone_holder="LOO", 
              action_list = [{"taunter":"AP", "word":"Truth"},
                              {"taunter":"SC", "word":"Listen"},
                              {"taunter":"SC", "word":"Truth"}])
__block4 = Block(zone_holder="SC", 
              action_list = [{"taunter":"LR", "word":"Listen"},
                              {"taunter":"LR", "word":"Truth"},
                              {"taunter":"LOO", "word":"Truth"},
                              {"taunter":"LOO", "word":"Listen"}])

block_module = BlockModule(block_lst = [__start, __block1, __block2, __block3, __block4])