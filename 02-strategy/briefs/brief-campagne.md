# Brief de campagne — {{NOM_CAMPAGNE}}

> Template : copier ce fichier en `briefs/AAAA-MM-slug.md` avant de le remplir (voir `README.md`).

| | |
|---|---|
| **Slug** | {{SLUG_CAMPAGNE}} (aussi utilisé en `utm_campaign`) |
| **Période** | du {{DATE_DEBUT}} au {{DATE_FIN}} |
| **Statut** | draft / validé / en cours / clôturé |
| **Validé par / le** | {{VALIDATEUR}} — {{DATE_VALIDATION}} |
| **Pilier(s)** | {{PILIER}} (voir `../content-pillars.md`) |

## 1. Objectif

- **Objectif servi** : `OBJ-{{N}}` — {{RAPPEL_OBJECTIF}} (obligatoirement un ID de `../objectifs.md` ; s'il n'y en a pas, réviser d'abord `objectifs.md`)
- **Contribution attendue de la campagne** : {{CONTRIBUTION}} (ex. {{NB_LEADS}} leads sur les {{NB_LEADS_TRIMESTRE}} du trimestre)

## 2. Cible

- **Persona principal** : {{PERSONA}} (voir `../../01-brand/personas.md`) — persona secondaire éventuel : {{PERSONA_2}}
- **Étape du parcours visée** : découverte / considération / décision / fidélisation (voir `../parcours-client.md`)
- **Signaux terrain (00-intel)** : {{SIGNAUX_INTEL}} — ce qu'on a entendu récemment en meeting/prospect qui justifie cette campagne maintenant (citer les fichiers `00-intel/...` consultés, sans jamais recopier de verbatim confidentiel dans un livrable public)

## 3. Message clé

- **Message central de la campagne** : {{MESSAGE_CLE}} (décliné du message persona de `../../01-brand/messaging-framework.md`)
- **Preuve(s) à l'appui** : {{PREUVES}} (chiffres / cas clients issus du messaging-framework — aucune affirmation sans preuve)
- **Objection principale à lever** : {{OBJECTION}} (voir `../parcours-client.md` et `personas.md`)
- **CTA principal** : {{CTA}}

## 4. Mix canaux

Chaque canal a un **rôle** dans la campagne — pas de duplication du même contenu partout.

| Canal | Rôle dans la campagne | Format(s) | Volume / cadence |
|---|---|---|---|
| {{CANAL_1}} (ex. blog) | {{ROLE_1}} (ex. asset de fond qui porte l'argumentaire) | {{FORMAT_1}} | {{VOLUME_1}} |
| {{CANAL_2}} (ex. linkedin) | {{ROLE_2}} (ex. amplification, 3 angles distincts) | {{FORMAT_2}} | {{VOLUME_2}} |
| {{CANAL_3}} (ex. newsletter) | {{ROLE_3}} (ex. conversion de l'audience existante) | {{FORMAT_3}} | {{VOLUME_3}} |

## 5. Livrables et calendrier

À la validation du brief, **créer une entrée par livrable** dans `../calendar/calendar.md` (statut `idée`, `utm_campaign={{SLUG_CAMPAGNE}}`).

| Date visée | Canal | Livrable | Rôle producteur | Entrée calendrier créée |
|---|---|---|---|---|
| {{DATE}} | {{CANAL}} | {{LIVRABLE}} | {{ROLE_DOSSIER}} (ex. 09-seo) | ☐ |
| {{DATE}} | {{CANAL}} | {{LIVRABLE}} | {{ROLE_DOSSIER}} | ☐ |

## 6. Budget (le cas échéant)

| Poste | Montant | Note |
|---|---|---|
| {{POSTE_BUDGET}} (ads, sponsoring, outil, prestataire…) | {{MONTANT}} | {{NOTE}} |
| **Total** | {{TOTAL_BUDGET}} | |

*Si campagne 100 % organique : indiquer « aucun » et supprimer le tableau.*

## 7. KPIs de succès et mesure

| KPI | Cible | Comment il sera mesuré | Quand |
|---|---|---|---|
| {{KPI_1}} | {{CIBLE_1}} | {{METHODE_1}} (outil + UTM `utm_campaign={{SLUG_CAMPAGNE}}`) | fin de campagne |
| {{KPI_2}} | {{CIBLE_2}} | {{METHODE_2}} | fin de campagne |

- **Définition du succès** : {{DEFINITION_SUCCES}} (une phrase — à quoi voit-on que ça a marché ?)
- **Point de mesure intermédiaire** : {{DATE_MI_PARCOURS}} — permet d'ajuster le mix en cours de route.

## 8. Apprentissages post-campagne

*À remplir à la clôture — obligatoire avant de passer le statut à `clôturé`. Alimente la révision trimestrielle de `../objectifs.md` et les prochains briefs.*

- **Résultats vs cibles** : {{RESULTATS}} (chiffres réels en face de chaque KPI du §7)
- **Ce qui a marché** : {{CE_QUI_A_MARCHE}}
- **Ce qui n'a pas marché et pourquoi** : {{CE_QUI_N_A_PAS_MARCHE}}
- **À refaire / à éviter / à tester** : {{DECISIONS}}
- **Signaux à reporter dans `personas.md` ou `parcours-client.md`** : {{SIGNAUX_A_REPORTER}}
