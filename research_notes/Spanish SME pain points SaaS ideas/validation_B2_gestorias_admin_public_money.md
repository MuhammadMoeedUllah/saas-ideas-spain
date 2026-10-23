# Validation batch 2: gestorías, the public administration and public money

*Validator: batch 2 of 8. Prepared 23 October 2026 (Cortes dissolved 6 Oct 2026; general election 29 Nov 2026).*
*Ideas: IDEA-06, IDEA-07, IDEA-08, IDEA-09, IDEA-10, IDEA-25, IDEA-26, IDEA-27, IDEA-28.*
*Searches used: 22 of the 24 allowed (log in section 4).*

*Conventions:*
- *[new: URL, date] = fetched or searched in this validation. The date is the page's publication or update date where shown, otherwise the date seen (23 Oct 2026).*
- *[notes: PAIN-ID] = stage-1 evidence.*
- *"Search summary" = a claim read only in a search-result summary; its page was not opened.*
- *"Single source" marks claims with one origin.*
- *Prices exclude VAT unless stated. Scores follow the batch rubric; Sellability is the mean of S1–S8, and Overall = 0.6 × Sellability + 0.4 × P.*

---

## 1. Batch summary

| ID | Name (validated or reshaped form) | Type | Verdict | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Sellability | P | Overall | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IDEA-06 | Gestoría client-readiness cockpit, reshaped as a cross-vendor tracker for the 2027–29 invoicing wave, with free modules | B | RESHAPE | 4 | 3 | 3 | 3 | 3 | 4 | 2 | 3 | 3.13 | 3 | 3.08 | medium |
| IDEA-07 | Official e-notification watchdog and tax-debt guard | C (B) | KILL | 4 | 5 | 2 | 2 | 2 | 4 | 1 | 3 | 2.88 | 3 | 2.93 | high |
| IDEA-08 | Hacienda letter shield (card/Bizum vs 303 cross-check) | B (C) | KILL | 3 | 4 | 2 | 2 | 3 | 3 | 2 | 3 | 2.75 | 3 | 2.85 | medium |
| IDEA-09 | Autónomo cuota and regularisation tracker | C | KILL | 4 | 5 | 2 | 3 | 2 | 5 | 1 | 3 | 3.13 | 3 | 3.08 | medium-high |
| IDEA-10 | SL director guard, reshaped as a gestoría-run director-duty screener | B (was C) | RESHAPE | 4 | 3 | 2 | 3 | 4 | 4 | 1 | 3 | 3.00 | 4 | 3.40 | medium-low |
| IDEA-25 | Pre-lease "can I open here?", reshaped as a B2B address pre-screen for agents and franchise teams (Madrid) | B (A) | RESHAPE | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3.00 | 3 | 3.00 | low |
| IDEA-26 | Grant justification and repayment-risk workspace | B | KILL | 4 | 3 | 2 | 2 | 3 | 4 | 2 | 2 | 2.75 | 3 | 2.85 | medium-low |
| IDEA-27 | Small public-contract radar, including contratos menores | B (A) | KILL | 2 | 3 | 3 | 3 | 2 | 4 | 1 | 3 | 2.63 | 2 | 2.38 | high |
| IDEA-28 | Flood-ready business evidence vault and claims tracker | C | KILL | 2 | 3 | 1 | 2 | 3 | 5 | 1 | 2 | 2.38 | 3 | 2.63 | medium |

**Reading the table**

- **No GO in this batch.** Six ideas are killed and three reshaped. The three reshapes (IDEA-06, IDEA-10, IDEA-25) are all B2B products sold to intermediaries, not €5/month direct subscriptions.
- **Every type C (about €5/month) idea here fails for the same reason.** The administration already gives the core away free, or an incumbent bundles it:
  - official free alerts in DEHú, the AEAT app and BOE NIF alerts (IDEA-07);
  - Declarando's recommended cuota and free calculators (IDEA-09);
  - free Consorcio and Generalitat channels (IDEA-28).

  None of these ideas has a data or integration moat.
- **The gestoría is the only concentrated channel found.** About 30,400 advisory firms with staff exist (CNAE 692), plus 5,869 practising gestores administrativos and 17,000 colegiados graduados sociales.
- **The best use of IDEA-06, IDEA-07, IDEA-09 and IDEA-10 is therefore one gestoría product, not four.** Each was too thin on its own:
  - the cross-vendor client-readiness tracker (IDEA-06) is the core;
  - the quarterly half-capital and accounts-deposit screener (IDEA-10) is a paid module;
  - an apoderamiento-based notification view (IDEA-07) and a bulk societario-base check (IDEA-09) are free retention features.
- **The ideas about dealing with public bodies (IDEA-25 to IDEA-28) are weak.**
  - IDEA-27: the State already publishes minor-contract data and a free tool.
  - IDEA-26 and IDEA-28: an incumbent (Fandit) or free public channels cover the job.
  - IDEA-25: survives only as a niche B2B pre-screen.

---

## 2. Ideas

#### IDEA-06: Gestoría client-obligation cockpit — RESHAPE (medium)

**Validated definition (after reshape).** A vendor-neutral **client-readiness tracker for small gestorías and asesorías** (1–9 staff), led by the 2027–2029 invoicing wave. The gestoría imports its client list (CSV or a3/Contasol/Sage exports). For each client the tool records:
- regime, turnover band and territory (common, foral, Canarias);
- invoicing software, and whether that product shows a VeriFactu declaración responsable;
- the documented VeriFactu or non-VeriFactu mode choice;
- the e-invoicing date (6 Oct 2027 for turnover above €8M, 6 Oct 2028 for the rest [notes: PRO-11, TAX-05]) and the status-reporting date.

It then sends bulk questionnaires and notices (ES/CA/EU), tracks replies, shows a progress board (contacted, diagnosed, needs new tool, ready) and keeps a dated rule-status feed (in the BOE, announced, draft, lapsed).

Three cheap retention modules sit on the same client list:
- the societario €1,424.40 base check (from IDEA-09);
- an apoderamiento-based notification view (from IDEA-07);
- a half-capital ratio check (from IDEA-10).

Price €29–59/month by client count. The €5/month SME "what changed for me" digest is **dropped**: free BOE alerts and vendor content cover it.

**(a) Problem reality and rule status.**
- The job is real and the vendors themselves tell asesorías to do it by hand:
  - TeamSystem's 8-step guide asks asesorías to build "un inventario real de la cartera" by client (entity type, turnover, software, complexity, contact, urgency), segment it and "mide el avance" (clients contacted, diagnosed, needing a tool change) [new: https://teamsystem.es/magazine/verifactu-factura-electronica-asesorias-2027/, 18 May 2026, updated 7 Oct 2026];
  - Sage's checklist asks for a documented per-client choice of VeriFactu mode [new: search summary of https://www.sage.com/es-es/blog/validacion-verifactu-entrada-en-vigor/, 2026; page not opened].
- **No official list of compliant software exists.** The AEAT FAQ says certification is a self-declaration by the producer, and "no se prevé ningún registro previo del producto SIF por parte de nadie" [new: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html, FAQ updated 21 Oct 2026]. Any "is this client's software compliant?" view therefore needs a privately maintained database of producers' declarations. This settles check 5, first part.
- **E-invoicing dates.** Orden HAC/1028/2026 was published in the BOE on 5 Oct 2026 and entered into force the next day, 6 Oct 2026. That starts the periods in DF 8ª of Ley 18/2022 and in DT 1ª–3ª and DF 4ª of RD 238/2026 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-20587, seen 23 Oct 2026]. The Consejo General de Gestores' table puts the periods at 12, 24 and 36 months, with status reporting for firms of €8M or less voluntary until the 36-month date [new: https://www.consejogestores.org/?p=14916, 30 Apr 2026, based on the draft order]. Batch 1 owns C-05 and C-08; the cockpit's value grows with exactly this kind of disagreement.
- **Rule churn under dissolution.**
  - Pending bills lapsed on 6 Oct 2026 (Reglamento del Congreso art. 207 [new: BOE-A-1982-5196 art. 207]).
  - Decree-laws now go to the Diputación Permanente.
  - The 2026 MEI is 0.90% and the 2027 MEI 1.00% (C-03 settled; see IDEA-09).
  - The 2027 módulos limits are again pending [notes: TAX-14].

  These are all rule-status items a gestoría must track per client [notes: TAX-02, LAB-25].

