import setuptools
import glob
def get_package_data():
        list_of_files = []
        list_of_files = list_of_files + glob.glob('appstore/docStore/img/*.png')
        list_of_files = list_of_files + glob.glob('appstore/docStore/ndcs/*.txt')
        list_of_files = list_of_files + glob.glob('appstore/docStore/sample/*.txt')
        list_of_files = list_of_files + glob.glob('appstore/docStore/sample/*.json')
        return list_of_files


install_requires=[
        "st-annotated-text==3.0.0",
        "markdown==3.4.1",
        "streamlit-aggrid",
]


setuptools.setup(
        name='appstore',
        version='1.0.2',
        description='Climate Policy Analysis Machine',
        author='Data Service Center GIZ',
        author_email='prashant.singh@giz.de',
        package_dir={"": "src"},
        packages=setuptools.find_packages(where='src'),  
        package_data={
        'appstore': get_package_data(),},
        install_requires=install_requires, #external packages as dependencies
        )