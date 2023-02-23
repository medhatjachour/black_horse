from fbs.cmdline import command
from os.path import dirname, join
from shutil import copy
import os
import fbs.cmdline


@command
def mv_inst():

    import fbs
    current_directory = os.getcwd()
    src = join(current_directory, 'Installer.nsi')
    des = join(dirname(fbs.__file__), '_defaults', 'src', 'installer', 'windows')
    os.remove(join(des, 'Installer.nsi'))
    copy(src, des)


if __name__ == '__main__':
    project_dir = dirname(__file__)
    fbs.cmdline.main(project_dir)
