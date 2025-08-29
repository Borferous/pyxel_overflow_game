import pyxel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App 

class Player:
    def __init__(self, game: "App"):
        self.game = game
        self.position = game.center()
        self.sprite = (0, 0)
        self.size = (8, 8)
        pass

    def update(self):
        pass

    def draw(self):
        x, y = self.position
        w, h = self.size
        u, v = self.sprite
        pyxel.blt(x-w/2,y-h/2,0,u,v,w,h)
        pass
    