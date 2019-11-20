# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 14:53
# @Author  : alvin
# @File    : seaborn.py
# @Software: PyCharm

import pandas as pd
import numpy as np

df = pd.DataFrame(dict(time=np.arange(500), value=np.random.randn(500).cumsum()))