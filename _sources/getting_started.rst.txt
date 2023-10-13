Getting Started
===============

This page details how to get started with PathSimAnalysis. 

Installation
------------

PyPi
~~~~

PathSimAnalysis can be installed from PyPI with:

.. code-block:: bash

	pip install pathsimanalysis

If you would like to test your installation, use the `test` optional dependencies and run the tests:

.. code-block:: bash

	pip install "pathsimanalysis[test]"
	pytest --pyargs pathsimanalysis.tests

From source
~~~~~~~~~~~

If you want the latest (non-release) version of PathSimAnalysis, you should install the package from source.

.. code-block:: bash

	git clone --depth=1 https://github.com/MDAnalysis/PathSimAnalysis
	cd PathSimAnalysis
	pip install .

If you want to run tests on your installation, install the `test` dependencies and run the tests:

.. code-block:: bash

	pip install ".[test]"
	pytest --pyargs pathsimanalysis.tests

