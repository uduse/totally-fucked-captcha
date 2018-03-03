from setuptools import setup, find_packages

setup(
        name='fcaptcha',
        version='0.1',
        author='uduse (Zeyi Wang)',
        packages=find_packages(),
        install_requires=['keras', 'captcha']
)