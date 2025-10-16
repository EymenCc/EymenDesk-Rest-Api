from setuptools import setup, find_packages

setup(
    name='Eymendesk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    author='Eymen Civelek',
    description='EymenDesk',
    url='https://github.com/EymenCc/EymenDesk-Rest-Api',
    license='MIT',
    python_requires='>=3.7',
)