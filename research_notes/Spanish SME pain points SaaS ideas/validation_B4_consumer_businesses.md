# Validation, batch 4 of 8: consumer-facing shops, hospitality and personal services

*Prepared 23 October 2026 (validation stage). Ideas: IDEA-14, IDEA-20, IDEA-21, IDEA-22, IDEA-23, IDEA-24, IDEA-37, IDEA-38, IDEA-39.*

*Method: the longlist (`stage2_idea_longlist.md`, sections 2, 5, 6.1 and batch 4), the group-file source blocks and the stage-1 evidence were read first. New evidence comes from direct fetches of official, vendor and review pages (unlimited) and from at most 24 web searches (log in section 4). Citations: [new: URL, date seen or published] for new evidence; [notes: PAIN-ID] for stage-1 evidence. "Single source" marks claims with one source only. Prices exclude VAT unless stated.*

*Status: work in progress. Ideas are appended as they are finished.*

---

## 1. Batch summary

(Filled in at the end.)

---

## 2. Ideas

#### IDEA-14: Review-attack alarm and evidence kit for local businesses — KILL (medium)

**Validated definition.** A €5–9/month monitor of a venue's Google (and, if access allows, Tripadvisor) reviews that detects bursts of 1–2-star reviews from new or empty profiles, alerts the owner, captures timestamped evidence and pre-fills Google's merchant extortion report, a police complaint and a TRLGDCU art. 20.4 removal request. Kill it as a standalone subscription: there is still no Spanish evidence that attacks are frequent; Google now runs its own extortion-report channel and defines the evidence it wants; review monitoring with alerts is sold for €0–19 a month or bundled into POS and booking suites; Tripadvisor access is partner-only; and there is no moat. Burst detection is a feature for review-management or POS vendors, not a business.

