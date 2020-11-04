from setuptools import setup, find_packages
import pathlib
from reservation import __about__

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name=__about__.__title__,
    version=__about__.__version__,
    license='MIT License',

    description='Airline seat reservations',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Noxell-zs/airline',
    author=__about__.__author__,
    author_email=__about__.__email__,

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Education',
        'Topic :: Office/Business',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='',

    packages=find_packages(),

    python_requires='>=3.8',

    entry_points={
        'console_scripts': [
            'reservation=reservation.__main__:main',
        ],
    },

    project_urls={'Source': 'https://github.com/Noxell-zs/airline/'},
)
