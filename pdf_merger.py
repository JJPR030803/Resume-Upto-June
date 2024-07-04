import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
import PyPDF2

class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Merger')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.select_button = QPushButton('Select PDF Files', self)
        self.select_button.clicked.connect(self.select_files)
        layout.addWidget(self.select_button)

        self.merge_button = QPushButton('Merge PDFs', self)
        self.merge_button.clicked.connect(self.merge_pdfs)
        layout.addWidget(self.merge_button)

        self.save_button = QPushButton('Save Merged PDF', self)
        self.save_button.clicked.connect(self.save_merged_pdf)
        layout.addWidget(self.save_button)

        self.status_label = QLabel('', self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.pdf_files = []
        self.merged_pdf = None

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, 'Select PDF Files', '', 'PDF Files (*.pdf)')
        if files:
            self.pdf_files = files
            self.status_label.setText(f'Selected {len(files)} files')

    def merge_pdfs(self):
        if not self.pdf_files:
            self.status_label.setText('No files selected')
            return

        self.merged_pdf = PyPDF2.PdfMerger()
        try:
            for pdf in self.pdf_files:
                self.merged_pdf.append(pdf)

            self.status_label.setText('PDFs merged successfully. Now you can save the merged PDF.')
        except Exception as e:
            self.status_label.setText(f'Error: {str(e)}')

    def save_merged_pdf(self):
        if not self.merged_pdf:
            self.status_label.setText('No merged PDF to save')
            return

        output_path, _ = QFileDialog.getSaveFileName(self, 'Save Merged PDF', '', 'PDF Files (*.pdf)')
        if not output_path:
            return

        try:
            with open(output_path, 'wb') as output_file:
                self.merged_pdf.write(output_file)

            self.status_label.setText('Merged PDF saved successfully')
        except Exception as e:
            self.status_label.setText(f'Error: {str(e)}')

def main():
    app = QApplication(sys.argv)
    ex = PDFMergerApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
