
class Object:

    def __init__(self,x,y,char,color,blocks_movement = False,name = ''):
        #Create object and instantiate characteristics
        #Creates unique ID for use in the object table
        self.id = self.__hash__()
        #position information
        self.x = x
        self.y = y
        #character to represent on screen and its color
        self.char = char
        self.color = color
        #flag to mark if the object blocks movement through or on top of
        self.blocks_movement = blocks_movement

    def move(self,dx,dy):
        #this will change the character's position for the next console update
        self.x += dx
        self.y += dy

    """def draw(self):
        tdl.Console.draw_char(self,self.x,self.y,self.char,fg=self.color)

    def clear(self):
        tdl.Console.draw_char(self, self.x, self.y, ' ')
    """
