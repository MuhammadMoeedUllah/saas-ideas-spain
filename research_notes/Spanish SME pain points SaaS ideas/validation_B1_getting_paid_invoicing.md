# Validation batch 1: getting paid, invoicing and the SME software bill

*Prepared 23 October 2026 by the batch 1 validator. Ideas: IDEA-01, IDEA-02, IDEA-03, IDEA-04, IDEA-05, IDEA-11, IDEA-12, IDEA-13, IDEA-36.*

*Status: work in progress. Sections are appended as each idea is finished.*

## 1. Batch summary

(to be filled when all ideas are done)

## 2. Ideas

(appended below as each idea is finished)

## 3. Cross-cutting findings

(to be filled)

## 4. Search log

(running count kept below)

| # | Query | Idea |
|---|---|---|

---

#### IDEA-01: MASC pre-litigation kit and court-ready claim file — RESHAPE (medium)

**Validated definition (after reshape).** A self-serve "small-claim lane" for B2B invoice creditors with claims of €300–2,000, plus a community-arrears module sold to administradores de fincas. It runs the whole path without a lawyer, which is legally possible only below €2,000: a direct-negotiation request or a confidential binding offer, sent by qualified or certified email/SMS (burofax optional), a 30-day clock, a reply log, an evidence pack and a pre-filled monitorio petition. Above €2,000 it switches to a negotiation request (no lawyer needed) and hands the file to a partner lawyer if the debtor opposes. The landlord-eviction module and the "court-criteria library" moat are dropped from the first version. Price: €19–29 per claim, or €9–15/month for a bundle; administradores at about €1 per community per month.

