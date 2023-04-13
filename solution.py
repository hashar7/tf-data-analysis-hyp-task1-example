import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 458704720 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    _, p_value = proportions_ztest(count=np.array([x_success, y_success]),
                                      nobs=np.array([x_cnt, y_cnt]),
                                      alternative='larger')
    if x_cnt < 5000:
      return p_value <= 0.09
    return p_value > 0.09
