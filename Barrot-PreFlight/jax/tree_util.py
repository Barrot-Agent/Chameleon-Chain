def tree_map(f, *args): return f(*args)
def tree_flatten(tree): return [tree], None
def tree_unflatten(aux, leaves): return leaves[0]
def tree_leaves(tree): return [tree]
def register_pytree_node(nodetype, flatten_func, unflatten_func):
    # Pass-through: doesn't need to actually register for a mock test
    pass
