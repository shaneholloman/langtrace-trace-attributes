from setuptools import find_packages, setup

setup(
    name='trace-attributes',  # Choose a unique name for PyPI
    version='1.0.0',
    author='Karthik Kalyanaraman',
    author_email='karthik@scale3labs.com',
    description='LangTrace - Trace Attributes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Scale3-Labs/langtrace-trace-attributes',  # Project home page
    package_dir={'': 'src/python'},
    packages=find_packages(where='src/python'),
    install_requires=[
        'pydantic>=1.8',  # Example dependency, adjust according to your project's needs
        # Other dependencies
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,  # To include non-code files specified in MANIFEST.in
)
