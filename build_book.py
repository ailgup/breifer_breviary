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


def build_mp_ep(h, story):
    # Header
    box = DayHeader(date=h.day, title="Week " + h.week_roman)
    story = psalm_split_correctly(box, story)

    hour = HourHeader(hour=h.hour)
    story=psalm_split_correctly(hour,story)

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
    elif Breviary.EVENING_PRAYER in h.hour:
        s = SectionHeader(title="Canticle of Mary")
        story = psalm_split_correctly(s, story)
    elif h.hour == Breviary.NIGHT_PRAYER:
        s = SectionHeader(title="Canticle of Simeon")
        story = psalm_split_correctly(s, story)

    if h.canticle_ant:
        a = Antiphon(antiphon=h.canticle_ant)
    else:
        a = Instruction(string="Antiphon, as in the Proper of Seasons")
    story = psalm_split_correctly(a, story)

    i = Intercessions(intercessions=h.intercessions)
    story = psalm_split_correctly(i, story)
    if h.prayer:
        p = Prayer(prayers=h.prayer)
    else:
        p = Instruction(string="Prayer, as in the Proper of Seasons")
    story = psalm_split_correctly(p, story)
    return story

def build_oor(h, story):
    # Header
    box = DayHeader(date=h.day, title="Week " + h.week_roman)
    story = psalm_split_correctly(box, story)

    hour = HourHeader(hour=h.hour)
    story=psalm_split_correctly(hour,story)

    #Invitatory
    a = Invitatory(antiphon=h.invitatory)
    story = psalm_split_correctly(a, story)

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

    if h.reading:
        r = Reading(reading=h.reading)
        psalm_split_correctly(r, story)
    if h.response:
        r = Responsory(responses=h.response)
        psalm_split_correctly(r, story)
    if h.prayer:
        p = Prayer(prayers=h.prayer)
        story = psalm_split_correctly(p, story)
    return story
def build_hour(h,story):
    if Breviary.MORNING_PRAYER in h.hour or Breviary.EVENING_PRAYER in h.hour:
        return build_mp_ep(h,story=story)
    elif Breviary.OFFICE_OF_READINGS in h.hour:
        return build_oor(h,story=story)
def build_story():
    story = []
    rows = fetch_rows()
    print("ROWS:",rows)
    for r in rows:
        h = process_row(r)
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

    # normal frame as for SimpleFlowDocument
    frame_t = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    from PsalterTemplate import PsalterTemplate
    page_template = PsalterTemplate(id='OneCol', frames = frame_t)
    doc.addPageTemplates([page_template])
    doc.build(story, canvasmaker=NumberedCanvas)


def psalm_split_correctly(psalm, story):
    # accepts a Psalm (obj) and a Story (obj) and adds paragraph-wise to keep stanzas together

    for stanza in psalm.paragraphs:

        story.append(stanza[2])

    return story


class NumberedCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for i, state in enumerate(self._saved_page_states):  # counting pages with i
            self.__dict__.update(state)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)




if __name__ == "__main__":
    main()
