from setuptools import setup, find_packages

setup(
    name='carbon',
    version='0.0.1',
    packages=find_packages(),
    author='Bucket-Inc',
    author_email='bucket.inc.contact@gmail.com',
    description='Python libary for CLI app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bucket-inc/Carbon',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'rich',  # No specific version requirement for requests
    ],
)
