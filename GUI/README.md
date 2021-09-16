Dependencies
cycler==0.10.0
future==0.18.2
iso8601==0.1.12
kiwisolver==1.1.0
matplotlib==3.2.0
numpy==1.18.1
pyparsing==2.4.6
PyQt5==5.14.1
PyQt5-sip==12.7.1
pyqtgraph==0.10.0
python-dateutil==2.8.1
PyYAML==5.3
qtgui==0.0.1
serial==0.0.97
six==1.14.0

Widget Choices & Reasoning
1. Window : MainWindow
2. Sensor tabs: QTabWidget
- Fits nicely accordingly to the Figma design
- Alternative QStackWidget did not work because it does not allow multiple widgets appear on the same stack, thus not able to layout widgets as shown in the design
3. Window Layout : QSplitter
- QSplitter splits the main window into different sections and allows layout embedding within the sections
- Alternative QLayout does not allow embedding of the sensor tabs
4. Plotting Graph : PlotWidget
- Embedded in the layouts of sensor tabs (on the left)
- Currently displaying data from dummy arrays
- But, can extract sample data from a txt file of the same file directory instead by replacing `second` and `temperature` with `xs` and `ys`
