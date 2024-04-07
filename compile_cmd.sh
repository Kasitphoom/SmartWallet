pyside6-rcc test.qrc -o test_rc.py
#compile the resource file to a python file

pyside6-uic mainwindow.ui -o mainwindow.py
#compile the ui file to a python file

pyside6-uic info.ui -o info.py