from setuptools import setup

APP = ['bomber.py']
DATA_FILES = ['rsc']

OPTIONS = {
	"argv_emulation": False,
	"compressed": True,
	"optimize": 2,
	"iconfile": "rsc/bomber.icns"
}

setup(
	app = APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS}
	)
