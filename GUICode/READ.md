Widget Choices & Reasoning
1. Window : MainWindow
2. Sensor tabs: QTabWidget
- Fits nicely accordingly to the Figma design
- Alternative QStackWidget did not work because it does not allow multiple widgets appear on the same stack, thus not able to layout widgets as shown in the design
3. Window Layout : QSplitter
- QSplitter splits the main window into different sections and allows layout embedding within the sections
- Alternative QLayout does not allow embedding of the sensor tabs