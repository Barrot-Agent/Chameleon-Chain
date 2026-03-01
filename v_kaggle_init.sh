#!/data/data/com.termux/files/usr/bin/bash
KAG_USER="Scribedpengenius"
KAG_KEY="KGAT_c9549bb514216a064954c8634684a69a"
mkdir -p ~/.config/kaggle
echo "{\"username\":\"$KAG_USER\",\"key\":\"$KAG_KEY\"}" > ~/.config/kaggle/kaggle.json
chmod 600 ~/.config/kaggle/kaggle.json
echo "[INIT] Identity Anchored."
