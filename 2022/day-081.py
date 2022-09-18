
import math
import numpy as np

p_col = [i for i in df.columns if i not in d_cols]


save_model_file(p_col,
                PathName.PRODUCT_COL_SAVE_PATH.value,
                FileName.PRODUCT_COL_NAME.value)
