#!/data/data/com.termux/files/usr/bin/bash
# BARROT-Ω: Live Sovereign Dashboard

# Ensure we have the latest snapshot visible
while true; do
    clear
    echo "--- [BARROT-Ω: LIVE SOVEREIGN PULSE] ---"
    echo "STABILITY: 0.7071 SHEAR | LOGIC: 1.58-BIT"
    echo "----------------------------------------"
    ./v_query.sh
    echo ""
    echo "[SYSTEM] Refreshing in 10s... (Ctrl+C to Exit)"
    sleep 10
done
