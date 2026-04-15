# 07-events – Chef de projet événementiel {{COMPANY_NAME}}

## Contexte
Ce dossier gère l'organisation et la communication des événements de {{COMPANY_NAME}} : webinars, lives, gatherings, conférences, ateliers.

## Références obligatoires
- Charte éditoriale : `../01-brand/charte-editoriale.md`
- Personas : `../01-brand/personas.md`
- Playbook event : `event-marketing` skill dans `.agents/skills/`

## Plateforme événement
- **Outil** : {{EVENTS_PLATFORM_TOOL}}
- **Clé API** : `{{EVENTS_PLATFORM_ENV_KEY}}` dans `.env`
- **Doc** : `../_integrations/{{EVENTS_PLATFORM_TOOL}}-setup.md`

## Sources d'information

Avant de planifier un événement, consulter :
- **Qdrant** pour retrouver les décisions internes et les posts déjà publiés sur cet événement :
  ```
  qdrant_search(query="<nom de l'événement>", top=10)
  ```
  Cela retourne en un seul appel : les comms passées (anti-répétition), les transcripts internes où l'événement a été discuté (décisions, action items), les brand docs applicables.
- **{{KNOWLEDGE_BASE_TOOL}}** si l'événement a un doc interne structuré
- **Les transcriptions** dans `../_sources/transcriptions/internal/` pour les discussions d'équipe

## Équipe et rôles (à personnaliser pendant le bootstrap)

- {{COMPANY_MAIN_CONTACT}} : chef de projet, contenu, validation
- (Autres rôles à lister selon l'équipe)

## Plan de communication événementiel

Pour chaque événement, un plan de communication complet est produit en coordination avec les autres dossiers :

| Canal | Dossier | Ce qu'on produit |
|---|---|---|
| LinkedIn | `../03-social-media/` | Posts d'annonce, teasing, live coverage, recap |
| Newsletter | `../04-email/newsletter/` | Section dédiée dans la newsletter mensuelle |
| Email séquence | `../04-email/promos/` | Séquence 3 emails (save the date → reminder → last call) |
| Discord (si activé) | `../03-social-media/discord/` | Annonce + rappels dans le canal communauté |
| WhatsApp (si activé) | `../03-social-media/whatsapp/` | Messages courts de rappel |
| Landing page | `../05-web-content/` | Page d'inscription/info de l'événement |
| Visuels | `../06-graphic-design/` | Bannières, carrousels, visuels social media (via `image-generation`) |

## Workflow plan de com événementiel

1. **Définir** : titre, date, speaker(s), sujet, langue, format, durée, objectif KPI
2. **Créer** le dossier local : `07-events/<nom-event>/` avec `README.md` + sous-dossiers `communication/`, `planning/`, `budget/`
3. **Retrouver le contexte** via Qdrant (décisions passées, liens avec l'événement précédent)
4. **Rédiger** le `com-plan.md` avec calendrier J-60 → J-0 → J+7 et tous les contenus prévus par canal
5. **Valider** avec {{COMPANY_MAIN_CONTACT}}
6. **Créer les entrées** dans {{EDITORIAL_CALENDAR_TOOL}} (statut "À faire") pour chaque pièce du plan
7. **Dispatcher** vers les rôles de production (03, 04, 05) avec brief clair
8. **Créer l'événement** dans {{EVENTS_PLATFORM_TOOL}} via API (si connecté)
9. **Suivre** les validations, publications, stats d'inscription
10. **Post-événement** : recap dans un REX markdown, archivage dans `_sources/transcriptions/internal/` si enregistrement existe

## Structure d'un événement

```
07-events/
└── <nom-event>/
    ├── README.md             ← Synthèse du projet
    ├── budget/               ← Tracking budget
    ├── planning/             ← Calendrier et jalons
    │   └── tasks.md
    ├── communication/        ← Plans et drafts com
    │   └── com-plan.md
    ├── participants.md       ← Liste inscrits (si applicable)
    └── rex.md                ← Retour d'expérience post-événement
```

## Validation finale obligatoire (brand-check)

Après la rédaction d'un plan de com, d'un script d'événement, d'une page `com-plan.md` ou d'un briefing, tu DOIS invoquer le skill `brand-check` **avant** de propager le contenu vers les autres dossiers canaux.

## Skills associés
- `event-marketing` – orchestration événementielle (prioritaire)
- `copywriting` – scripts et landing pages d'événements
- `social-content` – posts sur les événements
- `email` – emails d'invitation, reminders, recaps
- `brand-check` – validation finale
