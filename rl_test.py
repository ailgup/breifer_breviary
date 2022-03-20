from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Flowable

from reportlab.lib.pagesizes import C6
from reportlab.platypus import Paragraph, SimpleDocTemplate
# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from reportlab.lib.colors import Color

#homemade
from day_header_flowable import DayHeader, HourHeader, Antiphon, Psalm



MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)



def main():
    #used for titles
    pdfmetrics.registerFont(TTFont('Arno', 'ArnoPro-Bold.ttf'))
    #used for psalms
    pdfmetrics.registerFont(TTFont('Minion', 'Minion Pro Medium Cond Caption.ttf'))
    #used for day subheadings
    pdfmetrics.registerFont(TTFont('MinionSub', 'MinionPro-Subh.ttf'))
    #used for hour headings
    pdfmetrics.registerFont(TTFont('MinionSub_bold', 'Minion Pro Bold Subhead.ttf'))

    styles = getSampleStyleSheet()

    styleHeading = ParagraphStyle(name='Heading',
                                parent=styles['Normal'],
                                fontName = 'Arno')
    stylePsalm = ParagraphStyle(name='Psalm',
                                parent=styles['Normal'],
                                fontName = 'Minion',
                                alignment = 0,
                                allowOrphans = 0,
                                allowWidows = 1,
                                backColor = None,
                                borderColor = None,
                                borderPadding = 0,
                                borderRadius = None,
                                borderWidth = 0,
                                bulletAnchor = None,
                                bulletFontName = None,
                                bulletFontSize = 10,
                                bulletIndent = 0,
                                embeddedHyphenation = 0,
                                endDots = None,
                                firstLineIndent = 0,
                                fontSize = 10,
                                hyphenationLang = None,
                                justifyBreaks = 0,
                                justifyLastLine = 0,
                                leading = 12,
                                leftIndent = 0,
                                linkUnderline = 0,
                                rightIndent = 0,
                                spaceAfter = 0,
                                spaceBefore = 0,
                                spaceShrinkage = 0.05,
                                splitLongWords = 1,
                                strikeGap = 1,
                                strikeOffset = 0.25*mm,
                                strikeWidth =None,
                                textColor = Color(0,0,0,1),
                                textTransform = None,
                                underlineGap = 1,
                                underlineOffset = -0.125*mm,
                                underlineWidth =None,
                                uriWasteReduce = 0,
                                wordWrap = None
                                )
    styleDayTitle = ParagraphStyle(name='DayTitle',
                                parent=styles['Normal'],
                                fontName = 'Minion',
                                alignment = 0,
                                allowOrphans = 0,
                                allowWidows = 1,
                                backColor = None,
                                borderColor = None,
                                borderPadding = 0,
                                borderRadius = None,
                                borderWidth = 0,
                                bulletAnchor = None,
                                bulletFontName = None,
                                bulletFontSize = 10,
                                bulletIndent = 0,
                                embeddedHyphenation = 0,
                                endDots = None,
                                firstLineIndent = 0,
                                fontSize = 20,
                                hyphenationLang = None,
                                justifyBreaks = 0,
                                justifyLastLine = 0,
                                leading = 12,
                                leftIndent = 0,
                                linkUnderline = 0,
                                rightIndent = 0,
                                spaceAfter = 0,
                                spaceBefore = 0,
                                spaceShrinkage = 0.05,
                                splitLongWords = 1,
                                strikeGap = 1,
                                strikeOffset = 0.25*mm,
                                strikeWidth =None,
                                textColor = Color(0,0,0,1),
                                textTransform = None,
                                underlineGap = 1,
                                underlineOffset = -0.125*mm,
                                underlineWidth =None,
                                uriWasteReduce = 0,
                                wordWrap = None
                                )
    story = []
    #add some flowables
    
    for i in range (40):
       
        if i%20==0:
            box = DayHeader(date="March 19", title="St. Joseph",level="S")
            story.append(box)
                       
            hour = HourHeader(hour = "Office of Readings")
            story.append(hour)
            story.append(Antiphon(antiphon = [("Ant.","Your word, O Lord is the lantern to light our way, alleluia."),
                                                ("Advent:","New City of Zion, let your heart sing for joy; see how humbly your king comes to save you."),
                                                ("Lent, 2nd Sunday:","Jesus took Peter, James and his brother John and let them up a high mountain. There he was transfigured before them."),
                                                ("Lent Palm Sunday:","Day after day I sat teaching you in the temple and you did not lay hands on me. Now you come to scourge me and lead me to the cross."),
                                                ("Easter, 6th Sunday:","The man of truth welcomes the light, alleluia.")
                                                ]))
            story.append(Psalm(verse = "Psalm 119:105-112", 
                                 titles = ["XIV (Nun)","A Meditation on God's Law"], 
                                 summary="This is my commandment: that you should love one another", 
                                 summary_verse = "(John 15:12)", 
                                 text="Your word is a lamp for my steps <br />and a light for my path.<br />I have sworn and have made up my mind <br />to obey your decrees.<br /><br />Lord, I am deeply afflicted: <br />by your word give me life.<br />Accept, Lord, the homage of my lips <br />and teach me your decrees.<br /><br />Though I carry my life in my hands, <br />I remember your law.<br />Though the wicked try to ensnare me <br />I do not stray from your precepts.<br /><br />Your will is my heritage for ever, <br />the joy of my heart.<br />I set myself to carry out your will <br />in fullness, for ever.<br /><br />Glory to the Father, and to the Son, <br />and to the Holy Spirit:<br />as it was in the beginning, is now, <br />and will be for ever. Amen."
                                ))
            for i in range (10):
                story.append(Paragraph("<para color=red>hiiiiiii</para>",stylePsalm))
                story.append(Paragraph("Your word is a lamp for my steps <br />and a light for my path.<br />I have sworn and have made up my mind <br />to obey your decrees.<br /><br />Lord, I am deeply afflicted: <br />by your word give me life.<br />Accept, Lord, the homage of my lips <br />and teach me your decrees.<br /><br />Though I carry my life in my hands, <br />I remember your law.<br />Though the wicked try to ensnare me <br />I do not stray from your precepts.<br /><br />Your will is my heritage for ever, <br />the joy of my heart.<br />I set myself to carry out your will <br />in fullness, for ever.<br /><br />Glory to the Father, and to the Son, <br />and to the Holy Spirit:<br />as it was in the beginning, is now, <br />and will be for ever. Amen."
                                ,stylePsalm))                                    
            story.append(Antiphon(antiphon = [("Ant.","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Advent:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Lent, 2nd Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Lent Palm Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Easter, 6th Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                                                ]))
     # C6 = (114*mm,162*mm)
    doc = BaseDocTemplate('mydoc.pdf', pagesize=C6,
                            pageTemplates=[],
                            showBoundary=1,
                            leftMargin=10*mm,
                            rightMargin=10*mm,
                            topMargin=10*mm,
                            bottomMargin=10*mm,
                            allowSplitting=1,
                            title=None,
                            author=None,
                            _pageBreakQuick=1,
                            encrypt=None)
    doc.page_title = "Tuesday of Holy Week"
    
    #normal frame as for SimpleFlowDocument
    frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    
    doc.addPageTemplates([PageTemplate(id='OneCol',frames=frameT,onPage=add_header)
                       ])
    doc.build(story, canvasmaker = NumberedCanvas)

def add_header(canvas,doc):

    # Page Number
    canvas.setFont("Minion", 7)
    PAGE_NUMBER_Y_MARGIN = 5*mm
    PAGE_NUMBER_X_MARGIN = 5*mm
    
    # even pages get number on left, odd on right
    x_loc = PAGE_NUMBER_X_MARGIN
    if doc.page % 2:
        x_loc = C6[0] - PAGE_NUMBER_X_MARGIN
        canvas.drawRightString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
        "%d" % (doc.page))
    else:
        canvas.drawString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
        "%d" % (doc.page))
    
    # Title
    
    canvas.setFont("Minion", 7)
    canvas.setFillColor(MAGNIFICAT_RED)
    canvas.textTransform = "uppercase"
    PAGE_NUMBER_Y_MARGIN = 5*mm
    PAGE_NUMBER_X_MARGIN = 15*mm
    
    # even pages get number on left, odd on right
    x_loc = PAGE_NUMBER_X_MARGIN
    if doc.page % 2:
        x_loc = C6[0] - PAGE_NUMBER_X_MARGIN
        canvas.drawRightString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
        canvas.pageTitle)
    else:
        canvas.drawString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
        canvas.pageTitle)
            
    
    
def foot2(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(mm, 0.75 * mm, "Page %d" % doc.page)
    canvas.restoreState()

class NumberedCanvas(canvas.Canvas):
    
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
        self.pageTitle = "Monday of the First Week of Lent"

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            #self.draw_page_number(num_pages)
           # self.draw_page_title()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)


    
    def draw_page_number(self, page_count):
        
        self.setFont("Minion", 7)
        PAGE_NUMBER_Y_MARGIN = 5*mm
        PAGE_NUMBER_X_MARGIN = 5*mm
        
        # even pages get number on left, odd on right
        x_loc = PAGE_NUMBER_X_MARGIN
        if self._pageNumber % 2:
            x_loc = C6[0] - PAGE_NUMBER_X_MARGIN
            self.drawRightString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
            "%d" % (self._pageNumber))
        else:
            self.drawString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
            "%d" % (self._pageNumber))
            
if __name__ == "__main__":
    main()