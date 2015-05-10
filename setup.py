from setuptools import setup

setup(
    name='WorldHappiness',
    version='0.1',
    py_modules='worldhappiness',
    install_requires=[
        'click',
        'oauthlib',
        'redis',
        'requests',
        'requests-oauthlib',
        'six',
        'tweepy'
    ],
    entry_points ='''
        [console_scripts]
        worldhappiness=worldhappiness.run:cli
    ''',
)
