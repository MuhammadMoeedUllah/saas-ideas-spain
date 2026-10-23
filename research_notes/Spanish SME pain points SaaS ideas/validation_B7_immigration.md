# Validation batch 7: immigration and relocation (IDEA-52 to IDEA-58, with user idea U2 PermisoFast)

*Validator: batch 7. Date of work: 23 October 2026. Inputs: `stage2_idea_longlist.md` (sections 2, 3, 5, 6.1 and batch 7), `00_user_supplied_ideas.md` (U2), `stage2_G6_expat_startups_gaming.md`, `stage2_G2_labour_legal_admin.md` (G2-I05) and the stage-1 tracks `expat_relocation_bureaucracy.md` (EXP), `labor_hr_litigation.md` (LAB-08), `bureaucracy_licensing_funds.md` (ADM-09, ADM-10) and `startups_tech_ecosystem.md` (STA-09 to STA-11).*

*Citation format: [new: URL, date seen or published] for evidence gathered in this validation; [notes: PAIN-ID] for stage-1 evidence. "Single-source" marks a claim found in one place only. Prices are € excluding VAT unless stated.*

*Status: complete (provisional verdicts for the adversarial review). WebSearch calls used: 22 of 24.*

## 1. Batch summary

| ID | Name (as validated) | Type | Verdict | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Sellability | P | Overall | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IDEA-52 | PermisoFast reshaped: UGE evidence pre-check for law firms (module of IDEA-56 for employer-filed routes) [U2] | B (A) | RESHAPE | 3 | 1 | 3 | 3 | 3 | 4 | 2 | 3 | 2.75 | 3 | 2.85 | low |
| IDEA-53 | Renewal-wave case manager for immigration filers | B (A) | KILL | 4 | 2 | 2 | 3 | 2 | 4 | 1 | 3 | 2.63 | 3 | 2.78 | high |
| IDEA-54 | Extranjería rule and form-version radar | C (B) | KILL | 2 | 2 | 2 | 3 | 1 | 5 | 1 | 3 | 2.38 | 2 | 2.23 | medium |
| IDEA-55 | Office decision-time tracker, reshaped as a free crowdsourced data layer | B (C) | RESHAPE | 2 | 2 | 2 | 3 | 3 | 5 | 3 | 2 | 2.75 | 3 | 2.85 | low |
| IDEA-56 | Spain relocation critical-path engine, reshaped agency-first (white-label, then API) | B (A) | RESHAPE | 4 | 1 | 3 | 3 | 3 | 4 | 2 | 3 | 2.88 | 3 | 2.93 | low |
| IDEA-57 | Work-permit status and renewal monitor, reshaped gestoría-led | C (B) | RESHAPE | 5 | 3 | 2 | 3 | 3 | 5 | 1 | 3 | 3.13 | 4 | 3.48 | medium-low |
| IDEA-58 | Beckham-regime filing kit and six-year tracker | A (C) | KILL | 5 | 2 | 2 | 3 | 2 | 4 | 1 | 3 | 2.75 | 3 | 2.85 | medium |

**How to read the table**
- Scores are for the reshaped version wherever the verdict is RESHAPE.
- Sellability is the mean of S1–S8, shown to two decimals.
- Overall = 0.6 × Sellability + 0.4 × P, computed from the unrounded mean and rounded half up.

**Headline findings**
1. **Kill triggers met in substance.** GestoLab, a small, apparently solo-built AI vertical SaaS at €79–199 a month with unlimited files, already ships the core of IDEA-53. TaxDown already files modelo 149 and 151 inside a plan from €65 a year, which removes IDEA-58.
2. **IDEA-57, reshaped through payroll gestorías, is the batch leader at 3.48.** The rules behind it are verified in the BOE, and the 2027 wave of art. 191 modifications likely opens from February 2027. Employer demand is still inferred, not surveyed.
3. **The user's PermisoFast survives only as a narrow UGE evidence pre-check.** It scores 2.85, with a small buyer base and low defensibility. Of the original claims, the market, the target cities and error checking survive. The backlog framing, "regional portals", generic pre-fill and the HR filing-suite buyer do not.

## 2. Ideas

#### IDEA-52: PermisoFast reshaped: UGE evidence pre-check for immigration law firms (and, through IDEA-56, employer-filed routes) — RESHAPE (low)

**Validated definition (after reshape).** This is a narrow, per-case evidence pre-check for files that go to the national Unidad de Grandes Empresas y Colectivos Estratégicos (UGE): digital-nomad (teletrabajo internacional), highly qualified (national PAC and EU Blue Card) and intra-company routes.
- **Input:** the lawyer, or the client through the lawyer's link, uploads bank statements, payslips or invoices, the contract or employer letter, the health policy and the company documents.
- **Checks:**
  - deposits are reconciled against payslips or invoices month by month;
  - the policy is checked for copayments and waiting periods;
  - the income or salary line is computed from live SMI and INE data (2026: €2,849 a month for a single DNV applicant, plus €1,068 for the first family member and €356 per child; €41,356.36 for the PAC and Blue Card, €33,085.09 for the reduced Blue Card line);
  - company age (one year or more) and the prior relationship (three months or more) are checked.
- **Output:** a gap list and a cover memo for the lawyer.
- **Price and buyers:** sold per case (about €25–35) to DNV-specialist law firms and lawyer-led marketplaces.
- **Employer routes:** the same engine sits inside IDEA-56 for employer-sponsored routes where the company itself files (Ley 14/2013 art. 71.1).
- **Dropped from the stage-2 version:**
  - the multilingual intake portal and generic AI document validation, which GestoLab already ships;
  - any direct-to-applicant mode, because of intrusismo exposure;
  - anything near appointments.

As a standalone company it fails the size and moat tests, so the reshape keeps it as a cheap per-case pilot and a module.

**(a) Problem reality and rule status (Oct 2026)**
- **Legal frame: in force, and not exposed to the election.**
  - Ley 14/2013 art. 76.1: "El plazo máximo de resolución será de veinte días desde la presentación electrónica", with positive silence, and processing by the UGE "a través de medios telemáticos".
  - Art. 76.3: renewals run for two years, filing extends validity, and there is a 90-day late grace.
  - Art. 74 ter: the DNV needs a company with at least one year of real activity and at least three months of prior relationship.
  - Art. 71.1: a highly qualified application "podrá ser presentada por la empresa o por el profesional extranjero".
  - Art. 76.5: a passport is enough for the Social Security alta in the first six months.
  - [new: https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074, consolidated text seen 23 Oct 2026]
