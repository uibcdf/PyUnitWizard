.. pyunitwizard documentation master file

PyUnitWizard
============

There are several Python libraries to work with physical quantities in the market. Pint, unyt or simtk.unit, are just some of them. Imagine that your project, or workflow, requires the interaction with more than one of these tools. Or that you are not sure if you will work with a different quantities library in the future. Are you looking for a unique API to work with different quantities libraries? Wouldn't it be a relief? PyUnitWizard just do that. It is the wizard you need in your code to change the form of your quantities with few effort. With PyUnitWizard you can:

- Convert physical quantities and units between the different native objects from a set of :ref:`supported libraries<libraries-supported>`.
- Work with physical quantities with a simple syntaxis no matter the library you chose to do the hard work in the background.
- Integrate a quantities wizard in your library defining the default library and the standard units in you project.

Have a look to the `quick guide <https://uibcdf.org/PyUnitWizard/Quick_Guide.html>`_ to see some examples of PyUnitWizard in action.


.. _libraries-supported:

Libraries supported
-------------------

- `pint <https://github.com/hgrecco/pint>`_
- `unyt <https://github.com/yt-project/unyt>`_
- `simtk.unit <https://github.com/openmm/openmm/tree/master/wrappers/python/openmm/unit>`_ (openmm.unit in a near future)

.. toctree::
   :name: installation
   :caption: Installation and quick guide
   :maxdepth: 1

   contents/Installation.md
   contents/Quick_Guide.ipynb

.. toctree::
   :name: user_guide
   :caption: User guide
   :maxdepth: 2

   contents/Importing.ipynb
   contents/Quantities_and_Units.ipynb
   contents/Dimensionality.ipynb
   contents/Convert.ipynb
   contents/Strings.ipynb
   contents/Standardize.ipynb
   contents/In_Your_Library.ipynb

.. toctree::
   :caption: API Documentation
   :maxdepth: 2

   api

Glossary, indices and tables
============================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

