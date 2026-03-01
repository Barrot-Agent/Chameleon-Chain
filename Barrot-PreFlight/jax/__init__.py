import numpy as np
from . import numpy as jnp
from . import lax
from . import tree_util

# Mocking the base Array type for Barrot's KVMemory
class Array: pass

class Config:
    def update(self, key, val): pass

config = Config()

def jit(f): return f
def vmap(f): return f

class random:
    @staticmethod
    def PRNGKey(s): return np.array([0, s], dtype=np.uint32)
