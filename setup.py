#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
from setuptools import (setup, find_packages)
from pdfsplit import (__version__, __author__, __email__, __license__, __doc__)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

setup(
	# Basic
	name='pdfsplit',
	version=__version__,
	packages=find_packages(),
	# Entry ponit
	entry_points={
		'console_scripts': [
			'pdfsplit = pdfsplit:main',
		]
	},

	# Requirements
	install_requires=["tkinter", "pdfrw"],

	# About
	author=str(__author__),
	author_email=__email__,
	description="Cut out range of page from pdf.",
	license=__license__,
	long_description=__doc__,
	keywords="pdf split",
	url='',

	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Environment :: Gui',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Natural Language :: English',
		'Natural Language :: Czech',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Utilities'
	]
)
