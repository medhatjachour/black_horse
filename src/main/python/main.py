from app import app_context
from app import MainWindow
from PySide6.QtWidgets import QMessageBox
import sys
import subprocess
x = (subprocess.run("wmic diskdrive get serialnumber",  capture_output=True)).stdout
# id = int( str( x[21:37])[2:-1] )
id = (str( x[21:37])[2:-1]) 
if __name__ == '__main__':       # 1. Instantiate ApplicationContext
    
    # if id == "H2UBTY010211017":
    if id == "50026B73811921F3":
        window = MainWindow()
        window.show()
        exit_code = app_context.app.exec()      # 2. Invoke appctxt.app.exec_()
        sys.exit(exit_code)
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("It's not your Version")
        dlg.setText("this version is not authorized to run on this pc so تعالي لبابا يسطي\n the website is : medhatjachour.com")
        dlg.setIcon(QMessageBox.Critical)
        dlg.exec()