# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'colgado.py',
            'description'    : 'Descripcion del programa.',
            }],
        'zipfile' : None, 
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='nombreproyecto',
    author='Nombre del autor',
    author_email='autor@correo.com',
    **kwargs)
