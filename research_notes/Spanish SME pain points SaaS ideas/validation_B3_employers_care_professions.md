# Validation, batch 3 of 8: employers, care and regulated professions

*Validator: batch 3. Status date: 23 October 2026 (Cortes dissolved 6 Oct 2026; general election 29 Nov 2026).*
*Ideas: IDEA-16, IDEA-17, IDEA-18, IDEA-19, IDEA-40, IDEA-41, IDEA-42, IDEA-43, IDEA-44.*
*Citation forms: [new: URL, date seen or published] for evidence gathered in this validation; [notes: PAIN-ID] for stage-1 evidence. "Single source" is marked where only one source supports a claim.*

*Searches used: 22 of the 24 allowed (log in section 4). Direct fetches of BOE, INE, ministry, colegio, vendor and app-store pages were unlimited. Several official statistics sites were down during validation (mites.gob.es 503, MAPA 503, REGCESS 403), and the open checks say so.*

## 1. Batch summary table

Scores are 1–5. Sellability is the mean of S1–S8. Overall = 0.6 × Sellability + 0.4 × P. IDEA-17 is scored in its reshaped form; all others as specified.

| ID | Name | Type | Verdict | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Sellability | P | Overall | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IDEA-16 | Labour compliance pack for micro employers (gestoría white-label) | A (C) | KILL | 3 | 5 | 4 | 3 | 1 | 4 | 1 | 4 | 3.13 | 3 | 3.08 | high |
| IDEA-17 | Dismissal workflow, reshaped to an adviser-only pre-termination risk check | B | RESHAPE | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 3 | 3.00 | 4 | 3.40 | low |
| IDEA-18 | Convenio rules database and API | B | KILL | 3 | 2 | 4 | 3 | 2 | 2 | 3 | 4 | 2.88 | 3 | 2.93 | medium |
| IDEA-19 | Household-employer autopilot | C (B) | KILL | 2 | 4 | 3 | 2 | 3 | 4 | 2 | 3 | 2.88 | 2 | 2.53 | medium |
| IDEA-40 | Private-pay and reimbursement kit for health professionals | B | KILL | 2 | 3 | 3 | 3 | 4 | 4 | 2 | 2 | 2.88 | 4 | 3.33 | medium |
| IDEA-41 | RD 239/2026 staff qualification file | C (B) | KILL | 4 | 3 | 2 | 3 | 3 | 5 | 1 | 2 | 2.88 | 2 | 2.53 | medium |
| IDEA-42 | PRESVET and antibiotic-stewardship file for vet clinics | C (B) | KILL | 2 | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2.38 | 2 | 2.23 | medium-high |
| IDEA-43 | Driving-school exam-readiness tracker | B | KILL | 3 | 2 | 2 | 2 | 2 | 5 | 1 | 3 | 2.50 | 3 | 2.70 | medium |
| IDEA-44 | SAD route planning and visit verification | B | KILL | 3 | 1 | 3 | 2 | 2 | 3 | 2 | 4 | 2.50 | 3 | 2.70 | medium-high |

