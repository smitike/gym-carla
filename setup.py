from setuptools import setup, find_packages

setup(
    name='gym_carla',
    version='0.0.1',
    packages=find_packages(include=['gym_carla', 'gym_carla.*']),
    install_requires=[
        'gym',
        'pygame',
        'numpy',
        'opencv-python'
    ],
)
