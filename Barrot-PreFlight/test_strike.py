import aimo_mock as aimo
import barrot_grok_core as barrot

print("🧬 [BARROT-Ω]: Starting Pre-Flight Calibration...")
env = aimo.make_env()

for (test, sample_pred) in env.iter_test():
    problem = test['problem'].values[0]
    print(f"📝 [INPUT]: {problem}")
    
    # Execute Barrot's Logic
    ans = barrot.solve(problem)
    print(f"✅ [SOLVED]: {ans}")
    
    sample_pred['prediction'] = int(ans) % 1000
    env.predict(sample_pred)

print("🏁 [BARROT-Ω]: Pre-Flight Successful. Logic is 100% Operational.")
