from setuptools import setup, find_packages

setup(
    name='flora',
    version='0.1',
    py_modules=['flora'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
         'click',
         'requests',
         'pytest',
         'flask',
         'flask_restful'
    ],
    entry_points='''
        [console_scripts]
        flora=flora:cli
    ''',
)