#!/data/data/com.termux/files/usr/bin/bash
# BARROT-Ω: Sovereign Vault Observer

DB="barrot_sovereign.db"

echo "--- [BARROT-Ω VAULT SNAPSHOT: $(date)] ---"
echo "ID | TIMESTAMP           | CANDIDATE_ID       | PILLAR    | SHEAR"
echo "------------------------------------------------------------------"

# Query the last 5 entries
sqlite3 $DB "SELECT id, timestamp, candidate_id, pillar_origin, shear_stability FROM strike_candidates ORDER BY id DESC LIMIT 5;" | sed 's/|/  |  /g'

echo "------------------------------------------------------------------"
echo "LOGIC: 1.58-bit Ternary | STATUS: ANCHORED"
