from setuptools import setup, find_packages
from numpy.distutils.core import setup
from numpy.distutils.extension import Extension
#import distutils.extension

extensions_list=[]

setup(
    name='openexplorer',
    version='0.0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'openexplorer': 'openexplorer'},
    packages=find_packages(),
    ext_modules=extensions_list,
    package_data={'openexplorer': []},
    scripts=[],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/OpenExplorer',
    license='MIT',
    description="---",
    long_description="---",
)

