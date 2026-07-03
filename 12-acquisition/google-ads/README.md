# Google Ads — mode conseil (SEA piloté depuis le cockpit)

> **Sous-module du module `acquisition`** (activer via `/modules`). Prérequis : un compte Google Ads actif, un developer token Google Ads API et le serveur MCP [mcp-google-ads](https://github.com/FGRibreau/mcp-google-ads) compilé et connecté — voir `setup.md`. Tant que le module est inactif, ignorer ce dossier.

## Le principe : un consultant SEA, pas un pilote automatique

Le cockpit se connecte au compte Google Ads **en lecture** via MCP et joue le rôle d'un consultant SEA senior : il analyse, il chiffre, il recommande, il rédige des propositions. L'exécution dans l'interface Google Ads (ou via les outils d'écriture du MCP, après validation) reste une décision humaine.

### RÈGLE DURE — non négociable

**Le cockpit analyse et recommande. Il ne modifie JAMAIS une campagne, une enchère, un mot-clé ni un budget sans validation humaine explicite, demande par demande.** Concrètement :

- Le serveur MCP est configuré en **lecture seule** par défaut (`GOOGLE_ADS_READ_ONLY=true`, voir `setup.md`).
- Toute proposition de modification est livrée sous forme de **plan écrit** (fichier dans `propositions/`), jamais appliquée directement.
- Si l'humain choisit d'appliquer via le MCP (mode écriture), chaque mutation passe par le dry-run et la confirmation en deux étapes du serveur — et une validation explicite dans la conversation. « Vas-y pour tout » ne vaut pas validation d'une mutation individuelle sur un budget.

## Ce que le cockpit fait en mode conseil

1. **Audit de compte** — structure (campagnes / groupes d'annonces / correspondances), quality score, termes de recherche réels vs mots-clés achetés, budgets gaspillés (requêtes hors cible, doublons, enchères incohérentes), annonces et extensions, cohérence des landing pages, tracking des conversions. Grille complète : skill `sea-google-ads`.
2. **Plan d'optimisation priorisé** — chaque recommandation est chiffrée (coût actuel, gain estimé) et classée impact × effort. Les quick wins d'abord.
3. **Idées et propositions de campagnes** — alignées sur `../../01-brand/` (messaging framework, voix) et `../../01-brand/personas.md` : on n'achète pas un mot-clé qui ne correspond à aucun persona. Les annonces sont rédigées avec l'étape 0 doctrine, comme tout contenu de marque.
4. **Revue mensuelle** — coût, conversions, CPA, impressions versés dans le snapshot performance (`../../02-strategy/performance/AAAA-MM/data.json`, section `google_ads`) pour le dashboard `11-reporting/`.

L'analyse des données brutes du compte (anomalies, tendances, gaspillage) est déléguée au sous-agent **`sea-analyst`** (`.claude/agents/sea-analyst.md`), qui lit le compte via MCP et rend des constats chiffrés.

## Références obligatoires

- Personas et ICP : `../../01-brand/personas.md` — le ciblage et les mots-clés découlent des personas
- Doctrine de rédaction : `../../01-brand/checklist-pre-composition.md` (étape 0) + `../../01-brand/voice.md` — une annonce est un contenu de marque
- Preuves et chiffres : `../../01-brand/messaging-framework.md` — aucun claim non sourcé dans une annonce
- Landing pages : skill `landing-page` — une campagne sans page cohérente est un budget gaspillé

## Organisation

| Fichier / dossier | Contenu |
|---|---|
| `README.md` | Ce fichier — le principe du mode conseil |
| `setup.md` | Installation et connexion du serveur MCP mcp-google-ads |
| `audits/` | Un fichier par audit de compte (créé au premier audit) |
| `propositions/` | Plans d'optimisation et propositions de campagnes en attente de validation |

## Ce que ce rôle ne fait PAS

- ❌ Modifier une campagne, un budget, une enchère ou un mot-clé sans validation humaine explicite
- ❌ Activer une campagne — même une campagne qu'il a lui-même proposée
- ❌ Inventer des chiffres de performance : tout constat cite sa donnée MCP source
- ❌ Gérer l'outreach cold email (→ `../setup-lemlist.md`) ou le SEO (→ `09-seo/`)
