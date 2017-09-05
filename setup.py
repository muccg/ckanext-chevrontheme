#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-chevrontheme',
    version='0.14.0',
    description='',
    license='AGPL3',
    author='CCG, Murdoch University',
    author_email='chevron@ccg.murdoch.edu.au',
    url='https://github.com/muccg/ckanext-chevrontheme/',
    namespace_packages=['ckanext'],
    packages=['ckanext.chevrontheme'],
    zip_safe=False,
    include_package_data=True,
    package_dir={'ckanext.chevrontheme': 'ckanext/chevrontheme'},
    package_data={'ckanext.chevrontheme': ['*.json', 'templates/*.html', 'templates/*/*.html', 'templates/*/*/*.html', 'static/*.css', 'static/*.png', 'static/*.jpg', 'static/*.css', 'static/*.ico']},
    entry_points = """
        [ckan.plugins]
        chevron_theme = ckanext.chevrontheme.plugins:CustomTheme
    """
)
