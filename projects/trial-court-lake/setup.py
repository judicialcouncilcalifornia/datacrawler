# Automatically created by: portia

from setuptools import setup, find_packages

setup(
    name='trial-court-lake',
    version='1.0',
    packages=find_packages(),
    data_files = [
        ('', ['project.json', 'items.json', 'extractors.json']),
    ],
    entry_points={
        'scrapy': [
            'settings = spiders.settings'
        ]
    },
    zip_safe=True,
    include_package_data=True,
)

