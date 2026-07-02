# Démo du dashboard — Meridian Conseil (marque fictive)

Copie de démonstration de `../template.html` avec les tokens Meridian Conseil (la marque fictive du deck-catalogue et de la galerie `05-web-content/templates/`) et 4 snapshots mensuels **100 % fictifs** (mars → juin 2026, toutes sources : GA4, Search Console, Postiz, emailing, Google Ads).

**Double-clic sur `index.html` = ça marche** : les données de démo sont embarquées dans le HTML, aucun serveur requis. Les fichiers `data/*.json` restent la référence du format des snapshots (schéma : `../data-schema.md`) et servent de fallback fetch — c'est le mode du vrai dashboard : `../template.html` charge ses données en `fetch()` et se prévisualise via un serveur HTTP (voir `../../README.md`).

Ne rien réutiliser ici pour un client réel : le vrai dashboard part de `../template.html`, personnalisé par `/brand-discover`, avec des snapshots produits par la skill `performance-report`.