**(a) Problem reality and rule status**
- **Frequency is still unmeasured.** Search 18 found no police, OCU or association figures on review extortion or review bombing in Spain. The stage-1 evidence is anecdotal: one bar hit by about 20 reviews in under an hour, and offers of €200/month for 20 positive reviews [notes: VOX-01, VOX-02, HOS-07]. Search 18 did surface a TheFork Lab survey (July 2026, more than 6,000 diners): 62% drop a venue after reading bad reviews, and 10% admit writing reviews for a benefit the venue offered [new: Vinetur, 15 Jul 2026, search-result summary, page not opened]. CEHAT joined the European #StopFakeReviews campaign in April 2025 [new: cehat.com PDF "08042025 Stop Fake Reviews", search-result listing, not opened].
- **Legal basis.** TRLGDCU art. 20.4 as amended by Ley 10/2025 (in force 28 Dec 2025): traders must say whether they guarantee that reviews come from real buyers or users; reviews must concern products bought or used in the "treinta días naturales anteriores"; a trader may ask for removal of a fake review if it can prove the reviewer neither bought nor used the product [new: https://www.boe.es/eli/es/l/2025/12/26/10, DF tercera, seen 23 Oct 2026]. The "fines up to €100,000" for fake reviews come from Merca2 and were not checked against the BOE [notes: VOX-01].
- **Google has moved.** Google Business Profile Help has a page "Report negative review extortion scams on your Business Profile", with a merchant extortion report form. It asks for screenshots of the demands, links to the suspicious reviews, the scammers' identifiers and the timeline of the spike and the demand, and says the team "thoroughly investigates the claim and notifies you about the results". It covers only cases with a direct demand for money or favours [new: https://support.google.com/business/answer/16404809?hl=en-GB, seen 23 Oct 2026, undated]. Local-SEO practitioners report removals after using it (anecdotal) [new: seroundtable.com, search 22 listing, not opened]. Google therefore already defines and receives the "evidence pack" the idea proposed to build.
- Election risk: none.

**(b) Competitors**
- A vendor-published comparison (theStacc ranks itself first) lists review-management tools with prices: Reviux (reviux.app) Starter €19, Pro €49, Agency from €99 a month, with "alertas" in the Agency plan; Cinquo free up to 50 reviews, Starter €49.99 a year; Relvio €0–33.33 a month; Trustmary free plan, from €21 a month; EmbedSocial €0–80; Reputation $80 per location per month; Birdeye on quote. Its own summary: "Ninguna herramienta describe la detección de reseñas sospechosas o falsas de forma concreta" [new: https://thestacc.com/es/mejor/software-de-gestion-de-resenas/, updated 20 Aug 2026]. Note that reviux.com redirects to a domain-sale page; the product lives at reviux.app.
- Gastroranking (Madrid): "Análisis global y multicanal de reputación" with AI replies and custom reports; no public prices [new: https://www.gastroranking.es/, seen 23 Oct 2026]; it has a CoverManager integration [new: app.covermanager.com/en/integrations/gastroranking, search 19 listing].
- Bundled: Qamarero's Growth plan includes "gestión de reseñas" [new: https://www.qamarero.com/precios/, seen 23 Oct 2026]; Treatwell's plans include review management [new: https://www.treatwell.es/partners/precios/, seen 23 Oct 2026]. Partoo serves restaurant chains (search 19). OnbrandinG remains unpriced [notes: VOX-01].
- **Gap:** real but narrow. Nobody sells attack detection specifically, but the surrounding job (alerts, replies, reports) is cheap or free, and the evidence format is now set by Google.

**(c) Buyers and market size:** DIRCE 2025 food service 234,900 companies (restaurants 73,296; catering 14,751; bars 146,853) and accommodation 31,576 [new: INE table 39372, https://www.ine.es/jaxiT3/Tabla.htm?t=39372, CSV downloaded 23 Oct 2026]. Ceiling: 1% of food service at €7/month is about 2,350 × €84, or about €197k ARR.

**(d) Willingness to pay:** owners do spend on reputation (illegal paid reviews at €1.5–2.5 each or €200/month packages [notes: VOX-02]), but the legitimate tools above anchor monitoring at €0–19 a month. Paying monthly to insure against a rare event is a weak proposition.

**(e) Distribution:** POS and reservation vendors (Qamarero; CoverManager's integration marketplace), hospitality associations (CEHAT's campaign). Unproven.

**(f) Build and legal**
- Google: the Business Profile API lists all reviews of a location (`accounts.locations.reviews.list`, `batchGetReviews`) and replies to them (`updateReply`) after OAuth registration [new: https://developers.google.com/my-business/content/review-data, seen 23 Oct 2026]. Access needs approval ("If your quota limit for the Google Business Profile API is 0, you have not yet been granted access"); default 300 queries per minute; a Notifications API exists [new: https://developers.google.com/my-business/content/limits, seen 23 Oct 2026]. Monitoring an owner's own listings is therefore possible within Google's terms.
- Tripadvisor: the legacy Content API is deprecated ("This API is deprecated") [new: https://tripadvisor-content-api.readme.io/reference/overview, seen 23 Oct 2026]; its successor, Terra, is "a comprehensive content delivery platform for partners" with location allowlists, usage-based pricing and caching and review-implementation policies [new: https://docs.terra.tripadvisor.com/, seen 23 Oct 2026]. Whether monitoring or analytics is a permitted use was not established.
- MVP: 3–4 weeks plus the API approval wait. A certified-evidence partner is optional, since Google asks for screenshots.

**(g) Defensibility:** low. Any review tool can add burst detection, and Google's own process is improving.

**Type C check (~€5/month):** it can be automated with little support, but the monthly value is invisible in months without an attack, which is most months for most venues. It needs to be a free or €1–3 wholesale add-on inside a review, POS or booking product, or an on-demand incident service (hypothesis: €49–99 per attack response). Neither was tested.

**(h) Kill criteria**
- "Fewer than about 1 in 20 restaurants report an attack a year": **open**; still no data after searches in two stages.
- "Listing data cannot be monitored within platform terms": **not met for Google** (official API for owners, subject to approval); **open for Tripadvisor**.
- Top risk 3, "Google improves its own detection", has partly materialised: a dedicated extortion-report form exists.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 2 | Occasional event; no legal deadline. |
| S2 Buyers | 4 | About 235k food-service and 32k accommodation companies. |
| S3 Willingness to pay | 2 | Monitoring is €0–19 a month or bundled; insurance against a rare event. |
| S4 Reachability | 3 | POS and reservation marketplaces and associations exist; unproven. |
| S5 Competitive gap | 3 | Review tools are many; none detects attacks, but Google covers the report path. |
| S6 Build speed | 4 | 1–2 months including Google API approval. |
| S7 Defensibility | 1 | Trivially copyable. |
| S8 Retention | 2 | Passive monitoring with value only during attacks. |
| **Sellability** | **2.63** | |
| **P** | **2** | Painful when it happens, but no evidence it is frequent. |
| **Overall** | **2.38** | 0.6 × 2.625 + 0.4 × 2 |

**Open [I] checks:** a 50-venue survey through a hospitality association on attacks in the last 12 months and the revenue impact; a test application for Google Business Profile API access.

**What would change the verdict:** data showing at least 1 in 20 venues attacked a year with measurable revenue loss; a POS or reservation vendor wanting a white-label "attack shield"; Tripadvisor partner terms that allow monitoring.

---

#### IDEA-20: B2C complaint-clock and consumer-duty kit, with Hoj@ (Andalusia) and Catalan modules — KILL (medium)

**Validated definition.** A €5/month register for small B2C businesses: complaint intake with an ID key and written receipt, a 15-day reply clock (national, TRLGDCU art. 21), renewal notices, a Hoj@ deadline watcher for Andalusia (10 working days to reply, complaint deemed received 10 calendar days after notice) and a Catalan-language check of menus and signs. The duties are real and in force, but enforcement of the new clock is not visible, the per-business cost of non-compliance is small and rare, the free Hoj@ platform already handles Andalusian e-complaints end to end, and the product has no moat. Verdict: kill as a standalone product; keep the Hoj@ deadline watcher as a feature for gestoría, POS, booking or PMS products (see "what would change the verdict").

**(a) Problem reality and rule status (October 2026)**
- **Ley 10/2025 consumer duties have no adaptation period for ordinary SMEs (batch 4 owns this check; settles the section 5.2 item).**
  - The transitional rule is a *disposición transitoria única*, not a "first" one. Apartado 1 reads: "Las empresas incluidas en el ámbito de aplicación de la presente ley deberán adaptar sus servicios de atención a la clientela a las disposiciones de la misma en el plazo de doce meses desde su entrada en vigor" [new: https://www.boe.es/buscar/act.php?id=BOE-A-2025-26698, consolidated text seen 23 Oct 2026; BOE-A-2025-26698, BOE núm. 312, 27 Dec 2025].
  - "Ámbito de aplicación de la presente ley" is art. 2: basic-service providers of any size and large firms (at least 250 workers, or turnover above €50M, or balance sheet above €43M; the thresholds are alternatives) [new: same page].
  - The consumer-law amendments sit in *disposición final tercera* (TRLGDCU art. 20.1.c full price, art. 20.4 reviews from buyers within 30 days, art. 21.2 "una clave identificativa y un justificante por escrito", art. 21.3 reply "en el plazo máximo de quince días", art. 62.1 phone consent, art. 97.1.p 15 days' renewal notice). *Disposición final octava* puts the whole law in force the day after publication (28 Dec 2025); the only deferral is for language rules at credit cooperatives and savings banks [new: https://www.boe.es/eli/es/l/2025/12/26/10, seen 23 Oct 2026].
  - KPMG describes the 12-month regime as applying to "las entidades incluidas en su ámbito de aplicación", deadline 28 Dec 2026 [new: KPMG legal alert, Jan 2026, https://assets.kpmg.com/content/dam/kpmgsites/es/pdf/2026/01/legal-alert-regulacion-servicios-atencion-clientela-ley-10-2025.pdf.coredownload.inline.pdf, text extracted 23 Oct 2026].
  - **Conclusion:** for an ordinary shop, bar or salon, the complaint-key, 15-day, review and renewal-notice duties have applied since 28 Dec 2025. This is my reading of the BOE text, consistent with KPMG; I found no source arguing the opposite. The preamble's "seis meses" conflicts with the operative "doce meses"; the operative text governs.
  - **Awareness is poor, which cuts both ways.** The Comunidad de Madrid's consumer page tells businesses they have "doce meses para adaptarse" and lists the 3-minute rule as if general [new: https://www.comunidad.madrid/consumo/entra-vigor-nueva-ley-atencion-cliente, updated 5 Aug 2026]; other explainer pages say the law "entrará en vigor el 28 de diciembre de 2026" (search 6 results). Confused messaging means little felt pressure on micro firms.
- **Enforcement seen so far is of the old paper regime, and it is remedial.**
  - Madrid city's 2025 general establishment campaign: 2,541 first inspections plus 1,924 follow-ups; 67.8% had some irregularity; 12.7% had no complaint forms and 14.2% no official poster; after follow-up visits the irregular share fell to 16.8% [new: Instituto Municipal de Consumo, "Evaluación de la Campaña de Control General de Establecimientos 2025", https://www.madrid.es/UnidadesDescentralizadas/Consumo/EspecialInformativo/EspacioEmpresarios/02Inspecci%C3%B3n/Evaluaci%C3%B3nCampa%C3%B1asDeInspecci%C3%B3n_2026/EV_CGEstablecimientos2025.pdf, text extracted 23 Oct 2026].
  - Andalusia's 2026 campaigns check that complaint sheets and posters exist ("Control básico de establecimientos 2026") and complaint handling in web sales ("Contratación a distancia en web 2026") [new: consumoresponde.es campaign pages, via search 5, 23 Oct 2026; pages listed, not opened].
  - I found no inspection, campaign or fine aimed at the new ID key or the 15-day reply anywhere (searches 5 and 6).
- **Andalusia, Hoj@ (single-source issue settled from the BOJA).**
  - Orden de 24 de abril de 2026, "por la que se regula el Sistema de Hojas Electrónicas de Quejas y Reclamaciones", BOJA núm. 82, 30 Apr 2026, in force "a los 20 días de su publicación" (about 20 May 2026) [new: https://www.juntadeandalucia.es/boja/2026/82/1, seen 23 Oct 2026].
  - Registration is mandatory for every "empresa" selling goods or services in Andalusia: within six months for large firms (over 250 staff, over €50M turnover, over 20 establishments in Andalusia, basic services, public companies, concessions), about 20 Nov 2026; within one year for all others, about 20 May 2027 (DA tercera). At least two authorised persons per company, one for a sole trader [new: same].
  - Notice "a través del correo electrónico o de mensaje de la propia aplicación"; deemed received on access or after 10 calendar days; reply "en el plazo de diez días hábiles" (art. 16). The Order provides no pre-deadline reminders and no API or web service for company systems [new: same]. Chekin's summary matches [new: https://chekin.com/blog/boja-andalucia-nuevo-sistema-hoj-de-quejas-y-reclamaciones/, 9 Jun 2026]. Lawwwing's "20 February 2027" deadline for SMEs contradicts the BOJA's one-year term [new: https://lawwwing.com/nueva-normativa-hojas-reclamaciones-andalucia-hoja/, 12 Oct 2026].
  - Sanction: not replying in time is art. 71.8.3ª of Ley 13/2003 ("No responder en plazo las quejas y reclamaciones"), *leve* by default (art. 72.1), fined €200–5,000 (art. 74.1), or a reprimand with mitigating circumstances (art. 75) [new: https://www.boe.es/eli/es-an/l/2003/12/17/13/con, seen 23 Oct 2026].
- **Catalonia, language duty (settles C-19).** NacióDigital counts all case types (denúncies, queixes and comunicacions, Agència Catalana del Consum plus Política Lingüística): 666 in 2022, "més de 2.000" in 2023, about 1,250 in 2024; 6,145 files 2012–2024, of which 5,406 denúncies; 7% sanctioned (367, or 341 in the data section); average fine €2,240, maximum €10,000 (12 times); 29.9% of fines for fixed information, 25.5% for offers including menus; restaurants about half of cases [new: https://naciodigital.cat/societat/nomes-7-denuncies-vulnerar-drets-linguistics-consumidors-han-acabat-en-sancio.html, published 23 Mar 2025]. 3Cat's 1,873 for 2023 [notes: LEG-15] probably counts a narrower set of case types (my inference; 3Cat's definition was not re-read). The conflict is definitional, not factual. Even at 100 sanctions a year (367 over 13 years is about 28 a year), against about 178,000 B2C-facing companies in Catalonia (below), a sanction is a well-under-1-in-1,000-a-year event.
- **Election risk:** none. Ley 10/2025 and the Andalusian Order are in force; the dissolution does not touch them.

**(b) Competitors**
- No SME complaint-clock product found in two searches (searches 6 and 7). Law-firm explainers dominate the results.
- Lawwwing (compliance SaaS, €9.9–79/month for web legal texts [notes: LEG-05]) has published on both Ley 10/2025 and Hoj@ but sells no complaint or Hoj@ module as of 12 Oct 2026 [new: Lawwwing Hoj@ article above]. It is the most likely fast follower.
- Aunoa (conversational AI) markets "Cumple la Ley SAC de forma automática" to firms in the law's scope; no prices; enterprise focus [new: https://aunoa.ai/ley-de-atencion-al-cliente/, seen 23 Oct 2026].
- Free substitutes do the job for low volumes: the Hoj@ platform itself (intake, notices, reply channel and archive for Andalusian e-complaints), email plus a spreadsheet, and helpdesk free tiers (general knowledge, not re-verified in this pass).
- Bundling threat: POS, booking and PMS vendors can add a complaint log in days; Chekin already positions its unified inbox as a way to stop complaints becoming formal [new: Chekin article above].

**(c) Buyers and market size**
- INE DIRCE, companies at 1 Jan 2025, in B2C-facing CNAE groups (retail 47x, accommodation 55x, food service 56x, personal services 960, sport 931–932, other education 855, medical and dental 862, vets 750, car repair 452, travel agencies 791): **1,081,499 companies nationally, 606,043 with employees; Andalucía 202,933 (109,910 with employees); Cataluña 177,983 (100,712); Madrid 136,291; C. Valenciana 121,872** [new: INE table 39372, https://www.ine.es/jaxiT3/Tabla.htm?t=39372, CSV downloaded 23 Oct 2026; my aggregation].
- Ceiling at €5/month: 1% of national B2C companies is about 10,800 × €60 = about €650k ARR. Realistic reach for a self-serve micro product is well below 1%.

**(d) Willingness to pay**
- No evidence that micro B2C firms pay for complaint handling today; they buy paper complaint forms and handle replies by hand [notes: LEG-22, LEG-12].
- The downside a buyer avoids is small and unlikely: an Andalusian *leve* fine of €200–5,000 for a late reply, after a consumer complains; inspections lean to correction first (Madrid data above).

**(e) Distribution**
- Andalusian gestorías and associations before 20 May 2027 are the only time-bound channel; no gestoría Hoj@ offer was found (search 7), so the channel is unproven.
- Embedding in POS, booking, PMS and gym software is the realistic route, but those vendors can build it themselves.

**(f) Build and legal**
- Trivial: forms, numbering, timers on regional working-day calendars, email parsing of Hoj@ notices (no API). MVP in 2–3 weeks.
- Complaint data are personal data (GDPR). AI-drafted replies are fine with human approval; the business stays liable for the content and the deadline. The kit must not file on Hoj@ for the business unless a person authorised in Hoj@ does it.

**(g) Defensibility:** none. Any POS or PMS vendor, Lawwwing or the Junta itself can replicate it.

**Type C check (~€5/month):** the product can be fully automated with almost no support, but it fails the "visible monthly value" test: most micro businesses receive a handful of complaints a year, and Hoj@ already notifies them of each one. As a standalone it would churn at any price. Realistic prices are €0 (a free feature inside a POS, booking or PMS product), €1–2 per location wholesale to such vendors, or a one-off €29–49 Hoj@ onboarding sold through gestorías before 20 May 2027 (all hypotheses, untested).

**(h) Kill criteria**
- "Fewer than 1 in 5 of 30 B2C owners has faced a consumer-office case or worries about the 15-day rule": **open [I]**. Desk proxy points to low concern (confused official messaging; no enforcement of the new clock found).
- "No regional authority has enforced the new duties by mid-2027": **open**, but as of October 2026 there is no sign of enforcement of the clock; inspections target paper forms and posters.
- Hoj@ module: "kill if the Order does not impose these duties or if Hoj@ already sends reminders": **not met**. The Order imposes the duties and the dates; it provides receipt notices but no pre-deadline reminders (the app's interface was not inspected).

**Scores (national kit as specified, €5/month)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Duty in force since 28 Dec 2025 but no visible enforcement of the clock; the Hoj@ registration deadline (about 20 May 2027) applies only in Andalusia. |
| S2 Buyers | 5 | About 1.08M B2C-facing companies (DIRCE 2025). |
| S3 Willingness to pay | 2 | No current spend; rare *leve* fines; free substitutes. |
| S4 Reachability | 2 | Diffuse micro buyers; embedding partners would rather build it. |
| S5 Competitive gap | 4 | No dedicated SME tool, only manual and generic options; the gap exists because the job is small. |
| S6 Build speed | 5 | MVP in 2–3 weeks, no certification. |
| S7 Defensibility | 1 | Trivially copyable. |
| S8 Retention | 2 | Few complaints per business, so little visible monthly value. |
| **Sellability** | **3.00** | |
| **P** | **2** | Per-business losses well under €1k a year; a sanction is rare. |
| **Overall** | **2.60** | 0.6 × 3.00 + 0.4 × 2 |

**Open [I] checks:** the 30-owner interview test; whether Andalusian gestorías will charge for Hoj@ registration and what; whether the Hoj@ app shows deadline countdowns.

**What would change the verdict:** a regional campaign or published fines on the 15-day clock or on Hoj@ late replies; a POS, PMS or booking vendor willing to pay a wholesale fee per location for an embedded module; or gestorías paying for bulk Hoj@ onboarding before 20 May 2027. The deadline watcher is worth folding into IDEA-06 (gestoría cockpit) or a PMS product (IDEA-32 or IDEA-33) as a feature.

---

#### IDEA-21: Call-consent ledger and 400-prefix compliance layer for SMEs that sell by phone — RESHAPE (medium)

**Validated definition (after reshape).** A consent-proof and 2-year expiry gate for SMEs that call consumers to sell (energy and telecom resellers, solar and efficiency installers, insurance agents, estate agents, training providers): it captures and timestamps express consent from web forms, WhatsApp or recorded calls, stores the proof, expires it after two years, checks the Lista Robinson, and blocks or flags numbers without valid consent inside the dialer or CRM. It is sold as an integration in cloud-telephony and CRM marketplaces at about €9–19 per seat per month. The "400-prefix compliance layer" is dropped: operators assign and switch the numbering, so it is not a product.

**(a) Problem reality and rule status**
- **The 400 resolution (settles the BOE reference).** Resolución de 14 de abril de 2026, de la Secretaría de Estado de Telecomunicaciones e Infraestructuras Digitales, "por la que se atribuyen recursos públicos de numeración para la prestación del servicio de llamadas comerciales y se establecen las condiciones para su uso", BOE-A-2026-8409, BOE 16 Apr 2026, effective 17 Apr 2026 [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8409, seen 23 Oct 2026; reference first found by search 1].
  - Primero.2: firms within Ley 10/2025's scope "no podrán utilizar ningún otro rango" (save the small-retailer exception in its DT única.4).
  - Sexto: the range must be "plenamente operativo en el plazo de 6 meses"; "Una vez cumplido dicho plazo, las llamadas comerciales sólo podrán efectuarse a través del rango NXY = 400". That is a general rule, with no consumer or B2B qualifier.
  - Operator blocking comes from Ley 10/2025 art. 16.4: operators must block calls that show signs of commercial calling without the specific code or without complying with LGTel art. 66.1, using systems the Secretaría de Estado authorises [new: https://www.boe.es/eli/es/l/2025/12/26/10, seen 23 Oct 2026].
- **B2B and autónomos (settles the section 5 item as far as text allows).** Neither the resolution nor Ley 10/2025 art. 16 distinguishes consumer from business recipients. Vendors disagree: Aircall says the rule "does not explicitly distinguish between B2B and B2C" and advises preparing regardless [new: https://aircall.io/es/blog/prefijo-400-llamadas-comerciales/, 2 Sep 2026]; Clientify says B2B-only callers are probably unaffected and that autónomos selling to individuals are in a "zona gris" [new: https://clientify.com/prefijo-400, reviewed 23 Sep 2026]. My reading: the numbering rule covers commercial calls generally; the consent and void-contract rules (TRLGDCU) protect consumers only. B2B coverage is not excluded in the text, so the first kill limb fails.
  - The press reading on switch-on day was muddled. Moncloa.com (a private outlet, not the Government's La Moncloa) said "cualquier empresa que llame para vender" must use a 400 number, but also that Ley 10/2025 "deja fuera a las pymes que no presten servicios básicos", and called 28 Dec 2026 the "plazo real". It reported that the CNMC allocates ranges to operators in blocks of 1,000 numbers, that Movistar (400 00 1004) and Digi (four 400 120 1xx numbers) had published theirs, and that 400 numbers are one-way: "no se puede devolver la llamada" [new: https://www.moncloa.com/2026/10/17/prefijo-400-llamadas-comerciales-3450368/, 17 Oct 2026]. Operator blocking relies on traffic-pattern detection, so SMEs outside Ley 10/2025's scope face detection risk rather than a hard switch (inference).
  - **Practical consequence for the idea:** numbering is an operator job and its SME scope is disputed, so the durable demand driver is TRLGDCU art. 62.1 (void contracts without express consent renewed within two years), which binds every trader that contracts with consumers by phone.
- **Consent and void contracts.** TRLGDCU art. 62.1 as amended: consent must be express and "obtenido o renovado de forma expresa en los dos años anteriores a la comunicación"; a phone contract made in breach of the unsolicited-call rules is presumed to lack consent, "deviniendo nulo el contrato"; in force since 28 Dec 2025 with no deferral [new: BOE Ley 10/2025, DF tercera]. LGTel opt-in for commercial calls has applied since June 2023, with prior consent or a prior contractual relationship as the basis (Aircall's reading) [new: https://aircall.io/es/blog/prefijo-400-centros-de-llamadas/, 3 Sep 2026; Maldita explainer in search 2 results].
- Fines: LGTel serious infringement €50,001–2M for misuse of numbering, with a prior warning usual (single vendor source, Aircall) [new: Aircall, 2 Sep 2026].
- Election risk: none; all instruments are in force.

**(b) Competitors**
- Aircall: more than 23,000 customers and more than 250 integrations, but did not offer 400 numbers yet and lists no consent features (2–3 Sep 2026) [new: both Aircall pages above].
- Clientify (Spanish CRM with VoIP): no consent or Robinson features on its 400 page [new: Clientify page above]. Zadarma announced 400 numbers (per Clientify).
- Lista Robinson (Adigital): its own CSV tool, an API, or third-party tools; a consultation is valid for one month; free "bonificada" tariff for micro and small firms up to 30,000 records a year, then €1,900–5,500 a year [new: https://www.listarobinson.es/empresas, seen 23 Oct 2026].
- No dedicated consent ledger with a 2-year expiry gate was found (search 2). CRM consent fields and certified-communication providers can be assembled into one, so the gap is real but shallow.

**(c) Buyers and market size**
- DIRCE 2025: insurance auxiliaries (CNAE 662) 62,587 companies, 45,241 without employees; estate agencies (683) 60,683; call centres (822) 495 [new: INE table 39372, 23 Oct 2026]. About 541 active electricity retailers on the CNMC census [new: https://sede.cnmc.gob.es/listado/censo/2, downloaded 23 Oct 2026; my count of entries not marked "Baja"].
- Only firms that call consumers they have no contract with need the ledger. That share is unknown, so the realistic paying pool is perhaps 10k–40k firms (inference).
- Ceiling: 5,000 seats at €15/month is about €900k ARR.

**(d) Willingness to pay:** adjacent spend on cloud telephony, CRM seats and Robinson fees exists; the loss avoided is a voided contract (refund plus lost commission) and blocked campaigns. No voided-contract case or loss figure was found.

**(e) Distribution:** marketplaces of Aircall (250+ integrations), Ringover, Zadarma and CRMs; energy-reseller and insurance-agent networks. Unproven.

**(f) Build and legal:** a consent store, proof capture (web form hash, WhatsApp opt-in, call-recording reference), expiry jobs, the Robinson API, and a webhook or API gate for one dialer: 4–6 weeks. Consent records are personal data; LOPDGDD art. 23 governs exclusion lists [notes: LEG-11].

**(g) Defensibility:** medium-low. Integrations and stored proofs give some lock-in; a telephony vendor can add an expiry field.

**(h) Kill criteria**
- "Resolution does not cover B2B calls and B2C cold-calling collapses after blocking": **not met** on the first limb (no B2B exclusion in the text). Whether B2C cold-calling collapses after 17 Oct 2026 is **open**: search 20 found no reports of blocked SMEs, failures or volume data in the first week.
- "The two largest cloud-telephony vendors in Spain ship equivalent consent gating by Q1 2027": **open**; Aircall had none in September 2026.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Blocking live since 17 Oct 2026; void-contract rule in force since 28 Dec 2025; enforcement runs through consumer claims, not a dated audit. |
| S2 Buyers | 3 | Probably 20k–100k phone-selling SMEs, of which only consumer cold-callers need it. |
| S3 Willingness to pay | 3 | Adjacent telephony, CRM and Robinson spend; void-contract losses unquantified. |
| S4 Reachability | 3 | Telephony and CRM marketplaces and agent networks exist but are unproven for this. |
| S5 Competitive gap | 3 | No dedicated tool found, but CRMs and the Robinson API cover parts. |
| S6 Build speed | 4 | 4–6 weeks for one dialer integration, no certification. |
| S7 Defensibility | 2 | Integrations and stored proofs only; vendors can add the field. |
| S8 Retention | 4 | Proof must be kept and renewed every two years; records accumulate. |
| **Sellability** | **3.25** | |
| **P** | **3** | Blocked campaigns and void contracts are costly for phone sellers, but numbering is solved by operators and no loss data exist. |
| **Overall** | **3.15** | 0.6 × 3.25 + 0.4 × 3 |

**Open [I] checks:** interview 15 energy and telecom resellers and insurance agents on voided contracts and clawbacks since 2025; ask Aircall, Ringover and Zadarma partner teams whether they would list a consent app; measure post-17 Oct call volumes.

**What would change the verdict:** evidence of voided contracts or commission clawbacks (would raise P and S3 and make it a GO for a pilot); a top telephony vendor shipping consent expiry natively (kill); an official reading that limits the 400 rule to firms in Ley 10/2025's scope (does not affect the consent ledger, which rests on TRLGDCU art. 62.1).

---

#### IDEA-22: Customer-service compliance kit for small basic-service providers (Ley 10/2025) — RESHAPE (medium)

**Validated definition (after reshape).** An audit-evidence and deadline workspace for small electricity and gas retailers, local water companies, bus operators and postal operators in Ley 10/2025's scope: it imports queue and call records from the provider's PBX or helpdesk (CSV first, connectors later), computes the art. 8.2 and 10.3 service level (95% answered within three minutes on average) and dropped calls, issues complaint keys and tracks the 15-working-day, 2-hour and 5-day deadlines, logs co-official-language requests, and builds the annual (or biennial) evaluation file kept for five years. It is priced per audit cycle (about €1,500–3,000 a year) and sold with an accredited auditor once one exists. Small telecom operators are a secondary segment, because their sector rules come first.

**(a) Problem reality and rule status**
- **Deadline (settles the section 5 item):** 12 months from entry into force, so 28 Dec 2026 (DT única.1) [new: BOE consolidated text, seen 23 Oct 2026]; KPMG gives the same date [new: KPMG alert, Jan 2026]. No extension or development regulation found (search 4).
- **Duties in the BOE text:** 95% of calls answered "de media, en un plazo inferior a tres minutos" (arts. 8.2, 10.3); no cutting calls for long waits (art. 8.4); complaints resolved within 15 working days, service-continuity incidents within 2 hours, billing within 5 days (art. 17); co-official languages on request (arts. 7.2, 8.6, 13.6, 9.2); annual documented evaluation kept five years and published on the website (art. 21); annual audit by an ENAC-accredited auditor checking that measurement error is under 5% (art. 22) [new: BOE consolidated text].
- **Relief for small firms:** firms under 250 workers and under the turnover or balance thresholds may run the evaluation and the audit every two years "de forma justificada en atención al volumen" of complaints (arts. 21.1, 22.1) [new: same]. The first evaluation file is due to the authority by the end of Q1 of the following year (art. 21.3), so the first audit is probably a 2027–2028 event (inference).
- **Carve-outs:** electricity, gas and telephone retailers under 5% national share and not large are exempt only from the 24/7 line (art. 14.2) and the numbering rules (arts. 16.2–16.4) (DT única.4) [new: BOE]. Electronic communications and financial services "se regirán por la normativa sectorial", with Ley 10/2025 supplementary (art. 2.1; KPMG); sector rules also prevail for sanctions (art. 23.2).
- **Auditor scheme:** ENAC's site shows no accreditation scheme or news for Ley 10/2025 as of its latest items (14 Oct 2026) [new: https://www.enac.es/, seen 23 Oct 2026]; search 3 found no ENAC scheme or UNE standard either. Two months before the deadline, nobody can say what an auditor will accept.
- Sanctions: consumer-law infractions under the TRLGDCU and regional laws (art. 23.1); no amounts in the law. The €100,000 figure remains an unverified vendor claim [notes: LEG-13].
- Election risk: none for the law. An extension would need a decree-law, which nothing suggests.

**(b) Competitors:** enterprise contact-centre suites; Aunoa's AI agents ("lista para auditoría", no prices, enterprise focus) [new: Aunoa page above]; certification and advisory firms (TÜV SÜD [notes: LEG-13]; Kiwa publishes a Ley 10/2025 infographic [new: search 4 result, kiwa.com]). Queue service-level reports are a standard cloud-PBX feature (general knowledge; no vendor page verified in this pass). No SME-priced kit found.

**(c) Buyers and market size (kill test)**
- About 541 active electricity retailers on the CNMC census (948 entries, 407 marked "Baja") [new: CNMC census, downloaded 23 Oct 2026; my count]. Almost all are SMEs; only the small-retailer carve-out above applies to them.
- DIRCE 2025: water capture, treatment and distribution (CNAE 360) 3,158 companies; gas production and distribution (352) 99; telecom (61) 5,975, mostly without employees; other postal and courier (532) 33,467, of which 29,210 without employees; passenger land transport (493) 62,648, mostly taxis, which are out of scope [new: INE table 39372].
- So well over 500 SMEs are in scope; **the kill criterion is not met.** The paying pool is the firms with real consumer call volumes: perhaps 1,000–3,000 (inference). Ceiling: 2,000 × €2,000 a year is about €4M; a realistic 5% share is about €200k a year.

**(d) Willingness to pay:** audit fees are unknown (no scheme yet); compliance spend exists at regulated utilities. Tiny providers that can use the biennial regime will pay little.

**(e) Distribution:** CNMC registers as lead lists (public); auditors and certification bodies as referral partners once accredited; small-operator and independent-retailer associations (not verified in this pass).

**(f) Build and legal:** CSV import and metrics in 3–4 weeks; PBX connectors and the audit pack depend on a method nobody has published. Building connectors before the ENAC scheme exists risks rework. Customer data are personal data.

**(g) Defensibility:** medium-low. Auditor relationships and a maintained method are the only edges, and both are copyable once the method is public.

**(h) Kill criteria**
- "Fewer than about 500 SME providers remain in scope after sector-rule carve-outs": **not met** (electricity retailers alone are about 541; water, gas, bus and postal add more).
- "Auditors accept standard helpdesk reports": **open**, and I expect it to be met. Art. 22 asks auditors to confirm documentation and a measurement error under 5%, which standard queue reports could support. If so, the product shrinks to a documentation and deadline tool.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | Duty in the BOE with a 28 Dec 2026 deadline, then a recurring evaluation. |
| S2 Buyers | 2 | About 5k–20k entities in scope, most of them micro; perhaps 1–3k with real call volumes. |
| S3 Willingness to pay | 3 | Compliance and audit budgets exist at regulated firms; amounts unknown. |
| S4 Reachability | 3 | Public registers and auditors as partners; unproven. |
| S5 Competitive gap | 4 | Only enterprise suites and consultants. |
| S6 Build speed | 3 | 2–4 months for connectors and an audit pack tied to an unpublished method. |
| S7 Defensibility | 2 | Know-how and auditor ties, copyable. |
| S8 Retention | 4 | Recurring (annual or biennial) evaluation; five-year records. |
| **Sellability** | **3.25** | |
| **P** | **3** | Moderate: consumer-law fines and an audit cost; no closures. |
| **Overall** | **3.15** | 0.6 × 3.25 + 0.4 × 3 |

**Open [I] checks:** ask two or three likely auditors (Kiwa, TÜV SÜD, AENOR) what evidence they will accept and whether they would refer clients; interview ten small electricity retailers and water companies on call volumes and current reports.

**What would change the verdict:** a published ENAC scheme that demands evidence standard reports cannot give (raises S3 and S7; GO); auditors bundling their own templates, or acceptance of standard PBX reports (kill); a decree extending the deadline (lowers S1).

---

