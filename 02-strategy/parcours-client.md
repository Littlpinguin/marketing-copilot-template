# Parcours client — {{COMPANY_NAME}}

> **La carte que consultent la skill `content-strategy` et tout brief de campagne** avant de choisir un sujet, un format ou un canal. Pour chaque intersection étape × persona : la question que se pose la cible, le contenu/canal adapté pour y répondre, l'objection à lever pour passer à l'étape suivante.
>
> Rempli au wizard à partir de `../01-brand/personas.md`, puis enrichi en continu avec les signaux terrain (`00-intel/`) et les apprentissages de campagne (`briefs/`).

## Les 4 étapes

| Étape | État d'esprit de la cible | Ce que le marketing doit faire |
|---|---|---|
| **Découverte** | « J'ai un problème / une envie, je mets des mots dessus » | Être trouvable, nommer le problème mieux que la cible elle-même |
| **Considération** | « Quelles solutions existent ? Laquelle me correspond ? » | Éduquer, comparer honnêtement, prouver la compréhension du contexte |
| **Décision** | « Pourquoi eux, pourquoi maintenant, quel risque ? » | Rassurer : preuves, cas concrets, réduction du risque perçu |
| **Fidélisation** | « Ai-je bien choisi ? Que puis-je en tirer de plus ? » | Confirmer le choix, faire progresser, transformer en ambassadeur |

---

## Persona 1 — {{PERSONA_1_NOM}}

*Voir la fiche complète dans `../01-brand/personas.md`.*

| Étape | Question que se pose {{PERSONA_1_NOM}} | Contenu / canal adapté | Objection à lever |
|---|---|---|---|
| Découverte | {{P1_DECOUVERTE_QUESTION}} (ex. « pourquoi {{PROBLEME}} me coûte-t-il si cher ? ») | {{P1_DECOUVERTE_CONTENU}} (ex. article SEO sur {{REQUETE}}, post LinkedIn point de douleur) | {{P1_DECOUVERTE_OBJECTION}} (ex. « ce n'est pas prioritaire ») |
| Considération | {{P1_CONSIDERATION_QUESTION}} (ex. « {{SOLUTION_TYPE}} ou {{ALTERNATIVE}} ? ») | {{P1_CONSIDERATION_CONTENU}} (ex. guide comparatif, webinar, newsletter) | {{P1_CONSIDERATION_OBJECTION}} (ex. « trop complexe pour ma structure ») |
| Décision | {{P1_DECISION_QUESTION}} (ex. « quelle garantie que ça marche chez moi ? ») | {{P1_DECISION_CONTENU}} (ex. cas client chiffré, page offre, démo/RDV) | {{P1_DECISION_OBJECTION}} (ex. « {{OBJECTION_PRIX_OU_RISQUE}} ») |
| Fidélisation | {{P1_FIDELISATION_QUESTION}} (ex. « comment en tirer plus de valeur ? ») | {{P1_FIDELISATION_CONTENU}} (ex. newsletter clients, contenus avancés, événement) | {{P1_FIDELISATION_OBJECTION}} (ex. « je n'utilise pas tout ce que j'ai déjà ») |

## Persona 2 — {{PERSONA_2_NOM}}

| Étape | Question que se pose {{PERSONA_2_NOM}} | Contenu / canal adapté | Objection à lever |
|---|---|---|---|
| Découverte | {{P2_DECOUVERTE_QUESTION}} | {{P2_DECOUVERTE_CONTENU}} | {{P2_DECOUVERTE_OBJECTION}} |
| Considération | {{P2_CONSIDERATION_QUESTION}} | {{P2_CONSIDERATION_CONTENU}} | {{P2_CONSIDERATION_OBJECTION}} |
| Décision | {{P2_DECISION_QUESTION}} | {{P2_DECISION_CONTENU}} | {{P2_DECISION_OBJECTION}} |
| Fidélisation | {{P2_FIDELISATION_QUESTION}} | {{P2_FIDELISATION_CONTENU}} | {{P2_FIDELISATION_OBJECTION}} |

*Dupliquer le bloc pour chaque persona de `personas.md` (2 à 4 personas).*

---

## Comment utiliser cette carte

1. **Planification mensuelle** (`CLAUDE.md` de ce dossier) : vérifier que le plan couvre plusieurs étapes du parcours — un mois 100 % « découverte » ne convertit personne, un mois 100 % « décision » n'attire personne.
2. **Brief de campagne** : le §2 du brief cite l'étape visée ; le message clé (§3) répond à la question de cette intersection et lève l'objection associée.
3. **Production** (rôles 03-09) : avant de rédiger, lire la ligne correspondant au persona × étape du livrable — la « question que se pose la cible » est l'angle du contenu.

## Mise à jour

- À chaque classification `00-intel/` révélant une nouvelle question ou objection récurrente → l'ajouter ici (et dans la section « signaux 00-intel » de `personas.md`).
- À chaque clôture de brief : reporter les apprentissages (§8 du brief) qui changent cette carte.
- Revue complète au moins une fois par trimestre, en même temps que `objectifs.md`.
