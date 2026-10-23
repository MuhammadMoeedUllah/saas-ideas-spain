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
- Pay transparency (a draft decree) and the Spanish AI law (a bill that lapses with the dissolution) were filtered as N3. NIS2 is still a draft too, but its pain (LEG-18) was filtered as N1 for lack of evidence.
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

---

## 4. Candidate SaaS ideas

The ideas are numbered by theme, not ranked; ranking happens after validation. Prices are hypotheses to test.

### G2-I01: Electronic-notification watchdog for companies (DEHú and other sedes) with deadline alarms
- **Type:** C (primary). Secondary B: a multi-client version for gestorías.
- **Buyer:**
  - *Who pays:* the owner or administrator of an SL, SA, cooperative or other legal entity that receives its own notifications, especially a micro firm without an adviser holding them (ADM-08). Also professionals in compulsory professional colleges, who have the same duty (art. 14.2, ADM-08), and gestorías monitoring many clients.
  - *How many:* about 1.45M non-natural-person businesses — 3,310,824 active companies minus 1,859,925 natural persons (inference from INE DIRCE 2025; ADM-06, ADM-08). How many already delegate notifications to a gestoría: unknown — validate.
- **Pains addressed:** ADM-08, ADM-07
- **Problem:** Legal entities must deal with the administration electronically, and a notice left unopened for 10 calendar days is deemed rejected, after which the procedure moves to enforcement orders and account embargoes (ADM-08). The email alert is "mandatory", but its absence does not invalidate the notice, and courts are split: TS 1927/2017 upheld an embargo, TSJ Murcia 396/2025 annulled one. Meanwhile notices are spread over DEHú (the government's single e-notification address) and, per a vendor, more than 9,000 separate electronic offices (sedes) (ADM-08). The representative certificate needed to check them costs €14 + tax, expires every 2 years and is often shared among staff (ADM-07).
- **Product:**
  - *What it does:*
    - Checks DEHú and the sedes that matter to the company several times a day.
    - When something is pending, alerts two named people by WhatsApp, SMS and email, then by phone call if it is still unread.
    - Shows the issuer and the day-10 "deemed rejected" date, and escalates on days 5 and 8.
    - Sends a weekly "nothing pending" heartbeat so the value stays visible.
    - Keeps a monthly log documenting the company's diligence, useful if it later argues the alert was missing (ADM-08).
    - Tracks the representative certificate's 2-year expiry, with renewal steps: online accreditation only for tax IDs (NIF) starting with A, B, C or D, otherwise an in-person appointment at the tax agency (AEAT) (ADM-07).
    - Gestoría version: all clients on one board.
  - *MVP (4–6 weeks):* an "alert amplifier" that needs no certificate. The company points its official DEHú or sede alert email to a product mailbox; the product parses the alerts, computes deadlines and escalates across channels. It also tracks certificate expiry. A second phase adds active polling of DEHú, the AEAT and the TGSS — with the client's certificate on a local agent, with hardware-secured cloud custody, or as an authorised representative — if validation shows that is allowed.
  - *Deliberately not:*
    - opening notifications on the client's behalf by default (whether opening starts response deadlines is to validate);
    - answering or appealing them, or giving legal advice;
    - booking appointments (ADM-09 is N6).
- **Why now:**
  - The duty and the 10-day rule are in force (Ley 39/2015, consolidated 6 Nov 2024).
  - The case law on missing alerts is unsettled, with no Supreme Court ruling on the protective line as of Nov 2025 (ADM-08).
  - Legal persons have received first court summonses electronically since 20 Mar 2024, and summonses left unopened for 3 days go to the single court notice board (search snippet only, ADM-08).
  - There is no single deadline wave: demand is perennial.
- **Alternatives today:**
  - Gestorías acting as representatives: price not found, and they only cover clients who granted them powers.
  - IvNeos from Ivnosys, marketed as syncing "más de 9.000 sedes", and IvSign for certificate custody: no published prices; segment unknown.
  - Manual daily checks of several sedes (ADM-08, ADM-07).
  - The free official email alert: its absence is exactly the failure mode now being litigated (ADM-08).
- **Price hypothesis:**
  - €5/month per company (€50/year by direct debit) for alerts, escalation and certificate tracking.
  - €9/month with active polling of extra sedes.
  - Gestorías: €1.5–2 per client per month.
- **Channels:**
  - Gestorías and their associations; the Consejo General de Gestores Administrativos already circulates update bulletins (LAB-03).
  - Company-formation services and notaries at incorporation, since every new SL needs this from day one (ADM-06).
  - Cámaras de Comercio.
  - Business-bank onboarding, offered as embargo prevention (hypothesis).
  - Search terms: "notificación DEHú no abierta embargo", "notificaciones electrónicas empresa 10 días", "aviso notificación electrónica no recibido".
- **Build notes:**
  - *Integrations:* DEHú and individual sedes. Whether a recipient-side API exists is unknown; the notes could not read DEHú's coverage page (ADM-08).
  - *Security:* access by certificate is high-sensitivity, because the certificate lets its holder act for the company (ADM-07 documents misuse in the Kit Digital fraud). It needs hardware-backed key storage, per-use logs and least privilege.
  - *Data:* notification metadata is confidential tax and Social Security data.
  - *Complexity:* low for the alert amplifier; high for reliable polling across many sedes.
- **Moat in an AI-flooded market:** the alert amplifier alone is trivially copyable. Defensibility can come only from three things: reliable coverage of many sedes (the integration grind IvNeos sells), a security posture customers will trust with certificates, and gestoría distribution. Medium at best.
- **Key risks and kill criteria:**
  - *Risks:*
    - sedes block automated access, or their terms forbid it;
    - owners refuse to hand over certificates;
    - a Supreme Court ruling that makes the alert a condition of validity would shrink the fear factor;
    - DEHú may already push alerts to mobile.
  - *Kill if:*
    - active polling of DEHú, the AEAT and the TGSS is not legally and technically feasible without a certificate custody that fewer than 30% of interviewed owners would accept; or
    - fewer than half the companies in a pilot receive any notification within six months, which would make the value too invisible for €5/month.
- **Evidence strength:** strong. The obligation, the 10-day rule and the split case law come from the BOE and court rulings (ADM-08); how often harm actually occurs is unquantified.
- **Validation questions:**
  1. Does DEHú offer recipients or registered representatives a machine interface, an app push or an SMS channel, and on what terms? Which issuers that matter to micro firms — the AEAT, the TGSS, the DGT (traffic directorate), regional tax agencies, big-city councils — are not federated into DEHú?
  2. Legal: does viewing the list of pending notices count as accessing them? Can a third party monitor as a representative through a registered power of attorney (apoderamiento)? May a cloud service hold an FNMT representative certificate under FNMT and eIDAS terms?
  3. IvNeos (Ivnosys): price, minimum size, coverage claim and customer segment. Also search for other aggregators ("gestor de notificaciones electrónicas", "DEHú multiempresa", "alertas notificaciones AEAT").
  4. Frequency of harm: AEAT and TGSS data on enforcement surcharges (apremio) and embargoes after unopened notifications, and gestorías' estimates. Cross-check TAX-18 in the tax track.
  5. What do gestorías charge for notification monitoring, and what share of SLs is fully covered by an adviser?
  6. Has the Supreme Court ruled on the missing-alert question since Nov 2025?
  7. How exactly do legal persons receive first court summonses (a snippet-only fact), and can that channel be monitored too?

### G2-I02: MASC pre-litigation kit: court-ready negotiation file for SME claims
- **Type:** A (primary): a cheaper route than the €110–150 + VAT per-file certified platforms. Secondary B: city-specific admissibility rules and an inbox for incoming invitations, which no supplier in the notes offers.
- **Buyer:**
  - *Who pays:*
    - the owner or finance lead of an autónomo or SME claiming unpaid invoices or contract breaches;
    - the partners of the small law firms, procuradores (court agents) and gestorías acting for them;
    - collection agencies and landlords (cross-group);
    - any SME that receives a MASC invitation (LEG-01).
  - *How many:* 3,287,980 civil cases were filed in 2025, and most now need a MASC; the SME share is unknown (LEG-01). The claimant universe is the 3,310,824 active companies (ADM-06).
- **Pains addressed:** LEG-01, LEG-04, LEG-02
- **Problem:** Since 3 Apr 2025, most civil and commercial claims are inadmissible without proof of a good-faith negotiation attempt; 18 months on, there is still no official channel, registry or form, and local courts apply different proof rules (LEG-01). In an ICAM survey of 1,164 Madrid lawyers (reported by a single outlet), 49.3% had problems proving the attempt, and an inadmission means repeating a step that already adds 30–90 days (LEG-01). Private certified files cost €110–150 + VAT before any mediation, which is heavy for a €1,000–5,000 invoice (LEG-01, LEG-04).
- **Product:**
  - *What it does, for claimants:*
    - A guided intake: claim type, amount, debtor and court city.
    - Picks a valid method. Both a direct negotiation request and a confidential binding offer are recognised by LO 1/2025; referral to a registered mediator is available when wanted.
    - Sends the request through a qualified electronic delivery partner.
    - Runs the waits each city requires (LEG-01). Examples: Cádiz requires 30 days or 3 months; Sevilla excludes WhatsApp and SMS and accepts email only with consent; Zaragoza accepts burofax, buromail and certified email.
    - Logs replies and produces the court-ready pack (LEG-01):
      - proof of receipt, date and full content, as art. 10.2 requires;
      - the short description of the negotiation that the claim must attach.
    - Keeps an offer record, so the client can later ask for costs to be reduced if the other side rejected an offer close to the final judgment (LEG-04).
  - *What it does, for recipients:* an inbox that logs incoming invitations, tracks the 30-day window and drafts replies, so ignoring one does not count against them on costs (LEG-01).
  - *MVP (5–6 weeks):*
    - the claimant flow for unpaid B2B invoices in Madrid, Barcelona, Valencia, Sevilla and Zaragoza;
    - one certified-delivery partner;
    - a PDF evidence pack;
    - the recipient inbox, free, as a lead magnet.
  - *Deliberately not:* mediating (registered mediators do that), representing anyone in court, filing claims, or advising on the merits.
- **Why now:**
  - LO 1/2025 has been in force since 3 Apr 2025, and the official MASC services foreseen in additional provision 3 were still pending on 6 Oct 2026.
  - The Supreme Court has not unified the case law. AP Alicante and AP Navarra overturned rigid inadmissions, and AP Huelva raised constitutional doubts (LEG-01).
  - Courts remain slow — 11.0 months at civil first instance and 1.38M enforcement files pending — so settling before court is worth more (LEG-02).
- **Alternatives today:**
  - An unnamed eIDAS-certified platform: €110 + VAT per file (€150 with more than one invited party), €100 + VAT for a first mediation session, €120 + VAT per party afterwards (LEG-01, LEG-04).
  - Legal Pigeon: certificate "en menos de 30 días" (in under 30 days), no public prices, about 1,500 files (vendor data).
  - Lawyers' burofax or buromail (prices not found) and notarial demands.
  - Free conciliation before the court clerk, which takes about 6 months.
  - *Weaknesses:* no supplier can guarantee court acceptance, none documents city-specific packs, and per-file prices are high relative to small claims.
  - *Why a cheaper product is viable:* a direct-negotiation file needs no mediator time, only delivery, timers and documents (inference).
  - *Why customers would switch:* lower price on small claims and fewer inadmissions.
- **Price hypothesis:**
  - €29–39 per file, self-serve.
  - €99/month for law firms, gestorías and collection agencies, including 10 files, then €8 per file.
  - Recipient inbox free.
- **Channels:**
  - Small law firms (cross-group PRO-12) and procuradores.
  - Collection agencies (FIN-06, FIN-08).
  - Property managers and landlord associations (CON-20, CON-23, HOU-14).
  - Gestorías.
  - A "start MASC" button on overdue invoices inside invoicing tools such as Holded, Quipu and Billin (software table).
  - Bar-association training; ICAM is vocal on MASC (LEG-01).
  - Search terms: "MASC requisito de procedibilidad", "cómo acreditar MASC", "burofax MASC", "MASC monitorio".
- **Build notes:**
  - *Certification:* a partnership with a qualified trust-service provider for electronic registered delivery.
  - *Data:* a maintained database of local judges' agreements (juntas de jueces) and appeal rulings by city (LEG-01); debtors' personal data under the GDPR.
  - *Legal:* legal review of the templates.
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** medium. AI can generate the templates trivially. The defensible parts are:
  - the city-by-city admissibility dataset;
  - outcome data from users (which packs each court accepted or rejected);
  - the trust-service integration;
  - placement inside invoicing and collection workflows.
- **Key risks and kill criteria:**
  - *Risks:*
    - the Ministry or the regions launch free official MASC services (additional provision 3);
    - a reform after the 29-N election makes MASC voluntary, as ICAM demands (LEG-01);
    - courts refuse private certificates;
    - Legal Pigeon or burofax providers cut prices.
  - *Kill if:* a free official channel with court-accepted certificates is announced for 2027, or more than 10% of pilot files are inadmitted for proof defects.
- **Evidence strength:** strong. The BOE text, local judges' agreements, appeal decisions and a large lawyer survey (single outlet) all point the same way (LEG-01); Legal Pigeon's figures are self-reported.
- **Validation questions:**
  1. Identify the eIDAS platform priced at €110–150 + VAT (Moncloa.com, 6 Oct 2026), get Legal Pigeon's prices, and price burofax and buromail per send.
  2. Status of the official MASC services under additional provision 3 (Ministry of Justice and regions): any dates or budgets?
  3. Since Oct 2026, have the Supreme Court or more appeal courts ruled on MASC proof standards? Do courts in Madrid, Barcelona, Valencia, Sevilla, Zaragoza, Málaga and Bilbao accept qualified electronic delivery from a private provider?
  4. Is a negotiation request or confidential binding offer sent by the party itself valid without a lawyer, and does generating one raise any issue of activities reserved to lawyers?
  5. CGPJ (judiciary council) data: how many monitorio (fast-track debt) and verbal claims do companies file a year, and what share is below €2,000? Cross-check FIN-06 and FIN-07.
  6. Competitors: search "plataforma MASC online", "certificado MASC eIDAS", "mediación MASC precio"; check whether invoicing tools or collection firms already embed MASC.
  7. Do the parties' 29-N programmes propose changing MASC?

### G2-I03: Guided dismissal and termination workflow for owner-managers and their advisers
- **Type:** B (primary). Secondary A, against ad hoc hours from gestorías and labour advisers (fees not found).
- **Buyer:**
  - *Who pays:* the owner-manager of a micro or small employer without HR staff, and the gestoría partner, graduado social (licensed labour adviser) or labour lawyer who prepares terminations for such clients (LAB-11).
  - *How many:* about 1.35M employer companies (Consejo de Estado figure, LAB-01) and about 170k dismissal claims a year (inference, LAB-09). The number of graduados sociales and labour advisers is unknown — validate.
- **Pains addressed:** LAB-11, LAB-09, LAB-06
- **Problem:** Dismissal claims hit a record 45,230 in Q2 2026 (+11.2%), and labour trials in Madrid and Barcelona are being set for 2029–2030 (LAB-09, LAB-10). Recent case law and Social Security criteria turned routine steps into traps: a hearing before a disciplinary dismissal, nullity for dismissing someone days after they objected (STS 526/2026), contributions on notice pay under CRA code 0054 since RED 8/2026, withholding on back pay, and the Ley 2/2025 permanent-incapacity procedure with its 10-day and 3-month clocks (LAB-11, LAB-06). Owners who fire with a letter template turn defensible dismissals into unfair or null ones (LAB-11).
- **Product:**
  - *What it does:* one guided flow per termination type — disciplinary, objective, probation, end of temporary contract and permanent incapacity under Ley 2/2025 — covering:
    - a risk screen that flags recent complaints, objections or claims as possible retaliation (STS 526/2026);
    - the mandatory steps: hearing summons and minutes, notice;
    - generated documents: the letter, the hearing summons, a settlement-agreement draft and the final settlement;
    - calculations: statutory severance by tariff (the Supreme Court confirmed it cannot be topped up), notice pay with the right contribution coding, and back pay gross and net;
    - SMAC conciliation preparation and an export pack for the adviser (LAB-09, LAB-11);
    - for permanent incapacity, the 10-day and 3-month deadlines and the excessive-burden test for firms under 25 workers: adaptation cost against the greater of statutory severance or 6 months' salary (LAB-06);
    - a sibling flow for schedule changes, which must follow the art. 41 ET procedure (STS 491/2026, LAB-11).
  - *MVP (4–6 weeks):* disciplinary and objective dismissal flows with the letter, hearing and calculator, plus a checklist for coding notice pay (CRA 0054). Sold to advisers first.
  - *Deliberately not:* representing anyone at SMAC or in court, giving an opinion on the merits without a professional, or filing anything.
- **Why now:**
  - Litigation hit a record in 2026 (LAB-09), and the TGSS changed its criterion in July 2026 (LAB-11).
  - Rulings in 2024–2026 mean that "ya no basta con estudiar únicamente la carta de despido" (looking only at the dismissal letter is no longer enough) (LAB-11).
  - Tariff-fixed compensation (STS 1350/2024; STS 736/2025) makes the money side predictable enough to automate (LAB-09).
- **Alternatives today:**
  - Gestorías, graduados sociales and labour lawyers (fees not found).
  - Law-firm guidance articles (Augusta Abogados).
  - SMAC settlements and settlement agreements (LAB-09, LAB-11).
  - No dedicated SME tool found (LAB-11).
  - General legal subscriptions such as Legálitas: €16.92–45.50/month on promo pages, one plan excludes business matters, and reviews complain about cancelling (software table).
- **Price hypothesis:**
  - €49 per termination for owners.
  - €79/month for advisers, with unlimited cases and their own branding.
  - Optional fixed-fee review by a partner graduado social, €90–150 (hypothesis).
- **Channels:**
  - Colegios de Graduados Sociales; the Madrid and Barcelona colleges are active on these topics (LAB-05, LAB-10, LAB-15).
  - ASNALA (the labour lawyers' association) and gestorías.
  - HR-suite marketplaces.
  - Search terms: "carta de despido disciplinario", "audiencia previa despido disciplinario", "preaviso despido objetivo cotiza", "calcular indemnización despido improcedente".
- **Build notes:**
  - *Rules:* a rules engine kept current with case law and TGSS bulletins.
  - *Integrations:* salary and seniority imported from payroll exports (a3innuva and similar, LAB-21).
  - *Data:* incapacity cases involve health data, a special category.
  - *Legal:* disclaimers and a professional-review option to stay clear of activities reserved to licensed professionals (validate).
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** low to medium. Letters and calculators alone are trivially copyable. The edge is:
  - a rules engine kept current (case law moves fast, LAB-11);
  - a network of graduados sociales for reviews;
  - outcome data on which files held up.
- **Key risks and kill criteria:**
  - *Risks:*
    - owners often act on impulse and call the adviser afterwards;
    - advisers already have templates;
    - liability if a tool-built dismissal is ruled null.
  - *Kill if:* fewer than 1 in 5 interviewed advisers would pay €79/month, or owners convert at under 2% at the moment of need.
- **Evidence strength:** medium. Claim volumes and the new rulings are well sourced (LAB-09, LAB-11), but neither the share of dismissals lost on fixable procedural defects nor adviser fees are quantified.
- **Validation questions:**
  1. What do gestorías, graduados sociales and labour lawyers in Madrid, Barcelona and Valencia charge to prepare a dismissal and attend SMAC?
  2. Competitors: search "software despidos graduados sociales" and "generador carta de despido"; check whether a3innuva, Sage, Factorial or Sesame include termination workflows, and which free severance calculators exist.
  3. Verify the pre-dismissal hearing ruling (reported as STS of 18 Nov 2024, unverified) and any 2026 refinements.
  4. Reserved activities: may software generate dismissal letters for employers without a licensed professional? Ask the Consejo General de Graduados Sociales and a bar association.
  5. SMAC volumes and settlement rates (MITES conciliation statistics; the 2025 PDF returned an error).
  6. Is there any data on how many unfair-dismissal (improcedente) rulings stem from procedural defects rather than substance?

### G2-I04: Labour compliance pack for micro employers (time records, RD 723 statements, protocols, inspection vault), white-labelled for gestorías
- **Type:** A (primary), against Sesame, Factorial and Kenjo for micro firms. Secondary C: a low-touch subscription.
  - On price it is level with Woffu Lite and Holded's HR add-on, so it must win on the compliance bundle and the gestoría channel.
- **Buyer:**
  - *Who pays:* owners of micro employers (1–10 staff) and autónomos with employees in hospitality, retail, care, cleaning and building services. They are reached mainly through their gestorías, whose labour departments resell the product (LAB-01, LAB-24).
  - *How many:* the Consejo de Estado counts 1.35M employer companies (LAB-01). INE's business register (DIRCE) implies about 1.51M businesses with employees (45.6% of 3,310,824, my arithmetic; ADM-06). The two bases differ, and the notes do not give the micro share — validate.
- **Pains addressed:** LAB-01, LAB-02, LAB-14, LAB-15, LAB-18, LAB-20, LAB-12, LAB-24
- **Problem:** From the first employee, an employer must keep daily time records for 4 years, give every new hire a detailed RD 723/2026 statement before day one (since 5 Oct 2026), have harassment procedures and occupational-risk prevention (PRL) in place, and produce all of it when the Labour Inspectorate (ITSS) asks (LAB-01, LAB-15, LAB-18, LAB-20, LAB-12). Enforcement is at a record — €858M in proposed sanctions in 2025 and 11,824 anonymous complaints — and without a record a worker's concrete overtime claim can be taken as true (STS 372/2026) (LAB-12, LAB-02). The leading HR suites fit micro firms poorly: Sesame's 15-employee minimum means a 3-person firm pays for 15 (€71.25/month at €4.75), and Factorial and PayFit draw complaints about support (LAB-24; software table).
- **Product:**
  - *What it does:*
    - Clock-in by app, WhatsApp link or a QR code at the door. The log is tamper-evident, every correction records who, when and why, workers can see their own records, and the inspection export already matches what the draft decree would require (LAB-01).
    - Alerts on overtime and on part-time hours that drift from the contract, plus a log of call-ups for fijos discontinuos (permanent seasonal staff) (LAB-02, LAB-14).
    - An RD 723 statement generator (LAB-15):
      - builds each statement from contract and convenio data;
      - delivers it electronically with acknowledgment;
      - sends change notices by the day each change takes effect;
      - tracks the 30-working-day deadline for requests from existing staff.
    - A harassment-protocol template with a log of staff acknowledgments, and an LGTBI template for any gestoría client above 50 workers (LAB-18).
    - Prevention documents for firms legally allowed to self-manage (up to 10 workers, or 25 with one workplace, outside Annex I), plus heat-episode reminders (LAB-20).
    - An "inspection-ready" document vault with a checklist for answering an ITSS request (LAB-12).
    - A monthly export of incidents (absences, overtime, sick leave) to the gestoría (LAB-21).
  - *MVP (about 6 weeks):*
    - clock-in with audit trail and inspection export;
    - the RD 723 generator with e-delivery;
    - the document vault;
    - a gestoría console for 20 client companies.
  - *Deliberately not:* payroll calculation (the gestoría keeps that), health surveillance (it needs a medical service, LAB-20), biometrics, or legal advice.
- **Why now:**
  - RD 723/2026 has applied to all employers since 5 Oct 2026 (LAB-15).
  - The digital time-recording decree is still a draft, which is an N3 risk for that part (LAB-01):
    - the Consejo de Estado's opinion was unfavourable;
    - approval was postponed in July;
    - it was absent from the October agendas.

    It can still be approved before 29-N. A 6- or 12-month transition for SMEs is under discussion, which would set a hard deadline around mid-to-late 2027.
  - Enforcement is intensifying now (LAB-12).
- **Alternatives today:**
  - *Tools and prices* (LAB-01, LAB-24; software table):
    - Woffu Lite, from €1.5 per user per month for up to 10 employees.
    - Sesame, €4.75–8 per employee (annual billing), with a 15-employee minimum.
    - Factorial, from €5–5.5 per person; Rework puts Core from US$8, with other modules by quote.
    - Kenjo, €6–10 per employee.
    - Holded's HR add-on, €1.50 per employee.
    - Timu (Nimbo), priced by headcount.
    - Signaturit e-signature, from €35 per user per month for 5 envelopes.
    - Gestoría contract packs.
    - Paper and Excel, which remain legal.
  - *Weaknesses:* seat minimums, modular upsells, ticket-only or slow support, cancellation friction (LAB-24; software table), and no documented RD 723 workflow.
  - *Why cheaper is viable* (inference):
    - a narrow scope;
    - no field sales, because the gestoría channel does the selling;
    - the gestoría acting as first-line support keeps support costs down.
- **Price hypothesis:**
  - €6/month flat for up to 3 employees, then €1.5 per extra employee. Billed monthly, with online cancellation.
  - Gestoría white-label at €1 per employee per month wholesale.
- **Channels:**
  - Gestorías as white-label resellers. In Spain the adviser often chooses the software; the software table calls a3 "la opción obligada si tu asesor externo lo usa" (the obligatory choice if your external adviser uses it).
  - Hospitality, retail and cleaning associations.
  - Administradores de fincas (property managers), for comunidades (residents' associations) that employ caretakers and cleaners. The Consejo de Estado flagged caretakers as a hard case for digital records (LAB-01).
  - Search terms: "registro horario autónomo gratis", "fichaje empleados WhatsApp", "modelo información RD 723/2026".
- **Build notes:**
  - *Integrations:* exports to or integration with a3innuva (which Sesame already integrates with), Nominasol and Sage (LAB-21, LAB-24).
  - *Proof of delivery:* qualified timestamps.
  - *Data:* employees' personal data. Location tracking should be limited, because the data-protection agency (AEPD) and the Consejo de Estado raised data-protection concerns (LAB-01).
  - *If the decree passes:* records must be technically unalterable and open to remote ITSS access (LAB-01).
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** none on the product. HR and time-tracking apps are commoditised and quick to clone. The only edges are distribution through gestorías and compliance content kept current.
- **Key risks and kill criteria:**
  - *Risks:*
    - Woffu Lite and Holded already sit at €1.5 per employee;
    - if the decree dies, demand stays trigger-based (an inspection or a lawsuit), because paper remains legal;
    - gestorías may prefer the client portal of their payroll vendor.
  - *Kill if:*
    - a3innuva or another major payroll suite already gives gestorías an equivalent client portal at no extra cost; or
    - a 10-gestoría pilot converts fewer than 15% of their employer clients within 3 months.
- **Evidence strength:** strong on obligations and enforcement (BOE, ITSS, Supreme Court; LAB-01, LAB-12, LAB-15). Willingness to pay is the open question.
- **Validation questions:**
  1. Do a3innuva (Wolters Kluwer), Sage or Nominasol (DELSOL) give gestorías a client portal with time recording and RD 723 statements, and at what price?
  2. Confirm Woffu Lite's limits at €1.5, the scope of Holded's HR add-on and Timu's prices, and check for free time-recording apps.
  3. Was the digital time-recording decree approved after 23 Oct 2026, and with what transition period and technical requirements?
  4. Did SEPE (the public employment service) publish the RD 723 model document? Do LISOS sanctions (the labour-infringements law) apply to missing statements, given that the decree sets none?
  5. How many businesses have 1–2, 3–5 and 6–9 employees (INE DIRCE)? Is there a survey of how many still record hours on paper?
  6. How do administradores de fincas handle time records for comunidades' staff, and how many comunidades employ staff?
  7. Gestoría economics: would they resell at €1 per employee per month, and what do they charge clients today for contracts and RD 723 statements?

### G2-I05: Work-permit expiry monitor and right-to-work file for employers
- **Type:** C (primary). Secondary B: a multi-client board for gestorías and immigration lawyers.
- **Buyer:**
  - *Who pays:* the owner or admin person at employers of non-EU workers in agriculture, hospitality, care (including domestic employers), construction and logistics, and the gestorías and immigration lawyers who handle their files (LAB-08, ADM-10).
  - *How many:* unknown — validate. Foreign workers were 14.1% of Social Security contributors at the end of 2025 (search snippet only, ADM-10).
- **Pains addressed:** LAB-08, ADM-10
- **Problem:** In 2025 the Labour Inspectorate found 18,655 foreign workers without authorisation (+53.1%) and proposed €187.7M in fines, about €10k per worker (LAB-08, inference). Immigration offices are slow and inconsistent — Zaragoza averages six months after a 25% workload rise, and the Ombudsman reports "graves consecuencias… también para sus empleadores" (serious consequences… also for their employers) — and the 2026 regularisation drew more than 1.17M applications whose cards and renewals now have to be tracked (LAB-08, ADM-10).
- **Product:**
  - *What it does:*
    - Keeps a register of each foreign worker's authorisation type, expiry date and conditions. Example: arraigo sociolaboral, a residence route for people already in Spain, requires a contract on the same terms as an initial permit (LAB-08).
    - Sends alerts at 120, 90, 60 and 30 days to both the employer and the worker, in the worker's language.
    - Provides office-specific renewal checklists, maintained with partner professionals (ADM-10).
    - Logs the employer's checks at hiring and at each renewal, as evidence for an inspection.
    - Gives gestorías one board across all their clients.
  - *MVP (3–4 weeks):*
    - spreadsheet import;
    - alerts and the verification log;
    - checklists for the offices with documented bottlenecks: Madrid, Zaragoza, Tarragona and La Rioja, plus Cádiz and Valencia, which the Ombudsman also names (LAB-08, ADM-10).
  - *Deliberately not:* filing applications, booking appointments (bots are N6, ADM-09), giving immigration advice, or screening candidates by nationality.
- **Why now:**
  - RD 1155/2024, the new immigration regulation, has applied since about 20 May 2025. Two interpretive criteria were issued a month apart, and challenges are pending at the Supreme Court (LAB-08, ADM-10).
  - The RD 316/2026 regularisation window closed on 30 Jun 2026, and resolutions and card issuance are ongoing (LAB-08).
  - The expat track's headings flag a "2027 renewal cliff" (EXP-03; timing to validate).
- **Alternatives today:**
  - For Madrid's online regularisation filings: immigration lawyers (58%), Correos (17%) and individuals (11%). No prices found (LAB-08).
  - Gestorías (LAB-08).
  - Spreadsheets.
  - HR suites may hold document-expiry fields — not documented, validate.
- **Price hypothesis:**
  - €5/month for up to 5 foreign workers, then €1 per extra worker.
  - €29/month for a gestoría or lawyer board covering up to 100 workers.
- **Channels:**
  - Immigration lawyers and gestorías, who filed most regularisation applications (LAB-08).
  - Farm cooperatives and agricultural associations.
  - Hospitality and care-provider associations.
  - Temporary-work agencies.
  - Multilingual SEO: "renovación permiso de trabajo empleado", "trabajador extranjero permiso caducado multa".
- **Build notes:**
  - *Integrations:* no official way for employers to verify authorisations is documented (validate).
  - *Data:* immigration status is sensitive personal data, so the product needs minimal fields, encryption and access logs.
  - *Notifications:* multilingual.
  - *Complexity:* low.
- **Moat in an AI-flooded market:** low. The reminder engine is trivially copyable. The edges are office-by-office checklists kept current with partner professionals, and distribution through those same professionals.
- **Key risks and kill criteria:**
  - *Risks:*
    - employers may see renewals as the worker's problem;
    - low willingness to pay;
    - HR suites add expiry alerts.
  - *Kill if:* fewer than a third of interviewed employers with 5 or more non-EU staff report a lapse, a near miss or worry about inspections in the past two years, or immigration lawyers won't distribute it.
- **Evidence strength:** medium. The fine and regularisation figures are official or reported from official sources (LAB-08), and the Ombudsman corroborates the harm to employers (ADM-10). Employer counts and the timing of renewals are unverified.
- **Validation questions:**
  1. How many employers have non-EU employees (Social Security affiliation by nationality and employer size)? Confirm the 14.1% share of contributors.
  2. What validity periods do authorisations granted under RD 316/2026 and the RD 1155/2024 arraigo routes carry, and when do first renewals peak? Cross-check EXP-03.
  3. What protects an employer while a renewal is pending (receipts, legal extensions), and how do inspectors treat it?
  4. Can employers check a worker's authorisation through any official online service?
  5. Competitors: immigration case software for law firms ("software extranjería despachos"), document-expiry alerts in HR suites (Factorial, Sesame, Woffu), and gestoría tools.
  6. What do gestorías and lawyers typically charge for a renewal?

### G2-I06: Machine-readable database and API of collective-agreement (convenio) rules
- **Type:** B
- **Buyer:**
  - *Who pays:*
    - the product and engineering leads at HR and time-tracking vendors (Factorial, Sesame, Woffu, Kenjo, Holded HR, Timu, PayFit) and payroll-software vendors;
    - the labour partners of gestorías and asesorías laborales (labour advisory firms);
    - employers operating in several provinces (LAB-21, LAB-22, LAB-24).
  - *How many:* the vendors are a handful, all named in the notes. The number of gestorías and labour advisers is unknown — validate.
- **Pains addressed:** LAB-21, LAB-22, LAB-03, LAB-05
- **Problem:** Pay, hours, holidays, leave and sick-pay top-ups depend on convenios that are often provincial, and courts keep reinterpreting entitlements: the per-event 5-day care leave has no annual cap (TS 753/2026), leave counts on the real length of a shift (TS, 27 May 2026), and two Audiencia Nacional rulings disagree on holidays that fall on rest days (LAB-21, LAB-22). Each year the minimum wage (SMI) must be tested against compensable supplements (LAB-03), and companies bore €16.1bn of sick-leave costs in 2025, partly through convenio top-ups (LAB-05, single source). Gestorías absorb all this churn at €15–20 per payslip (LAB-21).
- **Product:**
  - *What it does:*
    - A versioned dataset of convenio rules: pay tables by professional group, hours, holidays, leave entitlements, sick-pay top-ups, shift and night bonuses, and absorption rules.
    - Each rule carries its effective dates and a link to the source bulletin.
    - An API answers queries such as "entitlement for event X under convenio Y", "top-up due on sick day N" and "does worker Z pass the SMI absorption test?".
    - Change alerts fire when a convenio, a pay table or a ruling changes.
  - *MVP (8–10 weeks):*
    - the 30–50 convenios covering most workers in hospitality, retail, cleaning, construction and metalworking in Madrid, Barcelona, Valencia, Sevilla, Málaga and Bizkaia;
    - AI-assisted extraction, with legal review of every rule;
    - a web lookup for gestorías.
  - *Deliberately not:* running payroll, filing anything, or interpreting disputes.
- **Why now:**
  - RD 723/2026 statements must state the applicable convenio and pay items (LAB-15), which pushes HR tools to hold structured convenio data (inference).
  - The churn keeps rising: the retroactive 2026 SMI, the RED 8/2026 change, the 2025 birth-leave reform and the 2026 rulings (LAB-03, LAB-21, LAB-22).
- **Alternatives today:**
  - Gestorías on a3innuva and similar engines; the notes do not say whether these carry machine-readable convenio rules.
  - Employers' association circulars, e.g., FADE on the SMI (LAB-03).
  - Generic leave modules in HR suites, e.g., Sesame "Vacaciones y Ausencias" from €4.75 per employee (LAB-05).
  - Nominasol (DELSOL), with no public prices (software table).
- **Price hypothesis:**
  - API for vendors: €0.10–0.20 per covered employee per month.
  - Gestorías: €49–149/month, depending on client count.
- **Channels:**
  - Direct B2B sales to the HR and payroll vendors named above.
  - Gestoría associations and the Colegios de Graduados Sociales.
  - A partnership with an employers' association that already issues circulars.
- **Build notes:**
  - *Sources:* REGCON, the Ministry's register of convenios and equality plans (LAB-17), and provincial bulletins.
  - *Data quality:* AI extraction followed by legal QA, with versioning and an audit trail.
  - *Legal:* professional-liability insurance for errors.
  - *Complexity:* high, driven by coverage and maintenance.
- **Moat in an AI-flooded market:** strong if achieved. A validated, versioned dataset with vendor integrations is hard to copy. AI also cuts rivals' extraction costs, so the real barrier is accuracy and update speed.
- **Key risks and kill criteria:**
  - *Risks:*
    - incumbents (Wolters Kluwer a3, Sage, DELSOL) may already maintain convenio tables;
    - vendors may build their own;
    - liability for wrong rules.
  - *Kill if:* 3 of the 5 largest HR vendors say they already hold this data or won't pay for it, or a public source already publishes convenios in structured form.
- **Evidence strength:** medium. Rulings and gestoría pricing show the complexity (LAB-21, LAB-22), but the notes do not give the number of convenios or show that vendors lack the data.
- **Validation questions:**
  1. How many convenios are in force, how many are provincial, and how many workers do the top 50 cover (Ministry of Labour statistics; REGCON)?
  2. Does REGCON or any official source publish convenio content in a structured, machine-readable form?
  3. Do a3innuva, Sage, Nominasol and PayFit ship convenio pay tables and leave and sick-pay rules? Do Factorial, Sesame and Woffu rely on manual set-up?
  4. Existing convenio databases or APIs: search "API convenios colectivos" and "tablas salariales convenios actualizadas", and check legal publishers' convenio products.
  5. Will 2–3 HR vendors and 10 gestorías sign letters of intent at the proposed prices?
  6. What is the status of the announced decree-law barring the absorption of certain supplements, unverified as of Oct 2026 (LAB-03)?

### G2-I07: Complaint register with a 15-day clock and renewal notices for B2C businesses (Ley 10/2025), with a Catalan module
- **Type:** C
- **Buyer:**
  - *Who pays:* owners and managers of B2C SMEs — shops, gyms, academies, clinics, beauty and hairdressing, e-commerce and subscription startups (LEG-12).
  - *How many:* every B2C business; the notes do not count them — validate.
- **Pains addressed:** LEG-12, LEG-15
- **Problem:** Since 28 Dec 2025 every trader must give each complaint an ID key and a written receipt and answer it within 15 days, show the full final price including fees, notify customers 15 days before a renewal opt-out deadline, and state whether its reviews are verified (LEG-12). Most small businesses take complaints by email, phone or WhatsApp without logging them, so they cannot prove they complied (LEG-12, inference). In Catalonia, signs, menus, price lists, receipts and contracts must also be available in Catalan; language complaints rose from 206 (2021) to 1,873 (2023), with an average fine of €2,240 (LEG-15).
- **Product:**
  - *What it does:*
    - Takes complaints through a QR code at the counter, a web form, WhatsApp or forwarded email.
    - Issues the ID key and written receipt automatically.
    - Runs a 15-day clock with reminders and reply templates, and keeps a log that can be exported for inspectors.
    - Schedules renewal notices for subscription businesses.
    - Checks price display on one page and generates the review-verification statement (LEG-12).
    - Catalan module: Catalan versions of receipts, notices and standard texts, and a check of menus, price lists and signs — the fixed materials behind most sanctions (LEG-15).
    - Where a region requires official complaint forms (LEG-22, folded in here), it links to the official form instead of replacing it.
  - *MVP (about 3 weeks):* intake, ID key, receipt, clock, templates and renewal notices driven by CSV.
  - *Deliberately not:* replacing official regional forms, moderating reviews, or handling disputes.
- **Why now:**
  - The consumer-law amendments have been in force since 28 Dec 2025. It is unclear whether the 12-month adaptation period also covers them (LEG-12).
  - Large and basic-service firms face their own 28 Dec 2026 deadline (LEG-13), which should raise awareness among smaller businesses too (inference).
- **Alternatives today:**
  - Ad hoc email and Excel (LEG-12).
  - Helpdesk tools aimed at larger firms (LEG-12).
  - Lawyers updating terms and conditions (LEG-12).
  - For the language duty: manual translation, or Catalan versions supplied by brands (LEG-15).
  - No SME-specific product or prices found (LEG-12).
- **Price hypothesis:**
  - €5/month per location.
  - €9/month with renewal notices and the Catalan module.
- **Channels:**
  - POS, booking and gym-management software, as an embedded add-on.
  - Retail and hospitality associations, gestorías and consumer-law webinars.
  - In Catalonia, Catalan SME bodies such as Pimec (cited in ADM-12).
  - Search terms: "hoja de reclamaciones online", "plazo 15 días reclamación cliente", "Ley 10/2025 pymes reclamaciones".
- **Build notes:**
  - *Build:* simple forms, numbering, notifications and storage.
  - *Costs:* WhatsApp Business messaging is paid.
  - *Data:* customers' personal data.
  - *Complexity:* low.
- **Moat in an AI-flooded market:** none — speed only. Any developer could build it in days. The only lever is distribution, probably by selling it as a module to POS and booking vendors.
- **Key risks and kill criteria:**
  - *Risks:*
    - weak enforcement means weak willingness to pay;
    - POS and booking vendors add the feature themselves.
  - *Kill if:* fewer than 1 in 5 of 30 interviewed B2C owners has faced a consumer-office case or worries about the 15-day rule, or no regional authority has enforced the new duties by mid-2027.
- **Evidence strength:** medium. The duties are in the BOE (LEG-12) and Catalan enforcement is well documented (LEG-15), but how far the 15-day rule is enforced in practice is unknown.
- **Validation questions:**
  1. Does the 12-month adaptation period (transitional provision 1) cover the amendments to art. 21 of the consumer law (TRLGDCU)? What sanctions do the consumer laws of Madrid, Andalucía, C. Valenciana and Cataluña set?
  2. Have there been any inspections or fines in 2026 for missing ID keys or late answers? What are the complaint volumes at municipal consumer offices (OMIC) and consumer-arbitration bodies?
  3. Does Andalusia's mandatory electronic complaints system (HOS-17) already digitise the business side? What digital complaint forms do other regions use?
  4. Competitors: search "software gestión reclamaciones clientes pyme" and "libro de reclamaciones digital", and check whether POS, booking and gym tools have complaint modules.
  5. What do the 2025 Catalan language-enforcement figures show, and would Catalan businesses pay for the module?
  6. How many B2C SMEs are there by sector (INE DIRCE)?

### G2-I08: Call-consent ledger and 400-prefix compliance layer for SMEs that sell by phone
- **Type:** B (primary). Secondary C: a light per-agent plan.
- **Buyer:**
  - *Who pays:* sales managers or owners at energy and telecom resellers and agents, insurance agents and brokers, solar and efficiency installers, estate agencies, training providers, B2B sales teams and small call centres (LEG-11).
  - *How many:* not quantified — validate.
- **Pains addressed:** LEG-11
- **Problem:** Since 17 Oct 2026, operators have blocked commercial calls that do not come from numbers with the 400 prefix, and customer-service calls must use 800/900 numbers, short codes or geographic numbers (LEG-11). Contracts concluded in calls that break the unsolicited-call rules are presumed to lack consent and are void, and consent must be express and given within the two years before the call; a telephony vendor puts fines for misusing numbering at €50,001–€2M (LEG-11). By August 2026 the anti-scam plan had blocked 300M calls and 26.6M SMS (LEG-11).
- **Product:**
  - *What it does:*
    - A consent ledger: source, timestamp, scope, proof file and 2-year expiry for each consent.
    - A pre-dial gate that lets the 400 line call only numbers with valid consent.
    - A check against the Lista Robinson (the national advertising opt-out list) before each campaign.
    - Call-purpose tagging (sales or service), so each call goes out on the right number type.
    - A consent pack per contract, to defend against a claim that the contract is void (LEG-11).
  - *MVP (4–5 weeks):* the ledger, CSV and CRM import, the Robinson check, a webhook or API gate for one cloud dialler, and evidence export.
  - *Deliberately not:* assigning numbers (operators do that), acting as a dialler, or buying lead lists.
- **Why now:**
  - The numbering resolution took effect on 17 Apr 2026 with a 6-month adaptation period, and blocking has been live since 17 Oct 2026 (LEG-11).
  - Ley 10/2025 art. 16.3–16.4 also requires a separate prefix for commercial calls and operator blocking (LEG-11).
- **Alternatives today:**
  - Operators, which supply 400 ranges assigned by the CNMC (the competition and telecoms regulator).
  - Cloud telephony vendors such as Aircall, which publish guidance.
  - The Lista Robinson itself: free for citizens; companies sending personalised advertising without consent must check it.
  - Lawyers.
  - No prices were collected (LEG-11).
- **Price hypothesis:**
  - €19 per agent seat per month.
  - €5/month "consent vault" plan for single self-employed (autónomo) agents.
- **Channels:**
  - Cloud-telephony marketplaces.
  - CRMs used by insurance and energy agents.
  - Insurance-broker and energy-reseller networks.
  - B2B sales communities.
  - Search terms: "prefijo 400 llamadas comerciales", "consentimiento llamadas comerciales dos años", "Lista Robinson empresas".
- **Build notes:**
  - *Integrations:* diallers and CRMs.
  - *Lista Robinson:* the access terms for companies need checking.
  - *Data:* consent recordings are personal data, and LOPDGDD art. 23 on exclusion lists applies (LEG-11).
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** medium-low and time-limited. Integrations and regulatory know-how are the edge, but a telephony vendor could add a consent ledger natively.
- **Key risks and kill criteria:**
  - *Risks:*
    - it is unclear whether B2B calls and calls involving autónomos are covered (LEG-11);
    - telephony vendors or CRMs build the feature;
    - small sellers may simply stop cold-calling.
  - *Kill if:* the resolution does not cover B2B calls and B2C cold-calling collapses after blocking, or the two largest cloud-telephony vendors in Spain ship equivalent consent gating by Q1 2027.
- **Evidence strength:** medium. The rule and its dates are official (La Moncloa, BOE; LEG-11). The scope, the fine range (a vendor figure) and the number of affected SMEs are unverified.
- **Validation questions:**
  1. Find the BOE reference and text of the 400-prefix resolution, and confirm whether it covers B2B calls and calls involving autónomos.
  2. Confirm the vendor's claim that calls to a firm's own customer base are covered, and how the 2-year consent window in TRLGDCU art. 62.1 applies to existing customers.
  3. What are the Lista Robinson's access terms and fees for companies (it is run by ADigital)?
  4. Competitors: what consent-management or compliance features do Aircall and other cloud-telephony and CRM tools used in Spain offer? Search "software consentimiento llamadas comerciales".
  5. How many target businesses exist: insurance agents and brokers (register of the insurance supervisor, DGSFP), energy retailers (CNMC list), telemarketing firms?
  6. What has happened since 17 Oct 2026: blocked-call statistics, complaints from SMEs, voided-contract cases?

### G2-I09: Customer-service compliance kit for small basic-service providers (Ley 10/2025)
- **Type:** B
- **Buyer:**
  - *Who pays:* customer-service or compliance managers at small and medium internet and telecom providers, local water utilities, small electricity and gas retailers, bus, coach and ferry operators, and postal and courier firms. All are in scope regardless of size (LEG-13).
  - *How many:* not quantified. The notes infer "a few thousand SMEs at most" (LEG-13) — validate.
- **Pains addressed:** LEG-13
- **Problem:** By 28 Dec 2026 these firms must answer 95% of requests for a human within 3 minutes on average, never cut calls because of waits, issue complaint keys and resolve complaints within 15 working days (2 hours for service interruptions, 5 days for billing), serve customers in a co-official language on request, and pass an annual audit by an ENAC-accredited body (ENAC is Spain's national accreditation body) (LEG-13). Retailers below 5% market share are exempt only from the 24/7 line and the numbering rules, not from the 3-minute rule or the audit (LEG-13).
- **Product:**
  - *What it does:*
    - Connects to the provider's cloud phone system (PBX) and helpdesk.
    - Measures the 3-minute rule and the no-dropped-calls rule.
    - Issues complaint keys and tracks each type of deadline.
    - Tags requests for service in a co-official language.
    - Assembles the evidence pack the auditor will ask for, with alerts when a metric drifts.
  - *MVP (6–8 weeks):* connectors for 2–3 common cloud PBXs plus email ticketing, a metrics dashboard, complaint-key issuing, and an audit-pack template agreed with one accredited auditor.
  - *Deliberately not:* staffing a contact centre, performing the audit, or translating calls.
- **Why now:** a hard deadline on 28 Dec 2026, then a recurring annual audit (LEG-13). Ley 10/2025 is already law, so the dissolution of the Cortes does not affect it.
- **Alternatives today:**
  - Contact-centre suites built for large firms (LEG-13).
  - Advisory and audit firms (TÜV SÜD, KPMG) (LEG-13).
  - No SME pricing found (LEG-13).
- **Price hypothesis:**
  - €199–499/month, depending on call volume.
  - A €1,000 onboarding and audit-preparation fee.
- **Channels:**
  - Associations of small operators and energy retailers (still to be identified).
  - ENAC-accredited audit bodies, as referral partners.
  - Cloud-PBX vendors.
  - CNMC registers as lead lists.
  - Search terms: "Ley 10/2025 atención a la clientela auditoría", "3 minutos atención humana ley".
- **Build notes:**
  - *Integrations:* call-record (CDR) data from the phone system.
  - *Data:* customers' personal data.
  - *Audit method:* the auditors' measurement method must be confirmed first.
  - *Scope:* financial services and telecoms are governed first by their own sector rules, which may change the scope for internet providers (LEG-13).
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** medium-low. The edge is regulatory know-how, relationships with auditors, and being first before 28 Dec 2026. Once the market is known, copying is easy.
- **Key risks and kill criteria:**
  - *Risks:*
    - the market is small;
    - existing helpdesks may already report these metrics;
    - auditors may supply their own templates;
    - the deadline could be extended.
  - *Kill if:*
    - fewer than about 500 SME providers remain in scope after the sector-rule carve-outs; or
    - auditors accept standard helpdesk reports.
- **Evidence strength:** medium. The obligations are in the BOE and in law-firm summaries (LEG-13), but the number of SMEs in scope and the cost of the audit are unknown, and the €100,000 fine figure is an unverified vendor snippet.
- **Validation questions:**
  1. How many firms fall under art. 2.1 regardless of size? Check the CNMC registers of telecom operators and energy retailers, transport-operator registers and municipal water companies. How many of them are SMEs?
  2. Do internet providers follow Ley 10/2025, or their own sector rules on user rights first?
  3. Which standard or method will ENAC-accredited auditors apply, and what will the annual audit cost?
  4. Has any guidance defined how to measure the 95%-within-3-minutes rule?
  5. Competitors: search "software cumplimiento Ley 10/2025" and "auditoría atención al cliente ENAC"; check whether the cloud PBXs sold to small internet providers already report these metrics.
  6. Is there any sign that the 28 Dec 2026 deadline will be extended?

### G2-I10: CCTV compliance kit with a ready response pack for data-protection complaints
- **Type:** C
- **Buyer:**
  - *Who pays:* owners or managers of shops, bars and restaurants, workshops, gyms and offices that run cameras, plus residents' associations (comunidades) through the property managers who run them (administradores de fincas) (LEG-06).
  - *How many:* unknown — validate.
- **Pains addressed:** LEG-06, LEG-05
- **Problem:** In 2025 video surveillance was the second-largest complaint area at the AEPD, Spain's data-protection authority (4,050 complaints, +19%), and the area with the most finished procedures (81). Typical cases involve cameras aimed at the street or a neighbour, missing signs and indefinite retention (LEG-06). Complaints overall rose 64% to 30,931, procedures take 45% longer and 76% of appeals to the Audiencia Nacional fail, so even a small case is slow and costly to fight (LEG-05).
- **Product:**
  - *What it does:*
    - Guided set-up with a photo of each camera's view and a checklist: does it capture the street, neighbours, staff areas or audio?
    - Generates the warning sign, the staff notice and the entry in the record of processing activities.
    - Reminds the owner about the 30-day retention limit and an annual re-check.
    - Keeps an evidence vault. If a letter from the AEPD arrives, it assembles a response pack from that evidence (LEG-06, LEG-05).
  - *MVP (2–3 weeks):* web wizard, sign and notice PDFs, record entry, reminders and evidence vault, plus an installer edition that sets up each client at installation.
  - *Deliberately not:*
    - installing or re-aiming cameras;
    - representing the business before the AEPD;
    - certifying compliance.
- **Why now:**
  - AEPD complaint volumes are at a record and its procedures are overloaded in 2025–2026.
  - AEPD fines in commerce, transport and hospitality rose 1,653% to €10.76M (LEG-05).
  - The AEPD updated its video-surveillance guide in February 2025 (LEG-06).
- **Alternatives today:**
  - The free AEPD guide and free AEPD tools: Facilita (51,979 accesses) and Gestiona RGPD (29,304) (LEG-05, LEG-06).
  - Templates from camera installers.
  - Data-protection consultancies: PymeLegal claims more than 5,000 clients and publishes no prices (LEG-10).
  - Lawwwing, at €9.9–79/month, which focuses on websites (LEG-05).
- **Price hypothesis:**
  - €29 one-off set-up, plus €2.90/month for the vault, updates and response pack.
  - Installers: €1 per site per month, wholesale.
- **Channels:**
  - CCTV and alarm installers, bundling the kit at installation.
  - Administradores de fincas.
  - Hospitality associations.
  - Gestorías that bundle data protection.
  - Search terms: "cartel videovigilancia AEPD", "cámara apunta a la calle multa", "registro actividades videovigilancia".
- **Build notes:**
  - *Data:* photos of camera views can contain personal data, so the product acts as a data processor with tight retention.
  - *Automatic photo check (optional):* it would need care, so that it does not give false assurance.
  - *Complexity:* low.
- **Moat in an AI-flooded market:** none on the software, which is trivially copyable. Installer partnerships are the only edge.
- **Key risks and kill criteria:**
  - *Risks:*
    - little ongoing value once the sign is printed, so churn is likely;
    - the AEPD could add a CCTV module to its free tools;
    - small CCTV cases may end in warnings rather than fines.
  - *Kill if:*
    - AEPD resolutions show that typical small-business CCTV cases end in warnings or fines under €500; or
    - installers will not bundle the kit.
- **Evidence strength:** medium. Complaint and procedure volumes are well sourced (LEG-05, LEG-06), but fine amounts for small CCTV cases were not found.
- **Validation questions:**
  1. What are the typical AEPD outcomes and fine amounts in small-business video-surveillance cases (sample 2025–2026 resolutions)?
  2. Does Facilita or another free AEPD tool already generate CCTV signs and records?
  3. How many businesses and comunidades run CCTV (security-industry or AEPD data)?
  4. Would installers bundle a compliance kit, and what do they give clients today?
  5. Competitors: search "kit RGPD videovigilancia" and "cartel zona videovigilada descargar", and check data-protection SaaS for CCTV modules.
  6. Can a software provider prepare an AEPD response pack without that counting as legal representation?

### G2-I11: Pre-lease "can I open here?" check and file builder for opening premises (Madrid first)
- **Type:** B (primary). Secondary A: a cheap first pass before paying €500–1,000 for a compatibility certificate from a licensing ECU.
- **Buyer:**
  - *Who pays:* entrepreneurs opening premises in hospitality, retail, personal services and clinics; franchise expansion managers; commercial estate agents; and the architects and engineers who prepare licensing files (ADM-01, ADM-03).
  - *How many:* Madrid handled 13,301 declaraciones responsables (self-declarations that let a business open before inspection) and licences in 2025 (ADM-01). National openings: unknown — validate.
- **Pains addressed:** ADM-03, ADM-01
- **Problem:** Businesses sign leases and start works before knowing whether their activity is allowed at the address. In Madrid, the council's own service standards set an average of 109 days to check a declaración responsable and 137 days to grant a licence, so owners operate exposed for months (ADM-01, ADM-03). Certainty is expensive: €500–1,000 for a compatibility certificate from an ECU (Madrid's private licensing collaborating entities), or €600–1,250+ for an ECU-managed file, plus inspection visits (€190–1,080), municipal fees and the 4% construction tax (ICIO); in València, the compatibility certificate went from 15–45 days to more than a year for large projects (2023 data) (ADM-01, ADM-03).
- **Product:**
  - *What it does:*
    - The user enters the address, the activity and the floor area.
    - The tool gives a preliminary verdict — allowed, conditional, needs a licence, or not allowed — based on the city's planning rules and Ordenanza 6/2022 (ADM-01, ADM-03).
    - With the verdict comes:
      - the procedure and the documents required;
      - a cost estimate from the regulated ECU price table and the ICIO;
      - the council's standard timelines;
      - a one-click referral to one of Madrid's 19 ECUs or to an architect.
  - *MVP (6–8 weeks):* Madrid only, the 20 most common activities, answers within 48 hours, with a planning expert reviewing each AI-drafted answer.
  - *Deliberately not:*
    - issuing binding certificates;
    - signing projects (a qualified technician, técnico competente, must);
    - filing anything with the council.
- **Why now:**
  - Madrid approved its 2027 ECU prices on 15 Oct 2026 (ADM-01).
  - València has been drafting a new licensing ordinance since May 2025, aligned with Ley 6/2024 de Simplificación Administrativa (ADM-02 context; approval status unknown).
- **Alternatives today:**
  - ECU urban-compatibility certificate (certificado de adecuación urbanística): €500 (up to 100 m²), €700 (up to 200 m²) or €1,000 (up to 300 m²) (ADM-01, ADM-03).
  - ECU-managed declaración responsable: from €600 (ADM-01, ADM-03).
  - The council's paid urban-planning consultation (fee not retrieved) (ADM-01, ADM-03).
  - Architects and engineers (fees not found) (ADM-01, ADM-03).
  - ALU, Málaga's free online licensing assistant (ADM-01, ADM-03).
  - Gestorías (ADM-01, ADM-03).
  - *Weakness:* every option is slow or paid, and only works once the business already has specific premises in mind.
- **Price hypothesis:**
  - €49 per address check.
  - €149 with the full file checklist and the cost and timeline estimate.
  - €199/month for agents and franchise teams (10 checks a month).
- **Channels:**
  - Commercial estate agents and property portals (cross-group with RET-02).
  - Franchise associations and hospitality associations.
  - ECUs and architects, with referral fees both ways.
  - Search terms: "qué licencia necesito para abrir un bar en Madrid", "compatibilidad urbanística local", "licencia de actividad local Madrid".
- **Build notes:**
  - *Data:* machine-readable planning (PGOU) and zoning data for each city.
  - *Rules:* a rules engine for the licensing ordinance.
  - *Liability:* clear disclaimers, and probably professional-liability insurance.
  - *Complexity:* medium-high per city.
- **Moat in an AI-flooded market:** medium. Each city is slow to model, and the edge is a city-by-city rules dataset plus a network of reviewing professionals and ECU partnerships.
- **Key risks and kill criteria:**
  - *Risks:*
    - liability for a wrong preliminary verdict;
    - cities may extend free assistants like ALU;
    - one-off purchases make customer acquisition expensive.
  - *Kill if:*
    - Madrid's planning data cannot be obtained in usable form; or
    - ECUs and architects already give the same answer free as lead generation.
- **Evidence strength:** medium. Madrid's standards and regulated prices are official (ADM-01), but actual 2025 delays and the size of the pre-lease problem are not quantified (ADM-03).
- **Validation questions:**
  1. Is Madrid's planning and land-use data available as open GIS data? Same question for Barcelona, Valencia, Sevilla and Málaga.
  2. How did Madrid actually perform in 2025 against its 109-day and 137-day standards, and what share of files went through ECUs?
  3. What do Madrid's paid urban-planning consultations cost, and how fast are they?
  4. What does Málaga's ALU do, and how much is it used? Do other cities have similar tools?
  5. Competitors: search "informe viabilidad local comercial online" and "consulta compatibilidad urbanística online", and check the ECUs' own pre-checks.
  6. How many openings a year in the big cities fail, or receive requirements after opening?
  7. Would franchise expansion teams and commercial agents pay €199/month?

### G2-I12: Grant justification and repayment-risk workspace
- **Type:** B
- **Buyer:**
  - *Who pays:*
    - finance leads or owners at SMEs and autónomos with direct grants (energy efficiency, EV charging, hiring, digitalisation, strategic-project lines);
    - grant consultancies, as white-label users;
    - installers who apply and justify on the beneficiary's behalf as participating firms (ADM-14, ADM-15).
  - *How many:* NextGenerationEU (NGEU) has 1.46M beneficiaries, 70% of them micro firms and SMEs. Most of these are Kit Digital vouchers, whose paperwork the digitalisation agents handled (ADM-14, ADM-12). How many beneficiaries manage their own justification is unknown — validate.
- **Pains addressed:** ADM-14, ADM-15
- **Problem:** The EU Recovery Facility's milestone deadline (31 Aug 2026) has passed and Spain has filed its final €25,861M payment request, so the risk now shifts to justification and repayment; companies cite "excesiva carga administrativa" (excessive administrative burden) and deadlines out of step with investment cycles (ADM-14). In 2025 payments reached only 18.7% of available credits and SMEs received 43% of awarded funds, while MOVES III (EV and charging grant) files stall when the participating installer stops responding (ADM-14, ADM-15).
- **Product:**
  - *What it does:*
    - The user uploads the award resolution and the call's rules (bases).
    - AI extracts obligations, deadlines, eligible costs and evidence requirements into a checklist and a calendar.
    - An evidence vault maps invoices, proofs of payment, contracts and publicity photos to each obligation.
    - It builds the justification package and flags repayment risks: missing evidence, late payments, approaching deadlines.
    - Beneficiaries can see the status of files that an installer or consultant manages for them (ADM-14, ADM-15).
  - *MVP (about 6 weeks):* a generic workspace plus templates for 5 high-volume programmes chosen during validation.
  - *Deliberately not:* finding grants (Fandit does that, ADM-16), applying for them, or defending repayment cases.
- **Why now:**
  - Justification continues through 2026–2028 (ADM-14).
  - CEOE, the main employers' confederation, asks for (ADM-14, ADM-15):
    - execution to run until 2028;
    - earlier justification guides;
    - easier corrections;
    - no repayment when delays are the administration's fault.
- **Alternatives today:**
  - Grant consultancies (fees not found) (ADM-14, ADM-15).
  - Fandit: tracks 81,665 grants for €56–600/month but does not process applications (ADM-16).
  - Installers and in-house teams (ADM-14, ADM-15).
- **Price hypothesis:**
  - SMEs: €19/month per active grant.
  - Consultancies: €149/month for up to 20 active grants.
- **Channels:**
  - Grant consultancies.
  - Installers (MOVES and energy grants).
  - Gestorías.
  - Cámaras de Comercio and regional employers' bodies.
  - Search terms: "justificación subvención", "cuenta justificativa", "reintegro subvención Next Generation".
- **Build notes:**
  - *Core technology:* document AI that reads calls and award resolutions.
  - *Integrations:* import of invoices and payments from accounting tools.
  - *Data:* financial documents are confidential.
  - *Complexity:* medium.
- **Moat in an AI-flooded market:** medium-low. Programme templates and consultancy distribution help, but the AI extraction itself is easy to copy.
- **Key risks and kill criteria:**
  - *Risks:*
    - the Recovery Facility wave fades after 2026–2028;
    - consultancies prefer their own processes;
    - programmes vary too much for templates to scale.
  - *Kill if:* fewer than a quarter of interviewed grant-holding SMEs manage justification themselves, or consultancies won't pay €149/month.
- **Evidence strength:** medium. The macro figures come from CEOE, citing EsadeEcPol and Funcas, plus the official recovery-plan site (ADM-14). The SME-level justification pain rests on qualitative complaints and the Ombudsman (ADM-15).
- **Validation questions:**
  1. How many non-Kit-Digital SME beneficiaries of NGEU and regional grants manage their own justification? Check the national grants database (BDNS).
  2. How many repayment proceedings were opened in 2025–2026? Check IGAE (the state comptroller) and the Tribunal de Cuentas (the court of audit).
  3. What do consultancies charge for justification, fixed or success-based?
  4. Competitors: search "software justificación subvenciones" and "gestión de subvenciones pymes"; check Fandit's roadmap and any grant features in accounting tools.
  5. Has execution or justification been extended to 2028 for any programmes?
  6. Which 5 programmes have the most SME beneficiaries justifying grants themselves in 2026–2027? Cross-check CON-07, CITY-01 and FIN-26.

### G2-I13: Autónomo contribution-band forecaster and regularisation alarm
- **Type:** C
- **Buyer:**
  - *Who pays:* autónomos (self-employed natural persons) who pay Social Security under the real-income system (ADM-11).
  - *How many:* the proxy is 1,859,925 natural-person businesses (INE DIRCE 2025). Membership of RETA, the self-employed scheme, was not retrieved — validate.
- **Pains addressed:** ADM-11
- **Problem:** Under RDL 13/2022, the TGSS (the Social Security treasury) regularises each year's provisional contribution bases and sends resolutions demanding the difference. Prior claims are "generally not upheld", and the Ombudsman says the method wrongly excludes months of activity such as birth leave (ADM-11). Autónomos receive surprise bills they could have seen coming.
- **Product:**
  - *What it does:*
    - Takes monthly income and expenses, entered by hand or imported from invoicing tools.
    - Forecasts annual net income and the matching contribution band.
    - Alerts when the year-to-date trajectory crosses into another band.
    - Estimates the coming regularisation and suggests a monthly reserve.
    - Checks the TGSS resolution (months counted, leave periods) and offers a claim template (ADM-11).
  - *MVP (2–3 weeks):* manual entry, the band table, alerts, the regularisation estimator and the resolution checker.
  - *Deliberately not:*
    - filing the band change (the user or the gestoría does that);
    - preparing tax returns;
    - representing the user.
- **Why now:** regularisations were ongoing in 2025–2026. The Ombudsman's criticism appeared in its 2025 annual report, published in March 2026 (ADM-11).
- **Alternatives today:**
  - Gestorías (prices not found in this track).
  - Autónomo platforms in the software table:
    - Declarando, €29.90–99.90/month + VAT;
    - Cuéntica, €9–129/month;
    - Quipu with an adviser, from €80;
    - Billeo's online gestoría, from €65 + VAT (snippet).
  - Whether any of these forecast the contribution band is not documented.
- **Price hypothesis:** €3/month or €29/year, with a free one-off check as a lead magnet.
- **Channels:**
  - Integrations and marketplaces of invoicing apps.
  - Autónomo associations.
  - Gestorías, as a client-retention tool.
  - Content around "regularización cuota autónomos" and "qué tramo de autónomos me corresponde".
- **Build notes:**
  - *Data:* annual band tables; invoice import. Income data is sensitive.
  - *Complexity:* low.
- **Moat in an AI-flooded market:** none — speed only. It is a calculator that any invoicing platform can add.
- **Key risks and kill criteria:**
  - *Risks:* the TGSS's own tools, or the big autónomo platforms, may already do this.
  - *Kill if:*
    - the TGSS portal already offers a reliable simulator with alerts; or
    - Declarando, Cuéntica and Quipu already warn users about band changes.
- **Evidence strength:** weak in this track. There is a single source (the Ombudsman) and no amounts or counts (ADM-11). The tax track (TAX-12) may corroborate.
- **Validation questions:**
  1. RETA membership, and the number and average amount of regularisation demands for 2023–2025 (TGSS data).
  2. Does Import@ss, the TGSS online portal, or another TGSS tool offer a band simulator or alerts?
  3. Do Declarando, Cuéntica, Quipu or Holded forecast the band and warn users?
  4. How often may autónomos change band each year, and from which dates does a change take effect?
  5. Has the TGSS corrected the method the Ombudsman criticised?
  6. Merge check against TAX-12 and TAX-13 in the tax track.

### G2-I14: Small public-contract radar, including contratos menores (minor contracts)
- **Type:** B (primary), for buyer intelligence on minor contracts, which nobody aggregates. Secondary A, but only if incumbents' tender alerts prove expensive; their prices are not published.
- **Buyer:**
  - *Who pays:* owners and sales leads at micro and small suppliers of services, supplies and works — cleaning, maintenance, IT, consulting, events — that want public-sector customers (ADM-17, ADM-18).
  - *How many:* unknown — validate.
- **Pains addressed:** ADM-18, ADM-17
- **Problem:** Spain's 206,242 tenders in 2024 (€113.1bn base budget) drew 2.94 bidders on average, and 40.69% of awarded lots had a single bidder, more often in smaller contracts (ADM-17). Tenders sit on PLACSP (the national procurement platform) plus seven regional platforms whose data do not match, and there is no aggregated data at all on contratos menores — below €15,000 for services and supplies, €40,000 for works — which are the natural entry point for micro firms (ADM-18).
- **Product:**
  - *What it does:*
    - One feed of small tenders from PLACSP and the seven regional platforms, filtered by activity code, region and size.
    - A minor-contract database built from what contracting bodies publish, showing who buys what, from whom, how often and at what price.
    - Alerts for recurring purchases and for contracts nearing expiry (ADM-17, ADM-18).
  - *MVP (6–8 weeks):* PLACSP plus two regional platforms, and minor contracts for about 100 municipalities in two regions.
  - *Deliberately not:*
    - writing bids;
    - promising awards;
    - handling registration in ROLECE, the official register of bidders.
- **Why now:**
  - The latest report from OIReScon, the procurement watchdog (approved 22 Dec 2025), confirms both the data gap and the fragmentation (ADM-17, ADM-18).
  - The 2023–2026 National Public Procurement Strategy (Estrategia Nacional de Contratación Pública) is ending (ADM-17).
- **Alternatives today:**
  - licitaciones.es: alerts (including contracts nearing expiry), an AI assistant, competitor and buyer intelligence, and help with ROLECE. Free trial; no public prices.
  - Euroalert: focused on EU calls; no public prices.
  - Consultants (ADM-17, ADM-18).
- **Price hypothesis:** €19/month for one region; €39/month nationwide.
- **Channels:**
  - SEO on searches like "contratos menores [city] ayuntamiento".
  - Cámaras de Comercio and sector associations (cleaning, maintenance).
  - Gestorías.
  - Partnerships with bid writers.
- **Build notes:**
  - *Data:* ingesting and normalising heterogeneous public sources, under the terms for reusing public-sector data.
  - *Complexity:* medium-high.
- **Moat in an AI-flooded market:** medium. A proprietary, normalised minor-contract dataset would be hard to copy quickly; tender alerts on their own are commoditised.
- **Key risks and kill criteria:**
  - *Risks:*
    - minor contracts may be published too patchily to aggregate;
    - micro firms may avoid public clients because of late payment (FIN-04);
    - the alert market is crowded.
  - *Kill if:*
    - fewer than half of sampled municipalities publish minor contracts with supplier and amount; or
    - licitaciones.es already covers them.
- **Evidence strength:** medium. The metrics come from OIReScon, an official source (ADM-17, ADM-18); micro-firm demand and incumbents' coverage are unknown.
- **Validation questions:**
  1. What share of contracting bodies publish their minor contracts (object, amount, supplier), where, in what format, and what does the law require?
  2. What does licitaciones.es charge, and does it cover minor contracts? What other tender tools exist? Search "buscador contratos menores" and "alertas licitaciones pymes precio".
  3. Does PLACSP offer free alerts, and how good are they?
  4. What share of public contracts goes to SMEs in Spain? (The EU Single Market Scoreboard page returned an error.)
  5. Interview 20 micro suppliers in cleaning, maintenance and IT on willingness to pay and on late-payment fears (cross-check FIN-04).

### G2-I15: Client-obligation radar for gestorías ("which new rule hits which client")
- **Type:** B (primary), for gestorías and asesorías (advisory firms). Secondary C: a €5/month "what changed for me" digest for SMEs.
- **Buyer:**
  - *Who pays:* partners at gestorías, labour and tax asesorías, and graduados sociales (licensed labour advisers); directly, SMEs without an adviser (LAB-25, ADM-05).
  - *How many:* unknown — validate.
- **Pains addressed:** LAB-25, ADM-05
- **Problem:** Employers and their advisers must plan around rules that are announced, delayed, rejected, retroactive or reinterpreted — the 37.5-hour week rejected, the digital time-recording decree postponed, pay transparency overdue, RD 723/2026 effective 20 days after publication, a retroactive minimum wage (SMI) — and the 29-N election adds another layer (LAB-25). Official bulletins published over 1.32M pages in 2022, 80.8% of them regional, and the state alone approved 6 laws, 267 normative royal decrees and 17 decree-laws in 2025 (ADM-05).
- **Product:**
  - *What it does:*
    - A curated feed of items from the BOE, regional bulletins, the TGSS's RED bulletins (Social Security filing system) and key court rulings.
    - Each item is tagged with:
      - *who it hits:* size, activity code, region, convenio (collective agreement), B2C or B2B, and flags such as "sells by phone", "has CCTV" or "employs non-EU staff";
      - *its status:* draft, approved, in force or lapsed;
      - *its effective date.*
    - It maps each item to the gestoría's client list and produces per-client action lists and ready-to-send client messages.
    - A status board tracks pending items such as the time-recording decree (LAB-25, ADM-05).
  - *MVP (4–6 weeks):* labour and administrative obligations for SMEs, a monthly digest, and client mapping from a CSV.
  - *Deliberately not:* giving legal advice or replacing a legal database.
- **Why now:** the Cortes were dissolved on 6 Oct 2026 and elections are on 29 Nov 2026. Pending bills lapse, decree-laws await convalidation, and the Government can still approve regulations until it becomes a caretaker — an unusually heavy period for tracking rule status (LAB-01, LAB-25).
- **Alternatives today:**
  - Adviser newsletters (Grant Thornton, PwC) and training sessions at the Colegios de Graduados Sociales (LAB-25).
  - The "Novedades destacadas" bulletins of the Consejo General de Gestores Administrativos (LAB-03).
  - Trade associations and legal publishers (products and prices not verified, ADM-05).
  - None maps changes to each client.
- **Price hypothesis:** €49–149/month per gestoría, by number of clients; €5/month for SMEs.
- **Channels:**
  - Gestoría associations and professional colleges.
  - Marketplaces of practice-management software.
  - Webinars with the graduados sociales colleges.
  - Search terms: "novedades laborales gestorías", "alertas normativas por cliente".
- **Build notes:**
  - *Content:* editorial staff plus AI tagging, with accuracy controls.
  - *Integrations:* client import from practice-management software, starting with CSV.
  - *Complexity:* medium, mostly in content operations.
- **Moat in an AI-flooded market:** none on the feed; AI makes summaries nearly free. The possible edges are integrations that map items to clients, and editorial accountability.
- **Key risks and kill criteria:**
  - *Risks:*
    - legal publishers or payroll vendors add AI client mapping;
    - gestorías won't take on another subscription.
  - *Kill if:* fewer than 3 of 10 trial gestorías convert, or a3 or another practice suite ships client-level obligation alerts.
- **Evidence strength:** medium. The rule churn and the volume are well documented (LAB-25, ADM-05); willingness to pay is unknown.
- **Validation questions:**
  1. What do gestorías pay for legal-update services today, and does any of them map changes to their client lists?
  2. Do a3 (Wolters Kluwer) or other practice-management suites offer client-level obligation alerts?
  3. How many gestorías and asesorías are there? Check Consejo General de Gestores Administrativos membership and INE CNAE 69 (legal and accounting activities).
  4. Interview 15 gestorías: which 2026 changes cost them the most time, and how did they tell clients?
  5. Competitors: search "alertas normativas gestorías", "monitorización BOE IA" and "novedades legislativas por cliente".

---

## 5. Cross-group links

The other-track IDs below come from those files' headings only. They show where a later merge should look; they were not used as evidence here.

| Theme | G2 pains and ideas | Pointers in other tracks | Note for the merge |
|---|---|---|---|
| **MASC pre-litigation step (flagged cross-group theme)** | LEG-01, LEG-04, LEG-02, which feed I02 | FIN-06, FIN-07, FIN-08 (cash flow: MASC before claiming unpaid invoices, friction in fast-track debt claims (monitorio), uneconomic collection); CON-20, CON-23 (unpaid rent, evictions, community arrears); HOU-14 (defaulting temporary tenants); PRO-12, PRO-13 (small law firms, court reorganisation, LexNET) | Build one MASC product covering unpaid invoices, rent arrears and community arrears. Law firms are both channel and buyer, and landlords and collection agencies widen the market. |
| E-notifications, enforcement surcharges (apremio) and embargoes | ADM-08, ADM-07, which feed I01 | TAX-18, TAX-10 (tax: notification traps, surcharges); EXP-12, EXP-23 (expats: certificate chicken-and-egg, fragile e-filing stack) | TAX-18 may hold the embargo-frequency evidence I01 lacks. Foreigners without a residence card (TIE) cannot get certificates, a segment I01 cannot serve. |
| Misuse of digital signatures | ADM-07, plus filtered ADM-12 | VOX-17 | Supports the custody and usage-log feature in I01. |
| Micro-employer HR, time records and the gestoría channel | LAB-01, LAB-15, LAB-24, which feed I04; LAB-21, which feeds I06 | VOX-14, VOX-21 (the gestor decides the software), TAX-22, PRO-10, PRO-11 (gestorías' capacity and client migrations), HOS-01, PRO-18 (households as employers: risk assessment) | I04, I06 and I15 share the gestoría distribution thesis; validate it once, for all three. Domestic employers (PRO-18) could be a vertical. |
| Absenteeism | LAB-05, which feeds I06 | CITY-20, HOS-01 | Corroborates sick-leave cost; HOS-01 adds hospitality detail. |
| Talent shortage and housing | LAB-07 (filtered N2) | CITY-16, CITY-05, HOS-26, IND-03 | CITY-05 and HOS-26 may fill the labour track's housing-as-hiring-barrier gap. |
| Seasonal contracts (fijos discontinuos, permanent seasonal staff) | LAB-14, which feeds I04 | HOS-26, CITY-06 | The call-up log in I04 could become a hospitality or island vertical. |
| Foreign workers and permits | LAB-08, ADM-10, which feed I05 | EXP-01, EXP-03 ("2027 renewal cliff"), EXP-07, EXP-09, STA-10 | EXP-03 may time I05's demand wave; merge office-checklist evidence. |
| Consumer-law duties and complaints | LEG-12, LEG-15, LEG-22, which feed I07 | HOS-17 (Andalusia's mandatory electronic complaints system, Hoj@), HOS-24, RET-09 (30-day "previous price" rule on discounts), VOX-09 (auto-renewals) | Check Hoj@ before building I07. RET-09 and the renewal notice could share one "B2C rules" kit. |
| Online reviews | LEG-14 (filtered N1) | VOX-01, VOX-02, HOS-07 | Fold the duty to say whether reviews are verified (art. 20.4) into the review ideas there. |
| Data protection on premises, and breaches | LEG-05, LEG-06, which feed I10; LEG-09 (filtered) | PRO-08 (clinics' health data), VOX-04 (breaches at SaaS vendors) | Clinics could be a vertical for I10. |
| Phone sales and consent | LEG-11, which feeds I08 | VOX-05, VOX-06 (telecom contracts, energy mis-selling by phone) | Energy and telecom resellers are I08's likely first buyers. |
| Accessibility | LEG-16 (filtered N4) | RET-17 | Retail track owns it. |
| AI Act | LEG-17 (filtered N3) | STA-15 | Startup track owns it. |
| Opening premises and licences | ADM-01, ADM-03, which feed I11 | CON-06 (works licences), HOU-18 (coliving use and licences), HOS-05 (terraces), HOS-19 (Madrid licence freeze), RET-02 (commercial rent shocks) | The same city-rules dataset could also cover works licences and coliving use. |
| Grant justification | ADM-14, ADM-15, which feed I12; ADM-16 (filtered) | CON-07 (rehabilitation grants), CITY-01, CITY-02 (Valencia flood aid), CITY-09, FIN-26, STA-05, GAM-04 | Flood aid and rehabilitation grants are concrete verticals for I12. |
| Kit Digital aftermath | ADM-12, ADM-13 (filtered N3) | VOX-15, VOX-16, VOX-17, VOX-18, RET-07 | Treat as closed; keep only as context on SME distrust of subsidised software. |
| Public procurement | ADM-17, ADM-18, which feed I14; ADM-19 (filtered) | STA-13, PRO-17, FIN-04 (public-sector late payment), FIN-02, CON-05 (subcontracting chains) | Late payment by public bodies (FIN-04) may dampen demand for I14. |
| Autónomo contributions | ADM-11, which feeds I13 | TAX-12, TAX-13 | Likely the same idea as the tax group's; merge and keep the better-evidenced version. |
| Regulatory whiplash | LAB-25, ADM-05, which feed I15 | CITY-15, ZBE-02, CITY-19, PRO-11 | One obligation radar could span labour, tax, low-emission-zone (ZBE) and invoicing rules. |
| Company formation | ADM-06 (filtered N4) | STA-07, STA-08 | Startup track owns it. |
| Regional and municipal patchwork | ADM-04 (filtered N2) | CITY-12, CON-15 | Same structural pattern; no G2 idea. |
| Appointments | ADM-09 (filtered N6) | EXP-01, EXP-14 | Appointment bots stay out of scope (N6) in any merge. |

---

## 6. Group top 5

This is a shortlist for validation, not a final ranking.

1. **G2-I01, the e-notification watchdog.** It addresses the top administrative pain. The duty covers about 1.45M legal entities, carries a 10-day trap that ends in embargoes, and rests on split case law. It is a low-touch type C product, with an integration edge if active polling across sedes proves feasible (ADM-08, ADM-07).
2. **G2-I02, the MASC pre-litigation kit.** The requirement is in force but has no official channel, and 49.3% of surveyed Madrid lawyers report trouble proving the negotiation attempt. A paid market at €110–150 + VAT per file already exists to undercut, and demand is shared with the collection and landlord tracks (LEG-01, LEG-04).
3. **G2-I03, the guided dismissal workflow.** Dismissal claims are at a record and keep growing, and fresh procedural traps keep appearing. Each dismissal is a moment when owners will pay, and graduados sociales and gestorías give a ready channel (LAB-09, LAB-11).
4. **G2-I06, the convenio rules API.** This is the group's most defensible idea: a proprietary, maintained dataset that HR vendors and gestorías need and that AI cannot simply generate. Its weakness is that incumbents may already hold the data (LAB-21, LAB-22).
5. **G2-I05, the work-permit expiry monitor.** Proposed fines average about €10k per unauthorised worker, and the 2026 regularisation drew more than 1.17M applications. That makes a cheap, set-and-forget monitor easy to justify, and immigration lawyers can distribute it (LAB-08, ADM-10).

**Close calls:**
- **G2-I04, the micro-employer compliance pack:** the strongest obligations of all, but crowded and with no moat.
- **G2-I08, the call-consent ledger:** a hard switch on 17 Oct 2026, but its scope is unclear and telephony vendors could absorb it.