**Why reshape.** Three findings changed the idea:
1. The law allows a lawyer-free path only in part. LO 1/2025 art. 6.2 makes a lawyer mandatory for a binding offer above €2,000, while direct negotiation between the parties needs none at any amount (art. 5.1) [new: BOE consolidated LO 1/2025, https://www.boe.es/buscar/act.php?id=BOE-A-2025-76, last update 04/06/2025, seen 23 Oct 2026]. The monitorio petition needs no lawyer or procurador at any amount, but an opposition above €2,000 does (LEC arts. 23.2.1º, 31.2.1º, 814.2, 818.1) [new: BOE consolidated LEC, https://www.boe.es/buscar/act.php?id=BOE-A-2000-323, last update 07/10/2026, seen 23 Oct 2026]. Eviction for non-payment is a juicio verbal by subject matter, so it always needs a lawyer and procurador (same articles; inference from art. 31.2.1º, which exempts only claims decided by amount).
2. Courts are converging on lenient proof, which shrinks the value of a city-by-city criteria dataset (see angle a).
3. LAU evictions fell 57.7% year on year in Q2 2026 (2,244), and the RDL 29/2026 suspension regime is in flux, so the landlord module has a shrinking, lawyer-bound court pipeline [new: LegalToday on CGPJ data, https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/los-organos-judiciales-practicaron-4-474-lanzamientos-en-el-segundo-trimestre-un-357-menos-que-en-el-mismo-periodo-del-ano-pasado-2026-10-16/, 16 Oct 2026].

**(a) Problem reality and rule status**
- **In force, no lapse.** LO 1/2025 is an enacted organic law. The BOE consolidated text shows no amendment since 4 Jun 2025 [new: BOE LO 1/2025, seen 23 Oct 2026]. The dissolution does not affect it; only a new law could change it.
- **Scope covers monitorios, community monitorios and evictions.** Art. 5.2 applies the requirement to all declarative processes in Book II of the LEC and the special processes in Book IV, which include the monitorio. Its exceptions list (fundamental rights, art. 158 CC, disability, filiation, summary possession, ruin demolition, minors, juicio cambiario) excludes neither the monitorio, nor the LPH art. 21 community monitorio, nor eviction for non-payment [new: BOE LO 1/2025]. This settles the G3 validation question on LPH art. 21 in favour of "MASC required", by the text. I found no court decision on that point.
- **Proof rules.** Without a neutral third party, the attempt is proved by a document signed by both parties, or by "cualquier documento que pruebe que la otra parte ha recibido la solicitud... en qué fecha, y que ha podido acceder a su contenido íntegro" (art. 10.2). The process ends without agreement 30 calendar days after receipt with no reply (art. 10.4). A binding offer lapses after one month (art. 17.4). Sending a request that defines the dispute interrupts limitation, including when sent "a través del medio de comunicación electrónico empleado por las partes en sus relaciones previas" (art. 7.1) [new: BOE LO 1/2025].
- **Courts are relaxing:**
  - Madrid's first-instance judges (26 Sep 2025) accept burofax, buromail, buroSMS, email, SMS and WhatsApp if identity, content, dates and real receipt are proven; a refused or uncollected notice counts as received [new: ECIJA, https://www.ecija.com/actualidad-insights/eidas-y-masc-claves-para-acreditar-electronicamente-la-negociacion-previa-en-determinados-procesos-civiles-y-mercantiles/, 15 Oct 2025].
  - AAP Barcelona 1190/2025 (25 Nov 2025) admitted a claim after a burofax that was never collected, and held that an offer to start negotiating is enough without a concrete proposal [new: Gómez-Acebo & Pombo, https://ga-p.com/publicaciones/oferta-de-un-masc-por-burofax-no-contestado/, 9 Feb 2026].
  - AP Murcia, Section 4, admitted a claim after an unanswered burofax: "no es posible que la eficacia de un acto jurídico penda de la voluntad del requerido" [new: CGPJ, https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Noticias-Judiciales/La-Audiencia-de-Murcia-avala-el-burofax-como-propuesta-de-negociacion-antes-de-la-demanda-de-divorcio, 6 Feb 2026].
  - Salamanca's judges (6 May 2026) accept certified "envíos MASC" and treat a missing mention or proof as curable, but a missing attempt as incurable [new: search-result summary of https://www.icasal.com/src/uploads/2026/05/4.11-Acta-jueces-salamanca-6-5-2026.pdf, not opened; single source].
  - I found no Supreme Court ruling unifying the doctrine (search 2).
- **Friction is still real.** 49.3% of 1,164 surveyed Madrid lawyers had trouble proving the attempt (ICAM, Dec 2025; one outlet) [new: Moncloa.com, https://www.moncloa.com/2026/10/06/requisito-masc-lo-1-2025-juzgados-3443197, 6 Oct 2026]. 89% of suppliers never or almost never claim interest [notes: FIN-03].
- **Official channel.** Additional provision 3 asks the Ministry and the regions to set up MASC services whose functions are information, registers of neutrals, support to courts and statistics. It does not create a delivery channel [new: BOE LO 1/2025]. The Ministry's PIMASC project would register attempts made through mediation or private conciliation and issue a "documento normalizado... firmado digitalmente" as proof. Negotiation is a later phase and the binding offer is "under analysis". The page said "Se espera estar en producción durante el mes de marzo de 2025", and I found no confirmation that it went live [new: Ministerio de Justicia, https://www.mjusticia.gob.es/es/servicio-justicia/proyectos-transformacion/Foro-Transformacion/innovacion-mejora-servicio-publico-justicia/masc, seen 23 Oct 2026]. On 6 Oct 2026 there was still no public register, official form or certified channel [new: Moncloa.com, 6 Oct 2026].
- **Reform risk.** ICAM wants MASC made voluntary [notes: LEG-01]. My search for 29-N party programmes on MASC found nothing (search 3), so this stays open.

**(b) Competitors**
| Name | Offer | Price | Notes |
|---|---|---|---|
| RedClaimer (redclaimer.es) | Lawyer-drafted burofax, plus certified email, SMS and calls; claims to meet LO 1/2025; ERP plan | €99.90 + VAT per file; no success fee | [new: https://redclaimer.es/productos/burofax/, seen 23 Oct 2026] |
| CertiDEMANDA (certidemanda.es) | "Terceros ajenos que certifican el proceso": drafting, up to two communications (burofax/buromail), certificate, reminders, mediation option | Not published; "no cobramos por cada envío" | Launched 21 Apr 2025 [new: https://www.certidemanda.es/, seen 23 Oct 2026; press release https://www.moncloa.com/2025/04/23/nace-certidemanda-la-1a-plataforma-para-acreditar-y-certificar-masc-previos-a-la-demanda-judicial-3223627/] |
| Unnamed platform using eIDAS certified delivery | Invitation in about five minutes, certificate after rejection or 30 days | €110 + VAT per file (€150 with several parties); mediation €100–120 + VAT per session | Single source [new: Moncloa.com, 6 Oct 2026] |
| Legal Pigeon | Online mediation with a certificate "en menos de 30 días" | Not published | [new: https://www.legalpigeon.com/masc-mediacion-conciliacion-masc-ley-2025/, seen 23 Oct 2026] |
| eGarante | Certified email (a sending layer, not a MASC product) | Packs of 5 for €14.90, 20 for €24.90, 150 for €89.90, 500 for €199.90 (VAT included), so €0.40–2.98 per send | QTSP status not stated [new: https://www.egarante.com/precios/, seen 23 Oct 2026] |
| Correos burofax | Physical certified letter | About €13.14 incl. VAT for one page in 2023, with certified copy and acknowledgment extra | Secondary, dated source; 2026 tariff not verified (search 6) |
| Agencies | Debitura 6–7.5%, Absolut from 5%, Recobrarte €1,500 minimum, Intercobros success fee | — | [notes: FIN-08] |
| Copilot Gestoría | AR automation for gestorías: reminders, interest, €40, claim letter | €15 or €150–450/month (the page contradicts itself) | Vendor claim [new: https://copilotgestoria.com/blog/gestion-impagos-morosidad-gestorias-2025-automatizar-cobros, 17 Dec 2025, updated 22 Oct 2026] |

- **The gap.** Nobody publishes a self-serve, sub-€40, per-claim MASC-plus-monitorio flow for small B2B claims. The building blocks, however, cost €0.40–3 (certified email), and the incumbents are one pricing decision away from it.
- **Court-criteria datasets.** Law-firm blogs and bar associations already publish judges' agreements (Martínez Bernabéu [notes: LEG-01]; ICASAL), so a criteria dataset is not proprietary.

**(c) Buyers and market size**
- **Monitorios.** 179,846 were filed in Q2 2026 (−20.7%), a run rate of about 720k a year, all creditor types included [new: LegalToday/CGPJ, 16 Oct 2026]. The share filed by SMEs and the share under €2,000 are not published (gap).
- **Evictions.** 25,540 in 2025 (C-15 resolved in favour of 25,540) [notes: CON-20]. 2,244 LAU evictions in Q2 2026 [new: LegalToday/CGPJ].
- **Communities.** About 16,000 administradores and 1M communities [notes: CON-24].
- **Rough ceiling (my arithmetic, not a forecast).** 60k SME creditors × 2 claims × €25 = €3M a year. 3,000 administradores × €40/month = €1.4M a year. This is a niche of €2–5M ARR, not a large market.

**(d) Willingness to pay.** Creditors who act already pay €99.90–150 + VAT per file (RedClaimer, the unnamed platform), 5–25% to agencies, or €110 for a first legal consultation [notes: FIN-06, FIN-08]. Abroad, AR automation with interest and late fees sells at €59/month (Paidnice Essentials) [new: https://www.paidnice.com/pricing, seen 23 Oct 2026]. €19–29 per claim sits well under the paid alternatives. The doubt is whether the 89% who never claim will start (FIN-03).

**(e) Distribution**
- Administradores are concentrated (about 16,000) and have a colegio channel: CAF Madrid has published MASC guidance [notes: PRO-12].
- Gestorías: Copilot Gestoría's positioning shows they are already being sold AR automation.
- Invoicing APIs exist for an overdue-invoice "start MASC" button without needing a partnership: TS Facturas lists "Integración con API" on every plan, and Holded allows 70–1,000 API calls a day by plan [new: https://www.billin.net/precios/ and https://www.holded.com/es/precios, seen 23 Oct 2026].
- High-intent search exists ("MASC monitorio", "burofax MASC"), but its volume is unmeasured.

**(f) Build feasibility and legal constraints**
- **MVP in 4–6 weeks:** two templates reviewed by a litigation lawyer (negotiation request; binding offer ≤€2,000), one certified-email/SMS API, the clock, a PDF pack and monitorio pre-fill.
- **Legal constraints:**
  - Art. 6.2 forbids a lawyer-free binding offer above €2,000.
  - The tool must remain a document tool for the party's own claim, with no advice on the merits (reserved profession; [notes: PRO-12]).
  - Debtor data can be processed on legitimate interest; a data-processing agreement with the delivery provider is needed (inference).
- **No certification is needed** unless the product itself wants to be a QTSP.

**(g) Defensibility.** Low to moderate:
- Templates and the clock are copyable in days.
- Certified sending is a commodity.
- The criteria dataset is public and converging.
- The only lasting edges are channel placement (administradores' software, gestoría bundles, invoicing-tool buttons) and outcome data at volume.
- RedClaimer, CertiDEMANDA or eGarante could ship a €29 lane quickly.

**(h) Kill criteria**
| Criterion | Status | Evidence |
|---|---|---|
| Fewer than 1 in 4 creditors would pay €20 or more per claim | Open [I] | Paid alternatives cost €99.90–150 |
| A valid certified send costs more than about €15 | Not met for electronic channels (€0.40–2.98 per certified email). Unverified for a full burofax | eGarante; Madrid criteria accept certified email/SMS |
| More than 10% of pilot files inadmitted | Open [I]. The desk proxy is favourable | Appellate trend |
| A free official channel with court-accepted certificates announced for 2027 | Not met. PIMASC is a register for neutrals, not a delivery channel. Watch item | Ministerio de Justicia page |
| MASC made voluntary after 29-N | Open; no evidence either way | Search 3 |

**Scores (reshaped version)**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 4 | An enforced duty, triggered by each claim (a frequent, costly event), with no calendar deadline. |
| S2 Buyers | 3 | Paying entities are likely 20k–100k: about 720k monitorios a year across all creditors, SME share unknown, plus about 16,000 administradores. |
| S3 Willingness to pay | 4 | Clear adjacent spend at €99.90–150 per file and 5–25% fees. Most small creditors write off instead. |
| S4 Reachability | 3 | Administradores, gestorías and invoicing APIs exist as channels; none is proven. |
| S5 Competitive gap | 3 | Tools exist but are priced for larger claims or are not self-serve (RedClaimer, CertiDEMANDA, the €110 platform). |
| S6 Build speed | 4 | MVP in about 4–6 weeks; no certification; needs lawyer-reviewed templates. |
| S7 Defensibility | 2 | Copyable; the criteria are public and converging; only channel placement defends it. |
| S8 Retention | 2 | Occasional per-claim use for SMEs; periodic only for administradores and gestorías. |
| **Sellability** | **3.13** | Mean of S1–S8. |
| P | 4 | Unpaid invoices are widespread and costly (3.3% of sales unpaid [notes: FIN-01]). The MASC step adds 30–90 days and inadmission risk. |
| **Overall** | **3.48** | 0.6 × 3.125 + 0.4 × 4 = 3.475 |

**Open [I] checks**
- Interview 15–20 B2B creditors: typical claim size, the threshold below which they write off, and willingness to pay €20+ per claim.
- Pilot 30 files across Madrid, Barcelona, Valencia and Sevilla and measure inadmissions.
- Ask five administradores and two administrador-software vendors (Gesfincas, Fynkus) whether they would embed a community-monitorio module.
- Measure search volume for "MASC monitorio" and "burofax MASC".

**What would change the verdict**
- **Up to GO:** the pilot shows creditors pay €20+ and fewer than 5% of files are inadmitted, and an administrador-software vendor agrees to embed the module.
- **Down to KILL:** PIMASC (or a regional service) starts issuing free certified-delivery proofs for direct negotiation; a post-election reform makes MASC voluntary; or RedClaimer or CertiDEMANDA launch a sub-€30 self-serve lane.

---

#### IDEA-02: Receivables autopilot (reminders, statutory interest, payment-date forecasts) — KILL (medium)

**Validated definition.** A €5–9/month subscription for B2B autónomos and micro firms. It reads issued invoices and the bank feed, sends escalating reminders, computes statutory interest (10.40% in H2 2026) and the €40 per invoice, forecasts each customer's payment date, and escalates to the MASC kit. **Verdict: KILL as a standalone product.** Keep the interest-and-€40 engine and the reminder sequence as a free feature and lead magnet of IDEA-01.

**(a) Problem reality and rule status**
- **The pain is real and has no deadline:**
  - 41.51% of invoices were paid on time in Q3 2026 [notes: FIN-05].
  - 89% of suppliers never claim interest and 94% never claim the €40 [notes: FIN-03].
  - In one survey, 84% of Spanish firms take no recovery action at the due date and only 5% apply late interest [new: search-result summary of Emprendedores, https://emprendedores.es/gestion/finanzas-y-legal/facturas-recobro/, undated; single source].
- **The law is in force and verified:**
  - Interest accrues automatically "sin necesidad de aviso de vencimiento ni intimación" (art. 5).
  - The rate is the ECB rate plus eight points (art. 7.2).
  - The €40 "se añadirá en todo caso y sin necesidad de petición expresa" (art. 8.1).
  - Source: [new: BOE consolidated Ley 3/2004, https://www.boe.es/eli/es/l/2004/12/29/3/con, last update 01/10/2014, seen 23 Oct 2026].
- **The H2 2026 rate of 10.40% is confirmed:** the ECB rate of 2.40% plus 8 points [new: BOE-A-2026-14327, Resolución de 30 de junio de 2026, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-14327, BOE 1 Jul 2026]. This settles the single-source flag in section 5.2.
- **No sanctions regime is pending and nothing lapses** [notes: FIN-01].
- **A future tailwind and a future threat.** From 6 Oct 2027 (firms above €8M) and 6 Oct 2028 (legal entities at or below €8M), recipients must report full payment and its date to the SPFE (RD 238/2026 art. 12). The AEAT will pass the data to the Observatorio Estatal de la Morosidad Privada to list firms that breach Ley 3/2004 (art. 14.2). Issuers may also report collections or non-payment voluntarily (art. 12.4) [new: BOE consolidated RD 238/2026, https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295, seen 23 Oct 2026]. These statuses will arrive inside e-invoicing platforms natively, which erodes the forecasting value of a stand-alone tool.

**(b) Competitors**
| Product | Reminders | Interest / €40 | Price | Source |
|---|---|---|---|---|
| TS Facturas (TeamSystem) | "Recordatorio de pagos automático" on every plan, from Básico | Not offered | Básico €6.60/month annual (€8 monthly), capped at 0–5 clients; Pro €14/€17; Ilimitado €23/€28 | [new: https://www.billin.net/precios/, seen 23 Oct 2026] |
| Holded (Visma) | "Recordatorios de pago" only from Avanzado | Not offered | Avanzado €49.50/month annual, €99 monthly | [new: https://www.holded.com/es/precios, seen 23 Oct 2026] |
| Cuéntica | "Revisa cobros pendientes, envía recordatorios" (Facturación plan) | Not offered | €9 + VAT | [new: https://cuentica.com/precios/, seen 23 Oct 2026] |
| Qonto | "Facturación automática" module: "cobra, recupera impagos" | Not stated | €12/month (€144/year); forecasting on Smart €19 | [new: https://qonto.com/es/pricing, seen 23 Oct 2026] |
| Agicap | AR module: "previsiones precisas basadas en el comportamiento real de tus clientes" | Not stated | Mid-market, on quote | [new: https://agicap.com/es/, seen 23 Oct 2026] |
| Banktrack | Forecasting | Not offered | €59 / €119 per month | [new: https://banktrack.com/precios, seen 23 Oct 2026] |
| Copilot Gestoría | Reminders by email, SMS and WhatsApp | Interest and €40, as claimed | €15 or €150–450/month (the page contradicts itself); quotes a stale 10.15% rate | [new: https://copilotgestoria.com/blog/gestion-impagos-morosidad-gestorias-2025-automatizar-cobros, 17 Dec 2025, updated 22 Oct 2026] |
| Paidnice (abroad) | Email and SMS reminders | "Late fees and interest charges" | From €59/month; Xero, QuickBooks and Stripe only | [new: https://www.paidnice.com/pricing, seen 23 Oct 2026] |

Quipu, Anfix, Contasimple and FacturaDirecta mention no reminders on their pricing pages (seen 23 Oct 2026). That is absence of evidence only. **The gap is narrow:** an automatic statutory-interest-and-€40 calculation at the micro tier, which incumbents can add in a sprint.

**(c) Buyers and market size.** 3,310,824 companies are in DIRCE 2025, of which 1,859,925 are personas físicas [new: INE DIRCE table 73019, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73019, reference 2025, seen 23 Oct 2026]. The share that invoices B2B on credit is unknown. The theoretical ceiling (100k payers × €84/year = €8.4M ARR) assumes adoption that the behavioural data contradict.

**(d) Willingness to pay.** Weak for a stand-alone tool. Reminders already come inside €6.60–12 tools, 89% never claim interest [notes: FIN-03], and a separate €5–9 bill would rival the price of the whole invoicing tool. Paid AR tools that work (Paidnice €59, Banktrack €59) sell to larger firms.

**(e) Distribution.** Invoicing APIs exist (TS Facturas API on all plans; Holded API limits by plan [new: vendor pricing pages]), so a marketplace listing needs no partnership. Distribution through invoicing vendors makes them the obvious copier, though. Gestorías are being sold the same thing (Copilot Gestoría).

**(f) Build feasibility.**
- MVP in 4–6 weeks with CSV import and one invoicing API.
- Bank feeds need a licensed AIS provider. I did not verify current Spanish AIS prices this session (open).
- WhatsApp service replies are free up to 1,000 per number a month, and are charged beyond that from 1 Oct 2026; templates are charged per message [new: https://developers.facebook.com/docs/whatsapp/pricing/, seen 23 Oct 2026].
- Pooling payer scores across customers would be a credit-information file under GDPR and LOPDGDD art. 20 (legal inference, not checked with counsel). Keep scores per customer.

**(g) Defensibility.** None. Every invoicing vendor holds the invoices and the bank reconciliation already, and the 2027–2029 e-invoice statuses will be native to their platforms.

**(h) Kill criteria**
- "Entry tiers already ship reminders plus statutory interest." **Half met:** reminders yes (TS Facturas Básico, Cuéntica), interest no.
- "Fewer than half of trial users keep reminders on after 60 days." **Open [I].**
- **Additional reason to kill:** the e-invoice payment statuses from 2027–2028 commoditise the "is it paid?" signal.

**Scores (stand-alone version)**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 3 | Strong recurring pain; no deadline or penalty. |
| S2 Buyers | 4 | Probably 100k–500k B2B credit sellers among 3.3M firms; the share is unknown. |
| S3 Willingness to pay | 2 | Reminders are bundled into €6.60–12 tools; the interest features go unused. |
| S4 Reachability | 3 | Marketplaces and gestorías exist; unproven. |
| S5 Competitive gap | 2 | Several decent reminder tools; the gap is only interest and €40. |
| S6 Build speed | 4 | 1–2 months. |
| S7 Defensibility | 1 | Trivially copyable by the vendors that own the data. |
| S8 Retention | 3 | Periodic use. |
| **Sellability** | **2.75** | |
| P | 4 | Late payment is widespread and costly (€1,957M financial burden in 2025 [notes: FIN-01]). |
| **Overall** | **3.25** | |

**Open [I] checks.** A 60-day reminder-retention test with 30 B2B autónomos. Framing test: "interest waived if paid by date X". Current AIS provider prices.

**What would change the verdict.** A large invoicing vendor or neobank offering to white-label the interest-and-€40 engine as a paid add-on, which is distribution without competition. Or evidence that more than 30% of trial users send interest notices.

---

#### IDEA-03: E-invoice inbox and payment-status reporter for small firms — RESHAPE (medium)

**Validated definition (after reshape).** A bulk status-reporting service for gestorías and asesorías, acting as apoderado or colaborador social of their clients. Each gestoría already receives its clients' bank statements, so the service:
- retrieves each client's received e-invoices from the SPFE by web service;
- matches them to bank movements;
- files the mandatory statuses (rejection, full payment date, due date) within four working days;
- flags invoices due for rejection.

It is sold at €1–3 per client per month and goes live for the 6 Oct 2028 wave (legal entities at or below €8M), with personas físicas following on 6 Oct 2029. The direct-to-SME inbox is dropped as a primary product because the free SPFE covers receiving and manual reporting, and incumbents with bank reconciliation will bundle automation.

**(a) Rule status (C-05 settled)**
- **Instruments:**
  - RD 238/2026 of 25 March: BOE 31 Mar 2026, BOE-A-2026-7295, in force 20 Apr 2026.
  - Orden HAC/1028/2026: BOE 5 Oct 2026, BOE-A-2026-20587, in force 6 Oct 2026.
  - Both are regulations, so they do not lapse with the dissolution [new: BOE summaries of 31 Mar and 5 Oct 2026 via the BOE open-data API, seen 23 Oct 2026].
- **Dates:**
  - 6 Oct 2027: firms above €8M issue, receive and report statuses.
  - 6 Oct 2028: everyone else issues and receives; legal entities at or below €8M also report statuses.
  - 6 Oct 2029: personas físicas and entidades en atribución de rentas report statuses.
  - Sources: [new: AEAT, https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/octubre/7/solucion-publica-facturacion-electronica.html, 7 Oct 2026, page updated 13 Oct 2026]. RD 238/2026 transitional provision 3 gives personas físicas at or below €8M the extra 12 months for arts. 10 and 12 [new: BOE RD 238/2026].
  - The AEAT version in the notes was right. The law-firm claim that reporting stays "voluntary for all below €8M until 2029" is wrong for legal entities. The Consejo General de Gestores draft dates (SPFE online 1 Aug 2027; small-firm status reporting from 1 Oct 2029) were superseded. The final order only requires the SPFE to be live at least two months before 6 Oct 2027 (additional provision 2) [new: BOE Orden HAC/1028/2026].
- **Statuses:**
  - Mandatory: commercial acceptance or rejection with its date, and full effective payment with its date (art. 10.1); plus the due date sent to the SPFE (art. 12.3).
  - Optional: partial acceptance, partial payment, assignment (art. 10.2).
  - Invoices count as accepted unless rejected (art. 12.1) [new: BOE RD 238/2026].
- **Deadline:** "un plazo máximo de cuatro días naturales, excluyendo sábados, domingos y festivos nacionales" (arts. 10.3 and 12.3), which in effect means four working days. This confirms the single-source "4 calendar days" with an important nuance.
- **Sanctions:**
  - RD 238/2026 contains no sanction article.
  - Ley 56/2007 art. 2 bis.9 provides a warning or a fine of up to €10,000, worded for firms that "no ofrezcan a los usuarios la posibilidad de recibir facturas electrónicas o no permitan el acceso" to invoices. The competent authority is the Secretaría de Estado de Digitalización [new: BOE consolidated Ley 56/2007, https://www.boe.es/buscar/act.php?id=BOE-A-2007-22440, seen 23 Oct 2026].
  - I found no explicit sanction for failing to report statuses, so enforcement of the small-firm reporting duty is unclear. B2Brouter still markets "sanciones de hasta 10.000 euros" [new: https://www.b2brouter.net/es/plazos-obligatoriedad-factura-electronica-b2b/, edited 18 Jun 2026].
- **Third-party access (kill check):**
  - The SPFE offers both "servicio web" (machine to machine) and "formulario" for issuing, interconnection, true copies, recovering received invoices, consultation, and "comunicación de estados y de pagos" (Orden arts. 5 and 9–11).
  - It can be used by "un tercero que actúe en su representación" under RGAT arts. 79–81 and colaboración social (Orden HAC/1398/2003).
  - Third parties using the forms, or retrieving and consulting invoices automatically, must be registered apoderados in the AEAT Registro de apoderamientos (art. 11.2) [new: BOE Orden HAC/1028/2026].
  - **The "no programmatic access" kill criterion is not met.**
  - The technical specifications ("especificaciones, condiciones técnicas y volumetría") are left to the AEAT Sede. The SPFE page (updated 14 Oct 2026) shows only general information, the calendar and the rules, with no technical section yet [new: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica.html, seen 23 Oct 2026].
- **Must the tool register as a private platform?**
  - Only if it wants to exchange invoices with other platforms. A platform "que forme parte del sistema" needs ISO/IEC 27001, AS2/AS4, advanced signature and seal, all four syntaxes with conversion, a continuity plan, "recursos de soporte disponibles en todo momento", data governance (UNE 0080 level 2) and free interconnection (RD 238/2026 art. 13) [new: BOE RD 238/2026]. That bar is too high for a 1–3 person team.
  - A recipient that has not agreed a private platform with its suppliers "se entenderá que optan por la solución pública" (art. 6), and may "recuperar en cualquier momento sus facturas recibidas, directamente o a través de un acceso automatizado" (Orden art. 9.3). So a non-platform tool can work through the SPFE as the client's representative.

**(b) Competitors**
- **Free SPFE:** receiving, consultation and status/payment forms at no charge, but no bank matching [new: BOE Orden HAC/1028/2026].
- **Peppol access points in Spain include** Atecna, B2Brouter, Consorci AOC, Docuten, easyap, EDICOM, GuruSoft, Indra, Invopop, Marosa VAT and NEXMART (visible part of the list) [new: https://peppol.org/members/peppol-certified-service-providers/, seen 23 Oct 2026].
- **B2Brouter:** Basic €0 (10 contacts, 24 transactions a year), Professional €110/year, Business €300/year + VAT [new: https://www.b2brouter.net/es/precios/, seen 23 Oct 2026].
- **Every SME accounting suite already reconciles bank feeds:** Holded, Qonto, TS Facturas "Conciliación bancaria", Anfix "Estado de las facturas" [new: vendor pricing pages, seen 23 Oct 2026]. Adding "report payment to SPFE" is a natural extension.
- **Public roadmaps.** TS Facturas' calendar post (13 May 2026) mentions the four-day duty without saying its product will automate it [new: https://www.billin.net/blog/calendario-final-factura-electronica-b2b/]. My search (search 7) found no vendor marketing automated status reporting yet.
- **Banks and neobanks** (Qonto Starter is free and already includes e-invoicing [new: Qonto pricing]) hold the payment date and are the most dangerous entrants.

**(c) Buyers and market size**
- From 6 Oct 2028 the duty covers about 1.45M legal entities: SL 1,127,515, SA 46,763, plus other forms. Personas físicas (1,859,925) follow in 2029 [new: INE DIRCE 2025, table 73019].
- Gestorías: CNAE 692 (accounting, bookkeeping, audit and tax advice) has 62,234 companies, 30,394 of them with employees. Batch 2 owns the gestoría count.
- Firms above €8M: no count found (search 8; gap).
- Ceiling (illustrative): 5,000 gestorías × 80 clients × €2 = €9.6M ARR. More realistically 500–1,500 gestorías in the first years.

**(d) Willingness to pay.** No compliance-cost estimate exists [notes: TAX-05, TAX-06]. Gestorías pay for automation (Kabilio [notes: TAX-23]; Copilot Gestoría lists €150–450/month). The price ceiling is set by the free SPFE form and by bundling in tools at €0–€12. **Unproven.**

**(e) Distribution.** Gestorías already act as colaboradores sociales and apoderados for filings. The Orden explicitly allows representation, which is the channel. A second route is white-labelling to invoicing vendors and banks that lack an AP module.

**(f) Build feasibility**
- Integration-heavy: UBL, Facturae, CII and EDIFACT parsing, SPFE web services (specs pending), apoderamiento onboarding, Norma 43/CSV or AIS bank data, and matching.
- MVP in about three months once the specs are out, but real testing waits for the SPFE (by about Aug 2027).
- The data are sensitive (every supplier invoice), so ISO 27001 will be a sales requirement even if it is not a legal one.

**(g) Defensibility.** Low to medium. Matching accuracy and gestoría relationships help. a3, Sage, TeamSystem, Holded and the banks can each add the feature, and the SPFE form is free.

**(h) Kill criteria**
| Criterion | Status |
|---|---|
| The SPFE app covers receiving, reporting and bank matching for free | Not met: no bank matching; receiving and manual reporting are free |
| No programmatic access | Not met: web services plus representation |
| The small-firm duty slips or stays voluntary until 2029 | Not met for legal entities (2028); met for personas físicas (2029) |
| Registration as a private platform required | Avoidable by working through the SPFE as representative |

**Scores (reshaped gestoría version)**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced duty for legal entities 23–24 months out (6 Oct 2028). |
| S2 Buyers | 3 | 20k–100k paying gestorías and asesorías (62,234 firms in CNAE 692). |
| S3 Willingness to pay | 3 | Gestorías buy automation; no data on this task. |
| S4 Reachability | 3 | Gestoría channel and representation rules exist; unproven. |
| S5 Competitive gap | 3 | No product yet, but the free SPFE and suite vendors will close it. |
| S6 Build speed | 3 | Integration-heavy, and the specs are not yet published. |
| S7 Defensibility | 2 | Incumbents and banks hold the data. |
| S8 Retention | 5 | Recurring per-invoice legal duty plus accumulated records. |
| **Sellability** | **3.25** | |
| P | 3 | A new recurring administrative task with an unclear sanction regime. |
| **Overall** | **3.15** | |

**Open [I] checks**
- Ten gestorías: how many clients will not have an AP-capable tool in 2028, and would they pay €1–3 per client per month?
- Whether the AEAT web-service specs allow bulk payment reporting by one apoderado for many NIFs.
- Whether a3, Sage Despachos and TeamSystem announce the feature.

**What would change the verdict**
- **Up to GO:** the AEAT publishes bulk web services for colaboradores sociales, and gestorías confirm that more than 30% of clients lack capable software.
- **Down to KILL:** a bank or a suite vendor ships free automated payment reporting, or a non-reporting sanction is never defined and gestorías tell clients to ignore it.

---

#### IDEA-04: VeriFactu retrofit adapter for legacy tills and scales — KILL (medium)

**Validated definition.** A capture device or driver that turns tickets from legacy tills and scales into VeriFactu records (hash chain, event log, QR printed on the existing printer) and submits them to the AEAT. It is sold through installers at €150–300 one-off plus €5–8/month. **Verdict: KILL.**

**(a) Problem reality and rule status (C-08 settled; this batch owns the check)**
- **The October 2028 move is not in the BOE:**
  - None of the BOE daily summaries of 1–23 October 2026 contains an instrument amending RD 1007/2023. I checked every Section I item, plus the full texts of RDL 28, 29, 30 and 31/2026 for "1007/2023" and "facturación" [new: BOE open-data API, https://www.boe.es/datosabiertos/api/boe/sumario/AAAAMMDD, seen 23 Oct 2026].
  - The consolidated RD 1007/2023 (last update 03/12/2025) still says IS taxpayers must adapt "antes del 1 de enero de 2027" and the rest "antes del 1 de julio de 2027" [new: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840, seen 23 Oct 2026].
  - The AEAT FAQ (updated 21 Oct 2026) still gives 1 Jan and 1 Jul 2027 [new: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html].
  - The Hacienda note of 5 Oct 2026 is a "Previsión de modificación". It sets a single date, "hasta octubre de 2028", for all pending obligations, aligned with e-invoicing for firms at or below €8M [new: https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf]. It contains no October 2027 date for firms above €8M, so Infoautónomos' split is not supported by the primary source.
- **The instrument.** RDL 15/2025's final provision 2, "Salvaguarda del rango", states that its amendment "no altera el rango reglamentario del Real Decreto 1007/2023" [new: BOE-A-2025-24446, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-24446]. A plain Real Decreto can therefore move the dates, with no convalidation needed. If the Government uses a decree-law again for speed, the Diputación Permanente must convalidate it within 30 days, and three decree-laws failed in 2026. The Government is not yet "en funciones" before the 29 Nov vote. ATA's line that it is "pendiente de un real decreto ley" [notes: TAX-02] describes the Government's likely choice, not a legal necessity.
- **Scope is narrower than the idea assumes** (AEAT FAQ, updated 21 Oct 2026):
  - A scale used only to weigh, with the amount keyed into the till, "no se consideraría SIF, sino un elemento -independiente- auxiliar de medida". Only scales that accumulate and issue the simplified invoice are SIFs.
  - Businesses under recargo de equivalencia, or under the régimen simplificado de IVA, are "No con carácter general" affected, because they are not obliged to invoice consumers [new: AEAT FAQ sub-pages, seen 23 Oct 2026]. This matches ROF art. 3.1.b–c.
  - ROF art. 26.1 brings back anyone on IRPF estimación directa: they must invoice "con independencia del régimen a que estén acogidos a efectos del Impuesto sobre el Valor Añadido" [new: BOE consolidated RD 1619/2012, https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696, last update 31/03/2026, seen 23 Oct 2026].
  - So the in-scope legacy base is shops and bars on estimación directa (or invoicing voluntarily) whose till or scale-till itself issues the ticket and cannot be updated.
- **ATA's €1,800–2,500 figures are single-source** [notes: TAX-01], and the FAQ's scale carve-out suggests they apply to integrated scale-tills only.

**(b) Competitors and alternatives**
- **Replacement is cheap for basic tills:** basic electronic cash registers under €200, touch registers about €600, a complete TPV for €259 (commercial source) [new: https://asest.es/story/cuanto-vale-una-caja-registradora-para-negocio/, 20 May 2026]. Olivetti list prices of €320–390 appear in an undated catalogue [new: search-result summary, search 10].
- **Software layers serve POS makers, not legacy hardware:** fiskaly's SIGN ES is "an API to comply with Verifactu and TicketBAI" for invoicing, ERP and POS vendors, with no mention of legacy hardware [new: https://www.fiskaly.com/blog/verifactu-ticketbai-fiscal-regulation-differences, 30 Dec 2024]. EPOS Now and LS Central publish Spanish fiscalisation modules (search 9).
- **Producers have been obliged since 29 Jul 2025** [notes: TAX-01], so every maintained POS software already has an update path.
- **No TicketBAI-era retrofit device turned up** (search 9), which is weak evidence that the Basque market solved this by replacement plus 30–60% deductions [notes: TAX-08 context].

**(c) Buyers and market size.** DIRCE 2025 [new: INE table 73019]:
| CNAE | Activity | Companies | Of which no employees |
|---|---|---|---|
| 472 | Food retail in specialised shops | 80,030 | 29,930 |
| 471 | Non-specialised retail | 35,696 | — |
| 561 | Restaurants | 73,296 | — |
| 563 | Bars | 146,853 | — |

The in-scope legacy share (estimación directa, ticket-issuing device, not upgradable) is unknown. It is likely a minority after the scale and regime carve-outs, perhaps 10–20%, which is an assumption.

**(d) Willingness to pay.** For basic tills the €150–300 device plus €5–8/month is at or above the cost of a new compliant TPV (€200–600). Only integrated scale-tills (ATA's €2,500 case) leave headroom, and their manufacturers can sell firmware upgrades themselves.

**(e) Distribution.** Installers are the only channel [I], and they earn more selling replacement hardware.

**(f) Build feasibility and legal constraints**
- The maker becomes a SIF producer: a declaración responsable under Orden HAC/1177/2024, and sanctions of up to €150,000 per year and system type [notes: TAX-01].
- The record must be generated at the moment of issue, and the QR must be printed on the ticket. A box on the printer line has to stop the legacy till from printing anything outside the chain.
- I found no DGT ruling or AEAT FAQ that accepts or rejects external capture. The FAQ defines a SIF as "el conjunto de hardware y software" [new: AEAT FAQ], which neither forbids nor blesses it.
- Per-model drivers and hardware logistics put the MVP at 4–6 months or more.

**(g) Defensibility.** Moderate if it works (hardware, installer network), but the window closes after the deadline and a replaced till never comes back.

**(h) Kill criteria**
| Criterion | Status |
|---|---|
| DGT or AEAT criteria rule out external capture | Open: no ruling found |
| Vendor upgrade or replacement cost below about €300 | Effectively met for basic tills (replacement €200–600). Open for integrated scale-tills (no quotes found) |
| The 2028 move removes urgency | Likely: announced; enactable by plain RD |
| Additional | The scope carve-outs (weighing-only scales; recargo de equivalencia or módulos without estimación directa) shrink the base |

**Scores (as proposed)**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 4 | The BOE deadline is 1 Jul 2027 (within 12 months, which would be a 5), but the announced October 2028 move is likely. |
| S2 Buyers | 3 | An in-scope legacy subset of about 336k food-retail and hospitality firms; likely 20k–100k. |
| S3 Willingness to pay | 2 | Replacement at €200–600 caps the price for basic tills. |
| S4 Reachability | 3 | An installer channel exists but is conflicted. |
| S5 Competitive gap | 3 | No retrofit product found; cheap replacement and POS fiscalisation APIs cover most cases. |
| S6 Build speed | 2 | Hardware, producer declaration and per-model drivers: 4–6 months or more. |
| S7 Defensibility | 3 | Hardware and installers, if legal. |
| S8 Retention | 3 | A monthly service, but devices are replaced at the next hardware cycle. |
| **Sellability** | **2.88** | |
| P | 3 | A one-off adaptation cost for a subset; the €50,000 fine is theoretical. |
| **Overall** | **2.93** | |

**Open [I] checks.** Quotes from Dibal, Epelsa and Bizerba distributors for adapting integrated scale-tills. Ask the DGT (consulta vinculante) whether an add-on capture box makes a legacy till a compliant SIF. Installer interviews.

**What would change the verdict.** A DGT ruling that explicitly accepts external capture, combined with manufacturer upgrade quotes for scale-tills above €1,000, and an installer network willing to resell. That would revive it as a niche hardware business, not SaaS.

---

#### IDEA-05: Fair-terms invoicing and e-invoicing for micro businesses — KILL (high)

**Validated definition.** A flat €6/month invoicing tool with VeriFactu, Facturae and UBL e-invoicing, unlimited invoices, one-click cancellation, a free six-year read-only archive after leaving, an Excel/Word importer, a free gestor seat with exports, and human WhatsApp support. **Verdict: KILL.**

**(a) Problem reality.** Complaints about caps, price creep, obstructed cancellation and locked data are real across at least six vendors [notes: VOX-08 to VOX-11]. The switching windows depend on VeriFactu (BOE: 2027; announced: October 2028; see IDEA-04) and on e-invoicing (6 Oct 2027 and 2028; see IDEA-03).
- **Retention rules:** 4 years for tax and 6 under the Código de Comercio [notes: TAX-05].
- **SPFE copies:** the SPFE acts as the invoice repository (RD 238/2026 art. 5.1), and recipients can retrieve their invoices at any time (Orden art. 9.3). I found no provision saying the SPFE copy discharges the taxpayer's own retention duty (open).

**(b) Competitors and price list (C-10 settled where fetched)**
| Product | Plans and prices (excl. VAT) | Source |
|---|---|---|
| Holded | Plus €7.50/month annual or €15 monthly (250 invoices a year); Básico €14.50/€29; Estándar €29.50/€59; Avanzado €49.50/€99; Premium €99.50/€199 | [new: https://www.holded.com/es/precios, seen 23 Oct 2026]. Settles the three sources: monthly is exactly double annual; GuiaDeSoftware's "€14.50–75" is outdated. |
| TS Facturas (ex-Billin) | Básico €6.60 annual / €8 monthly (0–5 clients, 10 products); Pro €14/€17 (6–50 clients); Ilimitado €23/€28. VeriFactu, Facturae and TicketBAI unlimited on all plans | [new: https://www.billin.net/precios/, seen 23 Oct 2026]. The current list replaces both conflicting lists. |
| Anfix | Básico €4.99 annual / €5.99 monthly (60 invoices a year); Avanzado €12.49/€14.99; Profesional €24.99/€29.99; Empresarial €58.33/€69.99; Premium €83.33/€99.99. "Todos los planes incluyen Veri*Factu" | [new: https://www.anfix.com/precios, seen 23 Oct 2026]. Both conflicting figures are correct: "from €15" is the Avanzado monthly price. |
| Contasimple | Básico free (12 documents a year); Profesional €10.95 annual / €12.95 quarterly (500 documents); Ultimate €15.95. Branded "Contasimple by Shine", and the page describes Shine with Cegid's corporate wording | [new: https://www.contasimple.com/precios, seen 23 Oct 2026]. Ownership: consistent with Shine being a Cegid brand; not confirmed from a corporate filing. |
| Cuéntica | Facturación €9; "Sin permanencia... Puedes darte de baja en cualquier momento"; on leaving "los guardamos por ti el tiempo que quieras... y puedes exportarlos en cualquier momento"; gestor access with own credentials; API; phone support Mon–Fri 8–15 h | [new: https://cuentica.com/precios/, seen 23 Oct 2026] |
| Declarando | VeriFactu Plus €9.90/month annual, with a "garantía antisanciones" | [new: https://declarando.es/precios, seen 23 Oct 2026] |
| Qonto | Starter €0 including e-invoicing and VeriFactu | [new: https://qonto.com/es/pricing, seen 23 Oct 2026] |
| B2Brouter | Basic €0 (24 transactions a year) | [new: B2Brouter prices] |
| AEAT free app | Free; "emite facturas completas, no facturas simplificadas"; "No es posible exportar registros para continuar con la facturación en otros sistemas" | [new: AEAT user guide v1.0, 10 Oct 2025, https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/Manual_facturacion/Manual_Usuario_Verifactu_Accesible.pdf] |
| FacturaDirecta | The pricing page could not be fetched (403); the notes give €0–40 | [notes: VOX table] |

Comparison sites in 2026 are written mostly by the vendors themselves (TS Facturas, Holded, TeamSystem) (search 11), which is a sign of a crowded, content-marketing-driven category.

- **The "fair terms" gap is already filled.** Cuéntica's terms match IDEA-05's core promise (no minimum term, data kept and exportable after leaving, gestor access) at €9, with phone support. Contasimple and Anfix undercut the €6 price point.

**(c) Buyers.** 3.48M RETA members [notes: TAX-12]. About half of autónomos use no invoicing software [notes: TAX-03]. The buyers are many, but the switching moment is mediated by gestorías [notes: VOX-21].

**(d) Willingness to pay.** Anchors range from €0 to €9.90/month. At €6, the margin cannot fund human support. Rough estimate: 15–20 minutes of human support per customer per month at about €17–25/hour costs €4–8, which is my assumption. Messaging itself is cheap: WhatsApp service replies are free up to 1,000 a month per number [new: Meta pricing, seen 23 Oct 2026].

**(e) Distribution.** Gestorías decide [notes: VOX-21]. Incumbents already court them: Holded gives "tu asesoría Partner Holded" free access on every plan [new: Holded pricing], Cuéntica gives gestor seats, and Quipu has an asesorías programme [notes: VOX-21].

**(f) Build.** It needs a producer declaración responsable (Orden HAC/1177/2024), VERI*FACTU submission, Facturae and UBL output plus the SPFE copy, and TicketBAI for Basque customers. Building blocks exist: Invopop is a Spanish Peppol access point [new: Peppol list]. The MVP takes 2–3 months, and compliance maintenance never ends.

**(g) Defensibility.** None. Every term is a product decision that Cuéntica has already made.

**(h) Kill criteria**
| Criterion | Status |
|---|---|
| CAC through gestorías above 12 months of revenue | Open [I]. At €72/year, almost any paid acquisition breaks it |
| Fewer than 1 in 5 complainers would switch | Open [I] |
| Saturation | Effectively met: Cuéntica plus €0–5 plans |

**Scores**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 4 | VeriFactu (2027 in the BOE, or October 2028) and e-invoicing (2028) force a tool choice. |
| S2 Buyers | 5 | More than 500k invoicing autónomos and micro firms. |
| S3 Willingness to pay | 3 | They pay €5–10 already, but €0 options abound. |
| S4 Reachability | 3 | Gestorías and search exist, but both are contested. |
| S5 Competitive gap | 1 | Saturated or free; Cuéntica already sells the fair terms. |
| S6 Build speed | 3 | 2–4 months plus producer duties. |
| S7 Defensibility | 1 | None. |
| S8 Retention | 4 | A recurring legal duty and records, but switching is easy by design. |
| **Sellability** | **3.00** | |
| P | 2 | The pain is about terms, and many cheap fair alternatives exist. |
| **Overall** | **2.60** | |

**Open [I] checks.** None worth running, given the competitive evidence.

**What would change the verdict.** Nothing at the product level. A gestoría network wanting a white-label tool it controls would be a different idea (a channel play), and belongs with IDEA-06.

---

#### IDEA-11: Supplier bank-detail change guard (anti-IBAN-fraud payment check) — KILL (medium-high)

**Validated definition.** A €5–9/month tool for micro and small firms. It keeps a register of verified supplier IBANs, watches invoices, emails and SEPA payment files for new or changed IBANs and look-alike senders, and enforces a call-back plus second approval before payment. **Verdict: KILL.** The core check is now a free, mandatory bank service, and the stronger tax-ID check is sold through banks.

**(a) Problem reality and rule status (C-06 settled)**
- **VoP is in force:**
  - Since 9 Oct 2025, payment providers must offer Verification of Payee "gratuitamente" for "transferencias bancarias en euros (ordinarias o inmediatas)".
  - Results: "Coincidente", "Casi coincidente" (showing the registered name), "No coincidente", "No se pudo verificar".
  - If the payer proceeds after a mismatch, the provider "no será considerado responsable".
  - For transfer files, the check "es opcional para el usuario no consumidor".
  - Source: [new: Banco de España, Portal del Cliente Bancario, https://clientebancario.bde.es/pcb/es/blog/nuevo-servicio-gratuito-de-verificacion-del-beneficiario-a-partir-del-9-de-octubre-de-2025-.html, 7 Oct 2025].
  - The legal basis is art. 5 quater of Regulation (EU) 2024/886 [new: LegalToday via search 12, https://www.legaltoday.com/sin-categoria/los-bancos-deberan-comprobar-nombre-e-iban-en-transferencias-para-evitar-fraudes-de-suplantacion-man-in-the-middle-2025-10-09/, 9 Oct 2025]. EUR-Lex blocked automated reads, so the regulation text itself was not read.
  - EU regulation; no election lapse risk.
- **What VoP does to the problem.** The classic fake IBAN change pays into an account whose holder name differs from the supplier's, and it now triggers a free warning at the moment of payment. The residual exposure is:
  - bulk SEPA files where the business has not switched VoP on;
  - mule accounts with look-alike names ("casi coincidente");
  - CEO or "new supplier" fraud, where the name matches because the fraudster owns the account;
  - users who click through.
- **Loss data.** Losses remain poorly measured: BEC above €15,000 per incident (secondary source); 22% of SMEs hit by invoice or payment fraud (vendor survey); INCIBE does not split firms from citizens [notes: FIN-12, VOX-03].
- **The liability shift cuts both ways.** Once a warning has been shown, the SME bears the loss, which raises the value of discipline but not of a separate tool.

**(b) Competitors**
- **Banks' VoP:** free and mandatory (above).
- **Iberpay "Valitic":** checks that an IBAN's holder matches a given NIF, CIF or NIE in real time (OK/KO), against Iberpay's SNCE clearing data. It covers "99% of Spanish bank accounts" (about 88M), with single and bulk API calls. It is sold through Powens (price on request) [new: https://www.powens.com/?p=953, seen 23 Oct 2026], and Bankinter offers it to business clients (search 13 summary of a Bankinter press page that returned 403 when fetched; date not confirmed).
- **Yousign Verify:** bank-account ownership verification across 20 European countries by API (search 13; price not found).
- **BBVA** publicly warns business clients about fake invoices and IBAN changes and recommends a "doble check" (search 13).
- **Spend-management tools** with approvals and per-vendor cards: Qonto, Spendbase (free business banking with per-vendor virtual cards and approvals [new: https://www.spendbase.co/, seen 23 Oct 2026]), Pleo, Payhawk. Prices of the last two were not checked.
- **E-invoicing will carry the payee IBAN.** The UBL mapping in Orden HAC/1028/2026 includes BT-84 "Identificador de la cuenta de pago... Con carácter general, se tratará de un código IBAN" (group BG-17, 0..n) [new: BOE Orden HAC/1028/2026 annex]. From 2027–2028, invoices received through the SPFE or a platform will come from an authenticated issuer with a structured IBAN, which platforms can check natively.

**(c) Buyers and market size.** About 1.45M legal entities plus autónomos with suppliers [new: INE DIRCE 2025]. Frequency of loss per firm is unknown.

**(d) Willingness to pay.** Weak before a loss [notes: FIN-12; VOX-03 rates SME investment as reactive]. The core function is free in every bank. Whether cyber insurers discount for payment controls remains open [I].

**(e) Distribution.** Banks are competitors, not channels. Insurers, MSPs and gestorías are unproven.

**(f) Build.** 1–2 months: an email add-in, the register, a pain.001 file check, and optionally a Valitic call (cost unknown). GDPR applies to supplier contact data.

**(g) Defensibility.** None. Banks and spend tools bundle the feature, and e-invoicing makes the IBAN a structured field.

**(h) Kill criteria**
| Criterion | Status | Evidence |
|---|---|---|
| VoP makes IBAN-change fraud rare | Largely met for single transfers (free warning on name mismatch); not met for bulk files where businesses opt out, or for look-alike or CEO fraud | BdE |
| SMEs will not pay €5/month before a loss | Open [I] | No contrary evidence found |
| Banks bundle the feature | Met (VoP for all; Valitic through Bankinter and Powens) | — |

**Scores**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 2 | Occasional pain; no duty on the SME. |
| S2 Buyers | 4 | Hundreds of thousands of firms pay suppliers by transfer. |
| S3 Willingness to pay | 2 | Weak before a loss; the core check is free. |
| S4 Reachability | 2 | Diffuse buyers; the natural channel (banks) competes. |
| S5 Competitive gap | 2 | VoP, Valitic and spend tools cover most of it; small gaps remain (bulk files, process). |
| S6 Build speed | 4 | 1–2 months. |
| S7 Defensibility | 1 | Trivially copyable. |
| S8 Retention | 3 | Used with each payment run. |
| **Sellability** | **2.50** | |
| P | 3 | Rare per firm but potentially existential (>€15k per incident). |
| **Overall** | **2.70** | |

**Open [I] checks.** Share of SMEs paying by bulk file with VoP switched off. Insurer premium discounts.

**What would change the verdict.** Evidence that most SME supplier payments run through bulk files with VoP disabled, plus a bank or insurer willing to distribute a "VoP-on-files" audit. Even then it is a feature, not a company.

---

#### IDEA-12: B2B subscription and contract guard — KILL (medium)

**Validated definition.** A €3–5/month tool that detects recurring charges from bank, card and email feeds, builds a renewal calendar (notice periods, permanencias), alerts before renewals and price rises, and sends certified cancellation requests. **Verdict: KILL.**

**(a) Problem reality**
- **Complaints are real:** forgotten renewals and obstructed cancellations across at least six vendors [notes: VOX-09].
- **Business telecom lines sit outside consumer protection** (an autónomo qualifies only if the line is not used professionally; companies can only go to court) [notes: VOX-05, citing Infoautónomos].
- **Kit Digital.** The bases fixed domain and hosting "durante un plazo mínimo de doce meses", with "la titularidad del dominio... en su totalidad de la pyme" [new: BOE Orden ETD/1498/2021, https://www.boe.es/buscar/act.php?id=BOE-A-2021-21873, original text, seen 23 Oct 2026]. The last calls closed at the end of October 2025 [new: https://espanadigital.gob.es/lineas-de-actuacion/programa-kit-digital, seen 23 Oct 2026], so the subsidised periods are ending through 2026 (inference).
- **No rule change is pending; no lapse risk.**

**(b) Competitors**
- **Qonto** Premium (€39/month annual) includes "Detección de suscripciones y alertas de renovación... para controlar tus pagos y evitar cargos sorpresa" [new: https://qonto.com/es/pricing, seen 23 Oct 2026]. This is the core feature, bundled by a neobank. The risk "banks add subscription views" has materialised.
- **Spendbase** has pivoted to "Free business banking" with a virtual card per vendor or subscription, budgets and approvals [new: https://www.spendbase.co/, seen 23 Oct 2026].
- **Enterprise SaaS-management tools** (Vendr, Zylo, Torii, Cledara) target larger firms (background; not priced).
- **Certified cancellation letters** can be sent for €0.40–3 by certified email (eGarante, IDEA-01).

**(c) Buyers and market size (kill test)**
- The INE ICT survey gives no micro-firm cloud figure. 79.9% of firms with fewer than 10 employees have internet access (−3.9 points), and 44.3% of firms with 10 or more employees buy paid cloud services [new: INE ETICCE 2024–Q1 2025, https://ine.es/dyngs/Prensa/ETICCE20241T2025.pdf, 22 Oct 2025].
- One micro firm in five offline suggests a thin SaaS stack. Counting telecom, energy, insurance and the gestor, the median contract count is probably at least three, but most of those renew monthly with no decision point (inference).
- The "median under three" test remains open.

**(d) Willingness to pay.** No evidence. Banks and neobanks give the feature away inside account plans, and savings are mostly one-off [notes: VOX-09, VOX-16].

**(e) Distribution.** Neobanks are the natural channel and are already competitors. Gestorías are a possible channel. Search terms ("dar de baja kit digital") have unmeasured volume.

**(f) Build.** 1–2 months: an AIS provider and email parsing.

**(g) Defensibility.** None.

**(h) Kill criteria**
| Criterion | Status |
|---|---|
| Fewer than 40% retained after three months | Open [I]. One-off value suggests failure |
| Median target user has fewer than three contracts | Open. The INE proxy is weak |
| Banks add subscription views | Met (Qonto Premium) |

**Scores**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 2 | Occasional pain. |
| S2 Buyers | 4 | Many potential firms. |
| S3 Willingness to pay | 1 | Buyers expect it free inside bank apps. |
| S4 Reachability | 2 | Diffuse. |
| S5 Competitive gap | 2 | Qonto, Spendbase and spreadsheets. |
| S6 Build speed | 4 | 1–2 months. |
| S7 Defensibility | 1 | None. |
| S8 Retention | 2 | Mostly one-off clean-up. |
| **Sellability** | **2.25** | |
| P | 2 | Minor: hundreds of euros a year. |
| **Overall** | **2.15** | |

**Open [I] checks.** Landing-page test for former Kit Digital beneficiaries (willingness to pay and three-month retention).

**What would change the verdict.** A large bank wanting a white-label contract-and-permanencia module for its SME app, which would be a B2B2B feature sale.

---

#### IDEA-13: Kit Digital website rescue and low-cost managed hosting — KILL (medium)

**Validated definition.** A free audit of what a former Kit Digital beneficiary pays and owns, a guided migration (content export, domain transfer), and managed hosting at €8–10/month with no minimum term. **Verdict: KILL.**

**(a) Problem reality and status**
- **The programme:** more than 860,000 grants; applications closed at the end of October 2025 [new: España Digital, seen 23 Oct 2026].
- **The website solution** (original bases) was €2,000 of aid for every segment, with a minimum 12 months of domain and hosting, and the domain wholly owned by the SME [new: BOE Orden ETD/1498/2021]. Legally the domain is portable. Content portability depends on the builder (open).
- **Post-subsidy fees** of €21.98/month (Arsys, snippet; the page now returns 404) to €66/month (one forum post) [notes: VOX-16]. There are no aggregate renewal or cancellation data. The window is closing.

**(b) Competitors**
- **Commodity hosting:** Hostinger Single at €1.49/month promotional (48 months for €71.52), "Se renueva por 6,99 €/mes"; Premium renews at €9.99/month [new: https://www.hostinger.com/es/hosting-web, seen 23 Oct 2026].
- **Others:** site builders; freelancers who rebuild for €20 plus hosting [notes: VOX-15]; and the agents themselves, who can cut prices to retain customers.
- **Whether hosts already market "Kit Digital migrations"** was not established (search 15 returned only generic maintenance guides). The offer is copyable by any host overnight.

**(c) Buyers and market size.** The number of grants that included a website and the share still paying are unknown (gap; no Red.es data found; the España Digital page gives no category counts).

**(d) Willingness to pay.** Owners pay €22–66/month today (anecdotal), but the switch-to alternative costs €7–10/month at renewal, and many owners will simply cancel. The €8–10 price sits on the commodity floor with service costs on top.

**(e) Distribution.** Diffuse: SEO, forums, gestorías. No partner programme.

**(f) Build.** Low complexity (migration playbooks, a hosting partner, domain transfers). Service-heavy.

**(g) Defensibility.** None.

**(h) Kill criteria**
| Criterion | Status |
|---|---|
| Most Kit sites cannot be exported | Open; domains are owned by the SME by rule |
| Median upkeep below about €15/month | Open; one vendor snippet at €21.98 |
| Window closes | Met over 2026 (inference) |

**Scores**
| Score | Value | Justification |
|---|---|---|
| S1 Urgency | 2 | Occasional; a one-time decision. |
| S2 Buyers | 3 | Unknown share of more than 860k grants; plausibly 20k–100k reachable payers. |
| S3 Willingness to pay | 4 | They already pay more for upkeep, though anecdotally. |
| S4 Reachability | 2 | Diffuse. |
| S5 Competitive gap | 2 | Hosts, builders and freelancers. |
| S6 Build speed | 5 | Under four weeks. |
| S7 Defensibility | 1 | None. |
| S8 Retention | 3 | Hosting recurs, with churn risk. |
| **Sellability** | **2.75** | |
| P | 2 | Minor overpayment (€170–700 a year). |
| **Overall** | **2.45** | |

**Open [I] checks.** Sample 50 Kit Digital sites: which builder, exportability, current fee.

**What would change the verdict.** Red.es data showing more than 300k sites still paying more than €20/month with exportable builders. Even then it is a service business, not low-touch SaaS.
