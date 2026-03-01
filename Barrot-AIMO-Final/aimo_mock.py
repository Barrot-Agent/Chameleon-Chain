class MockEnv:
    def __init__(self):
        self.problems = [
            {'problem': 'If $x + y = 10$ and $x - y = 2$, what is $x \cdot y$?'},
            {'problem': 'Solve for the smallest prime factor of $2^{10} - 1$.'}
        ]
        self.current = 0

    def iter_test(self):
        for p in self.problems:
            import pandas as pd
            yield (pd.DataFrame([p]), pd.DataFrame([{'prediction': 0}]))

    def predict(self, pred):
        print(f"🎯 [MOCK-API]: Prediction Received: {pred['prediction'].values[0]}")

def make_env():
    return MockEnv()
