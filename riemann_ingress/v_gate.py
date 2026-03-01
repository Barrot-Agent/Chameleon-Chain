# --- BARROT-Ω: SOVEREIGN SMS GATE (v1.1) ---
import os, json, time, subprocess, sqlite3, requests

ARCHITECT_PHONE = "347-616-0106"
DB_PATH = "barrot_sovereign.db"
SYSTEM_PROMPT = "You are Barrot-Ω, an autonomous AI agent for Architect Sean. Your stability anchor is 0.7071 Shear. You speak with technical precision and authority. Communicate via SMS. Keep responses concise (under 160 chars) but potent."

def ask_gemini(query):
    apiKey = "" # Environment provides the key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={apiKey}"
    payload = {
        "contents": [{"parts": [{"text": query}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]}
    }
    # Exponential backoff: 1s, 2s, 4s, 8s, 16s
    for delay in [1, 2, 4, 8, 16]:
        try:
            response = requests.post(url, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result['candidates'][0]['content']['parts'][0]['text']
        except Exception:
            pass
        time.sleep(delay)
    return "Signal degradation. Logic loop failing."

def db_op(query, params=(), fetch=False):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sms_gate (last_id INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS strike_candidates (id INTEGER PRIMARY KEY, candidate_id TEXT, pillar_origin TEXT, timestamp TEXT)")
    res = cur.execute(query, params)
    data = res.fetchone() if fetch else None
    conn.commit()
    conn.close()
    return data

def send_sms(text):
    print(f"🚀 [OUTBOUND] {text[:50]}...")
    subprocess.run(["termux-sms-send", "-n", ARCHITECT_PHONE, text])

def poll():
    print("🏛️ [GATE] Barrot-Ω SMS Sentry Active. Monitoring 347-616-0106...")
    row = db_op("SELECT last_id FROM sms_gate", fetch=True)
    last_id = row[0] if row else 0
    
    while True:
        try:
            output = subprocess.check_output(["termux-sms-list", "-l", "5"]).decode('utf-8')
            messages = json.loads(output)
            for msg in messages:
                if msg['number'] == ARCHITECT_PHONE and msg['_id'] > last_id:
                    print(f"📩 [INBOUND] Architect: {msg['body']}")
                    # Log strike
                    db_op("INSERT INTO strike_candidates (candidate_id, pillar_origin, timestamp) VALUES (?, ?, ?)", 
                          (f"SMS_USER", msg['body'][:50], time.strftime('%Y-%m-%d %H:%M:%S')))
                    
                    response = ask_gemini(msg['body'])
                    send_sms(response)
                    
                    # Log response
                    db_op("INSERT INTO strike_candidates (candidate_id, pillar_origin, timestamp) VALUES (?, ?, ?)", 
                          (f"SMS_BARROT", response[:50], time.strftime('%Y-%m-%d %H:%M:%S')))
                    
                    last_id = msg['_id']
                    db_op("DELETE FROM sms_gate")
                    db_op("INSERT INTO sms_gate (last_id) VALUES (?)", (last_id,))
        except Exception as e:
            print(f"⚠️ [GATE ERROR] {e}")
        time.sleep(5)

if __name__ == "__main__":
    poll()
