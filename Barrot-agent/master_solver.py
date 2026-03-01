import aimo
env = aimo.make_env()
for (test, sample_pred) in env.iter_test():
    sample_pred['prediction'] = 42 # Barrot placeholder
    env.predict(sample_pred)
