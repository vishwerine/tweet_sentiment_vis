from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.lib import colors
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker


class MyLineChartDrawing(Drawing):
    def __init__(self, width=600, height=400, *args, **kw):
        apply(Drawing.__init__,(self,width,height)+args,kw)
        self.add(LinePlot(), name='chart')

        self.add(String(200,180,'Hello World'), name='title')

        #set any shapes, fonts, colors you want here.  We'll just
        #set a title font and place the chart within the drawing.
        #pick colors for all the lines, do as many as you need
        self.chart.x = 20
        self.chart.y = 30
        self.chart.width = self.width - 100
        self.chart.height = self.height - 75
        self.chart.lines[0].strokeColor = colors.blue
        self.chart.lines[1].strokeColor = colors.green
        self.chart.lines[2].strokeColor = colors.yellow
        self.chart.lines[3].strokeColor = colors.red
        self.chart.lines[4].strokeColor = colors.black
        self.chart.lines[5].strokeColor = colors.orange
        self.chart.lines[6].strokeColor = colors.cyan
        self.chart.lines[7].strokeColor = colors.magenta
        self.chart.lines[8].strokeColor = colors.brown
	
        self.chart.fillColor = colors.white
        self.title.fontName = 'Times-Roman'
        self.title.fontSize = 18
        self.chart.data = [((0, 50), (100,100), (200,200), (250,210), (300,300), (400,500))]
        self.chart.xValueAxis.labels.fontSize = 12
        self.chart.xValueAxis.forceZero = 0
        self.chart.xValueAxis.gridEnd = 115
        self.chart.xValueAxis.tickDown = 3
        self.chart.xValueAxis.visibleGrid = 1
        self.chart.yValueAxis.tickLeft = 3
        self.chart.yValueAxis.labels.fontName = 'Times-Roman'
        self.chart.yValueAxis.labels.fontSize = 12
        self.title.x = self.width/2
        self.title.y = 0
        self.title.textAnchor ='middle'
        self.add(Legend(),name='Legend')
        self.Legend.fontName = 'Times-Roman'
        self.Legend.fontSize = 12
        self.Legend.x = self.width
        self.Legend.y = 85
        self.Legend.dxTextSpace = 5
        self.Legend.dy = 5
        self.Legend.dx = 5
        self.Legend.deltay = 5
        self.Legend.alignment ='right'
        self.add(Label(),name='XLabel')
        self.XLabel.fontName = 'Times-Roman'
        self.XLabel.fontSize = 12
        self.XLabel.x = 85
        self.XLabel.y = 5
        self.XLabel.textAnchor ='middle'
        #self.XLabel.height = 20
        self.XLabel._text = ""
        self.add(Label(),name='YLabel')
        self.YLabel.fontName = 'Times-Roman'
        self.YLabel.fontSize = 12
        self.YLabel.x = 2
        self.YLabel.y = 80
        self.YLabel.angle = 90
        self.YLabel.textAnchor ='middle'
        self.YLabel._text = ""
        self.chart.yValueAxis.forceZero = 1
        self.chart.xValueAxis.forceZero = 1
 

from reportlab.lib.pagesizes import cm, inch  
from reportlab.graphics.charts.piecharts import Pie  
from reportlab.graphics.charts.legends import Legend  
from reportlab.lib.colors import Color, PCMYKColor  
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin  
  
class MyPieChart(_DrawingEditorMixin,Drawing):  
    def __init__(self,width=400,height=200,*args,**kw):  
        apply(Drawing.__init__,(self,width,height)+args,kw)  
        self._add(self,Pie(),name='chart',validate=None,desc=None)  
        self.chart.x                    = 20  
        self.chart.y                    = (self.height-self.chart.height)/2  
        self.chart.slices.strokeWidth   = 1  
        self.chart.slices.popout        = 1  
        self.chart.direction            = 'clockwise'  
        self.chart.width                = self.chart.height  
        self.chart.startAngle           = 90  
        self.chart.slices[0].popout     = 10  
        self._add(self,Legend(),name='legend',validate=None,desc=None)  
        self.legend.x                   = width - 20  
        self.legend.y                   = 0  
        self.legend.boxAnchor           = 'se'  
        self.legend.subCols[1].align    = 'right'  
        # these data can be read from external sources  
        data                = (9, 7, 6, 4, 2.5, 1.0)  
        categories          = ('A','B','C','D','E','F',)  
        colors              = [PCMYKColor(0,0,0,x) for x in (100,80,60,40,20,5)]  
        self.chart.data     = data  
        self.chart.labels   = map(str, self.chart.data)  
        self.legend.colorNamePairs = zip(colors, categories)  
        for i, color in enumerate(colors): self.chart.slices[i].fillColor  = color  
  


