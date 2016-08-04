import random
COLOR_GRAY = (160,160,160)

class Tile:

    def __init__(self,char = ' ',blocks_movement = False,blocks_sight = False, fg = Ellipsis, bg = Ellipsis):
        #instantiate variables defining if a tile blocks movemnt or sight
        #defaults are that tiles are blocking sight and movement
        self.char = char
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight
        self.fg = fg
        self.bg = bg
        # does nothing


class Map:
    """
    This class will handle the map that will be rendered, it will also handle interactions with the world
    """

    def __init__(self, height, width):
        """
        This will create the Map object and populate the tiles inside and the piece dictionary

        :param height: this is the height of the map, y axis
        :param width:  this is the width of the map, x axis
        """

        #This creates a 2d array of Tiles, this can also add objects to the map
        self.map = [[Tile(char = ' ',blocks_movement=True,blocks_sight=True) for y in range(0,height)] for x in range(0,width)]

        #initialize the piece dictionary to hold all pieces
        self.piece_dict = {}
        
    def add_piece(self,piece = None):
        """
        This will add a piece to the map and store it in the piece dictionary

        :type piece: Piece
        """
        if isinstance(piece,Piece):
            #add dictionary item piece object with a key based on its ID

            self.piece_dict[piece.id] = piece
        

    def test(self,x,y,t = Tile(char = ' ', blocks_movement=True)):
        """

        :param x: x position of the tile
        :param y: y position of the tile
        :param t: tile object that will be put in x,y position
        :return: returns nothing, edits self.map
        """
        self.map[x][y] = t

    def movement_blocked(self,check_x, check_y):
        """

        :param x: x position to query
        :param y: y position to query
        :return: 'tile' if tile blocked, 'piece' if piece blocking
        """

        #check tiles first, since most likely faster
        if self.map[check_x][check_y].blocks_movement:
            blocking = 'tile'
            return blocking

        #if no tile blocks movemnt, iterate over pieces and see if a piece blocks movement
        for key, piece in self.piece_dict.items():
            #check if the piece blocks movement and in the same position
            if (piece.blocks_movement) and (piece.x == check_x) and (piece.y == check_y):
                blocking = 'piece'
                return blocking

    def pieces_at(self, check_x, check_y):

        pieces_here = {}
        for key, piece in self.piece_dict.items():
            if (piece.x == check_x) and (piece.y == check_y):
                pieces_here[key] = piece
        return pieces_here


class Piece:
    
    def __init__(self,map,x,y,char,color,blocks_movement = False,name = '',paint_below = True):
        #Create object and instantiate characteristics
        #Creates unique ID for use in the object table
        self.id = id(self)

        #store map reference to self
        self.map = map
        #position information
        self.x = int(x)
        self.y = int(y)
        #character to represent on screen and its color
        self.char = char
        self.color = color
        #flag to mark if the object blocks movement through or on top of
        self.blocks_movement = blocks_movement
        #allow renderer to change background to tile background
        self.paint_below = paint_below

    def move(self,dx,dy):
        """
        This will check for collision then try to move
        :param dx: distance to move in x + is right
        :param dy: distance to move in y + is down
        :return:
        """
        blocked = None
        #check with map to see if collision will occur
        blocked = self.map.movement_blocked(self.x + dx, self.y + dy)
        if blocked:
            #if blocked, move to other functions
            #ask map what is there
            pieces_in_way = {}
            if blocked == 'tile':
                print('blocked by tile', self.map.map[self.x + dx][self.y + dy])
                return

            pieces_in_way = self.map.pieces_at(self.x + dx,self.y + dy)
            print("Piece movemnt blocked by: ",pieces_in_way)

            #TODO add code to handle attacking, add to new function
            #do not move, just leave function

            return
        else:
            #this will change the character's position for the next console update
            self.x += dx
            self.y += dy


class Rect:

    def __init__(self, start_x, start_y, width, height):
        """

        :param start_x: x position, from left to right
        :param start_y: y position from top to bottom
        :param width: width of rectangle
        :param height: height of rectangle
        """
        # start coordinates
        self.x1 = start_x
        self.y1 = start_y
        # end coordinates
        self.x2 = start_x + width
        self.y2 = start_y + height


class Room(Rect):

    def __init__(self, start_x, start_y, width, height):
        # load rectangle object with positions start and end
        super().__init__(start_x, start_y, width, height)

        #give unique id to room
        self.id = id(self)

        # store height and width
        self.height = height
        self.width = width

        # coordinate of the center of the partition
        self.cx = round((self.x1 + self.x2) / 2)
        self.cy = round((self.y1 + self.y2) / 2)

        # volume of partition
        self.volume = self.height * self.width

        #get edges of the room
        self.edges = self.get_edges()

    def _get_edges(self):
        """
        This will retrieve all the edge points of the room (besides corners, no diagonal exits to room) and make a list
        :return: list of (x, y) tuples representing locations of edge tiles
        """
        edge_list = []

        for y in (self.y1, self.y2):
            for x in range(self.x1 + 1 , self.x2 ):
                edge_list.append((x,y))

        for x in (self.x1, self.x2):
            for y in range(self.y1 + 1, self.y2):
                edge_list.append((x, y))

        return edge_list


class OrganicGenerator:

    def __init__(self, map):
        # store map for calculations
        self.map = map
        self.height = map.height
        self.width = map.width
        #
        self.collision_map = [[0 for y in range(0,self.height)] for x in range(0,self.width)]

    def _create_start_room(self):
        start_x = random.uniform(0,self.width)
        start_y = random.uniform(0,self.height)
        room_width = random.uniform

    def grow_room(self,seed_room):

        # get location to start growing room
        start_point = random.uniform(0,len(seed_room.edges))
        #Test comment horay!
        print("horay!!")
        print("more horay!")

