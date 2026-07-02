# Screenshots — état avant lancement

7 des 8 captures sont produites (Playwright, Chrome headless, viewport 1440×900 @2x, redimensionnées à 1600 px de large, données fictives Meridian Conseil uniquement) :

| Fichier | État | Note |
|---|---|---|
| `deck-catalogue-overview.png` | ✅ | Overview 7 familles (touche `O`), 251 KB |
| `deck-catalogue-slide.png` | ✅ | Slide 7 (chiffre-choc), cadre 16:9, ~1 MB → compresser |
| `dashboard.png` | ✅ | Démo `11-reporting/dashboard/demo/` (juin 2026, KPI + deltas + graphiques), 206 KB |
| `landing-demo-b2b.png` | ✅ | ~1 MB → compresser |
| `landing-webinar.png` | ✅ | ~1,1 MB → compresser |
| `landing-waitlist.png` | ✅ | ~1,2 MB → compresser |
| `lead-magnet-roi.png` | ✅ | Sliders déplacés, carte résultat visible, ~0,9 MB → compresser |

## Restant avant commit

### 1. `wizard-terminal.png` — à capturer À LA MAIN

- Clone frais dans un dossier jetable, `claude`, puis taper `/start-copilot`.
- Capturer le message de bienvenue/préflight (le moment où le copilot explique le flux 30–60 min).
- Recadrer sur la fenêtre du terminal ; vérifier qu'aucun chemin personnel, email ou chaîne façon clé API n'est visible.

### 2. Passe de compression sur les 5 fichiers > 400 KB

`squoosh.app` ou `tinypng` (pngquant local fait aussi l'affaire) sur `deck-catalogue-slide`, `landing-*`, `lead-magnet-roi` — cible < 400 KB par image, qualité visuelle inchangée. `dashboard.png` et `deck-catalogue-overview.png` sont déjà sous la cible.

### 3. Vérification finale

`ls docs/launch/screenshots/*.png` doit lister les 8 fichiers, puis relire la preview GitHub du README pour confirmer qu'aucune image n'est cassée. Optionnel à fort impact : un GIF de 8–12 s de navigation du catalogue (flèches + `O`) à substituer en héro du README plus tard.
