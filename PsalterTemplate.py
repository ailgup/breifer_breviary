from reportlab.platypus import PageTemplate
from reportlab.lib.colors import Color
from reportlab.lib.units import mm
MAGNIFICAT_RED = Color(214 / 255, 50 / 255, 84 / 255, alpha=1)
class PsalterTemplate(PageTemplate):

    def __init__(self, *args, **kwargs):
        PageTemplate.__init__(self, *args, **kwargs)

    #needed overload as go-between of Flowables and Canvas
    #used to write headers, which need to know what is on the page
    # Flowable attribute -> DocTemplate afterPage() -> afterDrawPage() -> canvas

    def afterDrawPage(self, canv, doc):
        page_num = canv.getPageNumber()
        text = doc.current_title + " - " + doc.current_hour
        self.add_header(canv,text,page_num)

    def add_header(self,canv,text,page):
        # Page Number
        canv.setFont("Minion", 7)
        PAGE_NUMBER_Y_MARGIN = 5 * mm
        PAGE_NUMBER_X_MARGIN = 5 * mm

        # even pages get number on left, odd on right
        x_loc = PAGE_NUMBER_X_MARGIN
        # title = canvas.Canvas.
        print("P:", page, " T:", (text))
        if page % 2:
            x_loc = canv._pagesize[0] - PAGE_NUMBER_X_MARGIN
            canv.drawRightString(x_loc,canv._pagesize[1] - PAGE_NUMBER_Y_MARGIN, "%d" % page)
        else:
            canv.drawString(x_loc,canv._pagesize[1] - PAGE_NUMBER_Y_MARGIN, "%d" % page)

        # Title

        canv.setFont("Minion", 7)
        canv.setFillColor(MAGNIFICAT_RED)
        canv.textTransform = "uppercase"
        PAGE_NUMBER_Y_MARGIN = 5 * mm
        PAGE_NUMBER_X_MARGIN = 15 * mm

        # even pages get number on left, odd on right
        x_loc = PAGE_NUMBER_X_MARGIN
        title = str(text)
        if page % 2:
            x_loc = canv._pagesize[0] - PAGE_NUMBER_X_MARGIN
            canv.drawRightString(x_loc,canv._pagesize[1] - PAGE_NUMBER_Y_MARGIN,
                                 title)
        else:
            canv.drawString(x_loc, canv._pagesize[1] - PAGE_NUMBER_Y_MARGIN,
                            title)