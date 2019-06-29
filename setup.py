from setuptools import setup, find_packages

setup(
    name='jetracer',
    version='0.0.0',
    description='An easy to use AI racecar powered by NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'adafruit-circuitpython-servokit'
    ],
)
