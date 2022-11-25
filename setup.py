import setuptools
import glob
import os
def get_package_data():
        list_of_files = []
        list_of_files = list_of_files + glob.glob(os.path.join('docStore','img'+'*.png'))
        list_of_files = list_of_files + glob.glob(os.path.join('docStore','ndcs','r.txt'))
        list_of_files = list_of_files + glob.glob(os.path.join('docStore','sample','*.txt'))
        list_of_files = list_of_files + glob.glob(os.path.join('docStore','sample','*.json'))
        return list_of_files


install_requires=[
        "st-annotated-text==3.0.0",
        "markdown==3.4.1",
        "streamlit-aggrid==0.3.3",
]


setuptools.setup(
        name='appstore',
        version='1.0.2',
        description='Climate Policy Analysis Machine',
        author='prashant',
        author_email='prashant.singh@giz.de',
        packages=setuptools.find_packages(where='appstore'),  #same as name
        # package_data={
        # 'appstore': get_package_data,},
        install_requires=install_requires, #external packages as dependencies
        )