# json_xlsx 发布手册

将 json_xlsx 库发布到 PyPI

## 📁 项目结构

项目结构如下：

```
json_xlsx/
├── json_xlsx/
│   ├── __init__.py
│   ├── converter.py
│   ├── formatters.py
│   ├── config.py
│   └── examples.py
├── tests/
│   └── test_converter.py
├── examples/
│   └── basic_usage.py
├── pyproject.toml
├── README.md
├── LICENSE
├── MANIFEST.in
├── run_tests.py
└── PUBLISH_GUIDE.md
```

## 🔧 发布前准备

### 1. 安装构建工具

```bash
pip install build twine
```

### 2. 运行测试

```bash
# 运行完整测试套件
python run_tests.py

# 或者单独运行单元测试
python -m pytest tests/ -v
```

### 3. 更新版本号

在 `pyproject.toml` 和 `json_xlsx/__init__.py` 中更新版本号：

```toml
# pyproject.toml
[project]
version = "1.0.1"  # 更新版本号
```

```python
# json_xlsx/__init__.py
__version__ = "1.0.1"  # 更新版本号
```

### 4. 更新作者信息

在 `pyproject.toml` 中更新你的信息：

```toml
[project]
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
```

在 `README.md` 中更新 GitHub 链接：

```markdown
[GitHub Issues](https://github.com/quantatirsk/json_xlsx/issues)
```

## 🏗️ 构建包

### 1. 清理旧的构建文件

```bash
rm -rf build/ dist/ *.egg-info/
```

### 2. 构建分发包

```bash
python -m build
```

这会在 `dist/` 目录下生成：

* `json_xlsx-0.0.1.tar.gz` (源代码分发)
* `json_xlsx-0.0.1-py3-none-any.whl` (轮子分发)

### 3. 检查构建结果

```bash
twine check dist/*
```

## 🚀 发布到 PyPI

### 1. 注册 PyPI 账户

如果还没有账户，请到 [PyPI](https://pypi.org/) 注册。

### 2. 配置 API Token（推荐）

1. 登录 PyPI
2. 进入 Account settings > API tokens
3. 创建新的 API token
4. 配置 `.pypirc` 文件：

```ini
[distutils]
index-servers = pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-your-api-token-here
```

### 3. 首次发布到 TestPyPI（推荐）

在正式发布前，先发布到测试环境：

```bash
twine upload --repository testpypi dist/*
```

然后测试安装：

```bash
pip install --index-url https://test.pypi.org/simple/ json_xlsx
```

### 4. 发布到正式 PyPI

```bash
twine upload dist/*
```

## ✅ 发布后验证

### 1. 检查 PyPI 页面

访问 https://pypi.org/project/json_xlsx/ 确认包信息正确。

### 2. 测试安装

在新的环境中测试安装：

```bash
pip install json_xlsx
```

### 3. 测试功能

```python
from json_xlsx import convert_json_to_excel

data = [{"name": "test", "value": 123}]
result = convert_json_to_excel(data, "test.xlsx")
print(result)
```

## 🔄 更新发布

### 1. 修改代码

### 2. 更新版本号

### 3. 更新 CHANGELOG

### 4. 运行测试

### 5. 重新构建和发布

```bash
rm -rf build/ dist/ *.egg-info/
python -m build
twine check dist/*
twine upload dist/*
```

## 📋 发布检查清单

* [ ] 代码测试通过
* [ ] 版本号已更新
* [ ] README.md 内容准确
* [ ] 作者信息正确
* [ ] LICENSE 文件存在
* [ ] 构建成功无警告
* [ ] TestPyPI 测试通过
* [ ] 正式发布成功
* [ ] 安装测试通过

## 🐛 常见问题

### 构建失败

* 检查 `pyproject.toml` 语法
* 确保所有依赖都已安装
* 检查文件权限

### 上传失败

* 检查 API token 是否正确
* 确保版本号未重复
* 检查网络连接

### 安装失败

* 检查依赖包版本兼容性
* 确保 Python 版本要求正确

## 📚 参考资源

* [Python 打包用户指南](https://packaging.python.org/)
* [PyPI 官方文档](https://pypi.org/help/)
* [Twine 文档](https://twine.readthedocs.io/)

---

祝你发布成功！🎉
