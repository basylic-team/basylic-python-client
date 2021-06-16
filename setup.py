from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='basylic',
    version='0.12.2',    
    description="Python interface to Basylic's API",
    url='https://github.com/basylic-team/basylic-python-client',
    download_url = 'https://github.com/basylic-team/basylic-python-client/tarball/0.12.2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Petar Todorov',
    author_email='ptodorov@etaonis.com',
    license='MIT',
    packages=['basylic'],
    install_requires=['requests>=2.22.0',],
    keywords = ['insurance', 'anti-fraud', 'basylic'],
    classifiers=[
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
    ],
)