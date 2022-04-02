import sys
from ui import *
from PyQt5.QtWidgets import *
from trials import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
class main_windows(QMainWindow):

    def __init__(self):
        super(main_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.drop_down_box.addItems(["","NCTId", "Condition","InterventionName","LastKnownStatus", "StartDate", "PrimaryCompletionDate", "CompletionDate", "StudyFirstPostDate", "StudyFirstSubmitDate","MaximumAge", "MinimumAge","EnrollmentCount", "Phase", "OrgFullName", "BriefTitle", "LocationCountry", "PrimaryOutcomeDescription", "SecondaryOutcomeDescription"])
        self.ui.drop_down_box.currentIndexChanged.connect(self.convert_drop_box_text)
        self.ui.pushButton.clicked.connect(self.clickme)
        #  self.ui.textBrowser.setFixedWidth()
    def convert_drop_box_text(self):
        # self.ui.textedit_input.clear()
        text_selected = self.ui.drop_down_box.currentText()
        if text_selected != "":
            self.ui.selected_box.append(text_selected)
        #pass

    def clickme(self):
        search1 = self.ui.textEdit_1.toPlainText()
        search2 = self.ui.textEdit_2.toPlainText()
        huck_trial(search1,search2, self.ui.selected_box.toPlainText().split())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = main_windows()
    #w.resize(300,300)
    w.setWindowTitle("USRegi")

    w.show()
    sys.exit(app.exec_())