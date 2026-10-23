# saas-ideas-spain

Research into the day-to-day pain points of SMEs, autónomos and new startups in Spain's
major cities (Madrid, Barcelona, Valencia, Sevilla, Zaragoza, Málaga, Bilbao and others),
turned into ranked SaaS product ideas.

## Method

| Stage | What happens | Output |
|---|---|---|
| 1. Capture | 17 parallel research tracks collect evidence-backed pain points, lawsuits, sanctions and friction across all domains and cities | `research_notes/Spanish SME pain points SaaS ideas/*.md` |
| 2. Filter | Drop noise (weak evidence, not software-solvable, postponed rules, already cheaply solved) and turn real pains into candidate SaaS ideas | Idea longlist in `research_notes/` |
| 2b. Validate | Check each idea from several angles: competitors, regulation status, demand evidence, pricing, distribution, build effort, defensibility, plus an adversarial review | Validation notes in `research_notes/` |
| 3. Rank | Score validated ideas by how sellable they are and how severe the problem is | `reports/` |

Ideas are grouped into three types:

- **A. Cheaper alternatives** to products SMEs already pay for
- **B. New products** for real problems nobody solves well
- **C. Low-touch ~€5/month subscriptions** that customers keep and rarely think about

## Research tracks (stage 1)

| File | Area |
|---|---|
| `tax_invoicing_accounting.md` | VeriFactu, e-invoicing, TicketBAI, autónomo taxes, gestorías, accounting software |
| `labor_hr_litigation.md` | Time recording, HR obligations, payroll, absenteeism, hiring, labour lawsuits |
| `bureaucracy_licensing_funds.md` | Opening licences, company formation, e-government, Kit Digital, grants, tenders |
| `cashflow_finance_insolvency.md` | Late payment, debt collection, credit, payments, insolvency, DANA, cyber-fraud |
| `legal_disputes_compliance.md` | Civil/commercial disputes, MASC, consumer claims, GDPR fines, EAA, AI Act, NIS2 |
| `hospitality_tourism.md` | Bars, restaurants, hotels, tourist rentals, SES.Hospedajes, city rental rules |
| `retail_ecommerce_services.md` | Shops, online sellers, hairdressers, beauty, gyms, pet and repair businesses |
| `construction_realestate.md` | Builders, trades, CAE, agencies, landlords, property managers |
| `transport_industry_agrifood.md` | Haulage, manufacturing, farming, food industry, SIEX, food-chain law |
| `health_professional_education_care.md` | Clinics, vets, gestorías, law firms, academies, care services |
| `startups_tech_ecosystem.md` | Ley de Startups, ENISA, fundraising, hiring, foreign founders |
| `cities_macro_surveys.md` | City-by-city profiles, low-emission zones, municipal costs, national SME surveys |
| `voice_of_smes_software_market.md` | Forum complaints, software prices and complaints, Kit Digital aftermath |
| `midterm_housing_coliving.md` | Mid-term rentals, coliving, remote-worker housing, rent caps, ID verification |
| `expat_relocation_bureaucracy.md` | NIE/TIE, cita previa, visas, Beckham regime, relocation services market |
| `zbe_lez_fleets.md` | Low-emission zones by city, enforcement, fleet impact, LEZ data and routing tools |
| `gaming_streaming_creators.md` | Spanish gaming market, streamers, Kings League, creator leagues, gambling rules |

User-supplied ideas (ColivEs, PermisoFast, EcoRoute, Fandango Arena, LigaHub) and the claims
behind them are recorded in `00_user_supplied_ideas.md`. They go through the same validation
and ranking as every other idea.

## Datasets

`data/pain_points.csv` (and `.jsonl`) holds all structured pain points from stage 1, one row
each, with who/where, evidence and source URLs, scale, cost, regulatory status as of
October 2026, current solutions and prices, software-solvability and confidence. Once stage 2
runs it also carries each pain point's filter status. Rebuild it with
`python3 scripts/build_datasets.py`.

## Status

- [x] Stage 1: capture (395 pain points, ~1,500 source links, 17 tracks)
- [ ] Stage 2: filter into idea longlist (in progress)
- [ ] Stage 2b: multi-angle validation
- [ ] Stage 3: ranking and final report
