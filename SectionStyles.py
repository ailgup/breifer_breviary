from reportlab.lib.colors import Color, black
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable, \
    CondPageBreak, HRFlowable, Table, Spacer, KeepTogether
from Hour import *

MAGNIFICAT_RED = Color(214 / 255, 50 / 255, 84 / 255, alpha=1)

HEADER_WIDTH = 90 * mm

POINT_TO_MM = 0.3527




def resize_date_to_fit(text, font, font_size, width=HEADER_WIDTH, percentage_margin=0.75):
    while stringWidth(text, font, font_size) > width * percentage_margin:
        font_size = font_size - 1

    return font_size

# FORMATTING
DATE_FONT_SIZE = 13
LEVEL_FONT_SIZE = 8
TITLE_FONT_SIZE = 8

class BreviarySection(Flowable):
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = []

    def draw(self):
        """
        Draw the shape, text, etc
        """
        current_y = self.y + self.height

        for i in range(len(self.paragraphs)):
            self.paragraphs[i][2].drawOn(self.canv, self.x, current_y - self.paragraphs[i][1])
            current_y = current_y - self.paragraphs[i][1]


class DayHeader(BreviarySection):
    """
    Draw a header thing for the day with option for (Solem, Feast, Mem, Opt. Mem)
    
    ----                                        ----
    |                MARCH 19 (Date)                |
    |               SOLEMNITY  (Level)              |
    ----            St. Joseph  (Title)          ----
    
    """

    # ----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, date="", title="", level=""):
        Flowable.__init__(self)
        self.date_font_size = DATE_FONT_SIZE
        self.level_font_size = LEVEL_FONT_SIZE
        self.title_font_size = TITLE_FONT_SIZE

        self.TOP_MARGIN = 5
        self.BOTTOM_MARGIN = 2

        self.x = x
        self.y = y - self.BOTTOM_MARGIN#add offset to shift down some
        self.width = width
        self.date = date
        self.title = title
        self.level = level
        self.paragraphs = []

        if not height:
            self.height = self.calc_height()

        self.build_table()
    # ----------------------------------------------------------------------

    def calc_height(self):

        MARGIN_PERCENTALE = 1.5

        total_height = (bool(self.date) * self.date_font_size + bool(self.title) * self.title_font_size + bool(
            self.level) * self.level_font_size)
        total_height += self.TOP_MARGIN
        total_height += self.BOTTOM_MARGIN
        total_height = MARGIN_PERCENTALE * total_height
        return total_height

    def build_table(self):

        from reportlab.platypus import Paragraph, TableStyle
        from reportlab.lib.styles import ParagraphStyle, TA_CENTER
        date_para = Paragraph(self.date,
                          ParagraphStyle(name='Date', alignment=TA_CENTER,fontName='Minion', leading=13, textColor=MAGNIFICAT_RED, fontSize=13))
        if self.level:
            level_para = Paragraph(self.level,
                                  ParagraphStyle(name='Level', alignment=TA_CENTER,fontName='Minion', leading=8, textColor=MAGNIFICAT_RED,
                                                 fontSize=8))
        else:
            level_para=None
        title_para = Paragraph(self.title,
                              ParagraphStyle(name='Title', alignment=TA_CENTER,fontName='Minion', leading=8, textColor=black,
                                             fontSize=8))
        line_style = [('LINEABOVE',(0,0),(0,0),1,black,'butt'),('LINEABOVE',(2,0),(2,0),1,black,'butt'),
                      ('LINEBELOW',(0,4),(0,4),1,black,'butt'),('LINEBELOW',(2,4),(2,4),1,black,'butt'),
                      ('LINEBEFORE',(0,1),(0,3),3,black,'projecting'),('LINEAFTER',(2,1),(2,3),3,black,'projecting')]
        table_style = TableStyle([('BOTTOMPADDING',(0,0),(-1,-1),0),
                                  ('TOPPADDING',(0,0),(-1,-1),0)])

        row_heights = []
        row_heights.append(1)
        if self.date:
            row_heights.append(None)
        else:
            row_heights.append(0)
            print("No l")
        if self.level:
            row_heights.append(None)
        else:
            row_heights.append(0)
            print("No t")
        if self.title:
            row_heights.append(None)
        else:
            row_heights.append(0)
            print("No d")
        row_heights.append(1)

        t=Table([["","",""],["",date_para,""],["",level_para,""],["",title_para,""],["","",""]],colWidths=[5*mm,HEADER_WIDTH-10*mm,5*mm],rowHeights=row_heights, style = line_style, spaceBefore=self.TOP_MARGIN, spaceAfter=self.BOTTOM_MARGIN)


        t.setStyle(table_style)

        (w,h) = t.wrap(HEADER_WIDTH,99999)
        self.height = h
        self.paragraphs.append((w,h,KeepTogether(t)))

    # def draw(self):
    #     """
    #     Draw the shape, text, etc
    #     """
    #     # TODO resize font if too wide
    #     self.date_font_size = resize_date_to_fit(self.date, DATE_FONT, self.date_font_size)
    #
    #     # resize date if it is too long for container
    #
    #     bracket_width = 5 * mm
    #
    #     self.canv.setLineWidth(3)
    #
    #     offset = 0.5  # needed to square up corners
    #     # vertical members
    #     self.canv.line(self.x, self.y - offset, self.x, self.y + self.height + offset)
    #     self.canv.line(self.x + self.width, self.y - offset, self.x + self.width, self.y + self.height + offset)
    #
    #     self.canv.setLineWidth(1)
    #     # left horizontal
    #     self.canv.line(self.x, self.y, self.x + bracket_width, self.y)
    #     self.canv.line(self.x, self.y + self.height, self.x + bracket_width, self.y + self.height)
    #
    #     # right horizontal
    #     self.canv.line(self.x + self.width, self.y, self.x + self.width - bracket_width, self.y)
    #     self.canv.line(self.x + self.width, self.y + self.height, self.x + self.width - bracket_width,
    #                    self.y + self.height)
    #
    #     # DATE STYLE
    #     self.canv.setFont(DATE_FONT, self.date_font_size)
    #     self.canv.setFillColor(DATE_FONT_COLOR)
    #
    #     self.canv.drawCentredString(self.width / 2, self.y + self.height - self.date_font_size, self.date.upper())
    #
    #     # LEVEL STYLE
    #     self.canv.setFont(LEVEL_FONT, self.level_font_size)
    #     self.canv.setFillColor(LEVEL_FONT_COLOR)
    #     level_y_pos = self.y + (self.height / 2) - LEVEL_FONT_SIZE * POINT_TO_MM
    #     print("H:",self.height,"  Y:",self.y," Lin:",level_y_pos)
    #     self.canv.line(self.x, self.y+self.TOP_MARGIN+self.height, self.width, self.y+self.height+self.TOP_MARGIN)
    #     self.canv.line(self.x, self.y-self.BOTTOM_MARGIN, self.width, self.y-self.BOTTOM_MARGIN)
    #
    #     if (self.level == "S"):
    #         self.canv.drawCentredString(self.width / 2, level_y_pos, "SOLEMNITY")
    #     elif self.level == "F":
    #         self.canv.drawCentredString(self.width / 2, level_y_pos, "FEAST")
    #     elif self.level == "M":
    #         self.canv.drawCentredString(self.width / 2, level_y_pos, "MEMORIAL")
    #     elif self.level == "m":
    #         self.canv.drawCentredString(self.width / 2, level_y_pos, "OPTIONAL MEMORIAL")
    #
    #     # TITLE STYLE
    #     self.canv.setFont("MinionSub", 8)
    #     self.canv.setFillColor(black)
    #     self.canv.drawCentredString(self.width / 2, self.y + self.title_font_size, self.title)


