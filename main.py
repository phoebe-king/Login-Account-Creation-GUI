import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QGridLayout, QLabel, QLineEdit
)

class loginWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(10)
        self.setLayout(layout)
        self.setFixedHeight(250)
        self.setFixedWidth(285)

        title = QLabel("Welcome!")
        title.setProperty("class", "heading")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Username")
        layout.addWidget(self.user_input, 1, 0, 1, 3)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pass_input, 2, 0, 1, 3)

        loginBtn = QPushButton("Sign In")
        loginBtn.clicked.connect(self.login)
        layout.addWidget(loginBtn, 3, 0, 1, 0)

        registerBtn = QPushButton("Create Account")
        registerBtn.clicked.connect(self.register)
        layout.addWidget(registerBtn, 4, 0, 1, 0)

    def login(self):
        pass

    def register(self):
        login.close()
        register.show()

class registerWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(5)
        self.setLayout(layout)
        self.setFixedHeight(350)
        self.setFixedWidth(400)

        title = QLabel("Create Account")
        title.setStyleSheet("font-family: Helvetica; font-size: 20px;")
        layout.addWidget(title, 0, 0, 1, 4, Qt.AlignmentFlag.AlignCenter)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email Address")
        layout.addWidget(self.email, 1, 0, 1, 4)

        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("First Name")
        layout.addWidget(self.firstName, 2, 0, 1, 2)

        self.lastName = QLineEdit()
        self.lastName.setPlaceholderText("Last Name")
        layout.addWidget(self.lastName, 2, 2, 1, 2)

        self.userName = QLineEdit()
        self.userName.setPlaceholderText("Username")
        layout.addWidget(self.userName, 3, 0, 1, 4)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password, 4, 0, 1, 4)

        self.registerBtn = QPushButton("Create Account")
        self.registerBtn.clicked.connect(self.new_acct) 
        layout.addWidget(self.registerBtn, 5, 0, 1, 4)

        self.backBtn = QPushButton("Go back")
        self.backBtn.setStyleSheet("background-color: transparent; border: transparent; text-decoration: underline; font-size: 16px;")
        self.backBtn.clicked.connect(self.goBack)
        layout.addWidget(self.backBtn, 6, 1, 1, 2, Qt.AlignmentFlag.AlignCenter)

    def goBack(self):
        register.close()
        login.show()


    def new_acct(self):
        register.close()
        login.show()

app = QApplication(sys.argv)
login = loginWindow()
register = registerWindow()

with open("styles.css", "r") as file:
    app.setStyleSheet(file.read())

login.show()
app.exec()