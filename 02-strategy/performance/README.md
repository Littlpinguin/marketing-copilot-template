# performance/ — snapshots mensuels de mesure

Un dossier par mois : `performance/AAAA-MM/data.json`, au schéma défini dans `../../11-reporting/dashboard/data-schema.md`.

- **Alimenté par** : la skill `performance-report` (module `reporting` actif) ou relevé manuel.
- **Consommé par** : la révision trimestrielle de `../objectifs.md`, la clôture des briefs (`../briefs/`), et le dashboard `11-reporting/` (qui copie ici les snapshots validés vers `dashboard/data/`).
- **Règle** : aucun chiffre sans source (chaque valeur pointe vers son outil d'origine) ; jamais de données client réelles commitées dans le repo template.
