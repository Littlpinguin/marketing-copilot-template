#!/usr/bin/env python3
"""
PostToolUse hook: rappelle Claude d'invoquer le skill brand-check-n2 après
toute écriture ou édition de contenu dans un dossier de production N2.

Déclencheurs :
- Outils Write ou Edit
- Chemin contenant /03-social-media/, /04-email/, /05-web-content/,
  /07-events/ ou /09-blog-seo/
- Extension .md ou .html

Exclusions :
- CLAUDE.md, README.md, STATUS.md (méta)
- Sous-dossiers templates/, examples/, archives/, drafts/wip/ (références)
- Fichiers techniques (.py, .js, .sh, .json, etc.)
"""

import json
import os
import re
import sys

PRODUCTION_FOLDERS = (
    "/03-social-media/",
    "/04-email/",
    "/05-web-content/",
    "/07-events/",
    "/09-blog-seo/",
)

EXCLUDED_SUBPATHS = (
    "/templates/",
    "/examples/",
    "/archives/",
    "/drafts/wip/",
    "/wip/",
)

META_FILENAMES = ("CLAUDE.md", "README.md", "STATUS.md", "TODO.md", ".gitignore")


def should_trigger(file_path: str) -> bool:
    if not file_path:
        return False

    basename = os.path.basename(file_path)
    if basename in META_FILENAMES:
        return False

    if not re.search(r"\.(md|html|mdx)$", file_path, re.IGNORECASE):
        return False

    if not any(folder in file_path for folder in PRODUCTION_FOLDERS):
        return False

    if any(sub in file_path for sub in EXCLUDED_SUBPATHS):
        return False

    if "[WIP]" in basename or "[wip]" in basename:
        return False

    return True


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_input = payload.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""

    if not should_trigger(file_path):
        return 0

    reminder = (
        "🎯 BRAND CHECK REQUIRED\n\n"
        f"Tu viens d'écrire ou d'éditer `{os.path.basename(file_path)}` "
        f"dans un dossier de production N2 (`{file_path}`).\n\n"
        "**AVANT de rendre la main à l'utilisateur**, tu DOIS invoquer le skill "
        "`brand-check-n2` via l'outil Skill pour valider ce draft contre les "
        "standards de marque N2 (filtre 5 points : vocabulaire, ton, preuve, "
        "audience, visuel).\n\n"
        "Applique toutes les corrections 🟠 avant livraison. Remonte tout 🔴 à "
        "l'utilisateur. N'annonce PAS que c'est validé tant que brand-check-n2 "
        "n'a pas retourné ✅ PASS. Cette étape est non-négociable."
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": reminder,
        }
    }

    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
