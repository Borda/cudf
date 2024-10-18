# Copyright (c) 2020-2024, NVIDIA CORPORATION.

from packaging import version
import pandas as pd

PANDAS_CURRENT_SUPPORTED_VERSION = version.parse("2.2.3")
PANDAS_VERSION = version.parse(pd.__version__)


PANDAS_GE_210 = PANDAS_VERSION >= version.parse("2.1.0")
PANDAS_GE_220 = PANDAS_VERSION >= version.parse("2.2.0")
PANDAS_LT_300 = PANDAS_VERSION < version.parse("3.0.0")
