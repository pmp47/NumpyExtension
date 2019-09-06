from setuptools import setup
setup(name='Numpyextension',
	version='1.1.1',
	description='A library focused functions that only require numpy.',
	url='https://www.github.com/pmp47/Numpyextension',
	author='pmp47',
	author_email='phil@zeural.com',
	license='MIT',
	packages=['numpyextension'],
	install_requires=['numpy==1.17.1'],
	zip_safe=False,
	include_package_data=True,
	python_requires='>=3.6',

	package_data={'': ['data/*.*']}
)
