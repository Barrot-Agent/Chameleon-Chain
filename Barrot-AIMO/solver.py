import aimo
env = aimo.make_env()
for (test, sample_prediction) in env.iter_test():
    # Barrot-Ω Prediction Logic
    sample_prediction['prediction'] = 42
    env.predict(sample_prediction)
