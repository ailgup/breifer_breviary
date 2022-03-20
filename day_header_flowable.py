from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Flowable

from reportlab.lib.units import mm
from reportlab.lib.colors import Color, black
from reportlab.pdfbase.pdfmetrics import stringWidth

MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)

HEADER_WIDTH = 90*mm

##FORMATTING
DATE_FONT = "Minion"
DATE_FONT_SIZE = 13
DATE_FONT_COLOR = MAGNIFICAT_RED

LEVEL_FONT = "Minion"
LEVEL_FONT_SIZE = 8
LEVEL_FONT_COLOR = MAGNIFICAT_RED

TITLE_FONT = "MinionSub"
TITLE_FONT_SIZE = 8
TITLE_FONT_COLOR = black
class DayHeader(Flowable):
    """
    Draw a header thing for the day with option for (Solem, Feast, Mem, Opt. Mem)
    
    ----                                        ----
    |                MARCH 19 (Date)                |
    |               SOLEMNITY  (Level)              |
    ----            St. Joseph  (Title)          ----
    
    """
    

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=15*mm, date="", title="", level = ""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.date = date
        self.title = title
        self.level = level
        
        self.date_font_size = DATE_FONT_SIZE
        self.level_font_size = LEVEL_FONT_SIZE
        self.title_font_size = TITLE_FONT_SIZE
        
    #----------------------------------------------------------------------
    
    def resize_date_to_fit(self, text, font, font_size, width = HEADER_WIDTH, percentage_margin = 0.75):

        while (stringWidth(text,font,font_size) > width * percentage_margin):
            font_size = font_size - 1
            
        return font_size
        
    
    def calc_height(self):
        POINT_TO_MM = 1
        MARGIN_PERCENTALE = 1.5
        
        total_height = (bool(self.date)*self.date_font_size + bool(self.title)*self.title_font_size + bool(self.level)*self.level_font_size) 
        total_height = POINT_TO_MM * total_height
        total_height = MARGIN_PERCENTALE * total_height
        self.height = total_height
        
    
    def draw(self):
        """
        Draw the shape, text, etc
        """
        ## TODO resize font if too wide
        self.date_font_size = self.resize_date_to_fit(self.date,DATE_FONT,self.date_font_size)
        self.calc_height()
        
        #resize date if it is too long for container
        
        
        bracket_width = 5*mm
        
        self.canv.setLineWidth(3)

        offset = 0.5 #needed to suqare up corners
        #verticle members
        self.canv.line(self.x, self.y-offset, self.x, self.y+self.height+offset)
        self.canv.line(self.x+self.width, self.y-offset, self.x+self.width, self.y+self.height+offset)
        
        self.canv.setLineWidth(1)
        #left horozontal
        self.canv.line(self.x, self.y, self.x+bracket_width, self.y)
        self.canv.line(self.x, self.y+self.height, self.x+bracket_width, self.y+self.height)
        
        #right horozontal
        self.canv.line(self.x+self.width, self.y, self.x+self.width-bracket_width, self.y)
        self.canv.line(self.x+self.width, self.y+self.height, self.x+self.width-bracket_width, self.y+self.height)
        
        #DATE STYLE
        self.canv.setFont(DATE_FONT,self.date_font_size)
        self.canv.setFillColor(DATE_FONT_COLOR)
        
        self.canv.drawCentredString( self.width/2, self.y+self.height-self.date_font_size, self.date.upper())
        
        #LEVEL STYLE
        self.canv.setFont(LEVEL_FONT, self.level_font_size)
        self.canv.setFillColor(LEVEL_FONT_COLOR)
        
        if(self.level=="S"):
            self.canv.drawCentredString(self.width/2, self.y+self.height-self.date_font_size-self.level_font_size, "SOLEMNITY")
        elif self.level == "F":
            self.canv.drawCentredString(self.width/2, self.y+self.height-self.date_font_size-self.level_font_size, "FEAST")
        elif self.level == "M":
            self.canv.drawCentredString(self.width/2, self.y+self.height-self.date_font_size-self.level_font_size, "MEMORIAL")
        elif self.level == "m":
            self.canv.drawCentredString(self.width/2, self.y+self.height-self.date_font_size-self.level_font_size, "OPTIONAL MEMORIAL")
            
        #TITLE STYLE
        self.canv.setFont("MinionSub", 8)
        self.canv.setFillColor(black)
        self.canv.drawCentredString(self.width/2, self.y+self.title_font_size, self.title)
        