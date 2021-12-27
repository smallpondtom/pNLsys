from setuptools import find_packages, setup

setup(
  name='pNLsys',
  packages=find_packages(include=['pNLsys']),
  version='0.1.0',
  description='Python Nonlinear System Library',
  author='smallpondtom',
  license='MIT',
  install_requires=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  test_suite='test',
)
