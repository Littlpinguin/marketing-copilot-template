# Inventaire des livrables — {{COMPANY_NAME}}

> Fichier maintenu par la skill `inventory`. Ne pas éditer à la main ; lancer une reconstruction en cas de doute.
> Dernière mise à jour : — (aucun livrable indexé — lancer la skill `inventory` en mode reconstruction après les premières productions)

| Date | Canal | Type | Sujet | Chemin | Statut |
|---|---|---|---|---|---|

## Note d'usage

- **Rôle** : index unique de TOUS les livrables produits par le cockpit (posts, carrousels, emails, slides, pages, images). C'est la mémoire de production du repo — **toute skill de production le consulte avant de créer** (anti-répétition), et la skill `inventory` y ajoute une ligne après chaque livrable validé.
- **Tri** : du plus récent au plus ancien (nouvelle ligne en tête de tableau).
- **Date** : date de création du livrable (`YYYY-MM-DD`), pas la date d'indexation.
- **Canal** : `linkedin`, `discord`, `whatsapp`, `newsletter`, `email-promo`, `web`, `blog`, `event`, `slides`, `visuel`.
- **Type** : `post`, `carrousel`, `email`, `article`, `landing`, `deck`, `image`, `plan-comm`.
- **Sujet** : 5-10 mots, assez précis pour détecter un doublon à la lecture.
- **Chemin** : relatif à la racine du repo.
- **Statut** : `brouillon`, `validé`, `publié`, `archivé` — mettre à jour la ligne existante à chaque changement de statut, ne jamais dupliquer.

Format complet et modes (reconstruction / incrément) : voir `.claude/skills/inventory/SKILL.md`.
