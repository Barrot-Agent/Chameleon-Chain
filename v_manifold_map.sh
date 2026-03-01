#!/data/data/com.termux/files/usr/bin/bash
echo "--- [BARROT-Ω: MANIFOLD PROCESS MAP] ---"
echo "COMPONENT       | STATUS     | DETAIL"
echo "----------------------------------------"
pgrep -f "barrot_watch_zap.sh" > /dev/null && printf "%-15s | %-10s | ACTIVE\n" "Listener" "ACTIVE" || printf "%-15s | %-10s | OFFLINE\n" "Listener" "OFFLINE"
pgrep -f "v_pulse.sh" > /dev/null && printf "%-15s | %-10s | ACTIVE\n" "Dashboard" "ACTIVE" || printf "%-15s | %-10s | OFFLINE\n" "Dashboard" "OFFLINE"
echo "----------------------------------------"