class Partition:

    def __init__(self,start_x,start_y, height, width):
        """
        This will create a partition and set up variables
        :param start_x: upper left x coord + is right
        :param start_y: upper left y coord + is down
        :param length: length along x axis
        :param width:  length along y axis
        """
        # unique identifier
        self.id = id(self)
        # start point coordinates
        self.x1 = start_x
        self.y1 = start_y
        # height and width
        self.height = height
        self.width = width
        # final point coordinates
        self.x2 = start_x + width
        self.y2 = start_y + height
        # coordinate of the center of the partition
        self.cx = round((self.x1 + self.x2) / 2)
        self.cy = round((self.y1 + self.y2) / 2)
        # volume of partition
        self.volume = self.height * self.width
        # spawn room flag
        self.spawn_room = True

    def split(self):
        """
        This will check the size of the partition, and split it if it isn't too small
        :return: dictionary with the id of all contained Partition objects, or itself if itself is small enough
        """

        # first get a random number from Triangular distribution to compare to current volume
        # TODO possible make generator changeable, argument with generator type object
        vol_check_val = round(random.triangular(17,400,200))

        # check if partition is below check size
        if vol_check_val > self.volume:
            # return itself, since it is the last branch of the partition
            return {self.id:self}

        # get a number between 1 and the sum of the height and width, this leads to higher probabilities of splitting
        # along the longest axis
        # 4 is added here so that
        axis_split = random.randrange(1 + 4, self.height + self.width - 4)

        # check if the picked number maps to the height or width to direct the cut
        # TODO check if this might need to check if axis lenght is greater than min value
        if axis_split <= self.height:
            axis = 'y'
            start = self.y1
            end = self.y2
            length = self.height
            center = self.cy
        else:
            axis = 'x'
            start = self.x1
            end = self.x2
            length = self.width
            center = self.cx

        # pick distance along axis to split, using center as the mean and (length - 8)/ 6 for sigma
        # this means that 3 sigma away is very close to the 4 minimum partition size
        # 1 is added here since center will tend to be further to the left, due to int() in the center calculation
        cut_location = round(random.normalvariate(center,(length - 8) / 6))

        # this section scales the edge so the cut is at least 4 away from another edge
        if cut_location < start + 4:
            cut_location = start + 4
        elif cut_location > end - 4:
            cut_location = end - 4

        # now create two internal partitions
        if axis == 'y':
            # create new partitions based on y axis split
            part_1 = Partition(self.x1, self.y1, cut_location - self.y1,  self.width)
            part_2 = Partition(self.x1, cut_location, self.y2 - cut_location, self.width)
        else:
            # create new partitions based on x axis split
            part_1 = Partition(self.x1, self.y1, self.height, cut_location - self.x1)
            part_2 = Partition(cut_location, self.y1, self.height, self.x2 - cut_location)

        # add these partitions to partition dictionary
        check_partitions = [part_1, part_2]
        partitions = {}
        #loop through each partition and run it's split method
        for part in check_partitions:
            #run split on its children recursively. this will eventually pass upward the final partitions
            partitions.update(part.split())
        # return
        return partitions


class WorldGenerator:

    def __init__(self, map):
        self.map = map

    def carve_rect_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.map.map[x][y].blocks_movement = False
                self.map.map[x][y].blocks_sight = False
                self.map.map[x][y].bg = COLOR_GRAY

    def carve_h_tunnel(self,x1,x2,y,):
        for x in range(min(x1, x2), max(x1,x2) + 1):
            self.map.map[x][y].blocks_movement = False
            self.map.map[x][y].blocks_sight = False
            self.map.map[x][y].bg = COLOR_GRAY

    def carve_v_tunnel(self, x, y1, y2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map.map[x][y].blocks_movement = False
            self.map.map[x][y].blocks_sight = False
            self.map.map[x][y].bg = COLOR_GRAY

    # def carve_tunnel(self, x1, y1, x2, y2):
        """
        Carve a tunnel between two points, roughly trying to go in straight lines
        :param x1: x pos 1
        :param y1: y pos 1
        :param x2: x pos 2
        :param y2: y pos 2
        :return:
        """
        """
        # get x and y distance apart
        x_dist = max(x1,x2) - min(x1,x2)
        y_dist = max(y1,y2) - min(y1,y2)

        if x_dist >= y_dist:
    """

    def create_partitions(self,start_x, start_y, height,width):
        """

        :param height: height of first partition
        :param width: width of first partition
        :return: dictionary of all final partitions, key = partition id, item = partition object
        """
        # define the partition that spans the entire area to split apart
        start_partition = Partition(start_x, start_y, height, width)
        # fill the dictionary recursively using partition.split()
        all_partitions = start_partition.split()
        return all_partitions

    def spawn_partition_rooms(self,partition_dict, fill = True):
        """

        :param partition_dict: dictionary of partitions availabe
        :param fill: if true, fills entire partition with room, otherwise spreads and shrinks rooms randomly
        :return:
        """

        for key, part in partition_dict.items():
            if fill:
                # fill entire partition with the room
                self.carve_rect_room(Rect(part.x1,part.y1, part.width, part.height))
            else:
                # fill random section of a partition with a room
                # get a random height and width for the room, as big as the partition itself
                room_height = part.height - round(random.triangular(0, part.height - 3, round(part.height) / 4))
                room_width = part.width - round(random.triangular(0,part.width - 3, round(part.width) / 4))
                # set the new start position based on new width and height
                new_x = round(random.uniform(part.x1, part.x2 - room_width))
                new_y = round(random.uniform(part.y1, part.y2 - room_height))
                self.carve_rect_room(Rect(new_x, new_y, room_width, room_height))