HOUR_FONT = "MinionSub_bold"
HOUR_FONT_SIZE = 10
HOUR_FONT_COLOR = MAGNIFICAT_RED


def resize_font_to_fit(text, font, font_size, width=HEADER_WIDTH, percentage_margin=0.75):
    while stringWidth(text, font, font_size) > width * percentage_margin:
        font_size = font_size - 1

    return font_size


class HourHeader(BreviarySection):
    """
    Draw a header for the hour, center bolded, red text
    
                                            
    |                                               |
    |              Evening Prayer II                |
    
    
    """

    # ----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, hour=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.hour = hour
        self.hour_font_size = resize_font_to_fit(self.hour, HOUR_FONT, HOUR_FONT_SIZE, self.width)

        if not height:
            self.height = self.calc_height()
        else:
            self.height = height

    # ----------------------------------------------------------------------

    def calc_height(self):
        POINT_TO_MM = 1
        MARGIN_PERCENTALE = 2

        total_height = (bool(self.hour) * self.hour_font_size)
        total_height = POINT_TO_MM * total_height
        total_height = MARGIN_PERCENTALE * total_height
        return total_height

    def draw(self):
        """
        Draw the shape, text, etc
        """

        # DATE STYLE
        self.canv.setFont(HOUR_FONT, self.hour_font_size)
        self.canv.setFillColor(HOUR_FONT_COLOR)

        self.canv.drawCentredString(self.width / 2, self.y + self.height - self.hour_font_size, self.hour)


