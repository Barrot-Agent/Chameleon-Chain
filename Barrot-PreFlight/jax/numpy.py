import numpy as np
# Mirror standard numpy
for name in dir(np):
    globals()[name] = getattr(np, name)

# INJECT THE BRAIN-FLOAT ALIAS
# We map bfloat16 to float32 because it's the safest CPU fallback
bfloat16 = np.float32
float32 = np.float32
float16 = np.float16

def array(x, *args, **kwargs): 
    # Strip jax-specific kwargs if they leak in
    kwargs.pop('dtype', None)
    return np.array(x, dtype=np.float32)
