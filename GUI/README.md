Setup:
1. Clone this repo
2. Install the dependencies: python -m pip install -r requirements.txt
    -Python version > 3.5 (3.9 might be unstable)
3. Run the GUI: python hyperloop_gui.py

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
