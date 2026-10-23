# Stage 2, group G2: labour and HR, legal exposure, public administration

Noise filter and candidate SaaS ideas. Prepared 23 October 2026.

**Inputs:** `labor_hr_litigation.md` (LAB-01 to LAB-25), `legal_disputes_compliance.md` (LEG-01 to LEG-22), `bureaucracy_licensing_funds.md` (ADM-01 to ADM-19), plus product prices from the software-market table in `voice_of_smes_software_market.md`. No web searches were made.

**Conventions:**
- Every claim carries the ID of the pain it comes from.
- "Inference" marks arithmetic or reasoning that is not a sourced fact, whether it comes from the notes or from this stage.
- Prices are in € excluding VAT unless stated.
- "Validate" marks a point the next stage must check.
- IDs from other tracks (FIN-, CON-, TAX-, EXP-, HOS- and so on) were taken from those files' headings only. They are pointers for the merge, not evidence.

---

## 1. Summary

- **Pains reviewed:** 66 (25 LAB, 22 LEG, 19 ADM).
- **Carried forward:** 37, grouped into 16 clusters.
- **Filtered out:** 29 — N1 weak evidence 10; N2 not software-solvable 6; N3 postponed, draft or lapsed 5; N4 already solved or saturated 6; N5 too niche 0; N6 legally risky 1; N7 duplicate 1.

**Strongest themes:**
1. **Mandatory e-notifications (ADM-08).** About 1.45M legal entities face a rule that treats an unopened notice as rejected after 10 days, which leads to embargoes, and the case law is split. This is the top administrative pain.
2. **The MASC pre-litigation step (LEG-01).** It has been in force since April 2025, yet there is still no official channel and the proof rules differ city by city. It is a cross-group theme shared with the finance and property tracks.
3. **Labour risk at record levels.** Dismissal claims hit a record 45,230 in Q2 2026. The Labour Inspectorate (ITSS) proposed €858M in sanctions in 2025. New case-law traps keep appearing, and since 5 Oct 2026 every employer owes new hires a written statement under RD 723/2026 (LAB-09, LAB-11, LAB-12, LAB-15).
4. **Foreign-worker compliance (LAB-08).** The 2026 regularisation drew more than 1.17M applications.
5. **Ley 10/2025 consumer and phone-sales rules (LEG-11, LEG-12, LEG-13).** New complaint, renewal and call-prefix duties now apply to SMEs.

**Ideas:** 15 candidates — 2 of type A, 8 of type B and 5 of type C.
- Four are trivially copyable and are flagged as such: I07, I10, I13 and I15.
- The more defensible ones rest on one of three things:
  - integrations: I01 and I08;
  - maintained rules or outcome datasets: I02, I06, I11 and I14;
  - professional distribution channels: I03 and I05.

**Status cautions:**
- The digital time-recording decree is still a draft, although it could be approved before the 29-N election.
- Pay transparency, the Spanish AI law and NIS2 are drafts or lapsed bills and were filtered as N3.
- Kit Digital is closed.

---

## 2. Pain clusters

