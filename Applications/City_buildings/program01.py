import images

class palace:
  """
  This class is used as a custom data structure, and considering the palace in 2 dimension, each palace is defined by:
  -base
  -height
  -color
  """
  base = int()
  height = int()
  color = tuple() #(red,green,blue) parameters are int

  def __init__(self, base,height,color):
      self.base = int(base)
      self.height = int(height)
      self.color = color

def create_matrix(height, width, value=(0,0,0)):
    return [[value] * width for pixel in range(height)]

def fill_rect(im, x, y, Wr, Hr, col):
    """
    im is the image
    x,y are the coordinates of the start point
    Wr, Hr are the width and the height of the rectangle
    col is the color
    x,y -------------- x+Wr-1,y
    |-------------------- |
    |                     |                                          
    |                     |                     
    |                     |                     
    x,y+Hr-1,---------x+Wr-1,y+Hr-1
    """

    for delta_h in range(Hr):
        im[y+delta_h][x:x+Wr] = [col] * Wr



def create_map(line_lenght,spacing,list_of_palaces):
    #Given the standard lenght of the line, the spacing parameter and the list of palaces, creates the actual map
    
    def calculate_horizontal_spacing(line_of_palaces,spacing,line_lenght):      
      #Calculates the spacing between each palace on the line
      
      d = len(line_of_palaces)-1
      if not (len(line_of_palaces)-1):
        d = 1    
      return (line_lenght - sum([palace.base for palace in line_of_palaces])-2*spacing)//d

    y = spacing    
    im = [] + create_matrix(spacing,line_lenght,(0,0,0))
    for line_of_palaces in list_of_palaces:    
        horizontal_spacing = calculate_horizontal_spacing(line_of_palaces,spacing,line_lenght)
        line_height = max([palace.height for palace in line_of_palaces])
        im = im + create_matrix((line_height + spacing), line_lenght,(0,0,0))
        x = spacing
        for palace in line_of_palaces:    
            if not len(line_of_palaces) - 1:
                x = (line_lenght - 2*spacing - palace.base)//2 + spacing
            fill_rect(im,x,(y + ((line_height - palace.height)//2)),palace.base,palace.height,palace.color)                             
            x += palace.base + horizontal_spacing
        y += line_height + spacing
    return im


def ex(inputfile,outputfile,spacing):     
    input_list_of_palaces = [(line.replace("\t","").replace(" ","").split(",")) for line in inputfile]

    list_of_palaces = [[(palace(subline_palace[0],subline_palace[1],(int(subline_palace[2]),int(subline_palace[3]),int(subline_palace[4])))) \
                 for subline_palace in [line[:len(line)-1][i:i+5] for i in range(len(line[:len(line)-1])) if not (i%5)]] for line in input_list_of_palaces ]  
    
    line_lenght = max([(sum([palace.base + spacing for palace in line_of_palaces]) + spacing) for line_of_palaces in list_of_palaces])

    im =  create_map(line_lenght,spacing,list_of_palaces)  
    images.save(im, outputfile)
    return (line_lenght,len(im))

'''
Reference track:

The mayor of a city has to plan a new neighborhood.  You are part of
the architectural firm that has to design the neighborhood. You
are provided with a file that contains, divided into rows, the
information that describes the East-West (E-W) strip of buildings in
the plan. Each building is described with width, height, color.

The buildings must be arranged in a rectangular plan so that:
  - all around the neighborhood there is a street of minimum width
    indicated.
  - in the E-W (horizontal) direction, there are the main streets,
    straight and of the same minimum width, separating one strip of
    E-W buildings from the next.  Each E-W strip may
    contain a variable number of buildings.  If a strip contains one
    building will be placed in the center of the strip.
  - in the N-S direction, between each pair of consecutive buildings,
    there must be at least room for a side street of the same
    minimum width as the others.  


You are asked to calculate the minimum size of the plot of land that
will contain the buildings.  And also to construct the map that shows
the buildings in the plan.

Your firm of architects has decided to arrange the buildings so that
they are **equally spaced** in the E-W direction, and to make sure
that each strip E-W of building is distant from the next one the
minimum space required forthe main streets.

To make the neighborhood more diverse, your firm has decided that, the
buildings, instead of being aligned with the main streets, have to
have a front garden (in front of S) and one behind (behind N) of equal
depth. Similarly, where possible, the space between the side streets
and the buildings should be **evenly distributed** so that everyone
can have an E and a W garden of equal depth. Only those buildings that
face on the streets on the left and on the right side of the map do
not have gardens on that side.

You are provided with a txt file that contains data indicating which
buildings to put on the map.  The file contains on each line groups
of 5 integer values, followed by 1 comma and/or 0 (or more) spaces or
tabs. Each quintuple represents a building with:
  - width
  - height
  - intensity of R color channel
  - intensity of G color channel
  - intensity of B color channel

Each row contains at least one group of 5 positive integers related to
a building to be drawn. For each building you must draw a rectangle of
the given color and size.

Create the function ex(file_data, file_png, spacing) which:
  - reads the data from file_data
  - builds an image in PNG format of the map and saves it in the
    file_png file
  - returns the dimensions width, height of the map image

The map must have a black background and display all the buildings as follows:
  - the spacing argument indicates the number of pixels to be used for
    the space required for the external, main and secondary streets,
    i.e. the minimum spacing horizontally between rectangles; and
    vertically between rows of buildings
  - each building is represented by a rectangle described by a
    quintuple in the file
  - the buildings described on each line of the file must be
    drawn, vertically centered, on a strip in the E-W direction of the map
  - the buildings in the same strip must be equidistant horizontally
    from each other with a **minimum distance of pixel 'spacing'
    between one building and the next** so that all the the first
    buildings are on the edge of the left-vertical street;
    all the last buildings are on the edge of the right street.
    NOTE: if the strip contains a single building, it must be drawn
    centered horizontally
  - each strip is at a minimum distance vertically to make room for
    the main road. 
    NOTE: the vertical distance is calculated between the
    two tallest buildings highest of two consecutive bands.
    The largest building in the first row is leaning against the
    edge of the upper E-W main street. 
    The larger building in the last row is leaning against the edge of the
    lower E-W main street.
  - the image has the minimum possible size, therefore:
     - there is at least one building in the first/last row at a
       pixel 'spacing' from the top/bottom edge
     - there is at least one strip that has the first and last building
       at pixel 'spacing' from the left/right edge
     - there is at least one E-W strip where buildings have non gardens
       on the E or W side

    NOTE: in drawing the buildings you can assume that the coordinates
          will always be integer (if they are not, you have made a
          mistake). 
    NOTE: Width and height of rectangles are all multiples of two.
'''
