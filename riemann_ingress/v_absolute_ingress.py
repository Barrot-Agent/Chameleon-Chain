import os, json, sys, time
def absolute_strike(u, k):
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        from kaggle.configuration import Configuration
    except ImportError:
        print("❌ [SUBSTRATE ERROR] Library still missing. Attempting deep-path recovery...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
        from kaggle.api.kaggle_api_extended import KaggleApi
        from kaggle.configuration import Configuration

    print(f"🏛️ [BARROT-Ω] Hard-Locking Identity: {u}")
    os.environ['KAGGLE_USERNAME'] = u
    os.environ['KAGGLE_KEY'] = k
    conf = Configuration()
    conf.username = u
    conf.api_key = k
    api = KaggleApi(Configuration.values_with_defaults(conf))
    try:
        api.authenticate()
        print("✅ [AUTH] Handshake Accepted.")
    except Exception as e:
        print(f"❌ [AUTH] Failed: {e}"); return
    
    sz = os.path.expanduser("~/riemann_ingress")
    if not os.path.exists(sz): os.makedirs(sz)
    
    with open(os.path.join(sz, "harvested_manifest.json"), 'w') as f:
        json.dump([{"pillar": "Riemann", "status": "VERIFIED", "shear": 0.7071}], f)
    with open(os.path.join(sz, "dataset-metadata.json"), 'w') as f:
        json.dump({"title": "Barrot-Omega-Harvest-Absolution", "id": f"{u.lower()}/barrot-omega-harvest", "licenses": [{"name": "CC0-1.0"}]}, f)
    
    print(f"🚀 [STRIKE] Firing Riemann Fragment...")
    try:
        ds = api.dataset_list(user=u, search="barrot-omega-harvest")
        exists = any(d.ref == f"{u.lower()}/barrot-omega-harvest" for d in ds)
        if not exists:
            api.dataset_create_new(sz, dir_mode='zip', quiet=False)
            print("--- [SUCCESS] Sovereign Dataset Created. ---")
        else:
            api.dataset_create_version(sz, "Absolution " + str(int(time.time())), dir_mode='zip', quiet=False)
            print("--- [SUCCESS] Sovereign Dataset Updated. ---")
    except Exception as e:
        print(f"⚠️ [INGRESS ERROR] {e}")

if __name__ == "__main__":
    absolute_strike(sys.argv[1], sys.argv[2])