### C1. Working-time records and overtime exposure
- **Pain IDs:** LAB-01, LAB-02, LAB-14
- **Problem:**
  - *The duty.* Every employer must record each worker's daily start and end times and keep the records for 4 years. By the Consejo de Estado's count that is about 1.35M companies. Paper or Excel is still legal, so many micro firms underinvest until an inspection or a claim (LAB-01).
  - *Fines.* Enforcement is steady. Working-time and overtime fines totalled €17.2M in 2024 (13,681 infractions), plus €2.99M for missing records (1,869 infractions), at €751–7,500 per infraction ([El Derecho/EP](https://elderecho.com/inspeccion-de-trabajo-elevo-un-9-las-multas-por-infracciones-por-tiempo-de-trabajo-en-2024)) (LAB-01, LAB-02). Euskadi's inspectors find irregularities in more than 60% of working-time inspections (LAB-02).
  - *Overtime claims.* Unpaid overtime runs at about 2.4–2.5M hours a week. Since STS 372/2026, where there is neither a fixed schedule nor a record, a worker's concrete claimed hours can be taken as true ([RRHH Digital](https://www.rrhhdigital.com/secciones/legal/794593/el-tribunal-supremo-pone-limites-a-las-reclamaciones-de-horas-extra/)) (LAB-02).
  - *Contract conversions.* In 2025 the Inspectorate converted 70,163 temporary and fijo-discontinuo (permanent seasonal) contracts into ordinary permanent ones and extended 18,804 part-time contracts ([El Derecho/EP](https://elderecho.com/?p=489934)) (LAB-14).
  - *If the digital decree passes.* The Consejo de Estado puts the cost at €867M a year, about €640 per firm (inference) ([El Español](https://www.elespanol.com/invertia/economia/empleo/20260323/consejo-critica-tumba-registro-horario-yolanda-diaz/1003744181041_0.html)) (LAB-01).
- **Conflict in the notes:** one unsourced article gives €15.7M of working-time fines for 2025. It is not reconciled with the €17.2M for 2024 and may use a different scope (LAB-02).
- **Driver and status (Oct 2026):**
  - Art. 34.9 ET (RDL 8/2019) is in force.
  - The digital time-recording royal decree is a **draft**. The Consejo de Estado's opinion of 23 Mar 2026 was unfavourable, approval was postponed on 24 Jul 2026, and it was missing from the 6, 13 and 20 Oct Council of Ministers agendas. Because it is a regulation, it can still be approved before 29-N, with a 6- or 12-month transition for SMEs under discussion (LAB-01).
  - RDL 32/2021 and RD 723/2026, which requires written justification of temporary contracts, are in force (LAB-14).
- **Used today:**
  - Paper or Excel.
  - Woffu Lite from €1.5 per user per month (10 employees or fewer).
  - Sesame €4.75–8 per employee (15-employee minimum).
  - Factorial from €5–5.5 per person.
  - Timu (Nimbo), priced by headcount.
  - Gestorías and Contrat@ for contracts (LAB-01, LAB-14).
- **Feeds:** G2-I04.

### C2. The universal employer paperwork stack, and HR software that fits micro firms poorly
- **Pain IDs:** LAB-15, LAB-18, LAB-20, LAB-12, LAB-24
- **Problem:**
  - *RD 723/2026, since 5 Oct 2026.* Every hire on a contract longer than 4 weeks must receive a written statement before starting work ([BOE](https://www.boe.es/eli/es/rd/2026/09/09/723)) (LAB-15). It covers parties, duties, pay items, hours, probation, convenio (collective agreement), protocols, equality measures and any algorithmic decision systems. Changes must be notified by the day they take effect. Existing staff can request the statement, and the employer has 30 working days to reply.
  - *Other duties of the same micro employer:*
    - harassment procedures under LO 10/2022 art. 12, with LGTBI measures only above 50 workers (LAB-18);
    - an occupational risk prevention (PRL) set-up from the first worker. Firms of up to 10 workers (25 with a single workplace) may self-manage it, except health surveillance (LAB-20).
  - *Enforcement.* The Inspectorate proposed a record €858.26M in sanctions in 2025 (+58.6%), across 1,206,028 actions and 427,495 workplaces. Anonymous complaints rose 17.5% to 11,824 ([El Derecho/EP](https://elderecho.com/?p=489934)) (LAB-12).
  - *Poor software fit.* Sesame requires a 15-employee minimum, and Woffu's plans above Lite are annual-only. Factorial and PayFit draw complaints about slow or ticket-only support (LAB-24).
- **Driver and status (Oct 2026):**
  - RD 723/2026 has applied since 5 Oct 2026. Its text sets no sanctions, and publication of the SEPE model document was not verified.
  - LO 10/2022, RD 1026/2024, Ley 31/1995, RD 39/1997 and RDL 8/2024 (heat-episode protocols) are in force.
  - Inspection pressure is intensifying (LAB-12, LAB-15, LAB-18, LAB-20).
  - Spain also faces an EU infringement case for late transposition of Directive 2019/1152 (single source, LAB-15).
- **Used today:**
  - Gestoría contract packs and consultancy templates (prices not found).
  - HR suites with e-signature (Factorial Core).
  - External prevention services (SPA) such as Quirónprevención, Cualtis and Preving (prices not found) (LAB-15, LAB-18, LAB-20).
  - From the software table: Kenjo €6–10 per employee; Holded HR add-on €1.50 per employee; Signaturit e-signature from €35 per user per month for 5 envelopes.
- **Feeds:** G2-I04.

### C3. Dismissals and terminations
- **Pain IDs:** LAB-09, LAB-11, LAB-06
- **Problem:**
  - *Volume.* Dismissal claims reached a record 45,230 in Q2 2026 (+11.2%) and 87,802 in H1 2026 (+7.3%), about 170k a year ([Law&Trends/EFE](https://www.lawandtrends.com/noticias/laboral/las-demandas-por-despido-marcan-record-en-el-segundo-trimestre-con-45-230-procedimientos-1.html)) (LAB-09). The largest regional volumes in Q2 were Cataluña 9,075, Madrid 8,040, Andalucía 7,302 and C. Valenciana 5,885. Wage claims run at 32–35k a quarter.
  - *Procedural traps.* Owner-managers without HR staff miss steps that case law and the TGSS (Social Security treasury) added in 2024–2026 (LAB-11):
    - a hearing before any disciplinary dismissal;
    - nullity for retaliation even before a formal complaint (STS 526/2026);
    - contributions on notice pay, under RED 8/2026 (CRA code 0054);
    - income-tax and Social Security withholding on back pay;
    - nullity of clauses allowing unilateral schedule changes (STS 491/2026).

    The Inspectorate also proposed €459,587 in fines for improper probation terminations.
  - *Permanent incapacity.* Since Ley 2/2025, it no longer ends a contract automatically. The worker has 10 days to ask to stay, and the employer 3 months to adapt the post or justify an excessive burden (LAB-06).
  - *Risk is procedural, not monetary.* Compensation is fixed by tariff (STS 1350/2024; STS 736/2025). Trials in Madrid and Barcelona are being set for 2029–2030, so disputes remain open liabilities for years (LAB-09, LAB-10).
- **Driver and status (Oct 2026):** in force. ET arts. 49–56 and the LRJS; 2024–2026 case law; the TGSS criterion since 14 Jul 2026; Ley 2/2025 since 1 May 2025 (LAB-06, LAB-09, LAB-11).
- **Used today:**
  - Gestorías, graduados sociales (licensed labour advisers) and labour lawyers.
  - Settlements at SMAC (the pre-trial conciliation service) and settlement agreements.
  - Law-firm articles as guidance.
  - Prevention services plus lawyers for incapacity cases (LAB-06).
  - No prices were found and no dedicated SME tool exists (LAB-09, LAB-11).
- **Feeds:** G2-I03.

### C4. Payroll rule churn, convenios, absence and leave
- **Pain IDs:** LAB-03, LAB-05, LAB-21, LAB-22
- **Problem:**
  - *Cost of outsourced payroll.* Micro employers pay gestorías about €15–20 per payslip per month, with minimum fees from €49 to about €250 a month ([Billeo](https://www.billeo.es/blog/cuanto-te-cuesta-de-verdad-contratar-a-tu-primer-empleado); [PayFit](https://payfit.com/es/contenido-practico/software-de-nominas-vs-asesor-laboral/)). The gestorías absorb continuous rule changes, which are often province-specific because many convenios are provincial (LAB-21).
  - *Examples of churn:*
    - The 2026 minimum wage (SMI), €1,221 × 14 payments, was approved on 18 Feb and backdated to 1 Jan. Payroll had to be re-run, and employers must test each year whether existing supplements absorb the rise, measured against €17,094 a year. A decree-law barring absorption of some supplements was announced, but its status is unverified ([PwC](https://periscopiofiscalylegal.pwc.es/se-fija-la-cuantia-del-smi-el-problema-ahora-es-como-aplicarlo/)) (LAB-03).
    - Courts disagree on shift and holiday rules (LAB-21).
    - Birth leave is now 19 weeks, and the 5-day family-care leave applies per event with no annual cap (TS 753/2026) (LAB-22).
  - *Sick leave at a record.* Absenteeism reached 7.6% of agreed hours, with 1.41M workers absent. Companies directly bore €16.1bn of the €33.3bn cost of sick leave (incapacidad temporal), partly through convenio top-ups (single source, [Law&Trends](https://www.lawandtrends.com/noticias/laboral/las-empresas-necesitan-herramientas-para-gestionar-mejor-sus-bajas-medicas-y-reducir-sus-niveles-de-absentismo-1.html)) (LAB-05).
- **Driver and status (Oct 2026):** in force and changing continuously — the LGSS, the annual contribution order, convenios, TGSS bulletins, RD 126/2026, RDL 9/2025 and 2026 case law. Absenteeism itself is structural (LAB-03, LAB-05, LAB-21, LAB-22).
- **Used today:**
  - Gestorías on a3innuva and similar payroll engines.
  - PayFit.
  - Leave modules in HR suites, e.g., Sesame "Vacaciones y Ausencias" from €4.75 per employee.
  - Employers' association circulars and mutuas (LAB-03, LAB-05, LAB-21, LAB-22).
  - Nominasol (DELSOL), with no public prices (software table).
- **Feeds:** G2-I06.

### C5. Foreign-workforce compliance
- **Pain IDs:** LAB-08, ADM-10
- **Problem:**
  - *Fines.* In 2025 the Inspectorate found 18,655 foreign workers without authorisation (+53.1%) and proposed €187.7M in fines, about €10k per worker (inference) ([El Derecho/EP](https://elderecho.com/?p=489934)) (LAB-08).
  - *Regularisation wave.* RD 316/2026 drew more than 1.17M applications, 202,424 of them in Madrid, where lawyers filed 58% of the online applications ([Law&Trends](https://www.lawandtrends.com/noticias/abogacia/los-expertos-avalan-a-una-abogacia-leal-pero-firme-que-ha-ayudado-a-regularizar-a-mas-de-1-2-millones-de-inmigrantes-1.html)).
  - *Office overload.* Zaragoza handles about 34,000 files a year, its workload is up 25% and its average delay is six months ([CSIF Aragón](https://www.csif.es/es/noticia/portada/aragon/articulo/85294)). La Rioja has more than 1,000 files pending (LAB-08).
  - *Inconsistent criteria.* The Ombudsman reports worrying delays and diverging criteria between offices, with "graves consecuencias… también para sus empleadores" ("serious consequences… also for their employers"). Two interpretive criteria for the new immigration regulation were issued a month apart (ADM-10).
- **Driver and status (Oct 2026):**
  - RD 1155/2024 has applied since about 20 May 2025, with challenges pending at the Supreme Court.
  - The RD 316/2026 application window closed on 30 Jun 2026; resolutions and card issuance are ongoing (LAB-08, ADM-10).
- **Used today:** immigration lawyers, gestorías, Correos (17% of Madrid's online filings) and individuals (11%). No prices were found (LAB-08, ADM-10).
- **Feeds:** G2-I05.

### C6. Regulatory whiplash and obligation tracking
- **Pain IDs:** LAB-25, ADM-05
- **Problem:**
  - *Unstable rules.* Employers and their advisers plan around rules that are announced, delayed, rejected or applied retroactively (LAB-25):
    - the 37.5-hour week, rejected on 10 Sep 2025;
    - the digital time-recording decree, postponed;
    - pay transparency, overdue since 7 Jun 2026;
    - RD 723/2026, four years late and then effective 20 days after publication;
    - a retroactive SMI;
    - the decree-law on SMI absorption, still pending.
  - *Volume.* Official bulletins published 1.32M pages in 2022 (+22%), 80.8% of them regional; keeping up with the BOE alone takes about 698 pages a day ([INAP summary of CEOE](https://laadministracionaldia.inap.es/noticia.asp?id=1232548)). In 2025 the state approved 6 laws, 267 normative royal decrees and RDL 1/2025 to 17/2025. Only 36.18% of the 2025 regulatory plan was approved (ADM-05).
  - *Who it hits.* All businesses — 3,310,824 active companies (INE DIRCE) — and the gestorías serving them (ADM-05).
- **Driver and status (Oct 2026):**
  - Structural.
  - The Cortes were dissolved on 6 Oct 2026, elections are on 29 Nov 2026 and the new chambers constitute on 23 Dec 2026. Pending bills lapse, while regulations can still be approved before the caretaker period (LAB-01, LAB-25).
- **Used today:**
  - Grant Thornton and PwC newsletters.
  - Training at the Colegios de Graduados Sociales.
  - The "Novedades destacadas" bulletin of the Consejo General de Gestores Administrativos, the national council of gestorías (LAB-03).
  - Associations and legal publishers (products and prices not verified) (LAB-25, ADM-05).
- **Feeds:** G2-I15.

### C7. MASC and the cost of civil claims (cross-group theme)
- **Pain IDs:** LEG-01, LEG-04, LEG-02
- **Problem:**
  - *The requirement.* Since 3 Apr 2025, most civil and commercial claims need a documented good-faith negotiation attempt (MASC). That covers most of the 3,287,980 civil cases filed in 2025 ([CGPJ](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/En-Portada/Los-organos-judiciales-recibieron-en-2025-un-3-2---menos-asuntos-que-el-ano-anterior-y-aumentaron-en-un-2---su-capacidad-de-resolucion)) (LEG-01).
  - *No official channel.* There is still no official channel, registry or form; the implementing rules for the official MASC services were pending on 6 Oct 2026 (LEG-01).
  - *Proof problems.* In an ICAM survey of 1,164 Madrid lawyers, 49.3% had problems proving the attempt and 71.7% see inconsistent interpretation (single outlet, [Moncloa.com](https://www.moncloa.com/2026/10/06/requisito-masc-lo-1-2025-juzgados-3443197)) (LEG-01).
  - *City-specific rules:*
    - Las Palmas requires MASC in monitorio and treats its absence as incurable.
    - Valencia treats a missing attempt as an incurable defect.
    - Sevilla excludes WhatsApp and SMS and accepts email only with consent.
    - Cádiz imposes waits of 30 days or 3 months.
    - Zaragoza accepts burofax, buromail and certified email.
  - *Delay.* The step adds 30–90 days (vendor figure, LEG-01).
  - *Cost.* A private certified file costs €110–150 + VAT, plus €100–120 + VAT per mediation session; free conciliation before the court clerk takes about 6 months (LEG-01, LEG-04). Refusing an opponent's offer can backfire on costs (LEG-04).
  - *Slow courts.* Civil first instance takes 11.0 months and appeals 9.6 months; 1,384,591 enforcement files are pending. Murcia, Madrid and Sevilla have the most congested civil courts, Zaragoza and Valladolid the least (LEG-02).
- **Driver and status (Oct 2026):**
  - LO 1/2025 is in force, and the official channel is still pending.
  - The Supreme Court has not unified the case law. AP Alicante and AP Navarra overturned inadmissions, and AP Huelva raised constitutional doubts.
  - ICAM wants MASC to become voluntary (LEG-01).
- **Used today:**
  - Lawyers sending burofax or buromail, and notarial demands.
  - Mediators registered with the Ministry of Justice.
  - Legal Pigeon: no public prices; about 1,500 files and a 36% agreement rate in Q1 2026 (vendor data).
  - An unnamed eIDAS platform at €110–150 + VAT per file (LEG-01).
- **Feeds:** G2-I02.

### C8. Complaint-driven data protection on physical premises
- **Pain IDs:** LEG-05, LEG-06
- **Problem:**
  - *Complaints at a record.* Customers, neighbours and ex-employees filed a record 30,931 complaints with the AEPD (the data protection agency) in 2025 (+64%). The agency's resolution rate fell from 96% to 76%, procedures take 45% longer and 76% of appeals to the Audiencia Nacional fail ([BDO](https://es-admin.bdo.global/getattachment/29fdc619-d1c8-40fd-af4f-57757c6ceb21/AEPD-2025.pdf?lang=es-ES)) (LEG-05).
  - *Fines.* Fines in commerce, transport and hospitality rose from €0.61M to €10.76M (+1,653%). Typical SME fines run €600–3,000 (web cases, [Lawwwing](https://lawwwing.com/aepd-sanciones-2025/)) (LEG-05).
  - *CCTV.* Video surveillance is the second-largest complaint area (4,050, +19%) and the area with the most finished procedures (81). Typical cases are cameras aimed at the street or a neighbour, missing signs, indefinite retention and staff filmed without notice (LEG-06).
- **Conflict in the notes:** Lawwwing gives €33.9M as the 2025 total against €48.1M elsewhere, and the fine counts differ (325, 326 or 299) (LEG-05).
- **Driver and status (Oct 2026):** GDPR, LOPDGDD art. 22 and the AEPD video-surveillance guide (updated Feb 2025) are in force, and enforcement volume is rising (LEG-05, LEG-06).
- **Used today:**
  - Free AEPD tools: Facilita (51,979 accesses) and Gestiona RGPD (29,304).
  - The AEPD guide and installers' templates.
  - Consultancies such as PymeLegal (no public prices).
  - Lawwwing at €9.9–79 a month, web-focused (LEG-05, LEG-06).
- **Feeds:** G2-I10.

### C9. B2C consumer-law duties, including the Catalan-language rules
- **Pain IDs:** LEG-12, LEG-15
- **Problem:**
  - *Consumer-law duties for all traders.* Since 28 Dec 2025, Ley 10/2025 has amended the consumer law (TRLGDCU) for every trader (LEG-12):
    - each complaint gets an ID key and a written receipt and must be answered within a maximum of 15 days (art. 21.2–21.3);
    - prices must show the full final amount, fees included (art. 20.1.c);
    - customers get 15 days' notice before the deadline to opt out of a renewal (art. 97.1.p);
    - the business must state whether its reviews are verified (art. 20.4);
    - contracts from calls made without valid consent are void (art. 62.1) ([BOE](https://www.boe.es/eli/es/l/2025/12/26/10)).
  - *Who it hits.* Shops, gyms, academies, clinics, e-commerce and subscription businesses of every size. Most log nothing, so they cannot prove they complied (LEG-12, inference).
  - *Catalonia.* Under the Codi de consum (art. 128-1), signs, menus, offers, contracts and invoices must also be available in Catalan. Language complaints rose from 206 (2021) to 1,873 (2023), with 1,250 cases in 2024 (LEG-15).
    - Fines: 7% of 5,406 complaints (2012–2024) ended in a sanction, averaging €2,240 and up to €10,000 ([NacióDigital](https://naciodigital.cat/societat/nomes-7-denuncies-vulnerar-drets-linguistics-consumidors-han-acabat-en-sancio.html)).
    - Restaurants and bars account for nearly half of cases. Fixed information and purchase offers (menus, price lists) make up 55% of sanctions.
  - *Official complaint forms.* LEG-22 (filtered as a duplicate) adds the Catalan duty to offer official complaint forms, including online.
- **Conflict in the notes:** 1,873 complaints in 2023 (3Cat, Vozpópuli) against more than 2,000 (NacióDigital, which counts more case types) (LEG-15).
- **Driver and status (Oct 2026):**
  - The duties are in force.
  - It is unclear whether the 12-month adaptation period also covers the consumer-law amendments (LEG-12).
  - Catalan enforcement is complaint-driven and rising; 2025 figures are missing (LEG-15).
- **Used today:**
  - Email and Excel.
  - Helpdesk tools built for larger firms.
  - Lawyers updating terms and conditions.
  - Manual translation, or Catalan versions supplied by brands.
  - No SME-specific product or prices found (LEG-12, LEG-15).
- **Feeds:** G2-I07.

### C10. Customer-service regime for basic-service SMEs
- **Pain IDs:** LEG-13
- **Problem:**
  - *Who.* Basic-service providers of any size: small internet providers, local water utilities, small electricity and gas retailers, bus, coach and ferry operators, and postal firms.
  - *What, by 28 Dec 2026:*
    - put a human on the line for 95% of requests within 3 minutes on average;
    - never cut calls because of long waits;
    - issue complaint keys and resolve complaints within 15 working days (2 hours for service interruptions, 5 days for billing);
    - run a 24/7 incident line;
    - serve customers in a co-official language on request;
    - pass an annual audit by an ENAC-accredited body (accredited by Spain's national accreditation body) ([KPMG](https://assets.kpmg.com/content/dam/kpmgsites/es/pdf/2026/01/legal-alert-regulacion-servicios-atencion-clientela-ley-10-2025.pdf.coredownload.inline.pdf)) (LEG-13).
  - *Exemption.* Retailers below 5% market share are exempt only from the 24/7 line and the numbering rules, not from the 3-minute rule or the audit (LEG-13).
  - *Scale.* Not quantified; the notes infer "a few thousand SMEs at most". Fines of up to €100,000 per infringement come from an unverified vendor snippet (LEG-13).
- **Driver and status (Oct 2026):** Ley 10/2025 is in force, with a hard adaptation deadline of 28 Dec 2026. It is already law, so the dissolution does not affect it (LEG-13).
- **Used today:** contact-centre suites built for large firms, and advisory and audit firms (TÜV SÜD, KPMG). No SME pricing found (LEG-13).
- **Feeds:** G2-I09.

### C11. Outbound sales calls after 17 October 2026
- **Pain IDs:** LEG-11
- **Problem:**
  - *Who.* Energy and telecom resellers, insurance agents and brokers, solar installers, estate agencies, training providers and small call centres.
  - *Blocking.* Since 17 Oct 2026, operators block their commercial calls unless they come from 400-prefix numbers. Customer-service calls must use 800/900, short codes or geographic numbers.
  - *Volume blocked.* The anti-scam plan had blocked 192M calls and 17M SMS by April 2026, and 300M calls and 26.6M SMS by August 2026 ([La Moncloa](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/Paginas/2026/160426-prefijo-400-llamadas-comerciales.aspx); [ESdiario](https://www.esdiario.com/economia/260810/195137/gobierno-obligara-17-octubre-prefijo-400-llamadas-comerciales.html)) (LEG-11).
  - *Void contracts.* Contracts concluded in calls that break the rules are presumed to lack consent and are void. Consent must be express and given within the previous 2 years (TRLGDCU art. 62.1) (LEG-11).
  - *Fines.* A telephony vendor puts fines for numbering misuse under the telecoms law (LGTel) at €50,001–€2M (LEG-11).
- **Driver and status (Oct 2026):**
  - The Ministry resolution has been in force since 17 Apr 2026, and blocking has been live since 17 Oct 2026.
  - Ley 10/2025 art. 16.3–16.4 and LGTel art. 66.1 also apply.
  - Whether B2B calls and autónomos are covered is **unverified** (LEG-11).
- **Used today:** operators (400 ranges assigned by the CNMC, the competition and markets regulator), cloud telephony vendors such as Aircall, and checks against the Lista Robinson advertising-exclusion list. No prices collected (LEG-11).
- **Feeds:** G2-I08.

### C12. Mandatory e-notifications and company digital identity
- **Pain IDs:** ADM-08, ADM-07
- **Problem:**
  - *Who.* Every legal entity — about 1.45M non-natural-person businesses (inference from [INE DIRCE](https://www.ine.es/dyngs/Prensa/DIRCE2025.htm)) — plus professionals in compulsory professional colleges (ADM-08).
  - *The 10-day rule.* They must deal with the administration electronically, and a notification left unopened for 10 calendar days is deemed rejected, after which the procedure moves on to enforcement and bank-account embargoes (Ley 39/2015 arts. 14.2 and 43.2) (ADM-08).
  - *The missing-alert dispute.* The email alert is mandatory, yet its absence does not invalidate the notice (art. 41.6), and courts are split:
    - TS 1927/2017 upheld an embargo;
    - TSJ Murcia 396/2025 annulled one, in line with STC 84/2022 and SAN 78/2022 ([GA-P](https://ga-p.com/wp-content/uploads/2025/11/Aviso_previo_condicion_validez.pdf)).
  - *Fragmentation.* A vendor claims there are more than 9,000 separate electronic offices (sedes) (ADM-08).
  - *Court summonses.* Since 20 Mar 2024, legal persons receive first court summonses electronically (search snippet only, ADM-08).
  - *Digital identity.* A company's representative certificate costs €14 + tax and expires every 2 years (ADM-07):
    - entities whose tax ID (NIF) does not start with A, B, C or D must accredit identity in person at a tax-agency (AEAT) office;
    - the DNIe/NFC route is unreliable;
    - certificates are often shared among staff;
    - signatures were misused in the Kit Digital fraud case.
- **Driver and status (Oct 2026):** in force. The case law is evolving, with no Supreme Court ruling on the protective line as of Nov 2025. No statistics exist on embargoes caused by missed notifications (ADM-08).
- **Used today:**
  - Gestorías acting as representatives (prices not found).
  - IvNeos and IvSign from Ivnosys (no published prices).
  - Manual daily checks of several sedes (ADM-08, ADM-07).
- **Feeds:** G2-I01.

### C13. Opening premises: use compatibility and post-opening checks
- **Pain IDs:** ADM-01, ADM-03
- **Problem:**
  - *Lease before certainty.* Anyone opening or changing premises commits to a lease before knowing whether the use is allowed (ADM-03).
  - *Madrid.* The council handled 13,301 declaraciones responsables (DRs, self-declarations that let a business open before the council checks it) and licences in 2025. Its own standards target an average of 109 days to check a DR (only 40% within 90 days) and 137 days for a prior licence (40% within 60 days). Owners therefore operate exposed for months after spending on works ([Carta de Servicios ADA 2026](https://www.madrid.es/UnidadesDescentralizadas/Calidad/CARTAS%20SERVICIOS/SistemaCartasServicio/41%20CS_de%20la%20Agencia%20de%20Actividades/DEFINITIVA/CS_ADA_2026.pdf)) (ADM-01).
  - *Paid certainty.* Madrid's private collaborating entities (ECUs) charge regulated prices ([ECU prices 2026](https://www.madrid.es/UnidadesDescentralizadas/AgenciaActividades/ECUs/ficheros/AnexosI_II_III_IV_PreciosECU2026.pdf)) (ADM-01, ADM-03):
    - an ECU-managed DR costs €600–1,250 up to 300 m²;
    - visits cost €190–1,080;
    - a compatibility certificate costs €500–1,000;
    - on top come municipal fees and the 4% construction tax (ICIO).
  - *València.* The compatibility certificate went from 15–45 days to more than a year for large projects (2023 data, ADM-03). The city's backlog figures (ADM-02) were filtered as N1.
- **Driver and status (Oct 2026):**
  - Madrid Ordenanza 6/2022 is in force, and ECU prices for 2027 were approved on 15 Oct 2026 (ADM-01).
  - Valencia's Ley 6/2014 compatibility certificate is in force; a new municipal ordinance has been in drafting since May 2025, with approval unverified (ADM-02, ADM-03).
- **Used today:**
  - ECUs: 19 in Madrid, with discounts of 5–15%.
  - Architects and engineers (fees not found) and gestorías.
  - Málaga's free online licensing assistant, ALU (ADM-01, ADM-03).
- **Feeds:** G2-I11.

### C14. Grant justification and repayment after NextGenerationEU
- **Pain IDs:** ADM-14, ADM-15
- **Problem:**
  - *Beneficiaries and access.* NextGenerationEU (NGEU) reached 1.46M beneficiaries, 70% of them micro firms and SMEs, but SMEs received only 43% of awarded funds ([CEOE, Jun 2026](https://www.ceoe.es/sites/ceoe-corporativo/files/content/file/2026/06/26/104/informe-ejecucion-fondos-europeos-junio-2026.pdf)) (ADM-14).
  - *Slow money.* In 2025 payments reached only 18.7% of available credits, and 73% of the loan tranche was renounced. Funcas sees about €32bn at risk. Companies cite "excesiva carga administrativa" (excessive administrative burden) (ADM-14).
  - *Risk now shifts to justification.* The Recovery Facility's milestone deadline of 31 Aug 2026 has passed, and Spain has filed its final €25,861M payment request ([planderecuperacion.gob.es](https://planderecuperacion.gob.es/)). The pain now moves to proving execution and avoiding repayment through 2026–2028 (ADM-14).
  - *Intermediated grants.* MOVES III (EV and charging) files stay unresolved. In Andalucía only the participating installer can apply and justify, so beneficiaries are stuck if that firm stops responding (ADM-15).
- **Driver and status (Oct 2026):**
  - Regulation (EU) 2021/241: the milestone deadline has passed and the final request is pending EU assessment.
  - Ley 38/2003 General de Subvenciones (not re-verified).
  - CEOE asks for execution until 2028, earlier justification guides, easier corrections and advance payments (ADM-14, ADM-15).
- **Used today:**
  - Grant consultancies (fees not found).
  - Fandit, at €56–600 a month, for discovery only.
  - Installers and in-house teams (ADM-14, ADM-15, ADM-16).
- **Feeds:** G2-I12.

### C15. Public-procurement access for micro suppliers
- **Pain IDs:** ADM-17, ADM-18
- **Problem:**
  - *Scale and thin competition.* In 2024 Spain ran 206,242 tenders with a €113.1bn base budget ([OIReScon IAS 2025](https://www.hacienda.gob.es/rsc/oirescon/informe-anual-supervision-2025/ias2025-resumen-ejecutivo-es.pdf)) (ADM-17):
    - only 2.94 bidders per contract on average (3.99 in 2020);
    - 40.69% of awarded lots had a single bidder, more often in smaller contracts;
    - 7.63% of lots went unawarded;
    - processing averaged 117.47 days;
    - 5,053 special appeals were filed.
  - *Fragmented sources.* Tenders sit on the national platform (PLACSP) and seven regional platforms whose data lack homogeneity (ADM-18).
  - *Invisible small contracts.* There is no aggregated data at all on contratos menores (below €15,000 for services and supplies, €40,000 for works), the natural entry point for micro firms (ADM-18).
- **Driver and status (Oct 2026):** the public-procurement law (LCSP, Ley 9/2017) is in force, and the Estrategia Nacional de Contratación Pública 2023–2026 is ending (ADM-17, ADM-18).
- **Used today:**
  - licitaciones.es: alerts, an AI assistant, competitor intelligence and help registering in ROLECE; no public prices.
  - Euroalert: EU calls; no public prices.
  - Consultants (ADM-17, ADM-18).
- **Feeds:** G2-I14.

### C16. Autónomo contribution regularisation
- **Pain IDs:** ADM-11
- **Problem:**
  - *The mechanism.* Under the real-income system (RDL 13/2022), the TGSS regularises the previous year's provisional contribution bases and sends resolutions demanding the difference.
  - *Complaints.* Prior claims are "generally not upheld", and the Ombudsman says the method wrongly excludes months of activity such as birth leave ([Defensor del Pueblo 2025, pp. 226–227](https://www.defensordelpueblo.es/wp-content/uploads/2026/03/Defensor-del-Pueblo_Informe-anual-2025.pdf)) (ADM-11).
  - *Who.* The proxy population is 1,859,925 natural-person businesses (INE DIRCE); RETA (the self-employed Social Security regime) membership was not retrieved.
  - *Evidence limits.* Single source; amounts not available (ADM-11).
- **Driver and status (Oct 2026):** RDL 13/2022 is in force, and regularisations are ongoing in 2025–2026 (ADM-11).
- **Used today:**
  - Gestorías (prices not found) (ADM-11).
  - Autónomo platforms from the software table: Declarando €29.90–99.90 a month + VAT, Cuéntica €9–129 a month. Whether they forecast the contribution band is not documented.
- **Feeds:** G2-I13.

---

## 3. Noise log

| Pain ID | Title | Code | Justification |
|---|---|---|---|
| LAB-04 | Rising employer contributions and total labour cost | N2 | The pain is the cost itself (labour cost +4.0% a year, INE). The software parts — rate updates and cost simulators — are already done by payroll engines and free simulators. The notes also conflict on the 2026 intergenerational pension levy (MEI) rate: 0.80% official vs 0.90% secondary. |
| LAB-07 | Technical and trade talent shortages | N2 | A structural shortage (demographics, training mismatch) that software cannot fix; temp agencies and recruiters already serve hiring. Housing as a hiring barrier was not evidenced here (see CITY-05, HOS-26). |
| LAB-10 | Labour-court backlogs pushing trials to 2029–2030 | N2 | Court capacity is the constraint, and the notes rate it not software-solvable. Used only as context for G2-I03 (settlement pressure). |
| LAB-13 | Bogus self-employment and bogus internships | N1 | Single source, and the jump from 7,234 to 47,143 reclassifications may reflect a few large platform cases (unverified). The software answer would be a thin checklist. Revisit with startup-track evidence. |
| LAB-16 | Pay register and delayed pay-transparency transposition | N3 | Transposition is overdue and exists only as a draft royal decree (consulted Aug 2026; details single-source). After the dissolution, the parts needing a law are unlikely before 2027. The pay register already in force is a basic payroll report. Re-check if a decree is approved before 29-N. |
| LAB-17 | Equality plans (50+ staff) and REGCON registration friction | N1 | Low confidence on scale and cost (no counts from REGCON, the Ministry's register of convenios and equality plans; no consultancy prices). Rulings TS 519/2026 and STS 461/2025 already curtailed the registration friction, and the negotiation itself is human. |
| LAB-19 | Internal whistleblowing channel (50+ staff) | N4 | Deadlines passed in 2023, the software is commoditised and no enforcement by the whistleblower authority was found. |
| LAB-23 | Training-credit (FUNDAE) bureaucracy and under-use | N1 | Low-medium confidence. The 21% usage estimate mixes different bases, and lost credit is not quantified. Training providers already do the paperwork bundled with their courses. |
| LEG-03 | Congested commercial courts | N2 | Court capacity is the constraint. The 18.6% intake rise is probably driven by insolvency, and the share of partner, IP and unfair-competition cases is unknown. |
| LEG-07 | Website legal compliance (cookies, legal texts) | N4 | Already cheap: Cookiebot is free up to 50 subpages, then €7–90 a month; Lawwwing costs €9.9–79 a month including legal texts. The remaining configuration-audit gap is thin and easy to copy. |
| LEG-08 | Everyday data slips (no BCC, WhatsApp, internal snooping) | N1 | Few quantified cases (one €1,200 fine), and the risk is behavioural. BCC guards for email are trivially copyable. |
| LEG-09 | Personal-data breaches leading to AEPD procedures | N4 | The AEPD's free Comunica-Brecha (15,214 accesses) and Asesora-Brecha (9,237) tools cover the 72-hour notification step. SME breach fines are not quantified, and prevention is a security service (see VOX-04). |
| LEG-10 | Opaque outsourced data-protection market | N1 | Low confidence. No consultancy prices were found, so no cheaper-alternative case can be made, and the offer competes with free AEPD tools and SaaS from €9.9 a month. |
| LEG-14 | Online reviews: authenticity duties and fake reviews | N1 | Pain size is unquantified, and review extortion was not verified in this track. It is better evidenced in VOX-01, VOX-02 and HOS-07; merge there. |
| LEG-16 | Digital accessibility (EAA / Ley 11/2023) | N4 | Micro service firms are exempt, existing services have until 28 Jun 2030 and no enforcement is reported. Overlay and scanning tools are already sold (Accede Me; Lawwwing's accessibility module at €28 a month). See RET-17. |
| LEG-17 | AI Act literacy and transparency duties | N3 | The Spanish AI sanctions law was a bill in Congress and lapses with the 6 Oct 2026 dissolution. Art. 4 was softened, art. 50 disclosure is a banner that chatbot vendors already provide, and Lawwwing sells an AI add-on at €13 a month. |
| LEG-18 | NIS2 and ENS security demands from clients | N1 | No data on questionnaire volumes or ENS certification costs. Spain's NIS2 law is still a draft that has not reached Congress (also an N3 risk). |
| LEG-19 | Trademark and trade-name conflicts | N1 | One statistical source, no data on oppositions or disputes, and cost not quantified. A watch service built on open data from the Spanish patent and trademark office (OEPM) would be trivially copyable. |
| LEG-20 | ESG and VSME data requests from large clients and banks | N3 | Omnibus I (Directive 2026/470) removed CSRD reporting duties for firms under 1,000 employees and protects them from data requests beyond the voluntary SME standard (VSME). The carbon-footprint decree covers only large firms. |
| LEG-21 | Municipal noise sanctions and closures | N2 | The core fix is physical (soundproofing, sound limiters), and no enforcement data was found. Overlaps the hospitality track (HOS-05). |
| LEG-22 | Official complaint forms and regional consumer inspection | N7 | Duplicate of LEG-12: the same workflow, from complaint intake to the 15-day reply. The Catalan online-form detail is folded into cluster C9 and G2-I07. |
| ADM-02 | València: chronic activity-licence backlog | N1 | 2022–2023 data, mostly from the opposition and disputed by the city government at the time. The 2024–2026 status is unknown after the 2023 reorganisation. |
| ADM-04 | Diverging local and regional requirements (market unity) | N2 | The root cause is legal and political, and complaints to the CNMC or the Ministry's market-unity unit (SECUM) are free. A map of the rules cannot remove the barriers. |
| ADM-06 | Forming a limited company (SL) | N4 | Legally fast (6–12 business hours per step) and cheap (about €100–450 in official costs). Gestorías and law firms bundle it, sometimes free, and willingness to pay is low (see STA-07). |
| ADM-09 | Scarce appointments (cita previa) | N6 | The obvious automation, appointment-sniping bots, is abusive and legally risky. The legitimate remainder (pointing users to online channels) is thin, and the root cause is staffing. |
| ADM-12 | Kit Digital: overpricing, weak control and identity misuse | N3 | The programme closed in October 2025, so the driver has lapsed; residual repayment defence is one-off legal work. The signature-misuse lesson is reused in C12. |
| ADM-13 | Kit Digital: digitalisation agents paid slowly | N3 | The programme closed in October 2025, the data is from 2023 and the market is shrinking. |
| ADM-16 | Grant discovery | N4 | Already served by Fandit (81,665 grants from more than 8,500 administrations, €56–600 a month), consultancies and the Cámaras de Comercio. A cheaper alert service would be trivially copyable. |
| ADM-19 | Public-contract execution friction | N1 | Single source (OIReScon) and not quantified. The subcontractor-payment angle belongs with the construction and finance tracks (CON-05, FIN-02). |
