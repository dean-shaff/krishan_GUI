from connect3 import maker_of_poem
from send_email import send_email
import os 
import sys
import shutil
from PyQt4 import QtCore, QtGui

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# text_dir = "{}/texts".format(os.getcwd())
path_gui = resource_path(os.path.dirname(os.path.realpath(__file__)))
# print(path_gui)
text_dir = resource_path(os.path.join(path_gui, "texts"))

emails = []
poems = []

# fileconrad = "{}/{}".format(text_dir,"conrad.txt")
fileconrad = os.path.join(text_dir,"conrad.txt")
# filekafka = "{}/{}".format(text_dir,"kafka.txt")
filekafka = os.path.join(text_dir,"kafka.txt")
fileyellow = "{}/{}".format(text_dir,"yellow.txt")
filedickens = "{}/{}".format(text_dir,"DickensTaleofTwo.txt")
filechina = "{}/{}".format(text_dir,"china.txt")
filechristie = "{}/{}".format(text_dir,"christie.txt")
filedeadmen = "{}/{}".format(text_dir,"deadmen.txt")
filefairy = "{}/{}".format(text_dir,"fairy.txt")
filekant = "{}/{}".format(text_dir,"kant.txt")
filesteam = "{}/{}".format(text_dir,"steam.txt")
fileausten = "{}/{}".format(text_dir,"AustenPride.txt")
fileglass = "{}/{}".format(text_dir,"GlassbyEdwardDillon.txt")

# book_names = ["Heart of Darkness by Conrad", "kafka"]
books = {"Heart of Darkness by Joseph Conrad":fileconrad,
        "The Metamorphosis by Frank Kafka":filekafka,
        "A Collection of Chinese Fairy Tales":filechina,
        "A Collection of Persian Fairy Tales":filefairy,
        "The Yellow Wallpaper by Charlotte Gilman Perkins":fileyellow,
        "A Manual about the History of Steam Power":filesteam,
        "Dead Men Tell No Takes by E. W. Hornung": filedeadmen,
        "A Treatise of the History of Glass by Edward Dillon":fileglass,
        "A Take of Two Cities by Charles Dickens":filedickens,
        "A Critique of Pure Reason by Immanuel Kant":filekant }

for file in os.listdir(text_dir):
    if os.path.join(text_dir,file) in books.values():
        pass
    else:
        books[os.path.join(text_dir,file)] = os.path.join(text_dir,file)


