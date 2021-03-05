# Kepler Project

This project is not really useful. It's just for the fun of coding something when you don't have any inspiration...

## Table of contents
- [Kepler Project](#kepler-project)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Setting up](#setting-up)
    - [Environment configuration](#environment-configuration)

## Introduction

...

## Requirements

- **Python** >= 3.9
- **Virtualenv** package installed

## Setting up

This section is to describe the project setting up procedure.

### Environment configuration

:newspaper: All the procedures described below are done at the root of the project.  
  
First, you need to initialize a virtualenv (ensure to have `virtualenv` package installed in your python libs).

```sh
python -m venv venv

# For Windows dist
.\venv\Script\Activate.ps1

# Or Linux dist
source ./venv/script/activate
```

Then, install needed packages.

```sh
pip install -r requirements.txt -r requirements-dev.txt
```

:warning: **For production environment**, you must to install locked packages.

```sh
pip install -r requirements.lock
```

...