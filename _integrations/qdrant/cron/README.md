# Weekly cron — multi-source Qdrant sync with drift detection

This folder sets up a weekly background job (macOS launchd) that runs `sync.py --all` every Sunday at 22:00 local time, then audits the registry ↔ Qdrant consistency.

## Files

| File | Role |
|---|---|
| `run-weekly-sync.sh` | Wrapper that sources `.env`, runs sync, runs verify. |
| `help.{{PROJECT_SLUG}}.qdrant-weekly-sync.plist` | launchd definition with weekly Sunday 22:00 schedule. |

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Sync OK, no drift |
| `1` | `sync.py --all` failed (see log) |
| `2` | Sync OK but drift detected between registry and Qdrant — human attention required. macOS notification fires. |

## Installation (one-time)

Both the wrapper and the plist contain `{{PROJECT_ROOT}}` and `{{PROJECT_SLUG}}` placeholders that the bootstrap replaces with your actual values. After bootstrap, install with:

```bash
# 1. Make the wrapper executable
chmod +x {{PROJECT_ROOT}}/_integrations/qdrant/cron/run-weekly-sync.sh

# 2. Copy the plist to LaunchAgents (user-level, not root)
cp {{PROJECT_ROOT}}/_integrations/qdrant/cron/help.{{PROJECT_SLUG}}.qdrant-weekly-sync.plist \
   ~/Library/LaunchAgents/

# 3. Load the job
launchctl load ~/Library/LaunchAgents/help.{{PROJECT_SLUG}}.qdrant-weekly-sync.plist

# 4. Verify registration
launchctl list | grep qdrant-weekly-sync
```

## Manual test

```bash
{{PROJECT_ROOT}}/_integrations/qdrant/cron/run-weekly-sync.sh
tail -40 {{PROJECT_ROOT}}/_integrations/qdrant/logs/cron-weekly.log
```

## Immediate trigger (after installation)

```bash
launchctl start help.{{PROJECT_SLUG}}.qdrant-weekly-sync
```

## Uninstall

```bash
launchctl unload ~/Library/LaunchAgents/help.{{PROJECT_SLUG}}.qdrant-weekly-sync.plist
rm ~/Library/LaunchAgents/help.{{PROJECT_SLUG}}.qdrant-weekly-sync.plist
```

## Linux / WSL equivalent

This wrapper is shell-agnostic so it works on any POSIX system. For Linux, replace the launchd plist with a systemd timer or a crontab entry:

```
# crontab equivalent (every Sunday at 22:00)
0 22 * * 0 /path/to/run-weekly-sync.sh
```

systemd timer example in a future version of this template.

## Monitoring

Three log files to watch:

- `logs/cron-weekly.log` — primary report (sync + verify + exit code)
- `logs/cron-weekly.stdout.log` — wrapper stdout (useful if wrapper crashes before sync)
- `logs/cron-weekly.stderr.log` — wrapper/launchd errors (PATH, .env, permissions)

Weekly Monday-morning check:

```bash
grep -E "Weekly sync|DRIFT|FAILED" {{PROJECT_ROOT}}/_integrations/qdrant/logs/cron-weekly.log | tail -10
```

Expected result:

```
Cron weekly sync — 2026-04-19T22:00:01+02:00
Weekly sync OK — no drift. End: 2026-04-19T22:12:43+02:00
```
