from fbs.cmdline import command
from os.path import dirname, join
from shutil import copytree
from fbs import path
import fbs.cmdline
import os


@command
def fix_google_imports():

    import google_auth_oauthlib
    import googleapiclient
    import google.auth.transport

    src = join(dirname(google_auth_oauthlib.__file__))
    des = join(path('${freeze_dir}'), 'google_auth_oauthlib')
    src1 = join(dirname(googleapiclient.__file__))
    des1 = join(path('${freeze_dir}'), 'googleapiclient')
    src2 = join(dirname(google.auth.transport.__file__))
    des2 = join(path('${freeze_dir}'), 'google', 'auth', 'transport')
    copytree(src, des)
    copytree(src1, des1)
    copytree(src2, des2)


if __name__ == '__main__':
    project_dir = dirname(__file__)
    fbs.cmdline.main(project_dir)
