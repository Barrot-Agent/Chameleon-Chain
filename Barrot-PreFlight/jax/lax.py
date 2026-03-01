import numpy as np
def scan(f, init, xs, length=None): return init, xs
def cond(pred, true_fun, false_fun, *operands): 
    return true_fun(*operands) if pred else false_fun(*operands)
def with_sharding_constraint(x, sharding): return x