class Main_Window(QtGui.QMainWindow):

    def __init__(self,parent=None):
        super(Main_Window,self).__init__(parent)
        self.initwindow()

    def initwindow(self):

        self.widget = App_Widgets(self)
        self.setCentralWidget(self.widget)

        exitAction = QtGui.QAction('&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit) #just quitting

        choosefileaction = QtGui.QAction('&Choose File...',self)
        choosefileaction.triggered.connect(self.widget.browse)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(choosefileaction)

        self.setGeometry(300,300,600,600)
        self.setWindowTitle("Krishan's Poem Generator")
        self.show()

class App_Widgets(QtGui.QWidget):

    def __init__(self,parent):
        super(App_Widgets, self).__init__(parent)

        self.initUI()

    def initUI(self):

        self.welcome_string = "Welcome to Krishan's poem generating app!"
        self.directions_string = "Select two books at left and click \"Make a Poem\"\n\n"
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        self.grid = grid

        self.text_box = QtGui.QTextEdit("{}\n\n".format(self.welcome_string))
        self.text_box.append(self.directions_string)
        grid.addWidget(self.text_box,0,1,1,2)

        self.select_box = QtGui.QListWidget()
        self.select_box.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.select_box.setMaximumSize(200,1000)
        self.select_box.itemDoubleClicked.connect(self.rename)
        self.populate()
        grid.addWidget(self.select_box,0,0)
        
        self.send_email_btn = QtGui.QPushButton("Send email")
        grid.addWidget(self.send_email_btn, 1,0)
        self.send_email_btn.clicked.connect(self.send_email)

        self.poem = QtGui.QPushButton("Make a poem!")
        grid.addWidget(self.poem, 1,2)
        self.poem.clicked.connect(self.make_poem)

        self.reset = QtGui.QPushButton("Reset")
        grid.addWidget(self.reset, 1,1)
        self.reset.clicked.connect(self.reset_textbox)

        self.setLayout(grid)

    def display(self):

        print(self.text_box.toPlainText())

    def make_poem(self):

        try:
            text_files = [books[str(x.text())] for x in self.select_box.selectedItems()]
            if len(text_files) > 2:
                self.text_box.append("More than 2 books selected. Only using the first two selected...\n\n")

            poem = maker_of_poem(text_files[0],text_files[1])
            self.poem = poem

            if self.welcome_string in self.text_box.toPlainText():
                self.reset_textbox()
                self.text_box.append("{}\n\n\n".format(poem))
            else:
                self.text_box.append("{}\n\n\n".format(poem))               
        except IndexError:
            self.text_box.append("Make sure to select two books!")
        # except IOError as e:
        #   self.text_box.append("{}".format(str([books[str(x.text())] for x in self.select_box.selectedItems()])))
        #   self.text_box.append("{}\n\n".format(os.getcwd()))
        #   self.text_box.append("{}\n\n".format(text_dir))
        #   self.text_box.append("{}\n\n".format(e.strerror))

    def send_email(self):

        email_from = 'poetrytest1@gmail.com'
        input_box = QtGui.QInputDialog()
        input_box.setOkButtonText("Send!")
        input_box.setLabelText("Send yourself an email!")
        ok = input_box.exec_()
        to_email = str(input_box.textValue())
        # print(ok, str(to_email))
        if ok:
            try:
                response = send_email(to_email,email_from,self.poem) 
                response2 = send_email(email_from,email_from,"{}--{}".format(to_email,self.poem)) #so Krishan gets a copy as well.
                # print(response)
                self.text_box.append("{}\n\n\n".format(response))
                emails.append(to_email)
                poems.append(self.poem)
            except AttributeError:
                self.text_box.append("Make sure to generate a poem you like before sending email!\n\n\n")

    @QtCore.pyqtSlot(str) #omg my first decorator!!!!!
    def rename(self,item):
        file_path = item.text()
        self.text_box.append(books[str(file_path)])
        input_box = QtGui.QInputDialog()
        input_box.setOkButtonText("Rename")
        input_box.setLabelText("Rename text file")
        ok = input_box.exec_()
        new_name = str(input_box.textValue())
        if str(new_name) == "":
            self.text_box.append("Make sure to give the book a new name!\n\n")
        else:
            books[new_name] = file_path
            item.setText(new_name)

    def reset_textbox(self):

        self.text_box = QtGui.QTextEdit("")
        self.grid.addWidget(self.text_box,0,1,1,2)

    def populate(self):
        for key in books.keys():
            item = QtGui.QListWidgetItem(key)
            self.select_box.addItem(item)

    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,'Select File')
        if filename != "":
            file_no_path = filename.split("/")[-1]
            copy_path = "{}/{}".format(text_dir,file_no_path)
            if os.path.exists(copy_path):
                self.text_box.append("It looks like you already have this file in the texts folder.\n\n")
            else:
                shutil.copyfile(filename,copy_path)
                books[str(copy_path)] = str(copy_path)
                self.select_box.addItem(copy_path)
        elif filename == "":
            pass

def main():

    app = QtGui.QApplication(sys.argv)
    main_app = Main_Window()
    main_app.show()
    main_app.raise_()
    app.exec_()


if __name__ == "__main__":
    main()
    with open("Exit.txt", 'a') as writer:
        for email, poem in zip(emails,poems):
            writer.write("{} -- {}\n\n\n".format(email,poem))









