#pytest
#pytest-cov
import pytest
from custom_reversal import *


def test_reverse_text():
    assert reverse_text('python') == 'nohtyp'