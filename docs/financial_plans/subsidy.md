# Ontwikkelingsproject – Uitgebreid Aanvraagdocument van markov

**Author:** Olivier Debeuf De Rijcker  
**Date:** 2025-01-01

[TOC]

---

## Layman's Summary (max. 0,5 blz.)

Veel kleine en middelgrote ondernemingen (kmo's) en accountants spenderen nog steeds onnodig veel tijd aan het handmatig verwerken van facturen, bonnetjes en het controleren van btw-gegevens.  
Markov is een Vlaams technologiebedrijf dat hier een oplossing voor biedt. Wij ontwikkelen een AI-platform – een slim softwaresysteem – dat documenten zoals facturen en bonnetjes automatisch herkent, verwerkt in de boekhouding en analyseert. Denk hierbij aan het uitlezen van belangrijke data (bedragen, datums, leveranciersnamen) en deze direct in de juiste boekhoudposten te plaatsen. Zo kunnen financiële administraties sneller, efficiënter en nauwkeuriger werken, wat bedrijven kostbare tijd en fouten bespaart.

Ons doel is om de volledige boekhouding te automatiseren, van het ontvangen van een factuur tot en met de indiening van de jaarrekening bij MyMinFin (het online portaal van de FOD Financiën). Daarnaast investeren we in R&D rond grote taalmodellen (LLMs). Deze krachtige modellen – vergelijkbaar met de technologie achter ChatGPT – zetten we in om de uitkomsten van onze factuurverwerking te evalueren en te optimaliseren (“LLMs as Evals”). Stel je voor dat een tweede AI-systeem het werk van het eerste beoordeelt en feedback geeft. Dit resulteert in een zelflerend systeem dat continu verbetert. Op termijn willen we dit systeem uitbreiden met meerdere gespecialiseerde "agents" (bijv. CFO-agent, procurement-agent, marketing-agent) die kmo's proactief adviseren.

### Wat levert dit concreet op?
- **Volledige automatisering:**  
  Automatisering van het volledige traject – van binnenkomende factuur tot definitieve financiële rapportage en elektronische indiening via MyMinFin.
- **Innovatieve AI-technieken:**  
  Inzet van meta-optimisatie, modeldistillatie en (optioneel) reinforcement learning.
- **Multi-agent toekomst:**  
  Een uitbreidbaar systeem dat in de toekomst extra AI-agents toevoegt voor onder meer financiën, inkoop en marketing.
- **Impact:**  
  Aanzienlijke tijd- en kostenbesparing, minder fouten in de boekhouding en stimulering van de AI-adoptie in Vlaanderen.

<div class="page-break-after"></div>

## Samenvatting van het Project (± 1 blz.)

### Algemeen Doel (6 maanden: R&D & Opschaling)
Het doel is tweeledig:  
1. Opschaling van onze bestaande AI-boekhoudoplossing (van ca. 10.000 naar 100.000 facturen per maand).  
2. Verdere ontwikkeling via R&D, gericht op vier kernpunten.

#### LLM-based Optimization
- **Werking:**  
  Inzet van LLMs om de output van ons factuurverwerkend model te beoordelen en te corrigeren.
- **Feedback:**  
  De LLM fungeert als een kritische reviewer ("LLMs as Evals") die continu de nauwkeurigheid verbetert.
- **Innovatie:**  
  Een zelfverbeterend systeem met continue kwaliteitsverbetering.

#### Reinforcement Learning & Modeldistillatie
- **Reinforcement Learning:**  
  Het AI-model leert via beloningen en straffen, waardoor het ook zeldzame, kritieke scenario's leert herkennen.
- **Modeldistillatie:**  
  Complexe modellen worden gecomprimeerd voor een efficiëntere uitvoering, essentieel voor realtime toepassingen.

#### Volledige Accounting Flow (E2E-integratie)
- **Integratie:**  
  Realisatie van een end-to-end boekhoudcyclus, van documentinvoer tot rapportage en MyMinFin-upload.
- **Efficiëntie:**  
  Een uniforme infrastructuur resulteert in een doorlooptijd van minder dan 5 minuten per factuur.

#### Multi-agent Fundament
- **Proof-of-concept:**  
  Ontwikkeling van een eerste CFO-agent die financiële analyses en strategisch advies verzorgt.
- **Uitbreidbaarheid:**  
  Een modulair framework dat in de toekomst eenvoudig extra agents (zoals inkoop, marketing, compliance) kan toevoegen.

### Concrete Doelen & Criteria (SMART)

#### R&D in AI Reasoning & LLM-based Meta-Optimisatie
- **Doel:**  
  ≥90% correct uitgevoerde boekingen, ongeacht diverse factuurlay-outs.
- **Succescriterium:**  
  +5% verbetering in de F1-score ten opzichte van de baseline, gevalideerd door pilots.
- **Metrieken:**  
  Monitoring van feedbackcycli en doorlooptijden.

#### Accounting E2E-Integratie
- **Doel:**  
  Automatisering van het volledige boekhoudproces (factuurontvangst tot MyMinFin-upload).
- **Succescriterium:**  
  80% automatische verwerking in drie pilotprojecten.
- **Overweging:**  
  Integratie van veiligheidsprotocollen en audit trails voor volledige compliance.

#### Pilots & Licenties
- **Doel:**  
  Betrekken van drie accountancyfirma's en één ERP-partner in een beta-lancering.
- **Succescriterium:**  
  Minstens één licentiecontract en actieve pilots bij drie accountancykantoren.
- **Feedback:**  
  Regelmatige evaluaties en gebruikerstests.

#### Multi-Agent Foundations
- **Doel:**  
  Ontwikkeling van de API en datapipelines voor een CFO-agent proof-of-concept.
- **Succescriterium:**  
  Een werkende interne demo van de CFO-agent (bijv. kostenoptimalisatie, fiscaal advies).
- **Toekomst:**  
  Een modulair framework dat later extra agents eenvoudig kan toevoegen.

#### Impact
- **Economisch:**  
  +2 FTE tijdens het project, met op middellange termijn 5–10 extra banen.
- **Maatschappelijk:**  
  Tijd- en kostenbesparing, minder fouten en een breder inzetbaar AI-platform.
- **Innovatie:**  
  Een zelfverbeterend systeem dat een benchmark zet in de adoptie van AI-technologie in de boekhoudsector.

<div class="page-break-after"></div>

## 1. Business Case: Van Innovatief Idee tot Boost voor markov

### 1.1. Je Bedrijf en Innovatief Idee
Markov is een jong en dynamisch Vlaams AI-startup dat zich specialiseert in workflow-automatisering voor financiële documenten. Ons werkende prototype verwerkt ca. 10.000 facturen per maand met ±85–90% nauwkeurigheid. Het doel is om dit op te schalen tot een volwaardig end-to-end boekhoudplatform met extra R&D rond "LLMs as Evals" en de ontwikkeling van multi-agent uitbreidingen.

### 1.2. Marktpositie
- **Doelgroep:**  
  Accountants en kmo's in Vlaanderen en de EU.
- **Marktomvang:**  
  Miljoenen facturen per jaar, veelal nog handmatig verwerkt.
- **USP's:**  
  - Hogere nauwkeurigheid door "LLMs as Evals"  
  - End-to-end automatisering (inclusief MyMinFin)  
  - Uitbreidbare multi-agent architectuur
- **Positionering:**  
  Onze continue zelfoptimalisatie via feedbackloops en reinforcement learning biedt een strategisch en technisch voordeel.

### 1.3. Van Project tot Markt
Binnen 6 maanden:
- **Opschaling:**  
  Van 10k naar 100k facturen per maand.
- **R&D:**  
  Onderzoek naar LLM-based optimization en reinforcement learning.
- **Integratie:**  
  Koppeling met MyMinFin.
- **Pilots:**  
  Uitvoering bij drie accountancykantoren en één ERP-partner.

> **Aanvullende focus:**  
> Intensieve klantfeedback en marktanalyses zorgen voor een soepele marktintroductie.

### 1.4. Businessmodel
- **SaaS & Licenties:**  
  Maandabonnementen op basis van verwerkte facturen.
- **ERP-partners:**  
  Samenwerkingen via white-label of co-branding deals met revenue sharing.
- **Extra Modules:**  
  Premium add-ons als extra agents voor maatwerk.

> **Innovatieve uitbreiding:**  
> Een modulair platform waarmee klanten zelf kunnen kiezen welke extra agents zij inzetten, voor een schaalbare inkomstenstroom.

### 1.5. Impact

#### Economische Impact
- **Nieuwe Aanwervingen:**  
  +2 FTE in 6 maanden, later +5–10 banen.
- **Investeringen:**  
  In HPC en AI R&D.
- **Strategisch Voordeel:**  
  Ons meta-optimalisatieconcept positioneert Markov als innovator.

> **Toegevoegde waarde:**  
> Intensieve samenwerking met de Vlaamse technologiesector versterkt zowel ons bedrijf als het regionale ecosysteem.

#### Maatschappelijke Impact
- **Tijdwinst:**  
  Significante besparing voor kmo's en accountants.
- **Foutvermindering:**  
  Minder fouten en fraude door automatische controles.
- **Duurzaamheid:**  
  Extra agents ondersteunen duurzaam inkopen en bredere optimalisatie.
- **Brede Voordelen:**  
  Een transparante en efficiënte bedrijfsvoering verlicht de administratieve last.

<div class="page-break-after"></div>

## 2. Onze Ontwikkelingsaanpak

Naast de genoemde werkpakketten besteden we bijzondere aandacht aan data governance en cybersecurity.

### 2.1. Nieuwe Kennis & Uitdagingen

#### Reeds Beschikbare Kennis
- **Werkend Prototype:**  
  10k facturen/maand met 85–90% nauwkeurigheid.
- **Basis LLM Reasoning:**  
  Ervaring met Python, Databricks en LLMs.

#### Te Ontwikkelen Kennis
- **LLM-based Optimization ("LLMs as Evals"):**  
  Optimalisatietechnieken voor ons factuurmodel.
- **Reinforcement Learning & Distillatie:**  
  Onderzoek naar verbetering van AI-modellen.
- **Volledige E2E-integratie:**  
  Realisatie van een operationele end-to-end boekhoudflow.
- **Proof-of-Concept CFO-agent:**  
  Eerste versie van een CFO-agent voor strategisch advies.
- **Data Governance & Compliance:**  
  Inbouwen van robuuste beveiligings- en auditmechanismen.

#### Belangrijkste Uitdagingen
- **LLM "Hallucinaties":**  
  Mitigatie via extra QA-checks en realtime monitoring.
- **BTW/Regelcomplexiteit:**  
  Dynamisch regelmechanisme voor correcte verwerking.
- **Opschaling tot 100k Facturen/maand:**  
  Doorlooptijd <5 minuten, met redundantie en load balancing.
- **Privacy en Cybersecurity:**  
  Naleving van GDPR en beheersing van HPC-kosten via auto-scaling.

#### Risico's en Maatregelen
- **GPU-Kosten:**  
  Mitigatie via modeldistillatie, auto-scaling en kostenmonitoring.
- **Foutieve LLM-Suggesties:**  
  Inbouwen van fallback- en 'human-in-the-loop'-mechanismen.
- **Integratieproblemen met MyMinFin:**  
  Nauwe samenwerking met overheidsinstanties en een dedicated integratieteam.

### 2.2. Aanpak (met Uitgebreide Gantt)
#### Werkpakketten (WP1 – WP5)

| Werkpakket                                          | M1 | M2         | M3         | M4         | M5         | M6         |
|-----------------------------------------------------|----|------------|------------|------------|------------|------------|
| **WP1: R&D LLM-based Optimization & Distillatie**   | X  | X (Test)   |            |            |            |            |
| **WP2: Infra, HPC & E2E Accounting**                  |    | X          | X (Load)   |            |            |            |
| **WP3: Pilot Accountancies (Integration)**          |    | (Setup)    | X          | X          |            |            |
| **WP4: Licentie-API + "LLMs as Evals"**               |    |            | X          | X          | X (Beta)   |            |
| **WP5: Multi-Agent POC (CFO) + Go-to-Market**         |    |            |            | X          | X          |            |

#### Toelichting per WP
- **WP1:**  
  Ontwerp van de "LLMs as Evals" module, opzetten van een realtime feedbackloop en experimenten met domeinspecifieke distillatie.  
  *Resultaat:* Hogere F1-score en een prototype van meta-optimalisatie.  
  *Mensen:* Olivier (4 mm), Léon (3 mm).

- **WP2:**  
  Opschalen van Databricks/GPU's, integratie met MyMinFin en stresstests tot 100k documenten/maand.  
  *Resultaat:* Doorlooptijd <5 minuten en 80% automatische verwerking.  
  *Mensen:* Louis (2 mm), Léon (2 mm).

- **WP3:**  
  Onboarding van drie accountancykantoren, verzamelen van feedback en iteratieve softwareverbeteringen.  
  *Resultaat:* 3 actieve pilotkantoren en ≥80% automatische boekingen.  
  *Mensen:* Olivier (2 mm), Louis (1 mm).

- **WP4:**  
  Ontwikkeling van een publieke API met real-time tracking, finalisatie van de eval-module en lancering van een ERP beta.  
  *Resultaat:* 1 ERP-partner live en vermindering van manuele controles.  
  *Mensen:* Olivier (2 mm), Léon (2 mm), Louis (1 mm).

- **WP5:**  
  Ontwikkeling van een interne CFO-agent (voor kostenoptimalisatie en cashflow forecasting) en creatie van marketingcollateral voor demo's.  
  *Resultaat:* Werkende CFO-demo en strategisch rollout-plan.  
  *Mensen:* Olivier (3 mm), Léon (1 mm).

### 2.3. Expertise en Middelen

#### Teamleden
- **Olivier Debeuf De Rijcker** – Founder, AI Engineer & R&D Lead  
  Verantwoordelijk voor meta-optimalisatie en strategische planning.
- **Léon Moralis** – Management Consultant (Accenture), Handelsingenieur - Data Analytics  
  Expert in HPC, modeldistillatie en data governance.
- **Louis De Geest** – Lead Data Engineer (Cegeka)  
  Specialist in cloud-infrastructuren en veerkrachtige datapipelines.

#### Middelen
- **Infrastructuur:**  
  Azure Databricks met GPU auto-scaling, versleutelde API's en een MyMinFin sandbox.
- **Data Privacy & Security:**  
  Strikte naleving van GDPR met uitgebreide logsystemen en audit trails.
- **Financiering:**  
  ±€15k eigen inleg, startlening van €85k, subsidie en bridging van ±€11k, met mogelijke extra investeringen.

<div class="page-break-after"></div>

## 3. Toegevoegde Waarde van de Steun voor markov

Zonder Vlaamse steun zou Markov meer consultingopdrachten moeten aannemen, wat de strategische AI-ontwikkeling vertraagt. Met de subsidie kunnen we in 6 maanden vol inzetten op LLM-based R&D, HPC-uitbreiding en MyMinFin-integratie. Dit versnelt onze time-to-market en vergroot de kans op een doorbraak in AI-boekhouding en multi-agent optimalisatie.

**Extra Impactaspecten:**
- **Innovatieversnelling:** Snellere technische doorbraken en strategische partnerschappen.
- **Concurrentievoordeel:** Een robuust, zelflerend systeem positioneert ons als technologische pionier.
- **Kennisoverdracht:** Ontwikkelde modules kunnen later als white-label oplossingen worden aangeboden.

## 4. Toepassingsgebied: Geen Militaire Affiniteit

Dit project richt zich uitsluitend op civiele boekhoud- en bedrijfsautomatisering. Onze technologie wordt uitsluitend voor commerciële doeleinden gebruikt.

## 5. Toegevoegde Economische Waarde voor Vlaanderen

We voorzien een hefboomwerking van >36× op de subsidie over 5 jaar. De economische impact van dit project bedraagt ruim €2.870k, vergeleken met de gevraagde subsidie van circa €79.821.

### Impactberekening

| Impactberekening   | 6m  | Y1  | Y2  | Y3  | Y4  | Y5  | 5-jaars Totaal |
|--------------------|-----|-----|-----|-----|-----|-----|----------------|
| Nieuwe FTE         | +2  | +3  | +5  | +7  | +9  | +10 | –              |
| Loonkosten (k€)    | 120 | 250 | 400 | 500 | 550 | 600 | ~2.400         |
| Investeringen (k€) | 20  | 80  | 90  | 90  | 90  | 90  | ~470           |
| **TOTAAL (k€)**    | 140 | 330 | 490 | 590 | 640 | 690 | ~2.870         |
| Gevraagde Subsidie | 79,821  | -   | -   | -   | -   | -   | €79,821           |

### Budgetsamenvatting (6 Maanden)

| Category                                   | 6-Month Budget (€) | Comments                                                                                         |
|--------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------|
| Olivier Debeuf De Rijcker       | 60.000             | R&D kosten (6 maanden) – Externe partnerkosten voor onderzoek, ontwikkeling en strategische planning.  |
| Léon Moralis                   | 47.880             | R&D payroll (6 maanden) – Ondersteuning in AI-optimalisatie, modeldistillatie en data governance.|
| Overhead (17% op loon)                      | 15.300             | Kantoorkosten, administratie en beveiligingsimplementatie.                                       |
| Contractor: Louis De Geest                  | 45.000             | HPC-schaal en multi-tenant security – 6 maanden subcontract.                                     |
| Model Usage (OpenAI of eq.)                 | 6.000              | ~€1k/maand – LLM eval + (deels) reinforcement learning, inclusief licenties.                      |
| Cloud / Datacenter (GPU HPC)                | 6.000              | ~€1k/maand – Inclusief extra kosten voor monitoring en auto-scaling.                               |
| **TOTAAL**                                 | **177.380**        | (Rondingen mogelijk)                                                                             |

Wij vragen een subsidie van ±45% op deze kosten, oftewel ongeveer **€79.821**.

<div class="page-break-after"></div>

## 6. Bijkomende Informatie

### Start en Pilots
We kunnen starten zodra er een beslissing is. We zijn direct klaar voor uitvoering. Momenteel staan drie accountants en één ERP-partner in vergevorderde gesprekken.

> **Aanvullende opstart:**  
> We plannen een kickoff-workshop met alle betrokkenen om de implementatie, evaluatiecriteria en communicatieafspraken vast te leggen.

### Contact
- **Olivier Debeuf De Rijcker** – Founder, AI Engineer  
  **E:** [olivier@markov.bot](mailto:olivier@markov.bot)  
  **T:** +32 480 61 60 01
- **Léon Moralis** – Lead Data Scientist  
  **E:** [leon@markov.bot](mailto:leon@markov.bot)
- **Louis De Geest** – Data Engineer  
  **E:** [louis@markov.bot](mailto:louis@markov.bot)

<div class="page-break-after"></div>

## 7. Toekomstperspectieven en Duurzame Innovatie

Markov richt zich op een lange termijn visie waarin ons platform evolueert naar een breed inzetbaar AI-ecosysteem:
- **Uitbreiding Multi-Agent Systeem:**  
  Naast de CFO-agent ontwikkelen we extra agents (bijv. Procurement, Marketing & Sales, Risk & Compliance) die via een modulair framework naadloos integreren.
- **Integratie van Externe Datastromen:**  
  Het toevoegen van externe databronnen (marktdata, economische indicatoren) verbetert de contextuele intelligentie van onze AI.
- **Innovatieve Onderzoeksrichtingen:**  
  Naast reinforcement learning onderzoeken we de mogelijkheden van federated learning, waarbij organisaties gezamenlijk modellen trainen zonder data te delen.
- **Strategische Partnerschappen:**  
  We streven naar een "Innovation Hub" die samenwerkingen met andere innovatieve Vlaamse en Europese bedrijven faciliteert.

## 8. Extra Toelichting: Multi-agent Scenario "Beyond Accounting"

### Accounting Automatisering
Van factuur- en bonherkenning tot automatische balans, jaarrekening en MyMinFin-upload. De kernfunctionaliteit is een volledig geautomatiseerde boekhouding, ondersteund door continue kwaliteitscontroles en foutdetectie.

### LLM-based Optimization ("LLMs as Evals")
Grote taalmodellen genereren feedback om eigen uitkomsten te verbeteren, wat resulteert in een continu lerend en zelfverbeterend systeem.

### CFO-Agent
Naast cashflow forecasting biedt de CFO-agent "what-if" scenario's, investeringsanalyses en risicobeoordelingen, als strategisch financieel adviseur.

### Procurement-Agent
Vergelijkt leveranciers, analyseert offertes en integreert duurzaamheidscriteria, waardoor optimale inkoopstrategieën ontstaan.

### Marketing & Sales-Agent
Maakt gebruik van klantsegmentatie en churn-detectie om proactief marketingcampagnes aan te sturen en de klantbenadering te optimaliseren.

### Risk & Compliance-Agent
Houdt continu toezicht op btw-updates, fraude en wettelijke vereisten, en ondersteunt bedrijven bij compliance en interne controles.

## 9. Conclusie en Verwachtingen

Het Markov-project vertegenwoordigt een ambitieuze stap in de digitalisering van financiële processen en de ontwikkeling van een adaptief, zelflerend AI-ecosysteem. Met onze innovatieve aanpak in LLM-based optimalisatie, reinforcement learning en een uitbreidbaar multi-agent platform, bieden we aanzienlijke meerwaarde voor kmo's en accountants.

Onze lange termijnvisie richt zich op het creëren van een flexibel platform dat bedrijven op meerdere domeinen ondersteunt. Door technologische innovatie, strikte data governance en een duidelijke marktstrategie zet Markov de standaard in de Vlaamse en Europese bedrijfsautomatisering.

**EINDE AANVRAAGDOCUMENT**