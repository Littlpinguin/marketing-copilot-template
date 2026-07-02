# Objectifs — {{COMPANY_NAME}}

> **Note d'usage.** Ce fichier est rempli une première fois pendant le wizard (`/start-copilot` → `/brand-discover`), puis **révisé à chaque début de trimestre** (mettre à jour la date ci-dessous à chaque révision). C'est le sommet de la cascade : **toute production du copilot doit pouvoir se rattacher à un objectif de ce fichier** — un brief cite un `OBJ-x`, une entrée calendrier appartient à une campagne, une campagne sert un objectif. Si un contenu ne se rattache à rien, poser la question avant de produire.

- **Trimestre en cours** : {{TRIMESTRE_EN_COURS}} (ex. T3 2026)
- **Dernière révision** : {{DATE_DERNIERE_REVISION}}
- **Validé par** : {{COMPANY_MAIN_CONTACT}}

---

## 1. Objectifs business (horizon 12 mois)

Les objectifs de l'entreprise que le marketing sert. Ils viennent de la direction, pas du marketing.

| ID | Objectif business | Horizon | Indicateur de réussite |
|---|---|---|---|
| BIZ-1 | {{OBJECTIF_BUSINESS_1}} (ex. atteindre {{CA_CIBLE}} de CA récurrent) | {{HORIZON_1}} | {{INDICATEUR_BIZ_1}} |
| BIZ-2 | {{OBJECTIF_BUSINESS_2}} (ex. signer {{NB_CLIENTS_CIBLE}} nouveaux clients sur le segment {{SEGMENT}}) | {{HORIZON_2}} | {{INDICATEUR_BIZ_2}} |
| BIZ-3 | {{OBJECTIF_BUSINESS_3}} (ex. devenir référent sur {{THEMATIQUE}} dans {{ZONE_MARCHE}}) | {{HORIZON_3}} | {{INDICATEUR_BIZ_3}} |

## 2. Objectifs marketing du trimestre (SMART)

Chaque objectif marketing est **S**pécifique, **M**esurable, **A**tteignable, **R**éaliste, **T**emporel — et sert explicitement un objectif business.

| ID | Objectif marketing SMART | Sert | Indicateur | Valeur de départ | Cible fin de trimestre | Persona principal |
|---|---|---|---|---|---|---|
| OBJ-1 | {{OBJECTIF_MKT_1}} (ex. générer {{NB_LEADS}} leads qualifiés via {{CANAL}} d'ici le {{DATE}}) | BIZ-{{N}} | {{INDICATEUR_1}} | {{VALEUR_DEPART_1}} | {{CIBLE_1}} | {{PERSONA_1}} |
| OBJ-2 | {{OBJECTIF_MKT_2}} (ex. faire passer le trafic organique de {{X}} à {{Y}} sessions/mois) | BIZ-{{N}} | {{INDICATEUR_2}} | {{VALEUR_DEPART_2}} | {{CIBLE_2}} | {{PERSONA_2}} |
| OBJ-3 | {{OBJECTIF_MKT_3}} (ex. atteindre {{NB_ABONNES}} abonnés newsletter avec ≥ {{TAUX}}% d'ouverture) | BIZ-{{N}} | {{INDICATEUR_3}} | {{VALEUR_DEPART_3}} | {{CIBLE_3}} | {{PERSONA_3}} |

> Règle : 2 à 4 objectifs marketing par trimestre, pas plus. Au-delà, rien n'est prioritaire.

## 3. Cibles par canal (KPIs chiffrés)

Déclinaison opérationnelle des objectifs marketing. Les définitions et la méthode de mesure de chaque KPI vivent dans `kpi-framework.md` ; ici, uniquement les **cibles chiffrées du trimestre**.

| Canal | KPI | Valeur actuelle | Cible trimestre | Sert | Source de mesure |
|---|---|---|---|---|---|
| LinkedIn | Impressions / mois | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{OUTIL_MESURE}} (ex. Postiz, stats natives) |
| LinkedIn | Taux d'engagement | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{OUTIL_MESURE}} |
| Newsletter | Abonnés | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{OUTIL_EMAILING}} |
| Newsletter | Taux d'ouverture / clic | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{OUTIL_EMAILING}} |
| Blog / SEO | Sessions organiques / mois | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | GA4 / Search Console |
| Blog / SEO | Positions top 10 sur mots-clés cibles | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | Search Console |
| Site web | Conversions ({{TYPE_CONVERSION}} : démo, contact, inscription…) | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | GA4 |
| Événements | Inscrits / participants par événement | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{PLATEFORME_EVENEMENTS}} |
| {{AUTRE_CANAL}} | {{KPI}} | {{VALEUR}} | {{CIBLE}} | OBJ-{{N}} | {{OUTIL_MESURE}} |

> Supprimer les lignes des canaux non activés ; n'afficher que ce qui sera réellement mesuré.

## 4. Suivi de la performance

- **Snapshots mensuels** : `performance/AAAA-MM/data.json` (schéma : `../11-reporting/dashboard/data-schema.md`), produits par la skill `performance-report` si le module `reporting` est actif — sinon, relevé manuel des chiffres dans le tableau ci-dessus.
- **Dashboard** : module `11-reporting/` (HTML mensuel aux couleurs de la marque).
- **Revue trimestrielle** : comparer les cibles de ce fichier aux snapshots, écrire le bilan dans `reports/`, puis réviser les sections 2 et 3 pour le trimestre suivant. Un objectif non atteint n'est pas reconduit tel quel : on comprend pourquoi (voir « apprentissages » des briefs dans `briefs/`) avant de re-cibler.

## Historique des révisions

| Date | Trimestre | Changements | Par |
|---|---|---|---|
| {{DATE}} | {{TRIMESTRE}} | Création initiale (wizard) | {{COMPANY_MAIN_CONTACT}} |
