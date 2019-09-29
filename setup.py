from setuptools import setup, find_packages

setup(
    name='vmail-manager',
    version='0.1',
    pymodules=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'sqlalchemy',
        'pymysql',
        'tabulate',
        'argon2_cffi',
        'confuse',
    ],
    entry_points='''
    [console_scripts]
    vmail-manager=vmail_manager:cli
    ''',
)