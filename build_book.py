# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
from reportlab.lib.pagesizes import C6
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from BreviaryDocTemplate import *
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from reportlab.lib.colors import Color

# homemade
from SectionStyles import *
from Hour import *

MAGNIFICAT_RED = Color(214 / 255, 50 / 255, 84 / 255, alpha=1)

antiphon_on_current_page = False

def build_hour(h, story):
    # Header
    box = DayHeader(date=h.day, title="Week " + h.week_roman)
    story=psalm_split_correctly(box,story)

    hour = HourHeader(hour=h.hour)
    story.append(hour)

    # Hymn
    hymn = Hymn(hymns=h.hymn)
    story = psalm_split_correctly(hymn, story)

    # PSALMODY
    a = Antiphon(antiphon=h.ant_1)
    story = psalm_split_correctly(a, story)
    p = Psalm(h.ps_1)
    story = psalm_split_correctly(p, story)
    a = Antiphon(antiphon=h.ant_1)
    story = psalm_split_correctly(a, story)

    a = Antiphon(antiphon=h.ant_2)
    story = psalm_split_correctly(a, story)
    p = Psalm(h.ps_2)
    story = psalm_split_correctly(p, story)
    a = Antiphon(antiphon=h.ant_2)
    story = psalm_split_correctly(a, story)

    a = Antiphon(antiphon=h.ant_3)
    story = psalm_split_correctly(a, story)
    p = Psalm(h.ps_3)
    story = psalm_split_correctly(p, story)
    a = Antiphon(antiphon=h.ant_3)
    story = psalm_split_correctly(a, story)

    r = Reading(reading=h.reading)
    psalm_split_correctly(r, story)

    r = Responsory(responses=h.response)
    psalm_split_correctly(r, story)

    if h.hour == Breviary.MORNING_PRAYER:
        s = SectionHeader(title="Canticle of Zechariah")
        story = psalm_split_correctly(s, story)
    elif h.hour == Breviary.EVENING_PRAYER:
        s = SectionHeader(title="Canticle of Mary")
        story = psalm_split_correctly(s, story)
    elif h.hour == Breviary.NIGHT_PRAYER:
        s = SectionHeader(title="Canticle of Simeon")
        story = psalm_split_correctly(s, story)

    a = Antiphon(antiphon=h.canticle_ant)
    story = psalm_split_correctly(a, story)

    i = Intercessions(intercessions=h.intercessions)
    story = psalm_split_correctly(i, story)

    p = Prayer(prayers=h.prayer)
    story = psalm_split_correctly(p, story)
    return story

def build_story():
    story = []
    r = fetch_rows()
    h = process_row(r)
    for i in range(10):
        story = build_hour(h, story)



    return story


def main():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase.pdfmetrics import registerFontFamily

    # used for titles
    pdfmetrics.registerFont(TTFont('Arno', 'fonts/ArnoPro-Bold.ttf'))
    # used for psalms
    pdfmetrics.registerFont(TTFont('Minion_med', 'Minion Pro Medium Cond Caption.ttf'))
    pdfmetrics.registerFont(TTFont('Minion', 'fonts/Minion Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_b', 'fonts/Minion Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_b_i', 'fonts/Minion Bold Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Minion_i', 'fonts/Minion Italic.ttf'))

    # used for day subheadings
    pdfmetrics.registerFont(TTFont('MinionSub', 'fonts/MinionPro-Subh.ttf'))
    # used for hour headings
    pdfmetrics.registerFont(TTFont('MinionSub_bold', 'fonts/Minion Pro Bold Subhead.ttf'))

    registerFontFamily('Minion', normal='Minion', bold='Minion_b', italic='Minion_i', boldItalic='Minion_b_i')

    story = build_story()

    # add some flowables

    # C6 = (114*mm,162*mm)
    doc = BreviaryDocTemplate('mydoc.pdf', pagesize=C6,
                          pageTemplates=[],
                          showBoundary=1,
                          leftMargin=10 * mm,
                          rightMargin=10 * mm,
                          topMargin=10 * mm,
                          bottomMargin=10 * mm,
                          allowSplitting=1,
                          title='A Briefer Breviary',
                          author=None,
                          _pageBreakQuick=1,
                          encrypt=None)
    doc.page_title = "Tuesday of Holy Week"

    # normal frame as for SimpleFlowDocument
    frame_t = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

    doc.addPageTemplates([PageTemplate(id='OneCol', frames=frame_t, onPage=add_header)
                          ])
    doc.build(story, canvasmaker=NumberedCanvas)


def psalm_split_correctly(psalm, story):
    # accepts a Psalm (obj) and a Story (obj) and adds paragraph-wise to keep stanzas together

    for stanza in psalm.paragraphs:
        story.append(stanza[2])
    return story


def add_header(canvas, doc):
    # Page Number
    canvas.setFont("Minion", 7)
    PAGE_NUMBER_Y_MARGIN = 5 * mm
    PAGE_NUMBER_X_MARGIN = 5 * mm

    # even pages get number on left, odd on right
    x_loc = PAGE_NUMBER_X_MARGIN
    if doc.page % 2:
        x_loc = C6[0] - PAGE_NUMBER_X_MARGIN
        canvas.drawRightString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
                               "%d" % doc.page)
    else:
        canvas.drawString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
                          "%d" % doc.page)

    # Title

    canvas.setFont("Minion", 7)
    canvas.setFillColor(MAGNIFICAT_RED)
    canvas.textTransform = "uppercase"
    PAGE_NUMBER_Y_MARGIN = 5 * mm
    PAGE_NUMBER_X_MARGIN = 15 * mm

    # even pages get number on left, odd on right
    x_loc = PAGE_NUMBER_X_MARGIN
    if doc.page % 2:
        x_loc = C6[0] - PAGE_NUMBER_X_MARGIN
        canvas.drawRightString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
                               canvas.pageTitle)
    else:
        canvas.drawString(x_loc, C6[1] - PAGE_NUMBER_Y_MARGIN,
                          canvas.pageTitle)


class NumberedCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
        self.pageTitle = "Monday of the First Week of Lent"

    def show_page(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        for state in self._saved_page_states:
            self.__dict__.update(state)
            canvas.Canvas.show_page(self)
        canvas.Canvas.save(self)


if __name__ == "__main__":
    main()
