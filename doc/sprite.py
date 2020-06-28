import random

class Sprite(object):
    def __init__(self, screen_size, speed):
        self._SCREEN_SIZE = screen_size
        self._SPRITE_SPEED = speed

    def create_sprite(self, game, image):
        self._sprite = game.image.load(image)
        self._width = self._sprite.get_rect().size[0]
        self._height = self._sprite.get_rect().size[1]

    def move_X(self, speed):
        self._xpos = int( self._xpos + speed )
        #print( self._xpos )
        if ( self._xpos < 0 ):
            self._xpos = 0
        elif ( self._xpos > self._SCREEN_SIZE[0] - self._width ):
            self._xpos = self._SCREEN_SIZE[0] - self._width
        self._sprite_size = (self._xpos, self._ypos)

    def move_Y(self, speed):
        self._ypos = int( self._ypos + speed )
        if ( self._ypos > int( self._SCREEN_SIZE[1] - self._height) ):
            self._ypos = 0
        self._sprite_size = (random.randint(0, self._SCREEN_SIZE[0] - self.get_width ), self._ypos)

    def set_pos(self, xpos, ypos):
        self._xpos = int( xpos )
        self._ypos = int( ypos )
        self._sprite_size = (self._xpos, self._ypos )

    def get_spriteSize(self):
        return self._sprite_size

    def get_xpos(self):
        #print( self._xpos )
        return self._xpos

    def get_ypos(self):
        #print( self._xpos )
        return self._ypos

    @property
    def get_speed(self):
        return self._SPRITE_SPEED

    @property
    def get_sprite(self):
        return self._sprite

    @property
    def get_width(self):
        return self._width

    @property
    def get_height(self):
        return self._height

    @property
    def get_rect(self):
        #print( "rect: " + self._sprite.get_rect() )
        return self._sprite.get_rect()