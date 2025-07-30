# SimpleQuant Python Library
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

[中文版项目介绍](README-zh-CN.md)

**Note: This project is still under development. There are functionalities that are not implemented yet.**

A simple quantitative analysis library for Python. Used to analysis a single security or the whole market. Function implemented for multiple factors included.

-------

## Quick Start

### Clone this Repository

```
git clone https://github.com/bobliboya/SimpleQuant.git
```

### Install Dependencies

We suggest you to run this project in a virtural enviroment that is isolated from your default environent. You may use Python Virtural Enviroment `pyvenv` or Conda to create a virtural environment.

```
cd your/path/to/SimpleQuant       // Go to the tepo root directory
python --version                  // Make sure you have Python 3.12 or above installed
python -m venv ./venv             // Create the virtural enivonment in the root directory
venv/Scripts/activate             // (Windows) Activate the venv
venv/bin/activate                 // (Linux or MacOS) Activate the venv
```

After you successfully activate the vitural enviroment, you can see `(venv)` ahead the command prompt. You may now install all dependencies.

```
pip install -r requirements.txt
```

### Explore!

Congratulations! You are ready to explore this project now.

---

## Project Architecture

```
SimpleQuant
├── data/                    # Data files
│   ├── sample_data.csv      # We provided a sample dataset
│   └── ...
├── docs/                    # Documentation files
│   └── ...
├── simplequant/             # Core folder with multiple sub-packages and modules 
│   ├── factor/
│   ├── func.py
│   └── ...
└── tests/                   # Testing files
    └── ...

```

