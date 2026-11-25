"""版本号用例：确保包版本可被正确读取。"""

from rru_testkit import __version__


def test_version():
    """包版本应与 pyproject.toml 中声明的一致。"""
    assert __version__ == "0.1.0"
