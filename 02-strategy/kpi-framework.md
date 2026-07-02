# Cadre KPI — {{COMPANY_NAME}}

> **Définitions et méthode de mesure.** Les **cibles chiffrées du trimestre** vivent dans `objectifs.md` (§3) ; ici, ce que chaque KPI veut dire, où on le lit, à quelle fréquence. Le module `11-reporting/` ne mesure que ce qui est défini ici.

## KPIs suivis

| KPI | Définition exacte | Source (outil) | Fréquence de relevé | Seuil d'alerte |
|---|---|---|---|---|
| Impressions LinkedIn | {{DEFINITION}} (ex. somme des impressions des posts du mois, page + profils) | {{OUTIL}} (Postiz / stats natives) | mensuelle | {{SEUIL}} |
| Taux d'engagement LinkedIn | {{DEFINITION}} (ex. (réactions+commentaires+partages)/impressions) | {{OUTIL}} | mensuelle | {{SEUIL}} |
| Abonnés newsletter | {{DEFINITION}} (nets des désabonnements) | {{OUTIL_EMAILING}} | mensuelle | {{SEUIL}} |
| Taux d'ouverture / clic | {{DEFINITION}} | {{OUTIL_EMAILING}} | par envoi + moyenne mensuelle | {{SEUIL}} |
| Sessions organiques | {{DEFINITION}} (ex. sessions GA4 canal Organic Search) | GA4 | mensuelle | {{SEUIL}} |
| Positions SEO | {{DEFINITION}} (ex. requêtes cibles dans le top 10) | Search Console | mensuelle | {{SEUIL}} |
| Conversions site | {{DEFINITION}} ({{TYPE_CONVERSION}} : démo, contact, inscription…) | GA4 (événement `{{EVENEMENT_GA4}}`) | mensuelle | {{SEUIL}} |
| Leads qualifiés | {{DEFINITION}} (critères de qualification : {{CRITERES}}) | {{CRM_OU_MANUEL}} | mensuelle | {{SEUIL}} |
| {{KPI_METIER}} | {{DEFINITION}} | {{OUTIL}} | {{FREQUENCE}} | {{SEUIL}} |

> Supprimer les lignes des canaux non activés. Chaque KPI relevé doit pointer vers son outil d'origine — aucun chiffre sans source.

## Conventions UTM

Obligatoires sur tout lien sortant publié (règle du calendrier) — c'est ce qui permet d'attribuer les conversions aux campagnes :

- `utm_source` = canal (`linkedin`, `newsletter`, `discord`, …)
- `utm_medium` = type (`social`, `email`, `event`, …)
- `utm_campaign` = slug du brief de campagne (`briefs/AAAA-MM-slug.md`) ou `{{CAMPAGNE_FIL_ROUGE}}` pour le contenu hors campagne

## Cycle de mesure

1. **Mensuel** : snapshot `performance/AAAA-MM/data.json` (skill `performance-report`, module `reporting`) ou relevé manuel dans `objectifs.md` §3.
2. **Par campagne** : lecture filtrée par `utm_campaign` à la clôture du brief (§7-8 du brief).
3. **Trimestriel** : bilan dans `reports/`, révision des cibles dans `objectifs.md`.
