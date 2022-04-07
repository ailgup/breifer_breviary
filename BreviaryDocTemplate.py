from reportlab.platypus import BaseDocTemplate

from CustomFlowables import Table, KeepTogether, Paragraph

from reportlab.lib.units import mm
from reportlab.lib.pagesizes import C6

class BreviaryDocTemplate(BaseDocTemplate):
    def __init__(self, *args, **kwargs):
        BaseDocTemplate.__init__(self, *args, **kwargs)
        self.current_spread_para_ids = []
        self.current_title=""



    def afterPage(self):
        # after an odd page clear
        if not self.page%2:
            # clear because we are onto a new spread
            self.current_spread_para_ids = []


    def afterFlowable(self, flowable):
        try:
            if type(flowable) is Paragraph:
                print("after para")
                self.current_spread_para_ids.append(flowable.getPlainText(identify=1))
        except Exception:
            pass
    def filterFlowables(self,flowables):

        #ensure no duplicate antiphons on the same spread
        #TODO filter only for antiphons b/c other elements could be duplicated correctly
        #print(type(flowables[0]))
        if type(flowables[0]) is Paragraph:
            #print(self.current_spread_para_ids)
            #print(flowables[0].style)

            if flowables[0].getPlainText(identify=1) in self.current_spread_para_ids:
                flowables[0] = None
            try:
                if flowables[0].title == "hour_header":
                    self.current_hour = flowables[0].payload
            except Exception:
                pass
        #find the header info
        elif type(flowables[0]) is KeepTogether:

            try:
                if flowables[0].title == "day_header":
                    self.current_title = flowables[0].payload
            except Exception:
                pass
