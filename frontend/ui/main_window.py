#DESCRIPTION: Main layout, connects componenets like uploader, preview etc
#Sets the window title,size,global layout. Handles signals
#Acts as a the layout manager and signal handler

from PyQt5.QtWidgets import( 
    QMainWindow,QWidget,
    QVBoxLayout,QLabel)

from components.dataset_uploader import DatasetUploader
from components.dataset_preview import DatasetPreview

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Machine Learning Platform: No CODE")
        self.setMinimumSize(1000,600)

        #Central Widget
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        #Layout
        title=QLabel("📊 AutoML Platform")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(title)

        #Dataset Uploader component
        self.uploader=DatasetUploader()
        self.uploader.file_loader.connect(self.handle_file_loaded)
        self.layout.addWidget(self.uploader)
        
        #Dataset preview content
        self.preview=DatasetPreview()
        self.layout.addWidget(self.preview)

    def handle_file_loaded(self,df):
        """
            SLOT TO UPDATE PREVIEW WHEN FILE IS LOADED

        """
        self.preview.show_preview(df)

    