**Batch verdict in one line:** no GO. The batch's labour and care problems are real (P of 3–4 for IDEA-16, 17, 40, 43 and 44), but each product's gap is closed by one of the following:
- incumbents: a3/Wolters Kluwer, TeamSystem-DELSOL, Timu, Woffu, PayFit, Gesad, CIBERSAD;
- free official tools: Import@ss, Prevencion10, INSST, REPS, PRESVET web services;
- free sector apps (the CNAE's instructor app, Control-L);
- or a rule that turned out weaker than the notes said (the PRESVET fine is now minor; the RD 767/2025 duty binds farms, not clinics; the RD 723/2026 breach is a minor LISOS infraction).

IDEA-17 survives only as a narrow, AI-exposed adviser tool that needs interview evidence before any build.

## 2. Ideas

#### IDEA-16: Labour compliance pack for micro employers, white-labelled for gestorías — KILL (high)

**Validated definition.** As specified: an A-type, gestoría-resold pack for 1–10-employee employers (clock-in with tamper-evident log, RD 723/2026 statement generator, harassment and prevention templates, inspection vault, gestoría console) at €6/month for 3 employees. Validation found no price headroom and no open channel: the time-recording core is saturated down to €0, and the two payroll suites that gestorías already use sell the same client-and-employee portal. Killed as a standalone product. The one non-commodity piece (RD 723 statement generation, change notices and the 30-working-day request clock) should be carried as a module of IDEA-06 (gestoría cockpit, batch 2), not built alone.

**(a) Problem reality and rule status (Oct 2026)**
- Daily time records have been mandatory since 12 May 2019 (art. 34.9 ET). Paper is still legal. Failing to keep the record is a grave infraction under LISOS art. 7.5, fined €751–1,500 (minimum), €1,501–3,750 (medium) or €3,751–7,500 (maximum) per infraction (LISOS art. 40.1.b) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2000-15060, consolidated text seen 23 Oct 2026] [notes: LAB-01].
- **Digital time-recording decree (batch 3 owns this check): not approved as of 23 Oct 2026.**
  - Not in the BOE and absent from the 6, 13 and 20 Oct Councils of Ministers [new: https://controlhorariolegal.com/normativa-fichaje-2026, "Última revisión: 23 de octubre de 2026", vendor]. Not approved as of 19 Oct [new: https://www.evicron.com/blog/registro-horario-digital-rdley-8-2019-guia-empresas, updated 19 Oct 2026, vendor]. On 2 Oct the Secretary of State said the text review could be "dar por concluido" and that it should reach the Council "a lo largo de octubre" [new: https://fichme.com/noticias/registro-horario-digital-ultima-hora, updated 5 Oct 2026, vendor]. All sources are time-tracking vendors; no official source shows a date.
  - The Consejo de Estado's opinion was unfavourable: "no procede aprobar el real decreto proyectado"; 1.35M companies, about €867M a year; caretakers, train drivers and hospitality flagged; AEPD concerns shared; a broad transition recommended [new: https://www.elespanol.com/invertia/economia/empleo/20260323/consejo-critica-tumba-registro-horario-yolanda-diaz/1003744181041_0.html, 23 Mar 2026]. Fichme dates the opinion 19 Mar 2026 and says it called the 20-day transition "manifiestamente insuficiente".
  - **Election mechanics (settled from the BOE):** the Government "cesa tras la celebración de elecciones generales" and then "limitará su gestión al despacho ordinario de los asuntos públicos", except "casos de urgencia debidamente acreditados" or "razones de interés general" that it must expressly justify (Ley 50/1997, art. 21.1 and 21.3) [new: https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336, seen 23 Oct 2026]. As a royal decree (not a decree-law), it needs no convalidation. The realistic window is therefore the Councils of 27 Oct and 3, 10, 17 and 24 Nov 2026. After 29 Nov, approval by a caretaker government would need an express urgency justification and would be open to challenge (my inference from art. 21.3). If it is not approved by 24 Nov, it stalls until a new government is formed (the new chambers meet on 23 Dec 2026), and a different majority could drop it. Evicron's view: "el freno es político, no jurídico".
  - Transition still unsettled: 6 months (Trabajo) against 12 months for pymes (Economía); the draft text would enter into force 20 days after BOE publication [new: https://www.registrahora.es/noticias/registro-horario-digital-aplazado-septiembre-2026, updated 13 Oct 2026, vendor].
- **RD 723/2026 (settled from the BOE).** BOE 15 Sep 2026; in force 5 Oct 2026; applies to all employers under art. 1 ET; the general-information chapter covers relationships "cuya duración sea superior a cuatro semanas" (art. 2.2). Information is due "con carácter previo al inicio de la relación laboral" (art. 7.1), and changes "a más tardar, el día en que el cambio surta efecto" (art. 7.3). Existing staff who ask must get it within "treinta días hábiles" (DT única). Delivery may be on paper or electronic, and "la empresa conserve la prueba de la transmisión o recepción" (art. 6.2). The duty is deemed met if the written contract already contains the information (art. 3.1). The SEPE had to publish a model document within 20 days of publication (DA 1ª), and the decree says the model's availability does not condition enforceability. The decree sets no sanctions [new: https://www.boe.es/eli/es/rd/2026/09/09/723, seen 23 Oct 2026].
- **LISOS answer:** "No informar por escrito al trabajador sobre los elementos esenciales del contrato" is a **minor** infraction (LISOS art. 6.4), fined €70–150, €151–370 or €371–750 (art. 40.1.a) [new: BOE LISOS consolidated text, as above]. So a missing RD 723 statement costs at most €750 per infraction. Exposure comes mainly from complaints and litigation, which the Barcelona graduados sociales expect to rise ("habrá un aumento de las denuncias ante la Inspección de Trabajo") [new: https://www.lawandtrends.com/noticias/laboral/el-colegio-de-graduados-sociales-de-barcelona-girona-y-lleida-alerta-del-impacto-del-rd-723-2026-en-la-gestion-y-el-1.html, updated 2 Oct 2026].
- **SEPE model document:** not verified; the SEPE contract-models page returned HTTP 503 on 23 Oct 2026. Open.
- **Enforcement scale:** the ITSS proposed €858.26M in sanctions in 2025 (+58.62%) across 1,206,028 actions and 427,495 workplaces, with 11,824 anonymous-complaint cases. The report summary gives no working-time breakdown [new: https://elderecho.com/?p=489934, 7 Oct 2026]. Working-time fines: €17.2M from 13,681 infractions in 2024 [notes: LAB-02], and €15.7M from 14,728 infractions in 2025, a figure Finantres attributes only to "La Inspección" with no report cited [new: https://finantresnoticias.com/negocios-y-autonomos/multas-por-incumplir-horario-se-triplican-deben-revisar-ahora-pymes/, 25 Aug 2026]. **C-18 remains unresolved:** the scopes may differ, and the ITSS report summary does not settle it. Either way, about 14,000 working-time infractions a year against about 1.23M employers is roughly a 1% annual chance per employer (my arithmetic). Expected fines are small; the costly event is an overtime claim, where STS 372/2026 can take a worker's concrete hours as true when there is no record [notes: LAB-02].
- **Employer count (C-04), settled for all batches.** The three figures measure different things:
  - INE DIRCE, 1 Jan 2025: 1,510,381 companies with employees (3,310,824 total minus 1,800,443 with none). By size: 901,955 with 1–2 employees, 314,941 with 3–5, 132,013 with 6–9, 85,467 with 10–19 and 76,005 with 20 or more [new: https://www.ine.es/dyngs/Prensa/DIRCE2025.htm, published 11 Dec 2025].
  - INE CODEM, 2026Q2: 1,231,358 employer legal units with at least one employee registered with Social Security [notes: CITY anchors; G5 macro].
  - Consejo de Estado: 1.35M, base not stated. It sits between the two, and is numerically almost identical to DIRCE's 1–9 band (1,348,909), which may be a coincidence.
  - Use CODEM for paying entities and DIRCE for the size split. Micro firms (1–9) are 89.3% of DIRCE employers, which implies about 1.10M micro employer units on the CODEM base (my inference).
- No survey of the share of firms still keeping paper records was found. Open.

**(b) Competitors (prices as published, excl. VAT)**

| Product | Price | Fit for 1–10 staff | Notes |
|---|---|---|---|
| Woffu Lite | "Desde 1,5 €" per user/month, "hasta 10 empleados", monthly or annual, cancel any time | Direct | Geolocation and IP limits, basic reports and Excel/PDF export. QR and PIN clock-in only on Enterprise [new: https://www.woffu.com/es/precios, seen 23 Oct 2026] |
| Timu (Nimbo Software) | €9/month for 3 seats (€3/seat), then €2.50 for seats 4–20; €90/year | Direct, same price point as IDEA-16 | Audit trail with "doble autorización en correcciones", immutable records kept 4 years, PDF/CSV export; an ITSS API is "Próximamente"; multi-company panel for asesorías [new: https://timu.es/precios, seen 23 Oct 2026; launch: https://www.rrhhdigital.com/secciones/pymes/798970/la-nueva-plataforma-que-prepara-a-pymes-y-autonomos-para-la-inminente-normativa-de-control-horario/, 4 Jul 2026] |
| TeamSystem (DELSOL) Gestión de Empleados | €2.00 per employee/month or €24/year | Direct; built for the gestoría hand-off | Geolocated clock-in, absences, documents, expenses, payslip delivery. "El rol de asesor es gratuito", with one adviser login for many companies; feeds Nominasol payroll [new: https://www.sdelsol.com/gestion-de-empleados/, seen 23 Oct 2026]. Nominasol itself lists "Registro diario de jornada" [new: https://www.sdelsol.com/programa-nominas-nominasol/, seen 23 Oct 2026] |
| Wolters Kluwer a3innuva Nómina + Portal del empleado + a3gestión del tiempo / a3HRgo | Not published | Direct; the default gestoría suite | A "solución laboral colaborativa" between the despacho, client firms and employees: clients enter new hires, variables, sick leave and leave; employees get a free app; e-signature; time management "que permite cumplir la normativa de registro de jornada"; a3HRgo sells "solo el servicio de control horario y portal del empleado" [new: https://assets.contenthub.wolterskluwer.com/api/public/content/d515a50d17e347909eb536cc5b9828dc, product sheet seen 23 Oct 2026; search snippets for https://www.wolterskluwer.com/es-es/solutions/a3hrgo-para-empresa, 23 Oct 2026; direct pages returned 403] |
| Holded HR add-on | €1.50 per employee/month | Direct for Holded users | Scope not stated [new: https://www.infoautonomos.com/blog/mejor-programa-facturacion-pymes/, updated 25 May 2026] |
| Jibble | "Free forever · Unlimited users" | Partial: not Spain-specific | Mobile and web clock-in, basic timesheets [new: https://www.jibble.io/pricing, seen 23 Oct 2026] |
| Sesame HR | €4.75–8.00 per employee (card prices), "el mínimo de contratación son 15 empleados" | Poor (minimum) | Has an asesorías partner programme; integrates a3innuva [new: https://www.sesamehr.es/precios/, seen 23 Oct 2026] |
| Factorial | "desde 5€" / "desde 5.5€" per person, modules by quote | Poor | Core includes documents and e-signature; a "Factorial Professionals" portal for advisers [new: https://factorial.es/pricing, seen 23 Oct 2026]. Complaints about cancellation and support [notes: VOX table] |

- One search on the decree alone surfaced at least nine Spanish fichaje vendors publishing compliance guides (TramitApp, ControlLaboral, Fichme, ESI Soluciones, RegistraHora, ControlDeJornadaLaboral, ControlHorarioLegal, Evicron and others) [new: WebSearch results, 23 Oct 2026]. The category is crowded and SEO for "registro horario" is contested.
- **Gap:** none on price, segment or Spanish compliance for time recording. A dedicated RD 723 statement generator was not found, but incumbents already hold the inputs (contract, convenio, documents, e-signature: a3innuva, Factorial Core) and can add it cheaply.

**(c) Buyers and market size.** About 1.10–1.35M micro employers (see C-04 above). The reachable share through gestorías that are not already on a3 or DELSOL portals is unknown. Ceiling at the hypothesis: 100,000 firms at about €8/month is about €9.6M ARR (my arithmetic), but price competition (€2/employee with free adviser seats) caps realistic ARPU near €4–6 a firm.

**(d) Willingness to pay.** Buyers already pay €1.5–3 per employee for time recording (Woffu, Timu, DELSOL, Holded), and €15–20 per payslip to gestorías [notes: LAB-21]. Willingness to pay exists, but at today's commodity prices. A type-A "cheaper alternative" has no room below €1.5–2 per employee or a free tier.

**(e) Distribution.** The gestoría channel is real and concentrated, but incumbents own it: DELSOL gives advisers free seats, a3innuva is the gestorías' default payroll suite ("la opción obligada si tu asesor externo lo usa" [notes: LAB-24, VOX]), and Sesame and Factorial run adviser partner programmes. A new entrant would need gestorías to add a second portal alongside their payroll vendor's.

**(f) Build feasibility.** MVP in 4–6 weeks for a small team. If the decree passes, it requires unalterable records, remote ITSS access and traceable corrections [notes: LAB-01]. Data protection: avoid biometrics and limit geolocation (AEPD and Consejo de Estado concerns). No certification is needed.

**(g) Defensibility.** None. The product is trivially copyable and incumbents control the channel and the payroll data. Kept-current compliance content is replicated in vendors' SEO guides.

**(h) Kill criteria**
- "a3innuva or another major payroll suite already gives gestorías an equivalent client portal at no extra cost": **met in substance, not to the letter.** Equivalent portals exist at both leading gestoría suites (a3innuva Portal del empleado with time management; DELSOL Gestión de Empleados). DELSOL charges €2 per employee but makes the adviser role free; a3's price is unpublished. The gap the criterion protects is gone.
- "a 10-gestoría pilot converts fewer than 15% of employer clients within 3 months": **open [I]**, but the pilot is not worth running given the competitor evidence.

**Scores**
- S1 Urgency **3**: duties are in force, but the decree is uncertain and fines are per infraction with about a 1% yearly inspection chance; the RD 723 breach is minor (€70–750).
- S2 Buyers **5**: about 1.1–1.35M micro employers.
- S3 Willingness to pay **4**: clear adjacent spend on fichaje apps and gestorías, at commodity prices.
- S4 Reachability **3**: concentrated gestoría channel, but locked by a3 and DELSOL portals.
- S5 Competitive gap **1**: saturated, including a free tier (Jibble) and €1.5–3 per employee offers fitted to micro firms.
- S6 Build speed **4**: 4–6 weeks.
- S7 Defensibility **1**: trivially copyable; incumbents hold channel and data.
- S8 Retention **4**: recurring legal duty plus four years of accumulated records.
- **Sellability 3.13; P 3** (moderate: overtime claims cost thousands when they occur, but the per-firm probability is low); **Overall 3.08.** Confidence high: rules from the BOE, competitor prices from vendor pages.

**Open [I] checks:** the gestoría resale pilot (no longer recommended); the share of micro firms on paper; whether the SEPE model document is out (fetch failed).

**What would change the verdict:** a3 and DELSOL raising client-portal prices sharply, or gestorías reporting that clients refuse their payroll vendor's portal. A decree approved with a transition would raise urgency, but it would favour incumbents that are already decree-ready (Timu, a3, DELSOL) rather than a new entrant.

#### IDEA-17: Guided dismissal and termination workflow for owner-managers and their advisers — RESHAPE (low)

**Validated definition (reshaped).** Drop the owner-facing €49-per-termination product and the letter generator as a selling point; letter drafting and severance maths are now free (calculators, AI prompt guides). Sell only to advisers (graduados sociales, gestorías' labour departments and small labour firms) at about €29–49 a month. The core becomes a **pre-termination risk check and evidence file** kept current with case law and Social Security criteria:
- the hearing step under STS 1250/2024;
- a retaliation screen under STS 526/2026;
- notice-pay coding under CRA 0054 (RED 8/2026);
- the Ley 2/2025 permanent-incapacity clocks;
- a client-facing intake so the owner calls the adviser before acting.

Go-to-market is through one colegio partnership first. This is a narrow, AI-exposed product. It survives only if advisers say publishers' AI tools and templates do not already cover the procedural checks.

**(a) Problem reality and rule status**
- Dismissal claims reached a record 45,230 in Q2 2026 (+11.2%; the CGPJ series starts in 2007). Cataluña had 9,075, Madrid 8,040, Andalucía 7,302 and the Comunidad Valenciana 5,885. Wage claims were 35,043 (+3.4%) [new: https://www.lawandtrends.com/noticias/laboral/las-demandas-por-despido-marcan-record-en-el-segundo-trimestre-con-45-230-procedimientos-1.html, 16 Oct 2026]. With H1 2026 at 87,802, the run rate is about 175k claims a year (my arithmetic, based on [notes: LAB-09]).
- **Pre-dismissal hearing, verified.** STS 1250/2024 of 18 Nov 2024 (plenary, unanimous) applies art. 7 of ILO Convention 158 directly. Its consequences:
  - The hearing is required from the date of the ruling; dismissals before it fall under the art. 7 exception.
  - The ruling does not say what happens if the hearing is omitted. Commentators argue for "improcedente" by analogy.
  - STS 175/2025 of 5 Mar 2025 reiterates the doctrine without settling the consequence.
  - Sources: [new: WebSearch summary of the CEF/UDIMA RTSS commentaries (https://revistas.cef.udima.es/index.php/rtss/article/download/24801/24577/69983), the CECOT circular (https://cecot.org/wp-content/uploads/2024/11/circular_5-sts_despido-disciplinario-audiencia-previa-.pdf) and the Andersen alert, 23 Oct 2026; PDFs not opened].
  - The press still describes the omission as a risk of "improcedente" and says "ya no basta con estudiar únicamente la carta de despido" [new: https://www.lawandtrends.com/noticias/laboral/un-tramite-que-puede-cambiarlo-todo-cuando-un-despido-disciplinario-puede-ser-declarado-improcedente-1.html, updated 22 Oct 2026]. No 2026 refinement was found.
- **STS 526/2026, verified from secondary source.** The ruling of 23 Jun 2026 declared null a dismissal about six days after the worker objected to Saturday work, with no formal claim yet filed; the protection "no protege únicamente a quienes ya han ejercitado acciones legales" [new: https://www.rrhhdigital.com/secciones/legal/799602/el-supremo-refuerza-la-proteccion-frente-al-despido-represalia-incluso-antes-de-una-reclamacion-formal/, 15 Jul 2026].
- **RED 8/2026, verified from secondary source.** Bulletin of 14 Jul: pay in lieu of notice in objective dismissals "tiene naturaleza salarial y debe integrarse obligatoriamente en la base de cotización". It is reported under CRA 0054, renamed «INDEM. DESPIDO/CANTIDADES FALTA PREAVISO», through a supplementary settlement [new: https://www.rrhhdigital.com/secciones/legal/799952/la-tgss-cambia-el-criterio-la-compensacion-por-falta-de-preaviso-en-el-despido-objetivo-ya-cotiza/, 22 Jul 2026]. The bulletin itself was not read.
- **Lapse risk:** none. The drivers are statute, case law and TGSS criteria.
- **SMAC volumes:** still open. The MITES MAC statistics returned HTTP 503 on 23 Oct 2026 (index and the Dec 2025 PDF), as they did in stage 1.

**(b) Competitors and substitutes**
- **Free calculators:** Mutua Fácil, Campmany Abogados and Turnozo publish severance and finiquito calculators [new: WebSearch results, 23 Oct 2026: https://mutuafacil.es/guias-y-recursos/calculadora-indemnizacion-despido-finiquito/, https://www.campmanyabogados.com/despidos/calculadora-despido-finiquito-paro].
- **Generic AI with publisher prompt packs:** Economist & Jurist's "50 prompts profesionales ... abogado laboralista" (Aug 2026) includes "Carta de despido objetivo" (20 days a year, 15 days' notice, job-search leave, and a warning about "errores formales que provocan la improcedencia"), "Cálculo de indemnización por despido" (including the two tranches before and after 12/02/2012), "Papeleta de conciliación (SMAC)" and the art. 41 modification notice [new: https://casosreales.economistjurist.es/cr2/landing/recursos/guia-de-prompts-para-ia-derecho-laboral-y-de-seguridad-social.pdf, created 7 Aug 2026, text extracted]. The document layer of the original idea is now essentially free.
- **Legal publishers and AI assistants inside the target channel:** the graduados sociales council lists Wolters Kluwer (a3asesor) as a sponsor, and Lefebvre GenIA-L, Aranzadi La Ley, Sepín and "Ai Consultas" as collaborators [new: https://www.graduadosocial.org/, seen 23 Oct 2026]. Their dismissal features and prices were not checked.
- **Payroll suites:** a3innuva Nómina runs "simulaciones de costes ... de nóminas y finiquitos" [new: a3innuva sheet, as in IDEA-16].
- **No dedicated SME or adviser dismissal-workflow software was found** in the competitor search [new: WebSearch, 23 Oct 2026], consistent with [notes: LAB-11].

**(c) Buyers and market size.** Advisers: 17,000 colegiado graduados sociales in 43 provincial colegios [new: graduadosocial.org, as above]. Add gestorías' labour departments (count owned by batch 2) and labour lawyers (count not found). Ceiling: 2,000 adviser seats at €39/month is about €0.94M ARR (my arithmetic). The owner side (about 1.23M employers [C-04]) is a one-off, moment-of-need purchase.

**(d) Willingness to pay**
- Worker-side labour-lawyer fees: €300–800 fixed plus cuota litis, €300–500 for the SMAC stage and €800–3,000 for a trial, with Madrid at €500–3,000 [new: https://cuantomecuesta.com/es/abogado-laboral/, updated Apr 2026; comparator, worker-side].
- **Employer-side fees for preparing a dismissal were not found** (open), even after a dedicated search [new: WebSearch, 23 Oct 2026].
- Advisers already pay for publisher subscriptions, which is adjacent spend.

**(e) Distribution.** Colegios de graduados sociales are concentrated (43), but incumbent publishers sponsor them. The Barcelona and Madrid colegios are active on RD 723 and absenteeism [notes: LAB-10, LAB-15, LAB-25]. Search terms exist ("audiencia previa despido disciplinario", "carta de despido disciplinario").

**(f) Build feasibility and legal constraints.** The rules engine is simple. The cost is legal QA and keeping it current: case law moves every quarter, and each rule needs professional sign-off. Ley 2/2025 incapacity cases involve health data (special category). Liability if a tool-guided dismissal is ruled null. **Reserved activities: open [I].** The open sale of formularios and prompt packs suggests that template generation is not reserved, but personalised advice to third parties may raise issues; ask the Consejo General and a bar association. Time to MVP: 6–10 weeks including legal review.

**(g) Defensibility.** Low. Drafting and calculation are commoditised by AI. Publishers with AI assistants already sit in the colegio channel and can add a checklist. The only edges are speed in encoding new rulings and, over years, outcome data on which files held up, which needs scale.

**(h) Kill criteria**
- "Fewer than 1 in 5 interviewed advisers would pay €79/month": **open [I]**. The published evidence (free prompts, publisher AI) makes €79 unlikely, so test €29–49.
- "Owners convert at under 2% at the moment of need": **open [I]**. Dropped from the reshaped version.

**Scores (reshaped, adviser-only)**
- S1 Urgency **3**: a frequent, costly event for advisers, with no deadline.
- S2 Buyers **3**: about 17k graduados sociales plus gestoría labour departments and labour lawyers.
- S3 Willingness to pay **4**: advisers pay publishers; owners pay €300+ per case.
- S4 Reachability **3**: concentrated colegio channel, but incumbents sponsor it.
- S5 Competitive gap **3**: no dedicated workflow, but free calculators, AI prompt packs and publisher tools cover most of it.
- S6 Build speed **3**: legal QA and case-law upkeep.
- S7 Defensibility **2**: AI-exposed; rules engine and reviewer network are thin edges.
- S8 Retention **3**: periodic adviser use.
- **Sellability 3.00; P 4** (a record 175k claims a year; an unfair or null dismissal costs a micro employer thousands to tens of thousands of euros); **Overall 3.40.** Confidence low: no employer-side fee data, SMAC statistics unavailable, and adviser willingness to pay is untested.

**Open [I] checks:** 10 adviser interviews (what they use now, whether Lefebvre GenIA-L, Aranzadi or ChatGPT cover the procedural checks, willingness to pay at €29/49/79); the reserved-activities opinion; MITES SMAC statistics once the site is up.

**What would change the verdict**
- **To KILL:** if advisers report that publisher AI tools already flag the hearing, retaliation and CRA 0054 issues.
- **Towards GO:** if a colegio agrees to co-brand, or if case-law churn continues at the 2026 pace and advisers report missing it.

#### IDEA-18: Machine-readable database and API of collective-agreement (convenio) rules — KILL (medium)

**Validated definition.** As specified: a versioned dataset of convenio rules (pay tables, hours, leave, sick-pay top-ups, absorption), each with effective dates and source links, sold by API to HR, time-tracking and payroll vendors at €0.10–0.20 per covered employee per month, and as a web lookup to gestorías at €49–149/month. Validation found the dataset already exists, maintained and auto-updated, inside the payroll suites that gestorías use (a3convenios with 1,400–1,500 convenios; PayFit with 200+; Nominasol's tables and update service). That removes the gestoría segment and the claimed moat. What remains is a handful of non-payroll HR vendors that can build their own extraction with AI. Killed.

**(a) Problem reality and rule status**
- The churn is real and in force:
  - the retroactive 2026 SMI and the annual absorption test [notes: LAB-03];
  - TS 753/2026 on care leave with no annual cap, and leave counted on the real shift length (TS, 27 May 2026) [notes: LAB-22];
  - two Audiencia Nacional rulings in opposite directions [notes: LAB-21];
  - RD 723/2026 now requires naming the applicable convenio and pay items in each worker's statement (art. 3.2) [new: https://www.boe.es/eli/es/rd/2026/09/09/723, seen 23 Oct 2026].
- National collective bargaining to 30 Jun 2026: average agreed wage increase 3.01%, average agreed working time 1,740.67 hours a year [new: CCOO Canarias, "Estadísticas de Convenios Colectivos, junio 2026", 13 Jul 2026, citing the Ministry's Estadística de Convenios Colectivos, https://canarias.ccoo.es/1cc9dae4a6d437a3cd458f3d194f3e21000069.pdf].
- **Concentration illustration, Canarias:** 112 convenios with economic effects to 30 Jun 2026. 99 are company or group agreements covering 12,049 workers; 13 are sector agreements covering 104,227 [new: same PDF]. A small number of sector convenios covers most workers, which helps an MVP. But the long tail of company agreements is what vendors' customers actually need covered.
- **The anti-absorption reform** announced with the 2026 SMI [notes: LAB-03] **is still unconfirmed** (search 21).
  - It was left out of RD 126/2026 and expected in a separate decree-law, because absorption and compensation sit in art. 26.5 ET, which has the rank of law. In February the Secretary of State said it could not be approved in parallel with the SMI. RDL 16/2025 (the 2025 SMI extension) had already lapsed unconvalidated, and the ITSS issued Criterio Interpretativo 1/2026. No approval was found [new: WebSearch summary of https://periscopiofiscalylegal.pwc.es/se-fija-la-cuantia-del-smi-el-problema-ahora-es-como-aplicarlo/ and https://augustaabogados.com/wp-content/uploads/2026/02/ALERTA_Salario-minimo-interprofesional-para-2026_Augusta-Abogados_2026.pdf, 23 Oct 2026].
  - If it is still unapproved, the Government could still issue it as a decree-law before 29 Nov, for convalidation by the Diputación Permanente. That looks unlikely (inference).
  - For a convenio dataset it would only add one more rule to encode.

**(b) Competitors and existing data**
- **Wolters Kluwer a3convenios / "a3innuva | Convenios":** "más de 1.500 convenios ya mecanizados para descargar en a3innuva | Nómina", plus "a3innuva | BOE Laboral: para estar informado diariamente de los cambios normativos" [new: a3innuva Nómina product sheet, https://assets.contenthub.wolterskluwer.com/api/public/content/d515a50d17e347909eb536cc5b9828dc, text extracted 23 Oct 2026]. The a3convenios page claims "más de 1.400 convenios colectivos" with automatic updates of contribution tables, email notices when subscribed convenios change, and mass application of changes to affected workers [new: search snippet for https://www.wolterskluwer.com/es-es/solutions/a3convenios, 23 Oct 2026; direct fetch blocked with 403]. No open API is described.
- **PayFit Spain:** "más de 200 convenios colectivos disponibles" and about 200 legal and convenio updates a year [new: https://payfit.com/es/, seen 23 Oct 2026].
- **TeamSystem (DELSOL) Nominasol:** includes the office convenio, lets registered users download convenios shared by others, offers "Actualización de tablas salariales y cálculo de atrasos", and sells convenio change alerts as an extra contract [new: https://www.sdelsol.com/programa-nominas-nominasol/, seen 23 Oct 2026].
- **Non-payroll HR suites:** Sesame has "no payroll module" and integrates a3innuva [notes: LAB-21]. Woffu offers leave rules by day or hour [new: Woffu pricing, seen 23 Oct 2026]. Factorial's payroll is "asesoría digital y cálculo de nómina" with certified partners [new: https://factorial.es/pricing, seen 23 Oct 2026]. Whether these vendors hold convenio rule data or rely on manual set-up was not verified (interview check).
- **Public or structured sources:** REGCON offers a public consultation and full-text search of registered texts. No open data, XML or API is described, and the page shown was flagged as a test environment [new: https://expinterweb.mites.gob.es/regcon/index.htm, seen 23 Oct 2026]. A search found no public API; only WageIndicator's COLBAR research coding of 108 Spanish agreements (2019–2021) and BOE PDFs [new: WebSearch, 23 Oct 2026; https://wageindicator.org/es-es/trabajo-en-espana/convenios-colectivos/colbar-europe-base-de-datos-de-convenios-colectivos-espana]. Legal publishers' convenio databases were not priced.

**(c) Buyers and market size**
- Vendors are a handful: about 10–20 HR, time-tracking and payroll vendors selling in Spain (my count from the names in these notes).
- Gestorías: count owned by batch 2. Most run a3innuva, Nominasol or Sage, so they already receive convenio tables.
- National convenio counts were **not obtained**: the Ministry statistics site (mites.gob.es) returned 503 and the trabajo.gob.es domain did not resolve on 23 Oct 2026. The a3 figures (1,400–1,500 mechanised convenios) are the best proxy for the relevant universe.
- Ceiling: if non-payroll vendors cover 1–2M Spanish employees at €0.10, that is €1.2–2.4M a year only if all of them buy (my arithmetic, upper bound). A realistic first-years figure is a few hundred thousand euros.

**(d) Willingness to pay.** Gestorías pay for convenio updates inside their payroll suites (a3convenios as a paid module; Nominasol alerts as a paid extra). That is adjacent spend, but on incumbents. Vendor willingness to pay at €0.10–0.20 is untested [I].

**(e) Distribution.** Direct B2B sales to about 10–20 vendors, with long cycles. The gestoría channel is pre-empted by the payroll suites' own convenio services.

**(f) Build feasibility and liability.** AI-assisted extraction with legal QA. Maintenance is the cost: about 1,500 relevant convenios, annual pay tables, renegotiations and rulings. A 1–3-person team can cover 30–50 convenios in 8–10 weeks, but vendors need coverage of their customers' long tail before they integrate. Errors carry liability, so professional indemnity insurance and contractual caps are needed.

**(g) Defensibility.** A validated, versioned dataset would be a moat, but Wolters Kluwer already owns that moat for the payroll segment. AI lowers everyone's extraction cost, so a new entrant's edge is only update speed.

**(h) Kill criteria**
- "3 of the 5 largest HR vendors already hold this data or won't pay": **met for the payroll vendors**: a3 (1,400–1,500 convenios), PayFit (200+), DELSOL (tables and updates). **Open** for the non-payroll HR suites (Factorial, Sesame, Woffu, Kenjo, Timu).
- "A public source already publishes convenios in structured form": **not met** (REGCON and the bulletins publish text and PDFs only).

**Scores**
- S1 Urgency **3**: recurring churn (SMI, rulings, RD 723 content), no deadline.
- S2 Buyers **2**: about 10–20 vendors plus gestorías that are mostly already served.
- S3 Willingness to pay **4**: gestorías pay incumbents for convenio updates.
- S4 Reachability **3**: few concentrated buyers, slow B2B cycles.
- S5 Competitive gap **2**: a3convenios, PayFit and Nominasol already cover it; there is only no open API.
- S6 Build speed **2**: legal QA and coverage; the MVP is too thin to integrate.
- S7 Defensibility **3**: a dataset moat in principle, already held by the incumbent.
- S8 Retention **4**: API integrations are sticky.
- **Sellability 2.88; P 3** (moderate: gestorías absorb the churn at €15–20 a payslip, and errors lead to claims); **Overall 2.93.** Confidence medium: incumbents' coverage claims are vendor statements; the national convenio count and non-payroll vendors' needs are unverified.

**Open [I] checks:** letters of intent from 2–3 non-payroll HR vendors (would Factorial, Sesame or Woffu pay €0.10 per employee for leave and hours rules?); whether a3 licenses a3convenios data to third parties; the national convenio count once the Ministry site is reachable.

**What would change the verdict:** two or more non-payroll HR vendors committing to pay for a leave-and-hours rules API (a much narrower product), or Wolters Kluwer refusing to integrate with those vendors, which would leave a gap for an independent data layer.

#### IDEA-19: Household-employer autopilot for domestic and care workers — KILL (medium)

**Validated definition.** As tested: a C-type app at €5/month or €49/year per household (contract wizard, monthly payslips, contribution calendar, minimum-wage recalculation, Prevencion10 vault, inspection vault), plus a gestoría white-label at €1–2 per household. Validation shows that the state now provides free tools for the steps that carry legal weight: online registration and direct-debit contributions in Import@ss, the risk assessment in Prevencion10, and the INSST guide and harassment protocol. Enforcement inside homes is weak, and the job left over (a monthly payslip plus a few event-driven documents) is too thin and support-heavy for €5. Killed as specified. See "what would change the verdict" for the narrow condition under which a paid product makes sense.

**(a) Problem reality and rule status**
- **Duties in force:**
  - The employer must always register the worker and pay contributions: "La responsabilidad de tramitar el alta y de ingresar las cuotas corresponderá siempre al empleador" [new: Import@ss "Alta en empleo de hogar", https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Altas+y+afiliacion+de+trabajadores/Alta+en+empleo+de+hogar, search snippet 23 Oct 2026].
  - A monthly individual pay receipt: "La documentación del salario se realizará mediante la entrega al trabajador de un recibo individual" (RD 1620/2011 art. 8.6), with Ministry templates available.
  - Written information on the essential elements of the contract (art. 5.4, which cites RD 1659/1998). RD 723/2026 repealed RD 1659/1998 and says special employment relationships follow their own rules (art. 2.5). My inference is that the art. 5.4 reference now points to RD 723/2026, but that is not verified.
  - Termination: written notice stating the cause, compensation of 12 days' pay per year of service capped at six months, and notice of 20 days (7 if service is under a year). Missing these is presumed to be an unfair dismissal (art. 11) [new: https://www.boe.es/eli/es/rd/2011/11/14/1620/con, consolidated text last updated 08/09/2022, seen 23 Oct 2026].
- **Time records (check 3):** domestic employment has a carve-out, "no serán de aplicación las obligaciones de registro de la jornada" for part-time domestic workers (RD 1620/2011 art. 9.3 bis) [new: as above]. The EU Court of Justice ruled on 19 Dec 2024 that the record duty extends to domestic work, but "No hay noticia de que se haya adoptado ninguna medida" [new: https://www.elsaltodiario.com/trabajo-domestico/prevencion10-herramienta-evaluacion-riesgos-empleo-hogar, opinion piece by Isabel Otxoa, 26 May 2025]. The digital decree is unapproved (see IDEA-16), and whether it covers households is unknown. Status: **no enforceable record duty for most households today.**
- **RD 893/2024 status (check 2):**
  - The household assessment deadline (14 Nov 2025) has passed.
  - **Correction to the notes:** the INSST published the technical guide to RD 893/2024 and the "Protocolo de actuación frente a situaciones de violencia y acoso en el servicio del hogar familiar" on **14 May 2026** [new: https://www.insst.es/noticias-insst/el-insst-publica-la-guia-tecnica-para-la-prl-y-el-protocolo-de-actuacion-frente-a-violencia-y-acoso-en-el-servicio-del-hogar-familiar, 14 May 2026]. El Español's 20 May 2026 claim that they were still pending [notes: PRO-18] is therefore out of date. The INSST held a technical session on both on 23 Sep 2026 [new: WebSearch result, insst.es jornada page, 23 Oct 2026].
  - Worker training runs on a FUNDAE platform. A mutua deck says it was "actualmente adjudicada" to Quirón Prevención for €11,000, and health surveillance is a triennial medical check [new: Asepeyo, "Guía práctica para asesorías", 15 Oct 2025, https://eventos.asepeyo.es/wp-content/uploads/2025/10/Aplicacion-del-reglamento-de-prevencion-para-empleadas-del-hogar_-Guia-practica-para-asesorias-15-10-2025.pdf].
  - **Enforcement:** no inspection or fine data for households was found [new: WebSearch, 23 Oct 2026]. The result of the assessment "no se envía a ningún lado, se guarda en la casa". RD 893/2024 excludes domestic workers from the benefit surcharge for missing prevention measures, and the Inspectorate does not check "aquello que podría supervisar sin necesidad de entrar al domicilio" [new: El Salto, as above]. UGT and CCOO asked inspectors not to be punitive at first [notes: PRO-18].
- **MEI (C-03), settled:** the official page states "A partir del 1 de enero de 2026 será el 0,9 por ciento ... del que el 0,75 por ciento será a cargo del empleador y el 0,15 por ciento ... del empleado" (Empleados de Hogar section; the page still carries an "en proceso de actualización" banner pointing to Orden PJC/297/2026) [new: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537, seen 23 Oct 2026]. **0.90% is correct for 2026**; the 0.80% in the notes came from an un-updated section. The 2027 step to 1.0% follows the statutory schedule (LGSS DT 43ª), which was not re-read here. The 2026 domestic contribution scale has 8 pay bands, with bases from €306 to €1,424.40 [new: same page].
- **SMI:** €9.55 an hour for domestic workers in 2026 [notes: LAB-03].

**(b) Competitors and substitutes**
- **Free and official:**
  - Import@ss: online registration in about nine steps with Cl@ve, certificate or SMS, a direct-debit mandate and a contribution simulator [new: Import@ss snippet, as above].
  - Prevencion10: free assessment and plan.
  - The INSST guide and protocol: free.
  - Ministry payslip templates (RD 1620/2011 art. 8.6).
- **Gestorías:** Billeo charges "20 €/nómina al mes más IVA (desde 15 € por volumen)", covering registration, monthly payslip, contribution review, sick-leave handling, finiquito and Contrat@. Registration, contract and other changes are quoted separately. The page does not mention Prevencion10 [new: https://www.billeo.es/gestoria-empleada-hogar, reviewed 13 Sep 2026].
- **Care and placement agencies:** Cuideo sells a "Servicio Cuideo Gestión Familiar y Laboral" priced only on request [new: https://cuideo.com/precios, seen 23 Oct 2026]. Familia Fácil was reported at €45/month for its contact service, from an undated page of 2024 or earlier [new: WebSearch snippet of https://elreferente.es/mas/familia-facil-amplia-sus-servicios/, 23 Oct 2026; page returned 403; single source].
- **Mutuas:** mutuas train asesorías on the household duties for free (the Asepeyo deck above), so gestorías already have the know-how.
- **No low-cost, all-in-one household app was found** in one competitor search. Weak evidence of a gap, given only one query.

**(c) Buyers and market size (C-22 settled)**
- **"Más de 348.000 mujeres afiliadas"** counts women only [new: INSST press release, 14 May 2025, text extracted from the PDF at https://www.insst.es/documents/d/portal-insst/yolanda-diaz-presenta-la-herramienta-para-evaluar-los-riesgos-laborales-de-las-trabajadoras-del-hogar-nota-de-prensa].
- **"Más de 378.000 personas"** are in the special system, "en su mayoría mujeres", with no source date given [new: https://www.elespanol.com/mujer/estilo-vida/20260520/asesora-financiera-nueva-ley-limpiadoras-hogar-unico-consigue-nadie-contrate/1003744249353_0.amp.html, 20 May 2026].
- **About 540,000** is the EPA count, which includes informal work. The sector also lost 53,000 workers in a year, "la mayor caída de toda la economía" [new: El Español, as above].
- **Use about 378k registered workers.** The number of employing households (domestic-employer contribution accounts) was not found; it is of the same order, likely about 300–380k (inference). An official affiliation table was not fetched.
- **Ceiling:** 5% of about 350k households at €49/year is about €0.86M ARR (my arithmetic).

**(d) Willingness to pay.** Households that outsource pay about €20 a month plus one-off fees, which is 4× the price hypothesis. The share that outsources is unknown. Most can register and pay contributions for free, and the residual job (payslip, notice letters) is covered by templates. The "60 € + IVA por cada alta de trabajador" complaint about Declarando [notes: VOX] shows households and autónomos resent setup fees.

**(e) Distribution.** Search terms exist ("nómina empleada de hogar", "contrato empleada de hogar", "Prevencion10"). Otherwise the channel is diffuse B2C. Agencies and gestorías already sell the service themselves. A gestoría white-label adds little, because payroll suites already handle the domestic special system (inference; not verified per vendor).

**(f) Build feasibility.** Payslip, minimum-wage and calendar logic is low complexity: an MVP in 4–6 weeks. A third party cannot file registrations or contributions for a household without being an authorised representative; the Social Security RED authorisation terms were not verified (open). The product would therefore guide the household through Import@ss or hand off to a partner gestoría. Worker data may include immigration status, which calls for data minimisation.

**(g) Defensibility.** Low: templates and calculators are easy to copy, and the state keeps adding free tools.

**(h) Kill criteria**
- "Free tools dominate": **met for the official steps** (registration, contributions, assessment, protocol, guide). **Not met** for payslips and termination documents, where only templates exist.
- "Fewer than about 1 in 10 surveyed households would pay €5/month": **open [I].**

**Type-C check.** €5/month is not viable. The visible monthly value is one payslip, because the Social Security direct debit happens without the app. Support questions (sick leave, holidays, dismissal) are frequent and complex for laypeople, and churn follows the end of each employment. A self-serve product would need about €8–10/month or €79–99/year (my estimate) and would then compete with €15–20 human gestorías.

**Scores**
- S1 Urgency **2**: duties are mostly event-driven (hiring, the yearly minimum-wage change, termination); the assessment deadline has passed and enforcement in homes is light.
- S2 Buyers **4**: about 300–380k employing households.
- S3 Willingness to pay **3**: some households pay gestorías €15–20 a month; most do it themselves with free tools.
- S4 Reachability **2**: diffuse B2C, only SEO; agencies are competitors rather than channels.
- S5 Competitive gap **3**: free official tools for the steps that carry legal weight, human gestorías for the rest, no cheap app found.
- S6 Build speed **4**: 4–6 weeks.
- S7 Defensibility **2**: SEO and trust only.
- S8 Retention **3**: monthly payslip and records, but churn when the worker leaves.
- **Sellability 2.88; P 2** (minor for compliant households; the big costs, undeclared work and unfair dismissal, fall on households that would not buy); **Overall 2.53.** Confidence medium: rules and market size come from official sources; willingness to pay and competitors rest on one search.

**Open [I] checks:** the survey of about 200 employing households (current spend, willingness to pay €5 or €8); SEEH employer-account count; RED representation rules for households; whether payroll suites handle the domestic system for gestorías.

**What would change the verdict:** a household survey showing at least 10% would pay €8 or more a month; an ITSS campaign on domestic employment; or the digital time-recording decree explicitly covering households, which would create a recurring daily duty and visible monthly value.

#### IDEA-40: Private-pay and reimbursement-claim kit for self-employed health professionals — KILL (medium)

**Validated definition.** As tested: a payer-mix calculator (net € per hour by insurer and for private patients, from practice-software exports), per-session reimbursement packs with the fields each insurer requires, a patient guide, and templates for moving panel patients to private sessions, at €9–19/month. The pain is severe, but the product's engine (patients paying up front and claiming reimbursement) applies to a small minority of policies. The analysis is a one-off, and the private-pay tooling is ordinary practice software. Killed.

**(a) Problem reality and rule status**
- **The squeeze is real** [notes: PRO-01, PRO-02]: €5–20 per allied-health session, about €17–19 per specialist consultation, and 88.76% of surveyed psychologists say the terms are imposed (Infocop, 2023, partly interested parties).
- **Insurer concentration in 2025 (ICEA data to Dec 2025):** SegurCaixa Adeslas had €4,019M of premiums (29.68% share) and Asisa €1,885M (13.70%). Health premiums totalled €13,541M (+11.31%), of which "seguros de salud privados" €10,129M. The two MUFACE insurers billed €2,126M (+25.37%) under a 2025–2027 contract with a 41.2% premium rise and €4,805M of funding [new: https://www.elespanol.com/invertia/observatorios/sanidad/20260313/aseguradoras-dan-cobertura-muface-disparan-facturacion-pierden-asegurados/1003744167365_0.amp.html, 13 Mar 2026].
- **Correction to the notes: competition law no longer blocks collective bargaining.**
  - The CNMC told Unipromel that self-employed private doctors may negotiate "sus condiciones salariales" collectively with insurers and hospital groups, under the European Commission's 29 Sep 2022 guidelines on solo self-employed workers. It identified a bargaining imbalance (and so will not intervene) where the counterparty has €2M or more of turnover or more than ten employees, which covers "la práctica totalidad de las ocasiones" [new: https://okdiario.com/economia/cnmc-informa-unipromel-que-medicos-autonomos-podran-negociar-sus-derechos-aseguradoras-11666103, 3 Oct 2023, updated 18 Sep 2024].
  - The CNMC "en principio no intervendrá" in collective negotiations by self-employed health professionals with insurers or hospital groups whose aim is to improve working conditions. It answered a consultation that included the psychologists' Consejo General [new: https://www.infocop.es/la-cnmc-no-intervendra-en-las-negociaciones-de-los-autonomos-con-las-aseguradoras, 15 Nov 2023].
  - The barrier is therefore insurer bargaining power, not law. The March 2026 approach to the CNMC (physiotherapists' council with ATA and the Andalusian councils) [notes: PRO-02] is a follow-up whose outcome was not found.
  - The Unipromel challenge to the MUFACE contract: no ruling found [new: WebSearch, 23 Oct 2026]. Open.
- **Lapse risk:** none (market structure, not a rule).

**(b) Competitors.** No payer-mix or reimbursement tool was found.
- Clinni (€12.95/month plus taxes) covers booking, reminders and invoicing [new: https://clinni.com/precios/, seen 23 Oct 2026].
- Doctoralia Pro lists an online agenda, reminders, website, reviews and "Noa Notes" AI visit summaries, with no insurer analytics on the page and prices on request [new: https://pro.doctoralia.es/, seen 23 Oct 2026].
- Gesden (dental; it usually manages insurer tariffs) returned 503 and was not checked.
- Payer-mix maths is a spreadsheet task, so the gap is real but shallow.

**(c) Buyers and market size**
- INE DIRCE, 1 Jan 2025: natural-person businesses number 58,119 in CNAE 862 (medical and dental) and 76,906 in CNAE 869 (other health, including physiotherapy, psychology and podiatry) [new: INE table 73019, downloaded 23 Oct 2026].
- Self-employed psychologists: 43,200 in 2021 [notes: PRO-02].
- The REPS lists 49,239 physiotherapists, 9,297 podiatrists, 7,286 dietitian-nutritionists, 6,041 speech therapists and 15,625 dentists. These are registered totals and the register is incomplete [new: REPS report 2024, text extracted].
- The panel-dependent share is unknown.

**(d) Willingness to pay, and the kill test**
- **Reimbursement is a minority.** Reimbursement products took **€1,056M (+7.35%) of €13,541M** of 2025 health premiums, about **7.8% of premiums** (ICEA via El Español, as above; my arithmetic). Per insured person the share is probably lower, since reimbursement policies cost more (inference; no insured count by type was found).
- Some care policies add partial reimbursement with prior payment, limits and a one-year waiting period (an ASISA product sheet; FIATC reimburses up to 80%) [new: WebSearch snippets, 23 Oct 2026]. That widens eligibility a little.
- Professionals already pay €13/month for practice software and opaque Doctoralia fees [notes: PRO-03, PRO-04]. That is adjacent spend, but for other jobs.

**(e) Distribution.** Colegios (COP and the Consejo General de la Psicología; CGCFE), ATA and Unipromel are concentrated channels. Since the CNMC opinions, colegios and associations may pursue collective negotiation themselves, which competes with an "exit the panel" message.

**(f) Build feasibility and legal constraints.** CSV import and templates take 1–2 months. Avoid clinical content (GDPR art. 9). Invoices must follow invoicing rules (VeriFactu dates are owned by batch 1). Deontological limits on advertising sessions as reimbursable: **open [F]**, as the colegio codes were not fetched. Any feature that pools members' fee data would need to sit inside a lawful collective negotiation (the CNMC conditions above), not a vendor product.

**(g) Defensibility.** Low. The insurer-requirements dataset is small and public in policy documents.

**(h) Kill criteria**
- "Reimbursement cover held by only a small minority of insured patients": **met on premiums** (about 7.8%). The insured-person share is unknown and probably lower.
- "Colegio interviews show members will not leave panels": **open [I]**.

**Scores**
- S1 Urgency **2**: a chronic squeeze; leaving a panel is a rare, deliberate decision.
- S2 Buyers **3**: tens of thousands of self-employed professionals; the panel-dependent subset is unknown.
- S3 Willingness to pay **3**: they pay for practice software, not for analysis.
- S4 Reachability **3**: colegios and associations, unproven, now oriented to collective negotiation.
- S5 Competitive gap **4**: no tool, but spreadsheets suffice.
- S6 Build speed **4**: 1–2 months.
- S7 Defensibility **2**: copyable.
- S8 Retention **2**: one-off analysis, with recurring use only for the minority of reimbursement patients.
- **Sellability 2.88; P 4** (income "often does not cover the cost of running a practice", widespread); **Overall 3.33.** Confidence medium: premium shares are official ICEA data via press; the insured-person split and demand are unknown.

**Open [I] checks:** interview 15 panel professionals (insurers' share of revenue, willingness to drop panels); the insured-person share of reimbursement policies (ICEA report, not fetched); colegio deontological rules; the outcome of the March 2026 CNMC approach and the MUFACE challenge.

**What would change the verdict:** insured-person data showing reimbursement cover of 20% or more in target cities, or a colegio-led collective negotiation that wants a neutral fee-benchmark tool. The second would be a different B2B product, for about a dozen associations.

#### IDEA-41: Staff qualification file for private health centres (RD 239/2026) — KILL (medium)

**Validated definition.** As tested: a C-type register of each centre's health professionals (qualification, specialty, colegio number, documents), with safe-practice onboarding acknowledgements, an inspection dossier and reminders, at €5/month or €49/year per centre. The rule is real and the deadline is close, but the job is a one-off filing task with no format, no sanction in the decree and no enforcement evidence. A free state portal (REPS) already holds the staff data that centres must report. Killed as a paid product. At most it is a free lead magnet for a broader clinic product.

**(a) Problem reality and rule status (settled from the BOE)**
- **What RD 239/2026 requires.** It was published in BOE no. 75 on 26 Mar 2026 and has been in force since 1 Jul 2026 (final provision). It adds art. 7 to RD 1277/2003:
  - centres must hold "información actualizada de todo el personal sanitario que ejerza la actividad" and an "expediente personal actualizado con indicación de la titulación oficial";
  - this applies to all staff, "cualquiera que sea su vinculación jurídica" (employees, autónomos, partners);
  - the data must be communicated and kept up to date in the Registro Estatal de Profesionales Sanitarios (RD 640/2014) (art. 7.2);
  - new staff must be informed "sobre las actividades y/o prácticas seguras" (art. 7.3).
- **Deadline:** "En el plazo de seis meses desde la entrada en vigor" (DA 1ª), so about **1 Jan 2027**. Regions have one year to adapt their care offer (DA 2ª).
- **What the text does not set:** no inspection procedure, no file format and no sanctions [new: https://www.boe.es/eli/es/rd/2026/03/25/239, seen 23 Oct 2026].
- **Psychology colegio reading.** The file must hold the official qualification (Especialista en Psicología Clínica, or Máster en Psicología General Sanitaria plus the degree); "no es suficiente acreditar únicamente el Grado"; deadline 1 Jan 2027. Compliance "podrá ser comprobado por las autoridades sanitarias competentes en cualquier momento". The article offers no template and describes no inspection procedure [new: https://www.infocop.es/refuerzo-de-las-garantias-de-atencion-sanitaria-y-nuevas-obligaciones-para-consultas-y-centros-de-psicologia-claves-del-nuevo-real-decreto-239-2026/, 11 Jun 2026].
- **Regional inspection:** no guidance from the Madrid, Catalonia, Andalusia or Valencia inspectorates was found [new: WebSearch, 23 Oct 2026]. The Madrid doctors' colegio (ICOMEM) covered the decree in a bulletin, but the page was too large to fetch.
- **Lapse risk:** none (royal decree in force).
- **Enforcement signal from the REPS:** private centres have had to report their professionals to the REPS since 2017–18, yet on 1 Jan 2025 only 60,295 active professionals had private-sector activity registered, against 404,541 public. The Ministry says implementation "continúa" and some sectors are "infrarrepresentados" [new: REPS annual report 2024, Ministerio de Sanidad, 24 Apr 2025, https://www.sanidad.gob.es/areas/profesionesSanitarias/registroEstatal/docs/Informe_2024_REPS_DGOP.pdf, text extracted]. My inference: a staff-data duty for private centres has gone largely unenforced for seven years, and RD 239's file duty is likely to be treated the same way.

**(b) Competitors and substitutes**
- **REPS portal (free, official):** private centres in REGCESS designate a responsible person and must report "los datos de aquellos profesionales empleados directamente por ellas", and those with a commercial relationship, within 7 days of a change. This is done by web form or by uploading the "situacionesProfesionales" Excel file [new: https://www.sanidad.gob.es/areas/profesionesSanitarias/registroEstatal/entidadesREPS.htm, seen 23 Oct 2026]. A public lookup (https://reps.sanidad.gob.es/) shows name, official qualifications, the centres where each professional works, category and main function. It has been open since Oct 2022 and has no API or bulk access [new: https://www.sanidad.gob.es/areas/profesionesSanitarias/registroEstatal/ciudadanosREPS.htm, seen 23 Oct 2026].
- **Clinic software:** Clinni (€12.95/month plus taxes) has no staff, credential or HR feature [new: https://clinni.com/precios/, seen 23 Oct 2026]. Flowww lists only "Control de horarios y turnos" [new: https://www.flowww.es/, seen 23 Oct 2026]. Koibox (403) and Clinic Cloud (503) could not be checked, and Gesden and Doctoralia were not checked. No vendor advertises an RD 239 module, so the kill criterion "vendors add it free" is untested rather than met.
- **Generic options:** HR suites with per-employee document storage (Factorial Core includes document management [new: factorial.es/pricing, seen 23 Oct 2026]), or a shared folder.

**(c) Buyers and market size (INE DIRCE, 1 Jan 2025)** [new: INE table 73019 via https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73019?nult=1, downloaded 23 Oct 2026]
- CNAE 862 (medical and dental practice): 77,294 enterprises, 34,617 with employees.
- CNAE 869 (other health activities, including physiotherapy, psychology and podiatry): 89,528 enterprises, 17,796 with employees.
- About **52,400 health enterprises with staff**, plus about 114,400 without employees, whose own file is trivial.
- Ceiling: 10% of 52k centres at €49 a year is about €0.26M a year, mostly one-off around the deadline (my arithmetic).

**(d) Willingness to pay.** No evidence of spend. The obligation can be met with copies of diplomas in a folder plus the free REPS portal.

**(e) Distribution.** Colegios are informing members (Infocop for psychologists; ICOMEM in Madrid), which is a real but free channel. Clinic-software vendors could white-label it. "RD 239/2026" search demand exists, but colegios occupy it.

**(f) Build feasibility.** Under 4 weeks; no certification; personal data but not health data. A REPS Excel export ("situacionesProfesionales") is a possible integration hook. There is no colegiación API; only the REPS public lookup by name.

**(g) Defensibility.** None. It is a register with reminders, and the state and the colegios already cover the information side.

**(h) Kill criteria**
- "Regional inspectorates say there is no set format and no check": **open [I]**. No format exists in the decree or in colegio guidance as of 23 Oct 2026, which leans towards met.
- "Main clinic-software vendors add it free before Jan 2027": **open**. Not yet seen in two of the vendors checked.

**Type-C check.** €5/month is not viable: there is no visible monthly value after the one-time setup, and churn will be high after January 2027. A one-off €29–49 "file pack" would be the honest price, and the market for it is small.

**Scores**
- S1 Urgency **4**: a duty in force with a 1 Jan 2027 deadline, but no sanction in the decree and no enforcement evidence.
- S2 Buyers **3**: about 52k health enterprises with staff.
- S3 Willingness to pay **2**: no spend evidence; a folder plus REPS suffices.
- S4 Reachability **3**: colegios and clinic software are channels, but the colegios give the information away free.
- S5 Competitive gap **3**: no dedicated tool, but adequate free or generic substitutes.
- S6 Build speed **5**: under 4 weeks.
- S7 Defensibility **1**: trivially copyable.
- S8 Retention **2**: one-off with occasional updates.
- **Sellability 2.88; P 2** (minor: no defined penalty, no documented harm); **Overall 2.53.** Confidence medium: the rule is from the BOE; the absence of enforcement is inferred from REPS under-reporting; vendor coverage is partial.

**Open [I] checks:** ask the Madrid, Catalan, Andalusian and Valencian inspectorates whether they will check the file and in what format; ask 10 clinic managers whether they know of the duty and would pay for it.

**What would change the verdict:** a regional inspectorate announcing a campaign or a required format, or a large clinic-software vendor offering to resell the module (white-label revenue, no B2C acquisition). Either would make a two-week build for the January deadline worthwhile.

#### IDEA-42: Antibiotic-stewardship and PRESVET compliance file for small vet clinics — KILL (medium-high)

**Validated definition.** As tested: a C-type add-on for companion-animal clinics at €9–15/month with four parts: a prescription rule-checker (categories A–D, antibiogram), an evidence store, a register of antibiotic-reduction measures under RD 767/2025, and a 15-day reconciliation monitor with web-service submission for clinics that still type data in by hand. Three of the four pillars failed validation:
- the reduction-measures duty does not apply to clinics;
- the sanctions were cut to minor by Ley 1/2025;
- 80% of professionals already report automatically through their practice software.

What is left is a category checker for about 5–10k firms. Killed.

**(a) Problem reality and rule status (settled from the BOE)**
- **The reporting duty is in force.** Veterinarians "deberán comunicar los datos mínimos que figuran en el apartado 2 del anexo IV", at least fortnightly ("con una periodicidad, al menos, quincenal"). For companion animals the data go to the region where the prescriber habitually resides (RD 666/2023 art. 39.1), and the duty has applied to companion animals "a partir del 2 de enero de 2025" (DF 5ª) [new: https://www.boe.es/eli/es/rd/2023/07/18/666/con, consolidated text seen 23 Oct 2026].
- **Correction to the notes: the RD 767/2025 reduction-measures duty does not bind clinics.**
  - RD 767/2025 rewrote letter h) of art. 40 of RD 666/2023: "deberá adoptar y documentar las medidas tendentes a la reducción del consumo de antimicrobianos", with reference to RD 992/2022 [new: https://www.boe.es/eli/es/rd/2025/09/02/767, seen 23 Oct 2026].
  - Art. 40 ("Uso prudente de medicamentos") binds "Los titulares o responsables de las explotaciones ganaderas", that is, livestock holdings [new: RD 666/2023 consolidated text, as above].
  - The idea's "RD 767/2025's new duty to document antibiotic-reduction measures" [notes: PRO-05] therefore does not apply to companion-animal clinics.
- **Correction to section 5.2: the sanctions reform was enacted, not lapsed.**
  - Ley 1/2025 (food waste), final provision 5ª(Tres), rewrote art. 83.15 of Ley 8/2003: "La falta de notificación, sin causa justificada, de prescripciones veterinarias a la base de datos Presvet" is now a **minor** infraction [new: https://www.boe.es/eli/es/l/2025/04/01/1, seen 23 Oct 2026; consolidated Ley 8/2003 updated 2 Apr 2025, https://www.boe.es/eli/es/l/2003/04/24/8/con].
  - Minor infractions carry "una multa de 600 a 3.000 euros", or a warning (apercibimiento) when there was no intent and no other sanction in the previous two years (art. 88.1.c) [new: same].
  - The March 2025 claim that omission was "muy grave" with "sanción mínima ... 60.000 euros" and that the change was "en trámite en las Cortes Generales" [new: Colvet "Información Veterinaria", Mar 2025, https://colvet.es/files/reportajes/informacionveterinaria_marzo_2025.pdf, text extracted] described the position before this law.
  - The very serious band (€60,001–1.2M) still exists, but its antibiotic item (art. 85.18) concerns breach of the reduction obligations "para el rango que corresponda", a livestock concept.
  - The C-12 date conflict on when Ley 1/2025 entered into force remains with batches 4 and 6. The fetch reported DF 20ª as giving 2 January 2025.
- **No 2026 change found.** The OCV's demands (a moratorium on PRESVET, repeal of the sanctions) and a Castilla y León PP motion date from early 2025 [new: WebSearch, 23 Oct 2026; BOCCL https://sirdoc.ccyl.es/SIRDOC/PDF/PUBLOFI/BO/CCL/11L/BOCCL1100397/BOCCL-11-012026.pdf]. No fines or inspections of clinics in 2025–26 were found.
- **C-23 settled:** MAPA says "el 80% de los profesionales realiza la comunicación de datos a PRESVET de forma automatizada mediante servicios web", directly from clinic management systems and e-prescription platforms. So the 80% refers to **professionals, not prescriptions** [new: search snippet of the MAPA PRESVET page, 23 Oct 2026; the page itself returned 503]. The 16,460 clinicians and 3.22M prescriptions remain from a search summary and are not re-verified [notes: PRO-05].
- **Lapse risk:** none.

**(b) Competitors.** Practice-management software and e-prescription platforms already submit by web service for 80% of professionals. The rest use the free PRESVET web form. MAPA publishes an access guide that covers registering a "usuario de servicio web" for the vet profile [new: search snippet, guiadeaccesoapresvet_2024, 23 Oct 2026; PDF returned 503]. Qvet's site could not be read (JavaScript-rendered). Whether any vendor checks A–D categories or asks for antibiogram justification is still unverified.

**(c) Buyers and market size.** INE DIRCE, 1 Jan 2025, CNAE 750 (veterinary activities): 10,186 enterprises, of which 5,159 have no employees, 3,015 have 1–2 and 1,357 have 3–5. That is about 5,000 with staff, and the group includes livestock practices [new: INE table 73019, downloaded 23 Oct 2026]. The REPS lists 13,541 veterinarians, but it is incomplete [new: REPS report 2024]. Ceiling: 10% of about 6,000 clinics at €12/month is about €86k ARR (my arithmetic).

**(d) Willingness to pay.** None separate from the practice-software subscription was found. Clinics resent PRESVET as bureaucracy; the OCV calls it "rígida e ineficaz" [new: Colvet, as above]. That signals anger, not a budget.

**(e) Distribution.** The OCV and its 52 colegios are concentrated, but they are campaigning against the system rather than for tools. Practice-software vendors are the gatekeepers.

**(f) Build feasibility.** Web-service submission needs the vet's own web-service user. MAPA's site and documents were unstable (503) during validation. Category logic comes from RD 666/2023 art. 6 and Annex I, which follows the EMA categorisation; category B use should rest, where possible, on "la identificación etiológica del agente patógeno y su sensibilidad" [new: RD 666/2023 consolidated, as above]. About 2–3 months to MVP, integration-heavy.

**(g) Defensibility.** Low. Any practice-software vendor can add a category check.

**(h) Kill criteria**
- "Leading practice software already checks categories and keeps evidence": **open** (not verifiable from vendor pages). Moot given the findings above.
- "Colegios report no inspections or fines since 2025": **leans met.** No fines found, and the fine itself is now minor or a warning.

**Scores**
- S1 Urgency **2**: the duty is in force, but automated for most, and the fine is now €600–3,000 or a warning.
- S2 Buyers **2**: about 5–10k veterinary enterprises.
- S3 Willingness to pay **2**: no separate spend.
- S4 Reachability **3**: concentrated colegios, but hostile to the system; vendors gatekeep.
- S5 Competitive gap **2**: practice-software web services plus a free web form.
- S6 Build speed **3**: integration-heavy, unstable official endpoints.
- S7 Defensibility **2**: vendors can copy it.
- S8 Retention **3**: fortnightly use.
- **Sellability 2.38; P 2** (minor fines; an admin burden mostly absorbed by software); **Overall 2.23.** Confidence medium-high: the rules are from the BOE; vendor capabilities are unverified.

**Open [I] checks:** whether Qvet and the other leading vendors check categories and antibiograms; ask 2–3 colegios about inspections since 2025.

**What would change the verdict:** MAPA announcing audits of prescription categories with heavier sanctions, or evidence that the 20% who report manually are concentrated in reachable groups (exotic-animal or rural practices) and would pay.

#### IDEA-43: Exam-readiness tracker and slot planner for driving schools — KILL (medium)

**Validated definition.** As tested: an instructor app that scores each practical lesson against exam criteria, gives each student a readiness score and pass estimate, and adds a "whom to present" dashboard, lesson and car scheduling, student updates and a ready-student export, at €29–59/month per school plus €5 per instructor.

Validation first pointed to a RESHAPE: an instructor-only readiness app plus CAPA pass-rate analytics, sold through a management-software partner. The final competitor search then found free instructor apps that already do the core. Control-L evaluates students "con los criterios de un examen real" and shows "errores más comunes" and progression. The driving-school confederation's own publisher ships a free instructor app with per-student progress statistics, linked to the eGestion management platform. The market is small and shrinking, and schools' incentives are contested. Killed. The CAPA pass-rate analytics on their own would be a feature for eGestion or AEOL, not a product.

**(a) Problem reality and rule status**
- **C-20 settled from the DGT's own figures.** In its Plan de Refuerzo Operativo (PRO), the DGT offered every examiner needed and asked schools for lists of all trained students, including earlier fails. Navarra presented 275 of "más de 6.000", Lleida 312 of 5,000, Almería 630 of 8,000 and Palma 407 of 8,000. The DGT says the "mal llamada 'lista de espera'" is everyone who passed theory and has two years to sit the practical. Tenerife (575 of 11,000) and Barcelona (1,450 of 63,000, from 13 Jun 2026) were next. The DGT also added 130 examiner posts to reach 21 per million inhabitants [new: DGT press note, 16 Jun 2026, https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/2026/20260616-nota-de-prensa.pdf, text extracted]. **The sector's queue figures overstate immediate demand.**
- **Readiness selection is imperfect even when schools choose.** Pass rates among the students schools selected for PRO were 46.15% in Lleida (below its 51.71% Jan–Apr average), 164 of 275 (60%) in Navarra, 70% in Almería, and under half in Baleares (210 of 407 failed) [new: same]. This supports the case for a readiness tool.
- **Both sides' positions.** DGT head Pere Navarro: "solo un 8 % de la bolsa de alumnos está en condiciones de examinarse". CNAE: "inaceptable", the bottleneck is examiners, PRO is "un parche". More than 1 million practical tests a year; Catalonia, Madrid, Murcia and Cádiz are the most congested [new: https://www.motor.es/noticias/pere-navarro-dgt-enfurece-autoescuelas-listas-espera-2026114254.html, 19 May 2026].
- **CAPA does reward pass rates (kill check).** CAPA ("Capacidad para las Pruebas de Aptitud"), in place since 2017, splits each Jefatura's capacity using each school's theory passes over the last two years. It compares the school's practical pass share with its exam centre's average, "más cupo a las que tienen mejor porcentaje de aprobados", and applies a correction factor to schools with high failure rates. The first-attempt pass rate rose from 42% (2017) to 49% three years later [new: https://www.autofacil.es/conductor/carnet-conducir-sistema-capa-dgt/193432.html, 29 Oct 2020; press description, not the DGT instruction; dated]. **Kill criterion not met**, subject to the 2026 instruction being unchanged.
- **Regulatory-change risk.** In its 9 Jan 2025 study (E/CNMC/001/22), the CNMC recommends that "podría asignarse el examen al alumno en lugar de a la autoescuela", and that schools' pass rates be published and students be able to deal directly with the DGT. It also notes schools struggle "para adaptarse a la herramienta informática de la DGT" [new: https://www.cnmc.es/prensa/estudio-autoescuelas-20250109, 9 Jan 2025]. Assigning exams to students would weaken the CAPA lever, while publishing pass rates would strengthen demand for readiness tools. Either change needs DGT regulation; neither was found adopted.
- **Lapse risk:** none (administrative practice).

**(b) Competitors (decisive)**
- **Control-L** (developer Jorge Sarasola; free on iOS). Lessons are signed on the phone by instructor and student and "sincronizan con el programa de la administración". The instructor can evaluate the student "durante o después de la clase con los criterios de un examen real", and students see "sus errores más comunes y cuál es su progresión". It also has a calendar and teaching-hours log. Too few ratings to show; v1.6.8 [new: https://apps.apple.com/us/app/id1403711075, seen 23 Oct 2026].
- **Autoescuelas Clases Prácticas** (publisher Editorial CNAE; seller Autoescuelas Confederadas SRL; free). Student files for up to 50 students, digital signature of each class, "gráficas y estadísticas que reflejan su nivel de aprendizaje", and sync with "la plataforma de gestión de autoescuelas eGestion"; v3.0.0, 20 Apr 2025 [new: https://apps.apple.com/us/app/id1396551189, seen 23 Oct 2026]. **The main sector channel (CNAE) has its own tool.**
- **Others:**
  - Colibri and Klaxo (student progress, billing, booking) [new: https://www.appvizer.es/servicios/autoescuela, WebSearch result, 23 Oct 2026];
  - an Odoo "driving_school" module with lesson reports covering zones, manoeuvres and performance evaluation [new: https://apps.odoo.com/apps/modules/19.0/driving_school_odoo, WebSearch result];
  - PracticaVial's evaluation software [new: https://elreferente.es/?p=13739, WebSearch result];
  - AEOL Gestión Plus (student management, scheduling, billing, client portal; "from €12.50", with the period not stated; BookingTimes listed as an alternative) [new: https://www.getapp.es/software/2066260/aeol-gestion-plus, WebSearch result, 23 Oct 2026].
- **Gap:** none of these explicitly claims a calibrated readiness score or pass estimate. That residual is a feature, and it is copyable by the incumbents above.

**(c) Buyers and market size.** 7,898 driving schools, against 9,247 in 2015 (CNAE president Enrique Lorca); about 900 examiners, 350 short; 12 tests per examiner a day [new: https://avilared.com/art/80101/el-sector-de-las-autoescuelas-de-espana-pone-de-relieve-la-falta-de-examinadores, 8 Nov 2024]. Ceiling: 10% of schools with 3 instructors at €6 is about €170k ARR, or about €0.4M at €45 per school (my arithmetic). Small and shrinking.

**(d) Willingness to pay.** Schools pay for management software (AEOL from €12.50). There is no evidence of willingness to pay for readiness scoring. **Counter-incentive (single source, an interested party):** a Catalan driving-school workers' association told the CNMC that "la mayoría de autoescuelas basan el negocio en las renovaciones de examen", earning more from re-sits than from training [new: ATAAC submission to the CNMC consultation, https://www.cnmc.es/sites/default/files/Asociaciones_ATAAC.pdf, text extracted, undated]. This fits the longlist's top risk.

**(e) Distribution.** The CNAE and provincial associations are concentrated, but they reject the DGT's readiness framing ("inaceptable"), and the CNAE's publishing arm already distributes its own free instructor app linked to eGestion. A product sold as "your students aren't ready" is politically awkward. "Win more CAPA slots" fits better, but the channel is occupied.

**(f) Build feasibility.** A rubric app, dashboard and pass-rate analytics in under 2 months. There is no DGT API. Whether the DGT's practical-exam assessment criteria are public for a rubric was **not checked** ([S*] skipped). Students' personal data under GDPR.

**(g) Defensibility.** None. Free apps (including the confederation's) already score lessons. A moat would need lesson scores linked to exam outcomes across many schools, and the incumbents with the installed base are best placed to build that.

**(h) Kill criteria**
- "CAPA does not reward pass rates": **not met** (it rewards them, per the 2020 press description).
- "Schools say readiness is not their problem": **open [I]**. The CNAE's public stance leans that way, but it is a lobbying position.
- The longlist's risk 3, "driving-school software (not researched) may already do this": **confirmed.**

**Scores (original idea)**
- S1 Urgency **3**: a persistent bottleneck with no deadline.
- S2 Buyers **2**: about 7,900 schools.
- S3 Willingness to pay **2**: the closest tools are free.
- S4 Reachability **2**: the confederation channel distributes its own app.
- S5 Competitive gap **2**: several tools, including free ones, score lessons against exam criteria.
- S6 Build speed **5**: under 4 weeks.
- S7 Defensibility **1**: copyable, with incumbents installed.
- S8 Retention **3**: daily instructor use.
- **Sellability 2.50; P 3** (cars and instructors tied up, students lost; schools' own loss not quantified); **Overall 2.70.** Confidence medium: the official DGT figures are strong; CAPA rests on a 2020 press piece; the competitor evidence is from app-store listings.

**Open [I] checks:** whether eGestion or Control-L users get a readiness or pass estimate (a feature gap at most); the current DGT CAPA instruction; whether the DGT's exam fault criteria are public.

**What would change the verdict:** the DGT publishing school pass rates (the CNMC recommendation) while incumbents fail to add pass-rate benchmarking. Even then, the better route is a feature partnership with eGestion or AEOL, not a new product.

#### IDEA-44: Route planning, visit verification and hours reporting for home-help (SAD) providers — KILL (medium-high)

**Validated definition.** As tested: B2B software for SAD providers (route planning within visit windows, mobile check-in and check-out, monthly hours reports in each council's format, a rota builder that checks the full-time share) at €3–6 per carer or €99–299 per company per month. Validation found specialised SAD platforms already doing every listed function, often bought by the councils themselves and imposed on providers. The provider universe is about 3,000 firms. Killed.

**(a) Problem reality and rule status**
- **The margin squeeze is real.** Vigo's SAD contract costs €49.5M over three years, with a possible two-year extension. The hourly price rises from €16.70 to €22 "por el incremento de salarios", adding almost €5M, and the contract was due to start on 1 Dec 2025 [new: https://vigoe.es/vigo/local/vigo-pone-en-marcha-uno-de-sus-megacontratos-y-caballero-exige-que-lo-pague-la-xunta, 17 Mar 2025]. The article sets no control-system requirement.
- The Catalan tender clause folding travel, coordination, supervision and training into the hourly price rests on a TED summary [notes: PRO-17]. The TED PDF (https://ted.europa.eu/es/notice/92082-2025/pdf) came back empty on 23 Oct 2026, so the clause is **not re-verified.**
- **Accreditation targets:** the 2029 targets (at least 50% full-time contracts in SAD) and their regional transposition remain unverified [notes: PRO-16, PRO-17].
- **Lapse risk:** none.

**(b) Competitors (decisive)**
- **Gesad (Grupo Trevenque).**
  - Scale: "presente en 2.793 instituciones públicas", serving 195,780 users, with "78.456 auxiliares y 1.574 coordinadores del SAD" working with it daily.
  - Gesad Mobile shows each carer the day's plan, address, tasks, contacts and "la ruta más corta para llegar al domicilio", records presence, and logs incidents (for example, the user is not at home) with alerts to coordinators and families.
  - In Sep 2020 it won the Diputación de Sevilla contract for "un sistema de información único" for all entities providing SAD in the province, and "89 ayuntamientos y una Entidad Local Autónoma" use it, "de Chiclana a Barcelona".
  - Source: [new: Trevenque/Gesad article, Nov 2021, https://www.trevenque.es/wp-content/uploads/2021/11/gesad-balance-noviembre.pdf, text extracted; vendor material]. A search snippet also cites QR or NFC presence marking [new: WebSearch, 23 Oct 2026].
- **CIBERSAD (CIGESOC).**
  - Features: "Cálculo automático de kilometraje y tiempos de desplazamiento entre domicilios, a través de la geolocalización"; automatic control of carer assignment and times; "Exportación del fichero de registro de jornada"; analysis of planned against delivered time; billing "por horas asignadas o por horas efectivamente prestadas"; a family web portal showing the carer's clock-ins.
  - For "Ayuntamientos con gestión externalizada" it links council social workers with provider companies in real time.
  - Certified ENS, ISO/IEC 27001 and ISO 25000; "TODAS las funcionalidades ... incluidas en la cuota de uso".
  - Source: [new: CIBERSAD sheet on the Comunidad de Madrid transparency portal, https://www.comunidad.madrid/transparencia/sites/default/files/person/documents/activity/cibersad_web_0.pdf, text extracted, undated].
- **Gap:** none on features. Many providers must use the council's or diputación's chosen system, so a provider-side tool duplicates it.

**(c) Buyers and market size.** INE DIRCE, 1 Jan 2025, CNAE 881 (social services without accommodation for the elderly and disabled, which includes SAD and day centres): 3,145 enterprises; 877 have no employees; about 1,226 have 10 or more. That figure includes about 93 in the 200–999 bands, inferred by difference because the API output omitted those bands [new: INE table 73019, downloaded 23 Oct 2026]. IMSERSO counts of SAD hours or providers were not fetched; not needed given the competitor finding. Ceiling: 300 providers at €199/month is about €0.7M ARR (my arithmetic), before councils' systems displace it.

**(d) Willingness to pay.** Councils and diputaciones already pay specialised vendors (Gesad, CIBERSAD); their prices were not published.

**(e) Distribution.** Tender-driven and council-led. Providers follow the council's system, so a provider-first SaaS has no clean entry.

**(f) Build feasibility and legal constraints.** Route optimisation, NFC or QR check-in and reporting take 2–4 months. Public-sector-facing systems advertise ENS and ISO 27001, which raises the bar for new entrants. Location tracking draws AEPD and Consejo de Estado data-protection concerns [notes: LAB-01]; incumbents use presence marking at the home rather than continuous tracking (vendor material). Data on dependent people is health-adjacent (GDPR art. 9).

**(g) Defensibility.** Incumbents hold council contracts, ENS certification and integrations with regional dependency systems (CIBERSAD generates "la información del SAD para el Plan Concertado"). A newcomer has no moat.

**(h) Kill criteria**
- "Tenders mandate systems supplied by the council": **met in part.** The Diputación de Sevilla runs a single province-wide system for all SAD providers, 89 councils plus an ELA use Gesad, and CIBERSAD serves councils with externalised SAD.
- "Specialised SAD software already does this cheaply": **met on features** (route, presence, hours, billing, time-record export); price unknown.

**Scores**
- S1 Urgency **3**: a recurring margin squeeze with no deadline.
- S2 Buyers **1**: about 3,100 CNAE 881 firms, including day centres.
- S3 Willingness to pay **3**: councils and providers already pay specialised vendors.
- S4 Reachability **2**: council-led procurement.
- S5 Competitive gap **2**: Gesad and CIBERSAD cover the scope.
- S6 Build speed **3**: integrations plus ENS expectations.
- S7 Defensibility **2**: none against incumbents.
- S8 Retention **4**: daily operational use.
- **Sellability 2.50; P 3** (moderate: unpaid travel time inside capped prices); **Overall 2.70.** Confidence medium-high: the competitor evidence is vendor material (Gesad's figures are from 2021) but specific and consistent.

**Open [I] checks:** five small-operator interviews (which council system they must use; whether gaps remain in rota and full-time-share compliance); current Gesad and CIBERSAD prices.

**What would change the verdict:** evidence that small private-pay SAD operators (outside council contracts, for example families paying directly) lack tools. That is a different, smaller product.

---

## 3. Cross-cutting findings (rule status and market facts for other batches)

**Election and rule mechanics**
1. **Caretaker limits start after the vote, not at dissolution.** "El Gobierno cesa tras la celebración de elecciones generales"; it then "limitará su gestión al despacho ordinario de los asuntos públicos" except for "casos de urgencia debidamente acreditados" or expressly justified "razones de interés general". It may not approve the budget bill or send bills to the Cortes (Ley 50/1997, art. 21.1, 21.3 and 21.5) [new: https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336, seen 23 Oct 2026].
   - Until 29 Nov 2026 the Government can still approve royal decrees and decree-laws; decree-laws go to the Diputación Permanente.
   - Afterwards, any non-urgent regulation (for example the digital time-recording decree, the pay-transparency decree or the VeriFactu instrument in batch 1) would be legally exposed.
   - Owners of those checks should read the decision window as the Councils of Ministers on 27 Oct and 3, 10, 17 and 24 Nov 2026.
2. **Digital time-recording decree (owned by batch 3): not approved as of 23 Oct 2026.** No official date is set. The transition (6 or 12 months) is unsettled. See IDEA-16 (a). Lapse logic: it needs no convalidation, but it stalls if not approved by 24 Nov.
3. **SMI anti-absorption reform (LAB-03): status unknown.**
   - It needs law-rank change, because art. 26.5 ET has the rank of law, so a royal decree cannot do it [new: WebSearch summary of Augusta Abogados and PwC, 23 Oct 2026].
   - It was not approved alongside RD 126/2026. RDL 16/2025 (the 2025 SMI extension) lapsed unconvalidated, and the ITSS issued Criterio Interpretativo 1/2026 [new: same].
   - If it was not approved before 6 Oct, it can now come only as a decree-law, convalidated by the Diputación Permanente. Treat it as unlikely before the new legislature (inference).

**Labour law facts**
4. **LISOS fine bands, from the BOE** [new: https://www.boe.es/buscar/act.php?id=BOE-A-2000-15060, art. 40.1]: minor €70–750; serious €751–7,500; very serious €7,501–225,018.
   - Failing to inform workers in writing of the essential elements of the contract (RD 723/2026 statements) is **minor** (art. 6.4).
   - Time-record and working-time breaches are **serious** (art. 7.5).
   - Relevant to IDEA-06's rule feed and to any idea claiming large RD 723 fines.
5. **RD 723/2026, from the BOE:**
   - in force 5 Oct 2026; covers relationships of more than four weeks;
   - information is deemed given if the written contract already contains it (art. 3.1);
   - the SEPE model was due within 20 days, and its absence does not suspend the duty;
   - no sanctions in the decree;
   - existing staff who ask must be answered within 30 working days.
6. **C-04 employer count, settled.** INE DIRCE, 1 Jan 2025: 1,510,381 firms with employees (901,955 with 1–2; 314,941 with 3–5; 132,013 with 6–9; 85,467 with 10–19; 76,005 with 20+). INE CODEM, 2026Q2: 1,231,358 employer units. The Consejo de Estado's 1.35M has no stated base. Use CODEM for paying entities and DIRCE for the size split.
7. **C-03 MEI, settled:** 0.90% in 2026 (0.75% employer, 0.15% worker), per the official Social Security page (Empleados de Hogar section). Relevant to IDEA-09 and the IDEA-06 rule feed.
8. **C-18 working-time fines: unresolved.** The 2025 figure of €15.7M is unsourced, and the ITSS 2025 report summary has no breakdown.

**Competitors that affect other batches**
9. **Wolters Kluwer a3 is a direct competitor to IDEA-06 (gestoría cockpit, batch 2).**
   - a3innuva already offers gestorías "a3innuva | BOE Laboral: para estar informado diariamente de los cambios normativos".
   - It has "a3innuva | Convenios" with more than 1,500 mechanised convenios (a3convenios: "más de 1.400") with change alerts, and a client–employee collaborative portal with e-signature [new: a3innuva Nómina product sheet, text extracted].
   - TeamSystem-DELSOL gives advisers free seats in Gestión de Empleados at €2 per employee.
   - Batch 2 should test IDEA-06's labour module against both.
10. **Time-tracking price floor in Spain (Oct 2026):** Jibble free (unlimited users); Woffu Lite from €1.5 per user (up to 10 staff); Holded HR €1.50 per employee; DELSOL €2; Timu €9 for 3 seats. Relevant to any batch-4 idea with clock-in features, such as the hospitality and APPCC logbook (IDEA-37).

**Corrections to stage-1 notes and section 5**
11. **PRESVET sanctions (section 5.2): the reform passed.** Ley 1/2025, final provision 5ª(Tres), rewrote art. 83.15 of Ley 8/2003: a missing Presvet notification is a minor infraction, €600–3,000 or a warning. The fetch read final provision 20ª of Ley 1/2025 as setting entry into force on **2 January 2025** for a law published on 2 Apr 2025. That is the C-12 conflict, for batches 4 and 6 to settle.
12. **RD 767/2025's antimicrobial-reduction documentation duty binds livestock holdings** (art. 40 RD 666/2023), not clinics. Very serious infractions (€60,001–1.2M) cover breaches of reduction obligations "para el rango que corresponda" (Ley 8/2003 art. 85.18). This could matter for batch 6's farm-compliance idea (IDEA-51: fertilisation and nutrient records, which could add an antimicrobial-reduction module for farms).
13. **Competition law and health professionals (PRO-01, PRO-02).** The CNMC said in Oct and Nov 2023 that it would not intervene in collective negotiation between solo self-employed health professionals and insurers or hospital groups that have €2M or more of turnover or more than 10 staff (European Commission guidelines of 29 Sep 2022). Any idea that assumes a legal bar on collective negotiation is out of date.
14. **Domestic employment (PRO-18).** The INSST guide to RD 893/2024 and the household harassment protocol were published on 14 May 2026. The notes' "still pending in May 2026" is wrong. Domestic part-time employment is exempt from time records under RD 1620/2011 art. 9.3 bis, although the EU Court of Justice (19 Dec 2024) says the duty extends to domestic work and no national measure has followed. Registration and contributions are online and free through Import@ss.

**Market counts and data sources**
15. **INE DIRCE counts by CNAE group, 1 Jan 2025** [new: INE table 73019, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73019?nult=1]:
    - 691 legal activities: 83,943 (67,557 natural persons);
    - **692 accounting, bookkeeping, audit and tax advice: 62,234** (28,820 natural persons; 30,641 SLs), an upper bound for batch 2's gestoría and asesoría count;
    - 750 veterinary: 10,186;
    - 855 other education (includes driving schools): 91,715;
    - 862 medical and dental: 77,294;
    - 869 other health: 89,528;
    - 881 non-residential social services for the elderly and disabled: 3,145.
16. **Driving schools:** 7,898, against 9,247 in 2015 (CNAE, 8 Nov 2024). The CNMC's 9 Jan 2025 study recommends assigning exams to students rather than schools and publishing pass rates; neither was found adopted. The DGT's PRO data show schools presented under 10% of claimed "waiting" students.
17. **REPS:** private health centres must report each professional within 7 days of a change. Yet on 1 Jan 2025 only 60,295 active professionals had private activity registered, against 404,541 public. Private-sector staff-data duties have long been weakly enforced, which matters for any health-compliance idea.
18. **Unreachable official statistics.** The Ministry of Labour statistics site (mites.gob.es: CCT convenio statistics, MAC conciliation statistics) returned 503 throughout, and trabajo.gob.es did not resolve. MAPA's PRESVET pages returned 503 and REGCESS 403. Other batches needing these sources should plan around them.

---

## 4. Search log

**WebSearch calls: 22 of 24** (all standard mode except #1, extended).

| # | Query | For | Main result |
|---|---|---|---|
| 1 | registro horario digital real decreto Consejo de Ministros aprobación antes elecciones 29N octubre 2026 | IDEA-16, cross-cutting | Not approved; vendor sources only |
| 2 | a3innuva control horario portal del empleado asesorías clientes registro jornada precio Wolters Kluwer Sage Despachos | IDEA-16 | Irrelevant results (wasted) |
| 3 | gestión nómina empleada de hogar online precio al mes alta Seguridad Social servicio familias | IDEA-19 | Billeo €20 per payslip; Familia Fácil |
| 4 | empleo del hogar RD 893/2024 guía técnica INSST protocolo acoso formación Inspección de Trabajo sanciones hogares 2026 | IDEA-19 | INSST guide and protocol, 14 May 2026 |
| 5 | a3innuva control horario registro de jornada empleados asesoría precio (domains: wolterskluwer.com, a3software.com) | IDEA-16 | a3HRgo, a3gestión del tiempo, product sheet |
| 6 | empleados de hogar alta Import@ss empleador hogar familiar trámite online representante autorizado RED gestoría cotización domiciliación (domains: seg-social.es, seg-social.gob.es, inclusion.gob.es) | IDEA-19 | Import@ss online registration; RED rules not found |
| 7 | cuánto cuesta abogado laboralista para la empresa redactar carta de despido y asistir conciliación SMAC precio honorarios 2026 | IDEA-17 | Worker-side fees only |
| 8 | generador carta de despido online empresa software despidos asesorías calculadora indemnización finiquito automática | IDEA-17 | Free calculators; Economist & Jurist prompt guide |
| 9 | STS 1250/2024 18 noviembre 2024 audiencia previa despido disciplinario Convenio 158 OIT aplicación despidos posteriores Supremo 2025 2026 doctrina | IDEA-17 | Ruling verified; STS 175/2025 |
| 10 | API convenios colectivos España tablas salariales base de datos estructurada actualizada integración software RRHH nóminas | IDEA-18 | a3convenios; no public API |
| 11 | número de convenios colectivos con efectos económicos 2025 2026 trabajadores afectados convenios de empresa sectoriales provinciales estadística Ministerio de Trabajo | IDEA-18 | Regional (Canarias) figures only |
| 12 | "Real Decreto 239/2026" expediente personal profesionales sanitarios centros privados plazo inspección comunidad autónoma colegio circular REPS | IDEA-41 | Infocop and ICOMEM coverage; no inspection format |
| 13 | PRESVET sanciones Ley de Sanidad Animal modificación aprobada veterinarios multas infracción notificación antibióticos 2025 2026 reforma régimen sancionador | IDEA-42 | 2025 motions only; enactment found later on the BOE |
| 14 | programa de gestión clínica veterinaria integración PRESVET comunicación automática recetas antibióticos Qvet software veterinario precio | IDEA-42 | MAPA: 80% of professionals report by web service |
| 15 | DGT reparto plazas examen práctico autoescuelas fórmula CAPA porcentaje de aprobados criterios asignación puestos examen instrucción | IDEA-43 | CAPA rewards pass rates (2020 press) |
| 16 | software gestión autoescuela precio mensual programa autoescuelas España clases prácticas evaluación alumnos app profesor | IDEA-43 | AEOL Gestión Plus; CNMC consultation submissions |
| 17 | número de autoescuelas en España 2025 2026 escuelas particulares de conductores DGT censo secciones profesores | IDEA-43 | 7,898 schools; CNMC 2025 study |
| 18 | software servicio de ayuda a domicilio SAD gestión auxiliares app fichaje en domicilio NFC pliego ayuntamiento sistema control de presencia empresas | IDEA-44 | Gesad, CIBERSAD |
| 19 | seguro de salud modalidad reembolso de gastos porcentaje asegurados primas ICEA 2025 asistencia sanitaria cuadro médico España | IDEA-40 | Reimbursement €1,056M of €13,541M |
| 20 | CNMC informe profesionales sanitarios autónomos negociación colectiva aseguradoras baremos fisioterapeutas psicólogos 2026 Unipromel Audiencia Nacional MUFACE sentencia | IDEA-40 | CNMC 2023 non-intervention |
| 21 | real decreto-ley prohibir absorción compensación SMI complementos salariales 2026 aprobado Consejo de Ministros convalidación Congreso | IDEA-18, cross-cutting | Status unknown; needs a decree-law |
| 22 | app autoescuela profesor evaluación clases prácticas alumno preparado examen práctico DGT software seguimiento progreso alumnos | IDEA-43 | Control-L; CNAE app; Odoo module |

**Searches per idea:** IDEA-16 3 (one wasted), IDEA-17 3, IDEA-18 2 plus one cross-cutting, IDEA-19 3, IDEA-40 2, IDEA-41 1, IDEA-42 2, IDEA-43 4, IDEA-44 1.

**Checks left open for lack of budget or reachable sources:**
- whether the SEPE published the RD 723 model;
- the share of micro firms still on paper records;
- employer-side dismissal fees;
- SMAC statistics;
- the national convenio count;
- RED authorisation rules for households;
- Koibox, Gesden and Doctoralia staff modules;
- Qvet's category checks;
- the DGT exam fault criteria;
- IMSERSO SAD statistics;
- reimbursement-policy insured counts;
- colegio deontological codes.

**Main pages fetched directly (unlimited)**
- **BOE:**
  - RD 723/2026 (https://www.boe.es/eli/es/rd/2026/09/09/723);
  - RD 239/2026 (https://www.boe.es/eli/es/rd/2026/03/25/239);
  - RD 767/2025 (https://www.boe.es/eli/es/rd/2025/09/02/767);
  - RD 666/2023 consolidated (https://www.boe.es/eli/es/rd/2023/07/18/666/con);
  - Ley 8/2003 consolidated (https://www.boe.es/eli/es/l/2003/04/24/8/con);
  - Ley 1/2025 (https://www.boe.es/eli/es/l/2025/04/01/1);
  - LISOS consolidated (BOE-A-2000-15060);
  - Ley 50/1997 consolidated (BOE-A-1997-25336);
  - RD 1620/2011 consolidated (https://www.boe.es/eli/es/rd/2011/11/14/1620/con).
- **Official statistics and portals:**
  - INE DIRCE 2025 press release; INE API table 73019 (DIRCE by CNAE group and size);
  - Seguridad Social bases and rates for 2026;
  - Ministerio de Sanidad REPS pages and the REPS 2024 annual report;
  - REGCON public portal;
  - DGT press note of 16 Jun 2026;
  - CNMC driving-school study press release (9 Jan 2025);
  - INSST press release (14 May 2025) and news item (14 May 2026).
- **Press and professional sources:** El Español (Consejo de Estado, 23 Mar 2026; domestic workers, 20 May 2026; ICEA health premiums, 13 Mar 2026); Law&Trends (dismissal claims; pre-dismissal hearing; RD 723 and graduados sociales); RRHH Digital (RD 723; STS 526/2026; RED 8/2026; Timu launch); El Derecho (ITSS 2025 report); Finantres; Motor.es; Autofácil (CAPA); Ávila Red; Vigo e; Infocop (RD 239/2026; CNMC 2023); OKDiario (CNMC and Unipromel); graduadosocial.org.
- **Vendor and app pages:** Woffu, Sesame, Factorial, Timu, DELSOL Gestión de Empleados and Nominasol, the a3innuva product sheet, PayFit, Jibble, Billeo, Cuideo, Clinni, Flowww, Doctoralia Pro, the Control-L and "Autoescuelas Clases Prácticas" App Store listings, and the Gesad (Trevenque) and CIBERSAD sheets.
- **PDFs extracted locally** with pdftotext, from copies in the session scratchpad: Asepeyo (asesorías guide), Economist & Jurist (labour AI prompts), the CCOO Canarias convenio statistics, Colvet (Mar 2025), the ATAAC submission to the CNMC, and the DGT, REPS, INSST, Gesad and CIBERSAD documents.
- **Failed fetches:**
  - HTTP 503: SEPE models page, MITES statistics (CCT and MAC), MAPA PRESVET pages, Clinic Cloud, Gesden;
  - HTTP 403: Wolters Kluwer product pages, REGCESS, Koibox;
  - unreadable (empty or binary): the TED notice 92082-2025 and the Prevencion10 home page.