**(b) Competitors.**
- **Single-vendor client panels** cover only clients on that vendor's product:
  - Holded for asesorías: "Verifactu y factura electrónica de serie para todos tus clientes", one panel, partner programme;
  - Quipu: "panel para analizar el estado de tu cartera";
  - Bilky Portal Asesor;
  - CopilotGestoria: "Radar Fiscal" traffic light of clients at risk before filing, VeriFactu remission for clients on its portal, from €15/month, free plan for 5 clients, "100+ gestorías activas".

  CopilotGestoria states that for clients on other programs "el despacho no ve su estado en la pantalla de cartera" [new: search summaries of https://www.holded.com/es/pide-demo-asesorias, https://getquipu.com/es/asesorias and https://copilotgestoria.com/remision-verifactu; https://copilotgestoria.com/ fetched 23 Oct 2026]. That is the cross-vendor gap.
- **Regulatory content and AI Q&A.**
  - TeamSystem Asesor Excelente: training plus AI for regulatory queries; no price [new: TeamSystem article above].
  - a3ASESOR has an alert manager for deadlines and notifications [new: Wolters Kluwer brochure, see IDEA-07].
  - Minsait TaxFinder classifies regulation by client keywords, for large firms [new: search summary of https://www.minsait.com/sites/default/files/06_brochure_tax_finder_v5_1.pdf].
  - BOE a la Carta: free email alerts [new: search summary of datos.gob.es, 6 Nov 2017].
- No product mapping rule changes to a gestoría's client list was found (2 searches).
- Not checked: Sage Despachos and a3 portfolio dashboards (the pages blocked automated access), and Kabilio (invoice OCR only [notes: TAX-23]).

**(c) Buyers and market size (settles the cross-cutting gestoría-count check).**
- INE DIRCE, 1 Jan 2025, CNAE 692 (accounting, bookkeeping, audit and tax advice): **62,234 firms**:
  - 31,840 with no employees;
  - 19,098 with 1–2;
  - 6,557 with 3–5;
  - 2,785 with 6–9;
  - 1,599 with 10–19;
  - 239 with 20–49.

  So about **30,400 have employees** and **28,440 have 1–9 employees** [new: INE API table 73019, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73019?nult=1, seen 23 Oct 2026]. CNAE 691 (legal) adds 83,943 firms, some of them labour advisers.
- Practising gestores administrativos: **5,869**, of 7,466 colegiados at 31 Dec 2025, in 22 colegios. The largest are Cataluña (1,006 practising), Madrid (912), Valencia (476), Sevilla (453) and Galicia (432) [new: Consejo General de Colegios de Gestores Administrativos, Memoria 2025, https://www.consejogestores.org/wp-content/uploads/2026/03/Memoria-2025.pdf, Mar 2026].
- Graduados sociales: **17,000 colegiados** in 43 colegios [new: https://www.graduadosocial.org/, seen 23 Oct 2026].
- These groups overlap (many gestores and graduados sociales trade as CNAE 692 firms). A defensible target is **about 30,000 advisory firms with staff**.
- Ceiling: 5% × 30,000 × €40/month ≈ **€0.7M ARR**; 10% ≈ €1.4M.

**(d) Willingness to pay.**
- Adjacent spend:
  - CopilotGestoria from €15/month;
  - MsNotifica €40–120/month (see IDEA-07);
  - Fandit €56–480/month on annual billing (€70–600 monthly) [new: https://fandit.es/precios/, seen 23 Oct 2026; notes: ADM-16];
  - suites (a3, Sage), prices not published.
- What gestorías pay for legal-update subscriptions was **not found** (Iberley and other pricing pages blocked automated access).
- The original €49–149/month band is above what the visible anchors support; €29–59/month is safer.
- The kill test stays open [I]: fewer than 1 in 5 would pay €30/month or more.

**(e) Distribution.**
- Concentrated professional bodies: the Consejo General de Gestores circulates update bulletins and publishes the draft calendar, and there are 22 colegios de gestores and 43 colegios de graduados sociales.
- Vendor partner programmes: Holded and Quipu. They would be wary of a vendor-neutral tool that exposes migrations.
- Webinars on the 2027–2028 calendar.
- None of these channels is proven for this product.

**(f) Build feasibility and legal constraints.**
- MVP in 1–2 months: CSV import, five rule modules, bulk email/WhatsApp, status feed.
- The tool acts as a GDPR data processor for the gestoría.
- No reserved profession is involved, because the gestoría stays the adviser. The tool gives "status, not advice".
- A tax specialist is needed for the editorial feed, as a recurring cost.
- a3 and Contasol export formats were not verified [F open].

**(g) Defensibility.** Low to medium:
- a dated, accountable rule-status feed;
- a maintained product-declaration database (there is no official list);
- client tags and history as switching cost;
- colegio relationships.

AI makes the summaries nearly free, and each suite vendor can add a readiness panel for its own clients. The cross-vendor position is the only structural edge.

**(h) Kill criteria.**
1. "a3 or Sage already shows cross-vendor readiness for all clients": **not met** (nothing found; single-vendor panels only).
2. Fewer than 1 in 5 interviewed gestorías would pay €30/month or more: **open [I].**
3. "A spreadsheet handles it in a couple of hours per change": **open [I].** TeamSystem's manual checklist suggests the spreadsheet is today's answer.
4. Fewer than 3 of 10 trial gestorías convert: **open [I].**

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | E-invoicing duties 12–24 months out (6 Oct 2027 and 2028); VeriFactu 2027 still in the BOE |
| S2 Buyers | 3 | About 30k advisory firms with staff |
| S3 WTP | 3 | Gestorías already pay €15–120/month for adjacent tools; no direct evidence for rule mapping |
| S4 Reachability | 3 | Colegios and bulletins exist; unproven for this product |
| S5 Competitive gap | 3 | Single-vendor panels and manual checklists; no cross-vendor tool found |
| S6 Build speed | 4 | MVP in 1–2 months |
| S7 Defensibility | 2 | Maintained rules and a product database, but copyable and bundle-able |
| S8 Retention | 3 | Periodic use through the 2027–2029 waves; risk of fading afterwards |

- **Sellability** 3.13. **P** 3: real staff-hours and client-penalty exposure; hours never measured [notes: TAX-23, PRO-10].
- **Overall** = 0.6 × 3.125 + 0.4 × 3 = **3.08**.
- The original broad version would score lower on S3, S5 and S7 because of the free-content risk.

**Open [I] checks.**
- 10–15 gestoría interviews: hours per rule change, how they track clients' software today, WTP at €30/month.
- Five-gestoría concierge pilot on the e-invoicing inventory.
- a3 and Contasol export test.

**What would change the verdict.**
- **To GO:** at least 3 of 10 trial gestorías pay €30/month or more, or a colegio agrees to co-brand.
- **To KILL:** a3 (Wolters Kluwer), TeamSystem or Sage ships a free cross-vendor readiness panel, or interviews show the spreadsheet takes under 2 hours per change.

#### IDEA-07: Official e-notification watchdog and tax-debt guard — KILL (high)

**Validated definition.** A €4–9/month alert service per company (and a €1–2/client board for gestorías) that watches DEHú, the AEAT and the TGSS, escalates before the day-10 deemed-delivery date, tracks certificates and debts, and searches BOE edicts by NIF. Validation found that every core function except multi-channel escalation is already offered free by the administration or sold cheaply by incumbents to gestorías, and that the "no lawful access" fear is unfounded. As a standalone product it is killed. What survives is a feature: an apoderamiento-based, multi-client notification view inside IDEA-06, for gestorías that do not already run a3, Cegid or Sage tools.

**(a) Problem reality and rule status (Oct 2026).** The rule is in force and is not exposed to the election.
- Legal persons, entities without legal personality, professionals in compulsory colegios and their representatives must deal with the administration electronically (Ley 39/2015 art. 14.2). An e-notice is deemed rejected 10 calendar days after it is made available without access to its *content* (art. 43.2). The alert is sent, but "la falta de práctica de este aviso no impedirá que la notificación sea considerada plenamente válida" (art. 41.6) [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-10565/texto/bloque/a43 and /a41, consolidated text, seen 23 Oct 2026].
- Art. 43.1 defines "comparecencia" as access by the interested party or representative "al contenido de la notificación". Viewing the pending list is therefore not access, and the AEAT's own pending-notices screen separates the list (exportable to CSV) from a signed "Firmar y Enviar" step to open content [new: https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/notificaciones-electronicas-ayuda-tecnica/notificaciones-comparecencia-sede.html, updated 19 Oct 2026]. This settles the batch question "does viewing the pending list count as access": no.
- **DEHú coverage (settles part of the section-5 e-notification question).** RD 203/2021 art. 42.5: every notice from a state-level issuer "se pondrá a disposición del interesado a través de la Dirección Electrónica Habilitada única"; issuers may also notify in their own sede. Art. 44.3 tells all administrations to make their notices reachable through DEHú, but adhesion by regions and councils is voluntary (art. 65). Art. 43 calls the alert "de carácter meramente informativo" [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2021-5032/texto/bloque/a4-4, /a4-5, /a4-6, seen 23 Oct 2026]. The AEAT says all its notices, "no sólo las electrónicas", go to DEHú [new: AEAT, informacion-general-sobre-notificaciones-electronicas.html, updated 19 Oct 2026]. So the "9,000+ sedes" problem (vendor claim, [notes: ADM-08]) is real only for regional, local and judicial issuers.
- **Courts.** Legal persons must receive court communications electronically. A first summons unopened for 3 days goes to home delivery and then to the Tablón Edictal Judicial Único; other court communications are deemed made after 3 days (LEC arts. 155.1 and 162.2, versions in force since 20 Mar 2024 and 3 Apr 2025) [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a155 and /a162, seen 23 Oct 2026]. This confirms the snippet-only claim in [notes: ADM-08]; the judicial e-office is a separate channel from DEHú.
- **24-hour embargoes: confirmed, no longer single source.** Resolución de 4 de junio de 2026 of the AEAT's Directorate-General, BOE-A-2026-13031 (BOE 16 Jun 2026). Orders are made available before 20:00, collected between 20:00 and 07:00, and retained "antes de las 08:00 horas del día siguiente". Embargo extends to up to ten accounts per diligencia at the same entity. It applies to diligencias issued from **2 Nov 2026**, with the REST channel from 1 Mar 2027 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-13031, seen 23 Oct 2026]. The press summary was accurate [new: AyE, 22 Aug 2026, https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-podra-embargar-cuentas-bancarias-autonomos-menos-24-horas-partir-septiembre/20260821085621055511.html].
- **Case law is still split; no 2026 Supreme Court ruling was found** (1 search):
  - strict line: TS 1927/2017 [notes: ADM-08] and AN 489/2026 [notes: TAX-18];
  - protective line: TS 17 Dec 2024 (Colombo Enterprises SL v Agencia Tributaria de Andalucía). The court annulled an apremio because the switch to electronic notification was unannounced, and said the administration "debió haber tomado medidas alternativas" once it saw the notice had not been accessed [new: https://primeralecturaediciones.com/sentencias/archivo/el-ts-protege-el-derecho-a-la-tutela-judicial-efectiva-en-notificaciones-electronicas, 4 Feb 2025]. Also TSJ Murcia 396/2025 [notes: ADM-08].

  The fear factor that drives demand persists.

**(b) Competitors.**

| Product | Segment | Coverage claim | Price | Source |
|---|---|---|---|---|
| **Official DEHú** | everyone | AGE plus adhered bodies | free: email alerts to up to 5 addresses; push alerts through the official *Notifica App*; "Gran destinatario" web services for automated consultation | [new: AEAT help pages acceso-notificaciones-electronicas-dehu.html and recibir-avisos-nuevas-notificaciones-comunicaciones-dehu.html, updated 16 Oct 2026] |
| **AEAT avisos** | everyone | AEAT | free SMS and email alerts, plus notification alerts in the AEAT app; up to 30 "días de cortesía" a year when no AEAT notice is put in DEHú | [new: AEAT avisos-notificaciones-telefono-movil-correo-electronico.html and dias-cortesia-notificaciones.html, updated 19 Oct 2026] |
| **BOE TEU and TEJU alerts** | everyone | edicts | free same-day email alert when an edict carrying your NIF is published; companies sign up with a certificate. Caveat: some issuers omit the NIF | [new: https://www.boe.es/notificaciones/ciudadanos_y_empresas/index.php, seen 23 Oct 2026] |
| **MsNotifica (Cegid Microdata)** | professional firms reselling to clients | DEHú, AEAT, Seguridad Social, DGT, e-NOTUM, Junta de Andalucía, Euskadi; "más de 9000 organismos" | 50 CIFs €40/month; 100 €50; 250 €90; 500 €120; extra CIF from €0.25/month, i.e. **€0.24–0.80 per client per month** | [new: http://msnotifica.com/ and http://msnotifica.com/precios/, © 2025, seen 23 Oct 2026] |
| **a3ASESOR \| Portal Neos (Wolters Kluwer)** | asesorías | 060/PAG, AEAT, Seguridad Social, DGT, DEH, GENCAT, ORGT Barcelona, Xunta, Comunidad de Madrid NOTE, Basque foral bodies, LexNET; TEU tracking; certificate-expiry control; mass association of the despacho's certificates or apoderamiento; alert manager | pay per use (no list price) | [new: Wolters Kluwer brochure, https://assets.contenthub.wolterskluwer.com/api/public/content/079a0fe3f7f042369c4c1ecb4ee62ade, undated, older vintage] |
| **IvNeos (Ivnosys, Signaturit group, now Namirial)** | large companies (Cepsa, Iberdrola, Abertis testimonials) | "más de 9.000 organismos públicos" | quote only | [new: https://ivnosys.com/gestor-notificaciones-electronicas-ivneos-2/, seen 23 Oct 2026] |
| **EdasNEO (ZeroComa)** | asesorías; said to be included in Sage Despachos | not verified | not verified | [new: edasneo.com, seen 23 Oct 2026] |
| **CopilotGestoria** | gestorías | — | notification module said to be included in its SaaS (from €15/month) | [new: https://copilotgestoria.com/blog/dehu-2026-guia-apoderamiento-protocolo-gestion-notificaciones-electronicas-gestorias, 28 Apr 2026, vendor source] |
| **Online asesorías bundling it** | autónomos and SMEs | DEHú, via the client's apoderamientos | Ayuda T Pymes: "revisión periódica de DEHú" is part of the service, as an "obligación de medios"; liability capped at 2× fees; plans from €29.95/month | [new: https://www.ayudatpymes.com/terminos_y_condiciones, updated 1 Apr 2026] |

- **Gap.** What is left is multi-channel escalation (WhatsApp and phone call to two named people), a heartbeat, a diligence log, and coverage of non-DEHú regional, local and judicial sedes. All are thin and copyable.
- **Review complaints.** One vendor blog cites "una tasa de error del 41%" in DEHú and AEDAF criticism that email alerts were lost when DEHú replaced NEO. Both are second-hand, and the 41% figure is internally inconsistent [new: CopilotGestoria blog above]. If verified, they would be the strongest argument for an independent watchdog.

**(c) Buyers and market size.**
- INE DIRCE (1 Jan 2025):
  - 3,310,824 active companies, of which 1,859,925 are natural persons;
  - so 1,450,899 legal entities and entities without personality, including 1,127,515 SLs, 46,763 SAs and 108,354 comunidades de bienes [new: INE API table 73018, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73018?nult=1, seen 23 Oct 2026].
- Reachable share: the micro firms without an adviser holding apoderamientos. That share is unknown [I].
- Revenue ceiling at €5/month: 1% of 1.45M entities ≈ 14,500 × €60 ≈ €0.87M ARR. The gestoría channel at incumbent prices (€0.25–0.80/client) is far lower.

**(d) Willingness to pay.** Incumbents sell to gestorías at **€0.24–0.80 per client per month**, 2–8× below the hypothesis of €1–2. SMEs that pay an asesoría €25–130/month already get monitoring inside the fee [notes: TAX-22], [new: Ayuda T T&Cs]. Free official push, email and SMS alerts anchor the SME price near zero.

**Type C test (about €5/month).** Not viable direct to SMEs. The product would be automated and need little support, but its value is invisible in most months and the free official channels deliver the core alert. The only prices with evidence are €0.24–0.80 per client per month inside gestoría tools, or a fee paid by a bank or insurer (none found).

**(e) Distribution.**
- Gestorías are concentrated but are competitors' customers: a3, Cegid and Sage bundle this.
- Banks offering embargo prevention are speculative; no evidence found.
- Notaries and company-formation services at incorporation: unproven.
- Search demand was not measured.

**(f) Build feasibility and legal constraints (settles the cross-cutting access check batch 2 owns).**
- **Lawful access without holding clients' private keys exists.**
  - At the AEAT, the obligated party grants a natural or legal person the **GENERALNOT** power, or a specific power to receive notifications. It is granted online with certificate or Cl@ve, in person, or by notarial document, and the apoderado confirms it. The apoderado then sees the poderdante's notices in DEHú and in the AEAT sede ("En nombre de") with its own credentials [new: AEAT acceso-dehu-mediante-apoderamiento.html, updated 16 Oct 2026].
  - Representation can also be recorded in the State's Registro Electrónico de Apoderamientos (RD 203/2021 arts. 32–33) [new: BOE blocks a3-4, a3-5].
  - DEHú offers **"Gran destinatario"** services "para la consulta automatizada de notificaciones", with published specifications [new: AEAT acceso-notificaciones-electronicas-dehu.html]. Whether a third-party apoderado may use Gran destinatario for many poderdantes was not verified, because the specifications are on dehu.redsara.es, which blocked automated access.
- **Constraints.**
  - The apoderado can open content, which starts deadlines. That is liability (Ayuda T limits it to an "obligación de medios").
  - Non-DEHú regional and local sedes still need per-sede integration.
  - Data are confidential tax data.
  - Holding certificates is not required, but would be needed for sedes without apoderamiento.
- **Time to MVP:** 2–4 weeks for alert parsing and escalation; 1–2 months for an apoderamiento-based DEHú/AEAT reader (subject to the Gran destinatario terms).

**(g) Defensibility.** None for the alert layer. Incumbents own the gestoría base, and the official channels improve for free (Notifica App push, 5 email addresses). Multi-sede coverage is an integration grind that IvNeos, Cegid and Wolters Kluwer have already done.

**(h) Kill criteria.**
1. "No lawful programmatic access without holding clients' private keys" (or certificate custody unacceptable to more than 70% of owners): **not met.** Apoderamiento (GENERALNOT/REA) and Gran destinatario exist.
2. "The official apps already push reliable alerts": **largely met.** DEHú Notifica App push plus up to 5 emails, AEAT SMS/email/app, BOE NIF alerts. Reliability is disputed only by unverified vendor claims.
3. Pilot: under half of pilot companies receive a notice in six months: **open [I].**

Also met: the gestoría board is saturated at prices below the hypothesis.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced, continuous duty; overnight embargo regime from 2 Nov 2026 (BOE-A-2026-13031) |
| S2 Buyers | 5 | About 1.45M legal entities plus colegiados (DIRCE 2025) |
| S3 WTP | 2 | Official alerts are free; gestoría tools cost €0.24–0.80 per client |
| S4 Reachability | 2 | Gestorías already equipped by a3, Cegid and Sage; SMEs without advisers are diffuse |
| S5 Competitive gap | 2 | Several decent tools plus free official push and email; only escalation and non-DEHú sedes are open |
| S6 Build speed | 4 | Alert layer in weeks; apoderamiento reader in 1–2 months |
| S7 Defensibility | 1 | Trivially copyable; incumbents bundle it |
| S8 Retention | 3 | Recurring duty and a diligence log, but invisible value when no notices arrive |

- **Sellability** 2.88 (23/8). **P** 3: severe when it happens (apremio surcharges of 5–20%, embargo), but frequency per firm is unquantified and most firms already have a monitor.
- **Overall** = 0.6 × 2.875 + 0.4 × 3 = **2.93**.

**Open [I] checks.**
- Six-month pilot of notice frequency among micro SLs without an adviser.
- Share of SLs whose gestoría holds GENERALNOT or REA powers.
- Gran destinatario terms for third-party apoderados (download the specification from DEHú).
- Measured DEHú alert failure rate.

**What would change the verdict.**
- Verified evidence that DEHú or AEAT alerts fail often.
- A large set of high-stakes issuers outside DEHú (regional tax agencies, big-city councils, the judicial e-office) that the incumbents do not cover.
- A bank or neobank willing to pay for embargo prevention as a white-label service.

Any of these would justify a RESHAPE to a B2B2C watchdog sold through banks. Otherwise the useful parts become a free feature of IDEA-06.

#### IDEA-08: Hacienda letter shield (pre-filing cross-check and evidence pack) — KILL (medium)

**Validated definition.** A €7–12/month tool for B2C businesses that take cards or Bizum. Before each quarterly VAT and IRPF filing (modelos 303 and 130) it reconciles acquirer, POS and Bizum settlements against invoices and the draft bases. It explains gaps (refunds, tips, personal Bizum, third-party collections, exempt services) and assembles a response pack when a letter arrives.

The reporting rule is confirmed, but three things make a standalone product unattractive:
- there is no data on how often letters arrive;
- a large part of the named target segments cannot have a VAT-return mismatch at all;
- response handling is already bundled by online asesorías.

**(a) Problem reality and rule status.** Confirmed in the BOE; no election exposure.
- **RD 253/2025** of 1 April (BOE-A-2025-6599, 2 Apr 2025) reformulates RGAT art. 38 bis to cover "cualesquiera tipo de tarjetas así como los sistemas de cobro asociados a un número de teléfono móvil" (Bizum). Reporting moves "de ser anual a mensual, desapareciendo el umbral anual neto de 3.000 euros", with effect from 1 Jan 2026. A new art. 38 ter adds an annual report on all cards, excluding cards with under €25,000 a year of charges and credits [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-6599, seen 23 Oct 2026]. The €25,000 exclusion that some press pieces mention belongs to this new annual all-cards report (art. 38 ter; modelo 174 under the Orden below), not to merchants' monthly modelo 170.
- **Orden HAC/747/2025** of 27 June (BOE-A-2025-14600, 15 Jul 2025) approves the monthly modelo 170 for operations of "empresarios o profesionales adheridos al sistema de gestión de cobros a través de cualquier tipo de tarjetas y mediante pagos asociados a números de teléfono móvil". The first return, for January 2026, was filed in February 2026 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-14600, seen 23 Oct 2026].
- **Letters.** "La AEAT ha empezado a remitir cartas de requerimiento" by mismatches appears only in press narration, with **no count and no official source** [new: Xataka Móvil, 19 Aug 2026, https://www.xatakamovil.com/movil-y-sociedad/hacienda-bizum-autonomos-envian-cartas-descuadres-pagos]; [notes: TAX-15] (AyE, 18 Aug 2026). Two searches found no AEAT or Gestha figure.
- **Structural limit (desk inference from the VAT regimes).** Mismatches between card data and the VAT return can only arise for businesses whose VAT return reflects actual sales:
  - retailers in recargo de equivalencia do not file 303 returns for those sales;
  - módulos businesses (many bars and taxis) pay VAT by modules;
  - dental and medical services are VAT-exempt.

  For these groups the card data feed income-tax and módulos-limit checks instead. That shrinks the segment named in the source to general-regime B2C firms in estimación directa, SLs, salons and restaurants outside módulos. This is an inference to verify with gestorías [I].

**(b) Competitors.**
- **Declarando Pro with filings (€69.90/month + VAT):** "Gestión de requerimientos de Hacienda (¡ganamos el 75%!)", plus bank connection and an "antisanciones" guarantee [new: https://declarando.es/precios, seen 23 Oct 2026].
- **Bank reconciliation** is standard in Holded, Quipu and Anfix [notes: TAX-07 software table]. CopilotGestoria cross-checks returns against each other (303 against 390, 111 against 190), but not against modelo 170 [new: https://copilotgestoria.com/, seen 23 Oct 2026].
- **Gestorías and Legálitas** handle letters inside their fees [notes: TAX-16].
- **Gap:** no tool found that explicitly reconciles acquirer and Bizum settlements against 303 bases with the five known causes. The gap is narrow, because bank-feed reconciliation already does most of it.

**(c) Buyers and market size.**
- 94% of small retail and hospitality businesses accept cards [notes: FIN-13].
- After removing recargo de equivalencia, módulos and exempt activities, the addressable group is probably 100k–500k firms (inference, no direct count).
- Ceiling at €10/month: 1% of 300k ≈ 3k × €120 ≈ €0.36M ARR.

**(d) Willingness to pay.** Owners pay for help after a letter arrives (asesoría fees, Declarando's requerimiento handling), not for prevention. A €20/quarter prevention price has no observed anchor.

**(e) Distribution.**
- Acquirers: SumUp has a developer platform, but no partner programme was checked.
- Gestorías: letters land on their desks.
- Associations of salons and restaurants.

None is proven.

**(f) Build feasibility.**
- SumUp's API lists transactions, refunds, payouts and receipts [new: https://developer.sumup.com/api/transactions/list and https://developer.sumup.com/api/payouts/list, seen 23 Oct 2026]. Stripe offers balance transactions and a payout-reconciliation report [new: https://docs.stripe.com/reports/payout-reconciliation, seen 23 Oct 2026].
- Bank-acquired (Redsys) terminals and Bizum-for-business collections are reachable only as bank-statement lines or merchant-portal exports. No public merchant API was found, so ingestion is CSV and manual.
- **Can taxpayers download what their bank reported in modelo 170?** Not established (1 search). If not, the tool rebuilds the figures from the same settlements, which is fine for matching but cannot show "what Hacienda sees".
- MVP: 1–2 months for CSV ingestion and a PDF pack.

**(g) Defensibility.** Low. Accounting suites own the bank feeds and invoices and can add a "card data vs 303" check. The AEAT matching know-how is thin and public.

**(h) Kill criteria.**
1. Letters reach under about 5% of B2C businesses a year: **open.** No count exists, and the structural limit above makes high frequency less likely.
2. Taxpayers cannot see the modelo 170 data their bank filed: **open, probably met** (no access route found).
3. Acquirer data cannot be had without manual work: **partly met.** APIs exist for SumUp and Stripe; for bank terminals and Bizum it is manual.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Monthly reporting in force since 1 Jan 2026, but letters are sporadic and uncounted |
| S2 Buyers | 4 | General-regime B2C firms taking cards, plausibly 100k–500k |
| S3 WTP | 2 | Prevention is not bought; response handling is bundled |
| S4 Reachability | 2 | Diffuse micro B2C; acquirer and gestoría channels unproven |
| S5 Competitive gap | 3 | Bank reconciliation exists; no explicit modelo 170 matcher |
| S6 Build speed | 3 | Integration-heavy for bank terminals and Bizum (CSV only) |
| S7 Defensibility | 2 | Suites can copy it |
| S8 Retention | 3 | Quarterly use |

- **Sellability** 2.75. **P** 3: requerimiento non-response fines of €250–600 and possible reassessments, frequency unknown [notes: TAX-10].
- **Overall** = 0.6 × 2.75 + 0.4 × 3 = **2.85**.

**Open [I] checks.**
- Ask 10 gestorías how many card or Bizum requerimientos they handled in 2026, and the hours each took.
- Confirm whether the AEAT "datos fiscales" show modelo 170 amounts to the taxpayer.
- Validate which client types actually get 303-mismatch letters.

**What would change the verdict.**
- AEAT or Gestha data showing letters to more than 5% of general-regime B2C firms a year.
- An acquirer (SumUp, Revolut Business, a bank) willing to embed the check as a merchant feature and pay per merchant.

Either would support a RESHAPE to a white-label module for acquirers or gestorías.

#### IDEA-09: Autónomo cuota and regularisation tracker — KILL (medium-high)

**Validated definition.** A €3–4/month (or €29/year) subscription for autónomos and societarios. It:
- estimates year-to-date net income for RETA purposes from invoices, bank data or manual entries;
- maps the estimate to one of the 15 tramos;
- shows the coming regularisation in euros;
- reminds the user of base-change windows and checks the societario minimum.

Validation confirms the pain and the formula, but finds the core feature already sold inside the leading autónomo platform and given away as free calculators. Nothing defensible is left for a standalone subscription. It is killed as a product and kept as a free feature (a bulk societario-base check) inside IDEA-06.

**(a) Problem reality and rule status.**
- **2026 parameters (settles C-09).** The 2026 tables are in Orden PJC/297/2026 of 30 March (BOE-A-2026-7296, 31 Mar 2026), art. 18 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-7296, seen 23 Oct 2026]:
  - **Bases:** maximum €5,101.20 for every tramo. Fifteen tramos: three reduced (tramo 1 ≤€670: base €653.59–718.94) and twelve general (tramo 12 >€6,000: minimum base €1,928.10).
  - **Contribution rates:** common contingencies 28.30%, professional 1.30%, MEI 0.90%.

  The "€4,909 maximum base" in [notes: TAX-12] is the 2025 figure; €5,101.20 is correct for 2026. The same table is on the Seguridad Social site [new: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537, seen 23 Oct 2026].
- **MEI (settles C-03).** LGSS DT 43ª (added by RDL 2/2023) sets 0.80 points in 2025, **0.90 in 2026** and **1.00 in 2027**, rising to 1.2 by 2029 [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11724/texto/bloque/dt-14, seen 23 Oct 2026]. Orden PJC/297/2026 confirms 0.90% for 2026 and puts it wholly on the autónomo in RETA. The 0.80% figure in the labour notes came from a page that had not been updated.
- **Net-income rule.** LGSS art. 308.1.c (RDL 13/2022) computes income as IRPF net income plus Social Security contributions, minus a 7% generic-expense deduction (3% for societarios). The TGSS regularises once the tax administration transmits the data the following year [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11724/texto/bloque/a308, seen 23 Oct 2026]. The formula is public and simple.
- **Societarios.** Art. 308.1.a, rule 4ª: societarios and family collaborators cannot choose a base below the Régimen General group-7 minimum, and "en el procedimiento de regularización... la base de cotización definitiva no podrá ser inferior a dicha base mínima". For 2026 that minimum is €1,424.40. Orden PJC/297/2026 art. 18.4 lets them keep their 2025 provisional base during 2026, so a lump-sum back-charge arrives when 2026 is regularised. This confirms [notes: TAX-13].
- **Regularisation calendar.** The 2024 regularisation was notified from January to February 2026. Underpayments are due the month after notification; refunds are automatic [new: Última Hora, 12 Feb 2026, https://www.ultimahora.es/noticias/local/2026/02/12/2568841/pimem-gestores-administrativos-instan-autonomos-revisar-regularizacion-cuotas-2024.html]. Refunds are paid within four months (Seguridad Social page above).
- **Junts bill on societario bases.** No vote or approval was found (1 search). Opponents (PP, Junts, Vox) planned to act through amendments [new: Forbes, https://forbes.es/economia/903587/pp-junts-y-vox-trataran-de-frenar-en-el-congreso-el-sablazo-a-los-autonomos-societarios-y-colaboradores/, 2026]. Under Reglamento del Congreso art. 207 (as amended 22 Jul 2025), "Disuelto el Congreso... quedarán caducados todos los asuntos pendientes" except those for the Diputación Permanente [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1982-5196/texto/bloque/art207, seen 23 Oct 2026]. **Any pending bill lapsed on 6 Oct 2026, so the €1,424.40 floor stands.**
- **2027 bases.** Not set; the 2027 table needs a budget law or decree, and none was found. The MEI rises to 1.0% by law.
- **Pain evidence.** 35.1% paid after regularisation and rated the process 2.2/10 [notes: TAX-12]. Societarios face about +€135/month, and the Ombudsman criticises the method [notes: TAX-13, ADM-11]. National TGSS totals for the 2023 and 2024 regularisations were **not found** (1 search). Only a regional colegio figure exists: in Baleares, 29% of autónomos had well-adjusted bases [new: Última Hora above].

**(b) Competitors.**
- **Declarando Pro** (€39.90/month + VAT on the annual plan without filings; €69.90 with filings) includes "Cuota de autónomo recomendada para evitar reclamaciones de Seguridad Social — Usamos un algoritmo patentado que predice lo que vas a ganar durante el año, para que pagues la cuota adecuada". Declarando also publishes a free "Simulador de la cuota de autónomos" [new: https://declarando.es/precios, seen 23 Oct 2026].
- **Cuéntica** plans: "Calcula la cuota de autónomos y el tramo que te corresponde según tu contabilidad real". It also offers a free public calculator with the 2026 tables [new: https://cuentica.com/precios/ and https://cuentica.com/calculadora-cuota-autonomos/, seen 23 Oct 2026].
- **Import@ss (TGSS)** shows each person's "Regularización anual de cuotas" result and lets them change bases. No simulator with alerts was found on its landing page [new: https://portal.seg-social.gob.es/wps/portal/importass/importass/, seen 23 Oct 2026].
- Not checked: Quipu, Holded, TaxDown and Infoautónomos tool pages (Holded's calculator URL returned 404).
- **Gap.** Only autónomos who use a traditional gestoría or a basic invoicing app lack continuous tracking. Their gestoría already gets the regularisation notices through RED.

**(c) Buyers and market size.**
- 3,483,645 people in the RETA at end-Sep 2026 [notes: FIN-18], and about 1.2M societarios and collaborators [notes: TAX-13].
- Ceiling: at €29/year, 1% of the RETA is about 35k × €29 ≈ €1.0M ARR. The share willing to pay is unknown; ENA shows high outsourcing (57%) [notes: TAX-22].

**(d) Willingness to pay.** The adjacent spend is high (€25–150/month for gestorías and online asesorías [notes: TAX-22]), but this feature is bundled at no marginal price. Free calculators anchor the standalone price at €0. The source's own kill test (at least 1 in 10 trial users paying €2/month) is open [I], but the market anchors are discouraging.

**Type C test (about €5/month).** Not viable. The product would be automated with almost no support, but monthly value is invisible except around regularisation, and free calculators exist. No standalone price above €0 is evidenced. It works only as a bundled feature, in an invoicing app or a gestoría tool.

**(e) Distribution.**
- High-intent searches exist ("regularización cuota autónomos", "calculadora cuota autónomos"), but they are dominated by Infoautónomos, Declarando, Cuéntica and TaxDown content (desk observation).
- Gestorías and colegios already campaign on the regularisation: the colegio de gestores and PIMEM did so in Baleares [new: Última Hora].
- Invoicing apps can add the feature themselves.

**(f) Build feasibility.**
- Formula and tables are public (LGSS 308; Orden PJC/297/2026), so an MVP takes under 4 weeks.
- Changing the base for the user requires an Import@ss authorisation or RED access. The six change windows a year are from the notes [notes: TAX-12]; the regulation article was not re-fetched.
- Income data is sensitive, so GDPR applies; no certification is needed.

**(g) Defensibility.** None. The calculation is public and incumbents already market it (Declarando's "algoritmo patentado").

**(h) Kill criteria.**
1. "Declarando, Cuéntica and Quipu already warn users about band changes": **met** for Declarando (continuous recommendation) and Cuéntica (tramo from real accounts); Quipu not checked.
2. "The TGSS portal already offers a reliable simulator with alerts": **not met** (none found).
3. "Fewer than 1 in 10 trial users pay €2/month or more", or retention collapses after one regularisation: **open [I].**

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Annual enforced regularisation; societario back-charge on 2026 income; MEI to 1% in 2027 |
| S2 Buyers | 5 | 3.48M RETA members |
| S3 WTP | 2 | Bundled in paid plans and free calculators; no standalone spend evidenced |
| S4 Reachability | 3 | Search demand is real but owned by incumbents' content; gestorías campaign already |
| S5 Competitive gap | 2 | Declarando and Cuéntica track it; free simulators |
| S6 Build speed | 5 | Public formula; MVP in under 4 weeks |
| S7 Defensibility | 1 | Trivially copyable |
| S8 Retention | 3 | Periodic use; risk of churn after the regularisation |

- **Sellability** 3.13. **P** 3: a lump-sum cash shock (about €1,600/year for societarios) of money owed anyway, with no penalty if paid on time.
- **Overall** = 0.6 × 3.125 + 0.4 × 3 = **3.08**.

**Open [I] checks.**
- Paid conversion at €2–3/month among autónomos who use traditional gestorías.
- Whether gestorías would pay for a bulk societario-base check (about 1.2M affected).
- National TGSS regularisation totals.

**What would change the verdict.** Official data showing that a large share of autónomos (above 30%) receive back-charges above €1,000, plus a distribution deal with a large invoicing app or bank willing to embed and pay per user. Even then the moat stays at zero, so it would be at best a feature, not a business.

#### IDEA-10: SL director guard (dissolution-trigger and accounts-deposit alerts) — RESHAPE (medium-low)

**Validated definition (after reshape).** A gestoría-run **director-duty screener** rather than a €5/month owner app. Each quarter it bulk-imports trial balances for all of a gestoría's SL clients (a3, Contasol, Holded or Quipu exports, or CSV). It then:
- computes net equity *for dissolution purposes* against half the share capital;
- flags clients that crossed the line, including SLs whose 2020–2021 losses stopped being excluded after the financial year starting in 2024;
- generates a dated warning letter to the directors and a meeting-notice template reviewed by a commercial lawyer;
- logs the two-month clock (convene the meeting, or file for insolvency or restructuring talks);
- tracks the annual-accounts deposit (one month after approval; registry closure; ICAC fines).

Price: €19–39/month per gestoría, or €0.50–1 per SL in bulk, possibly as a module of IDEA-06. Owners can get a read-only alert.

**(a) Problem reality and rule status.** In force; not exposed to the election.
- LSC art. 363.1.e: a company must dissolve "por pérdidas que dejen reducido el patrimonio neto a una cantidad inferior a la mitad del capital social". Art. 365.1: directors must convene the general meeting "en el plazo de dos meses".
- Art. 367.1: directors who miss this "responderán solidariamente de las obligaciones sociales posteriores al acaecimiento de la causa de disolución". Art. 367.2: "Salvo prueba en contrario", claimed debts "se presumirán de fecha posterior". Art. 367.3: filing for insolvency or communicating restructuring talks within two months gives a safe harbour [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2010-10544/texto/bloque/a363, /a365, /a366, /a367, seen 23 Oct 2026].

  The burden of proof sits on the director, which is exactly why a dated evidence log has value.
- **New why-now not in the notes.** Ley 3/2020 art. 13, as last amended by RDL 20/2022, excluded 2020 and 2021 losses from the art. 363.1.e test only "hasta el cierre del ejercicio que se inicie en el año 2024" [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2020-10923/texto/bloque/a1-5, consolidated, seen 23 Oct 2026]. From the 2025 accounts, closed on 31 Dec 2025 and approved in 2026, those losses count again. SLs that survived on the exclusion may now be inside the dissolution cause without knowing it. How many is unknown.
- **STS 1477/2026** (single press source). The court reportedly held that "corregir tarde las pérdidas no elimina esa responsabilidad" and that "desconocer una deuda concreta no da al administrador un nuevo plazo de dos meses". The claim was €42,000. Experts advise owners to ask their accounting firm for "an explicit alert on equity balance and cash position" [new: AyE, 23 Oct 2026, https://www.autonomosyemprendedor.es/articulo/pymes/supremo-confirma-que-autonomos-societarios-pueden-asumir-deudas-sl-actuan-tiempo/20261022150439056494.html]. The ruling's date, chamber and ECLI were not given; CENDOJ was not checked.
- **Accounts deposit.** LSC arts. 279, 282 and 283: deposit within a month, registry closure, ICAC fines of €1,200–60,000 [notes: TAX-21]. The registry sheet closes one year after the year-end without a deposit [new: search summary of https://www.economistjurist.es/noticias-juridicas/el-cierre-registral-de-las-sociedades-mercantiles-que-es-cuales-son-sus-consecuencias-y-como-solucionarlo].
- **Calculation nuance.** Net equity for dissolution purposes includes adjustments, for example participative loans and ICAC criteria [new: search summary of BOICAC 136 commentary, https://primeralecturaediciones.com/documentos_diana/cursos/2025/CIERRE_2024/RESUMENES_BOICAC/BOICAC%20136_5.pdf]. A naive ratio is wrong in edge cases, which is a small rules moat.

**(b) Competitors.** No accounting suite or asesoría tool advertising a half-capital or dissolution alert was found (1 search covering a3, Sage, Holded and Contasol). Today the check is done by gestorías at year-end closing, "when they notice" [notes: FIN-17], or by lawyers. Any accounting vendor could add the ratio.

**(c) Buyers and market size.**
- **SLs:** INE DIRCE 2025 counts **1,127,515 SLs**: 334,941 with no employees, 398,349 with 1–2, 180,169 with 3–5 and 94,717 with 6–9. About 1.0M have fewer than 10 employees [new: INE table 73018, seen 23 Oct 2026].
- **Insolvency context:** SLs are 93.2% of company insolvencies [notes: FIN-17], and there were 1,427 micro-firm insolvency procedures in 2025 [notes: FIN-16]. In 2025, 2,656 "sin masa" insolvencies were concluded [new: Registradores, Anuario concursal 2025, https://www.registradores.org/documents/d/guest/anuario-concursal-2025, seen 23 Oct 2026]. Counts of art. 367 liability claims and of SLs that fail to deposit accounts were **not found** (1 search).
- **Reshaped buyer:** about 30k advisory firms with staff (see IDEA-06). At €29/month, 5% ≈ €0.5M ARR. At €0.75 per SL in bulk, 5% of SLs ≈ €0.5M ARR.

**(d) Willingness to pay.** No direct anchor. The adjacent spend is accounting services at €59.95–129/month for SLs [notes: TAX-21]. The gestoría's own professional-liability exposure, if it fails to warn a client, is the likely motive, but it was not evidenced [I].

**Type C test for the original (€5/month per SL).** Not viable. Owners of struggling SLs are the least likely to act on or pay for alerts, and asesorías treat the ratio as a free feature [notes: FIN-17]. The reshaped price is €19–39/month per gestoría, or €0.50–1 per SL in bulk, and still needs testing [I].

**(e) Distribution.**
- Asesorías, which hold the books.
- Colegios de gestores and economistas.
- Accounting-software marketplaces (Holded and Quipu partner programmes).
- D&O insurers and brokers (speculative).

**(f) Build feasibility.**
- Low complexity: trial-balance CSV import, ratio logic with ICAC adjustments, templates, audit log. MVP in 3–6 weeks.
- The templates need commercial-lawyer review. Output must be "information, not legal advice"; advice on insolvency strategy stays with lawyers.
- No certification is needed; the GDPR processor role applies.

**(g) Defensibility.** Weak. Any suite can add the ratio. The edge is the evidence trail (dated letters, meeting-notice templates, the deposit calendar), cross-vendor bulk import, and bundling with IDEA-06.

**(h) Kill criteria.**
1. The main suites already alert on the half-capital trigger: **not met** (none found).
2. Asesorías will not distribute it: **open [I].**
3. Behavioural risk that owners of struggling SLs ignore alerts: unresolved. The reshape moves the alert to the gestoría, which has an incentive to document its warning.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced duty with personal liability; 2020–21 losses count again from the 2025 accounts |
| S2 Buyers | 3 | About 30k gestorías as buyers; 1.13M SLs underneath |
| S3 WTP | 2 | No observed spend; motive is liability protection |
| S4 Reachability | 3 | Asesoría channel concentrated but unproven |
| S5 Competitive gap | 4 | Only manual, gestoría or lawyer options found |
| S6 Build speed | 4 | MVP in about 1 month, plus legal review |
| S7 Defensibility | 1 | Trivially addable by accounting vendors |
| S8 Retention | 3 | Quarterly screening plus the annual deposit cycle |

- **Sellability** 3.00. **P** 4: personal liability for company debts is existential for owner-managers, and art. 367.2 puts the burden on them; frequency unquantified.
- **Overall** = 0.6 × 3.0 + 0.4 × 4 = **3.40**.
- The original €5/month owner app scores about the same on the rubric: S2 rises to 5, while S3 falls to 1, S4 to 2 and S8 to 2, for a Sellability of about 3.0. The reshape is chosen for two reasons the rubric does not capture: it moves the alert to the party with an incentive to act and document it, and it uses a concentrated channel. The behavioural kill risk (owners of struggling firms ignore alerts) applies to the original, not the reshape.

**Open [I] checks.**
- Would 10 asesorías run a quarterly bulk screen, and pay €19–39/month?
- How many SL clients per gestoría are near the line, especially after the 2020–21 reactivation?
- Read STS 1477/2026 in CENDOJ.

**What would change the verdict.**
- **To GO:** gestorías say they already face client claims for not warning, or a D&O insurer wants it as a risk-reduction perk.
- **To KILL:** a3, Sage or Holded ship the alert, or gestorías say they check it at year-end anyway and see no value in quarterly screening.

#### IDEA-25: Pre-lease "can I open here?" check and file builder (Madrid first) — RESHAPE (low)

**Validated definition (after reshape).** A **B2B address pre-screen for people who place businesses into premises**: commercial estate agents, franchise expansion managers and the listing teams of portals, starting in Madrid. For an address plus an activity it returns:
- the planning zone and its use rules (PGOUM norma zonal, plus special plans and acoustic-protection zones; these two layers are background knowledge, not verified here);
- the licensed-activity history of the premises, from the council's open census of premises and licences;
- the likely procedure (declaración responsable or licence), the regulated ECU price and the standard timelines;
- a "needs technician" flag, with a paid referral to an ECU or architect.

Every answer is reviewed by a planning professional during the MVP. The subscription is €99–199/month for 10–30 checks. The €49 one-off check for first-time entrepreneurs is **dropped as a lead product**: it is a one-off purchase with diffuse buyers, so acquisition is expensive.

**(a) Problem reality and rule status.**
- Madrid's service charter (last evaluated 24 Feb 2026) confirms:
  - 13,301 declaraciones responsables and licences, 3,805 inspections and 22,695 people served in 2025;
  - standards (targets, not results) of an average 109 days to check a declaración responsable (40% within 90 days) and 137 days for a licence (40% within 60 days);
  - a paid "Consulta urbanística común y especial para actividades";
  - the 4% ICIO tax.

  Results against the standards are published separately on madrid.es ("Cartas de Servicios"), and **the 2025 results were not retrieved** [new: https://www.madrid.es/UnidadesDescentralizadas/Calidad/CARTAS%20SERVICIOS/SistemaCartasServicio/41%20CS_de%20la%20Agencia%20de%20Actividades/DEFINITIVA/CS_ADA_2026.pdf, read via WebFetch, 23 Oct 2026].
- Municipal rules are not exposed to the election. The 2027 ECU prices approved on 15 Oct 2026 were not re-verified [notes: ADM-01].
- **València.** Drafting of the new procedural ordinance began in May 2025 [notes: ADM-02]. A construction-regulation aggregator lists an "Ordenanza reguladora de licencias urbanísticas y de actividades y de otros títulos habilitantes en Valencia", "Versión 2026", published 27 Jan 2026 [new: https://normatia.com/es/normativa/licencias-urbanisticas-actividades-valencia/, seen 23 Oct 2026]. This is single source; approval and BOP publication are not verified, and it is unclear whether it is the new text.

**(b) Competitors.**
- **Technicians:** viability studies "around 300 €" for a change of use (Habitissimo guide). Technicians on Certicalia offer no-commitment assessments whose fee is deducted if they are later hired for the project. That is lead-generation-like, but not free [new: search summaries of https://www.habitissimo.es/presupuestos/estudio-viabilidad and https://www.certicalia.com/preguntas/p/convertir-local-en-vivienda-en-madrid-18478, 2026].
- **ECUs** (19 in Madrid; e.g. SGS): €500–1,000 for an urban-compatibility certificate [notes: ADM-01]. No ECU was found offering a free pre-check (1 search).
- **The council's paid consulta urbanística:**
  - "consulta urbanística especial de actividades": tasa €347.35 (2016 figure), documents "firmada por técnico competente", "un plazo de un mes para contestar". The council "quedará vinculado al informe técnico" only if the licence is later sought "en idénticos términos";
  - consulta común: tasa €52.85 (2016) [new: https://papelea.com/es/ayuntamiento-de-madrid/consulta-urbanistica-especial-de-actividades, updated 3 Aug 2020; Papelea's consulta común page, same site, via search summary].

  Current 2026 fees not verified. The official route is cheap-to-mid priced but slow (one month) and needs a technician, which is the speed gap a 48-hour pre-screen would fill. Madrid also publishes past planning consultations, e.g. CU 27-18 [new: https://transparencia.madrid.es/UnidadesDescentralizadas/UDCUrbanismo/Consultas Urbanisticas/2018/CU 27-18.pdf, search summary]. They are a free interpretive corpus a product could use, and that users can read themselves.
- **Málaga's free ALU assistant** [notes: ADM-03].
- No online "can I open X at address Y" product for Madrid was found (2 searches).

**(c) Buyers and market size.**
- Madrid: about 13,300 files a year (charter).
- The reshaped buyer (commercial agents, franchise teams) was not counted [I].
- Ceiling for Madrid: 300 agents and teams × €150/month ≈ €0.54M ARR. Each extra city needs its own rules work.

**(d) Willingness to pay.**
- Openers already pay €300 for a technician's viability study, €500–1,000 for an ECU certificate, and €600–1,250+ for an ECU-managed declaración responsable [notes: ADM-01]. The council's own consulta cost €52.85 (común) or €347.35 (especial) in 2016, with a one-month answer [new: Papelea, above].
- A €49–149 pre-screen sits well under these anchors, but is less authoritative.
- **Type A (secondary) test.** The price gap is large: €49–149 against €300–1,000. But the switch is not realistic as a substitute, because ECU certificates and the council's consulta carry legal weight and a pre-screen does not. It works as a complement that filters premises before paying for the binding step, which is why the reshape targets repeat placers.
- Agents' willingness to pay is unevidenced [I].

**(e) Distribution.**
- Commercial agents and portals.
- Franchise associations.
- ECU and architect referral fees, both ways.
- High-intent searches ("qué licencia necesito para abrir un bar en Madrid"); demand not measured.

**(f) Build feasibility and legal constraints (settles the data-availability kill test for Madrid).**
- Madrid's Geoportal lists "Planeamiento Urbanístico" among its services [new: https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/index.iam, seen 23 Oct 2026]. Services follow OGC standards (WMS, WFS) and data can be downloaded as shapefiles under a commercial-reuse licence. The PGOUM97 building-conditions plan is catalogued as open vector data [new: search summaries of the Ayuntamiento's JIIDE 2019 Geoportal presentations, https://idee.es/resources/presentaciones/JIIDE19/28-JIIDE2019_Ayuntamiento_Madrid_Geoportal.pdf].
- The charter says datos.madrid.es publishes granted licences, declaraciones responsables, the census of premises and activities, and the ECU list "en formatos reutilizables". The portal was "En mantenimiento" on 23 Oct 2026.
- **What is missing:** the *use-compatibility rules* themselves (the PGOUM normative text, and any special plans or acoustic-zone rules) are legal text, not data. They must be encoded and maintained by hand. That is the main build cost (2–4 months for Madrid's top 20 activities, with professional review), and also the moat.
- Barcelona, València, Sevilla and Málaga data were **not checked**.
- **Liability:** a wrong "allowed" verdict can cost a lease and fit-out. The product needs clear disclaimers, review by a técnico competente and professional-liability insurance. Binding certification stays with ECUs and the council.

**(g) Defensibility.** Moderate: a city-by-city encoded rules set plus a licence-history join, reviewer network and ECU partnerships. AI lowers the cost of a first draft, not of a legally reviewed answer. Each city is slow to model.

**(h) Kill criteria.**
1. "Madrid's planning data cannot be obtained in usable form": **not met.** GIS layers and licence and premises data are open; the rules must be hand-encoded.
2. "ECUs or architects answer free as lead generation": **partly met.** Some technicians offer no-commitment assessments credited against later fees; no free ECU pre-check was found.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Strong recurring pain for placement teams; no legal deadline |
| S2 Buyers | 2 | Madrid agents and franchise teams, likely 5k–20k at most |
| S3 WTP | 3 | Openers pay €300–1,000 for adjacent services; agents' spend unknown |
| S4 Reachability | 3 | Agents and portals are concentrated but unproven |
| S5 Competitive gap | 4 | Only technicians, ECUs and the paid council consultation |
| S6 Build speed | 3 | 2–4 months of rules encoding, plus review and insurance |
| S7 Defensibility | 3 | Encoded city rules plus reviewer network |
| S8 Retention | 3 | Subscription for repeat placers |

- **Sellability** 3.00. **P** 3: months of rent and fit-out at risk per wrong premises; scale unquantified [notes: ADM-03].
- **Overall** = 0.6 × 3.0 + 0.4 × 3 = **3.00**.
- The original B2C €49 check scores lower: S2 2, S4 2, S8 1, giving a Sellability of about 2.75 and an Overall of about 2.85.

**Open [I] checks.**
- Will 10 Madrid commercial agents or franchise teams pay €99–199/month?
- Madrid's 2025 results against its charter standards.
- The current consulta urbanística fees (last seen at €52.85 and €347.35, 2016).
- Whether ECUs will pay referral fees.
- Data and rules in Barcelona, València, Sevilla and Málaga.

**What would change the verdict.**
- **To GO:** a portal or franchise network commits to a pilot, or measured search demand is high.
- **To KILL:** Madrid launches a free ALU-style assistant, or reviewers cannot keep turnaround under 48 hours at a viable cost.

#### IDEA-26: Grant justification and repayment-risk workspace — KILL (medium-low)

**Validated definition.** A workspace where an SME (€19/month per active grant) or a grant consultancy (€149/month for up to 20 grants) uploads the award resolution and call rules. AI extracts obligations, deadlines, eligible costs and evidence requirements. An evidence vault maps invoices, payments, contracts and publicity proof to each obligation, and the tool flags repayment risk.

The repayment risk is now formalised and real. The product still fails on four counts:
- the wave of new NextGenerationEU grants has ended;
- the largest SME cohort (Kit Digital) is justified by intermediaries;
- the consultancy segment is already served by an incumbent grant-management platform priced near the hypothesis;
- no defensible asset remains.

**(a) Problem reality and rule status (settles the NGEU section-5 item).**
- The official recovery-plan site says "España cierra en plazo el Plan de Recuperación y España Crece toma el relevo para movilizar más de 120.000 M€". It also lists the seventh and final payment request, with 148 milestones (the €25,861M amount appears only in the URL) and the definitive milestones document dated 20 Aug 2026. **No extension of beneficiary execution or justification to 2027 or 2028 is mentioned** [new: https://planderecuperacion.gob.es/, seen 23 Oct 2026].
- CEOE's request to extend to 2028 remains a proposal [notes: ADM-14].
- **Orden HAC/580/2026** of 9 June (BOE-A-2026-12520, 10 Jun 2026) regulates the procedure for repaying funds received from the Recovery and Resilience Facility (art. 37 RDL 36/2020) [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-12520, seen 23 Oct 2026]:
  - **procedure:** where the instrument sets none, Ley 38/2003 art. 42 applies;
  - **evidence window:** a prior requirement gives "un plazo no inferior a veinte días hábiles" to produce documentation, extendable by 10 working days when it depends on third parties;
  - **presumption of breach:** missing compliance certificates create a presumption of non-compliance, which "no recaerá sobre los perceptores últimos";
  - **relief:** private beneficiaries may defer or split repayment debts.

  So the repayment exposure for 2026–2028 is real and has a short evidence window. Merca2 links the order to Kit Digital, digitalisation, energy-efficiency and solar grants [new: https://www.merca2.es/2026/06/11/reintegro-fondos-mrr-orden-hac580-2394640/, 11 Jun 2026, secondary].
- The flow of *new* NGEU grants ended with the 31 Aug 2026 milestone deadline. Merca2 reports €14,972M of grants still unawarded in July 2026; a vendor blog says about €25,000M is pending execution; the two figures measure different things [new: search summaries of https://www.merca2.es/2026/07/29/fondos-next-generation-plazo-2426560/ and https://tecnociminnova.com/es/noticias/fondos-next-generation-empresas].
- Ordinary national and regional grants (Ley 38/2003) continue [notes: ADM-16, 81,665 calls].

**(b) Competitors.**
- **Fandit** [new: https://fandit.es/precios/, seen 23 Oct 2026]:
  - **plans:** PRO €56/month (annual billing, 1 licence); PREMIUM €200/month (5 licences) with an "ERP de subvenciones" (unlimited files, tasks and internal tracking), white label and a client area; CORPORATE €480/month (15 licences);
  - **features:** a "Radar de oportunidades" showing "qué ayudas encajan con cada cliente", an AI assistant that drafts technical reports, an API and an MCP server;
  - **service:** it does not process applications itself and refers users to consultancies through a marketplace.

  Fandit is the natural owner of post-award tracking for consultancies and can add justification checklists.
- **Consultancies and installers:** fees not found [notes: ADM-14, ADM-15].
- **GrantBite** compares grant-management software. The page blocked fetching and its tools are mostly aimed at nonprofits [new: search summary of https://www.grantbite.com/es/blog/10-mejores-software-de-gestion-de-subvenciones-en-2026].
- No Spanish SME-side justification SaaS was found (1 search).

**(c) Buyers and market size.**
- NGEU had 1.46M beneficiaries, 70% SMEs, mostly Kit Digital, whose paperwork was handled by agents [notes: ADM-14, ADM-12].
- The number of non-Kit SME beneficiaries who justify grants themselves was **not found**; the BDNS records awards, not who prepares the justification. Those who could buy are plausibly in the tens of thousands (MOVES, energy, hiring and regional lines), but this is inference.
- The consultancy segment is probably 1–3k firms (inference, not counted).
- Ceiling at €19 per grant per month: 10k active grants ≈ €2.3M ARR, an optimistic case.

**(d) Willingness to pay.**
- Consultancies already pay €56–480/month for Fandit (adjacent).
- SMEs pay consultants (fees unknown) or installers who bundle the paperwork.
- The €149/month consultancy price sits below Fandit Premium (€200) and would be compared directly with it.

**(e) Distribution.**
- Consultancies (but Fandit already owns them), installers (MOVES and energy), gestorías, Cámaras.
- Search terms "justificación subvención" and "reintegro" were not measured.

**(f) Build feasibility.**
- Document AI for calls and resolutions, an evidence vault and checklists: MVP in about 6 weeks.
- Programme templates need per-programme legal reading (DNSH, publicity, double-funding and compliance-certificate rules for MRR).
- Liability: the output is a checklist, not advice. Financial documents are confidential.

**(g) Defensibility.** Low. Extraction is a commodity, templates are copyable, and the channel incumbent (Fandit) has 25,000+ companies and consultancies on its platform [notes: ADM-16].

**(h) Kill criteria.**
1. Fewer than a quarter of interviewed grant-holding SMEs manage justification themselves: **open [I].** The Kit Digital structure and the Andalusian MOVES "empresa adherida" model point that way [notes: ADM-15].
2. Consultancies won't pay €149/month: **open [I].** An incumbent at €200 with ERP features makes a new €149 tool a hard sell.
3. The NGEU wave fades after 2026–2028: **met in direction.** No new NGEU grants after 31 Aug 2026. The successor "España Crece" is described only as mobilising more than €120bn; its instruments (grants or loans) were not read.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Formal repayment procedure with a 20-working-day evidence window (Orden HAC/580/2026) |
| S2 Buyers | 3 | Self-justifying SME beneficiaries plausibly 20k–100k (unverified) |
| S3 WTP | 2 | SMEs rarely pay software per grant; consultancies already have Fandit |
| S4 Reachability | 2 | Beneficiaries are diffuse; the consultancy channel is owned |
| S5 Competitive gap | 3 | No SME-side tool found; the consultancy side is served |
| S6 Build speed | 4 | MVP in about 6 weeks |
| S7 Defensibility | 2 | Copyable; incumbent channel |
| S8 Retention | 2 | Grant-bound lifecycle |

- **Sellability** 2.75. **P** 3: repayment plus interest can be large, but frequency is unquantified.
- **Overall** = 0.6 × 2.75 + 0.4 × 3 = **2.85**.

**Open [I] checks.**
- The share of non-Kit SME grant holders who justify alone.
- Consultancy fee models.
- How many Orden HAC/580/2026 requirements are being issued (IGAE, managing bodies).

**What would change the verdict.** Evidence that thousands of SMEs and installers face 20-day repayment requirements with no consultant. That would justify a narrow, paid "repayment-defence evidence pack". So would a white-label deal with Fandit or a regional agency.

#### IDEA-27: Small public-contract radar, including contratos menores — KILL (high)

**Validated definition.** A €19–39/month feed of small tenders plus a "who buys what, from whom, at what price" database of minor contracts, with alerts on recurring purchases and expiring contracts. Its claimed moat, a normalised minor-contract dataset nobody else has, is **false**:
- the State publishes minor contracts as daily open data;
- the State provides a free tool to process them;
- an incumbent already sells minor-contract intelligence and alerts from €300 a year.

**(a) Problem reality and rule status.**
- **Thresholds:** contratos menores are below €40,000 for works and €15,000 for supplies and services (LCSP art. 118, 2020 version) [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2017-12902/texto/bloque/a1-30, seen 23 Oct 2026].
- **Publication duty:** art. 63.4 requires publishing minor contracts "al menos trimestralmente" with "su objeto, duración, el importe de adjudicación, incluido el Impuesto sobre el Valor Añadido, y la identidad del adjudicatario". Only contracts under €5,000 paid through an anticipo de caja fija are exempt [new: BOE-A-2017-12902, block a6-5].
- **Tribunal de Cuentas:** art. 335.1 adds an annual list of all contracts, including minor ones, sent to the Tribunal de Cuentas [new: block a3-47].
- **Statistics vs raw data:** OIReScon still states "no se dispone de datos agregados de la contratación menor del Sector Público", and audits flag splitting of minor contracts [new: OIReScon IAS 2025 executive summary, https://www.hacienda.gob.es/rsc/oirescon/informe-anual-supervision-2025/ias2025-resumen-ejecutivo-es.pdf, approved 22 Dec 2025]. That refers to national statistics, not raw availability (see f).

**(b) Competitors.**
- **Official open data (free).** The Ministry of Hacienda publishes the dataset "Contratos menores publicados en los perfiles del contratante ubicados en la Plataforma de Contratación del Sector Público (desde el 1 de enero de 2018)":
  - updated daily (ATOM/CODICE), with yearly and monthly zips (sindicación 1143);
  - a separate feed aggregates *tenders* from the regional platforms since 2016, but it explicitly excludes minor contracts. Minor contracts of bodies whose perfil sits only on a regional platform are therefore not in the national feed;
  - plus the free **OpenPLACSP** tool "para facilitar el tratamiento de los conjuntos de datos abiertos" [new: https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx and .../contratosmenores.aspx, seen 23 Oct 2026].
- **A sample of the live feed** (167 entries on 23 Oct 2026) carries the object, contracting body, amounts with and without VAT, the awardee's NIF and name, CPV code, award date and an SME-awarded flag [new: https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_1143/contratosMenoresPerfilesContratantes.atom, fetched 23 Oct 2026].
- **Gobierto Contratación** (company plans) [new: https://contratos.gobierto.es/empresas/planes and https://contratos.gobierto.es/empresas, seen 23 Oct 2026]:
  - Intro €300/year (3 alerts, 3-month history, awards); Mid €500/year;
  - Pro €150/month; Intel €300/month; Corp €475/month; Enterprise €1,490/month;
  - one-off reports on any company, body or sector "Desde 18 €", including "qué contratos de tus competidores terminan pronto";
  - its explorer lists "Contrato Menor" records.
- **licitaciones.es:** alerts, AI and ROLECE help; prices not published (pricing URLs return HTTP 410) [notes: ADM-17]; [new: licitaciones.es, seen 23 Oct 2026].
- **Euroalert:** EU focus [notes: ADM-18].
- **Free PLACSP tender alerts** for registered operators: background knowledge, not verified this session.

**(c) Buyers and market size.**
- 206,242 tenders in 2024 (€113.1bn) [notes: ADM-17].
- The number of micro suppliers selling to public bodies is unknown. 19% of firms reportedly avoid public tenders because of late payment (attribution uncertain) [notes: FIN-04].
- The price ceiling is set by Gobierto Intro at €300/year.

**(d) Willingness to pay.** Anchors are €18 per report and €300–500/year entry plans (Gobierto). The hypothesised €19–39/month (€228–468/year) is the same price as an incumbent that already has the data.

**Type A (secondary) test.** Fails. The incumbent's entry price (€300/year) is not high enough to leave room for a cheaper alternative, and the underlying data is free.

**(e) Distribution.** SEO ("contratos menores [ayuntamiento]"), Cámaras, sector associations and gestorías. All unproven, and Gobierto and licitaciones.es already compete on SEO.

**(f) Build feasibility.**
- Easy for PLACSP-hosted bodies: the documented ATOM feed can be ingested in weeks.
- Harder for bodies on regional platforms that do not syndicate minor contracts: Catalonia, Madrid region and others were not checked.
- Reuse is permitted under public-sector-data rules [notes: ADM-18].

**(g) Defensibility.** None. The data is public and pre-aggregated by the State, and incumbents already sell the intelligence layer.

**(h) Kill criteria.**
1. Fewer than half of sampled municipalities publish supplier and amount: **not met** for PLACSP-hosted bodies (legal duty plus open feed). Regional-platform coverage is not sampled.
2. licitaciones.es already covers minor contracts: **unverified.** The equivalent condition is **met by Gobierto Contratación**, whose explorer includes minor contracts with alerts.
3. Copy-risk test (does anyone already hold a normalised minor-contract dataset?): **met** for PLACSP-hosted bodies. The State (PLACSP open data and OpenPLACSP) and Gobierto hold it. The only residual gap is minor contracts on the seven regional platforms and on municipal profiles outside PLACSP; Gobierto's coverage of these was not checked.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 2 | Opportunity-driven; no duty |
| S2 Buyers | 3 | Public-sector suppliers, plausibly 20k–100k |
| S3 WTP | 3 | Some spend, but anchors are €300/year |
| S4 Reachability | 3 | SEO and associations; unproven |
| S5 Competitive gap | 2 | Several decent tools plus free official data |
| S6 Build speed | 4 | Documented feed |
| S7 Defensibility | 1 | Public data |
| S8 Retention | 3 | Alerts are used periodically |

- **Sellability** 2.63. **P** 2: missed opportunities, not losses.
- **Overall** = 0.6 × 2.625 + 0.4 × 2 = **2.38**.

**Open [I] checks.**
- Interviews with 20 micro suppliers on willingness to pay and late-payment fears.
- Minor-contract syndication on the seven regional platforms.

**What would change the verdict.** Only a distinct product would. For example, a bid-preparation co-pilot for micro firms (ROLECE, the European Single Procurement Document, solvency) with evidence that micro firms convert, or a vertical (cleaning, maintenance) where recurring-contract renewal prediction beats Gobierto. That would be a new idea, not this one.

#### IDEA-28: Flood-ready business evidence vault and multi-programme claims tracker — KILL (medium)

**Validated definition.** A €4/month-per-premises app. Before a flood it guides an inventory of premises, stock and equipment (photos, serial numbers, invoices) and stores policies off-site. After a flood it produces a claim dossier and tracks announced aid programmes. It would be sold through insurers, brokers and gestorías in Valencia and Alicante.

The need is real after an event. But prevention has no observed willingness to pay, the post-event steps are already free and simple, and the product has no moat.

**(a) Problem reality and rule status.**
- **DANA 2024 (La Moncloa, data at 19 Oct 2026)** [new: https://www.lamoncloa.gob.es/info-dana/Paginas/2026/191026-datos-seguimiento-actuaciones-gobierno.aspx, updated 19 Oct 2026]:
  - AEAT direct aid: 27,466 applications with a payment order (16,035 autónomos, 11,431 companies); €347.5M paid;
  - Consorcio: 251,940 claims, €4,658.6M paid, "ya se han gestionado el 99,7%";
  - ERTE: 4,169 company applications;
  - Reinicia Auto+: 42,245 grants;
  - CDTI LIC/LICa: 70 applications, 26 rejected.

  The 2024 backlog is essentially cleared, which weakens the "files still pending two years later" pain [notes: CITY-01].
- **dana Adam (Oct 2026), single outlet, two articles:**
  - 6,528 Consorcio claims between 16 and 18 Oct (Valencia province 5,007, Oliva alone 2,760; Alicante 847), with no split by type [new: elDiario.es, 22 Oct 2026, https://www.eldiario.es/comunitat-valenciana/consorcio-compensacion-seguros-recibe-6-500-solicitudes-indemnizacion-dana-adam_1_13605957.html];
  - the first €23.5M package covers households (€6,000 per main home, €3,000 per second home, €800/month for rehousing) and councils (up to €200,000);
  - a second package "en los próximos días" will cover vehicles, the primary sector, commerce, hospitality and animal shelters, with no amounts;
  - there will be "una única solicitud" online at the Generalitat's e-office [new: elDiario.es, 21 Oct 2026, https://www.eldiario.es/comunitat-valenciana/gobierno-valenciano-aprueba-paquete-ayudas-23-5-millones-euros-afectados-dana-adam_1_13603195.html].
- **What evidence the Consorcio asks for:** policy details, bank account, repair estimates and invoices, and photos of removed damaged goods; an adjuster then visits. Claims can be filed by phone, online or through the insurer or broker, and are accepted after the seven-day legal window [new: elDiario.es, 22 Oct 2026].

  These are simple steps that a phone camera and a folder already cover.

**(b) Competitors.**
- No Spanish insurer pre-loss inventory app was found. Mapfre's business multi-risk pages describe flood cover only [new: search summary of https://www.mapfre.es/seguros/empresas/negocio/seguro-multirriesgo-empresarial/, seen 23 Oct 2026] (1 search).
- Substitutes are free: phone photos and cloud storage, the Generalitat's single application, and free legal and notarial help [notes: CITY-02].

**(c) Buyers and market size.**
- Valencia and Alicante provinces have 186,970 and 145,106 companies [notes: CITY-01 via G5].
- More than 12% of the Comunitat Valenciana's population lives in flood-susceptible areas [new: MITECO PATRICOVA document, search summary of https://www.miteco.gob.es/es/agua/formacion/Patricova%20Comunidad%20Valenciana_tcm30-82916.pdf].
- The 2024 DANA hit 2,386 industrial firms in the "zona cero", 21% of the province's industrial firms [new: Cámara Valencia, Apr 2025, search summary of https://www.camaravalencia.com/wp-content/uploads/2025/04/Recuperacion-economica-de-la-zona-cero-seis-meses-despues-de-la-dana.pdf].
- No count of businesses in mapped flood zones was found. Proportional inference gives roughly 40k in the region (12% of about 332k), unverified.

**(d) Willingness to pay.** None observed for prevention. Post-event help is free (Consorcio filing, Generalitat legal aid). The insurer-bundled route is unevidenced.

**Type C test (€4/month).** Not viable. The value appears only after a rare event, the refresh tasks need user effort, and free substitutes exist. Only a per-policy fee paid by an insurer or bank could work, and no such price was found.

**(e) Distribution.**
- Insurers and brokers (B2B2C), gestorías, associations in affected comarcas.
- No partner evidence. Post-event search spikes are short.

**(f) Build feasibility.** Low complexity: mobile capture, OCR of invoices, encrypted storage. MVP in 3–4 weeks.

**(g) Defensibility.** None. A generic vault is trivially copyable, and insurers can add an inventory step to their own apps.

**(h) Kill criteria.**
1. No insurer, broker or gestoría network agrees to a pilot: **open [I].**
2. Pre-event sign-up converts below 2%: **open [I].**

The desk evidence (free substitutes, simple Consorcio requirements, a cleared 2024 backlog) makes both likely.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 2 | Event-driven; no pre-event duty |
| S2 Buyers | 3 | Tens of thousands of firms in flood-prone Valencia and Alicante (inference) |
| S3 WTP | 1 | Prevention unpaid; post-event help free |
| S4 Reachability | 2 | Depends on unproven insurer or broker deals |
| S5 Competitive gap | 3 | No dedicated tool, but free substitutes |
| S6 Build speed | 5 | MVP in 3–4 weeks |
| S7 Defensibility | 1 | Copyable |
| S8 Retention | 2 | Rarely used |

- **Sellability** 2.38. **P** 3: catastrophic when it strikes, but rare per firm and largely insured or Consorcio-covered.
- **Overall** = 0.6 × 2.375 + 0.4 × 3 = **2.63**.

**Open [I] checks.**
- Broker and insurer pilot appetite.
- Whether documented pre-loss inventories change Consorcio payouts or speed (ask adjusters).
- The share of dana Adam claims from businesses.

**What would change the verdict.** An insurer, bank or the Consorcio funding the app per policy, ideally with an adjusting workflow that uses the inventory, or evidence that payouts rise materially with pre-loss documentation. Either would support a B2B2C reshape sold to insurers.

---

## 3. Cross-cutting findings (rule status and market facts for other batches)

**3.1 E-notifications and third-party access (batch 2 owns this check)**
- **Who must receive electronically, and the 10-day rule.** Legal persons, entities without legal personality (such as comunidades de bienes), professionals in compulsory colegios and their representatives must deal electronically (Ley 39/2015 art. 14.2). A notice is deemed rejected 10 calendar days after it is made available without access to its *content* (art. 43.2). A missing alert does not invalidate it (art. 41.6; RD 203/2021 art. 43, "meramente informativo"). Viewing the pending list is not access (art. 43.1). All rule status is in force with no election exposure [new: BOE API, Ley 39/2015 and RD 203/2021].
- **All state-level issuers must notify through DEHú** (RD 203/2021 art. 42.5), and the AEAT sends all its notices there. Regional and local issuers adhere voluntarily, so the residual fragmentation is regional, local and judicial.
- **Lawful third-party monitoring without holding clients' keys exists:**
  - the AEAT GENERALNOT power (or a specific power to receive notifications) to a natural or legal person;
  - REA apoderamientos (RD 203/2021 arts. 32–33);
  - DEHú "Gran destinatario" services for automated consultation (terms for third parties not verified).

  This matters to any idea that assumes "we will read the client's official mailbox". Examples are the immigration ideas (IDEA-52, IDEA-53, IDEA-57), where colegiado filers receive resolutions electronically as representatives (Ley 39/2015 art. 14.2.c–d), and the gestoría channel generally [new: AEAT help pages, 16–19 Oct 2026].
- **Free official alerts now exist:**
  - DEHú email to up to 5 addresses, and push through the *Notifica App*;
  - AEAT SMS, email and AEAT-app alerts;
  - up to 30 AEAT "días de cortesía" a year;
  - BOE same-day email alerts by NIF for the Tablón Edictal Único (administrative edicts) and the judicial edict board.
- **Courts.** Legal persons receive court communications electronically. A first summons unopened for 3 days goes to physical delivery and then to the judicial edict board; other communications are deemed made after 3 days (LEC arts. 155.1 and 162.2, in force). Relevant to IDEA-01 (MASC and claims, on the defendant side) and IDEA-17 (dismissal claims) [new: BOE API, LEC].
- **Overnight bank embargoes confirmed.** Resolución AEAT 4 Jun 2026, BOE-A-2026-13031 (16 Jun 2026): retention before 08:00 the day after the order, up to ten accounts per diligencia. It applies to diligencias from **2 Nov 2026**, with a REST channel from 1 Mar 2027. This upgrades TAX-19 from single source to official, and is relevant to IDEA-01, IDEA-02 and any cash-flow idea.

**3.2 Market counts (gestorías and companies)**
- **CNAE 692** (accounting, bookkeeping, audit, tax advice), INE DIRCE at 1 Jan 2025: **62,234 firms**; 31,840 without employees; **about 30,400 with employees**; 28,440 with 1–9. CNAE 691 (legal): 83,943 [new: INE API table 73019].
- **Gestores administrativos:** 7,466 colegiados at 31 Dec 2025, **5,869 practising**, in 22 colegios. The largest are Cataluña (1,006 practising), Madrid (912), Valencia (476), Sevilla (453) and Galicia (432) [new: CGCOGA Memoria 2025, Mar 2026].
- **Graduados sociales:** **17,000 colegiados** in 43 colegios [new: graduadosocial.org].
- **Legal forms** (DIRCE 2025): 1,127,515 SLs (334,941 with no employees; about 1.0M with fewer than 10); 46,763 SAs; 108,354 comunidades de bienes; 19,181 cooperatives; 140,321 associations; 1,859,925 natural persons [new: INE API table 73018].
- **Employers (for batch 3, C-04).** DIRCE 2025 counts 1,800,443 companies with no employees, so **1,510,381 have at least one**. This confirms G2's roughly 1.51M arithmetic on the DIRCE basis; the Consejo de Estado's 1.35M and CODEM's 1.23M are different bases.

**3.3 Social-security parameters (settles C-03 and C-09)**
- **MEI:** 0.90% in 2026 (Orden PJC/297/2026 art. 18.2.c; LGSS DT 43ª), **1.00% in 2027**, 1.10% in 2028, 1.2% from 2029 [new: BOE-A-2026-7296; LGSS DT 43ª]. The 0.80% figure is the 2025 rate. This affects IDEA-16, IDEA-19 and the IDEA-06 feed.
- **RETA 2026** (Orden PJC/297/2026, BOE-A-2026-7296):
  - 15 tramos; minimum base €653.59; maximum base €5,101.20 for every tramo (the "€4,909" figure was 2025's);
  - societarios and family collaborators have a floor of €1,424.40, which also binds in the regularisation (LGSS art. 308.1.a, rule 4ª);
  - net income for RETA = IRPF net income plus SS contributions, minus 7% (3% for societarios) (LGSS art. 308.1.c).

**3.4 Parliamentary lapse rule (for every batch)**
- Reglamento del Congreso art. 207 (as amended 22 Jul 2025): "Disuelto el Congreso... quedarán caducados todos los asuntos pendientes de examen y resolución por la Cámara", except matters for the Diputación Permanente (decree-law convalidation) [new: BOE-A-1982-5196 art. 207].
- **Every bill pending on 6 Oct 2026 has lapsed:** the Junts societario-base bill (IDEA-09), the minors' digital-protection bill (IDEA-63), the PRESVET sanctions reform if it was still a bill (IDEA-42), and others. Regulations (royal decrees, orders) can still be approved by the Government.

**3.5 Tax-tech items for batch 1 and others**
- **No official list of compliant VeriFactu software.** The AEAT FAQ (updated 21 Oct 2026) says certification is the producer's self-declaration and "no se prevé ningún registro previo del producto SIF". Any idea promising "is my software compliant?" (IDEA-04, IDEA-05, IDEA-06, IDEA-39) must build its own database.
- **Orden HAC/1028/2026** (BOE-A-2026-20587), published 5 Oct 2026, entered into force on 6 Oct 2026, starting the periods in DF 8ª of Ley 18/2022 and in RD 238/2026 DT 1ª–3ª and DF 4ª. The Consejo de Gestores' draft table makes status reporting for firms of €8M or less voluntary until the 36-month date. Batch 1 owns C-05 and C-08.
- **Modelo 170 confirmed in the BOE:**
  - RD 253/2025 (BOE-A-2025-6599): monthly reporting of collections by any card and by "sistemas de cobro asociados a un número de teléfono móvil" (Bizum), with no €3,000 threshold, from 1 Jan 2026;
  - Orden HAC/747/2025 (BOE-A-2025-14600): first return for Jan 2026, filed in Feb 2026; also approves the monthly modelo 196 (accounts) and the annual modelo 174 (cards, €25,000 threshold).

  Relevant to IDEA-39 (salon payments), IDEA-05 and C-24.

**3.6 Public money**
- **Orden HAC/580/2026** (BOE-A-2026-12520, 10 Jun 2026) regulates repayment of Recovery Facility funds. A prior requirement gives **at least 20 working days** to produce documentation, extendable by 10; private beneficiaries may defer or split repayment debts. Relevant to IDEA-13 (Kit Digital websites), IDEA-60 (startup public funding post-award) and IDEA-61.
- **No extension of NGEU beneficiary execution to 2028** is shown on planderecuperacion.gob.es. The site headlines "España Crece toma el relevo para movilizar más de 120.000 M€" (details not read; IDEA-60 should check whether it is grants or loans).
- **Minor contracts are open data.** PLACSP has published minor contracts daily since 2018 (sindicación 1143), with object, body, amounts, awardee NIF and name, CPV and an SME flag, plus the free OpenPLACSP tool. This covers only bodies whose perfil is on PLACSP; the regional-platform aggregation excludes minor contracts. Gobierto Contratación sells alerts and competitor intelligence from €300/year and reports from €18. Relevant to any procurement or B2G idea (STA-13, PRO-17).

**3.7 Company law (for startup and finance ideas)**
- LSC arts. 363.1.e, 365, 366 and 367 are confirmed: the two-month duty; joint liability for later debts; a presumption that claimed debts post-date the cause; a safe harbour if insolvency or restructuring is filed within two months.
- Ley 3/2020 art. 13 excluded 2020–21 losses only up to the close of the financial year starting in 2024. **From the 2025 accounts those losses count again.**
- Relevant to IDEA-59 and IDEA-60: loss-making startups often sit near the half-capital line. The treatment of participative loans as equity for this test appears only in a search summary and was not verified.

**3.8 Disaster data**
- La Moncloa (19 Oct 2026): 99.7% of the 251,940 DANA-2024 Consorcio claims are processed, and €4.66bn paid.
- dana Adam: 6,528 Consorcio claims in three days; business aid still undefined (single outlet).

**3.9 City licensing (for IDEA-29, IDEA-32, IDEA-37 and IDEA-39)**
- Madrid publishes open data on granted licences, declaraciones responsables, the census of premises and activities, and ECUs (per the service charter; datos.madrid.es was "en mantenimiento" on 23 Oct 2026).
- The Geoportal offers planning layers (WMS/WFS, shapefile downloads).
- Madrid's consulta urbanística especial: one-month answer, tasa €347.35 (2016 figure).

---

## 4. Search log

**WebSearch queries (22; limit 24)**

| # | Idea | Query |
|---|---|---|
| 1 | IDEA-07 | DEHú "gran destinatario" consulta automatizada notificaciones apoderados certificado especificaciones |
| 2 | IDEA-07 | gestor notificaciones electrónicas DEHú para pymes y autónomos precio al mes alertas WhatsApp |
| 3 | IDEA-07 | Tribunal Supremo 2026 sentencia aviso notificación electrónica falta de aviso correo validez embargo DEHú casación |
| 4 | IDEA-06 | asesorías panel cartera de clientes estado VeriFactu factura electrónica por cliente a3 Wolters Kluwer Sage TeamSystem Holded partners |
| 5 | IDEA-06 | alertas normativas personalizadas por cliente para asesorías y gestorías IA BOE boletines autonómicos precio suscripción |
| 6 | IDEA-09 | Seguridad Social regularización cuotas autónomos 2024 resultados cuántos pagarán devolución millones Import@ss simulador aviso ajustar base 2026 |
| 7 | IDEA-09 | proposición de ley Junts base mínima cotización autónomos societarios familiares colaboradores Congreso votación 2026 |
| 8 | IDEA-06 | software asesorías "radar normativo" OR "obligaciones por cliente" clientes afectados cambios normativos gestoría avisos automáticos clientes VeriFactu |
| 9 | IDEA-08 | modelo 170 datos fiscales "cobros con tarjeta" consultar autónomo sede AEAT ver información que el banco ha declarado Bizum 2026 |
| 10 | IDEA-08 | Hacienda cartas requerimientos autónomos descuadre cobros tarjeta Bizum modelo 303 2026 cuántas cartas Gestha comprobaciones |
| 11 | IDEA-10 | software contabilidad alerta "causa de disolución" patrimonio neto inferior mitad capital social aviso automático a3 Sage Holded Contasol asesoría |
| 12 | IDEA-10 | Registradores estadística depósito de cuentas anuales 2025 número sociedades que no depositan cuentas cierre registral porcentaje pymes abreviado |
| 13 | IDEA-25 | Madrid geoportal datos abiertos planeamiento PGOUM normas zonales usos compatibles descarga WFS shapefile visor urbanístico licencias actividad |
| 14 | IDEA-25 | informe de viabilidad local comercial antes de alquilar Madrid precio compatibilidad urbanística online licencia de actividad estudio previo euros |
| 15 | IDEA-25 | ECU Madrid "estudio previo" OR "consulta previa" gratuita viabilidad local actividad entidad colaboradora urbanística gratis antes de alquilar |
| 16 | IDEA-26 | software justificación subvenciones empresas cuenta justificativa plataforma gestión ayudas públicas pymes consultoras precio SaaS |
| 17 | IDEA-26 | expedientes de reintegro subvenciones Next Generation empresas 2026 número justificación pymes requerimientos reintegro MRR datos IGAE |
| 18 | IDEA-27 | buscador contratos menores adjudicatarios alertas pymes licitaciones.es precio planes Tendios Licitalia contratos menores base de datos |
| 19 | IDEA-28 | aseguradora app inventario de bienes fotos antes del siniestro comercio pyme España seguro multirriesgo inventario digital inundación Mapfre AXA Allianz |
| 20 | IDEA-28 | número de empresas y polígonos industriales en zonas inundables Comunitat Valenciana PATRICOVA estudio 2025 riesgo de inundación actividades económicas |
| 21 | IDEA-25 | València nueva ordenanza de licencias de obras y actividades 2026 aprobación pleno declaración responsable plazos Urbanismo Catalá |
| 22 | IDEA-25 | Madrid "consulta urbanística especial" actividades tasa importe euros plazo de respuesta Agencia de Actividades ordenanza fiscal servicios urbanísticos |

- **Allocation against plan:** IDEA-06 3 (plan 4); IDEA-07 3 (4); IDEA-08 2 (2); IDEA-09 2 (3); IDEA-10 2 (2); IDEA-25 5 (3); IDEA-26 2 (2); IDEA-27 1 (2); IDEA-28 2 (2).
- IDEA-25 overspent because the open-data and official-consultation questions decided its verdict. The IDEA-27 kill came from direct fetches of official data.

**Main pages fetched directly (no general search engine was queried through any fetch tool)**

- **BOE open-data API** (consolidated articles and daily summaries; the daily summaries were scanned by date only to locate BOE identifiers):
  - Ley 39/2015 arts. 14, 41 and 43;
  - RD 203/2021 arts. 32–34 and 41–45;
  - LEC arts. 155 and 162;
  - LSC arts. 363 and 365–367;
  - Ley 3/2020 art. 13;
  - LGSS art. 308 and DT 43ª;
  - LCSP arts. 63, 118 and 335;
  - Reglamento del Congreso art. 207;
  - BOE-A-2026-13031 (embargo resolution), BOE-A-2026-7296 (Orden PJC/297/2026), BOE-A-2026-20587 (Orden HAC/1028/2026), BOE-A-2026-12520 (Orden HAC/580/2026), BOE-A-2025-6599 (RD 253/2025) and BOE-A-2025-14600 (Orden HAC/747/2025);
  - BOE Tablón Edictal Único information and alert pages.
- **AEAT help pages:** notifications, DEHú, apoderamiento GENERALNOT, alerts, días de cortesía (updated 16–19 Oct 2026); VeriFactu FAQ on the declaración responsable (21 Oct 2026).
- **INE API:** DIRCE tables 73018 and 73019.
- **datos.gob.es catalogue API:** queried by dataset title for city planning datasets (5 calls, mostly HTTP 403). This is the official open-data catalogue, not a general search engine, and it yielded nothing used here.
- **Professional bodies and official sites:**
  - Consejo General de Gestores: Memoria 2025 and the e-invoicing calendar post;
  - graduadosocial.org;
  - planderecuperacion.gob.es;
  - La Moncloa DANA tracking (19 Oct 2026);
  - Hacienda open data for PLACSP and the PLACSP minor-contract ATOM feed;
  - the OIReScon IAS 2025 summary;
  - the Madrid Agencia de Actividades service charter 2026 and the Madrid Geoportal;
  - Seguridad Social cotización 2026 and the Import@ss landing page;
  - the Registradores Anuario concursal 2025.
- **Vendors:**
  - notifications: MsNotifica (home and prices), Ivnosys IvNeos, the Wolters Kluwer a3ASESOR Portal Neos brochure, EdasNEO (JavaScript only), CopilotGestoria (home and DEHú blog), the Ayuda T Pymes T&Cs;
  - autónomo platforms: Declarando prices, Cuéntica prices and calculator;
  - VeriFactu content: the TeamSystem magazine;
  - payments: SumUp and Stripe API docs;
  - grants and procurement: Fandit prices, Gobierto Contratación (company page and plans), licitaciones.es (prices URL returned HTTP 410);
  - Normatia.
- **Press:**
  - AyE (24-hour embargo article; STS 1477/2026 article);
  - elDiario.es (two dana Adam articles);
  - Xataka Móvil (Bizum letters);
  - primeralecturaediciones.com (TS 17 Dec 2024);
  - Papelea (Madrid consulta especial).
- **Blocked or unavailable** (recorded so later stages do not retry blindly): dehu.redsara.es and administracionelectronica.gob.es (WAF); datos.madrid.es (maintenance); sage.com, iberley.es and grantbite.com (403); datos.gob.es API (partly 403).

**Checks left open for later stages ([I] or unresolved desk checks)**

| Idea | Open checks |
|---|---|
| IDEA-06 | Gestoría interviews: hours per rule change, WTP at €30/month or more; a3 and Contasol export formats; legal-update subscription prices |
| IDEA-07 | Notice-frequency pilot; Gran destinatario terms for third-party apoderados; measured alert failure rate |
| IDEA-08 | Letter counts (AEAT, Gestha); whether taxpayers can see their modelo 170 data; which client types get 303-mismatch letters |
| IDEA-09 | National TGSS regularisation totals; paid conversion at €2–3/month |
| IDEA-10 | Gestoría distribution and WTP; counts of art. 367 claims and of SLs failing to deposit accounts; STS 1477/2026 text in CENDOJ |
| IDEA-25 | Agent and franchise WTP; Madrid's 2025 results against its standards; current consulta fees; other cities' data |
| IDEA-26 | Share of SMEs justifying grants alone; consultancy fees; volume of Orden HAC/580/2026 requirements |
| IDEA-27 | Micro-supplier interviews; regional platforms' minor-contract syndication |
| IDEA-28 | Insurer and broker pilot appetite; effect of pre-loss inventories on payouts |
