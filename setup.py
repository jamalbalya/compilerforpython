from setuptools import setup
APP=['MonitoringBandwith.py'] #put your python file
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
