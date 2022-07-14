#  Selecting columns based on dtype

import numpy as np
import pandas as pd


def subdtypes(dtype):
    subs = dtype.__subclasses__()
    if not subs:
        return dtype
    return [dtype, [subdtypes(dt) for dt in subs]]


subdtypes(np.generic)