- **Salary thresholds (C-25 conflict settled).**
  - Orden PJC/44/2026 (BOE-A-2026-2142) sets the Blue Card line at 1.4 × INE's average gross annual salary, with a 0.8 coefficient for shortage occupations and recent graduates. New INE data apply to applications from one month after publication (art. 3.2). Its art. 1 covers only the art. 71.2.a modality. [new: https://www.boe.es/eli/es/o/2026/01/27/pjc44, published 30 Jan 2026]
  - With INE's 2024 average of €29,540.26 [notes: EXP-09], that gives €41,356.36 and €33,085.09 (my arithmetic).
  - The national PAC uses a single €41,356.36 line according to a practitioner [new: https://machelindiaz.com/actualizacion-umbral-salarial-altamente-cualificado-2026/, ~Jun 2026]. That is UGE practice, not the order.
  - Both sides of the conflict were partly right: the order covers only the Blue Card, and the same figure is applied to the national PAC in practice.
- **2026 minimum wage.**
  - RD 126/2026 (BOE-A-2026-3815) sets €1,221 a month in 14 payments [new: https://www.boe.es/eli/es/rd/2026/02/18/126, published 19 Feb 2026].
  - 200% prorated over 12 months is €2,849 a month (my arithmetic), matching Anchorless [notes: STA-10] and most 2026 guides [new: search 11 results, e.g. https://movingtospain.com/?p=1056, seen 23 Oct 2026].
  - The market is still confused:
    - Cohen y Aguirre gives €2,700 [new: https://cohenyaguirre.es/nuevos-requisitos-visado-de-nomada-digital, 3 Mar 2026];
    - Lexidy shows €2,763 "as of 2025" and "Over 2,850€" on the same page [new: https://www.lexidy.com/services/spain/immigration/digital-nomad/, seen 23 Oct 2026].
- **UGE practice (no official statistics).** There are no official figures on document requests or denials.
  - Practitioners list these denial causes:
    - a badly framed employment or professional relationship;
    - telework not authorised in the contract;
    - a relationship under three months, or payslips and invoices "sin trazabilidad bancaria";
    - a foreign company without one year of real activity;
    - Social Security not accredited (A1 certificate or Spanish registration);
    - deficient translations or legalisations;
    - for freelancers, more than 20% Spanish clients.

    [new: https://machelindiaz.com/denegaciones-tipicas-en-nomada-digital-y-como-recurrir-sin-perder-el-foco/, ~Nov 2025]
  - Cohen y Aguirre says the UGE-CE "ha endurecido la revisión de los seguros de salud y la cobertura de la Seguridad Social". Denials often come from generic service contracts (from 200+ cases it reviewed in 2025), and telematic resolution "se ha estabilizado en 20 días hábiles" [new: 3 Mar 2026, law-firm source].
  - Klevvera claims "35%+" denials in 2025 for self-filed UGE applications, "by our observation" [new: https://www.klevvera.com/blog/spain-digital-nomad-visa-cost-breakdown/, 22 Sep 2026; vendor claim, single-source].
  - Criterio de Gestión 2/2025 itself was not found (search 2), so it stays single-source [notes: EXP-08].
  - Verdict on the pain: it is real according to practitioner consensus, but unquantified.
- **Annual UGE grants by type.**
  - Not published in any source reached: search 1 found nothing, and the La Moncloa note of 20 Mar 2026 has no UGE data [new: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/200326-poblacion-extranjera-con-residencia.aspx, seen 23 Oct 2026].
  - Stock: 174,357 in Sep 2025, including 44,966 DNV, 47,190 executives and highly qualified, 6,083 Blue Card and 4,592 ICT [notes: EXP-08, EXP-09].
  - Inference (low confidence): the DNV stock grew by about 17,000 in nine months, so new DNV grants including family are probably around 20,000–25,000 a year, and all UGE talent routes around 30,000–50,000 a year including family.
- **Fee conflict (C-25): open.**
  - Klevvera gives €73.26 per applicant on modelo 790-038 for 2026 [new: 22 Sep 2026]; Anchorless gives €70.40 / €75.60 [notes: STA-10].
  - The general fee order, Orden PJC/617/2025 (BOE-A-2025-12056), does not list the UGE fee [new: https://www.boe.es/buscar/act.php?id=BOE-A-2025-12056, seen 23 Oct 2026], and the ministry's UGE pages return HTTP 403.
  - Not material to the idea.
- **Election risk: none.** The frame is a law plus regulations, and thresholds update administratively.

**(b) Competitors**
- **GestoLab (gestolab.com), the closest and most likely copier.**
  - **Product:** an extranjería practice suite for gestorías and lawyers:
    - AI validation of 33 document types;
    - a client portal in 9 languages and WhatsApp intake;
    - 26 EX forms filled and editable;
    - a Chrome extension that fills the Mercurio draft and uploads documents; per the page it neither files nor signs;
    - DEHú handling and e-signature of the engagement letter;
    - expiry alerts, and AI reading of document requests.
  - **Prices:** €79, €99 or €199 a month, VAT included (€790–1,990 a year), with unlimited clients and files.
  - **Coverage:** "Nómada digital (teletrabajo internacional)" is listed as a covered procedure, but no UGE or Ley 14/2013 feature (reconciliation, insurance check, thresholds) appears on its pages.
  - **Company:** the controller is a named individual; the product is hosted in the EU (Ireland), with some processing by Anthropic in the US; it has 5.0★ from 3 reviews; no press footprint (search 22).
  - [new: https://www.gestolab.com/ , /producto , /abogados-extranjeria, seen 23 Oct 2026]
- **Corporate platforms.**
  - Jobbatical: Spain "Immigration Assessment" €150 and "Immigration Package" €1,500 per person, with legal and government fees at cost. Every package includes "automated visa form filling", tracking and renewal alerts [new: https://www.jobbatical.com/pricing, seen 23 Oct 2026].
  - Deel: US$250 documentation fee per process [new: https://www.deel.com/blog/how-to-get-a-visa-and-work-permit-in-spain/, updated 9 Jun 2026]; EOR from $599 per employee per month [new: https://www.deel.com/pricing/, seen 23 Oct 2026].
  - Localyze: subscription plus case-service tiers, no public prices [new: https://www.localyze.com/pricing, seen 23 Oct 2026].
- **Law firms and intermediaries.**
  - Lexidy DNV packages: €900, €2,050, €2,300 or €3,900; it claims "Over 10K" and "Over 7K" clients on the same page [new: Lexidy, seen 23 Oct 2026].
  - Klevvera: legal representation €1,500–4,500 for a single applicant [new].
  - Nomadlex: a marketplace ("not a law firm") quoting full visa services at €800–2,000 [new: https://www.nomadlex.io/, seen 23 Oct 2026].
  - Anchorless: an intermediary "Up to 999€", mostly Portugal, claiming "+5000" relocations in Spain [new: https://anchorless.io/, seen 23 Oct 2026].
  - NIM Extranjería: an online law firm, so a buyer rather than a competitor [new].
  - myspanishdnv.com returned 403.
- **Abroad.**
  - Cicerai is a US legal-research AI with immigration forms; it has no Spanish product [new: https://www.cicerai.com/, seen 23 Oct 2026], which settles the notes' open question.
  - Mitratech INSZoom is US-centric case management [new: search 3 result].
- **Gap.** No product was found that reconciles deposits with payslips or invoices, checks insurance clauses or applies UGE thresholds (searches 3, 11 and 17). The gap is real but one feature wide, and GestoLab already holds the intake, the DNV procedure and an AI layer.

**(c) Buyers and market size**
- **Filers in general.** More than 14,000 lawyers had joined the Abogacía's Registro de Representantes for online immigration filing by April 2021, up from 3,000 in May 2020 [new: https://www.abogacia.es/actualidad/noticias/mas-de-14-000-abogados-inscritos-en-el-registro-de-representantes-de-la-abogacia-para-realizar-tramites-de-extranjeria-online/, via search snippet]. ICAM has 5,925 lawyers on Mercurio, and Catalonia about 2,000 immigration lawyers [notes: EXP-06].
- **UGE talent work** is concentrated in far fewer firms:
  - named DNV and UGE firms: Lexidy, Klevvera, Polaris, Platinum Legal, Latitude Law, Lexmovea, NIM, Cohen y Aguirre, Machelin Díaz;
  - EuRA's Spanish directory: about 24 destination-service and relocation-management firms (some are branches), plus supplier immigration law firms such as Marfour, Sagardoy Legal & Expat, MG International Mobility and Grupo Adlanter [new: https://www.eura-relocation.com/membership/our-members?country=ES, 5 pages, seen 23 Oct 2026];
  - about 110 "Relocation" companies [notes: EXP-21].
- **Estimates (inference, low confidence).**
  - Between 200 and 600 firms handle 15 or more UGE files a year.
  - Ceiling at 30,000–50,000 cases × €30: €0.9–1.5M a year at 100% share, so €0.1–0.3M at a realistic 10–20%.
  - As a subscription: 300 firms × €199 a month is about €0.7M a year.
  - This is a side business, not a venture.

**(d) Willingness to pay**
- **Client fees:** €900–3,900 for DNV packages and €1,500 for Jobbatical's package, so €30 per case is 1–3% of the fee [new: Lexidy, Jobbatical, seen 23 Oct 2026].
- **Tool spend:** firms already pay €79–199 a month for GestoLab [new], which shows tool spend. But buyers may expect reconciliation to come inside such a suite.
- **Unknowns:** hours per case and price per case need interviews.

**(e) Distribution**
- ICAM's extranjería area and its new web [new: https://web.icam.es/area-de-extranjeria/, via search snippet], ICAB and the CGAE Subcomisión de Extranjería.
- Direct outreach to roughly 24 EuRA destination-service firms (the directory is public).
- White-label deals with lawyer marketplaces (Nomadlex) and online firms (NIM).
- Applicants search with high intent, but serving them directly is legally exposed (see f). No channel is proven.

**(f) Build feasibility and legal constraints**
- **Integration and time to MVP.** There is no UGE API, so the output is a pack for manual upload. An MVP covering DNV reconciliation, the insurance checker and the threshold calculator would take about 6–8 weeks for 1–3 people using LLM extraction. Statements from many banks, currencies and formats are the hard part.
- **Criminal records.** LOPDGDD art. 10.3 lets abogados and procuradores, and no one else, process criminal data "facilitada por sus clientes para el ejercicio de sus funciones" when no specific legal norm covers it [new: https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673, art. 10, seen 23 Oct 2026]. The SaaS would act as the lawyer's processor; gestorías acting as controllers need legal advice. Art. 28.2 flags large-scale or special-category processing for a DPIA.
- **AI Act.** Annex III point 7 covers only systems "intended to be used by or on behalf of competent public authorities" [new: https://artificialintelligenceact.eu/annex/3/, seen 23 Oct 2026; EUR-Lex blocked automated fetching]. So a private lawyer's pre-check is not an Annex III high-risk system (my reading).
- **Intrusismo.**
  - Supreme Court doctrine holds that intrusismo can arise from simple acts of legal advice, without any court appearance [new: search 13 results].
  - On 18 Feb 2026 ICAM asked the parliamentary groups to extend Penal Code art. 403 to automated systems that give advice "sin intervención directa de un profesional habilitado". The proposal explicitly excludes "herramientas internas usadas por profesionales bajo su dirección" [new: https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/el-icam-propone-reformar-el-codigo-penal-para-frenar-el-neointrusismo-digital-en-el-asesoramiento-juridico-con-ia-2026-02-18/].
  - It lapses with the dissolution (inference), but it marks the line: sell to professionals only.

**(g) Defensibility**
- Low. The thresholds are public, the reconciliation logic is copyable, and GestoLab is one feature away.
- The only lasting asset would be an outcome dataset (which evidence gaps led to UGE document requests or denials), and that needs firms to share outcomes.

**(h) Kill criteria**
- Fewer than five firms run a paid pilot: open [I].
- Reconciliation does not measurably cut document requests: open [I].
- Neither is triggered by desk evidence.
- Proposed new kill test: GestoLab or Jobbatical ships bank-statement reconciliation before the pilot converts.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | A recurring, costly per-case risk for firms, but no legal duty on the buyer and no deadline. |
| S2 Buyers | 1 | Probably 200–600 firms with UGE volume, plus some dozens of agencies and marketplaces: under 5k. |
| S3 Willingness to pay | 3 | Adjacent spend: firms pay GestoLab €79–199 a month and clients pay €900–3,900 a file. No direct evidence for this feature. |
| S4 Reachability | 3 | Colegio sections, the EuRA directory and marketplaces exist, but none is proven as a partner channel. |
| S5 Competitive gap | 3 | Nobody reconciles UGE evidence, but GestoLab's AI validation and Jobbatical's expert packages cover part of the job. |
| S6 Build speed | 4 | A DNV MVP in about 1–2 months; no certification. |
| S7 Defensibility | 2 | Maintained thresholds plus a possible outcome dataset, but trivially reachable by GestoLab. |
| S8 Retention | 3 | Steady per-case use and renewals every 2–3 years; no legal obligation on the firm. |
| **Sellability** | **2.75** | |
| P (severity) | 3 | A denial or document request costs the applicant weeks and the firm paralegal hours and reputation. Frequency per firm is moderate. |
| **Overall** | **2.85** | 0.6 × 2.75 + 0.4 × 3 |

**Open [I] checks**
- Hours a DNV or PAC case spends on reconciling evidence, and the share of UGE files that get a document request.
- Price per case that five DNV-specialist firms would pay in a pilot.
- Whether firms would share outcome data.
- Whether GestoLab or Nomadlex would integrate or resell the module.

**What would change the verdict**
- **Up to GO:** five or more firms pay €30 or more per case in a pilot and document requests fall measurably; or a distribution deal with GestoLab or a marketplace.
- **Down to KILL:** GestoLab ships reconciliation; or interviews show under one hour of reconciliation work per file.

**User idea U2 (PermisoFast): what survives validation**

| Original claim or feature | Verdict after validation | Evidence |
|---|---|---|
| NIE backlogs | **Partly supported; not a product.** | NIE appointments take 3–5 days to 6–8 weeks according to an alert vendor [notes: EXP-01]. The binding bottleneck is the TIE fingerprint step. Since 8 Oct 2026 the police auto-assign it for "inicialmente un 10%" of resolved files [new: DGP notice via ICAB, https://www.icab.es/export/sites/icab/.galleries/documents-noticies/2026-INICIO-PROYECTO-PILOTO-ASIGNACION-AUTOMATICA-DE-CITA-PARA-TOMA-DE-HUELLA.pdf, dated 08/10/2026]. |
| Cita previa backlogs | **Supported as a pain; unusable as a feature.** | Bots and resale are prosecuted [notes: EXP-02]. The state is replacing booking with push assignment. Málaga's office says notices go by SMS or email "a la persona interesada o a su representante", cancelling puts the person back in the automatic queue, and conditional grants are excluded [new: OFEX Málaga note of 8 Oct 2026, https://www.arc-legal.es/storage/2026/10/OFEX-Malaga-Asignacion-Cita-automatica.pdf]. The pilot is a "fase de prueba", with no commitment to full roll-out (DGP note). Only tracking the 20-day window survives, inside IDEA-56. |
| Beckham Law status backlogs | **Contradicted.** | AEAT must issue the certificate "en el plazo máximo de los diez días hábiles" (RIRPF art. 119.4) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820]. The real pain is the six-month option window from the Social Security alta (art. 116.1.a) and the fact that exclusion is permanent (art. 118.5). TaxDown already files modelo 149 (see IDEA-58). |
| Corporate HR teams and relocation agencies as buyers | **Partly supported. The notes' "contradicted" overstated it.** | A company can itself file the UGE highly qualified application (Ley 14/2013 art. 71.1) and the 2027 art. 191 modification for its workers (RD 1155/2024 art. 191.5). "Cualquier persona física o jurídica" can represent someone else if a notarial or apud-acta power accredits it (art. 197.4.a) [new: BOE consolidated RD 1155/2024, https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099, last update 22 Sep 2026]. But scalable third-party filing runs through convenio professionals (lawyers filed 58% of regularisation e-applications [notes: EXP-22]), and HR buys services (Jobbatical €1,500 per person) rather than filing software. HR and agencies survive as buyers of IDEA-56's orchestration layer, not of a filing suite. |
| Scraping real-time changes on regional portals | **Contradicted as specified; the need survives.** | The sources are national (BOE, ministry, DGGM, SEM, Delegaciones, police notices). Ministry pages return HTTP 403 to automated access (curl and WebFetch, 23 Oct 2026) [new]. The changes keep coming: the Supreme Court annulments published 22 Sep 2026, and police notes on 8 and 16 Oct 2026. Free weekly newsletters already cover them (IDEA-54). Keep as an internal feed only. |
| Pre-filling forms from document data | **Supported need, already commoditised.** | GestoLab fills 26 EX forms and pre-fills the Mercurio draft (€79–199 a month), and Jobbatical includes "automated visa form filling" [new]. Not a differentiator. |
| Computer vision to catch errors before submission | **Supported need, partly served. The UGE-specific checks are the only surviving differentiator.** | GestoLab validates 33 document types (for example a padrón older than 90 days) [new]. No one reconciles bank deposits with payslips or checks insurance clauses against UGE practice (searches 3, 11, 17). This is the core of reshaped IDEA-52, and it is copyable. |
| Target cities Madrid, Barcelona and Málaga | **Supported for demand; the product is national.** | The largest UGE stocks are Barcelona 53,700, Madrid 41,680 and Málaga 19,056 [notes: EXP-08]. The UGE is a single national unit. The cities matter for marketing and for the in-person steps: all three are in the police pilot. |
| (Implied) a generative-AI suite handling the whole file | **Risky as scoped.** | Criminal-record data is lawful for lawyers' tools (LOPDGDD art. 10.3). The AI Act's Annex III does not bite on private tools (point 7 covers public authorities). Direct-to-applicant advice carries intrusismo risk (Penal Code art. 403 doctrine; ICAM's 2026 proposal). Keep a professional in the loop. |

**Net verdict on U2.** The market (non-EU talent moving to Madrid, Barcelona and Málaga) and two features survive: document-based error checking, now narrowed to UGE evidence, and a national rule feed used internally. The buyer, the "regional portals", the backlog framing and the generic pre-fill do not. The surviving product is small, and its best home is as a module of IDEA-56 or a per-case add-on for law firms.

#### IDEA-53: Renewal-wave case manager for immigration filers (2027 regularisation renewals) — KILL (high)

**Validated definition.** A tool for habilitated filers (lawyers, gestores administrativos, graduados sociales and registered collaborators) that imports the 2026 regularisation caseload, computes each client's 2027 window for the art. 191 modification, chases documents through multilingual links, cross-checks identity data and produces the filing pack for Mercurio. The validation confirms the job is real and the rules are fixed. But the core of the product (caseload import from Excel plus a per-client view of the modification window plus renewal alerts) is already on sale from GestoLab at a flat price with unlimited files. That triggers the idea's own kill and pivot criterion. The NGO-tier pivot is not a business: collaborators must represent for free.

**(a) Problem reality and rule status (Oct 2026). Batch 7 owns this check.**
- **RD 316/2026** [new: https://www.boe.es/eli/es/rd/2026/04/14/316, BOE-A-2026-8284, published 15 Apr 2026, in force 16 Apr 2026] adds DA 20 (international-protection applicants) and DA 21 (people in Spain before 1 Jan 2026) to RD 1155/2024. In both cases:
  - **Validity.** The permit "tendrá una vigencia de un año" and allows employed and self-employed work anywhere (DA 21.10).
  - **Renewal route.** "Durante los dos meses previos a la fecha de expiración … sus titulares deberán solicitar una modificación conforme al artículo 191". DA 21 uses "deberán"; DA 20 uses "podrán".
  - **Filing extends validity** until resolution. So does filing up to three months late, but that remains an infraction under LOEX art. 52.b (minor, up to €500, art. 55.1.a) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2000-544].
  - **Fallback.** A one-year extension for active job search or a regional integration report; four years for serious illness, disability or retirement age.
  - **Retroactive effect.** The definitive permit "su eficacia se retrotraerá al momento en el que se presentó la solicitud" (DA 20.3 and DA 21.4). If, as this suggests, the year runs from filing, expiries fall between mid-April and end-June 2027. The two-month windows would then open from mid-February 2027, a concentrated wave rather than a spread one (inference; confirm against the expiry dates stated in the first resolutions or in DGGM criteria).
- **The modification is a full file, not automatic.**
  - Art. 191.3: after a year of residence with a work-enabled permit, the holder must meet art. 80 (employed) or art. 86 (self-employed), and the new permit lasts four years.
  - Art. 191.5: "podrán ser presentado por el empleador o por la persona extranjera".
  - Art. 80.2 asks for one of: continuity of the job; at least three months of work a year plus a new contract or registration; or nine months worked in twelve.
  - Criminal records and tax and Social Security compliance are checked ex officio (arts. 80.5 and 86.5).
  - Unanswered renewals are deemed granted after three months (art. 80.9).
  - [new: https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099, consolidated to 22 Sep 2026]
- **Kill trigger 1 ("renewal simplified or automatic") is not met.** The 2027 step needs evidence of employment or activity.
- **Office load.**
  - Madrid was resolving "modificaciones … desde situaciones que habilitan a trabajar" filed on 05-07-26 as of 1 Oct 2026, a queue of about three months [new: Madrid Delegación PDF "Fechas de instrucción de los procedimientos", https://mptmd.gob.es/content/dam/mpt/delegaciones_gobierno/delegaciones/madrid/servicios/extranjeria/2026/2026%2010%20OCT.pdf, dated 1 Oct 2026].
  - Art. 197.2, which made electronic filing compulsory for some categories, was annulled in full on 8 Jul 2026 (BOE 22 Sep 2026). In-person filing remains possible, and professional e-filing is unaffected [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-19632].
- **Volume.**
  - Applications: 1,174,978, of which 609,737 had been processed by 2 Jul 2026. The ministry published no later balance [new: La Moncloa, 2 Jul 2026; search 4 and search 20 found no later figure].
  - Affiliates: the minister cited 262,475 regularised people affiliated on 4 Aug 2026 [new: search 20 snippet], and Funcas 337,917 by end-Aug [notes: EXP-03].
  - The 2027 wave is therefore somewhere between about 0.3M and 1M files (inference).
- **Election risk: none.** RD 316/2026 is a royal decree and needs no convalidation. A new government could amend DA 21 only in 2027.

**(b) Competitors**
- **GestoLab, as of 23 Oct 2026** [new: https://www.gestolab.com/abogados-extranjeria and /producto, seen 23 Oct 2026]:
  - it covers the 2026 regularisation permits ("Las autorizaciones de la regularización duran un año") and their 2027 modification ("Las modificaciones del art. 191 de 2027, cada una con su fecha");
  - a caseload view on all plans: "La pantalla de Caducidades te dice, cliente por cliente, desde qué día se puede pedir la modificación, si la ventana está abierta o si va tarde";
  - roster import: "En GestoLab importas la cartera desde un Excel con el trámite «Regularización extraordinaria» y la fecha de caducidad" (quotes re-checked verbatim on 23 Oct 2026);
  - migration is free: "Nos mandas tu Excel o tus carpetas…";
  - the Empresa plan (€199 a month, VAT included) adds "Aviso de renovación a 60 días y expediente en un clic";
  - all plans have unlimited clients and files, plus AI document validation, a 9-language portal, WhatsApp intake, EX forms and the Mercurio extension.
- Other options: manual work; gestoría renewal at €90 [notes: EXP-03]; free NGO help.
- No other extranjería-specific SaaS was found (search 17).

**(c) Buyers and market size**
- E-filing shares in the 2026 regularisation: lawyers 58%, gestores 8.4%, graduados sociales 3.6%, registered collaborators 5.1%. The collaborators are 495 third-sector and union entities [new: La Moncloa, 2 Jul 2026].
- More than 14,000 lawyers were registered for online immigration filing in 2021 [new: Abogacía, via search snippet].
- At €3–5 per case on a 0.3–1M wave, the theoretical ceiling is €1–5M, but only once, in 2027. GestoLab's flat pricing caps what filers will pay.

**(d) Willingness to pay**
- Filers earn €100–400 per file [notes: EXP-22].
- GestoLab charges €79–199 a month with unlimited files. For a filer with 200 renewals that is well under €1 per case, against the hypothesis of €3–5 per case.
- Kill trigger 3 (filers refuse per-case pricing) is therefore likely in practice.

**(e) Distribution**
- Colegios of lawyers, gestores and graduados sociales. GestoLab already markets the 2027 modification message to the same buyers.

**(f) Build feasibility and legal constraints**
- Easy (weeks).
- Renewal files avoid most of the GDPR art. 10 risk, because the office obtains the criminal-record certificate itself (art. 86.5) or checks it ex officio (art. 80.5).
- Collaborators under Orden ISM/164/2026 must represent "de forma gratuita" [notes: EXP-22], so the NGO tier earns little.

**(g) Defensibility**
- None against an incumbent that already ships the workflow.

**(h) Kill criteria**
- Renewal automatic or simplified: **not met**.
- GestoLab ships bulk renewals at around €1 per case: **met in substance**. It ships roster import and window tracking at a flat fee with unlimited files.
- Filers refuse per-case pricing: **likely met**, given the flat-fee anchor.
- The 20–30 filer interview criterion: open, but moot.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | A dated 2027 wave within 12 months, but the legal duty sits with the filers' clients. |
| S2 Buyers | 2 | Roughly 5k–20k filing firms and professionals. |
| S3 Willingness to pay | 2 | The incumbent's flat fee with unlimited files sets the anchor below €1 per case. |
| S4 Reachability | 3 | Colegio channels exist, but are contested. |
| S5 Competitive gap | 2 | GestoLab already offers the core workflow. |
| S6 Build speed | 4 | MVP in 1–2 months. |
| S7 Defensibility | 1 | Already copied before launch. |
| S8 Retention | 3 | Modifications, then four-year renewals; caseload records. |
| **Sellability** | **2.63** | |
| P (severity) | 3 | Capacity and correction costs for filers; existential for their clients, but not for the buyer. |
| **Overall** | **2.78** | 0.6 × 2.625 + 0.4 × 3 |

**Open [I] checks**
- Whether the DGGM will issue renewal criteria for DA 20/21, or accept collective or batch filings.
- Whether filers find GestoLab adequate. Not needed for the kill.

**What would change the verdict**
- GestoLab stalls or exits.
- The 2027 modification proves evidence-heavy in a way GestoLab does not automate. In that case, revive it as a feature of the gestoría-led IDEA-57 rather than as a standalone filer tool.

#### IDEA-54: Extranjería rule and form-version radar, tagged by procedure — KILL (medium)

**Validated definition.** A paid feed that watches the national sources (BOE, ministry instructions and DGGM criteria, Delegación and police notices, UGE thresholds, AEAT and DGT) and turns each change into a dated note tagged by procedure and province, with alerts. The pace of change is confirmed. But the professional audience already gets it free and fast. Automated access to the key ministry sources is blocked. And nothing in it is defensible. Keep the feed as an internal component of IDEA-52, IDEA-56 and IDEA-57, and as free content marketing, not as a product.

**(a) Problem reality and rule status**
- **The changes keep coming.** Since the stage-1 count (at least 20 changes):
  - the two Supreme Court rulings were published on 22 Sep 2026, annulling ten provisions including art. 197.2 [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-19632 and -19633];
  - DGP notices on 8 Oct and 16 Oct 2026 [new: ICAB PDF; ARC Legal, search 16 snippet];
  - the Málaga office note of 8 Oct 2026 [new];
  - a DGGM Criterio de Gestión 1/2025 under Ley 14/2013 on collective processing of intra-company transfers [new: https://www.gestoresalicante.org/blog/wp-content/uploads/2025/08/CRITERIO-DE-GESTION-DGGM-1-2025_LEY-14-2013_TRAMITACION-COLECTIVA-ITC.pdf, via search 10];
  - DGT consulta V2467-25 on the Beckham main home [new: Andersen alert, Jul 2026].
- **Thresholds update in automatic monthly steps** after each INE release (Orden PJC/44/2026 art. 3.2) [new].
- **Election.** Decrees pause while criteria continue [notes: EXP-06]. There is no lapse risk for the radar itself.

**(b) Competitors and free alternatives**
- **ARC Legal's "Extranjería Legal"**: a weekly newsletter for professionals by email plus Substack, "Suscríbete gratis", with no paid tier [new: https://www.arc-legal.es/extranjeria-legal-newsletter-semanal-para-estar-al-dia/; https://extranjerialegal.substack.com/about, seen 23 Oct 2026].
- **Machelin Díaz**: a blog with monthly processing-time posts since 2019 [new: search 18 results].
- **Infoextranjeria**: returned 503 when fetched.
- **Parainmigrantes**: sells professional seminars; a 17 Sep 2026 session on the Ley de Emprendedores is marked "plazas agotadas". Price not retrieved [new: search 1 result].
- **Colegios**: ICAB circulated the DGP pilot notice in a PDF created on 8 Oct 2026, the day the notice was dated [new: ICAB PDF metadata]. The Madrid and Málaga offices publish their own notes [new].
- **Others**:
  - CGAE Subcomisión de Extranjería communications [new: search 8];
  - Aranzadi LA LEY courses (a 100-hour course on RD 1155/2024) [new: search 8];
  - legal databases (vLex, Aranzadi, Lefebvre), whose extranjería alert prices were not verified;
  - GestoLab's checklists "revisada contra el BOE", including RD 316/2026 [new].

**(c) Buyers**
- More than 14,000 lawyers registered for online immigration filing (2021) [new], plus gestorías, about 110 relocation firms [notes: EXP-21] and about 24 EuRA destination-service firms [new].

**(d) Willingness to pay**
- Weak. No paid alert tier was found among the specialist newsletters (search 8). Professionals pay for training and databases, not for a feed.

**(e) Distribution**
- Colegios, LinkedIn and newsletter co-marketing. Plausible but unproven, and the incumbents are the channel.

**(f) Feasibility and legal constraints**
- **Blocked or unstable sources:**
  - ministry pages (inclusion.gob.es instructions and UGE pages) returned HTTP 403 to both curl and WebFetch on 23 Oct 2026;
  - the sede (sede.administracionespublicas.gob.es) returned 503 [new].
- **Accessible sources:**
  - the BOE open-data API returns consolidated texts block by block, with version dates [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2024-24099/texto/indice];
  - Delegación PDFs are fetchable (Madrid) [new].
- Police notices surface only through colegios and law firms.
- DGGM criteria "carecen de valor normativo" [notes: EXP-06], so there is liability for mis-summaries.

**(g) Defensibility**
- None. A weekend scraper plus an LLM matches it, and the free newsletters already do the curation.

**(h) Kill criteria**
- Under 5% of free subscribers convert within three months: open [I].
- Colegio circulars already cover every change in time: partly evidenced. ICAB circulated the pilot notice the same day. Leaning met, but "every change" cannot be confirmed by desk research.

**Type C check.** €9 per seat is not supported, and neither is about €5 a month: the substitutes are free and weekly. It would need to be free with an upsell. It is not a standalone low-touch subscription.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 2 | A recurring information need with no duty or deadline. |
| S2 Buyers | 2 | Roughly 5k–20k professionals and firms. |
| S3 Willingness to pay | 2 | Weak. No paid alert products in the niche; spend goes to training. |
| S4 Reachability | 3 | Colegios and newsletters exist, but they are the competition. |
| S5 Competitive gap | 1 | Free, weekly and good enough (ARC Legal, Machelin Díaz, colegios). |
| S6 Build speed | 5 | MVP in under 4 weeks. |
| S7 Defensibility | 1 | Trivially copyable. |
| S8 Retention | 3 | Periodic use if subscribed. |
| **Sellability** | **2.38** | |
| P (severity) | 2 | Missed changes cause occasional document requests or denials. Rare per professional. |
| **Overall** | **2.23** | 0.6 × 2.375 + 0.4 × 2 |

**Open [I] checks**
- What ICAM and ICAB send, how fast and in what format.
- Free-to-paid conversion test at €9 per seat with 30 professionals.

**What would change the verdict**
- Evidence that professionals pay for procedure-tagged alerts, for example 5% or more conversion.
- A colegio white-label deal.
- Otherwise it stays a feature.

#### IDEA-55: Expected-decision-time tracker for each Extranjería office and procedure — RESHAPE (low)

**Validated definition (after reshape).** A free, public office-timing tracker. It archives the monthly resolution-date PDFs of the only three offices that publish them, Madrid, Valencia and Baleares; two of them overwrite their files, so history has to be captured from now on. It collects anonymised, dated data points for the 49 demarcations that publish nothing, Barcelona first, from applicants and professionals. It shows an expected window, labelled with the legal deadline and the meaning of silence:
- two months with negative silence for initial reunification;
- three months with positive silence for renewals;
- twenty days with positive silence at the UGE.

It earns money only indirectly:
- as the timing layer inside IDEA-56 and its agency and white-label customers;
- through law-firm and agency subscriptions to an office dashboard at €29–49 a month, if interviews show demand.

The €3-a-month personal alert is dropped. The consumer anchor is a one-off €6.99, and law firms already publish estimates free.

**(a) Problem reality and rule status**
- **Who publishes.** "Solo tres oficinas de extranjería publican sus fechas de resolución: Madrid, Valencia e Illes Balears." In the other 49 demarcations "la única vía oficial es consultar tu expediente concreto" [new: https://espanaabogados.com/fechas-de-resolucion-de-tramites-de-extranjeria-en-espana/, updated 12 Oct 2026].
  - Madrid publishes monthly on the 1st, one PDF a month, so older months are kept.
  - Valencia publishes monthly but overwrites the file.
  - Baleares is irregular: the file name changes, and the table was unchanged for almost four months before 2 Oct 2026.
  - The ministry's own provincial averages cover two procedures and were last published in February 2025.
- **The Madrid PDF** ("Fechas de instrucción de los procedimientos", 1 Oct 2026) is machine-readable text. It has about 35 procedure lines, each with a "solicitudes" date and a "recursos" date. Examples: initial employee permit filings from 22-08-26; renewals from 27-07-26; modifications from work-enabled situations from 05-07-26; initial reunification from 31-07-26 [new: https://mptmd.gob.es/content/dam/mpt/delegaciones_gobierno/delegaciones/madrid/servicios/extranjeria/2026/2026%2010%20OCT.pdf].
- **Barcelona.** Lawyers estimate 7–9 months ("la espera real se está moviendo en una franja aproximada de entre 7 y 9 meses"), from their own caseload, not official data [new: https://machelindiaz.com/retrasos-oex-barcelona-extranjeria/, ~Mar 2026]. Another firm gives regional ranges in working days, for example 120–210 for Catalonia and Valencia, again from its own caseload [new: https://cohenyaguirre.es/plazos-reales-tramitacion-extranjeria-por-provincia, 10 Jun 2026].
- **Legal deadlines (C-25 conflict settled).**
  - Initial reunification: "resolverá … en el plazo máximo de dos meses … Transcurrido dicho plazo … se entenderá que la solicitud ha sido desestimada" (RD 1155/2024 art. 68.6, unchanged since the original text). The "three months or 45 working days with positive silence" version is wrong for initial reunification.
  - Employed-work renewals: positive silence after three months (art. 80.9).
  - UGE: twenty days, positive (Ley 14/2013 art. 76.1).
  - Regularisation files: three months, negative (DA 21.4).
  - [new: BOE consolidated texts, seen 23 Oct 2026]
- **Kill test 2 is not met.** The official status service shows a status, not an expected date. Secondary sources describe the states "En trámite", "Resuelto favorable", "Resuelto no favorable" and "Archivado", and none of the results describes an official expected-date field [new: search 15 results such as https://cohenyaguirre.es/estados-expediente-de-extranjeria-significados and https://www.ineaf.es/tribuna/como-consultar-estado-de-expediente-de-extranjeria/; secondary sources only]. The sede itself returned 503 to automated access.
- **For corporate talent hires**, the main HR segment, the UGE decides nationally in about 20 days. Office queues bite mainly on general-regime hires, family reunification and students (inference from the rules above). That shrinks the HR-buyer case.

**(b) Competitors**
- **Free compilers:**
  - España Abogados: a monthly table plus archived PDFs [new];
  - Machelin Díaz: monthly timing posts going back to 2019 [new: search 18];
  - Cohen y Aguirre: estimates published as lead generation for €60 consultations [new].
- **GestoLab**: a free legal-deadline calculator by procedure, with no office timings [new: https://www.gestolab.com/calculadora-plazos].
- **Extranjería App** [new: https://extranjeriapp.es/, seen 23 Oct 2026]:
  - more than 300k downloads and 13k+ Google Play reviews at 4.6★;
  - Premium is a one-off "6,99 €" (launch offer; normally €9.99): "Pago único · No es una suscripción";
  - no file tracking and no office timings.
- No crowdsourced tracker was found (search 18).

**(c) Buyers**
- Individuals: 3,497,284 general-regime residents [notes: EXP-04].
- HR and agencies: about 110 relocation firms and about 24 EuRA destination-service firms [new; notes: EXP-21].
- Law firms.
- Paying B2B entities are probably under 5k (inference).

**(d) Willingness to pay**
- Consumer: a one-off €6.99 (Extranjería App).
- Law firms give timing estimates away free.
- HR and agency willingness to pay is untested.

**(e) Distribution**
- Strong, high-intent consumer search ("cuánto tarda arraigo Madrid") and expat communities.
- B2B through IDEA-56 and agencies, unproven.

**(f) Build feasibility**
- Simple PDF parsing (Madrid text) plus a contribution form, moderation and small-sample statistics.
- Low data sensitivity if contributions carry no NIE.

**(g) Defensibility**
- The public-PDF layer is already done free.
- The only moat is a crowdsourced dataset for the 49 silent offices. It has network effects if it is seeded early through professionals and kept free for applicants.

**(h) Kill criteria**
- Fewer than 200 Barcelona data points in three months: open [I].
- The official status service already shows expected dates: **not met**.
- HR does not plan around office timing: open [I], and weakened in advance because UGE talent routes bypass office queues.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 2 | Occasional planning pain with no duty. |
| S2 Buyers | 2 | Paying entities (agencies, law firms, HR) roughly 5k–20k at most; consumers will not pay a subscription. |
| S3 Willingness to pay | 2 | Consumer anchor €6.99 one-off; law firms give estimates away. |
| S4 Reachability | 3 | High-intent consumer search exists; B2B channel unproven. |
| S5 Competitive gap | 3 | Static free compilers exist; no dataset for the 49 silent offices. |
| S6 Build speed | 5 | MVP in under 4 weeks. |
| S7 Defensibility | 3 | A crowdsourced dataset could become a real moat if seeded. |
| S8 Retention | 2 | Individuals leave once resolved; B2B use is periodic. |
| **Sellability** | **2.75** | |
| P (severity) | 3 | Months of uncertainty for families and hires; moderate money cost. |
| **Overall** | **2.85** | 0.6 × 2.75 + 0.4 × 3 |

**Open [I] checks**
- Fifteen HR and mobility interviews on whether timing data changes offers, start dates or spend.
- Whether 200 or more Barcelona data points arrive in three months.
- Whether three agencies pay for a dashboard.

**What would change the verdict**
- **Up:** the Barcelona data threshold is met and an agency or IDEA-56 customer pays for the feed.
- **Down to KILL:** Barcelona or the ministry starts publishing per-procedure dates, which would remove the gap; or contributions fail.

#### IDEA-56: Spain relocation orchestrator, reshaped agency-first — RESHAPE (low)

**Validated definition (after reshape).** A Spain-specific critical-path engine sold first to relocation agencies (destination-service providers) as a white-label case workspace. A later API would serve mobility platforms and HR teams that already run their own UGE filings.

It tracks the personal clocks that nobody else models end to end:
- the Beckham modelo 149 window: six months from the start date on the Social Security alta;
- the foreign driving licence: valid up to six months from acquiring normal residence;
- the police TIE auto-assignment: an appointment expected within about 20 days, otherwise self-booking;
- renewals and the family files, with reunification at two months and negative silence.

It also carries route templates, a document vault, family sub-cases and a hand-off pack for the chosen filer. Office timings come from IDEA-55 and the UGE evidence pre-check from IDEA-52. Not included:
- filing or booking;
- direct HR sales of a full platform, where Jobbatical, Localyze and Deel already sell bundled services.

Price hypothesis: about €150–250 a month per agency, plus €10–15 per active case.

**(a) Problem reality and rule status**
- **Beckham.** "en el plazo máximo de seis meses desde la fecha de inicio de la actividad que conste en el alta en la Seguridad Social" (RIRPF art. 116.1.a). The certificate follows within ten working days (art. 119.4). Excluded taxpayers cannot opt again (art. 118.5) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820]. Correction: the notes cited art. 119.4 for the deadline (via BM Consulting); the deadline is art. 116.1.a.
- **Driving licence.** "Que no haya transcurrido el plazo de seis meses, como máximo, contado desde que su titular adquiera su residencia normal en España", unless an agreement says otherwise (Reglamento General de Conductores art. 21.2.c) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481]. The agreement-country list is per DGT [notes: EXP-13].
- **TIE.**
  - The police pilot covers "inicialmente un 10%" of files resolved from 8 Oct 2026, in Madrid, Barcelona, Valencia, Alicante, Málaga and Murcia from 9 Oct, after earlier provinces. After 20 days without an appointment, the person books on the web. Full roll-out is undecided [new: DGP notice via ICAB, 08/10/2026].
  - A police clarification of 16 Oct 2026 repeats 10% [new: ARC Legal, search 16 snippet].
  - Málaga: appointments are at the nearest station; notices go to the applicant or the representative; cancelling re-queues the person; grants conditional on entry to Spain or on the Social Security alta are excluded [new: OFEX Málaga note, 8 Oct 2026].
  - A Coruña has auto-assigned since June 2026 [new: search 16 snippet].
  - Coverage of renewal TIEs is not stated in the official notes (open).
- **Return authorisation (EX-13).** Instrucción 1/2026 expired on 30 Sep 2026 [notes: EXP-17]. Current handling was not re-checked (no search spent; open).
- **UGE.**
  - Twenty days with positive silence (Ley 14/2013 art. 76.1).
  - The company may file (art. 71.1).
  - A passport is enough for the Social Security alta in the first six months (art. 76.5), which starts the Beckham clock [new: BOE Ley 14/2013].
- **Reunification.** Two months, negative silence (RD 1155/2024 art. 68.6) [new].
- **Election risk: none.** All these are laws, regulations or administrative practice.

**(b) Competitors**
- **Jobbatical:**
  - Spain "Immigration Assessment" €150 and "Immigration Package" €1,500 per person, with government, translation and legal fees at cost;
  - an "Experience Package" for settling in: registration, housing search, bank, tax number and schools (price not shown);
  - every package includes a dedicated expert, automated form filling, real-time tracking, document storage and renewal alerts;
  - platform modules for case management, renewals, expenses and HRIS/ATS integrations.

  [new: https://www.jobbatical.com/pricing, seen 23 Oct 2026]
- **Localyze:** Starter, Business and Enterprise software tiers, plus Basic (self-managed guide), Assisted and Premium case services, with no prices [new: https://www.localyze.com/pricing].
- **Deel:** US$250 documentation fee; EOR from $599 a month [new].
- **Agencies:**
  - Locallista admin pack €400; Relocation Angel €1,200–3,500 [notes: EXP-21];
  - EuRA's Spanish members include Eres Relocation, Anywr/Antares, SIT, BRS Global Mobility, Sterling Lexicon, aRelocation (Madrid, Barcelona, Valencia, Mallorca), Hasenkamp, EMS, Steps, Holistic, Matrix and Global Immigration-Relocation-Moving;
  - Grupo Adlanter lists "Mobility IT" [new: EuRA directory].
- **GestoLab:** tracks fingerprint appointments and TIEs, with client reminders, for gestorías [new].
- **Gap.** Platforms cover the immigration case. None found models the Spanish personal clocks (Beckham, licence, police pilot) as one engine for agencies. Global platforms could add this depth.

**(c) Buyers and market size**
- **Stock.** About 58,000 employer-sponsored UGE permits (Sep 2025): 47,190 highly qualified, 6,083 Blue Card and 4,592 ICT [notes: EXP-09].
- **Sponsors.** The number of companies registered with the UGE is not published (search 10).
- **Agencies.**
  - EuRA lists about 38 Spanish entries over five pages. About 24 are destination-service or relocation-management firms, some of them branches; the rest are suppliers [new].
  - About 110 firms are listed under "Relocation" in Empresite [notes: EXP-21].
- **Ceiling.** 100 agencies × (€200 a month + €12 per case × 20 cases) ≈ €0.5M a year (inference). Small.

**(d) Willingness to pay**
- Clear spend on services: €1,500 per person at Jobbatical, €1,200–3,500 per agency package, $599 a month EOR.
- Agencies' spend on tooling is unknown.

**(e) Distribution**
- The EuRA directory: public contacts, concentrated, but no partner programme.
- HRIS marketplaces: Factorial is Spanish; its marketplace terms were not checked.
- Startup hubs and the Barcelona International Welcome Desk [notes: EXP-21].

**(f) Build feasibility and legal constraints**
- A rules and workflow engine with templates; MVP in about 1–2 months.
- Sensitive identity and family data, so EU hosting, processor agreements and agency security reviews.
- No filing, no booking, and no tax advice: the Beckham clock is a reminder plus a hand-off.

**(g) Defensibility**
- Low to moderate: a maintained Spain step graph plus timing data from IDEA-55 plus agency white-label lock-in.
- Jobbatical or Localyze could add the same depth.

**(h) Kill criteria**
- Fewer than 10 HR teams in Barcelona and Madrid with five or more non-EU moves a year: open [I]. Large companies use relocation-management firms in any case, which supports the agency-first reshape.
- Agencies will not pay for tooling: open [I]. This is now the main test.
- Jobbatical or Deel is good enough: partly evidenced for the immigration case (Jobbatical's Spain package includes tracking and renewal alerts), but not for the personal clocks.

**Scores (reshaped version; the stage-2 HR-first version would score about 2.78)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Hard personal deadlines per move: the six-month Beckham window, the six-month licence rule, the 20-day TIE window. |
| S2 Buyers | 1 | About 100–150 agencies plus few platforms: under 5k. |
| S3 Willingness to pay | 3 | Large service spend per move; tooling spend unproven. |
| S4 Reachability | 3 | A concentrated, public agency directory, but no proven programme. |
| S5 Competitive gap | 3 | Global platforms cover the immigration case, not the Spanish personal clocks. |
| S6 Build speed | 4 | 1–2 months. |
| S7 Defensibility | 2 | A maintained step graph and white-label lock-in; copyable by platforms. |
| S8 Retention | 3 | Steady case flow per agency; renewals and the six Beckham years. |
| **Sellability** | **2.88** | |
| P (severity) | 3 | A missed Beckham window costs one person thousands of euros a year. Per agency the cost is moderate. |
| **Overall** | **2.93** | 0.6 × 2.875 + 0.4 × 3 |

**Open [I] checks**
- Ten agency interviews on tooling spend and margins; target three or more paid pilots at €150 a month or more.
- Whether HR teams with recurring moves exist outside the relocation-management firms' clients.
- Current EX-13 practice.

**What would change the verdict**
- **Up to GO:** three or more agencies pay; or a mobility platform licenses the engine.
- **Down to KILL:** agencies refuse to pay; or Jobbatical or Localyze ships Spanish personal-clock features.

#### IDEA-57: Work-permit status and renewal monitor, reshaped gestoría-led — RESHAPE (medium-low)

**Validated definition (after reshape).** A white-label "foreign-worker status board" for payroll gestorías (gestorías laborales) and graduados sociales. They already hold the employer relationship and the worker list, and they can sell the renewal filing. Employers who come direct get a free or €5-a-month tier. It does three jobs:
1. **Pending regularisation files.** It tracks provisionally authorised workers: who has been resolved, and how. The worker "deberá poner inmediatamente en conocimiento de la persona empleadora el sentido" of the resolution, and a denial "supondrá la automática pérdida de la habilitación provisional para trabajar".
2. **The 2027 modification campaign.** It runs the art. 191 modification campaign for the DA 21 one-year permits, with windows likely from February to June 2027. The employer or its gestoría can file (art. 191.5).
3. **Ongoing expiries and renewals.** It tracks expiries, captures the filing receipt (resguardo), sends multilingual WhatsApp reminders to workers and keeps an employer log as inspection evidence.

It does not file, advise or hold criminal-record data. Price hypothesis:
- gestoría: €29–49 a month for up to 100–200 workers, then €1 per worker a month;
- direct employers: €49 a year.

**(a) Problem reality and rule status (Batch 7 owns the DA 20/21 rules)**
- **What protects the employer while a renewal is pending: settled.**
  - A renewal filed in the two months before expiry "prorrogará la validez de la autorización anterior hasta la resolución del procedimiento". The same applies to filing up to three months late, though that is still a minor infraction (RD 1155/2024 arts. 80.1 and 86.1; DA 20.10 and DA 21.10) [new: BOE consolidated RD 1155/2024].
  - The Madrid immigration office's employer note: once the renewal is filed in those windows, "el extranjero continua en situación regular en España y está autorizado para trabajar" [new: https://mptmd.gob.es/content/dam/mpt/delegaciones_gobierno/delegaciones/madrid/servicios/extranjeria/Nota_empleadores.pdf, PDF created 22 Apr 2025].
  - So the resguardo (filing receipt) is the employer's key evidence.
- **The employer's exposure.**
  - Hiring a foreign worker without the authorisation is a very serious infraction, counted per worker (LOEX art. 54.1.d), fined €10,001–100,000 (art. 55.1.c) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2000-544].
  - The Labour Inspectorate found 18,655 unauthorised foreign workers in 2025 and proposed €187.7M in fines [notes: LAB-08].
- **The 2026–27 status wave.**
  - Regularisation applicants could work provisionally from the start of processing.
  - Resolution is due within three months, after which the application is deemed rejected by silence (DA 21.4).
  - The employer depends on the worker's disclosure.
  - How negative silence interacts with the provisional work right is ambiguous in the text. Check the DGGM criteria before building any feature on it (open).
- **Official verification.** No official online service lets an employer verify a worker's authorisation.
  - In Feb 2024 TGSS told graduados sociales that checking authorisation at the alta through ADEXTRA was a priority, blocked by the document support number [new: https://www.cograsova.es/blog/wp-content/uploads/2024/03/Acta56_20240223_GRADUADOS.pdf, via search snippet, single-source].
  - If TGSS automates the check at the alta, unauthorised hires would be caught, but not lapses during employment (inference).
- **Election risk: none.** Royal decrees and organic law.

**(b) Competitors**
- **Factorial** (Spanish HR suite, from €5.5 per person a month): "Também pode configurar alertas para documentos que expirem, contratos a termo, certificados, autorizações" [new: https://factorialhr.pt/blog/softwares-de-gestao-documental/, modified 23 Oct 2026; https://factorial.es/blog/?p=199846, prices checked Aug 2026]. These are generic expiry alerts with no immigration logic.
- **GestoLab**, for extranjería gestorías:
  - expiry alerts at 30, 7 and 1 days;
  - a 60-day renewal alert;
  - a regularisation modification-window view [new].
- **Payroll suites** (a3nom, Sage, Nominasol): a permit-expiry feature is unverified (search 21 and the Sage blog fetch found nothing).
- **The gap:** a worker-facing multilingual reminder plus resguardo capture plus an employer inspection log, run through the payroll gestoría.

**(c) Buyers and market size**
- Foreign Social Security affiliates: 3.55M in Aug 2026, 15.9% of 22,345,226 [new: https://www.economistjurist.es/?p=253141, via search snippet].
- Non-EU affiliates: 2,148,064 in Sep 2025 [new: search 6 snippet].
- General-regime foreign affiliates in Jan 2026: 2,537,204, of which 245,104 were in the agricultural special system [new: Junta de Extremadura note, via search snippet].
- Regularised affiliates: 337,917 by end-Aug 2026 [notes: EXP-03]; hostelería took 38,776 of the first 159,097 [new: La Moncloa, 2 Jul 2026].
- The employer count is unknown (C-04 belongs to batch 3). Inference: more than 100k employers have a worker on a temporary or provisional permit. The realistic payers reached through gestorías are about 20k–100k (low confidence).

**(d) Willingness to pay**
- Employers pay nothing today for monitoring. Gestorías charge about €90 per renewal [notes: EXP-03].
- The fine (€10k or more per worker) is a strong argument, but lapses are rare per employer.

**(e) Distribution**
- Payroll gestorías and colegios of graduados sociales.
- Hospitality and farm associations.
- Payroll-software marketplaces (unverified).

**(f) Build feasibility and legal constraints**
- MVP in under 4 weeks: list import, OCR of the TIE expiry, WhatsApp reminders, receipt upload and a board.
- Legal basis: the employer's legal duty not to employ unauthorised workers (LOEX art. 54.1.d) supports processing an authorisation copy and its expiry. Keep it to minimal fields.
- Never contact workers without the employer's lawful basis.
- Stay clear of representation.

**(g) Defensibility**
- None in the product. Factorial or GestoLab can add it.
- The edge is distribution through payroll gestorías.

**(h) Kill criteria**
- Under a third of employers report a lapse, near miss or worry, or under 20% track expiries at all: open [I].
- HR and payroll suites add expiry alerts: **partly met**. Factorial has generic alerts and GestoLab covers the extranjería-gestoría side.
- Fewer than three gestorías want to resell: open [I].
- Lawful basis: not a blocker.

**Type C check.** €5 a month is technically viable: automated, with almost no support. But monthly visible value is low, because alerts fire around renewal events, so churn risk is high. Sell annually (€49 a year) or bundle through gestorías (€29–49 a month per gestoría).

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | Enforced duty with €10,001+ fines, a 2027 deadline wave within 12 months, and live 2026 status changes. |
| S2 Buyers | 3 | Payers reached through gestorías, roughly 20k–100k (inference). |
| S3 Willingness to pay | 2 | No current spend on monitoring; gestorías earn about €90 per renewal. |
| S4 Reachability | 3 | Gestoría and graduado social channels exist; no partner programme yet. |
| S5 Competitive gap | 3 | Generic expiry alerts (Factorial) and extranjería tools (GestoLab), but no employer-side worker workflow. |
| S6 Build speed | 5 | MVP in under 4 weeks. |
| S7 Defensibility | 1 | Trivially copyable. |
| S8 Retention | 3 | Recurring renewals (one to four years) and an inspection log. |
| **Sellability** | **3.13** | |
| P (severity) | 4 | Very large fines and a 2026–27 status wave across hundreds of thousands of workers; the frequency of actual lapses is unknown. |
| **Overall** | **3.48** | 0.6 × 3.125 + 0.4 × 4 |

**Open [I] checks**
- Thirty employers with five or more non-EU staff: lapses, near misses, whether they track expiries.
- Five payroll gestorías: would they resell at €1 per worker a month, and what do they charge for renewals?
- DGGM criteria on negative silence and provisional work rights.

**What would change the verdict**
- **Up to GO:** three or more payroll gestorías pilot before February 2027.
- **Down to KILL:** employers prove indifferent; or a3nom, Sage or Factorial ship immigration-aware renewal workflows.

#### IDEA-58: Beckham-regime filing kit and six-year tracker — KILL (medium)

**Validated definition.** A guided modelo 149 kit at €149 per person: an eligibility check, a deadline clock and pre-filled data, with an optional adviser review. It would add a modelo 151 tracker at €4.99 a month. The rules are clear and stable. But an established Spanish tax app already offers expert-done modelo 149 and 151 filing inside a plan priced "desde 65 €/año", which meets the idea's own kill criterion. Keep only the six-month clock, as a reminder plus hand-off inside IDEA-56.

**(a) Problem reality and rule status (Batch 7 owns the Beckham filing rules)**
- **Deadline.** The option must be exercised "en el plazo máximo de seis meses desde la fecha de inicio de la actividad que conste en el alta en la Seguridad Social en España" (RIRPF art. 116.1.a). Correction: the notes, via a vendor, cite art. 119.4 for this.
- **AEAT response.** AEAT issues the accreditation "en el plazo máximo de los diez días hábiles" (art. 119.4).
- **Exclusion.** Excluded taxpayers "no podrán volver a optar" (art. 118.5).
- **Duration.** The year of residence plus five (art. 115).
- [new: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820, consolidated, seen 23 Oct 2026]
- **Filing.**
  - Modelo 149 is filed only electronically (Orden HFP/1338/2023 art. 8).
  - The taxpayer must first be in the Censo de Obligados Tributarios (art. 7.1). Supporting documents go up through a specific trámite before the 149 (art. 10) [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-25416].
  - Who may file: the taxpayer, voluntary representatives with powers, or colaboradores sociales using their own certificate (Orden HAP/2194/2013 arts. 19–21) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2013-12385].
  - So newcomers without a TIE-based certificate can file through a representative. The Cl@ve-and-NIE part of C-25 stays open, because the official Cl@ve pages do not state the document rules for foreigners [new: https://clave.gob.es/registro/preguntas-frecuentes, seen 23 Oct 2026], but it is no longer blocking.
- **Digital nomads (S\* check, resolved from the BOE text).**
  - Employees teleworking for foreign employers qualify; RIRPF art. 119.2.c lists the employer's letter for remote work.
  - Freelancers qualify only through an ENISA-backed "actividad emprendedora", or as highly qualified professionals serving startups (arts. 113.2 and 119.2.e–f).
- **Doctrine in flux on the main home.** TSJ Madrid exempted it (6 May 2024 and ruling 665/2025). A TEAC unification resolution of 17 Jul 2025 held the opposite. DGT consulta V2467-25 of 11 Dec 2025 points back towards exemption [new: https://es.andersen.com/wp-content/uploads/2026/07/Alerta-LA-VIVIENDA-HABITUAL-BAJO-LA-LEY-BECKHAM-VF.pdf, Jul 2026]. This adds adviser value and liability for any self-serve kit.
- **Election risk: none.** No pending Beckham bill [notes: EXP-10].

**(b) Competitors**
- **TaxDown** [new: https://taxdown.es/extranjeros/calculadora-ley-beckham; https://taxdown.es/extranjeros/modelo-149, updated 19 Oct 2026]:
  - the plan "FULL (desde 65 €/año)" includes "149: Solicitud ley Beckham", "151: Ley Beckham" and "210: No residentes", with "Tu experto hace todo el proceso";
  - on modelo 149: "Revisamos requisitos, preparamos la documentación y la presentamos ante la AEAT dentro de plazo";
  - TaxDown presents itself as a "Colaborador social de la Agencia Tributaria" with "Más de 300 asesores fiscales expertos";
  - the final price "depende de tu situación fiscal", so the price for a Beckham case may exceed €99 (unverified);
  - a free Beckham calculator.
- **Advisers:** €500–1,500 for one person, €800–2,200 for a family [new: Klevvera, 22 Sep 2026].
- **Law firms:** they list Beckham as a separate, unpriced service [new: Lexidy].

**(c) Market size**
- No official count of modelo 149 filings was found (search 7). A 2024 opinion article in Expansión said no statistics exist [new: search 7 snippet].
- The single-source figure of about 37,000 users over a decade [notes: EXP-10] implies about 3,700 a year historically. With the DNV and highly qualified stock growing, the current flow is probably 5,000–10,000 a year (inference, low confidence).
- The "fewer than about 3,000 a year" kill test stays open, but leans not met.

**(d) Willingness to pay**
- People pay advisers €500–1,500, but TaxDown resets the anchor to tens of euros a year.

**(e) Distribution**
- High-intent search ("Ley Beckham modelo 149"), HR and relocation bundles. TaxDown already holds the search and the colaborador social position.

**(f) Build feasibility**
- A rules engine and pre-fill are easy.
- Filing needs a colaborador social or representative partner.
- Liability for eligibility calls is real while the main-home doctrine is unsettled.

**(g) Defensibility**
- None.

**(h) Kill criteria**
- TaxDown or another app offers guided 149 filing at €99 or less: **met in substance**. Expert-done filing comes inside a plan from €65 a year; the exact Beckham-case price was not shown.
- Fewer than about 3,000 new filings a year: open, leaning not met.

**Type A check.** The incumbent advisers' price (€500–1,500) is high, but a cheaper incumbent (TaxDown) already exists. Switching to a €149 kit is not realistic.

**Type C check.** A €4.99-a-month tracker is not viable when TaxDown's annual plan already includes modelo 151.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | A hard six-month option deadline; the loss of the regime is permanent. |
| S2 Buyers | 2 | Probably 5k–20k new eligible people a year plus some HR buyers (inference). |
| S3 Willingness to pay | 2 | TaxDown sets the anchor at about €65+ a year. |
| S4 Reachability | 3 | High-intent search, but TaxDown and advisers dominate it. |
| S5 Competitive gap | 2 | Several decent options, including a cheap expert-done service. |
| S6 Build speed | 4 | 1–2 months, with a partner colaborador social. |
| S7 Defensibility | 1 | None. |
| S8 Retention | 3 | Six annual modelo 151 returns. |
| **Sellability** | **2.75** | |
| P (severity) | 3 | Costly for the individual who misses it, but a one-off event and not widespread. |
| **Overall** | **2.85** | 0.6 × 2.75 + 0.4 × 3 |

**Open [I] checks**
- TaxDown's actual price for a Beckham 149 case.
- Whether HR teams would pay €99 per employee for a reminder plus hand-off.

**What would change the verdict**
- TaxDown's Beckham price turns out to be far above €99 and its service poor (review evidence).
- HR bulk demand appears. Even then, the product is better as IDEA-56's clock than as a standalone kit.

## 3. Cross-cutting findings

### 3.1 Rule status established by batch 7 (the shared checks this batch owns)

| Topic | Finding (23 Oct 2026) | Source | Election or lapse risk |
|---|---|---|---|
| **RD 316/2026 renewal rules (DA 20 and DA 21)** | **Validity:** one year. **2027 step:** a "modificación conforme al artículo 191", filed in the two months before expiry. DA 21 uses "deberán"; DA 20 "podrán". **Pending filing:** keeps the permit valid until resolution; a three-month late grace exists, but late filing is a minor infraction. **Fallback:** a one-year extension for job search or an integration report, or four years for justified reasons. **Retroactivity:** the grant's effect is backdated to the filing date, so expiries probably fall in Apr–Jun 2027 and windows open from Feb 2027 (inference). **Requirements:** art. 191.3 points to art. 80 or 86, and the new permit lasts four years. **Who files:** the employer or the worker (art. 191.5). **Office checks:** criminal records ex officio (arts. 80.5, 86.5). **Silence:** positive after three months (art. 80.9). **Not automatic.** | BOE-A-2026-8284; consolidated BOE-A-2024-24099 | None: royal decrees need no convalidation. A new government could amend in 2027. |
| **Provisional work right of regularisation applicants** | **During processing:** applicants may work. **On resolution:** the worker must inform the employer. **On denial:** "automática pérdida de la habilitación provisional para trabajar". **Deadline:** three months, after which the application is deemed rejected by silence (DA 21.4). How silence affects the provisional right is ambiguous; check the DGGM criteria. | BOE-A-2024-24099, DA 21.4 | None. |
| **Supreme Court partial annulment of RD 1155/2024** | **Rulings:** STS 868/2026 of 8 Jul 2026 (recurso 19/2025; rectification order of 1 Sep 2026) and STS of 29 Jul 2026 (recurso 21/2025, Cáritas, CEAR and others). Both were published in the BOE on 22 Sep 2026 (BOE-A-2026-19632 and -19633). **Annulled:** art. 101.1 para. 3 (temporary-work agencies and seasonal permits); incisos of art. 94.1.f, art. 196.b (ascendants' dependency), arts. 97.4 and 98.1 (automatic denial for criminal records in TFEU art. 20 cases), arts. 159.1 ("solteras"; absence since birth), art. 160.1 ("solteros"), art. 160.2 and art. 166.1 ("en su caso"); and **art. 197.2 in full**. The government may re-impose compulsory e-filing only with a justified, proportionate rule (Ley 39/2015 art. 14.3). **Everything else was upheld.** The notes' partial list is confirmed and completed. | BOE txt pages | None: final rulings. |
| **Police fingerprint-appointment pilot** | **Start and scope:** from 8 Oct 2026, "inicialmente un 10%" of files resolved from that date. It had already begun elsewhere, including Girona, Tarragona and Lleida "así como en el resto del territorio Nacional", and from 9 Oct covers Madrid, Barcelona, Valencia, Alicante, Málaga and Murcia. **Notices:** email and SMS. **Fallback:** without an appointment within 20 days, book on the web. **Roll-out:** "fase de prueba"; full roll-out undecided. **Clarification of 16 Oct 2026:** still 10% (secondary source). **Málaga:** nearest station; notices to the applicant or representative; cancelling re-queues the person; conditional grants (pending entry to Spain or pending Social Security alta) excluded. **A Coruña:** since June 2026. **Renewal TIEs:** coverage not stated (open). | ICAB PDF; Málaga OFEX note; ARC Legal (snippet) | Administrative practice; none. |
| **Who may file on behalf of others** | **Any representative:** "cualquier persona física o jurídica" may represent with a notarial power or an apud-acta entry in the electronic powers register (RD 1155/2024 art. 197.4.a). **Convenio professionals** under Ley 39/2015 art. 5 (abogados, gestores administrativos, graduados sociales) file with simpler mandates and may be required to keep representation registers (art. 197.4.b). **Registered collaborators** (unions and NGOs; free representation under Orden ISM/164/2026) (art. 197.4.c). **Bar associations** may file centrally for their members under a 2024 protocol (BOE-A-2024-6698, via search 12 snippet). **Companies** can file their own UGE highly qualified applications (Ley 14/2013 art. 71.1) and the art. 191 modification for their workers (art. 191.5). **Personal appearance:** met by electronic filing when the applicant is in Spain (art. 197.1). | BOE consolidated texts | None. |
| **Beckham-regime filing rules** | **Deadline:** six months from the start date on the Social Security alta (RIRPF art. 116.1.a); the notes' "art. 119.4" is wrong for the deadline. **AEAT certificate:** within ten working days (art. 119.4). **Exclusion:** permanent (art. 118.5). **Duration:** six years (art. 115). **Filing:** modelo 149 electronic only (Orden HFP/1338/2023 art. 8), after census registration. **Who files:** the taxpayer, apoderados or colaboradores sociales (Orden HAP/2194/2013 arts. 19–21). **Teleworking employees of foreign firms:** eligible. **Freelancers:** only through ENISA or startup routes. **Main-home doctrine:** conflicting (TEAC, 17 Jul 2025, against TSJ Madrid and DGT V2467-25). | BOE-A-2007-6820; BOE-A-2023-25416; BOE-A-2013-12385; Andersen | None. |
| **C-25 items** | **Reunification deadline: settled.** Two months, negative silence (art. 68.6). **June 2026 thresholds: settled.** Orden PJC/44/2026 covers the Blue Card only; the national PAC uses the same €41,356.36 in practice (practitioner source). **UGE fee: open.** €73.26 per Klevvera, Sep 2026. **TIE waits: open.** Still only commercial figures, plus the official pilot. **Cl@ve and NIE: open,** but not blocking for AEAT filings because representatives can file. **Madrid padrón: not checked.** | see ideas | — |
| **UGE annual grants (owned for IDEA-56)** | Not published in any source reached. The stock remains the anchor. | searches 1, 10 | — |

### 3.2 Facts that matter outside batch 7

- **Batch 3 (employers; C-04).**
  - **SMI 2026:** €1,221 a month in 14 payments (RD 126/2026, BOE-A-2026-3815, in force 20 Feb 2026 and applying from 1 Jan 2026).
  - **Foreign affiliates:** 3.55M (15.9% of 22,345,226) in Aug 2026 (search 6 snippet); non-EU 2,148,064 (Sep 2025); general-regime foreign 2,537,204 (Jan 2026).
  - **Fines:** €10,001–100,000 per worker employed without authorisation (LOEX arts. 54.1.d and 55.1.c).
  - **Domestic and care employers:** regularised domestic workers need the art. 191 modification in 2027, and the employer can file it. This matters for IDEA-19 and IDEA-44.
  - **Factorial:** from €5.5 per person a month, with generic document-expiry alerts. An incumbent feature for IDEA-16 and IDEA-41.
  - **TGSS:** its check of authorisations at the alta is unverified (ADEXTRA, 2024 minutes).
- **Batch 2 (gestorías, rule feeds).**
  - **GestoLab:** €79–199 a month (VAT included) with unlimited files. Apparently built by a solo founder with AI. It ships 26 forms, a Mercurio extension, DEHú triage, an AI copilot and a Claude connector. It is a price anchor for gestoría SaaS and direct evidence of the user's "AI flood" thesis: features are cheap, distribution decides.
  - **BOE open-data API:** returns consolidated texts block by block with version dates. Useful for IDEA-06 and IDEA-18.
  - **Ministry pages blocked:** Ministerio de Inclusión pages return 403 to automated access, and the sede.administracionespublicas pages return 503.
- **Batches 1 and 2 (tax tools).** TaxDown is a colaborador social with plans PRO from €35, LIVE €45 and FULL €65 a year, and covers modelos 149, 151 and 210. A price anchor for IDEA-08 and IDEA-09.
- **All batches (legal design rules).**
  - **Criminal-record data:** LOPDGDD art. 10.3 allows processing of client-provided criminal data outside a specific legal norm only by abogados and procuradores. Ideas that touch sexual-offence or criminal certificates (IDEA-31 tenant screening, IDEA-41 staff files, IDEA-44 home-help staff, IDEA-19) need a specific legal basis, such as the minors-protection duty, and art. 10 safeguards.
  - **AI Act:** Annex III points 7 and 8 cover tools used by or for public or judicial authorities. Private professional tools in this longlist are not Annex III high-risk on these points (my reading).
  - **ICAM's proposal (18 Feb 2026)** to criminalise automated legal advice without a professional (Penal Code art. 403) excludes tools used by professionals. It lapses with the dissolution (inference), but expect it to return. Design IDEA-01, IDEA-17 and IDEA-08 with a professional in the loop, or give general information only.
- **Election (29 Nov 2026).**
  - None of batch 7's rules rests on a pending bill or a decree-law awaiting convalidation: LOEX and Ley 14/2013 are laws; RD 1155/2024 and RD 316/2026 are regulations; the thresholds are a ministerial order.
  - The caretaker government can keep issuing DGGM criteria and police instructions.
  - Pending items lapse: the ICAM art. 403 proposal and the homologación reform [notes: EXP-11].
- **Correction to the stage-2 U2 table.** The notes rated "HR teams and agencies as filing buyers" as partly contradicted. Validation finds the legal bar weaker than stated: companies are legitimate UGE applicants, and any person can represent with a notarial or apud-acta power. The practical bar remains: professionals with convenios dominate filing, and HR buys services. (In this file, the IDEA-52 U2 table's phrase "The notes' 'contradicted'" refers to that "partly contradicted" rating.)

## 4. Search log

**WebSearch calls: 22 of the 24 allowed.** 2 were left unused.

| # | Query | Idea(s) | Result |
|---|---|---|---|
| 1 | Unidad de Grandes Empresas autorizaciones concedidas 2025 nómadas digitales altamente cualificados cifras anuales | 52, 56 | No annual grant data. |
| 2 | UGE denegación visado nómada digital 2026 motivos requerimiento extractos bancarios seguro copago "criterio de gestión 2/2025" | 52 | Practitioner denial reasons; Criterio 2/2025 not found. |
| 3 | software gestión despachos extranjería inteligencia artificial expedientes Mercurio abogados gestorías 2026 | 52 | NIM (law firm), INSZoom, generic legal software. |
| 4 | regularización extraordinaria resoluciones favorables concedidas autorizaciones octubre 2026 balance Ministerio Inclusión | 53, 57 | No post-July balance. |
| 5 | Factorial Sesame Woffu Personio alerta caducidad documentos empleado permiso de trabajo NIE vencimiento | 57 | Factorial document-expiry alerts. |
| 6 | afiliados extranjeros Seguridad Social septiembre 2026 récord hostelería agricultura construcción régimen general extracomunitarios | 57 | Aug 2026 totals; no sector split for 2026. |
| 7 | número de contribuyentes régimen especial trabajadores desplazados Ley Beckham modelo 149 Agencia Tributaria cifra anual 2024 2025 | 58 | No official count; doctrinal conflict found. |
| 8 | suscripción de pago novedades extranjería para abogados boletín alertas normativas extranjería Lefebvre Aranzadi vLex Machelin Díaz Parainmigrantes | 54 | Free ARC Legal newsletter; no paid tiers. |
| 9 | Oficina de Extranjería Barcelona tiempos de resolución expedientes 2026 retraso meses arraigo reagrupación cuenta ajena datos | 55 | Lawyer estimates of 6–9 months. |
| 10 | "Unidad de Grandes Empresas" empresas inscritas número inscripción tres años Ley 14/2013 movilidad internacional empresas registradas | 56 | No count; ICT collective-processing criterion. |
| 11 | AI tool Spain digital nomad visa application review bank statements check eligibility platform lawyers 2026 | 52 | No AI pre-check tool; 2026 thresholds. |
| 12 | cuántos abogados de extranjería hay en España colegiados especializados extranjería convenio Mercurio número abogados adheridos | 52, 53 | More than 14,000 in the Registro de Representantes (2021). |
| 13 | intrusismo asesoramiento jurídico extranjería sin ser abogado gestores administrativos plataformas online legal España artículo 403 Código Penal asesoría | 52 | Penal Code art. 403 doctrine; ICAM 2026 proposal. |
| 14 | empresa comprobar autorización de trabajo trabajador extranjero vigente consulta online TGSS Sistema RED alta trabajador extranjero autorización caducada | 57 | TGSS ADEXTRA check pending (2024). |
| 15 | "consulta del estado de los expedientes de extranjería" qué muestra estado "en trámite" "resuelto favorable" fecha estimada número expediente NIE sede | 55 | Status only; no expected date. |
| 16 | asignación automática cita toma de huellas TIE policía ampliación porcentaje resultados octubre 2026 renovaciones excluidas | 56, 52 | 16 Oct clarification; Málaga note; A Coruña. |
| 17 | programa software para gestorías de extranjería rellenar formularios EX automáticamente expedientes clientes alternativa GestoLab | 52, 53, 57 | No other extranjería SaaS found. |
| 18 | Spain extranjería processing times tracker crowdsourced timelines spreadsheet community residency application wait times by province 2026 | 55 | No crowdsourced tracker. |
| 19 | asociación empresas de relocation España socios EuRA miembros Spain relocation companies association number members destination services | 56 | EuRA directory. |
| 20 | Elma Saiz regularización extraordinaria autorizaciones concedidas resueltas favorablemente cifra septiembre octubre 2026 | 53, 57 | 262,475 affiliated (4 Aug); no grant count. |
| 21 | a3nom Sage Nominasol aviso caducidad permiso de trabajo trabajador extranjero fecha fin autorización residencia nómina alerta | 57 | No payroll feature found. |
| 22 | GestoLab extranjería inteligencia artificial gestorías startup Daniel Martín García clientes lanzamiento | 52, 53 | No press footprint. |

**Searches by idea**

| Idea | Dedicated | Shared | Total touching the idea |
|---|---|---|---|
| IDEA-52 | 6 | 3 | 9 |
| IDEA-53 | 2 | 3 | 5 |
| IDEA-54 | 1 | 0 | 1 |
| IDEA-55 | 3 | 0 | 3 |
| IDEA-56 | 2 | 2 | 4 |
| IDEA-57 | 4 | 2 | 6 |
| IDEA-58 | 1 | 0 | 1 |

Shared searches are counted under each idea they served. The plan's [F] checks were all done by direct fetch, which costs no searches.

**Main pages fetched directly (not counted against the budget)**
- **BOE, legislation.** Through the BOE open-data API (`/datosabiertos/api/legislacion-consolidada/...`, an official database query, not a general search engine) or the ELI and txt pages:
  - RD 316/2026 (BOE-A-2026-8284);
  - RD 1155/2024, consolidated to 22 Sep 2026 (BOE-A-2024-24099), arts. 68, 80, 86, 191, 197 and DA 20/21;
  - Ley 14/2013 (BOE-A-2013-10074), arts. 71, 74 ter, 75, 76;
  - Orden PJC/44/2026 (BOE-A-2026-2142);
  - RD 126/2026 (BOE-A-2026-3815);
  - Orden PJC/617/2025 (BOE-A-2025-12056);
  - RIRPF (BOE-A-2007-6820), arts. 113–120;
  - Orden HFP/1338/2023 (BOE-A-2023-25416);
  - Orden HAP/2194/2013 (BOE-A-2013-12385);
  - LOPDGDD (BOE-A-2018-16673), arts. 10 and 28;
  - LOEX (BOE-A-2000-544), arts. 52, 54, 55;
  - Reglamento General de Conductores (BOE-A-2009-9481), art. 21.
- **BOE, rulings:** BOE-A-2026-19632 and BOE-A-2026-19633.
- **Official notices:** the ICAB PDF of the DGP pilot notice; the Madrid Delegación extranjería page, its "2026 10 OCT.pdf" and its "Nota_empleadores.pdf"; the OFEX Málaga note (hosted by ARC Legal).
- **La Moncloa:** the 2 Jul 2026 regularisation balance and the 20 Mar 2026 resident population note.
- **AI Act:** Annex III at artificialintelligenceact.eu (EUR-Lex returned an empty page).
- **Cl@ve:** registration pages and FAQ.
- **Vendors and competitors:**
  - GestoLab: home, /producto, /abogados-extranjeria, /calculadora-plazos;
  - Jobbatical pricing; Localyze pricing; Deel pricing and Spain blog;
  - TaxDown Beckham calculator and modelo 149 pages;
  - Extranjería App;
  - Anchorless, Nomadlex, Cicerai, NIM Extranjería;
  - Klevvera DNV cost breakdown; Lexidy DNV;
  - Factorial ES and PT blogs; Sage ES blog.
- **Practitioner pages:**
  - España Abogados resolution-date table;
  - Machelin Díaz on thresholds, DNV denials and Barcelona delays;
  - Cohen y Aguirre on 2026 DNV requirements and provincial times;
  - ARC Legal newsletter and Extranjería Legal Substack;
  - LegalToday on the ICAM art. 403 proposal;
  - Andersen's Beckham alert (Jul 2026);
  - the EuRA member directory filtered to Spain (5 pages).
- **Blocked or unavailable:**
  - inclusion.gob.es instructions and UGE pages: HTTP 403;
  - sede.administracionespublicas.gob.es: HTTP 503;
  - infoextranjeria.org: 503;
  - myspanishdnv.com: 403;
  - EUR-Lex HTML: empty;
  - the Parainmigrantes seminar page: empty.

**Checks left open:**
- annual UGE grants by type;
- the number of DA 20/21 grants and their stated expiry dates;
- the number of companies registered with the UGE;
- AEAT modelo 149 statistics;
- EX-13 practice after Instrucción 1/2026;
- renewal-TIE coverage of the police pilot;
- payroll-suite permit features;
- legal-database alert prices;
- Cl@ve document rules for foreigners;
- the Madrid padrón conflict;
- every [I] interview test listed under each idea.
