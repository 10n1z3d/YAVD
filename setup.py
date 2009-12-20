from distutils.core import setup
import yavd

setup (
        name = 'YAVD',
        version = yavd.__version__,
        description= 'Download videos from Youtube and others.',
        author = '10n1z3d',
        author_email = '10n1z3d@w.cn',
        url = '',
        license = 'GPLv3',
        packages = ['YAVD'],
        data_files = [('YAVD/', ['README', 'COPYING', 'TODO'])]
      )
