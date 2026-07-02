# État de l'art — LinkedIn 2026

> Recherche multi-sources, juillet 2026. Bases de données principales croisées : Algorithm InSights Report de Richard van der Blom (1,3-1,8 M de posts), étude Metricool 2026 (673 658 posts / 63 108 comptes, comparaison janv.-fév. 2025 vs janv.-fév. 2026), Buffer (2 M+ posts / 94 000 comptes, août 2025), benchmarks Socialinsider 2026. Attention : beaucoup de chiffres circulant sur « l'algorithme LinkedIn » sont des reprises de van der Blom sans réplication indépendante — les règles ci-dessous privilégient les points confirmés par ≥ 2 sources.

---

## 1. Règles vérifiées

### A. Fonctionnement de l'algorithme (2025-2026)

**R1. Le dwell time est le signal n°1 : écrire pour retenir la lecture, pas pour récolter des likes.**
Posts générant 61 s+ de dwell time : ~15,6 % d'engagement vs 1,2 % pour 0-3 s. Conséquence rédactionnelle : posts qui se lisent (aération, tension narrative, listes), documents à feuilleter, pas de posts « one-liner + lien ».
Sources : [Meet-Lea — LinkedIn algorithm explained 2026](https://meet-lea.com/en/blog/linkedin-algorithm-explained) ; [Hootsuite — LinkedIn algorithm 2026](https://blog.hootsuite.com/linkedin-algorithm/) ; [Dataslayer — LinkedIn algorithm 2026](https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now).

**R2. Golden hour : les 30-60 premières minutes déterminent la distribution. L'auteur doit répondre à chaque commentaire dans l'heure.**
Le test initial sur un échantillon d'audience décide du passage à l'étape de distribution élargie. Nuance 2025-2026 : LinkedIn ressert désormais des posts vieux de 2-3 semaines s'ils restent pertinents (« suggested posts ») — la golden hour conditionne le pic initial, plus la durée de vie totale.
Sources : [van der Blom — Algorithm InSights Report 2025, relayé par Mercer-Mackay](https://mercermackay.com/thinking/blog/a-leaders-guide-to-the-linkedin-algorithm-what-the-data-says/) ; [AuthoredUp — LinkedIn algorithm](https://authoredup.com/blog/linkedin-algorithm) ; [Sprout Social — LinkedIn algorithm 2026](https://sproutsocial.com/insights/linkedin-algorithm/).

**R3. Les commentaires pèsent beaucoup plus que les likes (~15× selon van der Blom), et les commentaires longs (> 10-15 mots) pèsent ~2,5× plus que les courts.**
Conséquence : (a) terminer les posts par une question qui appelle une réponse argumentée, pas un « d'accord ? » ; (b) la stratégie de commentaires substantiels sur les posts d'autrui est un levier de visibilité à part entière ; (c) les pods d'engagement sont détectés et pénalisés.
Sources : [Digital Applied — LinkedIn engagement strategy 2026](https://www.digitalapplied.com/blog/linkedin-algorithm-2026-engagement-strategy-guide) ; [Louise Brogan — LinkedIn comment strategy](https://louisebrogan.com/linkedin-comments/) ; [Botdog — LinkedIn algorithm 2025](https://www.botdog.co/blog-posts/linkedin-algorithm-2025).

**R4. Lien externe dans le corps du post = perte de portée mesurée. Fourchette selon les études : −18,8 % (médiane, van der Blom 2026, 1,3 M posts) à −60 % (études antérieures). Le lien en commentaire est aussi dégradé (jusqu'à −80 % de visibilité du commentaire).**
Règle pratique pour l'agent : contenu natif d'abord ; si un lien est indispensable, l'ajouter en édition après publication ou assumer la perte et le mettre dans le post (le « lien en commentaire » n'est plus une échappatoire fiable en 2026). Ne jamais construire une stratégie LinkedIn dont le KPI est le trafic sortant.
Sources : [Melanie Goodman — LinkedIn algorithm 2026 (données van der Blom)](https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority) ; [Dataslayer — LinkedIn 2026](https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now) ; [Hootsuite — LinkedIn algorithm 2026](https://blog.hootsuite.com/linkedin-algorithm/).

**R5. Le contenu IA générique est structurellement pénalisé : non par détection directe, mais parce qu'il génère un dwell time quasi nul, zéro save et zéro discussion. LinkedIn a annoncé vouloir limiter la portée du contenu IA de masse.**
Depuis 2025-2026, le ranking (nouveau système de type « 360Brew », modèle de fondation LinkedIn qui lit le contenu sémantiquement) évalue aussi l'**autorité thématique** : un profil qui poste sur tout perd ; un profil cohérent sur 2-3 thèmes gagne. Conséquence pour un agent IA : chaque post doit contenir un élément non générable (donnée client, anecdote datée, position tranchée, chiffre interne) — c'est un critère de validation, pas un bonus.
Sources : [Social Media Today — LinkedIn wants to limit AI-generated content](https://www.socialmediatoday.com/news/linkedin-wants-to-limit-the-reach-of-ai-generated-content/820935/) ; [Zoomsphere — Generic AI content kills reach](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach) ; [Melanie Goodman — topic authority 2026](https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority).

**R6. Profils personnels ≫ pages entreprise : engagement moyen +63 % (Metricool 2026), les posts organiques de pages ne représentent que ~2 % du feed. La stratégie par défaut = publier via les profils des fondateurs/employés, la page en support.**
Sources : [Metricool — press release LinkedIn study 2026](https://metricool.com/press-release-linkedin-study-2026/) (fetch direct) ; [Growleads — LinkedIn 2026](https://growleads.io/blog/linkedin-algorithm-2026-text-vs-video-reach/).

### B. Performance par format (données chiffrées)

**R7. Carrousels/documents et multi-images sont les formats n°1 en 2026, devant la vidéo qui recule.**
- Metricool 2026 (673 658 posts) : multi-image 3,71 % d'engagement vs vidéo 1,80 % et image seule 1,81 % ; carrousels ≈ 1 451 impressions/post vs 605 pour la vidéo.
- Buffer 2025 (2 M posts) : carrousels +278 % d'engagement vs vidéo, +303 % vs image, +~600 % vs texte seul.
- Socialinsider Q1 2026 (par impressions) : multi-image 6,6 %, documents natifs 6,1 %, vidéo 5,6 %, image ~5,2 %, texte seul 4,3 %.
- Vidéo : vues −36 % en un an (Socialinsider 2026) ; reste utile pour la notoriété (onglet vidéo dédié) mais n'est plus le format « boosté ».
- Sondages : < 1 % des posts mais impressions moyennes les plus élevées sur les pages entreprise (Metricool 2026) — format sous-exploité, à utiliser avec parcimonie (1-2/mois) et avec une vraie question métier.
Sources : [Metricool — LinkedIn study 2026](https://metricool.com/press-release-linkedin-study-2026/) ; [Buffer — How often to post on LinkedIn](https://buffer.com/resources/how-often-to-post-on-linkedin/) ; [Socialinsider — LinkedIn benchmarks](https://www.socialinsider.io/social-media-benchmarks/linkedin) ; [The State of Brand — LinkedIn killing video reach](https://www.thestateofbrand.com/news/linkedin-killing-video-reach).

**R8. L'engagement « visible » baisse, l'engagement « invisible » monte : likes −13 %, commentaires −17 %, partages −10 %, mais engagement total +14 % (clics, swipes de carrousel, vues vidéo, saves).**
Conséquence reporting : ne pas conclure « ça ne marche plus » sur la seule base des likes ; suivre impressions, clics, saves et swipes.
Source : [Metricool — LinkedIn study 2026](https://metricool.com/press-release-linkedin-study-2026/) (fetch direct, méthodo vérifiée).

**R9. Vidéo LinkedIn : verticale (9:16 ou 4:5), < 60-90 s, sous-titrée, insight dans les 3 premières secondes ; la vidéo native fait ~5× l'engagement d'un lien vidéo externe (YouTube).**
Ne jamais poster un lien YouTube : toujours uploader en natif.
Sources : [Visla — LinkedIn video 2026](https://www.visla.us/blog/guides/linkedin-video-in-2026-whats-working-and-how-to-make-it/) ; [OpusClip — LinkedIn video length](https://www.opus.pro/blog/ideal-linkedin-video-length-format-for-retention) ; [Yans Media — LinkedIn video specs 2026](https://www.yansmedia.com/blog/linkedin-video-specs).

### C. Hooks et rédaction

**R10. Le hook doit tenir dans la troncature mobile : ~140 caractères / 2 lignes sur mobile (~210 caractères / 3 lignes sur desktop avec média). La coupe est en lignes, pas en caractères : une première ligne courte + une deuxième qui crée la tension.**
Patterns validés : chiffre précis + contexte inattendu ; affirmation contrarienne ; début d'histoire in medias res. Anti-patterns : « Ravi d'annoncer… », question rhétorique creuse, emoji en rafale.
Sources : [AuthoredUp — LinkedIn character limits](https://authoredup.com/blog/linkedin-character-limit) ; [MagicPost — LinkedIn post formatting](https://magicpost.in/blog/linkedin-post-formatting) ; [ContentIn — LinkedIn post specs 2026](https://contentin.io/blog/linkedin-post-specs/).

**R11. Cadence optimale : 2 à 5 posts/semaine par profil. C'est le meilleur ROI effort/portée (+1 182 impressions/post et +0,23 pt d'engagement vs 1 post/semaine). Au-delà de 5/semaine le gain existe mais l'engagement par post s'érode (−18 à −32 % selon les sources) — réserver 6-10+/semaine aux comptes en croissance agressive avec assez de matière originale.**
Jamais 2 posts à moins de ~6-8 h d'intervalle sur un même profil (cannibalisation du test initial).
Sources : [Buffer — 2M+ posts study, août 2025](https://buffer.com/resources/how-often-to-post-on-linkedin/) (fetch direct) ; [Linkboost — posting frequency 2026](https://www.linkboost.co/blog/linkedin-posting-frequency-best-practices-2026/).

### D. Ce qui a changé récemment (2025 → 2026)

- **Déflation générale de la portée** : vues −50 %, engagement −25 %, croissance de followers −59 % en un an (van der Blom 2025). Les objectifs clients doivent être recalibrés en conséquence — promettre les portées de 2023 est irréaliste.
- **Fin de la prime à la vidéo** (poussée en 2024-début 2025, en recul net en 2026 : vues −36 %).
- **Autorité thématique** : le nouveau ranking évalue la cohérence profil ↔ sujet du post.
- **Suggested posts** : un bon post vit 2-3 semaines ; l'evergreen redevient rentable.
- **Pods et automatisations d'engagement** : détectés, pénalisés.
Sources : [Mercer-Mackay — synthèse van der Blom](https://mercermackay.com/thinking/blog/a-leaders-guide-to-the-linkedin-algorithm-what-the-data-says/) ; [The State of Brand](https://www.thestateofbrand.com/news/linkedin-killing-video-reach) ; [Melanie Goodman — 2026](https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority).

---

## 2. Chiffres clés (datés)

| Métrique | Valeur | Source, date |
|---|---|---|
| Engagement multi-image / carrousel | 3,71 % (vs vidéo 1,80 %, image 1,81 %) | Metricool, janv.-fév. 2026, 673 658 posts |
| Impressions carrousel vs vidéo | 1 451 vs 606 par post | Metricool 2026 |
| Carrousel vs autres formats (engagement) | +278 % vs vidéo, +303 % vs image, +~600 % vs texte | Buffer, août 2025, 2 M posts |
| Engagement par impressions Q1 2026 | multi-image 6,6 %, document 6,1 %, vidéo 5,6 %, texte 4,3 % | Socialinsider 2026 |
| Vues vidéo LinkedIn | −36 % sur un an | Socialinsider 2026 |
| Profil personnel vs page entreprise | +63 % d'engagement ; pages ≈ 2 % du feed | Metricool 2026 |
| Likes / commentaires / partages | −13 % / −17 % / −10 % (mais engagement total +14 %) | Metricool 2026 |
| Poids commentaire vs like | ~15× ; commentaire > 15 mots ≈ 2,5× un court | van der Blom 2025-2026 (non répliqué indépendamment) |
| Lien externe dans le post | −18,8 % de portée médiane (vdB 2026) à −60 % (études antérieures) | van der Blom 2026 / synthèses 2025 |
| Cadence optimale | 2-5 posts/semaine (+1 182 impressions/post vs 1/sem.) | Buffer, août 2025 |
| Hook mobile | ~140 caractères avant « voir plus » | AuthoredUp 2026 |
| Dwell time | 61 s+ → ~15,6 % d'engagement vs 1,2 % à 0-3 s | Meet-Lea/synthèses vdB 2026 |

---

## 3. À intégrer dans les skills du template

| Skill | Intégration concrète |
|---|---|
| `social-content` | Réécrire la section LinkedIn : hook contraint à 140 caractères/2 lignes mobile (R10) ; question finale appelant une réponse > 15 mots (R3) ; interdiction du lien externe dans le corps sauf demande explicite du client, avec mention de la perte de portée chiffrée (R4) ; critère de validation « élément non générable par IA présent » (donnée, anecdote, position) avant livraison (R5) ; rappel à l'utilisateur de répondre aux commentaires dans les 60 min post-publication (R2). |
| `content-strategy` | Défaut stratégique : profils personnels porteurs, page en relais (R6) ; cadence recommandée 2-5 posts/semaine/profil, jamais 2 posts < 6-8 h (R11) ; mix formats pondéré par les données 2026 : carrousel/document et multi-image prioritaires, vidéo en support notoriété, 1-2 sondages/mois max (R7) ; cohérence thématique (2-3 piliers max par profil) comme contrainte d'autorité thématique (R5). |
| `carousel` / `carrousel-linkedin` | Confirmer le carrousel comme format à plus fort ROI 2026 avec les chiffres Metricool/Buffer en préambule ; optimiser pour le swipe (chaque slide doit donner envie de la suivante = « invisible interactions », R8) ; slide 1 = hook autonome lisible en feed. |
| `performance-report` / `veille-strategy` | Ajouter les benchmarks 2026 comme référentiel de comparaison (tableau ci-dessus) ; ne pas juger un post sur les likes seuls — suivre impressions, clics, swipes, saves (R8) ; recalibrer les attentes clients avec la déflation de portée documentée (−50 % de vues YoY). |
| `video-editing` (posts LinkedIn) | Export vertical 9:16/4:5, < 60-90 s, sous-titres incrustés, upload natif uniquement (R9). |
