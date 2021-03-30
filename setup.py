# based on https://github.com/pypa/sampleproject/blob/main/setup.py

from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
file_with_version = here / 'us_county_map' / '__init__.py'


def get_version():
    for line in open(file_with_version, encoding='utf-8'):
        if line.startswith('__version__ = '):
            return line.split()[-1].replace("'", "")
    raise ValueError(f'Package version not found in {file_with_version}')


setup(
    name='us_county_map',
    version=get_version(),
    description='Python package to generate styled US county map as SVG',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/trawick/us-county-map/',
    author='Jeff Trawick',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: U.S.A. Maps',
        'License :: OSI Approved :: Apache Software License',
    ],
    packages=['us_county_map'],
    package_data={
        "us_county_map": ["images/*.svg"],
    },
    python_requires='>=3.6, <4',
    install_requires=['beautifulsoup4>=4', 'click>=7'],
    entry_points={
        'console_scripts': [
            'us_county_map = us_county_map:cli',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/trawick/us-county-map/issues',
        # 'Funding': 'https://donate.something.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/trawick/us-county-map/',
    },
)
