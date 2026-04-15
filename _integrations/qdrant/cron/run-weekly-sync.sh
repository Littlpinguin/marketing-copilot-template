#!/bin/bash
# run-weekly-sync.sh – wrapper exécuté par launchd pour la sync multi-sources hebdomadaire.
#
# Lance `sync.py --all` pour rafraîchir toutes les sources actives, puis enchaîne
# avec `sync.py --verify` pour détecter toute dérive entre le registry local et Qdrant.
#
# Exit codes :
#   0  = sync OK, pas de drift
#   1  = sync.py --all a échoué
#   2  = sync OK mais drift détecté (attention humaine requise)
#
# IMPORTANT : ajuster PROJECT_ROOT ci-dessous pour pointer sur ton propre projet.

set -uo pipefail

# ADJUST THIS to your actual project path
PROJECT_ROOT="{{PROJECT_ROOT}}"
QDRANT_DIR="$PROJECT_ROOT/_integrations/qdrant"
LOG_DIR="$QDRANT_DIR/logs"
LOG_FILE="$LOG_DIR/cron-weekly.log"

mkdir -p "$LOG_DIR"

# Load environment variables
set -a
# shellcheck disable=SC1091
source "$PROJECT_ROOT/.env"
set +a

# Fallback PATH so launchd can find python3
export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:$PATH"

cd "$QDRANT_DIR"

STARTED_AT="$(date -Iseconds)"
{
    echo "======================================"
    echo "Cron weekly sync — $STARTED_AT"
    echo "======================================"
} >> "$LOG_FILE"

# Phase 1: multi-source sync
python3 sync.py --all >> "$LOG_FILE" 2>&1
SYNC_EXIT=$?

if [ $SYNC_EXIT -ne 0 ]; then
    {
        echo ""
        echo "sync.py --all FAILED with exit code $SYNC_EXIT"
        echo "End: $(date -Iseconds)"
        echo ""
    } >> "$LOG_FILE"
    exit 1
fi

# Phase 2: drift check
{
    echo ""
    echo "--- Drift check ---"
} >> "$LOG_FILE"

VERIFY_OUTPUT="$(python3 sync.py --verify 2>&1)"
echo "$VERIFY_OUTPUT" >> "$LOG_FILE"

if echo "$VERIFY_OUTPUT" | grep -q "DRIFT"; then
    {
        echo ""
        echo "DRIFT DETECTED between registry and Qdrant."
        echo "Human attention required. Run: python3 sync.py --verify"
        echo "End: $(date -Iseconds)"
        echo ""
    } >> "$LOG_FILE"
    osascript -e 'display notification "Qdrant registry drift detected. Check cron-weekly.log." with title "Marketing Copilot Weekly Sync"' 2>/dev/null || true
    exit 2
fi

{
    echo ""
    echo "Weekly sync OK — no drift. End: $(date -Iseconds)"
    echo ""
} >> "$LOG_FILE"

exit 0
