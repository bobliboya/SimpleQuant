# SimpleQuant / "简单量化" Python 计算库
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

----

A simple quantitative analysis library for Python. Used to analysis a single security or the whole market. Function implemented for multiple factors included.

一个简单的Python量化分析库，可用于分析特定某个证券或整个市场的形势。内置多个因子的计算函数。

-------

## Quick Start / 快速开始

### Clone this Repository / 克隆存储库

```
git clone https://github.com/bobliboya/SimpleQuant.git
```

### Install Dependencies / 安装依赖项

We suggest you to run this project in a virtural enviroment that is isolated from your default environent. You may use Python Virtural Enviroment `pyvenv` or Conda to create a virtural environment.

我们建议您使用虚拟环境来运行本项目。您可以使用Python Virtual Environment (`pyvenv`) 或者 Conda 来创建一个虚拟环境：

```
cd your/path/to/SimpleQuant       // Go to the tepo root directory
python --version                  // Make sure you have Python 3.12 or above installed
python -m venv ./venv             // Create the virtural enivonment in the root directory
venv/Scripts/activate             // (Windows) Activate the venv
venv/bin/activate                 // (Unix) Activate the venv
```

After you successfully activate the vitural enviroment, you can see `(venv)` ahead the command prompt. You may now install all dependencies.

当您成功激活虚拟环境以后，您能在命令行最前面看到`(venv)`字样。现在请安装所有的依赖项：

```
pip install -r requirements.txt
```

### Explore! / 尽情探索！

Congratulations! You are ready to explore this project now.

恭喜您已经准备好了！您可以尽情探索该项目了。

---

## Architecture / 结构

```
SimpleQuant
├── data/                    # Data files
│   ├── sample_data.csv      # We provided a sample dataset
│   └── ...
├── docs/                    # Documentation files
│   └── ...
├── simplequant/             # Core folder with multiple sub-packages and modules 
│   ├── factor/
│   ├── plot/
│   ├── func.py
│   └── ...
└── tests/                   # Testing files
    └── ...

```