class Hymn(BreviarySection):
    """
    Hymn


    """

    # ----------------------------------------------------------------------
    def __init__(self, hymns:Breviary.Hymn, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        self.hymns = hymns

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []

        s = SectionHeader(title="Hymn")
        for p in s.paragraphs:
            paragraphs.append(p)
        self.height = self.height + s.height
        for h in self.hymns:
            if h["saint_michaels_num"]:
                st_m_string = " { #"+h["saint_michaels_num"]+"} "
            antiphon_string = "<para><b> " + h["name"] + "</b><font color='#D63254'> ( #" + h["number"] + ")"+st_m_string+"</font></para>"
            P = Paragraph(antiphon_string,
                          ParagraphStyle(name='Psalm', fontName='Minion', leading=9, textColor=black, fontSize=8))

            w, h = P.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraphs.append((w, h, P))

        S = Spacer(HEADER_WIDTH, 5)
        w, h = S.wrap(HEADER_WIDTH, 99999)
        paragraphs.append((w, h, S))
        self.height += h
        return paragraphs
class Antiphon(BreviarySection):
    """
    antiphon(s) for the psalms, for multiple, pass a list of tuples
        eg. [("Easter","Alleluia, He is Risen"),("Lent","Let us take up our cross")...]
    
    
    """

    # ----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, antiphon="", number=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        self.multiple_antiphons = len(antiphon) > 1

        self.antiphon = antiphon

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []
        for a in self.antiphon:

            if self.antiphon.index(a) == 0:
                antiphon_string = "<para><font color='#D63254'>" + a["title"] + '</font> ' + a["ant"] + "</para>"
                P = Paragraph(antiphon_string,
                              ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=black, fontSize=8))

            else:
                antiphon_string = "<para leftIndent='15' firstLineIndent='-5'> <font color='#D63254'>" + a[
                    "title"] + "</font> " + a["ant"] + "</para>"
                P = Paragraph(antiphon_string,
                              ParagraphStyle(name='Psalm', fontName='Minion', leading=7, textColor=black, fontSize=6))

            w, h = P.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraphs.append((0, 0, CondPageBreak(h)))  # keep each individual antiphon on one page
            paragraphs.append((w, h, P))

        S = Spacer(HEADER_WIDTH, 5)
        w, h = S.wrap(HEADER_WIDTH, 99999)
        paragraphs.append((w, h, S))
        self.height += h
        return paragraphs


