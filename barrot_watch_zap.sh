#!/data/data/com.termux/files/usr/bin/bash
# BARROT-Ω: Robust Sovereign Listener (v5.2)

PORT=8080
DB="barrot_sovereign.db"

echo "[LOG] Watch-Zap Listener RE-DEPLOYED (High-Stability Mode)..."

while true; do
    # Listen with a 5-second timeout (-w 5) to prevent permanent stalls
    RESPONSE=$(nc -lp $PORT -w 5)
    
    if [ ! -z "$RESPONSE" ]; then
        (
            ID=$(echo "$RESPONSE" | grep -o '"candidate_id":[^,]*' | sed 's/"candidate_id"://;s/"//g')
            PILLAR=$(echo "$RESPONSE" | grep -o '"pillar":[^,]*' | sed 's/"pillar"://;s/"//g')
            sqlite3 $DB "INSERT INTO strike_candidates (candidate_id, pillar_origin, logic_state, shear_stability) VALUES ('${ID:-Generic}', '${PILLAR:-Unknown}', '1.58-bit', 0.7071);"
            echo "--- [STRIKE LOGGED: $(date '+%H:%M:%S')] ---"
        ) & # Run in background to keep the loop moving
    fi
    sleep 0.5
done
