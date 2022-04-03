from reportlab.platypus import BaseDocTemplate, Paragraph


class BreviaryDocTemplate(BaseDocTemplate):
    def __init__(self, *args, **kwargs):
        BaseDocTemplate.__init__(self, *args, **kwargs)
        self.current_spread_para_ids = []


    def afterPage(self):
        # after an odd page clear
        if not self.page%2:
            # clear because we are onto a new spread
            self.current_spread_para_ids = []

    def afterFlowable(self, flowable):
        if type(flowable) is Paragraph:
            #print("after para")
            self.current_spread_para_ids.append(flowable.getPlainText(identify=1))
    def filterFlowables(self,flowables):

        #ensure no duplicate antiphons on the same spread
        #TODO filter only for antiphons b/c other elements could be duplicated correctly
        if type(flowables[0]) is Paragraph:
            #print(self.current_spread_para_ids)
            if flowables[0].getPlainText(identify=1) in self.current_spread_para_ids:
                flowables[0] = None


