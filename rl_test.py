from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Flowable

from reportlab.lib.pagesizes import C6
from reportlab.platypus import Paragraph, SimpleDocTemplate
# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from reportlab.lib.colors import Color

#homemade
from day_header_flowable import DayHeader, HourHeader, Antiphon, Psalm, Reading, Intercessions



MAGNIFICAT_RED = Color( 214/255 ,50/255, 84/255, alpha=1)

antiphon_on_current_page = False

def main():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
 
    
    
    #used for titles
    pdfmetrics.registerFont(TTFont('Arno', 'fonts/ArnoPro-Bold.ttf'))
    #used for psalms
    pdfmetrics.registerFont(TTFont('Minion_med', 'Minion Pro Medium Cond Caption.ttf'))
    pdfmetrics.registerFont(TTFont('Minion', 'fonts/Minion Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_b', 'fonts/Minion Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_b_i', 'fonts/Minion Bold Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_i', 'fonts/Minion Italic.ttf'))
    
    #used for day subheadings
    pdfmetrics.registerFont(TTFont('MinionSub', 'fonts/MinionPro-Subh.ttf'))
    #used for hour headings
    pdfmetrics.registerFont(TTFont('MinionSub_bold', 'fonts/Minion Pro Bold Subhead.ttf'))

    registerFontFamily('Minion', normal='Minion', bold='Minion_b', italic='Minion_i', boldItalic='Minion_b_i')

    story = []
    #add some flowables
    
    for i in range (40):
       
        if i%20==0:
            box = DayHeader(date="Sunday", title="Week II")
            story.append(box)
                       
            hour = HourHeader(hour = "Evening Prayer I")
            story.append(hour)
            a = Antiphon(antiphon = [("Ant.","Your word, O Lord is the lantern to light our way, alleluia."),
                                                ("Advent:","New City of Zion, let your heart sing for joy; see how humbly your king comes to save you."),
                                                ("Lent, 2nd Sunday:","Jesus took Peter, James and his brother John and let them up a high mountain. There he was transfigured before them."),
                                                ("Lent Palm Sunday:","Day after day I sat teaching you in the temple and you did not lay hands on me. Now you come to scourge me and lead me to the cross."),
                                                ("Easter, 6th Sunday:","The man of truth welcomes the light, alleluia.")
                                                ])
            psalm_split_correctly(a,story) 
            p=Psalm(verse = "Psalm 119:105-112", 
                                 titles = ["XIV (Nun)","A Meditation on God's Law"], 
                                 summary="This is my commandment: that you should love one another", 
                                 summary_verse = "(John 15:12)", 
                                 text="Your word is a lamp for my steps <br />and a light for my path.<br />I have sworn and have made up my mind <br />to obey your decrees.<br /><br />Lord, I am deeply afflicted: <br />by your word give me life.<br />Accept, Lord, the homage of my lips <br />and teach me your decrees.<br /><br />Though I carry my life in my hands, <br />I remember your law.<br />Though the wicked try to ensnare me <br />I do not stray from your precepts.<br /><br />Your will is my heritage for ever, <br />the joy of my heart.<br />I set myself to carry out your will <br />in fullness, for ever. Glory..."
                                )
            psalm_split_correctly(p,story)  

            p=Psalm(verse="Psalm 16",
                    titles=["The Lord himself is my heritage"],
                    summary = "The Father raised up Jesus, freeing him from the grip of death",
                    summary_verse = "Acts 2:24",
                    text='<p>Preserve me, God, I take refuge in you.<br />I say to you Lord "You are my God.<br />My happiness lies in you alone."<br /><br />You have put into my heart a marvelous love<br />for the faithful ones who dwell in your land.<br />Those who choose other gods increase their sorrows.<br />Never will I offer their offerings of blood.<br />Never will I take their name upon my lips.<br /><br />O Lord, it is you who are my portion and cup,<br />it is you yourself who are my prize.<br />The lot marked out for me is my delight,<br />welcome indeed the heritage that falls to me!<br /><br />I will bless the Lord who gives me counsel,<br />who even at night directs my heart.<br />I keep the Lord ever in my sight:<br />since he is at my right hand, I shall stand firm.<br /><br />And so my heart rejoices, my soul is glad;<br />even my body shall rest in safety.<br />For you will not leave my soul among the dead,<br />nor let your beloved know decay.<br /><br />You will show me the path of life,<br />the fullness of joy in your presence,<br />at your right hand happiness for ever. Glory...</p>'
                    )
            psalm_split_correctly(p,story)         
                 
            p=Psalm(verse = "Canticle  -  Philippians 2:6-11", 
                                 titles = ["Christ, God's holy servant"], 
                                 summary="", 
                                 summary_verse = "",
                                 text='Though he was in the form of God, <br />Jesus did not deem equality with God <br />something to be grasped at.<br /><br />Rather, he emptied himself <br />and took the form of a slave, <br />being born in the likeness of men.<br /><br />He was known to be of human estate, <br />and it was thus that he humbled himself,<br />obediently accepting even death, <br />death on a cross!<br /><br />Because of this, <br />God highly exalted him<br />and bestowed on him the name <br />above every other name,<br /><br />So that at Jesus&rsquo; name <br />every knee must bend<br />in the heavens, on the earth, <br />and under the earth,<br />and every tongue proclaim <br />to the glory of God the Father: <br />JESUS CHRIST IS LORD! Glory...'
            )
            psalm_split_correctly(p,story)
            
            #reading
            r=Reading(book="Colossians",verse="1:2b-6a",text="May God our Father give you grace and peace. We always give thanks to God, the Father of our Lord Jesus Christ, in our prayers for you because we have heard of your faith in Christ Jesus and the love you bear toward all the saints - moved as you are by the hope held in store for you in heaven. You heard of this hope through the message of truth, the gospel, which has come to you, has borne fruit, and has continued to grow in your midst, as it has everywhere in the world.")
            psalm_split_correctly(r,story)
                
            i = Intercessions(first = "God aids and protects the people he has chosen for his inheritance.  Let us give thanks to him and proclaim his goodness:",
                                response = "Lord, we trust in you.",
                                intercessions = [["We pray for N., our Pope, and N., our bishop,","protect them and in your goodness make them holy."],["May the sick feel their companionship with the suffering Christ,","and know that they will enjoy his eternal consolation."],["In your goodness have compassion on the homeless,","help them to find proper housing."],["In your goodness give and preserve the fruits of the earth,","so that each day there may be bread enough for all."],["Lord, you attend the dying with great mercy,","grant them an eternal dwelling."]]
                                )
            psalm_split_correctly(i,story)   
           
           
            a = Antiphon(antiphon = [("Ant.","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Advent:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Lent, 2nd Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Lent Palm Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
                                                ("Easter, 6th Sunday:","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                                                ])
            psalm_split_correctly(a,story)
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

def psalm_split_correctly(psalm, story):
    # accepts a Psalm (obj) and a Story (obj) and adds paragraph-wise to keep stanzas together

    for stanza in psalm.paragraphs:
        story.append(stanza[2])
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