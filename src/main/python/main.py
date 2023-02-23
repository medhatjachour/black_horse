from app import app_context
from app import MainWindow
import sys
id = 0
import wmi
c = wmi.WMI()
if __name__ == '__main__':       # 1. Instantiate ApplicationContext
    for item in c.Win32_PhysicalMedia():
        id  = item.SerialNumber
        if id == "50026B73811921F3":
            window = MainWindow()
            window.show()
            exit_code = app_context.app.exec()      # 2. Invoke appctxt.app.exec_()
            sys.exit(exit_code)
