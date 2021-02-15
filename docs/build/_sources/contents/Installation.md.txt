# Installation

The latest "stable" version of MolModMT can be installed from the UIBCDF Anaconda channel:

```bash
conda -c uibcdf pyunitwizard # Not working yet
```

If you want to work with the not so tested last beta version, the installation command is the following:

```bash
conda install -c uibcdf/label/dev pytunitwizard # Not working yet
```

The former beta version is nothing but a quenched version from the main github repository of this project which it is done from time to time with few scruples. The raw code fully alive can be installed from this github repo as follows:

```bash
git clone https://github.com/uibcdf/PyUnitWizard.git
cd PyUnitWizard
python setup.py develop
```

In the first two cases, PyUnitWizard can be uninstalled with conda:

```bash
conda remove pyunitwizard
```

But if you installed PyUnitWizard straight from its github central repository, do the following to uninstall it:

```bash
pip uninstall pyunitwizard
```
