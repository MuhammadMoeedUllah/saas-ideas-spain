# Pain points of Spanish transport & logistics, manufacturing/industrial, and agriculture/fishing/agrifood SMEs (2024–2026)

Notes compiled 23 Oct 2026. **Method caveat for the report writer:** the shared web-search budget was used up after the first round of 8 searches. Everything else comes from about 90 direct page fetches: official sources (BOE consolidated texts and daily summaries, European Commission, Eurostat API, AICA annual report PDF), sector associations (Fenadismer, CETM, UNO, Cooperativas Agro-alimentarias, UPA, ASAJA, Unió de Pagesos, CEPESCA, SCRATS, FIAB) and trade press (mainly trans.info). Several requested topics could not be verified. They are listed under each Gaps section. Do not treat missing topics as evidence that a pain does not exist.

**Big 2026 context that changes almost every entry:** the US–Israel military operation against Iran (from 28 Feb 2026) set off an energy shock. Brent peaked above US$119/bbl, and TTF gas spot prices rose 55% in two weeks to above €50/MWh ([BOE, RDL 7/2026 preamble, 21 Mar 2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544)). Spain answered with RDL 7/2026 (20 Mar 2026, "Plan Integral de Respuesta a la Crisis en Oriente Medio", €5,000M), RDL 9/2026 (14 Apr 2026, transport) and RDL 25/2026 (29 Sep 2026, extending measures to 31 Dec 2026). A snap general election is set for 29 Nov 2026 ([Wikipedia, 2026 in Spain](https://en.wikipedia.org/wiki/2026_in_Spain)), so draft regulations may stall.

---

## Key question 1: Transport and logistics (road haulage, couriers, last mile): what are the day-to-day pains, rules and costs?

### Takeaway
The sharpest pain in October 2026 is the **mandatory digital control document (DeCA)**, live since 5 Oct 2026. Rollout failures, roadside fines and shippers pushing liability onto drivers make it a purely software-shaped problem. Around it sit the 2026 **fuel shock and the fight to enforce the fuel-indexation formula** (RDL 9/2026), a structural **driver shortage** (about 30,000 drivers missing), chronic **late payment** (38% of payers still beyond 60 days), and the new **tachograph obligation for 2.5–3.5 t vans** in international work.

### Cited Findings
The structured entries IND-01 to IND-09 follow. Every fact in them carries its source and date.

### IND-01: Mandatory digital control document (DeCA): chaotic rollout, fines and liability shifting
- **Who:** Every public road-freight carrier, from the autónomo with one truck to medium fleets (50–249). Shippers (cargadores contractuales) and freight forwarders/operators are jointly liable.
- **Where:** National. It covers all domestic public road freight in Spain, cabotage included. International CMR transport is **not** covered, and final-mile parcel delivery is exempt.
- **Day-to-day reality:** Since 5 Oct 2026 every domestic haulage service needs a native digital PDF with a QR code. The QR must link to a public HTTPS URL, and the document must be created before the truck leaves. Drivers are being fined at the roadside when inspectors' tablets or the shipper's repository fail. Some large shippers force carriers' drivers to log into private platforms en route and "validate" provisional DeCAs, which moves liability onto the driver.
- **Evidence:**
  - Ley 9/2025, transitional provision 8: the control document "deberá ser necesariamente digital a los diez meses desde la entrada en vigor de esta ley" ("must necessarily be digital ten months after the law enters into force") ([BOE, Ley 9/2025 consolidated](https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545); published BOE 4 Dec 2025, in force 5 Dec 2025 per the [Hacienda bulletin record](https://www.hacienda.gob.es/BoletinesHacienda/Boletines/2025/93921.pdf)). Ten months after 5 Dec 2025 gives **5 Oct 2026**.
  - Technical rules come from the Resolución DGTCF of 5 June 2026 (BOE 12/06/2026, replacing the Resolución of 22 May 2023), Orden TRM/282/2026 and Orden FOM/2861/2012. They require:
    - a native PDF of at most 5 MB with creation/modification metadata;
    - a QR code pointing to a unique HTTPS URL (TLS ≥1.2) that downloads without credentials (a numeric code alone is no longer enough);
    - a timestamp before the service starts and a copy to the driver before departure;
    - retention for at least one year by **both** shipper and carrier.
    Handwritten annotations are no longer valid. An e-signature is not required unless the document is also used as a contract or eCMR ([Gómez-Acebo & Pombo, 16 Jul 2026](https://ga-p.com/publicaciones/guia-para-no-perderte-con-el-nuevo-deca/)). A second source agrees: RD 1211/1990 art. 222, Orden FOM/2861/2012 art. 6, HTTPS/TLS 1.2, one-year repository ([Viafirma, 1 Sep 2026](https://www.viafirma.com/en/keys-mandatory-deca/)).
  - The digital requirement was originally due on 1 Sep 2024 and was postponed to Oct 2026 ([Fieldeas, 22 Jan 2025, updated 4 Dec 2025](https://www.fieldeas.com/en/ecmr-mandatory/); vendor source, single source for the original date).
  - **Readiness:** a Fenadismer/Continental survey of 750 transport professionals (Oct 2025) found 17% prepared, 35% insufficiently prepared and 23% not prepared at all. 25% expected the shipper to provide the document ([trans.info, 5 Feb 2026](https://trans.info/es/documentos-digitales-452450)).
  - **Rollout incidents:**
    - QR codes failed to scan at roadside checks.
    - One major shipper required each external driver to register on its private DeCA platform, photograph the delivery note and correct data en route. It cancelled the carrier's services when the carrier objected.
    - Shippers issued "provisional DeCAs" that only become final once the driver validates them. Fenadismer questions whether this is legal ([Fenadismer, 8 Oct 2026](https://www.fenadismer.es/primeras-incidencias-del-deca-tras-su-entrada-en-vigor/)).
  - **Fines:** inspectors fined drivers "more than 400 euros" for "carecer del documento de control" (lacking the control document) even though the drivers showed the QR they had been given. Fenadismer says the haulier is "el eslabón más débil de la cadena" ("the weakest link in the chain") ([Fenadismer, 15 Oct 2026](https://www.fenadismer.es/deca-sanciones-injustas-a-transportistas-por-errores-de-sus-cargadores-o-de-las-inspecciones-en-carretera/)).
  - **Ministry climb-down:** the DeCA and HeRU systems had incidents from 5 to 19 Oct 2026, and Guardia Civil tablets could not download documents. The DG de Transporte told the autonomous communities to archive reports caused by download failures in that window. Other DeCA infractions, such as missing data, are still prosecuted ([Fenadismer, 22 Oct 2026](https://www.fenadismer.es/deca-transportes-reconoce-fallos-tecnicos-y-no-tramitara-las-multas-impuestas/)).
  - **Fine level:** not carrying a DeCA or omitting essential data is a serious infraction ("infracción grave", LOTT art. 141.17) with a fine of €401–600 under art. 143.1.d ([Veritas Gestión, updated 18 Oct 2026](https://veritasgestion.com/?p=7976); single source for the article numbers, consistent with Fenadismer's ">400 euros").
  - **Scope details:**
    - Shipper and carrier are jointly liable for the document existing. The shipper answers for shipment data and the carrier for vehicle data.
    - Removals, cranes and small loads one person can handle are exempt. The sector reads a full pallet as in scope.
    - **Final-mile parcel delivery from the hub to the end customer is exempt**, so only "primary" transport is covered ([Fenadismer training PDF, created 29 May 2026](https://www.fenadismer.es/wp-content/uploads/Pildora-formativa.-todo-sobre-el-Documento-Electronico-de-Control.pdf)).
- **Scale:**
  - 152,871 road-freight companies at the start of 2026, 61,716 of them in heavy transport ([trans.info, 24 Aug 2026](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)).
  - Fenadismer represents more than 32,000 companies and 60,000 vehicles ([Fenadismer](https://www.fenadismer.es/)). CETM represents more than 31,000 companies, 129,000 industrial vehicles and 215,000 workers ([CETM](https://www.cetm.es/)).
  - Shippers in every sector that buy domestic haulage are co-liable.
- **Cost/impact:** fines of €401–600 per infraction (more for falsification). Cancelled services when carriers refuse shipper platforms. Extra admin per trip (not quantified; gap).
- **Driver & status:** Ley 9/2025 transitional provision 8, Orden FOM/2861/2012, Resolución DGTCF 5 Jun 2026 and Orden TRM/282/2026. **In force since 5 Oct 2026.** Fines for the 5–19 Oct download failures are waived; nothing else is.
- **How it is solved today:**
  - Vendor DeCA tools range from "opciones viables desde los 5 euros al mes" (viable options from €5/month) to offers priced up to 1,000% higher for the most basic tool. Some tools do not meet the legal requirements ([Fenadismer, 10 Sep 2026](https://www.fenadismer.es/ojo-ofertas-abusivas-para-el-nuevo-documento-electronico-de-control/)).
  - "No hace falta ningún programa homologado" (no homologated software is needed) ([Veritas Gestión](https://veritasgestion.com/?p=7976)).
  - eCMR and e-signature vendors (Fieldeas, Viafirma, Edicom) do not publish prices.
  - Shippers impose their own private platforms (see the complaints above).
  - UNO has a "Guía DeCA" project page ([UNO](https://unologistica.org/proyectos-e-informes/guia-documento-electronico-de-control-administrativo-deca/); content and price not read).
- **Software-solvable?:** **Yes.** The obligation is entirely digital: generation, QR hosting with guaranteed uptime, a one-year repository, audit trail, shipper–carrier data reconciliation and proof for inspections. The unsolved problem is now reliability and liability evidence, not basic issuance, and basic issuance is already priced as a commodity at about €5/month.
- **Confidence:** High.

### IND-02: 2026 fuel-cost shock and the fight to enforce fuel-price indexation on invoices
- **Who:** Road hauliers of every size (autónomos to medium), plus the shippers and intermediaries who pay them.
- **Where:** National.
- **Day-to-day reality:** Diesel costs jumped after the Iran war began. Carriers must now put a regulated fuel-revision line on every invoice, but many shippers resist it or quietly cut base rates first. Meanwhile carriers track per-litre and per-vehicle aid that changes month by month.
- **Evidence:**
  - RDL 9/2026 says energy price rises have increased haulage costs "del orden del 30%" (around 30%). Road carries about 95% of goods transport ([BOE, RDL 9/2026, 15 Apr 2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8283)).
  - What RDL 9/2026 changes:
    - The revision is mandatory and must be itemised on the invoice.
    - It applies automatically at a fuel variation of 5% or more, and continuous contracts are revised every billing period.
    - There is a new formula with a weekly diesel index (G) and a coefficient (C). For trucks of 20 t or more, C is 0.3 when pre-tax diesel is below €0.85/l, 0.4 between €0.85 and €1.40/l, and 0.5 at €1.40/l or above.
    - New infractions apply to payers who block a separate fuel line. It is "grave" when the price is €3,000 or less (fines from €401–600 up to €801–1,000) and "muy grave" above €3,000 (from €1,001–2,000 up to €4,001–6,000). Repeat offences within 12 months can reach €18,000 (same source).
  - Ley 15/2009 art. 38: the price "se incrementa o reduce de manera ineludible" (must rise or fall, no exceptions) with fuel. Revision is automatic at 5% or more, and any agreement to the contrary is void ([BOE, Ley 15/2009 consolidated, latest update 15/04/2026](https://www.boe.es/eli/es/l/2009/11/11/15/con)).
  - The Ministry's "Coeficiente G" rose 44.6% for heavy vehicles and 38.4% for light vehicles between early January and 1 Oct 2026. Fenadismer opened a confidential complaint channel. It wants inspectors to catch shippers that "artificially lowered" base prices before applying the formula ([Fenadismer, 13 Oct 2026](https://www.fenadismer.es/canal-de-denuncias-contra-los-cargadores-que-no-indexen-el-combustible-a-sus-transportistas/)).
  - **Aid under RDL 7/2026:**
    - €0.20/l for holders of the professional-diesel refund (supplies up to 30 Jun 2026).
    - Up to €2,000M in ICO re-guarantees for the bank guarantees fuel-card holders must provide.
    - Beneficiaries may not make crisis-related dismissals until 30 Jun 2026 ([BOE, RDL 7/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544)).
  - **Per-vehicle aid under RDL 9/2026:**
    - €1,800 for heavy gas-powered trucks (and diesel trucks registered in the Canaries, Ceuta or Melilla).
    - €665 for trucks under 7.5 t.
    - €300 for light vans.
    - €200 for taxis and VTC vehicles ([BOE, RDL 9/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8283)).
  - **RDL 25/2026 extension:** professional-diesel aid of €0.05/l in October, €0.12/l in November and €0.19/l in December 2026. Paying with the professional-diesel card counts as the aid application ([Cooperativas Agro-alimentarias summary of RDL 25/2026, Oct 2026](https://www.agro-alimentarias.coop/docs_download/apoyar-al-campo-y-a-las-cooperativas-para-hacer-frente-al-impacto-de-la-crisis-energetica)).
  - A French comparison: French hauliers called off protests after their government agreed fuel-indexation enforcement and an 18 c/l diesel cut. Fenadismer says many of those measures "ya se encuentran implementadas en España" (are already in place in Spain) ([Fenadismer, 19 Oct 2026](https://www.fenadismer.es/crisis-diesel-los-transportistas-franceses-desconvocan-movilizaciones-tras-acuerdo-con-gobierno/)).
- **Scale:** All of the roughly 152,871 road-freight companies ([trans.info, 24 Aug 2026](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)).
- **Cost/impact:** Operating costs up about 30% (RDL 9/2026). The G index is up 44.6% in 2026 (Fenadismer). Shippers risk fines of up to €6,000, or €18,000 for repeat offences.
- **Driver & status:** A market shock from the Iran war. RDL 7/2026 has been in force since 21 Mar 2026, RDL 9/2026 since 16 Apr 2026 and RDL 25/2026 since 1 Oct 2026, with measures running to 31 Dec 2026. All are **in force**. Some aid depends on EU state-aid compatibility (Cooperativas summary). **Not verified:** whether Congress validated each RDL. In July 2025 Parliament repealed an earlier decree-law, RDL 7/2025 ([Wikipedia, 2025 Iberian blackout](https://en.wikipedia.org/wiki/2025_Iberian_Peninsula_blackout)).
- **How it is solved today:**
  - CETM's site lists a "Calculadora de Costes e Indexación" (cost and indexation calculator; price and access terms not shown) ([CETM](https://www.cetm.es/)).
  - Fenadismer runs its complaint channel.
  - The Ministry's historical ACOTRAM cost simulator is described in past Observatorio de Costes editions ([Observatorio de costes, abril 2016](https://sarreplec.caib.es/pluginfile.php/21164/mod_resource/content/0/OTM02/OTM02_Web_2016/ObservatorioCostes_abril2016.pdf)).
  - Otherwise, invoices in a TMS or ERP or by hand (no price data).
- **Software-solvable?:** **Yes.** A tool can pull the weekly G index, apply the right coefficient per vehicle class, itemise the fuel line on every invoice, keep an evidence file for inspection complaints, and track eligibility and claims for monthly aid.
- **Confidence:** High.

### IND-03: Driver shortage, an ageing workforce and slow, expensive licensing
- **Who:** Haulage companies of every size. The autónomos who make up much of the sector are themselves ageing.
- **Where:** National. Regional shortage lists name heavy-lorry drivers in Galicia, the Basque Country, Aragón, Castilla-La Mancha and Catalonia ([EURES, 24 Feb 2025](https://eures.europa.eu/living-and-working/labour-market-information/labour-market-information-spain_en)). Base pay is highest in Gipuzkoa and Barcelona and lowest in Ourense (CETM via [El Español, 8 Aug 2026](https://www.elespanol.com/sociedad/20260808/espana-necesita-conductores-camiones-faltan-camioneros-pagan-sueldos-euros-ano/1003744347084_0.html)).
- **Day-to-day reality:** Trucks stand idle without drivers. Firms recruit in Peru, Morocco and Colombia and then wait on licence exchanges and the CAP (Certificado de Aptitud Profesional, the professional-driver certificate). Young people avoid the job because of time away from home, waits at docks and insecure rest stops.
- **Evidence:**
  - CETM puts the deficit at 30,000 drivers and says it "could double by 2028". Average driver age is 55. Employers and unions filed a joint request for early retirement in Dec 2025, which is still pending ([Europa Press via Bolsamanía, 4 Feb 2026](https://www.bolsamania.com/noticias_amp/empresas/economia--los-transportistas-piden-medidas-reales-ante-la-grave-falta-de-camioneros-y-critican-trabas-administrativas--21606838.html)).
  - Major employers' associations estimate up to 116,000 drivers will be needed by 2028. Only 3% of drivers are under 25. SEPE has added the job to its Catálogo de Ocupaciones de Difícil Cobertura (official list of hard-to-fill occupations). Gross pay is €20,000–24,000/yr in general haulage, about €37,900 for international drivers in Spain, and €45,000–50,000 in Germany, Belgium or Italy ([El Español, 8 Aug 2026](https://www.elespanol.com/sociedad/20260808/espana-necesita-conductores-camiones-faltan-camioneros-pagan-sueldos-euros-ano/1003744347084_0.html)).
  - In a parliamentary answer the Government said more than 20,000 drivers are needed. Exchanges of foreign C/D licences rose from 13,903 (2024) to 15,589 (2025), +12%: Peru 4,317, Morocco 2,248, Colombia 1,206. The DGT process has been fully online since May 2025 ([EFE via Menorca.info, 3 May 2026](https://www.menorca.info/actualidad/nacional/2026/05/03/2621635/escasez-camioneros-acelera-canje-carnes-extranjeros-15500-pasado-ano.html)).
  - UNO Logística puts the deficit at 20,000 ([Europa Press via Bolsamanía](https://www.bolsamania.com/noticias/empresas/economia--uno-reclama-soluciones-urgentes-ante-la-falta-de-20000-conductores-de-transporte-por-carretera-en-espana--21479501.html); seen only as a search snippet, not opened).
  - Road-freight companies fell by 3,608 in 2025 (−2.31%) to 152,871. Heavy-transport companies fell by 2,754 (−4.27%) to 61,716 (trans.info citing SNAP, [24 Aug 2026](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)).
  - Getting the licences costs €3,000–4,000 and takes close to a year. The Plan Reconduce offers aid of up to €3,000. More than 50% of drivers are over 55 ([trans.info, 31 Mar 2026](https://trans.info/es/espana-sin-camioneros-465872)).
- **Scale:** The whole road-haulage sector (about 152,871 companies). Estimates of the gap range from 20,000 (Government, UNO) to 30,000 (CETM). There is no official figure.
- **Cost/impact:** Lost capacity. €3,000–4,000 and about a year to train each new driver. Firms leaving the market (−3,608 in 2025).
- **Driver & status:** A demographic and working-conditions problem. The CAP is required under RD 284/2021 (a 140-hour course, per El Español). The early-retirement request is **pending**.
- **How it is solved today:** Foreign recruitment plus licence exchange, the Plan Reconduce (up to €3,000), and vocational training proposals from CETM. Recruiters' fees are not verified.
- **Software-solvable?:** **Partly.** Software can run foreign-driver pipelines (licence exchange, CAP, residence paperwork) and retention tools such as home-time planning and dock-wait reduction. The root causes, demographics and pay, are not software problems.
- **Confidence:** High on the existence and direction of the shortage. Medium on the exact size of the gap, since the figures are association estimates.

### IND-04: Late payment by shippers and intermediaries
- **Who:** Carriers, especially autónomos and micro firms subcontracted through intermediaries.
- **Where:** National.
- **Day-to-day reality:** Carriers finance their clients for about two months. More than a third of payers still break the 60-day legal maximum, despite a transport-specific sanction regime.
- **Evidence:**
  - In August 2026 the average payment period was **52 days**, the best in Fenadismer's series, and 38% of shippers and intermediaries paid after 60 days. Of those late payers, 76% paid at 60–90 days and 6% after 120 days. The figures were 59 days and 48% in December 2025, and 83 days in 2021. Bank transfers make up 69% of payments and confirming 25%. The proposed EU 30-day payment regulation is "blocked" in the Council ([trans.info, 22 Sep 2026](https://trans.info/es/los-transportistas-espanoles-esperan-52-dias-para-cobrar-la-reforma-europea-se-atasca-504049)).
  - Baseline: in February 2022, 63% of payments exceeded 60 days and the average was 78 days. Of the late payers, 34% paid after more than 90 days and 21% after more than 120 days. The sanction regime approved in October 2021 allows fines of up to €6,000, or €30,000 for repeat or abusive cases ([EFE via Vivir Ediciones, 29 Mar 2022](https://vivirediciones.es/?p=102403)).
  - Ley 15/2009 art. 41: the payer is in default after 30 days, by reference to Ley 3/2004 ([BOE, Ley 15/2009](https://www.boe.es/eli/es/l/2009/11/11/15/con)).
- **Scale:** All hauliers. Fenadismer's observatory covers the whole sector.
- **Cost/impact:** Working capital tied up for about 52 days on average. Confirming and factoring costs (not quantified; overlaps with the finance researcher).
- **Driver & status:** Ley 3/2004 and Ley 15/2009, plus a transport-specific sanction regime in force since Oct 2021 (the name of the amending law was not verified). The EU Late Payment Regulation proposal is **stalled**.
- **How it is solved today:**
  - Wtransnet's freight exchange includes a payment guarantee with Coface covering at least 90% of the invoice, plus payment mediation. Prices are quote-only ([Wtransnet](https://www.wtransnet.com/es/), [pricing page](https://www.wtransnet.com/es-es/bolsa-de-cargas/precios/)).
  - CETM runs "Icired", a published registry of payment defaults ([CETM](https://www.cetm.es/)).
  - Confirming and factoring.
- **Software-solvable?:** **Partly.** Software can score shippers' payment behaviour, generate statutory interest and compensation claims automatically, and assemble inspection complaints. Enforcement itself stays legal and administrative.
- **Confidence:** High.

### IND-05: Tachograph now required on 2.5–3.5 t vans in international transport and cabotage
- **Who:** Van operators (autónomos, micro and small firms) doing paid international transport or cabotage.
- **Where:** National, on cross-border work.
- **Day-to-day reality:** Since 1 July 2026 these vans need a smart tachograph (G2V2) fitted by an authorised workshop. The operator also needs a company card, driver cards, data downloads, file retention and EU driving-time rules, which is truck-level admin for very small firms.
- **Evidence:**
  - The device costs "en torno a 1.000 euros netos" (around €1,000 net) plus installation. Spain's sanction is €2,001. Driver cards must be downloaded at least every 28 days and the vehicle unit every 90 days, with files kept for 1–2 years. Drivers fall under the 9-hour daily and 56-hour weekly limits, posting rules and the return-to-base obligation. The exemptions are the craftsman exemption (art. 3(aa), within 100 km) and own-account transport (art. 3(ha)) ([trans.info FAQ, 23 Jun 2026](https://trans.info/es/tacografo-en-furgonetas-desde-el-1-de-julio-de-2026-a-quien-afecta-exenciones-y-sanciones-faq-484861)).
  - An IRU survey found 88% of affected vans still without the device in May 2026. 27.7% of operators expected to be ready and 46.5% admitted they would not be. Workshop shortages, cost and compatibility were cited ([trans.info, 11 May 2026](https://trans.info/es/cuenta-atras-para-las-furgonetas-el-88-aun-sin-tacografo-para-2026-473744)).
  - After the deadline, about a third of fleets had not finished adapting and 15.6% had not started. Cost was the biggest obstacle for 62.5% (Kienzle clients, n=116, which the article says is not representative) ([trans.info, 12 Aug 2026](https://trans.info/es/el-plazo-del-tacografo-ya-ha-vencido-muchas-furgonetas-siguen-sin-adaptarse-495758)).
  - Only authorised workshops can install and activate the G2V2. From 7 Jul 2026, new heavy-vehicle types also need event data recorders ([trans.info, 29 Jun 2026](https://trans.info/es/revolucion-de-julio-en-el-transporte-europeo-tacografos-en-furgonetas-cajas-negras-en-camiones-y-nuevos-peajes-486204)).
- **Scale:** The number of Spanish vans affected is unknown (gap).
- **Cost/impact:** About €1,000 per van plus installation. A €2,001 sanction. Recurring download and retention admin.
- **Driver & status:** Reg. (CE) 561/2006 and the tachograph rules as amended by the EU Mobility Package. **In force since 1 Jul 2026**, with no general grace period.
- **How it is solved today:** Authorised workshops plus tachograph download and analysis services or telematics (for example Geotab). No price data was verified.
- **Software-solvable?:** **Partly.** Remote download, infringement analytics and posting declarations can be software. The hardware cannot.
- **Confidence:** Medium-high. The sources are trade press and the surveys are not representative.

### IND-06: Waiting times at loading docks, and detention compensation that goes unclaimed
- **Who:** Carriers (all sizes) and shippers' warehouses.
- **Where:** National.
- **Day-to-day reality:** Trucks wait more than an hour at distribution centres. The law entitles carriers to hourly compensation, but claiming it needs proof of arrival times and risks the client relationship.
- **Evidence:**
  - Over 40% of shippers and 70% of carriers report waits of more than one hour. 70% of carriers say the main consequence is missing agreed deadlines. 46% of shippers use dock-management technology. 86% of carriers say fewer than half of their clients provide rest areas (CEL and CargoON study, [CadenadeSuministro, 21 Nov 2023](https://cadenadesuministro.es/noticias/cargadores-y-transportistas-siguen-sufriendo-esperas-en-los-muelles-de-carga-y-descarga_478995_102.html); this predates 2024 and is a single study).
  - Ley 15/2009 art. 22: after the first hour of waiting the carrier may claim 2×IPREM/day for each hour or fraction, up to 10 hours a day. Day two pays 25% more and day three onwards 50% more ([BOE, Ley 15/2009](https://www.boe.es/eli/es/l/2009/11/11/15/con)).
  - Waiting at docks is cited as a reason drivers leave the job ([trans.info, 31 Mar 2026](https://trans.info/es/espana-sin-camioneros-465872)).
- **Scale:** Sector-wide (70% of carriers in the 2023 study).
- **Cost/impact:** Lost truck hours. How much statutory compensation goes unclaimed is unknown (gap).
- **Driver & status:** Ley 15/2009 art. 22, **in force**.
- **How it is solved today:** Dock booking and slot tools (used by 46% of shippers in 2023). Vendor prices not verified.
- **Software-solvable?:** **Yes.** Geofenced arrival and departure timestamps can generate paralización claims automatically, and slot booking cuts waits.
- **Confidence:** Medium. The data is dated, but the legal hook is solid.

### IND-07: Cargo theft and insecure rest stops
- **Who:** Long-haul carriers and their drivers.
- **Where:** The source singles out the AP-7. That motorway runs along the Mediterranean corridor through Catalonia, Valencia, Murcia and Andalusia (the regional list is my geographic inference).
- **Day-to-day reality:** Drivers check for theft after sleeping in the cab. A lack of secure parking discourages new drivers.
- **Evidence:**
  - There are "about 20,000 robberies a year in goods transport, especially on the AP-7" ([trans.info, 31 Mar 2026](https://trans.info/es/espana-sin-camioneros-465872); **single source**, and the underlying data source is not named).
  - Limited access to secure parking and rest areas is cited as a barrier to recruitment ([trans.info, 24 Aug 2026](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)). CETM asks for "áreas de descanso seguras" (secure rest areas) ([Bolsamanía, 4 Feb 2026](https://www.bolsamania.com/noticias_amp/empresas/economia--los-transportistas-piden-medidas-reales-ante-la-grave-falta-de-camioneros-y-critican-trabas-administrativas--21606838.html)).
- **Scale:** About 20,000 incidents a year (single source).
- **Cost/impact:** Not quantified (gap).
- **Driver & status:** A market and infrastructure problem; no regulation identified.
- **How it is solved today:** Telematics alarms and paid secure parking (not verified).
- **Software-solvable?:** **Partly.** Software can book secure parking and raise theft alerts. Physical infrastructure is the real fix.
- **Confidence:** Low-medium.

### IND-08: Last mile and urban delivery: a patchwork of city rules, seasonal peaks and new EU customs paperwork
- **Who:** Couriers, parcel companies and their subcontracted van autónomos. Also e-commerce logistics operators (micro to medium).
- **Where:** City-specific. In UNO's directory, Madrid, Barcelona, Sevilla and Málaga have a "Ordenanza Definitiva" (final mobility ordinance), while Valencia, Zaragoza and Bilbao are "Pendiente Borrador ZBE" (low-emission-zone draft still pending) ([UNO, Ordenanzas de movilidad directory, accessed Oct 2026](https://unologistica.org/proyectos-e-informes/ordenanzas-de-movilidad/)).
- **Day-to-day reality:** Each city has its own ordinance and low-emission-zone rules, and many are still in draft. Peak seasons stretch capacity. Cross-border e-commerce parcels now carry a per-item EU customs duty and new data requirements.
- **Evidence:**
  - Ley 7/2021 required municipalities of more than 50,000 inhabitants to adopt mobility plans "antes de 2023" (before 2023). Most have not defined a final low-emission zone or ordinance (UNO directory, above).
  - More than 127 million shipments are expected over Black Friday and Christmas 2026, +2.4% on 2025 ([UNO press release, 15 Oct 2026](https://unologistica.org/sala-de-prensa/nota-de-prensa/la-logistica-gestionara-durante-el-black-friday-y-la-navidad-un-24-mas-de-envios-que-en-2025/)).
  - Final-mile parcel delivery is exempt from the DeCA ([Fenadismer training PDF, May 2026](https://www.fenadismer.es/wp-content/uploads/Pildora-formativa.-todo-sobre-el-Documento-Electronico-de-Control.pdf)).
  - From 1 Jul 2026 the EU charges a flat €3 customs duty on non-EU e-commerce consignments of up to €150, **per item line rather than per parcel**. Product identifiers (PIDs) were voluntary from 1 Jul and become mandatory from 1 Nov 2026 ([trans.info, 29 Jun 2026](https://trans.info/es/revolucion-de-julio-en-el-transporte-europeo-tacografos-en-furgonetas-cajas-negras-en-camiones-y-nuevos-peajes-486204); single trade-press source).
  - Ley 9/2025 amends LOTT art. 42 so vehicles limited to 40 km/h (for example small delivery vehicles) are exempt from transport authorisation. It also promotes bicycles for the "último tramo del reparto de mercancías" (last leg of goods delivery) ([BOE, Ley 9/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545)).
- **Scale:** UNO has more than 350 members ([UNO](https://www.unologistica.org/)). 127 million or more peak-season shipments.
- **Cost/impact:** Not quantified. Loading-zone fines and time limits were not verified (gap).
- **Driver & status:** Municipal ordinances: final in Madrid, Barcelona, Sevilla and Málaga; still in draft in Valencia, Zaragoza and Bilbao. EU €3 duty **in force** since 1 Jul 2026; PID requirement from 1 Nov 2026. (Low-emission zones themselves are another researcher's topic.)
- **How it is solved today:** Not verified. The examples I would expect (route-planning SaaS, municipal loading-zone apps) could not be checked because the pages would not load.
- **Software-solvable?:** **Partly.** Software can provide a rules database per city, plan routes and handle customs product data for cross-border parcels. Kerb space and city infrastructure are not software.
- **Confidence:** Low-medium.

### IND-09: Sustainable-mobility-law duties for larger logistics employers (mobility plans, EDIM data)
- **Who:** Logistics and warehouse operators with more than 200 workers or 100 per shift, so medium firms and up. Most SMEs are **exempt**.
- **Where:** National.
- **Day-to-day reality:** Large warehouses must draw up sustainable work-mobility plans and may have to supply data to the State mobility data platform (EDIM, Espacio de Datos Integrado de Movilidad).
- **Evidence:**
  - Ley 9/2025 makes "las empresas con más de 200 personas trabajadoras o 100 por turno" (companies with more than 200 workers or 100 per shift) responsible (art. 104 b). Missing the plan deadline is a minor infraction (art. 106.2 a). Transport operators must supply data to EDIM, and supplying false data is a serious infraction. Fines are €101–2,000 for minor and €2,001–6,000 for serious infractions (art. 107) ([BOE, Ley 9/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545)).
  - RDL 7/2026 cut the deadline for mobility plans from 24 to 12 months ([BOE, RDL 7/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544); taken from a summary, the article text was not read).
- **Scale:** Only large employers. The count is unknown.
- **Cost/impact:** Fines of €101–6,000.
- **Driver & status:** Ley 9/2025, **in force** since 5 Dec 2025. The plan deadline is in art. 26, which was not read.
- **How it is solved today:** Not verified (presumably mobility consultancies).
- **Software-solvable?:** **Yes.** Software can run employee mobility surveys, generate plans and report data to EDIM. The market is narrow because SMEs are exempt.
- **Confidence:** Medium. This overlaps with the bureaucracy and HR researchers.

### Inferences
- The DeCA turns every Spanish domestic freight movement into a digital transaction with a QR code and a one-year retention duty. Basic issuance is already priced at about €5/month (Fenadismer). The money is more likely in **reliability and dispute evidence**: guaranteed repository uptime, offline inspection proof, shipper–carrier data validation and a fine-appeal record. Such a layer would sit naturally next to **fuel-indexation invoicing** (IND-02) and **detention-claim timestamps** (IND-06), since all three run on the same trip record.
- Fenadismer's complaints show the power balance: large shippers set the platform and push the compliance work onto small carriers. A carrier-side, neutral tool that interoperates with shippers' platforms answers a demand the associations have documented.
- Late payment is improving (83 days in 2021, 52 days in Aug 2026), so a stand-alone collections tool for hauliers faces a shrinking pain. Bundling it with fuel-indexation enforcement looks stronger.

### Gaps
- No verified **TMS prices** and no **published prices** from Timocom or Wtransnet (both quote-only; Timocom's homepage shows no pricing).
- **City loading-zone (DUM) rules** for Madrid, Barcelona (Àrea DUM), Valencia, Sevilla, Zaragoza, Málaga and Bilbao: the pages were unavailable (503).
- The **smart tachograph v2 retrofit deadline for heavy international trucks** (believed to be 2025) and Mobility Package posting-declaration burdens were not verified.
- The RDL 3/2022 **ban on drivers loading and unloading**: my BOE extract of Ley 15/2009 art. 20 showed no express ban, so it is unverified.
- 2025–2026 figures from the **Observatorio de Costes** (cost per km) were not found. A datos.gob.es data request dated 30/06/2026 asks for the historical series ([datos.gob.es](https://datos.gob.es/es/solicitud-de-datos/series-historicas-estructuradas-del-observatorio-de-costes-del-transporte-de)).
- No data on how often carriers claim statutory **paralización** compensation.
- Whether Congress **validated** RDL 9/2026 and RDL 25/2026 was not verified.
- **eCMR adoption** by Spanish SMEs.

---

## Key question 2: Manufacturing and industrial SMEs: energy, skills, digitalisation, compliance

### Takeaway
For Spanish manufacturers the 2026 pain is **energy volatility and reliability** (the 2025 blackout, then the 2026 gas and oil shock) rather than the electricity price level, which stays well below the EU average. On top of that comes a wave of **EU product and supply-chain compliance**: packaging EPR and the PPWR from 12 Aug 2026, CBAM's definitive regime since 1 Jan 2026, EUDR from 30 Dec 2026, and the Machinery Regulation from 20 Jan 2027. There are also **occupation-specific skill shortages** (welders, mechanics, machine operators). A basic ERP is not the gap: Spanish firms with 10 or more staff use ERP more than the EU average.

### Cited Findings
The structured entries IND-10 to IND-17 follow.

### IND-10: Energy volatility and supply reliability (the 2025 blackout and the 2026 gas/oil shock)
- **Who:** Manufacturing SMEs (small and medium), the food industry (cold chain) and cooperatives' processing plants.
- **Where:** National. The blackout covered the whole peninsula.
- **Day-to-day reality:** Plants lost a day's production on 28 Apr 2025. In 2026 gas and fuel prices spiked again. Firms are now juggling temporary tax cuts, a window to change contracted volumes, and aid whose levels depend on CPI triggers.
- **Evidence:**
  - CEOE estimated losses from the 28 Apr 2025 blackout at **€1.6bn**. The ENTSO-E/ACER expert panel's final report (20 Mar 2026) identified many interacting causes, including gaps in voltage and reactive-power control. RDL 7/2025 (24 Jun 2025), which contained grid and storage measures, was **repealed by Parliament in July 2025**. Running gas plants for voltage stability added about 1 c€/kWh (Bloomberg, 19 May 2025) ([Wikipedia, 2025 Iberian Peninsula blackout, citing these sources](https://en.wikipedia.org/wiki/2025_Iberian_Peninsula_blackout); secondary source).
  - Non-household electricity (500–1,999 MWh band, excluding VAT), in €/kWh ([Eurostat nrg_pc_205 via API](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_205?geo=ES&geo=DE&geo=FR&geo=IT&geo=PT&geo=EU27_2020&nrg_cons=MWH500-1999&tax=X_VAT&currency=EUR&unit=KWH&sinceTimePeriod=2024-S1)):
    - 2026-S1: Spain 0.1336, EU27 0.1800, Germany 0.2058 (provisional), Italy 0.2253, France 0.1567, Portugal 0.1273.
    - 2024-S2: Spain 0.1426.
  - In the 2026 shock TTF spot gas rose 55% in two weeks to above €50/MWh. RDL 7/2026 for industry:
    - cut access tolls (peajes) for electro-intensive consumers;
    - allowed contracted gas and electricity volumes to be adjusted without extra charges until the end of 2026;
    - topped up compensation for indirect CO₂ costs;
    - cut the electricity tax from 5.11% to 0.5% until 30 Jun 2026 ([BOE, RDL 7/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544)).
  - RDL 25/2026 allows a possible 0.5% electricity tax in November and December if electricity CPI exceeds 15%, with a minimum of €0.5/MWh for industrial uses (low-voltage irrigation counts as industrial). It also puts generation plants of 0.5 MW or more under new voltage-control obligations from three months after its entry into force ([Cooperativas Agro-alimentarias summary, Oct 2026](https://www.agro-alimentarias.coop/docs_download/apoyar-al-campo-y-a-las-cooperativas-para-hacer-frente-al-impacto-de-la-crisis-energetica)). That last point may touch large industrial self-consumption plants; this is my inference.
- **Scale:** Nationwide. No SME-level survey was found.
- **Cost/impact:** €1.6bn from the blackout (CEOE). The size of the 2026 gas spike on SME bills is not quantified.
- **Driver & status:** A market shock. RDL 7/2026 and RDL 25/2026 are **in force**, with measures to 30 Jun and 31 Dec 2026. RDL 7/2025 was **repealed**.
- **How it is solved today:** Energy brokers and consultants, PPAs and self-consumption (none of the prices verified).
- **Software-solvable?:** **Partly.** Monitoring, re-optimising contracts while the flexibility window is open, and tracking eligibility for tax relief and aid can be software. Prices and grid reliability cannot.
- **Confidence:** High on the facts. Medium on what it means for SMEs.

### IND-11: Shortage of skilled technical trades (welders, mechanics, machine operators, technicians)
- **Who:** Small and medium manufacturers, metalworking and the food industry.
- **Where:** National, with regional variation ([EURES, updated 24 Feb 2025, data to Dec 2024](https://eures.europa.eu/living-and-working/labour-market-information/labour-market-information-spain_en)):
  - Galicia: welders, vehicle mechanics.
  - Basque Country: electricians, industrial engineers.
  - Navarra: electrical engineers and technicians, crane operators.
  - Castilla-La Mancha: industrial electricians, welders.
  - Catalonia: vehicle mechanics.
  - Murcia: machine-tool operators, welders, electricians, forklift operators.
- **Day-to-day reality:** Firms cannot fill trade roles even though overall vacancy rates are low, so the shortage is specific to certain occupations.
- **Evidence:**
  - The national 2024 shortage list includes "stationary plant and machine operators". In industry the shortages are welders, mechanics, machine-tool operators and industrial technicians (EURES, above).
  - Spain's job vacancy rate was **0.9% in 2023, against an EU27 average of 2.8%** (EURES, above). This contradicts any general labour-shortage story.
- **Scale:** Not quantified for manufacturing SMEs (gap).
- **Cost/impact:** Not quantified.
- **Driver & status:** A market and demographic problem; no regulatory driver.
- **How it is solved today:** Not verified (FP dual vocational training, temp agencies).
- **Software-solvable?:** **Partly.** Training, knowledge capture and maintenance work instructions can be software. The shortage itself cannot.
- **Confidence:** Medium. This rests on a single official aggregator and overlaps with the HR researcher.

### IND-12: Packaging EPR (RD 1055/2022) plus the EU PPWR from 12 Aug 2026
- **Who:** Manufacturers and food and drink SMEs (micro to medium) that place packaged goods on the market, including commercial and industrial (B2B) packaging.
- **Where:** National, plus the EU single market.
- **Day-to-day reality:** Firms must register as packaging producers, declare tonnes placed on the market every year, join and pay a collective system (or set up their own), mark packaging, and now redesign labels and recyclability documentation for the EU regulation.
- **Evidence:**
  - RD 1055/2022:
    - Producers of commercial and industrial packaging who had no previous obligation had to set up extended-producer-responsibility systems "antes del 31 de diciembre de 2024" (before 31 Dec 2024), with applications before 31 Dec 2023.
    - Marking obligations (art. 13) apply "desde el 1 de enero de 2025" (from 1 Jan 2025).
    - Producers must register in the packaging section of the Registro de Productores de Productos.
    - Annual data is due before 31 March. Firms placing under 15 t a year may report in simplified form. When a producer places under 50,000 kg of commercial and industrial packaging, its manufacturer, importer or acquirer registers on its behalf.
    - Collective-system fees must appear separately on invoices.
    - Separate collection of industrial packaging must reach 75% in 2027, 85% in 2030 and 95% in 2035 ([BOE, RD 1055/2022 consolidated](https://www.boe.es/eli/es/rd/2022/12/27/1055/con)).
  - The PPWR (Regulation (EU) 2025/40) has been in force since 11 Feb 2025 and **applies from 12 Aug 2026**. Packaging must be recyclable by 2030. PFAS are limited in food-contact packaging, and reuse and deposit-return targets apply. A December 2025 Environmental Omnibus proposal would suspend the authorised-representative obligation for direct cross-border sellers; it is still under examination ([European Commission, packaging page](https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en)).
- **Scale:** Food and drink alone counts more than 27,300 companies, 483,300 jobs and €52,565M of exports ([FIAB](https://fiab.es/); reference year not shown).
- **Cost/impact:** Collective-system fees and admin (amounts not verified). RD 1055/2022 refers sanctions to Ley 7/2022 (amounts not read).
- **Driver & status:** RD 1055/2022 is **in force** (commercial and industrial EPR from end-2024, marking from 2025). The PPWR is **in force and applicable since 12 Aug 2026**. The Omnibus amendment is a **proposal**. (The plastic-packaging tax overlaps with the tax researcher.)
- **How it is solved today:** Collective-system membership, consultants and spreadsheets (prices not verified).
- **Software-solvable?:** **Yes.** Software can keep a packaging bill-of-materials inventory, compute tonnage by material, prepare the annual declaration and the fee lines on invoices, and check PPWR labelling and recyclability.
- **Confidence:** High on the obligations, which come from official texts.

### IND-13: CBAM definitive regime for importers (steel, aluminium, cement, fertilisers, hydrogen, electricity)
- **Who:** SME importers of covered goods, such as metalworking firms buying non-EU steel or fasteners, foundries, building-materials distributors, and fertiliser distributors and cooperatives (sizes micro to medium). The examples are my inference from the covered sectors.
- **Where:** National.
- **Day-to-day reality:** Importers must get authorisation, collect embedded-emissions data from non-EU suppliers, file declarations and buy and surrender CBAM certificates. Default values and benchmarks kept changing during 2026.
- **Evidence:**
  - CBAM "applies in its definitive regime from 1 January 2026". Importers must meet authorisation requirements, report, and buy and surrender certificates matching embedded emissions. Certificate prices follow EU ETS auction prices. Covered sectors are cement, iron and steel, aluminium, fertilisers, electricity and hydrogen ([European Commission, CBAM page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)).
  - Regulation (EU) 2025/2083 simplified CBAM (consolidated text dated 20 Oct 2025).
  - Default values were **corrected by Implementing Regulation (EU) 2026/1740** ("UPDATE JULY 2026"; definitive-period Excel dated 10 Aug 2026). Benchmarks are set in Implementing Regulation 2025/2620 (Excel dated 13 Feb 2026).
  - Proposal COM(2025) 989 would **extend CBAM to downstream goods** and add anti-circumvention measures ([European Commission, CBAM legislation and guidance](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en)).
- **Scale:** The number of Spanish CBAM importers is not found (gap).
- **Cost/impact:** Certificate costs at ETS-linked prices plus data and verification costs (not quantified).
- **Driver & status:** Regulation (EU) 2023/956 as amended by 2025/2083. Definitive regime **in force since 1 Jan 2026**. The downstream extension is a **proposal**.
- **How it is solved today:** Customs brokers and consultants (prices not verified).
- **Software-solvable?:** **Yes.** Software can collect supplier emissions data, monitor thresholds, prepare declarations and track certificate needs.
- **Confidence:** Medium-high. The official framework is verified, but the SME-relevant thresholds are not (see Gaps).

### IND-14: EU Deforestation Regulation (EUDR) due diligence: deadline 30 Dec 2026
- **Who:** Importers, processors and traders of cattle, wood, cocoa, soy, palm oil, coffee and rubber and their derived products (leather, chocolate, tyres, furniture). In practice that means furniture and carpentry SMEs, chocolate makers, coffee roasters, feed mills using soy and tanneries (these examples are my inference from the commodity list).
- **Where:** National.
- **Day-to-day reality:** Firms need plot geolocation and due-diligence statements from upstream suppliers before placing goods on the market. Micro and small firms get six more months.
- **Evidence:**
  - Application dates:
    - **30 Dec 2026** for large and medium operators.
    - **30 Jun 2027** for micro and small operators.
    - 30 Dec 2026 for micro and small firms already covered by the EU Timber Regulation.
    - 30 Dec 2027 for products added by Delegated Regulation (EU) 2026/2102 (soluble coffee, certain palm-oil derivatives, frozen cattle tongues).
  - The regulation was amended in December 2024 (Reg. 2024/3234) and in December 2025 (simplification) ([European Commission, EUDR page](https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en)).
- **Scale:** Not quantified for Spain (gap).
- **Cost/impact:** Not quantified.
- **Driver & status:** Regulation (EU) 2023/1115. **Upcoming deadline**, after two postponements.
- **How it is solved today:** Not verified.
- **Software-solvable?:** **Yes.** Software can collect supplier geolocation, run risk checks and prepare due-diligence statements.
- **Confidence:** High on the dates. Low on Spanish SME impact.

### IND-15: New EU Machinery Regulation applies from 20 Jan 2027
- **Who:** Machinery manufacturers and integrators (small and medium).
- **Where:** National. Where these firms cluster was not verified.
- **Day-to-day reality:** Technical files, conformity routes, cybersecurity of safety software and digital instructions all have to be reworked for machinery placed on the market from 20 Jan 2027.
- **Evidence:** Regulation (EU) 2023/1230 "applies on a mandatory basis as of 20 January 2027". Machinery placed earlier stays under Directive 2006/42/EC. The new rules cover AI-based safety functions, cyber-safety of safety-relevant software, higher-risk machinery assessment, and digital instructions and declarations of conformity. The page mentions no postponement ([European Commission, machinery page](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en)).
- **Scale:** Not quantified (gap).
- **Cost/impact:** Not quantified.
- **Driver & status:** **Upcoming (20 Jan 2027).**
- **How it is solved today:** Notified bodies and consultants (not verified).
- **Software-solvable?:** **Partly to yes.** Software can manage technical files and risk assessments, host digital instructions and hold cybersecurity documentation.
- **Confidence:** Medium.

### IND-16: Digitalisation: compliance-ready ERP and manufacturing modules for small manufacturers
- **Who:** Small manufacturers (10–49) and micro firms (under 10).
- **Where:** National.
- **Day-to-day reality:** Most firms with 10 or more staff already run an ERP. The friction is bolting on the new compliance modules (DeCA, packaging EPR, CBAM, EUDR, food-chain contract registration) and keeping micro firms off spreadsheets.
- **Evidence:**
  - In 2025, **60.38% of Spanish enterprises with 10 or more staff used ERP, against an EU average of 46.45%**. EU ERP use by size is 41.08% for small, 69.93% for medium and 88.71% for large firms. EU CRM use is 28.51%. EU AI use is 19.95% overall and 17% for small firms ([Eurostat, Digital economy and society statistics – enterprises](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_enterprises)).
  - Odoo's Spanish pricing page (prices shown in US$):
    - "Estándar" US$31.10 per user/month billed annually, or US$38.90 monthly.
    - "Personalizado" US$61.00 annually or US$76.20 monthly.
    - Both include all apps, including Manufacturing, Quality, Maintenance and PLM. Implementation success packs are extra and unpriced ([Odoo pricing](https://www.odoo.com/es_ES/pricing)).
  - Ekon is now sold as "Cegid Ekon XRP" for mid-size industry and distribution, with no public price ([Cegid; ekon.es redirects here](https://www.cegid.com/ib/es/productos/erp-empresas-medianas-xrp-enterprise/)).
  - Sage 200 and a3ERP pages refused automated access (HTTP 403), so their prices are **not verified**.
- **Scale:** About 40% of Spanish firms with 10+ staff have no ERP (my arithmetic from Eurostat). Micro firms are not measured.
- **Cost/impact:** Not quantified.
- **Driver & status:** Market. The compliance pull comes from IND-01, IND-12, IND-13, IND-14 and IND-18.
- **How it is solved today:** Odoo (from US$31.10/user/month), Cegid Ekon, Sage and a3 (prices unverified), and spreadsheets.
- **Software-solvable?:** **Partly.** The basic ERP market is crowded. Vertical compliance add-ons are the gap.
- **Confidence:** Medium.

### IND-17: US tariff turbulence for exporters (machinery, metals, agrifood)
- **Who:** Exporting SMEs (small and medium) in machinery, steel and aluminium products, and agrifood.
- **Where:** National.
- **Day-to-day reality:** US tariff rules changed several times in a year: legal challenges, replacement tariffs and refunds. That makes pricing and contracts with US buyers hard.
- **Evidence:** All from [Wikipedia, Tariffs in the second Trump administration](https://en.wikipedia.org/wiki/Tariffs_in_the_second_Trump_administration). The article carries a maintenance notice, so it is a secondary source.
  - Section 232 steel and aluminium tariffs went to 50% on 4 Jun 2025. In April 2026 they were restructured: 50% for articles made almost entirely of these metals, 25% for substantially derivative articles, and 15% for certain industrial and grid equipment through 2027.
  - Auto tariffs are 15% for the EU.
  - On 20 Feb 2026 the US Supreme Court ruled 6-3 in *Learning Resources v. Trump* that IEEPA does not authorise tariffs. About US$166bn is to be refunded, through a CBP portal opened in April 2026.
  - A 10% global tariff under Section 122 ran until 24 Jul 2026. The Court of International Trade ruled it illegal on 7 May 2026, and the ruling is on appeal.
  - From 24 Jul 2026 Section 301 tariffs of 10% or 12.5% cover 60 partners including the EU, with some exemptions (for example cork).
- **Scale:** **Spanish export figures were not found (gap).**
- **Cost/impact:** Not quantified for Spain.
- **Driver & status:** US trade policy. Section 301 at 10% applies to the EU from 24 Jul 2026. IEEPA tariffs were **struck down** on 20 Feb 2026.
- **How it is solved today:** ICEX support, customs brokers and US importers of record (not verified).
- **Software-solvable?:** **Partly.** HS classification, landed-cost scenarios and duty or refund tracking can be software. The policy cannot.
- **Confidence:** Medium.

### Inferences
- Spain's industrial electricity price advantage (€0.1336/kWh against €0.1800 for the EU in 2026-S1) means a "cheaper electricity" pitch is weak. **Volatility, gas and fuel exposure, and reliability**, together with the paperwork of temporary tax cuts and aid, are stronger hooks.
- The common thread for manufacturers is a **stack of EU product and supply-chain data obligations** (packaging, CBAM, EUDR, Machinery Regulation) landing between 2025 and 2027. Each needs supplier data, product master data and declarations. A modular "product compliance data hub" that sits on top of an existing ERP fits better than a new ERP.
- The low overall vacancy rate (0.9%) suggests manufacturing skill pains are niche-trade problems. Software for knowledge capture or maintenance instructions would solve only a part of them.

### Gaps
- The CBAM **50-tonne de minimis threshold**, the share of importers exempted, authorised-declarant deadlines and the certificate sales start date. EUR-Lex returned empty pages and the EC Q&A URL gave a 404, so none of this is verified.
- The number of **Spanish CBAM importers** and the Spanish competent authority.
- **Industrial-safety registrations** (Registro Integrado Industrial, periodic inspections by authorised inspection bodies, the industrial fire-safety rules): nothing was fetched or verified.
- **ESG data requests from large customers** (VSME): not researched. This overlaps with the cross-sector ESG researcher.
- **Sage 200, a3ERP and SAP Business One prices**: pages blocked or not public.
- **Spanish export data to the US** in 2025–2026 (olive oil, wine, machinery).
- An SME-level energy cost survey for 2026.
- Robot density and automation figures for Spanish SMEs (Eurostat's page had no robotics figures).

---

## Key question 3: Agriculture, fishing and agrifood: farm paperwork, food-chain law, water, labour, inputs

### Takeaway
The best-documented pain is **food-chain-law contract compliance**. AICA sanctioned 991 infractions in 2025, and 51% of them were failures to register contracts in the digital food-contract register (RCA) before delivery, almost all by the "industry" link and concentrated in wine-grape purchases. Next comes the **2026 input-cost shock** (diesel, fertilisers) with its monthly aid and tax-relief paperwork, and farm-record duties. The digital farm notebook (CUE) has been **postponed to the next CAP programming period**, but the **fertilisation plan obligation started on 1 Sep 2026**. Fishing fleets face a fuel spike plus a 44% cut in Mediterranean trawl days. Water (Tajo-Segura), animal-disease trade bans (lumpy skin disease and live-cattle exports to Morocco) and Mercosur are severe but mostly not software-solvable.

### Cited Findings
The structured entries IND-18 to IND-25 follow.

### IND-18: Food-chain law: written contracts, cost-of-production pricing, pre-delivery RCA registration and payment terms
- **Who:** Buyers of primary products: food-industry SMEs (small and medium), wholesalers in origin and destination markets, retailers, and cooperatives buying from non-members. Farmers (autónomos and micro) are the counterparty.
- **Where:** National. AICA's 399 on-site inspections in 2025 were spread as follows: fruit and vegetables 224, meat 53, dairy 28, wine 22, olive 15.
- **Day-to-day reality:** For every purchase from a farmer the buyer needs a signed written contract with minimum terms, including a price above the producer's costs. Each contract and each change must be uploaded to the RCA **before delivery**. Missing that step is now the most common sanctioned infraction.
- **Evidence:**
  - AICA 2025 headline figures ([AICA, Memoria Anual 2025, published 24 Sep 2026](https://www.aica.gob.es/content/dam/aica/docs/publicaciones/memorias/Memoria_Anual_de_Actividades_2025.pdf)):
    - 399 on-site inspections, 2,978 commercial relationships checked and 28 complaints investigated.
    - **991 infractions sanctioned**; 109 companies sanctioned (99 in 2024).
    - Since 2014: 4,947 infractions and **€27,923,451 in fines** (€17,311,313 actually paid).
  - Infractions by type in 2025 (same report):
    - **506 failures to register in the RCA (51%), all in the "industria" link.**
    - 186 payment-term breaches (124 wholesalers, 38 industry, 24 retail).
    - 98 contracts missing minimum terms, 67 of them missing the price.
    - 74 with no written contract.
    - 53 price changes not agreed by both parties.
    - 50 cases of obstructing inspectors.
  - Other 2025 figures (same report):
    - 66 warnings, including 31 in fruit and vegetables for not registering contracts and 30 in pork for missing minimum terms.
    - 82 sanctions published.
    - The RCA went live in Dec 2022 and is sized for 30 million documents a year and 300,000–400,000 users. Its help desk has handled 3,266 queries and incidents (700 in 2025). An API exists for high-volume buyers.
  - Ley 12/2013:
    - contracts in writing before delivery (art. 8.1);
    - the price "deberá ser, en todo caso, superior al total de costes asumidos por el productor" (must always exceed the producer's total costs) (art. 9.1.c);
    - every operator pays the previous one "un precio igual o superior al coste de producción" (a price equal to or above the cost of production) (art. 12 ter);
    - RCA registration before delivery (art. 11 bis), with non-registration a minor infraction (art. 23.1.k).
    - Fines: minor €250–3,000, serious €3,001–100,000, very serious €100,001–1,000,000, capped at 5% or 10% of turnover ([BOE, Ley 12/2013 consolidated](https://www.boe.es/eli/es/l/2013/08/02/12/con)).
  - The RCA is regulated by RD 1028/2022. The buyer registers, or the integrator in integration contracts. Contracts between a cooperative and its members are exempt, but a cooperative buying from non-members must register. Uploads are by web form with a digital certificate (up to 5 documents and 5 MB per upload) or by API ([AICA, RCA FAQ](https://www.aica.gob.es/servicios-en-linea/Registro%20de%20Contratos%20Alimentarios/preguntas-frecuentes-rca)).
  - On 30 Sep 2026 AICA opened a public consultation on a new Real Decreto for its inspection regime ([AICA homepage](https://www.aica.gob.es/)).
- **Scale:** More than 27,300 food and drink companies ([FIAB](https://fiab.es/)) and 3,669 agri-food cooperatives ([Cooperativas Agro-alimentarias](https://www.agro-alimentarias.coop/datos-cooperativismo)), plus wholesalers.
- **Cost/impact:** Fines from €250 up to €1M per infraction; €27.9M in fines since 2014. Fines for serious and very serious infractions are published, which names the company.
- **Driver & status:** Ley 12/2013 as amended by Ley 16/2021 (in force), and RD 1028/2022 (RCA operating since Dec 2022). A new AICA inspection decree is a **draft** (consultation 30 Sep 2026).
- **How it is solved today:** Manual RCA uploads, the RCA API for large buyers, and gestorías or consultants (prices not verified).
- **Software-solvable?:** **Yes.** Software can generate contracts with a cost-of-production clause, register them in bulk through the RCA API before the weighbridge or delivery event, manage amendments and monitor payment terms.
- **Confidence:** High (official enforcement data).

### IND-19: Wineries buying grapes: sanctions concentrated in wine
- **Who:** Wineries (bodegas, small and medium) and wine cooperatives buying from non-members. Grape growers are the counterparty.
- **Where:** National. AICA gives no regional breakdown.
- **Day-to-day reality:** At harvest wineries receive grapes from many growers within days. Each purchase needs a written, registered contract before delivery, plus monthly wine-market declarations.
- **Evidence:**
  - **619 of the 991 infractions sanctioned in 2025 (62%) were in the wine sector, 616 of them on wine grapes (uva de vinificación).** Wine had only 22 inspections that year. Since 2014 there have been 34 complaints in wine, 24 of them about grapes ([AICA Memoria 2025](https://www.aica.gob.es/content/dam/aica/docs/publicaciones/memorias/Memoria_Anual_de_Actividades_2025.pdf)).
  - INFOVI, the wine market information system, handled 44,826 declarations and 1,003 reports in 2025 (same source).
  - FEV, the Spanish wine federation, has more than 950 member wineries, which account for 83% of bottled-wine value ([FEV](https://www.fev.es/)).
- **Interpretation (inference):** Industry accounts for all 506 RCA failures and wine grapes for 616 infractions. Together this suggests that **harvest-time grape contracts not registered before delivery** drive most of the wine infractions. AICA does not publish this cross-tabulation.
- **Scale:** National wine sector (more than 950 FEV members).
- **Cost/impact:** Fines from €250–3,000 (minor) up to serious levels.
- **Driver & status:** Ley 12/2013 and RD 1028/2022 (**in force**).
- **How it is solved today:** Not verified (winery ERPs, gestorías).
- **Software-solvable?:** **Yes.** Software can create grower contracts and register them through the RCA API from weighbridge receipts in real time, and handle INFOVI declarations.
- **Confidence:** Medium-high. The numbers are official; the reading of the cause is inference.

### IND-20: Farm records: the fertilisation plan and records apply now, the digital farm notebook (CUE) is deferred
- **Who:** Farmers (autónomos, micro and small), agronomic advisers and cooperatives' technical services.
- **Where:** National, with regional administration of the records.
- **Day-to-day reality:** Farmers face shifting digital-record rules. Each fertilisation must be logged within a month and a plan de abonado (fertilisation plan) is needed from 1 Sep 2026. The full CUE obligation has been pushed back to the next CAP programming period, which leaves farmers and software vendors unsure what to adopt.
- **Evidence:**
  - RD 1054/2022, final provision 8: the CUE becomes "de obligado cumplimiento para el siguiente periodo de programación de la PAC" (mandatory for the next CAP programming period). It will apply to farms with more than 30 ha of permanent crops and arable land, more than 5 ha irrigated, or more than 0.1 ha of greenhouses. Administrations must offer free software for voluntary use. Phytosanitary data must be supplied "al menos, con carácter mensual" (at least monthly). The consolidated text was last updated 22/01/2025 ([BOE, RD 1054/2022 consolidated](https://www.boe.es/eli/es/rd/2022/12/27/1054/con)).
  - RD 1051/2022 (BOE-A-2022-23052, consolidated 03/11/2025) ([BOE, RD 1051/2022 consolidated](https://www.boe.es/eli/es/rd/2022/12/27/1051/con)):
    - each fertilisation must be recorded in the farm notebook **within one month**;
    - a **plan de abonado is required "a partir del 1 de septiembre de 2026"** (from 1 Jan 2026 for irrigated units sown between 1 Mar and 30 Jun 2026);
    - fertilisation advisers must register in REGFER from **1 Jul 2026**;
    - agronomic advice becomes mandatory one year after the plan obligation in vulnerable zones and two years after elsewhere;
    - soil analyses every 5 years (irrigated) or 10 years (rainfed) once sampling guides are published;
    - exemptions: farms of 5 ha or less with 1 ha or less irrigated (records), and rainfed units of 10 ha or less (plan).
  - Complaint: "una carga burocrática inasumible, donde al productor se le trata como presunto defraudador" ("an unbearable bureaucratic burden in which the producer is treated as a presumed fraudster") ([Cooperativas Agro-alimentarias, 23 Oct 2026](https://www.agro-alimentarias.coop/posts/cooperativas-agro-alimentarias-de-espana-apoya-la-movilizacion-del-28-de-octubre-dar-de-comer-tiene-que-dar-para-vivir)).
  - Administrative simplification "so farmers can spend more time producing" is one of five demands of the 28 Oct 2026 tractorada (tractor protest) in Madrid ([ASAJA, 21 Oct 2026](https://www.asaja.com/gran-tractorada-del-28-de-octubre-en-madrid-dar-de-comer-tiene-que-dar-para-vivir/)).
  - Cooperativas Agro-alimentarias shows a rollout map for a "Cuaderno de Campo Cooperativo" (cooperative field notebook) ([Cooperativas homepage](https://www.agro-alimentarias.coop/)).
- **Scale:** More than 1 million cooperative member families and 3,669 cooperatives ([Cooperativas datos](https://www.agro-alimentarias.coop/datos-cooperativismo)). The number of farms above the CUE thresholds was not found (gap).
- **Cost/impact:** Time spent on records and advisers' fees (not quantified).
- **Driver & status:** The CUE is **postponed** to the next CAP programming period. Since the current CAP Strategic Plan runs to 2027, I infer that means 2028 or later. The plan de abonado is **in force from 1 Sep 2026** and REGFER registration from 1 Jul 2026. The norm that inserted the CUE postponement was not identified (BOE version of 22/01/2025).
- **How it is solved today:** Free public CUE software, cooperatives' notebooks, advisers, and private farm apps (prices not verified).
- **Software-solvable?:** **Yes.** Software can generate fertilisation plans, log operations within the one-month window, run adviser workflows and export to SIEX, while staying ready for the CUE.
- **Confidence:** High on the obligations (official). Medium on how heavy the burden is.

### IND-21: 2026 input-cost shock (diesel, fertilisers, energy) and the paperwork of aid and tax relief
- **Who:** Farmers and livestock keepers (autónomos and micro) and cooperatives, which buy fuel and inputs jointly.
- **Where:** National. Protests took place in Puertollano (Castilla-La Mancha) on 9 Oct 2026 and in Madrid on 28 Oct 2026. Rice prices are below cost in the Ebro Delta (Catalonia).
- **Day-to-day reality:** Agricultural diesel and fertiliser costs rose with the Iran war. Farmers claim aid through the partial excise-refund procedure and wait on tax relief in the IRPF "módulos" (flat-rate income tax) regime. Producer prices do not cover costs.
- **Evidence:**
  - RDL 7/2026 created an extraordinary aid for agricultural diesel, a separate aid for fertiliser costs, and an expanded ICO-MAPA-SAECA credit line ([BOE, RDL 7/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544)).
  - RDL 25/2026 extends the agricultural diesel aid to **31 Dec 2026** ([Cooperativas Agro-alimentarias summary, Oct 2026](https://www.agro-alimentarias.coop/docs_download/apoyar-al-campo-y-a-las-cooperativas-para-hacer-frente-al-impacto-de-la-crisis-energetica)):
    - the aid is up to 70% of the gap between the weekly average agricultural-diesel price and the pre-conflict price, capped at **€0.20/l**;
    - it is claimed through the partial excise-refund application, available since 1 Apr 2026;
    - beneficiaries may not make crisis-related dismissals until 31 Dec 2026;
    - the CNMC must study food-chain prices;
    - full effect depends on EU state-aid approval.
  - IRPF módulos relief: −35% for agricultural diesel purchases, −15% for fertilisers, plus a −10% general reduction. The sector saves more than €600M ([UPA, 22 Oct 2026](https://upa.es/upa-celebra-la-publicacion-de-la-orden-que-rebajara-la-carga-fiscal-de-gasoleo-y-fertilizantes-lo-hemos-conseguido/)). This overlaps with the tax researcher.
  - Protests:
    - Hundreds of UPA farmers protested at Repsol's Puertollano refinery over diesel and input costs on 9 Oct 2026 ([UPA](https://upa.es/trescientos-agricultores-de-upa-se-concentran-a-las-puertas-de-repsol-en-puertollano/)).
    - The 28 Oct 2026 tractorada in Madrid demands a "plan de choque" (emergency plan) on costs and a "gasóleo profesional agrícola" (professional diesel scheme for farmers) ([ASAJA](https://www.asaja.com/gran-tractorada-del-28-de-octubre-en-madrid-dar-de-comer-tiene-que-dar-para-vivir/)).
    - Unió de Pagesos rejects calling the Ebro Delta rice campaign "stable" while prices are below costs ([Unió de Pagesos, 22 Oct 2026](https://uniopagesos.cat/comunicat-de-premsa/rebutgem-que-es-qualifiqui-destable-la-campanya-darros-del-delta-de-lebre-quan-els-preus-estan-sota-costos/)).
- **Scale:** Sector-wide, including more than 1 million cooperative members.
- **Cost/impact:** More than €600M in tax relief. The input-price increases are **not quantified** in the sources fetched (gap).
- **Driver & status:** The Iran-war energy shock. RDL 7/2026 and RDL 25/2026 are **in force to 31 Dec 2026**.
- **How it is solved today:** Cooperatives' joint purchasing, gestorías for aid and tax, and the excise-refund procedure (no fees verified).
- **Software-solvable?:** **Partly.** Software can track aid and tax-relief claims, pool cooperative purchases and calculate cost of production, which also feeds IND-18's "price must exceed costs" rule. Input prices cannot be fixed by software.
- **Confidence:** High on the facts. Medium on the impact.

### IND-22: Fishing fleets: fuel spike, cuts to fishing days and new digital control duties
- **Who:** Fishing companies (micro and small, with some medium), cofradías (fishermen's guilds) and fish importers and processors (catch certificates).
- **Where:** Western Mediterranean trawlers (the WestMed plan) and the national fleet. Which regions are worst hit was not verified.
- **Day-to-day reality:** Fuel more than doubled in early 2026 and threatened to keep vessels in port. Mediterranean trawlers now get about 130 fishing days a year, and new EU control rules digitise catch reporting and traceability.
- **Evidence:**
  - Fuel went from €0.50–0.60/l in January to more than €1.30/l in many Spanish ports by April 2026 (€2.20 in other countries). "numerosos buques podrían verse obligados a cesar su actividad de forma inminente" ("many vessels could be forced to stop operating imminently"). CEPESCA asked for aid to rise from €0.20 to €0.50/l and for an exemption from Social Security contributions ([CEPESCA, 10 Apr 2026](https://cepesca.es/el-sector-pesquero-reclama-al-gobierno-medidas-urgentes-ante-el-inminente-amarre-de-la-flota/)).
  - Mediterranean trawl fishing days fell from about 230 a year (2019) to an average of about 130 (2026), a **44% cut**. CEPESCA says the sector is "al límite de su supervivencia" ("at the limit of its survival") ([CEPESCA, Senate hearing, 7 May 2026](https://cepesca.es/cepesca-advierte-en-el-senado-de-que-la-politica-pesquera-del-mediterraneo-pone-en-peligro-el-futuro-del-sector/)).
  - 87 zones were closed to bottom gear after the EU General Court rejected appeals ([CEPESCA, 2025](https://cepesca.es/cepesca-lleva-sus-reivindicaciones-a-bruselas-con-foco-en-el-cierre-de-87-zonas-a-la-pesca-de-fondo-y-en-la-defensa-de-la-pesca-de-arrastre-del-mediterraneo/)).
  - EU Control Regulation (EU) 2023/2842 ([European Commission, Control regulation](https://oceans-and-fisheries.ec.europa.eu/fisheries-management/enforcing-rules/control-regulation_en)):
    - in force since 9 Jan 2024; Implementing Regulation 2025/2196 adopted 17 Oct 2025;
    - **importers must use the CATCH IT tool for catch certificates from 10 Jan 2026**;
    - a 2026 implementing regulation on weighing;
    - vessel tracking (VMS) for all vessels, and remote electronic monitoring for high-risk vessels over 18 m;
    - some rules apply from 2026 and others from 2028.
  - RDL 7/2026 gave fishing compensatory aid for fuel and electricity and an exemption from the fresh-fish fee ([BOE, RDL 7/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-6544)).
- **Scale:** CEPESCA members alone run 725 vessels, more than 700 companies, about 8,000–10,000 crew and about 50% of national catches ([CEPESCA](https://cepesca.es/)).
- **Cost/impact:** Fuel more than doubled. Fishing days cut 44%.
- **Driver & status:** The energy shock, the WestMed multiannual plan (**in force**) and Control Regulation 2023/2842 (**phasing in 2026–2028**).
- **How it is solved today:** Public aid, and electronic logbook systems on larger vessels (not verified).
- **Software-solvable?:** **Partly.** E-logbooks, CATCH IT certificates, weighing records and traceability can be software. Fishing days, quotas and fuel prices cannot.
- **Confidence:** Medium. Sources are CEPESCA plus the EC. The deadline for small vessels under 12 m is unverified.

### IND-23: Water scarcity and uncertainty over the Tajo-Segura transfer
- **Who:** Irrigated farms and cooperatives (micro to medium) supplied by the Tajo-Segura transfer.
- **Where:** Región de Murcia (the source of the figures). The transfer also serves Alicante and Almería, but that is my inference and was not verified.
- **Day-to-day reality:** Transfer water is suspended until spring while an infrastructure breakdown (Liétor) waits to be repaired. Irrigators plan crops without knowing what water they will have.
- **Evidence:**
  - SCRATS, the transfer's irrigators' association, says the closure until April puts **€260M and 5,600 jobs** at risk in the Región de Murcia (Facebook post of 22 Oct 2026). It reports no visible repair progress a month after the Liétor breakdown, and that a court dismissed its appeal against the Tajo river plan (date not given) ([SCRATS homepage](https://www.scrats.es/); **single source, and an interest group**).
  - Cooperativas Agro-alimentarias asks for a "Plan Nacional del Agua" (national water plan) ([Cooperativas, 23 Oct 2026](https://www.agro-alimentarias.coop/posts/cooperativas-agro-alimentarias-de-espana-apoya-la-movilizacion-del-28-de-octubre-dar-de-comer-tiene-que-dar-para-vivir)).
- **Scale:** 5,600 jobs at risk (SCRATS figure).
- **Cost/impact:** €260M at risk (SCRATS figure).
- **Driver & status:** Infrastructure failure plus the Tajo hydrological plan. The court ruling date is unverified.
- **How it is solved today:** Desalinated water and wells (prices not verified).
- **Software-solvable?:** **Partly.** Irrigation optimisation and water accounting can help. Water allocation is political.
- **Confidence:** Low-medium.

### IND-24: Animal-disease trade bans (lumpy skin disease, Morocco) and emerging diseases
- **Who:** Cattle farmers and exporters (micro and small), live-animal traders.
- **Where:** The outbreak was in Catalonia and Aragón. The export impact is national.
- **Day-to-day reality:** After lumpy skin disease (dermatosis nodular contagiosa) appeared in north-eastern Spain at the end of 2025, Morocco closed its border to Spanish live cattle and has kept it shut for more than ten months.
- **Evidence:**
  - Morocco took sanitary precautions after the outbreak at the end of 2025, detected only in Catalonia and Aragón. Exports of beef cattle over 300 kg fell from 61,715 head (2024, 52% of live exports) to 51,986 (2025, 64%) to **0 in 2026**. UPA wants Morocco to accept regionalisation, and the Ministry meets its Moroccan counterpart at the end of November 2026 ([UPA, 16 Oct 2026](https://upa.es/upa-traslada-a-agricultura-el-clamor-del-vacuno-de-carne-debemos-recuperar-ya-las-exportaciones-a-marruecos/)).
  - Unió de Pagesos demands action protocols for the spread of the Shamonda virus and other emerging animal diseases ([Unió de Pagesos, 23 Oct 2026](https://uniopagesos.cat/comunicat-de-premsa/reclamem-protocols-dactuacio-davant-lexpansio-del-virus-de-shamonda-i-daltres-malalties-animals-emergents/)).
  - An avian influenza outbreak was declared in Andalusia on 9 Sep 2025 ([Wikipedia, 2025 in Spain](https://en.wikipedia.org/wiki/2025_in_Spain)).
- **Scale:** About 52,000 head a year of lost export volume.
- **Cost/impact:** The value is not quantified.
- **Driver & status:** Animal-health trade barriers. The ban is ongoing (Oct 2026).
- **How it is solved today:** Diplomatic regionalisation negotiations.
- **Software-solvable?:** **Partly.** Traceability and evidence of regional disease-free status can be software. Bans are political decisions.
- **Confidence:** Medium.

### IND-25: Food-waste law (Ley 1/2025): prevention plans and donation agreements
- **Who:** Food manufacturers, wholesalers and cooperatives' processing businesses with 10 or more staff or more than €2M turnover (small and medium). Microenterprises and small farms are **exempt**.
- **Where:** National. The autonomous communities define infractions in detail.
- **Day-to-day reality:** Covered firms must keep a prevention plan, follow a priority order for surplus food (donation first, then animal feed, then recycling), sign donation agreements and cooperate with waste measurement.
- **Evidence:**
  - Agents must "disponer de un plan de aplicación para la prevención de las pérdidas y desperdicio alimentario" (have a plan for preventing food loss and waste) and promote donation agreements unless they are unfeasible and justified. Any contractual ban on donation is void.
  - Microenterprises (fewer than 10 employees and €2M or less) are exempt, as are establishments of up to 1,300 m², and small farms are excluded.
  - Fines: minor up to €2,000 (for example not donating edible food where obliged); serious €2,001–60,000 (for example **having no prevention plan**); very serious €60,001–500,000. The art. 6 obligations apply **one year after BOE publication** ([BOE, Ley 1/2025 consolidated](https://www.boe.es/eli/es/l/2025/04/01/1/con)).
  - The BOE extract shows publication on 02/04/2025 and an inconsistent "entrada en vigor 02/01/2025", so verify the dates.
  - FIAB has a "Prevención del desperdicio alimentario" section ([FIAB](https://fiab.es/)).
- **Scale:** The share of FIAB's 27,300 companies with 10 or more employees is not known (gap).
- **Cost/impact:** Fines of up to €60,000 for having no plan.
- **Driver & status:** Ley 1/2025, **in force**. The art. 6 duties apply from about April 2026 (my inference from "one year after publication").
- **How it is solved today:** Consultants and food-bank agreements (not verified).
- **Software-solvable?:** **Yes.** Software can generate the plan, measure waste, manage donation logistics and certificates, and handle reporting.
- **Confidence:** High on the obligations. The burden is not quantified.

### Inferences
- AICA's data points to a concrete, measurable workflow failure: **registering contracts before delivery**. It sits mainly with the industry link and spikes at the grape harvest. An API already exists, so a vendor does not need any government favour to automate it. That makes it one of the most "SaaS-ready" pains in this inventory.
- The CUE postponement removes the expected 2025–2026 "digital notebook" wave. The **fertilisation plan from 1 Sep 2026** and REGFER adviser registration are the live triggers, and the buyers are advisers, cooperatives and larger farms rather than all farmers.
- Many severe agrifood pains (water, disease bans, fishing days, Mercosur, prices below costs) are policy or market problems. Software can only help at the edges, with traceability, cost-of-production evidence and aid claims.

### Gaps
- **GECCO / contracting in origin of seasonal workers** (Huelva, Lleida, Murcia, Almería): ministry pages returned 403, and Freshuelva and Interfresa were unreachable. Unverified.
- **African swine fever** (reported near Barcelona in late 2025): the MAPA site returned 503 and other URLs 404. Unverified, so do not include it without checking.
- **CAP paperwork metrics** (hours, applicant counts, eco-scheme complexity, satellite monitoring): the FEGA site returned 503.
- The **norm that postponed the CUE** (BOE version of 22/01/2025) is not identified. Prices of farm-notebook software (for example Agroptima or cooperative tools) are not verified.
- **Drought status in 2025–2026** (Catalonia, Andalusia), desalinated water prices and irrigation metering obligations.
- **Wine e-labelling, the excise SILICIE ledger, US tariffs on wine and olive oil**: FEV's homepage had no figures.
- The **deadline for e-logbooks on fishing vessels under 12 m**: the EC page says only "some rules 2028".
- Export certificates (CEXGAN), food-industry labelling and traceability burdens.
- Surveys of digitalisation in cooperatives.
- **How CBAM on fertilisers affects farm input prices**: not verified.

---

## Synthesis: which pains are most severe and widespread, and which are noise?

### Takeaway
The strongest SaaS-shaped pains in these sectors are **new, mandatory digital workflows with active enforcement**: the DeCA control document, fuel indexation on invoices and food-contract registration in the RCA, followed by the 2025–2027 EU product-compliance stack. Each has official enforcement data or sanctions, a large affected population and a clear digital interface (QR/HTTPS, invoice formula, RCA API, EU declarations). Many loud pains (energy prices, water, disease bans, Mercosur, fishing days) are real but mostly not software-solvable.

### Inferences
- These pains cluster around the **document of record for one transaction**: a haulage trip (DeCA plus fuel line plus detention timestamps plus payment term), or a farm-gate purchase (contract plus RCA registration plus payment term plus cost-of-production evidence). Building on that record may beat building single-purpose tools.
- Enforcement can shift quickly. The Ministry waived DeCA fines for 5–19 Oct after system failures, and the 29 Nov 2026 snap election may stall draft decrees such as AICA's new inspection RD. Status checks will be needed before any launch.

### Top pains
1. **IND-01 DeCA digital control document.** It has applied to all domestic public road freight (about 152,871 firms) since 5 Oct 2026. Fines are €401–600, rollout failures are live, and shippers push liability onto drivers. The pain is software-native, and cheap issuance at about €5/month leaves the reliability and evidence problems unsolved.
2. **IND-02, IND-21, IND-22: the 2026 fuel and input shock and fuel-indexation enforcement.** Haulage costs are up about 30% and the G index up 44.6%. The formula is mandatory and shippers face fines of up to €18,000. Aid changes every month to 31 Dec 2026, and the same shock hits farmers (aid of up to €0.20/l) and fishers (fuel from €0.50–0.60/l to more than €1.30/l).
3. **IND-18 and IND-19: food-chain contracts and RCA registration.** 991 infractions were sanctioned in 2025: 51% were RCA registration failures and 62% were in wine. Fines run up to €1M, the API already exists, and the workflow peaks at harvest.
4. **IND-03 driver shortage.** About 30,000 drivers are missing, the average age is 55 and only 3% are under 25. 3,608 firms disappeared in 2025. It affects every haulier, though software can only help with recruitment and retention.
5. **IND-20 farm fertilisation plan and records.** New legal duties started on 1 Sep 2026 and 1 Jul 2026 (REGFER), while the CUE is postponed. Bureaucracy is a headline demand of the 28 Oct 2026 farm protests.
6. **IND-04 late payment in haulage.** It is chronic (38% of payers beyond 60 days in Aug 2026) despite sanctions, but improving, so it is best bundled with indexation and DeCA records.
7. **IND-12 packaging EPR and PPWR.** The PPWR has applied since 12 Aug 2026, on top of RD 1055/2022 registration, declarations and fees. It affects every manufacturer and food SME that ships packaged goods, including the 27,300 food and drink firms.
8. **IND-13 and IND-14: CBAM (live since 1 Jan 2026) and EUDR (30 Dec 2026, or 30 Jun 2027 for micro and small firms).** Both are supplier-data due-diligence duties for SME importers and processors and lend themselves to software. Their Spanish scale is not quantified.

### Noise and dead ends
- **eCMR / eFTI as an imminent mandate:** this is noise for now. Authorities must accept eFTI data only from **9 Jul 2027**, platform certification rules are due by December 2026, and mandatory use will not be evaluated before 2029 ([European Commission, eFTI](https://transport.ec.europa.eu/transport-themes/logistics-and-multimodal-transport/efti-regulation_en); [Fenadismer PDF](https://www.fenadismer.es/wp-content/uploads/Pildora-formativa.-todo-sobre-el-Documento-Electronico-de-Control.pdf)). International CMR is unaffected by the DeCA, and eCMR remains voluntary.
- **The digital farm notebook (CUE) as a 2025–2026 mandate:** **postponed** to the next CAP programming period ([BOE, RD 1054/2022](https://www.boe.es/eli/es/rd/2022/12/27/1054/con)). The live trigger is the RD 1051/2022 fertilisation plan instead.
- **"Spanish industry pays too much for electricity":** weakly supported. Spain's non-household electricity cost €0.1336/kWh against €0.1800 for the EU in 2026-S1 ([Eurostat](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_205?geo=ES&geo=DE&geo=FR&geo=IT&geo=PT&geo=EU27_2020&nrg_cons=MWH500-1999&tax=X_VAT&currency=EUR&unit=KWH&sinceTimePeriod=2024-S1)). The real pains are gas and fuel volatility and grid reliability.
- **"Spanish firms lack ERP":** weak for firms with 10 or more staff, whose ERP use is 60.38% against the EU's 46.45% ([Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_enterprises)). The basic ERP market is crowded (Odoo from US$31.10/user/month; Cegid Ekon, Sage, a3). The gap is compliance add-ons and micro firms.
- **A new generic freight exchange:** a dead end. Wtransnet alone has more than 80,000 professionals, more than 350,000 offers a day and a Coface payment guarantee ([Wtransnet](https://www.wtransnet.com/es/)), and Timocom already offers a freight exchange, tenders, route and cost planning, transport orders and TMS/ERP interfaces ([Timocom](https://www.timocom.es/)). Neither publishes prices.
- **DeCA "certified software" upsell:** no homologated software is required ([Veritas Gestión](https://veritasgestion.com/?p=7976)), and Fenadismer warns of mark-ups of up to 1,000% ([Fenadismer](https://www.fenadismer.es/ojo-ofertas-abusivas-para-el-nuevo-documento-electronico-de-control/)). Basic issuance is a commodity priced at about €5/month.
- **DeCA for last-mile couriers:** final-mile parcel delivery is exempt ([Fenadismer PDF](https://www.fenadismer.es/wp-content/uploads/Pildora-formativa.-todo-sobre-el-Documento-Electronico-de-Control.pdf)).
- **Sustainable mobility plans as an SME pain:** only firms with more than 200 workers or 100 per shift are covered ([BOE, Ley 9/2025 art. 104](https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545)).
- **The post-blackout grid decree (RDL 7/2025):** repealed by Parliament in July 2025 ([Wikipedia](https://en.wikipedia.org/wiki/2025_Iberian_Peninsula_blackout)).
- **The EU Late Payment Regulation (30-day cap):** blocked in the Council and not a near-term driver ([trans.info, 22 Sep 2026](https://trans.info/es/los-transportistas-espanoles-esperan-52-dias-para-cobrar-la-reforma-europea-se-atasca-504049)).
- **A general labour shortage in manufacturing:** weakly supported. The vacancy rate was 0.9% against the EU's 2.8% in 2023 ([EURES](https://eures.europa.eu/living-and-working/labour-market-information/labour-market-information-spain_en)). Shortages are specific trades (welders, machine operators, drivers).
- **Real but not software-solvable at the root:**
  - Mercosur, provisionally applied since **1 May 2026** after the European Parliament referred it to the Court of Justice on 21 Jan 2026 ([Wikipedia, EU–Mercosur](https://en.wikipedia.org/wiki/European_Union%E2%80%93Mercosur_Free_Trade_Agreement)).
  - US tariff policy (IEEPA tariffs struck down on 20 Feb 2026; Section 301 at 10% from 24 Jul 2026) ([Wikipedia](https://en.wikipedia.org/wiki/Tariffs_in_the_second_Trump_administration)).
  - Mediterranean fishing-day cuts (−44%), water allocation on the Tajo-Segura, and Morocco's ban on Spanish cattle. Software can help only at the edges (traceability, aid claims, evidence).
- **Upcoming, not yet biting:** the Machinery Regulation (20 Jan 2027) and EUDR (30 Dec 2026 / 30 Jun 2027; postponed twice, so further changes are possible). These are real but timing-sensitive.
- **Unverified and excluded:** African swine fever impacts, GECCO seasonal-worker pains, Spanish CBAM thresholds, city loading-zone fines and TMS price levels. They may be real but could not be evidenced in this pass, so they should be checked again before any ranking relies on them.
