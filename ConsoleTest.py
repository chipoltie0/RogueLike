import tdl
from Map import *

WIDTH = 200
HEIGHT = 100
WINWIDTH = 200
WINHEIGHT = 200

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)
COLOR_YELLOW = (255,255,0)

console = tdl.init(WIDTH,HEIGHT,title='Test')
next_console = tdl.Console(WIDTH,HEIGHT)

# player positions
# px = WIDTH / 2
# py = HEIGHT / 2

dungeon = Map(HEIGHT,WIDTH)
# dungeon.test(90,50,Tile(char=' ',blocks_movement=True,bg=COLOR_RED))
gen = WorldGenerator(dungeon)
# gen.carve_rect_room(Rect(85,40,40,40))
# gen.carve_rect_room(Rect(65,40,15,15))
# gen.carve_h_tunnel(66,85,44)
parts = gen.create_partitions(0,0,HEIGHT-1,WIDTH-1)
gen.spawn_partition_rooms(parts, fill=False)

# print(random.choice(list(parts.keys())))
# place player in a room
player_part = parts[random.choice(list(parts.keys()))]
px = player_part.cx
py = player_part.cy

player = Piece(dungeon, px, py, '@', COLOR_YELLOW, False)
dungeon.add_piece(player)

npc = Piece(dungeon, px+5,py, '^', COLOR_BLUE, True)
dungeon.add_piece(npc)
"""
def move_object(dx, dy,piece_name = None,):


    if isinstance(object:
        new_x = object.x + dx
        new_y = object.y + dy

        for p in dungeon.piece_dict:
            #check if any object is in the way is blocking
            if (new_x == p.x) or (new_y == p.y):
                if p.blocks_movement:
                    return 'collided with object'

        if dungeon.map[new_x][new_y].blocks_movement:
            return 'collided with tile'

"""


while not tdl.event.is_window_closed():

    for y in range(0,HEIGHT):
        for x in range(0,WIDTH):
            #print('x=',x,'y=',y)
            next_console.draw_char(x,y, dungeon.map[x][y].char,fg = dungeon.map[x][y].fg, bg = dungeon.map[x][y].bg)

    for key, piece in dungeon.piece_dict.items():
        #render each object
        if piece.paint_below:
            bg_paint = dungeon.map[piece.x][piece.y].bg
        #render object
        next_console.draw_char(piece.x, piece.y, piece.char, fg=piece.color,bg=bg_paint)

    console.blit(next_console,width = WIDTH, height = HEIGHT)
    tdl.flush()

    for key, piece in dungeon.piece_dict.items():
        #Clear next_console for new information
        next_console.draw_char(piece.x, piece.y, ' ', fg=piece.color)

    event = tdl.event.wait()
    #print(event)

    #check if keypress, for new location
    if event.type == 'QUIT':
        raise SystemExit()
        print("Quitting")
        #tdl.flush()
        #del console
    elif event.type == 'KEYDOWN':

        if event.key =='KP8' or event.key == 'UP':
            player.move(0,-1)
        elif event.key =='KP2'or event.key == 'DOWN':
            player.move(0, 1)
        elif event.key =='KP4'or event.key == 'LEFT':
            player.move(-1, 0)
        elif event.key =='KP6'or event.key == 'RIGHT':
            player.move(1, 0)
        elif event.key == 'KP7':
            player.move(-1, -1)
        elif event.key == 'KP9':
            player.move(1, -1)
        elif event.key == 'KP1':
            player.move(-1, 1)
        elif event.key == 'KP3':
            player.move(1, 1)




