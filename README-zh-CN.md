# SimpleQuant "简单量化" Python 计算库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English Project Description](README.md)

**注意：本项目仍在持续开发中，目前尚有一些功能还没有正式加入**



一个简单的Python量化分析库，可用于分析特定某个证券或整个市场的形势。内置多个因子的计算函数。

-------

## 快速开始

### 克隆存储库

```
git clone https://github.com/bobliboya/SimpleQuant.git
```

### 安装依赖项

我们建议您使用虚拟环境来运行本项目。您可以使用Python Virtual Environment (`pyvenv`) 或者 Conda 来创建一个虚拟环境：

```
cd your/path/to/SimpleQuant       // 移动到项目根目录
python --version                  // 确保安装了 Python 3.12 或以上
python -m venv ./venv             // 为项目创建虚拟环境或使用Conda
venv/Scripts/activate             // (Windows) 激活虚拟环境
venv/bin/activate                 // (Linux or MacOS) 激活虚拟环境
```

当您成功激活虚拟环境以后，您能在命令行最前面看到`(venv)`字样。现在请安装所有的依赖项：

```
pip install -r requirements.txt
```

### 尽情探索！

恭喜您已经准备好了！您可以尽情探索该项目了。

---

## 项目结构

```
SimpleQuant
├── data/                    # 数据文件
│   ├── sample_data.csv      # 我们提供了一个示例数据文件
│   └── ...
├── docs/                    # 项目文档文件
│   └── ...
├── simplequant/             # 核心源码文件夹，包含数个子模块和子包 
│   ├── factor/
│   ├── plot/
│   ├── func.py
│   └── ...
└── tests/                   # 测试文件
    └── ...

```

