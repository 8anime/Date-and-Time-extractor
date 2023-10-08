
import sys
import csv
import logging

from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QPushButton, 
    QTextEdit, 
    QFileDialog, 
    QVBoxLayout, 
)

from extractDates import extractDateFromInput

class DateExtractorApp(QMainWindow):
    """The Date Extractor App is a powerful tool that streamlines the process of extracting dates from a variety of textual sources. 
    It is particularly useful for users who need to quickly and accurately identify dates within text documents or input data without 
    manually searching or parsing the content."""
    def __init__(self):
        super().__init__()

        self.inititializeUserInterface()

    def inititializeUserInterface(self):
        """This method is used to build the user interface of the application"""
        self.setWindowTitle('Date Extractor')  # Set the title for the application
        self.setGeometry(300, 100, 800, 600)   # Determine the width and height of the application and where on the screen it will appear

        # Create widgets
        self.textArea = QTextEdit()      # Provides an area where you can display and edit text
        self.textArea.setReadOnly(True)  # Text can only be read but not edited

        self.btnOpenFile = QPushButton('Open CSV File')               # Button that opens a csv file from the file system
        self.btnExtractDates = QPushButton('Extract Dates and time')  # Button that extacts data from the csv file

        # Determines the arrangement and alignment of the various widgets within the application's main window.
        # It is responsible for organizing the widgets in the main window in a vertical orientation from top to bottom.
        widgetLayout = QVBoxLayout()
        widgetLayout.addWidget(self.btnOpenFile)
        widgetLayout.addWidget(self.btnExtractDates)
        widgetLayout.addWidget(self.textArea)

        container = QWidget()              # Widget that holds other widgets(QVBoxLayout, QPushButton, QTextEdit)
        container.setLayout(widgetLayout)  # Set the layout of the container widget to be in a vertical orientation

        self.setCentralWidget(container)   # Determine what will be displayed in the main content area of the application's window

        # Connect signals to slots
        self.btnOpenFile.clicked.connect(self.openFileDialog)     #  Signal for opening a file from the file system
        self.btnExtractDates.clicked.connect(self.extractDates)   #  Signal for extracting dates from file

    def openFileDialog(self):
        """Open a file dialog from the file system of your computer"""
        options = QFileDialog.Options()  # Specify various options and flags that control the behaviour and appearance of the file dialog
        options |= QFileDialog.ReadOnly  # Set the 'ReadOnly' option for the file dialog. The '|=' operator is used to add this option to the existing options

        # Open a file dialog that allows the user to select a file for opening 
        filePath, _ = QFileDialog.getOpenFileName(  
            # Main window, Title of the file dialog, current directory, Display all files and files with .csv extension and pass the options variable
            self, 'Open CSV File', '', 'CSV Files (*.csv);;All Files (*)', options=options
        )
        
        if filePath:  # Check if the user selected a file in the file dialog
            # If a file was selected, this line assigns the selected file's path to the 'self.filePath' attribute of the instance. 
            # This attribute can be used later in your application to access and work with the selected file.
            self.filePath = filePath

    def extractDates(self):
        """This method reads data from a CSV file and extracts dates using 
        the extractDateFromInput function."""

        # Check if a file path has been set
        if not hasattr(self, 'filePath'):
            logging.error('File path has not been set')  # Display a message if an error occured
            return
        
        # Initialize an empty list to store the data from the CSV file
        csvData = []

        # Open the CSV file and read its contents
        try:
            with open(self.filePath, 'r', encoding='utf-8') as csvFile:  # Open the csv file
                reader = csv.reader(csvFile)                             # Read contents from the csv file
                for row in reader:                                       # Go through every row in the csv file
                    csvData.extend(row)                                  # Add every row at the end of the list
        except Exception as e:
            logging.error(f'Error reading CSV file: {e}')  # Display error message in the terminal if an error occured

        # Convert the list of data to a single string for date extraction
        inputData = ' '.join(csvData)

        # Call extractDateFromInput to extract dates
        dates = extractDateFromInput(inputData)

        # Display the extracted dates in the text area
        self.textArea.setPlainText('\n'.join(dates))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateExtractorApp()
    window.show()
    sys.exit(app.exec_())

