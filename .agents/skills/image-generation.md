---
name: image-generation
description: "Génère des visuels conformes à la marque {{COMPANY_NAME}} via Google Gemini (nano-banana-pro / gemini-3-pro-image-preview). Chaque prompt utilisateur est automatiquement préfixé avec les guidelines du style guide (palette, typo, style illustratif, interdits visuels)."
---

# image-generation – Visuels brand-compliant via Gemini

Tu génères des visuels (hero images, bannières, illustrations, carrousels, visuels sociaux) pour {{COMPANY_NAME}} en appelant l'API Gemini `gemini-3-pro-image-preview` (alias "nano-banana-pro"). Ton rôle : **ne jamais faire une requête brute**. Tu injectes systématiquement les guidelines de marque dans chaque prompt pour garantir la cohérence visuelle.

## Prérequis

- **Variable d'environnement** : `GOOGLE_AI_API_KEY` dans `.env`
- **Modèle** : `GOOGLE_AI_IMAGE_MODEL` dans `.env` (par défaut `gemini-3-pro-image-preview`)
- **Brand source** : `01-brand/style-guide.md` doit exister et contenir les sections palette, typographie, style illustratif, et interdits visuels
- **Répertoire de sortie** : `06-graphic-design/outputs/` doit exister

## Workflow à suivre

### 1. Lire le style guide
Avant toute génération, lire `01-brand/style-guide.md` et extraire :
- **Palette couleurs** : primary, accent, dark, light, gradient signature
- **Typographie** : police principale, poids utilisés
- **Style illustratif** : flat / line art / isométrique / photo-realistic / etc.
- **Éléments mandatoires** : logo, gradient, watermark si applicable
- **Interdits visuels** : photos stock, handshakes, post-its, bureaux génériques, etc.

### 2. Comprendre la demande utilisateur
L'utilisateur décrit ce qu'il veut en langage naturel :

> "Une hero image pour notre landing page sur l'IA pour les PME, format 16:9, sujet : une métaphore de transformation progressive"

Extraire :
- **Format** : aspect ratio demandé (square / 16:9 / 9:16 / 4:5 / banner)
- **Usage** : où sera utilisé (LinkedIn cover, hero web, post social, infographie)
- **Sujet** : description du contenu visuel
- **Contraintes spécifiques** : texte à inclure, éléments précis

### 3. Construire le prompt final

Le prompt envoyé à Gemini est construit par concaténation structurée :

```
[CONTRAINTES DE MARQUE — NON NÉGOCIABLES]
- Color palette: primary {{BRAND_COLOR_PRIMARY}}, accent {{BRAND_COLOR_ACCENT}}, dark {{BRAND_COLOR_DARK}}, light background {{BRAND_COLOR_LIGHT}}
- Signature gradient: {{BRAND_GRADIENT}}
- Typography (if any text in image): {{BRAND_FONT_PRIMARY}}
- Illustration style: {{BRAND_ILLUSTRATION_STYLE}}
- MUST include: [éléments mandatoires selon style guide]
- MUST NOT include: {{BRAND_BANNED_VISUALS}}, no stock photos, no generic office imagery, no handshakes, no post-its

[DEMANDE UTILISATEUR]
[prompt utilisateur tel quel]

[FORMAT]
Aspect ratio: [16:9 / 1:1 / etc.]
High resolution, no text watermark, suitable for [usage].
```

### 4. Appeler l'API Gemini

```python
import os, requests, base64, json
from pathlib import Path
from datetime import datetime

API_KEY = os.environ["GOOGLE_AI_API_KEY"]
MODEL = os.environ.get("GOOGLE_AI_IMAGE_MODEL", "gemini-3-pro-image-preview")

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
payload = {
    "contents": [{"parts": [{"text": full_prompt}]}],
    "generationConfig": {
        "responseModalities": ["IMAGE"],
    },
}
r = requests.post(url, params={"key": API_KEY}, json=payload, timeout=120)
```

### 5. Sauvegarder l'image et la metadata

```
06-graphic-design/outputs/
├── YYYY-MM-DD-<slug>.png            ← l'image générée
└── YYYY-MM-DD-<slug>.json           ← sidecar metadata
```

Le sidecar contient :
```json
{
  "slug": "hero-ia-pme-2026-04-15",
  "generated_at": "2026-04-15T10:30:00Z",
  "model": "gemini-3-pro-image-preview",
  "user_prompt": "Une hero image pour notre landing page sur l'IA...",
  "full_prompt_sent": "[CONTRAINTES DE MARQUE...][DEMANDE UTILISATEUR...][FORMAT...]",
  "format": "16:9",
  "usage": "landing page hero",
  "brand_guidelines_version": "01-brand/style-guide.md@HEAD"
}
```

### 6. Vérifier la conformité

Avant de livrer, inspecter visuellement le résultat et vérifier :
- ✅ Palette respectée (couleurs dominantes = primary/accent)
- ✅ Style cohérent avec {{BRAND_ILLUSTRATION_STYLE}}
- ✅ Aucun des interdits visuels
- ✅ Aspect ratio correct

Si l'image échoue sur un critère, **régénérer avec un prompt renforcé** sur le point qui a échoué. Max 3 tentatives, puis remonter à l'utilisateur.

## Règles d'usage

### Ce qui est autorisé
- Prompts directs avec description du sujet voulu
- Demande d'une série de variations (appeler 3-5 fois avec variations du prompt)
- Intégration d'éléments du contenu écrit (chiffres, citations courtes)

### Ce qui ne l'est pas
- Générer un visage reconnaissable (deep fake) sans consentement
- Générer un logo concurrent
- Reproduire un style copyrighté (artiste vivant nommé, franchise)
- Générer du contenu qui contredit la charte éditoriale

### Limites techniques de Gemini nano-banana-pro
- Texte dans l'image : peut être mal rendu, toujours vérifier l'orthographe
- Faces humaines : plausibles mais peuvent avoir des artefacts
- Logos : Gemini ne connaît pas votre logo. Si tu veux le logo dans l'image, compositer après avec un outil externe.
- Pas de négation efficace : dire "no office" peut produire un bureau. Reformuler en positif : "outdoor urban scene" marche mieux.

## Personnalisations {{COMPANY_NAME}}

{{IMAGE_GEN_SPECIFIC_RULES}}

## Exemples de prompts qui fonctionnent bien

{{IMAGE_GEN_EXAMPLES}}

## Skill associé
- `brand-check` – validation de conformité sur le sidecar metadata si doute
