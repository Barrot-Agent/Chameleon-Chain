#!/data/data/com.termux/files/usr/bin/bash
# BARROT-Ω: Sovereign Bash Sentry (v5.3)

DB="barrot_sovereign.db"
TARGET_PHONE="3476160106"

# Get the starting ID so we only alert on NEW strikes
LAST_ID=$(sqlite3 "$DB" "SELECT MAX(id) FROM strike_candidates;" || echo 0)
LAST_ID=${LAST_ID:-0}

echo "[GATE] Sentry Active. Monitoring Vault from ID: $LAST_ID"

while true; do
    # Query for any new high-priority pillars (Riemann, P_vs_NP, Navier)
    NEW_STRIKES=$(sqlite3 "$DB" "SELECT id, candidate_id, pillar_origin FROM strike_candidates WHERE id > $LAST_ID AND (pillar_origin LIKE '%Riemann%' OR pillar_origin LIKE '%P_vs_NP%' OR pillar_origin LIKE '%Navier%');")

    if [ ! -z "$NEW_STRIKES" ]; then
        echo "$NEW_STRIKES" | while IFS='|' read -r ID CANDIDATE PILLAR; do
            MSG="BARROT-Ω: $PILLAR Candidate Detected! ID: $CANDIDATE"
            echo "[MATCH] Triggering Alerts for $PILLAR..."

            # 1. Android Notification
            termux-notification -t "Sovereign Strike" -c "$MSG" --priority high
            
            # 2. SMS Failover to Brooklyn Core
            termux-sms-send -n "$TARGET_PHONE" "$MSG"
            
            # 3. Auditory Pulse (880Hz)
            termux-beep -f 880 -d 500
            
            # Update LAST_ID to the one we just processed
            LAST_ID=$ID
        done
    fi
    sleep 2
done
