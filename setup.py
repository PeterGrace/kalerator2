from setuptools import setup, find_packages

setup(
    name='kalerator2',
    author='pgrace',
    author_email='pete@stackoverflow.com',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'setuptools-lint',
        'pytest',
    ],
    entry_points='''
        [console_scripts]
        kalerator2=kalerator2.main:main
    ''',
)
