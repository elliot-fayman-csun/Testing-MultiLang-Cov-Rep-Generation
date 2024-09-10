#pytest
#pytest-cov
import pytest
from Python_Src.python_custom_reversal import *


def test_reverse_text():
    assert reverse_text('python') == 'nohtyp'
