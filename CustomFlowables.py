from reportlab import platypus


class Table(platypus.Table):
    def __init__(self, *args, **kwargs):
        platypus.Table.__init__(self, *args, **kwargs)
        self.title=""
        self.payload=""

class Paragraph(platypus.Paragraph):
    def __init__(self, *args, **kwargs):
        platypus.Paragraph.__init__(self, *args, **kwargs)
        self.title=""
        self.payload=""
class KeepTogether(platypus.KeepTogether):
    def __init__(self, *args, **kwargs):
        platypus.KeepTogether.__init__(self, *args, **kwargs)
        self.title=""
        self.payload=""
