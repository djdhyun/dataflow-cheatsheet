import setuptools

setuptools.setup(
    name='helloworld',
    install_requires=[
        'apache-beam==2.38.0',
        'emoji==1.7.0'
    ],
    packages=setuptools.find_packages(),

    # warnings suppressors
    description='Say Hello to the world',
    author='me',
    author_email='me@my.self',
    url='https://my.self/',
)
