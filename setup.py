#!/usr/bin/python3

from setuptools import setup, find_packages
import inshorts

setup(name='Inshorts',
      version='0.2.4',
      description='Short news right into your terminal',
      author='Vinay Khobragade',
      author_email='vinaykhobragade99@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'inshorts = inshorts.inshorts:main',
            ]
      },
      url='https://www.github.com/feat7/inshorts',
      keywords=['inshorts', 'terminal', 'command-line', 'news', 'python'],
      license='MIT',
      classifiers=[],
      install_requires=[
            'BeautifulSoup4',
      ]
     )