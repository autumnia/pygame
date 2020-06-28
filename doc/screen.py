
def create_screen( game, title, screen_size ):
    #print("title: " + title)
    #print("screen size: " + str(screen_size) )

    game.display.set_caption( title )  # 게임 타이틀
    screen = game.display.set_mode( screen_size )
    return screen

def create_backgound( game, image ):
    #print( "이미지경로: " + image )
    background = game.image.load( image )
    return background


