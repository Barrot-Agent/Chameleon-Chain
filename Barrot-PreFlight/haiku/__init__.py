import typing
import numpy as np

# Types
class Params(dict): pass
class State(dict): pass

class PRNGSequence:
    def __init__(self, key): self.key = key
    def __next__(self): return self.key

# Decorators
def transform(f): return f
def transform_with_state(f): return f
def transparent(f): return f

# Layers
class RMSNorm:
    def __init__(self, axis=-1, eps=1e-6, *args, **kwargs): pass
    def __call__(self, x): return x

class Embed:
    def __init__(self, vocab_size, embed_dim, *args, **kwargs): pass
    def __call__(self, x): return np.zeros((*x.shape, 128)) # Mocked concept vector

# Logic
class Module:
    def __init__(self, name=None): self.name = name

def get_parameter(name, shape, dtype, init): 
    return np.zeros(shape, dtype=dtype)
