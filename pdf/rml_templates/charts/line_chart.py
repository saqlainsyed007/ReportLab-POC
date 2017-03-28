# Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.charts.lineplots import SimpleTimeSeriesPlot
from reportlab.lib.colors import Color


class LineChart(_DrawingEditorMixin, Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # Width and height of chart.
        self.width = 772
        self.height = 280
        # Add title.
        self._add(self, Label(), name='title', validate=None, desc=None)
        self.title._text = 'Sample Bar Chart'
        self.title.fontSize = 24
        self.title.fontName = "Calibri"
        # Position Title.
        self.title.x = 386
        self.title.y = 220
        # Add Line chart to the Drawing.
        self._add(self, SimpleTimeSeriesPlot(), name='chart', validate=None, desc=None)
        # Line Chart Position.
        self.chart.x = 150
        self.chart.y = 20
        # Line Chart Dimensions.
        self.chart.width = 400
        self.chart.height = 150
        # Color the lines.
        self.chart.lines[0].strokeColor = Color(.19, .49, 1, 1)
        self.chart.lines[1].strokeColor = Color(.2, .199, .199, 1)
        # Line thickness
        self.chart.lines.strokeWidth = 1.5
        # Format Labels on X-Axis
        self.chart.xValueAxis.xLabelFormat = '{dd}/{mm}/{yy}'
        # Grid Lines Visible on Graph.
        self.chart.yValueAxis.visibleGrid = 1
        # Format labels on Y-Axis
        self.chart.yValueAxis.labelTextFormat = '%.1f%%'
        # Avoid assuming lowest value as origin
        self.chart.yValueAxis.avoidBoundSpace = (10, 0)
        # Add legends to the graph
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        # Initialize Color vs Desc text
        self.legend.colorNamePairs = [(Color(.19, .49, 1, 1), 'Data1'), (Color(.2, .199, .199, 1), 'Data2')]
        # Position Legend
        self.legend.x = 600
        self.legend.y = 100


if __name__ == "__main__":  # NORUNTESTS
    LineChart().save(formats=['pdf'], outDir='.', fnRoot=None)
