from setuptools import setup

setup(name='pyPackTF',
      description="Unofficial Python API to commuincate with the Backpack.TF API",
      long_description=open('README.md').read(),
      url="https://github.com/djfigs1/pyPackTF",
      packages=["pyPackTF", "pyPackTF.bpktf", "pyPackTF.community", "pyPackTF.market", "pyPackTF.tests"],
      include_package_data = True,
      package_data={'pyPackTF.tests': ['*.json']},
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      )
