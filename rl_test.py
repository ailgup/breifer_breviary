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
from day_header_flowable import DayHeader



MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)



def main():
    #used for titles
    pdfmetrics.registerFont(TTFont('Arno', 'ArnoPro-Bold.ttf'))
    #used for psalms
    pdfmetrics.registerFont(TTFont('Minion', 'Minion Pro Medium Cond Caption.ttf'))
    #used for day subheadings
    pdfmetrics.registerFont(TTFont('MinionSub', 'MinionPro-Subh.ttf'))

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
        story.append(Paragraph("O Lord open my lips...",stylePsalm))
        if i%20==0:
            box = DayHeader(date="March 19", title="Solemnity of St. Joseph",level="S")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="March 17", title="St. Patrick",level="m")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="February 2", title="Presentation of the Lord",level="F")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="December 3", title="St. Francis Xavier",level="M")
            story.append(box)
            
            box = DayHeader(date="Tuesday Week III")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="Common of the Blessed Virgin Mary", title="Evening Prayer I")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="Thirty-Second Sunday in Ordinary Time")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="March 19", title="Solemnity of St. Joseph",level="S")
            story.append(box)
            
            story.append(Paragraph("O Lord open my lips...",stylePsalm))
            
            box = DayHeader(date="Solemnity of Jesus Christ the King of the Universe")
            story.append(box)
     # C6 = (114*mm,162*mm)
    doc = BaseDocTemplate('mydoc.pdf', pagesize=C6,
                            pageTemplates=[],
                            showBoundary=0,
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