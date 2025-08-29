import pyxel

from src.player import Player

class App:
    screenSize = (128,128)
    def __init__(self):
        
        self.player = Player(self)
        
        pyxel.init(self.screenSize[0], self.screenSize[1], title="Overflow", quit_key=pyxel.KEY_ESCAPE, fps=60)
        pyxel.load("res.pyxres")
        pyxel.run(self.update, self.draw)
        
    def center(self,ox=0,oy=0):
        return [self.screenSize[0] / 2 + ox, self.screenSize[1] / 2 + oy]

    def update(self):
        self.player.update()
        pass

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        pass
        

App()