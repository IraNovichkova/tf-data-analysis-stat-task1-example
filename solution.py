import pandas as pd
import numpy as np


chat_id = 335933917 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return (2 * sum(np.abs(x)))/ (53 * 53 * len(x))
