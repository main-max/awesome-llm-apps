# rru-testkit

RRU 自动化测试工具包，用于承载频谱仪、信号源等仪器的自动化测试与报告输出。

## 目录结构

```
src/rru_testkit/   核心代码
tests/             测试用例
```

## 开发环境

```powershell
# 依赖（清华镜像）
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pytest pytest-cov pydantic pyyaml typer ruff pyright

# 运行测试
pytest

# 静态检查
ruff check .
```

## 版本

0.1.0 - 项目初始化骨架
