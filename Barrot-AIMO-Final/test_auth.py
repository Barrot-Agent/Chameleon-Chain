import os, json, urllib.request, base64

key_path = os.path.expanduser('~/.kaggle/kaggle.json')
print("📡 [BARROT-Ω]: Initiating direct X-Ray on credentials...")

try:
    with open(key_path, 'r') as f:
        creds = json.load(f)
        user = creds.get('username')
        key = creds.get('key')
        print(f"🔑 User Found: {user}")
        print(f"🔑 Key Found:  {key[:5]}.......{key[-5:]}")
except Exception as e:
    print(f"❌ CRITICAL: Cannot read kaggle.json: {e}")
    exit()

url = "https://api.kaggle.com/v1/competitions/list"
auth_string = f"{user}:{key}"
base64_string = base64.b64encode(auth_string.encode("ascii")).decode("ascii")

req = urllib.request.Request(url)
req.add_header("Authorization", f"Basic {base64_string}")

try:
    response = urllib.request.urlopen(req)
    print(f"✅ HANDSHAKE ACCEPTED! HTTP {response.getcode()}")
    print("If you see this, the CLI is broken. The key is fine.")
except urllib.error.HTTPError as e:
    print(f"❌ HANDSHAKE REJECTED: HTTP {e.code} - {e.reason}")
    print("If you see this, Kaggle has permanently killed this key.")
