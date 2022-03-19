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
        self.font_scaling_ratio = 1
        
    #----------------------------------------------------------------------
    
    def resize_date_to_fit(self):
        print("stringWidth ",stringWidth(self.date,DATE_FONT,(DATE_FONT_SIZE*self.font_scaling_ratio))*mm)
        print(90*mm)
        while stringWidth(self.date,DATE_FONT,(DATE_FONT_SIZE*self.font_scaling_ratio)) > HEADER_WIDTH:
            self.font_scaling_ratio=self.font_scaling_ratio*0.85
        
    
    def calc_height(self):
        POINT_TO_MM = 1
        MARGIN_PERCENTALE = 1.5
        
        total_height = (bool(self.date)*DATE_FONT_SIZE + bool(self.title)*TITLE_FONT_SIZE + bool(self.level)*LEVEL_FONT_SIZE) 
        total_height = POINT_TO_MM * total_height
        total_height = MARGIN_PERCENTALE * total_height
        self.height = total_height
        
    
    def draw(self):
        """
        Draw the shape, text, etc
        """
        ## TODO resize font if too wide
        
        self.calc_height()
        
        #resize date if it is too long for container
        self.resize_date_to_fit()
        
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
        self.canv.setFont(DATE_FONT,DATE_FONT_SIZE * self.font_scaling_ratio)
        self.canv.setFillColor(DATE_FONT_COLOR)
        
        self.canv.drawCentredString( self.width/2, self.y+self.height-DATE_FONT_SIZE, self.date.upper())
        
        #LEVEL STYLE
        self.canv.setFont(LEVEL_FONT, LEVEL_FONT_SIZE)
        self.canv.setFillColor(LEVEL_FONT_COLOR)
        
        if(self.level=="S"):
            self.canv.drawCentredString(self.width/2, self.y+self.height-DATE_FONT_SIZE-LEVEL_FONT_SIZE, "SOLEMNITY")
        elif self.level == "F":
            self.canv.drawCentredString(self.width/2, self.y+self.height-DATE_FONT_SIZE-LEVEL_FONT_SIZE, "FEAST")
        elif self.level == "M":
            self.canv.drawCentredString(self.width/2, self.y+self.height-DATE_FONT_SIZE-LEVEL_FONT_SIZE, "MEMORIAL")
        elif self.level == "m":
            self.canv.drawCentredString(self.width/2, self.y+self.height-DATE_FONT_SIZE-LEVEL_FONT_SIZE, "OPTIONAL MEMORIAL")
            
        #TITLE STYLE
        self.canv.setFont("MinionSub", 8)
        self.canv.setFillColor(black)
        self.canv.drawCentredString(self.width/2, self.y+TITLE_FONT_SIZE, self.title)
        