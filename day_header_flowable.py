from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Flowable

from reportlab.lib.units import mm
from reportlab.lib.colors import Color, black
MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)
class DayHeader(Flowable):
    """
    Draw a header thing for the day with option for (Solem, Feast, Mem, Opt. Mem)
    
    ----                                  ----
    |                MARCH 19                |
    ----    Solemnity of St. Joseph       ----
    
    """
    #----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=90*mm, height=15*mm, date="", title="", level = ""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.date = date
        self.title = title
        self.level = level
        
    #----------------------------------------------------------------------
    def draw(self):
        """
        Draw the shape, text, etc
        """
        ## TODO calc if all fields present and center text vertically
        
        #self.canv.rect(self.x, self.y, self.width, self.height)
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
        self.canv.setFont("Minion", 13)
        self.canv.setFillColor(MAGNIFICAT_RED)
        
        self.canv.drawCentredString( self.width/2, self.y+10*mm, self.date.upper())
        

        if(self.level=="S"):
            self.canv.setFont("Minion", 8)
            self.canv.setFillColor(MAGNIFICAT_RED)
            self.canv.drawCentredString(self.width/2, self.y+6*mm, "SOLEMNITY")
            self.canv.setFont("MinionSub", 8)
            self.canv.setFillColor(black)
            self.canv.drawCentredString(self.width/2, self.y+2*mm, self.title.upper())
        elif self.level == "F":
            self.canv.setFont("Minion", 8)
            self.canv.setFillColor(MAGNIFICAT_RED)
            self.canv.drawCentredString(self.width/2, self.y+6*mm, "FEAST")
            self.canv.setFont("MinionSub", 8)
            self.canv.setFillColor(black)
            self.canv.drawCentredString(self.width/2, self.y+2*mm, self.title)
        elif self.level == "M":
            self.canv.setFont("Minion", 8)
            self.canv.setFillColor(MAGNIFICAT_RED)
            self.canv.drawCentredString(self.width/2, self.y+6*mm, "MEMORIAL")
            self.canv.setFont("MinionSub", 8)
            self.canv.setFillColor(black)
            self.canv.drawCentredString(self.width/2, self.y+2*mm, self.title)
        elif self.level == "m":
            self.canv.setFont("Minion", 8)
            self.canv.setFillColor(MAGNIFICAT_RED)
            self.canv.drawCentredString(self.width/2, self.y+6*mm, "OPT. MEMORIAL")
            self.canv.setFont("MinionSub", 8)
            self.canv.setFillColor(black)
            self.canv.drawCentredString(self.width/2, self.y+2*mm, self.title)