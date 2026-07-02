# Veille & intelligence marché — état de l'art 2026

> Recherche multi-sources, juillet 2026. Sources primaires 2025-2026 citées à chaque règle.
> Objectif : règles actionnables pour un agent IA qui produit une veille concurrentielle et sectorielle débouchant sur des décisions de contenu.

---

## 1. Signaux à suivre (par ordre de valeur)

### Constats sourcés

- **Pages pricing = la source la plus riche par page** : une restructuration tarifaire en dit plus sur la stratégie d'un concurrent qu'un mois de posts de blog. En B2B SaaS, la page pricing médiane change **tous les ~37 jours** (mesure IndustryLens sur 84 concurrents, 26 semaines). Sources : [Visualping, "27 Competitive Intelligence Sources Worth Monitoring"](https://visualping.io/blog/competitive-intelligence-sources), [Content Camel, "Competitive Intelligence for Sales 2026"](https://www.contentcamel.io/blog/competitive-intelligence-sales-content-2026/).
- **Vélocité des offres d'emploi = le signal le plus sous-coté** : passer de 3 à 15 postes ingénierie/mois signale un mouvement majeur (nouveau produit, levée, pivot) avant toute annonce. Source : [Visualping, "27 CI Sources"](https://visualping.io/blog/competitive-intelligence-sources).
- **Changelogs et docs API = les pages les plus honnêtes** d'un site concurrent : écrites par les ingénieurs, elles révèlent les features avant les communiqués. Source : [Visualping, "27 CI Sources"](https://visualping.io/blog/competitive-intelligence-sources).
- **Publicités concurrentes** : Meta Ad Library et Google Ads Transparency Center sont publics, gratuits, mis à jour quotidiennement — messages, offres et ciblages des concurrents à livre ouvert. Source : [Cotera, "Free Competitor Analysis Tools 2026"](https://cotera.co/articles/free-competitor-analysis-tools).

### Grille de signaux (à configurer par concurrent)

| Priorité | Signal | Où le lire | Ce qu'il révèle |
|---|---|---|---|
| 1 | Page pricing | Site (monitoring de changement) | Positionnement, cible, pression sur les marges |
| 2 | Offres d'emploi (volume + intitulés) | Careers, LinkedIn | Roadmap réelle, expansion géographique, pivot |
| 3 | Changelog / notes de version | Docs produit | Vitesse d'exécution, direction produit |
| 4 | Publicités actives | Meta Ad Library, Google Ads Transparency | Messages testés, offres, budgets relatifs |
| 5 | Contenus publiés (blog, social, events) | Site + RSS + LinkedIn | Piliers éditoriaux, angles non couverts |
| 6 | Avis clients (G2, Google, Trustpilot) | Alertes plateformes | Faiblesses exploitables, arguments de bataille |
| 7 | Actualité corporate (levées, dirigeants, presse) | Google Alerts, registres publics | Moyens et intentions |

---

## 2. Outils et sources gratuits/accessibles

| Besoin | Outil gratuit ou accessible | Source |
|---|---|---|
| Alertes news/mentions | Google Alerts (concurrents + mots-clés secteur + marque) | [Cotera 2026](https://cotera.co/articles/free-competitor-analysis-tools) |
| Changements de pages (pricing, features) | Visualping (tier gratuit) ou équivalent diff-checker | [Visualping, "Top Free CI Tools 2026"](https://visualping.io/blog/top-free-competitive-intelligence-tools) |
| Trafic et tendances concurrents | Similarweb gratuit (contrôle mensuel) | [Cotera 2026](https://cotera.co/articles/free-competitor-analysis-tools) |
| Avis | Alertes G2 / Google Business / Trustpilot | [Cotera 2026](https://cotera.co/articles/free-competitor-analysis-tools) |
| Pubs | Meta Ad Library, Google Ads Transparency Center | [Cotera 2026](https://cotera.co/articles/free-competitor-analysis-tools) |
| Signaux stratégiques | Suivi LinkedIn des pages et dirigeants concurrents | [Cotera 2026](https://cotera.co/articles/free-competitor-analysis-tools) |
| Données publiques (FR) | Pappers/societe.com (comptes, dépôts), BODACC, INPI (marques), registres sectoriels | usage standard, à croiser avec les signaux ci-dessus |
| Newsletters sectorielles | 3-5 newsletters de référence du secteur du client, listées à l'onboarding | [Visualping, "27 CI Sources"](https://visualping.io/blog/competitive-intelligence-sources) |

Contexte marché : la CI pèse **38,6 Md$ en 2025** (+13 %/an) et **60 % des équipes CI utilisent l'IA quotidiennement** (Crayon, State of CI 2025) — l'agent IA qui lit ces sources est désormais la norme, pas l'exception. Source : [Visualping, "Top Free CI Tools 2026"](https://visualping.io/blog/top-free-competitive-intelligence-tools).

---

## 3. Transformer la veille en décisions de contenu

### Constats sourcés

- **La CI ne compte que si elle change un comportement** : mesurer la veille en « rapports produits » plutôt qu'en « décisions influencées » est la voie garantie vers l'effort gaspillé. Commencer par des **questions d'intelligence explicites** (« que fait X sur le pricing ? », « quel angle personne ne couvre ? ») évite de collecter du bruit. Source : [The Growth Syndicate, "Competitor Analysis Framework"](https://www.thegrowthsyndicate.com/resources/competitor-analysis-framework).
- **Une intelligence sans propriétaire est du bruit** : un responsable, une cadence de restitution, un chemin d'escalade. Source : [Klue, "Framework for Competitive Intelligence"](https://klue.com/blog/framework-for-competitive-intelligence).
- **Win/loss** : 63 % des entreprises avec un programme formel d'interviews acheteurs augmentent leur taux de gain, 84 % après 2 ans de programme. Source : [Klue, "Competitive Battlecard Win Rate"](https://klue.com/blog/competitive-battlecard-win-rate).

### Framework signal → décision (à appliquer par l'agent)

Chaque signal retenu passe par 4 questions ; s'il ne franchit pas la Q1, il est archivé sans suite :

1. **Et alors ?** — impact concret sur le client (positionnement, prix, contenu, vente). Pas d'impact = pas de restitution.
2. **Quelle réponse ?** — 3 sorties possibles : *idée de contenu* (angle non couvert, contre-narratif, page comparateur), *ajustement stratégique* (pilier, pricing, cible), *battlecard commerciale*.
3. **Quand ?** — daté au calendrier éditorial ou au backlog, avec échéance.
4. **Qui décide ?** — l'utilisateur/client valide ; l'agent propose, ne décrète pas.

Règle de rendement : **une veille qui ne produit aucune idée de contenu datée et sourcée est un échec** (principe déjà inscrit dans la skill `veille-strategy` — confirmé par l'état de l'art : la CI se mesure aux décisions, pas aux rapports. Source : [The Growth Syndicate](https://www.thegrowthsyndicate.com/resources/competitor-analysis-framework)).

---

## 4. Fréquences pertinentes

| Cadence | Quoi | Source |
|---|---|---|
| Hebdo (15 min) | Revue des alertes ; flaguer l'actionnable. **Une cadence hebdo régulière bat un rapport trimestriel exhaustif que personne n'exploite.** | [The Growth Syndicate](https://www.thegrowthsyndicate.com/resources/competitor-analysis-framework) |
| Sous 24-48 h | Changement matériel (pricing, lancement, dirigeant) → mise à jour battlecard/positionnement. Les équipes qui actualisent leurs battlecards au moins chaque semaine ont un taux de gain compétitif **+15 %** vs cycles mensuels/trimestriels. | [Content Camel 2026](https://www.contentcamel.io/blog/competitive-intelligence-sales-content-2026/) |
| Mensuel | Synthèse : tendances, mouvements de fond, réallocation éditoriale | [Klue, "Sales Battlecards 101"](https://klue.com/blog/competitive-battlecards-101) |
| Trimestriel | Revue stratégique : paysage complet, profils concurrents, pertinence de la liste suivie (ajouts/retraits) | [Valona, "How to conduct CI step by step"](https://valonaintelligence.com/resources/blog/how-to-conduct-competitive-intelligence-and-analysis-step-by-step) |

Adapter au secteur : marchés rapides (SaaS, e-commerce) = hebdo ; marchés lents (industrie, réglementé) = mensuel suffit. Source : [Battlecard, "What is Competitive Intelligence 2025"](https://www.battlecard.com/blog/what-is-competitive-intelligence-and-why-it-matters-in-2025).

---

## 5. Pièges documentés

| # | Piège | Parade (règle agent) | Source |
|---|---|---|---|
| P1 | **Biais de confirmation** : ne retenir que ce qui valide la stratégie en place ; des analyses biaisées détruisent la crédibilité de toute la fonction veille. | Formuler les questions d'intelligence AVANT de collecter ; chercher activement le signal contraire (« qu'est-ce qui invaliderait notre lecture ? ») ; séparer fait observé et interprétation dans la synthèse. | [Uncovered, "Confirmation Bias in Competitive Intelligence"](https://uncovered.so/blog/confirmation-bias-in-competitive-intelligence) |
| P2 | **Bruit** : tout collecter, ne rien décider. | Filtre « Et alors ? » (§3) ; croiser tout signal important avec une 2e source indépendante (dépôt légal, mouvement de capital, comportement contractuel) avant de le faire entrer dans une décision. | [SafeGraph, "Competitive Intelligence Guide"](https://www.safegraph.com/guides/competitive-intelligence/) |
| P3 | **Rapport-fleuve trimestriel** que personne ne lit ni n'exploite. | Cadence courte + restitution courte : le livrable hebdo tient en une page, chaque item porte une action proposée. | [The Growth Syndicate](https://www.thegrowthsyndicate.com/resources/competitor-analysis-framework) |
| P4 | **Obsession concurrents = stratégie réactive** : copier les mouvements des autres au lieu de servir sa cible. | Plafonner la part « concurrents » de la veille ; garder les niveaux secteur/tendances/clients comme contrepoids ; toute idée de contenu issue de la veille doit répondre à un besoin de l'audience, pas seulement « faire comme X ». | [The CX Lead, "Master Competitive Intelligence Analysis"](https://thecxlead.com/cx-strategy/competitive-intelligence-analysis/) |
| P5 | **Signaux périmés** : battlecard trimestrielle vs pricing concurrent qui change tous les 37 jours. | Horodater chaque fait ; règle de péremption (un signal pricing > 60 jours doit être revérifié avant usage dans un livrable client). | [Content Camel 2026](https://www.contentcamel.io/blog/competitive-intelligence-sales-content-2026/) |

---

## Chiffres clés (datés)

| Chiffre | Valeur | Date | Source |
|---|---|---|---|
| Fréquence médiane de changement d'une page pricing B2B SaaS | ~37 jours | 2025-2026 (IndustryLens, 84 concurrents / 26 semaines) | [Content Camel](https://www.contentcamel.io/blog/competitive-intelligence-sales-content-2026/) |
| Lift de taux de gain avec battlecards mises à jour ≥ hebdo | +15 % | 2025-2026 | [Content Camel](https://www.contentcamel.io/blog/competitive-intelligence-sales-content-2026/) |
| Programmes win/loss formels → hausse du taux de gain | 63 % (84 % après 2 ans) | 2025 | [Klue](https://klue.com/blog/competitive-battlecard-win-rate) |
| Marché de la competitive intelligence | 38,6 Md$ (+~13 %/an) | 2025 | [Visualping](https://visualping.io/blog/top-free-competitive-intelligence-tools) |
| Équipes CI utilisant l'IA quotidiennement | 60 % | 2025 (Crayon, State of CI) | [Visualping](https://visualping.io/blog/top-free-competitive-intelligence-tools) |
| Organisations utilisant le win/loss pour la roadmap produit | 75 % | 2025 | [Klue](https://klue.com/blog/competitive-battlecard-win-rate) |

---

## À intégrer dans les skills

### skill `veille-strategy`
- **Grille de signaux §1 comme checklist du niveau 1 (concurrents)** : pricing, jobs, changelog, pubs (Ad Libraries), contenus, avis, corporate — dans cet ordre de valeur. Ajouter la vélocité d'embauche et les bibliothèques publicitaires, absentes du tableau actuel.
- **Framework signal → décision §3** : chaque item de la synthèse hebdo/mensuelle porte les 4 champs (impact, réponse proposée, échéance, décideur). Archiver sans restitution ce qui échoue au « Et alors ? ».
- **Anti-biais P1** : ajouter au workflow une étape « signal contraire » obligatoire (chercher au moins un fait qui contredit la lecture dominante avant de conclure) et séparer typographiquement fait/interprétation dans la synthèse.
- **Péremption P5** : horodater chaque fait dans `02-strategy/veille/` ; revalider tout signal pricing > 60 jours avant réutilisation.
- **Cadences §4** : caler la config `cadence` du wizard sur la vitesse du secteur (weekly pour SaaS/e-commerce, monthly pour secteurs lents) et ajouter un déclencheur hors-cycle « changement matériel sous 48 h ».

### skill `content-strategy`
- Les idées issues de la veille arrivent au calendrier avec leur source et leur angle différenciant (« angle non couvert par X et Y ») — appliquer P4 : rejeter toute proposition dont la seule justification est « le concurrent le fait ».
- Utiliser la veille pour l'audit d'équilibre : les contenus concurrents cartographiés révèlent les trous de couverture à prioriser dans les piliers.

### skill `seo`
- Alimenter les briefs avec la veille : pages comparateur/alternatives déclenchées par les changements pricing des concurrents (signal n°1), clusters construits sur les angles non couverts identifiés au niveau 3.

### skill `performance-report`
- Ajouter une section « contexte concurrentiel » optionnelle au rapport mensuel : 2-3 mouvements marquants du mois (sourcés, datés) pour expliquer les variations de performance (ex. campagne paid concurrente vs hausse des CPC).
