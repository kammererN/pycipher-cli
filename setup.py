
'''
GNU General Public License v3+

PyCipher-CLI: tool that encrypts/decrypts a text (.txt) file.  
Copyright (C) 2023 Nicholas Kammerer (nkammerer@albany.edu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

'''


from distutils.core import setup


setup(
    name='PyCipher-cli',
    version='0.1.0-alpha1',
    description='Encrypts/decrypts a text file based on user defined parameters',
    author='Nicholas Kammerer',
    author_email='dev.nxrada@gmail.com',
    license='LICENSE',
    
    packages=['pycipher-cli',],
    scripts=['bin/pycipher-cli.py'],
#    url='https://github.com/nxrada/pycipher-cli',
#    test_suite='tests',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',

        'Topic :: Scientific/Engineering',
        'Topic :: Security :: Cryptography',
        'Topic :: Text Processing :: General',
    ],

    long_description=open('README').read(),
    )
