# Instructions

## Required

```bash
conda install conda-build anaconda-client
```

## Building and pushing to https://anaconda.org/uibcdf

```bash
#conda build . --no-anaconda-upload
PACKAGE_OUTPUT=`conda build . --no-anaconda-upload --output`
anaconda login
anaconda upload --user uibcdf $PACKAGE_OUTPUT --label dev
conda build purge
anaconda logout
```

## Install

```
conda install -c uibcdf/label/dev pyunitwizard
```

## Additional Info
https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages

