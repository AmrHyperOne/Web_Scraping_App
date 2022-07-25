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
        self.Username = self.lineEdit_Username.text()
        self.Password = self.lineEdit_Password.text()

        dic = {1: ['admin', '123'], 2: ['user1', 'user1'], 3: ['user2', 'user2'], 4: ['user3', 'user3']
               , 5: ['user4', 'user4'], 6: ['user5', 'user5'], 7: ['user6', 'user6']
               , 8: ['user7', 'user7'], 9: ['user8', 'user8'], 10: ['user9', 'user9']
               , 11: ['user10', 'user10']}

        # if Username == 'admin' and Password == '123':
        if [self.Username, self.Password] in dic.values():
            if self.Username != 'admin' and self.Password != '123':
                self.parent.parent.MACaddress = self.Username
                self.parent.read_db()
            self.parent.show()
            self.parent.Cashier_window.close()

        # return Username, Password
