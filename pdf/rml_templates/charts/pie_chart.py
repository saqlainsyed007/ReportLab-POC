# Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.piecharts import Pie


class PieChart(_DrawingEditorMixin, Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # Width and height of chart.
        self.width = 772
        self.height = 280
        # Add title
        self._add(self, Label(), name='title', validate=None, desc=None)
        self.title._text = 'Simple Pie Chart'
        self.title.fontSize = 24
        # Position Title
        self.title.x = 386
        self.title.y = 240
        # Add Bar chart to the Drawing.
        self._add(self, Pie(), name="chart", validate=None, desc=None)
        # Bar Chart Dimensions
        self.chart.width = 150
        self.chart.height = 150
        # Bar Chart Position
        self.chart.x = (self.width - self.chart.width) / 2
        self.chart.y = 20
        # Data will be sent from RML. However, defaults can be initialized here.
        self.chart.data = []
        # Sector Labels. Data will be sent from RML. However, defaults can be initialized here.
        self.chart.labels = []
        # Start angle for Pie Chart. 90 indicates 12'o Clock position.
        self.chart.startAngle = 90
        # Pie Chart direction.
        self.chart.direction = 'clockwise'


if __name__ == "__main__":  # NORUNTESTS
    PieChart().save(formats=['pdf'], outDir='.', fnRoot=None)