class Psalm(BreviarySection):
    """
    psalm
    Psalm(verse = "Psalm 119:105-112", 
                                 titles = ["XIV (Nun)","A Meditation on God's Law"], 
                                 summary="This is my commandment: that you should love one another", 
                                 summary_verse = "(John 15:12)", 
                                 text
    
    """

    # ----------------------------------------------------------------------

    BREAK_STRING = "<br /> "

    def __init__(self, psalm: Breviary.Psalm, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        # PSALM {"titles": [], "verse": "", "summary": "", "summary_verse": "", "text": ""}
        self.verse = psalm["verse"]

        self.titles = psalm["titles"]
        self.summary = psalm["summary"]
        self.summary_verse = psalm["summary_verse"]
        self.text = psalm["text"]

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle
        paragraphs = []

        # title
        psalm_string = "<para align='center'><b>" + self.verse + "</b></para>"
        P = Paragraph(psalm_string,
                      ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED, fontSize=9))
        P.keepWithNext = True
        psalm_width = HEADER_WIDTH
        w, h = P.wrap(HEADER_WIDTH, 99999)
        self.height = self.height + h
        paragraphs.append((w, h, P))

        psalm_string = "<para align='center'>"
        for t in self.titles:
            psalm_string += t + " -  "
        psalm_string = psalm_string[:-3]  # remove trailing dash
        psalm_string += "</para>"
        P = Paragraph(psalm_string,
                      ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED, fontSize=8))
        P.keepWithNext = True
        psalm_width = HEADER_WIDTH
        w, h = P.wrap(HEADER_WIDTH, 99999)
        self.height = self.height + h
        paragraphs.append((w, h, P))

        # summary string
        # psalm_string = "<para align=right fontsize=6><i>" + self.summary + "</i>" + "  " + self.summary_verse + Psalm.BREAK_STRING+ "</para>"
        # P = Paragraph(psalm_string, PSALM_PARA_STYLE)
        # P.keepWithNext = True  # does not always keep together if near end of page
        # w, h = P.wrap(HEADER_WIDTH, 99999)
        # self.height = self.height + h
        # paragraphs.append((w, h, P))

        # psalm itself
        psalm_stanzas = self.text.split(Psalm.BREAK_STRING + Psalm.BREAK_STRING)
        paragraph_staging = []
        for stanza in psalm_stanzas:
            psalm_string = "<para>" + stanza + Psalm.BREAK_STRING + Psalm.BREAK_STRING + "</para>"
            P = Paragraph(psalm_string,
                          ParagraphStyle(name='Psalm', fontName='Minion_med', leading=8, textColor=black, fontSize=8))
            psalm_width = HEADER_WIDTH
            w, h = P.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraph_staging.append((w, h, P))
        for p in paragraph_staging:
            stanza_height = 0

            stanza_height = p[1]
            paragraphs.append((0, 0, CondPageBreak(stanza_height)))
            paragraphs.append(p)

        return paragraphs


class Reading(BreviarySection):
    """
    Reading                   Gen 1:1
    ---------------------------------
        In the begining....
    
    """

    # ----------------------------------------------------------------------
    def __init__(self, reading=Breviary.Reading, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        self.verse = reading["verse"]
        self.text = reading["text"]

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):
        from reportlab.platypus import Paragraph, TableStyle

        from reportlab.lib.styles import ParagraphStyle

        LINE_BREAK = "<br />"
        paragraphs = []

        # title
        title_1 = "<para><b>READING</b></para>"
        title_2 = "<para align=right>" + self.verse + "</para>"

        P1 = Paragraph(title_1, ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED,
                                               fontSize=10))
        P2 = Paragraph(title_2,
                       ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=MAGNIFICAT_RED, fontSize=8))

        psalm_width = HEADER_WIDTH
        w, h = P1.wrap(HEADER_WIDTH, 99999)
        w, h = P2.wrap(HEADER_WIDTH, 99999)

        T = Table([[P1, P2]])
        T.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))

        w, h = T.wrap(HEADER_WIDTH, 999999)
        self.height = self.height + h

        paragraphs.append((w, h, T))

        # horozontal line

        line = HRFlowable(
            color=MAGNIFICAT_RED,
            thickness=1,
            width=HEADER_WIDTH,
            spaceBefore=1,
            spaceAfter=0
        )
        w, h = line.wrap(HEADER_WIDTH, 999999)
        self.height = self.height + h

        paragraphs.append((self.width, 3, line))
        # ensure all <br/> are space-less otherwise we could split one inadvertantly
        self.text = self.text.replace("<br />", LINE_BREAK)

        # dropcap
        reading_string = self.text[0]
        reading_string = "<para align=right>" + reading_string + "</para>"
        P = Paragraph(reading_string,
                      ParagraphStyle(name='Psalm', fontName='Minion', leading=20, textColor=MAGNIFICAT_RED,
                                     fontSize=20))
        w, h = P.wrap(HEADER_WIDTH, 99999)

        # first two lines
        table_width = HEADER_WIDTH / 2 - 1
        FONT_SIZE = 8
        para_height = 0
        word_number = 1
        P2 = None
        substring = ""
        # create two line paragraph
        # TODO this fails if split occours on a style tag ;-(, also this code is a mess
        import re
        # as per recommendation from @freylis, compile once only
        CLEANR = re.compile('<.*?>')

        text_without_tags = re.sub(CLEANR, '', self.text[1:-1])
        split_substring = text_without_tags.rsplit(' ')
        # add words to paragraph until it takes up 3 lines then remove one
        while para_height <= (FONT_SIZE) * 2:

            substring = " ".join(split_substring[:word_number])
            reading_string = "<para align=left>" + substring + "</para>"

            P2 = Paragraph(reading_string, ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black,
                                                          fontSize=FONT_SIZE))
            w, h = P2.wrap(table_width, 99999)
            para_height = h

            if para_height > (FONT_SIZE) * 2:  # we have now gone over need to back up one
                substring = " ".join(split_substring[:word_number - 1])
                reading_string = "<para align=left>" + substring + "</para>"

                P2 = Paragraph(reading_string,
                               ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black,
                                              fontSize=FONT_SIZE))
            word_number += 1

        # remainder
        text_remainder = self.text[len(substring) + 1:-1]
        text_remainder = text_remainder.replace(LINE_BREAK, LINE_BREAK + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        reading_string = "<para align=left >" + text_remainder + "</para>"


        T2 = Table([[P, P2]])
        # T=Table([["1","2"],["3","4"]])
        T2.setStyle(TableStyle([('SPAN', (0, 1), (1, 1)),
                                # ('GRID', (0, 0), (-1, -1), 0.25, black),
                                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                ('RIGHTPADDING', (0, 0), (0, 0), 3),
                                ('TOPPADDING', (0, 0), (-1, -1), 0),
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                                ('BOTTOMPADDING', (0, 1), (1, 1), 5)]))


        w, h = T2.wrap(HEADER_WIDTH, 999999)
        self.height += h
        paragraphs.append((w, h, T2))

        P3 = Paragraph(reading_string,
                       ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black, fontSize=FONT_SIZE))

        w, h = P3.wrap(HEADER_WIDTH, 162*mm)
        self.height += h
        paragraphs.append((w, h, P3))

        return paragraphs


