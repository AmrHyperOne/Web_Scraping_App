from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class CL_UserPassword(QtWidgets.QDialog):

    def __init__(self, parent=None):
        try:
            super(CL_UserPassword, self).__init__()
            mod_path = Path(__file__).parent
            self.dirname = mod_path.__str__()
            # + '/presentation/main_login_ui'
            filename = self.dirname + '/UserPassword.ui'
            print(filename)
            self.parent = parent
            loadUi(filename, self)
        except Exception as e:
            print(e)

    def GetUserPassword(self):
        Username = self.lineEdit_Username.text()
        Password = self.lineEdit_Password.text()

        dic = {1: ['admin', '123']}

        # if Username == 'admin' and Password == '123':
        if [Username, Password] in dic.values():
            self.parent.show()
            self.parent.Cashier_window.close()

        # return Username, Password
