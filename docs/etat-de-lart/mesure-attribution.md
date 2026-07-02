# Mesure & attribution marketing PME — état de l'art 2026

> Recherche multi-sources, juillet 2026. Sources primaires 2025-2026 citées à chaque règle.
> Objectif : règles actionnables pour un agent IA qui collecte, analyse et restitue la performance marketing d'une PME.

---

## 1. KPIs qui comptent par canal (au-delà des vanity metrics)

### Constats sourcés

- En GA4, privilégier **sessions engagées et taux d'engagement** plutôt que le total de sessions ; limiter les dashboards à **10-15 métriques** max pour éviter la noyade. Sources : [Swydo, "Key GA4 Metrics to Track in 2025"](https://www.swydo.com/blog/google-analytics-4-metrics/), [1ClickReport, "GA4 Dashboard Best Practices 2025"](https://www.1clickreport.com/blog/ga4-dashboard-best-practices).
- Côté Search Console, les 4 KPIs de base restent **clics, impressions, position moyenne, CTR** — mais les impressions gagnent un rôle nouveau : elles capturent la visibilité dans les AI Overviews même sans clic. Source : [Data Bloo, "Google Search Console KPIs 2025"](https://www.databloo.com/blog/google-search-console-kpis/).
- Le rapport client doit être cadré par **l'objectif business, pas la métrique marketing** (« réduire le CAC de 15 % », pas « +12 % d'impressions »). Source : [Swydo, "Client Reporting Best Practices"](https://www.swydo.com/blog/client-reporting-best-practices/).

### Grille de référence par canal (PME)

| Canal | KPI de pilotage (décision) | KPI de contexte | Vanity à bannir du rapport |
|---|---|---|---|
| SEO / blog | Leads ou conversions organiques, clics GSC sur requêtes non-marque | Impressions (visibilité IA incluse), position sur requêtes cibles | Position moyenne globale, nombre d'articles publiés |
| Social organique | Clics sortants, leads attribués + auto-déclarés | Taux d'engagement par post, croissance abonnés qualifiés | Impressions totales, likes |
| Email | Taux de clic, conversions, croissance nette de liste | Taux d'ouverture (indicatif seulement depuis Apple MPP), désabonnements | Volume d'envois |
| Paid | CPA / ROAS par campagne, part de budget sur mots-clés marque vs non-marque | CTR, quality score | Impressions, portée |
| Site | Sessions engagées, taux de conversion par source, key events GA4 | Pages/session sur les pages d'argent | Sessions totales, pages vues brutes |

Règle transversale : **5 à 7 métriques liées aux objectifs du client par rapport** — pas plus. Source : [AgencyAnalytics, "20 Client Reporting Tips"](https://agencyanalytics.com/blog/client-reporting-tips).

---

## 2. Attribution réaliste post-cookies

### Constats sourcés

- La couverture d'identité utilisable est tombée à **30-60 %** (contre 90 %+ à l'ère cookie) : tout modèle multi-touch « au clic » est structurellement incomplet. Source : [Digital Applied, "Marketing Attribution Statistics 2026"](https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch).
- Le standard 2026 est la **triangulation** : attribution logicielle (tendances tactiques) + **attribution auto-déclarée** (« Comment nous avez-vous connus ? » — la vérité mémorisée par l'acheteur) + **MMM léger** (allocation budgétaire). L'auto-déclaré révèle un écart allant jusqu'à 90 % avec le tracking logiciel seul. Sources : [Digital Applied, "MMM vs Attribution Playbook 2026"](https://www.digitalapplied.com/blog/marketing-mix-modeling-2026-mmm-vs-attribution-playbook), [Layerfive, "Marketing Attribution Guide 2026"](https://layerfive.com/blog/marketing-attribution-guide-2026/).
- Le MMM se démocratise : **46,9 % des marketeurs US prévoient d'y investir davantage** et 27,6 % le citent comme la méthode la plus fiable (enquête EMARKETER/TransUnion) ; des outils open source (Meta Robyn, Google Meridian) suppriment la barrière de coût. Source : [Digital Applied, "MMM 2026"](https://www.digitalapplied.com/blog/marketing-mix-modeling-2026-mmm-vs-attribution-playbook).

### Règles vérifiées (à appliquer par l'agent)

| # | Règle | Source |
|---|---|---|
| R1 | **Modèle par défaut PME : last non-direct click GA4, assumé et documenté** — simple, défendable, comparable dans le temps. Ne jamais présenter un modèle multi-touch data-driven comme « la vérité » avec une couverture identitaire à 30-60 %. | [Digital Applied 2026](https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch) |
| R2 | **Champ « Comment nous avez-vous connus ? » obligatoire** sur tout formulaire de lead/commande (texte libre + options fermées incluant « recommandation », « message privé/Slack/WhatsApp », « podcast/newsletter », « ChatGPT/IA »). Croiser chaque mois avec l'attribution GA4. | [Layerfive 2026](https://layerfive.com/blog/marketing-attribution-guide-2026/), [Oktopost](https://www.oktopost.com/blog/dark-social-in-b2b-marketing/) |
| R3 | **MMM light seulement au-delà d'un seuil** : réserver la modélisation (Robyn/Meridian ou régression simple sur 18-24 mois de données hebdo) aux clients avec ≥3 canaux payants significatifs. En dessous, triangulation R1+R2 suffit. | [Digital Applied 2026](https://www.digitalapplied.com/blog/marketing-mix-modeling-2026-mmm-vs-attribution-playbook) |
| R4 | **Toujours réconcilier les 3 vues** (tracking, auto-déclaré, tendance) dans l'analyse mensuelle et signaler les divergences plutôt que de les masquer. | [Digital Applied 2026](https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch) |

### Conventions UTM (prérequis de toute attribution)

| # | Règle | Source |
|---|---|---|
| R5 | **Tout en minuscules** (les UTM sont case-sensitive : `Facebook` ≠ `facebook` = doublons de sources). | [Improvado, "UTM Naming Conventions"](https://improvado.io/blog/utm-naming-conventions) |
| R6 | **Taxonomie fermée** : `utm_source` = plateforme (`facebook`, `google`, `newsletter`), `utm_medium` = canal normalisé (`paid-social`, `email`, `cpc`, `organic-social`), `utm_campaign` = format structuré `[année]-[trimestre ou mois]-[initiative]`. Tirets pour les multi-mots. | [Uplifter, "UTM Governance & Taxonomy"](https://uplifter.ai/article/what-is-the-best-practice-for-utm-management) |
| R7 | **Registre central + création contrôlée** : un document unique liste les valeurs approuvées ; les liens se créent via un builder à listes fermées, jamais à la main. Audit trimestriel : exporter les valeurs distinctes de GA4, flaguer tout ce qui n'est pas dans la taxonomie. | [Prooflytics, "UTM Governance Guide"](https://prooflytics.io/blog/utm-governance-guide) |
| R8 | **Jamais d'UTM sur les liens internes** (ça écrase la session source d'origine). | [UTM.io, "UTM Parameters Best Practices"](https://web.utm.io/blog/utm-parameters-best-practices/) |

---

## 3. GA4 + Search Console : usage efficace

| # | Règle | Source |
|---|---|---|
| R9 | **Lier GA4 ↔ Search Console** (et GA4 ↔ Ads le cas échéant) dès le setup : c'est le seul moyen de croiser requêtes, pages d'atterrissage et conversions. | [Munalytics, "GA4 for Small Business 2025"](https://munalytics.com/ga4-for-small-business/) |
| R10 | **Définir les key events (conversions) avant de reporter quoi que ce soit** : lead, achat, prise de rendez-vous, inscription newsletter. Un rapport sans conversions configurées est un rapport de vanity metrics. | [Codefixer, "GA4 Best Practices 2025"](https://www.codefixer.com/blog/google-analytics-best-practices/) |
| R11 | **Lire GSC en 3 découpes systématiques** : requêtes marque vs non-marque, pages « d'argent » vs blog, et delta impressions vs delta clics (un écart croissant = absorption par AI Overviews, pas une perte de ranking). | [Data Bloo 2025](https://www.databloo.com/blog/google-search-console-kpis/), [Ahrefs 2025](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/) |
| R12 | **Explorer avec les rapports standards, décider avec des explorations ciblées** (funnel, cohortes) — et utiliser les métriques prédictives GA4 (probabilité d'achat/churn) seulement si le volume d'événements les rend fiables. | [Swydo 2025](https://www.swydo.com/blog/google-analytics-4-metrics/) |

---

## 4. Dark social : part et estimation

- **~84 % du partage de contenu B2B** se fait dans des canaux intraçables (messageries, Slack, email transféré) ; en B2B, **70-80 % du parcours d'achat** se déroule dans le « dark funnel ». Sources : [Intent Amplify, "Dark Social: 84% of Sharing"](https://intentamplify.com/blog/dark-social/), [Geisheker, "Dark Funnel & Dark Social 2026"](https://www.geisheker.com/is-marketing-attribution-dead-dark-funnel-dark-social/).
- Ordre de grandeur défendable : **20-40 % du pipeline** provient de sources dark social non visibles dans l'analytics. Source : [Chief Content Marketer, "Dark Social Is Eating Your Pipeline"](https://chiefcontentmarketer.com/dark-social-demand-generation-pipeline/).

### Comment l'estimer (méthode agent)

1. **Proxy analytics** : traiter le trafic `direct` sur des URLs profondes (pas la home) comme du dark social probable. Source : [Cognism, "Inside Out of Dark Social"](https://www.cognism.com/blog/inside-out-of-dark-social).
2. **Auto-déclaré** (R2) : les réponses « recommandation / message privé / bouche-à-oreille » du champ « Comment nous avez-vous connus ? » donnent la part réelle mémorisée.
3. **Écart tracking vs auto-déclaré** : présenter chaque mois la part « non attribuable par le tracking » comme une ligne à part entière du rapport — jamais la fondre dans « direct ».

---

## 5. Présenter les résultats à un client (reporting)

### Constats sourcés

- **Près de la moitié des clients d'agences sont insatisfaits des rapports** reçus ; les facteurs de rétention n°1 sont la relation (81 %) et la communication (67 %). Source : [Swydo, "Client Reporting Best Practices" / 2025 Marketing Agency Benchmarks](https://www.swydo.com/blog/client-reporting-best-practices/).
- **65 % des agences reportent mensuellement** — cadence qui laisse aux campagnes le temps de se normaliser. Source : [AgencyAnalytics, "Why Client Reporting Is Important"](https://agencyanalytics.com/client-reporting-guide/why-is-client-reporting-important).

### Règles vérifiées

| # | Règle | Source |
|---|---|---|
| R13 | **Structure narrative fixe** : 1) résumé exécutif en langage business (3-5 phrases), 2) les 5-7 KPIs vs objectif, 3) pourquoi ça a bougé (analyse), 4) ce qu'on fait le mois prochain (actions). Un rapport sans action item est raté. | [AgencyAnalytics 2025](https://agencyanalytics.com/blog/client-reporting-tips) |
| R14 | **Commenter le « pourquoi », pas le « quoi »** : le client voit que le trafic a baissé ; la valeur est dans la cause (saisonnalité, AI Overviews, update Google) et la réponse apportée. | [Swydo 2025](https://www.swydo.com/blog/client-reporting-best-practices/) |
| R15 | **Cadrer chaque KPI par l'objectif business du client** défini en onboarding, et rappeler cet objectif en tête de rapport. | [Swydo 2025](https://www.swydo.com/blog/client-reporting-best-practices/) |
| R16 | **Annoncer les mauvaises nouvelles soi-même, avec le diagnostic et le plan** — la transparence est un facteur de rétention mesuré (26 %). | [Swydo/Benchmarks 2025](https://www.swydo.com/blog/client-reporting-best-practices/) |

---

## Chiffres clés (datés)

| Chiffre | Valeur | Date | Source |
|---|---|---|---|
| Couverture d'identité utilisable post-cookies | 30-60 % (vs 90 %+ avant) | 2026 | [Digital Applied](https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch) |
| Marketeurs US prévoyant d'investir plus en MMM | 46,9 % | 2025-2026 (EMARKETER/TransUnion) | [Digital Applied](https://www.digitalapplied.com/blog/marketing-mix-modeling-2026-mmm-vs-attribution-playbook) |
| Écart tracking logiciel vs attribution auto-déclarée | jusqu'à 90 % | 2026 | [Digital Applied](https://www.digitalapplied.com/blog/marketing-attribution-statistics-2026-multi-touch) |
| Partage B2B dans des canaux intraçables | ~84 % | 2025 | [Intent Amplify](https://intentamplify.com/blog/dark-social/) |
| Part du pipeline issue du dark social | 20-40 % | 2025-2026 | [Chief Content Marketer](https://chiefcontentmarketer.com/dark-social-demand-generation-pipeline/) |
| Clients insatisfaits des rapports d'agence | ~50 % | 2025 | [Swydo](https://www.swydo.com/blog/client-reporting-best-practices/) |
| Agences reportant en cadence mensuelle | 65 % | 2025 | [AgencyAnalytics](https://agencyanalytics.com/client-reporting-guide/why-is-client-reporting-important) |
| Métriques max par dashboard / par rapport | 10-15 / 5-7 | 2025 | [1ClickReport](https://www.1clickreport.com/blog/ga4-dashboard-best-practices), [AgencyAnalytics](https://agencyanalytics.com/blog/client-reporting-tips) |

---

## À intégrer dans les skills

### skill `performance-report`
- Imposer la structure narrative R13 dans `analyse.md` (résumé business → KPIs vs objectif → causes → actions) et plafonner le dashboard à 5-7 KPIs de pilotage (grille §1) ; reléguer le reste en annexe du `data.json`.
- Ajouter au snapshot mensuel : la découpe GSC marque/non-marque et le delta impressions vs clics (R11) avec interprétation AI Overviews automatique ; une ligne « part non attribuable / dark social » (§4) alimentée par le champ auto-déclaré ; le canal AI referrals.
- Documenter dans le rapport le modèle d'attribution utilisé (R1) — une note de bas de page fixe « attribution : last non-direct click GA4, complétée par l'auto-déclaré ».
- Ajouter R16 : quand un KPI est en baisse, l'analyse doit contenir cause + plan, jamais le chiffre seul.

### skill `copilot-setup` (wizard) — via les conventions du template
- Le setup doit générer un **registre UTM** (R5-R8) dans `02-strategy/` avec taxonomie fermée pré-remplie par canal, et vérifier la liaison GA4↔GSC et la définition des key events (R9-R10) avant d'activer le reporting.
- Ajouter à la checklist d'onboarding : champ « Comment nous avez-vous connus ? » sur les formulaires du client (R2) — prérequis déclaré de l'attribution.

### skill `content-strategy`
- Les objectifs de contenu fixés au calendrier doivent référencer les KPIs de pilotage de la grille §1 (leads, sessions engagées, clics non-marque) — jamais impressions ou volume publié comme objectif.

### skill `veille-strategy`
- Le niveau 4 (e-réputation) alimente l'estimation dark social : mentions non liées (podcasts, newsletters tierces, communautés) à consigner comme « touchpoints invisibles » et à rapprocher des réponses auto-déclarées dans le rapport mensuel.