class Intercessions(BreviarySection):
    """
    Reading                   Gen 1:1
    ---------------------------------
        In the begining....
    
    """

    # ----------------------------------------------------------------------
    def __init__(self, intercessions: Breviary.Intercessions, x=0, y=0, width=HEADER_WIDTH, height=None, ):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        self.first = intercessions["first"]
        self.response = intercessions["response"]
        self.intercessions = intercessions["intercessions"]
        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):

        from reportlab.platypus import Paragraph, Spacer

        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []

        # title
        # title_1 = "<para><b><i>Intercessions</i></b></para>"
        # P1 = Paragraph(title_1, ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED,
        #                                       fontSize=10))
        # w, h = P1.wrap(HEADER_WIDTH, 99999)
        # self.height = self.height + h
        # paragraphs.append((w, h, P1))
        s = SectionHeader(title="Intercessions")
        for p in s.paragraphs:
            paragraphs.append(p)
        self.height = self.height + s.height

        # first
        title_1 = "<para leftIndent='5' firstLineIndent='-5'>" + self.first + "</para>"
        P1 = Paragraph(title_1,
                       ParagraphStyle(name='Psalm', fontName='Minion_med', leading=8, textColor=black, fontSize=8))
        w, h = P1.wrap(HEADER_WIDTH, 99999)
        self.height = self.height + h
        paragraphs.append((w, h, P1))

        # resp
        title_1 = "<para leftIndent='15' firstLineIndent='-5'><i>" + self.response + "</i></para>"
        P1 = Paragraph(title_1, ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black, fontSize=8))
        w, h = P1.wrap(HEADER_WIDTH, 99999)
        self.height = self.height + h
        paragraphs.append((w, h, P1))

        S = Spacer(HEADER_WIDTH, 2)
        w, h = S.wrap(HEADER_WIDTH, 99999)
        paragraphs.append((w, h, S))
        self.height += h

        for i in self.intercessions:
            title_1 = "<para leftIndent='5' firstLineIndent='-5'>" + i[
                'verse'] + "<br /><font color='#D63254'> - </font>" + \
                      i['response'] + "</para>"
            P1 = Paragraph(title_1,
                           ParagraphStyle(name='Psalm', fontName='Minion_med', leading=8, textColor=black, fontSize=8))
            w, h = P1.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraphs.append((w, h, P1))

            S = Spacer(HEADER_WIDTH, 2)
            w, h = S.wrap(HEADER_WIDTH, 99999)
            paragraphs.append((w, h, S))
            self.height += h

        S = Spacer(HEADER_WIDTH, 5)
        w, h = S.wrap(HEADER_WIDTH, 99999)
        paragraphs.append((w, h, S))
        self.height += h

        return paragraphs


