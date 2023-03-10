# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QGridLayout, QWidget,QToolTip,QGraphicsLineItem
from PySide6.QtCore import QPointF
from PySide6.QtGui import QColor, QPen,QPainter,QCursor,QBrush
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QSplineSeries

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QChart {{
	border: none;
    color: {_color};
	background-color: {_bg_color};
}}
QLineSeries {{
    border: none;
    color: {_color};
    background-color: {_bg_color};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyLineChart(QWidget):
    def __init__(
        self, 
        color= "#343b48",
        bg_color = "#343b48",
        line_color = "#cd1234",
        data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ],
        seriesNames = []
    ):
        super().__init__()
        self.chart = QChart()
        self._data = data
        self._seriesNames = seriesNames
        self.series = QSplineSeries()
        self.lineItem = QGraphicsLineItem(self.chart)
        self.lineItem.setZValue(998)
        self.lineItem.hide()
        
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        # Create chart view with the chart
        self.chart_view = QChartView(self.chart, self)
        
        self.series.setColor(QColor(line_color))
        self.main_layout.addWidget(self.chart_view, 0, 1, 3, 1)
        self.setLayout(self.main_layout)


        self.chart_view.setRenderHint(QPainter.Antialiasing)  
        self.initChart(line_color)
        

        # SET STYLESHEET
        self.set_stylesheet(
            color,
            bg_color,
        )



    def mouseMoveEvent(self, event):
        super(QChartView, self).mouseMoveEvent(event)
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(event.pos()).x()
        y = self._chart.mapToValue(event.pos()).y()
        index = round((x - self.min_x) / self.step_x)
        pos_x = self._chart.mapToPosition(
            QPointF(index * self.step_x + self.min_x, self.min_y))
            #self.lineItem.setLine(pos_x.x(), self.point_top.y(),
            #                      pos_x.x(), self.point_bottom.y())
        self.lineItem.show()
    def onSeriesHoverd(self, point, state):
        if state:
            try:
                name = self.sender().name()
            except:
                name = ""
            QToolTip.showText( QCursor.pos() , "%s\nx: %s\ny: %s" % (name, round(point.x()),round( point.y())))

    def initChart(self,line_color):
        self.chart = QChart(title="Line Chart")
        self.chart.setAcceptHoverEvents(True)
        dataTable = self._data
        for i, data_list in enumerate(dataTable):
            series = QLineSeries(self.chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName(self._seriesNames[i])
            series.setPointsVisible(True)  # 显示原点
            series.hovered.connect(self.onSeriesHoverd)
            self.chart.addSeries(series)

        brush = QBrush(QColor(line_color))
        pen = QPen(brush,2)
        pen.setWidth(3);
        series.setPen(pen);

        self.chart.createDefaultAxes()  

        
        self.chart.axisX().setTickCount(13)  
        self.chart.axisY().setTickCount(8) 
        
        #self.chart.axisY().setLinePenColor(series.pen().color()); #extrct the same color as the main lineChart
        self.chart.axisY().setLinePenColor(line_color)
        z = 0
        for i in self._data:
            if z <= max(i):
                z = max(i)
             
        self.chart.axisY().setRange(0, z + ( (20 * z) / 100) ) #add 20% on the biggets item in data 

        self.chart_view.setChart(self.chart)
        self.chart_view.setContentsMargins(0,0,0,0)
        self.chart_view.setStyleSheet("background-color: transparent;\n")
        self.chart.setBackgroundBrush(QBrush(QColor("transparent")))
        


    # SET STYLESHEET
    def set_stylesheet(
        self,
        color,
        bg_color,
    ):
        # APPLY STYLESHEET
        style_format = style.format(    
            _color = color,
            _bg_color = bg_color,
        )
        self.setStyleSheet(style_format)


    