class Responsory(BreviarySection):
    """



    """

    # ----------------------------------------------------------------------
    def __init__(self, responses: Breviary.Response, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        self.responses = responses

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):

        from reportlab.platypus import Paragraph, Spacer

        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []

        # title
        # title_1 = "<para><b><i>Intercessions</i></b></para>"
        # P1 = Paragraph(title_1, ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED,
        #                                       fontSize=10))
        # w, h = P1.wrap(HEADER_WIDTH, 99999)
        # self.height = self.height + h
        # paragraphs.append((w, h, P1))
        s = SectionHeader(title="Responsory")
        for p in s.paragraphs:
            paragraphs.append(p)
        self.height = self.height + s.height

        for i in self.responses:
            title_1 = "<para leftIndent='5' firstLineIndent='-5'>" + i["verse"] + "</para>"
            P1 = Paragraph(title_1,
                           ParagraphStyle(name='Psalm', fontName='Minion_med', leading=8, textColor=black, fontSize=8))
            w, h = P1.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraphs.append((w, h, P1))

            # resp
            title_1 = "<para leftIndent='15' firstLineIndent='-5'><font color='#D63254'> - </font>" + i[
                "response"] + "</para>"
            P1 = Paragraph(title_1,
                           ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black, fontSize=8))
            w, h = P1.wrap(HEADER_WIDTH, 99999)
            self.height = self.height + h
            paragraphs.append((w, h, P1))

            S = Spacer(HEADER_WIDTH, 2)
            w, h = S.wrap(HEADER_WIDTH, 99999)
            paragraphs.append((w, h, S))
            self.height += h

        return paragraphs


# section header eg. Psalmody, Intercessions, Canticle of Mary, etc
class SectionHeader(BreviarySection):
    """
    Intercessions...

    """

    # ----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=HEADER_WIDTH, height=None, title=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.title = title

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):

        from reportlab.platypus import Paragraph, Spacer

        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
        paragraphs = []

        # title
        title_1 = "<para><b><i>" + self.title + "</i></b></para>"
        P1 = Paragraph(title_1, ParagraphStyle(name='Psalm', fontName='Minion', leading=10, textColor=MAGNIFICAT_RED,
                                               fontSize=10, alignment=TA_RIGHT))
        w, h = P1.wrap(HEADER_WIDTH, 99999)
        self.height = self.height + h
        paragraphs.append((w, h, P1))

        S = Spacer(HEADER_WIDTH, 5)
        w, h = S.wrap(HEADER_WIDTH, 99999)
        paragraphs.append((w, h, S))
        self.height += h

        return paragraphs


class Prayer(BreviarySection):
    """
    Closing Prayer, allows for up to two

    """

    # ----------------------------------------------------------------------
    def __init__(self, prayers: list, x=0, y=0, width=HEADER_WIDTH, height=None):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width

        if not prayers:
            self.prayers = []
        else:
            self.prayers = prayers

        if not height:
            self.height = 0
        else:
            self.height = height

        self.paragraphs = self.build_paragraphs()

    def build_paragraphs(self):
        from reportlab.platypus import Paragraph, TableStyle

        from reportlab.lib.styles import ParagraphStyle

        paragraphs = []

        # title
        s = SectionHeader(title="Prayer")
        for p in s.paragraphs:
            paragraphs.append(p)
        self.height = self.height + s.height

        temp_para = []
        for p in self.prayers:
            reading_string = "<para align=left >" + p + "</para>"
            para = Paragraph(reading_string, ParagraphStyle(name='Psalm', fontName='Minion', leading=8, textColor=black,
                                                            fontSize=8))
            temp_para.append(para)

        T = Table([temp_para])
        T.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))

        w, h = T.wrap(HEADER_WIDTH, 999999)
        self.height = self.height + h
        paragraphs.append((w, h, T))

        return paragraphs
