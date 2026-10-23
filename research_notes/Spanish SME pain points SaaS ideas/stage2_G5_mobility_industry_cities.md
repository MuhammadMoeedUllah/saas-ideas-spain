# Stage 2, group G5: transport, industry, agrifood, low-emission zones and city conditions

*Noise filtering and idea generation, 23 October 2026.*

*Inputs:*
- *`transport_industry_agrifood.md` (IND entries);*
- *`zbe_lez_fleets.md` (ZBE entries);*
- *`cities_macro_surveys.md` (CITY entries and the national surveys);*
- *`00_user_supplied_ideas.md` (U3 EcoRoute);*
- *the software table in `voice_of_smes_software_market.md` (prices only).*

*Method: no web searches; anything that needs checking became a validation question. Every claim cites a pain ID. "My arithmetic" marks numbers I derived from figures in the notes. "Folded" means a filtered duplicate whose evidence is reused in the surviving cluster.*

---

## 1. Summary

- **Reviewed 71 pain entries:** IND-01 to 25 (25), ZBE-01 to 23 (23) and CITY-01 to 23 (23).
- **Carried forward 33** into 9 clusters.
- **Filtered 38:**
  - N1 weak evidence: 4
  - N2 not software-solvable: 13
  - N3 regulation annulled or transient: 1
  - N4 saturated: 2
  - N5 too niche or outside the SME scope: 7
  - N6 legally risky: 0
  - N7 duplicate: 11. Most are city-track entries that the ZBE track covers in more depth, or pains that belong to other groups.
- **Strongest theme: new mandatory digital workflows with live enforcement and a machine interface.** These rest on laws already in force, so the dissolution and the 29 Nov 2026 election matter little to them.
  - The DeCA road-freight control document, in force since 5 Oct 2026, with €401–600 fines (IND-01).
  - The itemised fuel-revision line on haulage invoices, with payer fines up to €18,000 (IND-02).
  - Contract registration in the RCA (Registro de Contratos Alimentarios, the food-contract register) before delivery: 506 of the 991 infractions AICA (the food-chain enforcement agency) sanctioned in 2025 (IND-18).
- **Second theme: low-emission zone (ZBE) rules differ by city and flip with court rulings,** on top of a free national feed that is stale and has little rule detail (ZBE-01, ZBE-02, ZBE-03). The opening is a curated, versioned rules layer plus in-zone dispatch and permit logic, not routing (ZBE-15).
- **Third theme: the EU product-compliance stack.** Packaging EPR and the PPWR apply now, CBAM is live, and EUDR starts on 30 Dec 2026 or 30 Jun 2027 depending on firm size (IND-12, IND-13, IND-14).
- **Most loud pains are macro and were filtered:** energy, labour, housing, water, disease bans, fishing days and industrial distress. Surveys still rank energy, uncertainty and labour highest (section 2).
- **9 ideas: 6 type B, 3 type C, none type A.** The notes have almost no verified incumbent prices in these sectors: TMS, freight exchanges and LEZ data vendors are quote-only. A type A play needs price discovery first.
- **U3 EcoRoute: reshape, do not discard.** Keep the ZBE-compliance market. Drop "routing avoids penalties". Treat Valencia as a pilot channel, not a launch market (section 6, G5-I09).

---

## 2. Macro weighting (for use across all groups)

**Survey caveats.**
- EBAE (Banco de España) samples companies only, about 6,000–7,000 responses a quarter, and excludes autónomos trading as natural persons. Use ATA for sole traders (CITY entries, Q3).
- ECB SAFE asks for the single "most pressing problem", while EBAE asks which factors "limit" activity, with several answers allowed. Do not compare percentages across the two.
- ATA and CEPYME are advocacy bodies. INE, the Banco de España and the ECB are official sources.

| Obstacle | Strongest survey numbers | Trend | Software leverage | How to weight ideas |
|---|---|---|---|---|
| **Energy and input costs** | EBAE: energy limits **63.2%** of firms in 2026Q3, up from 42% in 2026Q1. In 2026Q2, 63% felt negative effects from energy and 57% from non-energy inputs ([BdE Q3 2026](https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/proyecciones-macro-informe-trimestral/proyecciones-e-informe-trimestral-de-la-economia-espanola-tercer-trimestre-2026.html); [BdE 18 Jun 2026](https://www.bde.es/f/webbe/GAP/Secciones/SalaPrensa/NotasInformativas/26/presbe2026-52.pdf)). ATA Q1 2026: **81.1%** of autónomos saw costs rise, 23.9% of them by more than 16%; 68.9% raised prices and 27.3% absorbed the rise ([ATA via Bolsamanía](https://www.bolsamania.com/noticias/economia/economia--solo-el-56-de-los-autonomos-considera-suficientes-las-medidas-adoptadas-por-la-guerra-de-iran-segun-ata--22277520.html)) (CITY-14) | Sharp rise in 2026 (the Iran war), still below the ~80% seen after Ukraine | **Low** for "cut your energy bill": Spanish industrial electricity cost €0.1336/kWh against €0.1800 for the EU in 2026-S1 (IND-10). **Medium** where a law or contract lets firms pass costs on (IND-02) | The most widespread obstacle. Boost ideas that recover or pass on costs; discount ideas whose value is cheaper energy |
| **Policy uncertainty and regulation** | EBAE: uncertainty limits **57.6%** (Q3) and 62% (Q2); 40.9% say it hurts investment (Q3). SAFE: "regulation" is the most pressing problem for **14.9%** of Spanish SMEs (2025-H2), up from 10.9% (2023-H1) and above the euro area's 13.6% ([ECB SAFE](https://data.ecb.europa.eu/data/datasets/SAFE/SAFE.H.ES.SME.A.0.0.0.Q0.ZZZZ.P3.AL.WP)). ATA: 87.4% say instability hurts them. ATA's president puts autónomos' bureaucracy cost at €10bn a year ([CEOE/CEPYME, 16 Jun 2026](https://cepyme.es/storage/2026/06/260616-NP-CEOE_Encuentro-Empresarial-Absentismo.pdf)). ATA Asturias: 226 h and €3,390 per autónomo a year, methodology undisclosed (CITY-15, CITY-19). CEPYME: "excesivas cargas administrativas" (excessive administrative burdens) | Steady rise. Elections on 29 Nov 2026 | **High**: compliance automation, alerts, calendars | Widespread and rising. Boost compliance ideas tied to rules in force and actively enforced; discount ideas built on drafts or bills that lapse with the dissolution |
| **Labour and skills** | SAFE: skilled staff is the **#1** most pressing problem, **25.0%** (2025-H2). EBAE: 43.1% limited (Q3); in Q2, construction about 60%, hospitality 57.8% and agriculture 47.5%. ATA: 29.8% of hiring autónomos had difficulty and 17.9% could not hire (CITY-16) | Persistent, structural | **Low** at the root; medium for scheduling, recruiting reach and retention | Weight HR ideas by sector rate (construction, hospitality, agriculture, haulage drivers in IND-03), not the average. Spain's vacancy rate was 0.9% against the EU's 2.8% in 2023, so shortages are trade-specific (IND-11) |
| **Late payment** | ATA: **38.3%** of autónomos are affected (private clients only: 19.6%). Haulage: 38% of payers beyond 60 days, 52 days on average in Aug 2026, down from 83 days in 2021 (IND-04, CITY-18) | Improving slowly | **Medium**: interest and compensation claims, dunning | Medium prevalence. Stronger bundled into a document-of-record workflow than as a stand-alone collections tool |
| **Cost of and access to finance** | EBAE Q3 2026: borrowing costs **26.8%** (+2.5 pp, SMEs more affected) and access **18.2%** (+5.4 pp). In 2025Q4, 15.4% of SMEs against 9.7% of large firms. SAFE: access is the most pressing problem for only 5.0%. ATA: 3% of autónomo credit applications refused (CITY-17) | Rising from a low base | Low–medium | Minority concern. Low weight unless the idea is cash-flow forecasting |
| **Finding customers** | SAFE: 16.8% (2025-H2). GEM 2025–26: market access rated 3.8/10 | Flat | Medium | Relevant to marketing and sales ideas (retail, hospitality) |
| **Adoption capacity** (a multiplier, not an obstacle) | INE ETICCE, Q1 2026 ([INE, 22 Oct 2026](https://www.ine.es/dyngs/Prensa/ETICCE20251T2026.htm)). Firms under 10 staff: website 36.2%, online sales 11.8%, AI **21.4%** (13.4% a year earlier). Firms with 10+ staff: ERP 60.9%, CRM 33.9%, AI 33.6%. Laggards: Castilla-La Mancha CRM 25.0%, Baleares ERP 47.3%, Canarias ERP 49.4%; Madrid and Cataluña lead. 2025 methodology break (CITY-22, CITY-23) | AI adoption rising fast | n/a | Discount ideas that need micro firms to self-onboard complex software. Boost those sold through gestorías, associations or tools firms already use. Launch first in Madrid or Cataluña |
| **Fragility and churn** | INE CODEM: two-quarter survival of 83.36% for young employer units with 1–5 staff and 85.54% for autónomos under 30 ([INE 82128](https://www.ine.es/jaxiT3/Tabla.htm?t=82128)). EPA Q2 2026 via CEPYME: employers −2.9% y/y, individual entrepreneurs −4.0% (CITY-21) | Worsening for micro employers | n/a | Assume higher churn and lower lifetime value for products aimed at new micro employers |

**Market-size anchors** (CITY Table A):
- DIRCE at 1 Jan 2025: 3,310,824 companies, 54.4% with no employees. By size: 1,348,909 with 1–9 staff, 134,826 with 10–49, 21,307 with 50–249 and 5,339 with 250+.
- INE CODEM, 2026Q2: 1,231,358 employer units and 3,186,989 autónomos.
- EC SME Fact Sheet 2026: 3,662,315 SMEs, 94.9% of them micro.

**How the merge stage should apply this:**
1. Score each pain on prevalence and software leverage together. Energy is the most widespread but least solvable. Regulation is widespread, rising and the most solvable.
2. Use the sector rate when an idea is sector-specific. Labour pains in construction and hospitality run at about 58–60%, against a 43% average.
3. Use ATA, not EBAE, for sole traders.
4. Penalise ideas that rest on Spanish drafts or bills, given the dissolution. EU regulations, laws already in force and municipal ordinances are unaffected by the election.

---

## 3. Pain clusters

### Cluster 1: Haulage trip-record compliance and revenue leakage
- **Pain IDs:** IND-01, IND-02, IND-04, IND-06.
- **Problem.** Every domestic public road-freight trip now produces four pieces of paperwork that small carriers handle badly. The notes infer that all four run on the same trip record (IND inferences). These trips are run by 152,871 road-freight companies, 61,716 of them in heavy transport ([trans.info, 24 Aug 2026](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)). Carriers range from the autónomo with one truck to fleets of 50–249, and shippers are jointly liable.
  1. **The DeCA control document (IND-01).**
     - **What it requires:** since 5 Oct 2026, a native PDF with a QR code pointing to a public HTTPS URL. It must be created before departure and kept for a year by both shipper and carrier ([BOE, Ley 9/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545); [GA-P guide](https://ga-p.com/publicaciones/guia-para-no-perderte-con-el-nuevo-deca/)).
     - **Readiness:** in a survey of 750 transport professionals (Oct 2025), 17% were prepared, 35% insufficiently prepared and 23% not prepared at all ([trans.info, 5 Feb 2026](https://trans.info/es/documentos-digitales-452450)).
     - **Fines:** drivers were fined "more than 400 euros" while showing the QR they had been given ([Fenadismer, 15 Oct 2026](https://www.fenadismer.es/deca-sanciones-injustas-a-transportistas-por-errores-de-sus-cargadores-o-de-las-inspecciones-en-carretera/)). The infraction carries €401–600 (a single source for the article numbers).
     - **Liability shifting:** some large shippers force drivers onto private platforms and issue "provisional DeCAs" ([Fenadismer, 8 Oct 2026](https://www.fenadismer.es/primeras-incidencias-del-deca-tras-su-entrada-en-vigor/)).
  2. **The fuel-revision line on every invoice (IND-02).**
     - **The cost shock:** haulage costs rose "del orden del 30%" (about 30%) ([BOE, RDL 9/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8283)). The Ministry's G index rose 44.6% for heavy and 38.4% for light vehicles between January and 1 Oct 2026 ([Fenadismer, 13 Oct 2026](https://www.fenadismer.es/canal-de-denuncias-contra-los-cargadores-que-no-indexen-el-combustible-a-sus-transportistas/)).
     - **Payer fines:** payers who block a separate fuel line face fines from €401–600 up to €4,001–6,000, and up to €18,000 for a repeat offence within 12 months.
     - **Resistance:** many shippers resist the line or quietly cut base rates first.
  3. **Detention at docks (IND-06).** 70% of carriers and over 40% of shippers report waits of more than an hour (a single 2023 study, [CadenadeSuministro](https://cadenadesuministro.es/noticias/cargadores-y-transportistas-siguen-sufriendo-esperas-en-los-muelles-de-carga-y-descarga_478995_102.html)). After the first hour the law grants 2×IPREM per day for each hour, up to 10 hours a day, with surcharges on days 2 and 3 ([BOE, Ley 15/2009](https://www.boe.es/eli/es/l/2009/11/11/15/con)). Claiming needs proof and risks the client relationship, and how much goes unclaimed is unknown.
  4. **Payment (IND-04).** In Aug 2026 the average was 52 days and 38% of payers broke the 60-day maximum ([trans.info, 22 Sep 2026](https://trans.info/es/los-transportistas-espanoles-esperan-52-dias-para-cobrar-la-reforma-europea-se-atasca-504049)). That is down from 59 days and 48% in Dec 2025 and 83 days in 2021.
- **Driver and status (Oct 2026):**
  - **DeCA.** Based on Ley 9/2025 (transitional provision 8), the Resolución DGTCF of 5 Jun 2026, Orden TRM/282/2026 and Orden FOM/2861/2012. In force since 5 Oct 2026. Only fines for download failures between 5 and 19 Oct are waived ([Fenadismer, 22 Oct 2026](https://www.fenadismer.es/deca-transportes-reconoce-fallos-tecnicos-y-no-tramitara-las-multas-impuestas/)). Final-mile parcel delivery and international CMR transport are out of scope (IND-01).
  - **Fuel line.** RDL 9/2026, in force since 16 Apr 2026. Ley 15/2009 art. 38 makes the revision automatic at a fuel variation of 5% or more and voids contrary agreements. RDL 25/2026 extends the aid to 31 Dec 2026. Whether Congress convalidated either decree-law is **unverified** (IND-02).
  - **Detention.** Ley 15/2009 art. 22, in force.
  - **Late payment.** Ley 3/2004 and Ley 15/2009 art. 41 (default after 30 days). A transport sanction regime has applied since Oct 2021, with fines up to €6,000, or €30,000 for repeat or abusive cases. The EU 30-day payment regulation is stalled in the Council (IND-04).
  - **No competing mandate soon.** Authorities must accept eFTI data only from 9 Jul 2027 (IND noise list).
- **Used today and price:**
  - **DeCA:** tools "desde 5 euros al mes" (from €5/month) and offers priced up to 1,000% higher, some of which are not compliant ([Fenadismer, 10 Sep 2026](https://www.fenadismer.es/ojo-ofertas-abusivas-para-el-nuevo-documento-electronico-de-control/)). No homologated software is required. eCMR and e-signature vendors Fieldeas, Viafirma and Edicom publish no prices. Shippers impose private platforms. UNO has a "Guía DeCA" (content not read) (IND-01).
  - **Fuel:** CETM's "Calculadora de Costes e Indexación" (price and access not shown), Fenadismer's complaint channel, and TMS, ERP or manual invoicing (no prices) (IND-02).
  - **Payment:** the Wtransnet freight exchange with a Coface guarantee covering at least 90% of the invoice (quote-only), CETM's Icired default registry, confirming (25% of payments) and factoring (IND-04).
  - **Docks:** slot-booking tools used by 46% of shippers in 2023; vendor prices unverified (IND-06).

### Cluster 2: ZBE rule fragmentation, legal whiplash and thin official data
- **Pain IDs:** ZBE-01, ZBE-02, ZBE-03, ZBE-04, ZBE-12, ZBE-18, ZBE-19, ZBE-20, ZBE-23. Folded: CITY-12, IND-08.
- **Problem:**
  - **Few enforce.** About 150 municipalities must have a ZBE (149 or 151 depending on the source). Only 56 were "fully active" in Feb 2026 ([Motor16, 16 Feb 2026](https://www.motor16.com/las-ultimas-noticias/zbe-ciudades-multas-coches/)) and 68 in Sep 2026 ([Motor16, 26 Sep 2026](https://www.motor16.com/las-ultimas-noticias/zonas-bajas-emisiones-68-ciudades/), CITY-12). Probably no more than about 50 actually fine (ZBE inference). Only 6 of 23 large Catalan municipalities fined effectively in 2025 ([Metrópoli Abierta, 10 Sep 2026](https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html)).
  - **The 16 profiled cities split.** Nine sanction by label and A Coruña by access control. Six do not: Málaga stopped on 14 Oct 2026; Valencia, Murcia and Las Palmas have no ZBE in force; Alicante issues notices only; Vigo is information-only until 10 Sep 2027 (ZBE city table).
  - **The legal answer has many dimensions.** For a fleet it depends on label × vehicle category × MMA (maximum authorised mass) × domicile × time window × day type × permit × purpose (ZBE inference).
  - **It changes overnight (ZBE-02).** Madrid's annulment became final on 15 Apr 2026, while Ordenanza 2/2026 has applied since 7 Apr 2026 ([Infobae, 21 Apr 2026](https://www.infobae.com/espana/2026/04/21/el-tribunal-supremo-confirma-la-anulacion-parcial-de-la-zona-de-bajas-emisiones-en-madrid-al-rechazar-el-recurso-del-ayuntamiento/)). Málaga's ZBE chapter was annulled on 6 May 2026 and fines stopped on 14 Oct 2026 ([Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)). Valladolid's ordinance was annulled but the city keeps fining. Barcelona was suspended for about eight weeks.
  - **Fragile domicile tests (ZBE-04).** The tax-domicile tests in Madrid and Granada are legally fragile after Málaga.
  - **Episodes and switch-on dates.** Same-day pollution-episode bans apply in Madrid and, for label B since 1 Jan 2026, in Barcelona at €260. Catalonia has declared no episode since 2015 (ZBE-12). Switch-on dates cause surprise fines: Vigo on 10 Sep 2027, Badalona on 1 Jan 2027, and the end of Madrid's resident warnings on 31 Dec 2026 (ZBE-23).
  - **Cost.** Each breach costs €200, or €100 if paid early (ZBE-01).
  - **Official data is thin (ZBE-03).** The free DGT NAP feed has 45 resources in 46 DATEX II files (CC BY 4.0). It has no files for Zaragoza, Vigo, Córdoba, Murcia or Las Palmas. It shows Valencia "active" from 1 Jun 2026 and Málaga still "active". Its data model has no fields for vehicle category, MMA, domicile, quotas, phase end-dates or episodes ([NAP index](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/); [DGT ED MOV 2023/01](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf)). City portals publish perimeters only.
  - **Demand for a national dataset is unmet (ZBE-19).** A public request for a national ZBE table has gone unanswered since 16 Nov 2025 ([datos.gob.es](https://datos.gob.es/es/solicitud-de-datos/zonas-de-bajas-emisiones)).
  - **Vendors miss Spanish semantics.** Commercial engines key on Euro class, not DGT labels (ZBE-18), and do not list Spanish coverage or prices (ZBE-20).
  - **Even trade bodies have stale data.** The logistics association UNO's directory lists Bilbao, Valencia and Zaragoza as "Pendiente Borrador ZBE" (ZBE draft pending) ([UNO](https://unologistica.org/proyectos-e-informes/ordenanzas-de-movilidad/), IND-08). That contradicts Bilbao's ZBE, in force since 2024.
- **Driver and status:** Ley 7/2021 art. 14 and RD 1052/2022 are in force; art. 10.2 requires municipalities to notify the DGT within a month. Each municipal ordinance has its own status, as above (ZBE-01, ZBE-03).
- **Used today and price:**
  - **Information sites and apps:** the Astac Condal/RACC national ZBE site for hauliers (price unknown); the "ZBE España" iOS app (tagged free); and the ecomovilidad, Iberfurgo and RACE guides (free, secondary).
  - **Commercial data and routing:** HERE Environmental Zones and routing (Euro class, fuel, weight, no DGT-label parameter, price unknown); TomTom LEZ (376 cities globally, Spanish coverage unverified); urbanaccessregulations.eu (268 LEZs, price unknown); Green-Zones (visibly stale: "one of 7 zones in Spain").
  - **Developer tools:** @cargoffer/zbe-mcp (compares Euro class only; no price or licence) and an Apify "EU LEZ Route & Vehicle Checker" (not inspected) (ZBE-01, ZBE-20).

### Cluster 3: In-zone deliveries, permits, quotas and loading windows
- **Pain IDs:** ZBE-06, ZBE-07, ZBE-15, ZBE-16, ZBE-17. Folded: CITY-04.
- **Problem:**
  - **Routing cannot help in-zone.** When the stop is inside the zone, avoidance routing is useless. Compliance instead comes from five levers (ZBE-15 and section 4 inference):
    - dispatching a compliant vehicle;
    - scheduling inside label- and MMA-specific windows;
    - using and notifying a permit or quota;
    - using an exempt car park or hand-off point;
    - holding the right standing registration.
  - **Madrid Distrito Centro (ZBE-06, ZBE-16)** ([madrid.es professionals page](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD)):
    - C-label vehicles may enter 7–15h and ECO 7–21h; B light vans have been banned since 2024.
    - Holders need IAE (business tax) registration and per-plate pre-registration. Rented, leased and replacement vehicles need contracts or repair orders.
    - Night deliveries (23–7h) and early food deliveries (5–7h) need a yearly declaración responsable with proof of deliveries.
  - **Quotas (ZBE-07; one secondary source per city):** Bilbao gives each business 6 invitations a month, notified within 2 days of access. Barcelona allows 24 day-passes a year, Zaragoza 8 accesses a month and Sevilla 10 a month (snippet-level).
  - **Exempt car parks and loading windows (ZBE-15, ZBE-16):** Granada exempts vehicles parked over an hour in its 36 public car parks. A Coruña's loading window is 6–11h.
  - **Exemptions for older and low-income autónomos (ZBE-17).** They need sworn statements, fleet lists, ITV (roadworthiness test) and income proof, renewed every year:
    - Madrid: aged 59+ with at least 50% of the fleet unlabelled.
    - Barcelona: within 5 years of retirement, until 31 Mar 2028.
    - Granada: income under €16,800. Valladolid: under 1.3× IPREM.
  - **Cost.** Each slip is a €200 fine; volumes per business are unknown.
  - **Stop-start enforcement (CITY-04).** Barcelona bans unlabelled vans on weekdays 7–20h. Restrictions were suspended from late January and restored on 16 Mar 2026; the suspension came via Resolució TER/194/2026.
- **Driver and status:**
  - Madrid's OMS as amended by Ordenanza 2/2026, plus Decreto 178 (in force).
  - The Bilbao, Barcelona/AMB, Zaragoza, Granada, A Coruña and Córdoba ordinances are in force.
  - Barcelona's near-retirement exemption runs to 31 Mar 2028 (ZBE-06, ZBE-07, ZBE-16, ZBE-17).
- **Used today and price:** manual registration in Madrid's Mi Carpeta or by appointment; per-city portals and apps, most without APIs; the free AMB registry; gestorías (no prices found); dispatchers' spreadsheets (inference). No Spanish ZBE-aware dispatch product was found (ZBE-06, ZBE-07, ZBE-15).

### Cluster 4: Fine exposure and who pays (including rented and leased vans)
- **Pain IDs:** ZBE-09, ZBE-10. Folded: CITY-03.
- **Problem:**
  - **What a fine costs.** Each non-compliant entry is a €200 serious infringement (€100 if paid early, €260 in Barcelona episodes), arriving days later by post or electronic address (ZBE-10).
  - **Volumes in Madrid.** More than 3.4M ZBE sanction files worth more than €663M up to 31 Dec 2025. The source is AEA, an interested drivers' association ([El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)).
  - **H1 2025 alone, from a single source citing AEA** ([Híbridos y Eléctricos](https://www.hibridosyelectricos.com/coches/191347190-en-multas-madrid-logra-record-historico-en-espana-por-acceso-sin-etiqueta-zbe_83375_102.html), CITY-03): 261,115 unlabelled-access fines worth €52.2M, +94.6% year on year, and about €100.5M across all ZBE access fines.
  - **Málaga** issued 46,562 fines in under a year (ZBE-10).
  - **Unknown split.** No city publishes the share of fines that goes to businesses (ZBE-10).
  - **Rented and leased vans (ZBE-09; thin evidence: one trade article plus the official Madrid page).** Camera fines go to the registered holder, so lessors and van-rental firms must pass them to the driver. They must also hold per-vehicle documents before a vehicle may use Madrid's permits.
- **Driver and status:** Ley sobre Tráfico art. 76 z3 plus the municipal ordinances, in force (ZBE-09, ZBE-10).
- **Used today and price:** paying; appealing through lawyers or associations (AEA, OCU); "fine-management services" (not researched); manual fine transfer at lessors (inference). No prices (ZBE-09, ZBE-10).

### Cluster 5: Ageing van fleet and dated phase-outs
- **Pain IDs:** ZBE-05, ZBE-13, ZBE-14.
- **Problem:**
  - **The fleet is old (ZBE-05).** 1,084,677 of Spain's 2,741,010 vans and 1,021,451 of its 2,462,425 trucks are 20 or more years old ([DGT Anuario 2024](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)). Pre-2006 diesel vans carry no label, so roughly 1.1–1.3M vans are probably unlabelled (an inference, not a DGT figure).
  - **Owners comply until they exit.** They are mainly trades, small couriers and market or food suppliers, and they keep old vans running until they retire or leave rather than renew them (ZBE inference).
  - **Vans legal today become illegal on known dates (ZBE-14):**
    - Palma allows only C, ECO and Cero from 1 Jan 2027 ([BOIB 37](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590)).
    - Catalan municipalities over 50,000 must restrict label B before 1 Jan 2028 (Decree 132/2024; its binding status is disputed between the notes).
    - Bilbao's B exemptions end by 31 Dec 2029.
    - Vigo restricts B from 2029, or 2027 per Motor16 (conflict).
  - **Madrid's NO2 kill-switch (ZBE-13).** Unlabelled vans may circulate outside the special zones only while NO2 limits hold at every station. One breach lets the city end the regime, with fines six months after publication.
- **Driver and status:**
  - The label system is reportedly unchanged at least to 2027 (snippet-level); the ordinances are in force.
  - The MOVES III page lists N1 van aid of up to €7,000, or €9,000 with scrapping. But its application deadline reads 31 Dec 2024 and no 2026 successor is named ([IDAE](https://www.idae.es/ayudas-y-financiacion/para-movilidad-y-vehiculos/programa-moves-iii)) (ZBE-05).
- **Used today and price:** dealers and renting, MOVES aid (uncertain), city exemptions for older autónomos. No planning tool was found (ZBE-05, ZBE-14).

### Cluster 6: Food-chain contracts and RCA registration before delivery
- **Pain IDs:** IND-18, IND-19, IND-21.
- **Problem:**
  - **The rule.** For every purchase from a farmer, the buyer needs a signed written contract with minimum terms, including a price above the producer's total costs. Each contract and each change must be registered in the RCA before delivery (IND-18).
  - **Who must comply.** Food-industry SMEs, origin and destination wholesalers, retailers, and cooperatives buying from non-members: more than 27,300 food and drink companies ([FIAB](https://fiab.es/)) and 3,669 cooperatives ([Cooperativas Agro-alimentarias](https://www.agro-alimentarias.coop/datos-cooperativismo)).
  - **AICA 2025 enforcement** ([AICA Memoria 2025](https://www.aica.gob.es/content/dam/aica/docs/publicaciones/memorias/Memoria_Anual_de_Actividades_2025.pdf)):
    - 399 inspections, 2,978 commercial relationships checked, **991 infractions** sanctioned and 109 companies sanctioned.
    - **506 failures to register in the RCA (51%), all by the "industry" link.**
    - 186 payment-term breaches, 124 of them by wholesalers.
    - 98 contracts missing minimum terms (67 missing the price), 74 with no written contract, and 53 price changes not agreed by both parties.
    - Since 2014: €27.9M in fines.
  - **Wine (IND-19).** 619 of the 991 infractions (62%) were in wine, 616 of them on wine grapes, from only 22 wine inspections. The notes infer these are mostly harvest contracts not registered before delivery.
  - **Fines** ([BOE, Ley 12/2013](https://www.boe.es/eli/es/l/2013/08/02/12/con)). Minor €250–3,000 (non-registration is minor, art. 23.1.k); serious €3,001–100,000; very serious up to €1M. Serious and very serious fines are published, which names the company.
  - **The cost floor is getting harder to evidence (IND-21).** The rule that the price must exceed costs bites harder after the 2026 diesel and fertiliser shock. Agricultural diesel aid of up to €0.20/l runs to 31 Dec 2026, and IRPF módulos (flat-rate income tax) relief is worth more than €600M ([UPA, 22 Oct 2026](https://upa.es/upa-celebra-la-publicacion-de-la-orden-que-rebajara-la-carga-fiscal-de-gasoleo-y-fertilizantes-lo-hemos-conseguido/)). Only IND-21's cost-of-production angle is carried forward; its aid paperwork is transient.
- **Driver and status:**
  - Ley 12/2013, as amended by Ley 16/2021, is in force.
  - RD 1028/2022: the RCA has been live since Dec 2022 and is sized for 30M documents a year and 300,000–400,000 users. It has an API for high-volume buyers. Web uploads need a digital certificate and take at most 5 documents and 5 MB each ([AICA RCA FAQ](https://www.aica.gob.es/servicios-en-linea/Registro%20de%20Contratos%20Alimentarios/preguntas-frecuentes-rca)).
  - A new AICA inspection decree is a **draft** (consultation opened 30 Sep 2026) and may stall with the election (IND-18).
- **Used today and price:** manual uploads; the RCA API, integrated in-house by large buyers; gestorías and consultants; winery ERPs (not verified). No prices in the notes. The RCA help desk has handled 3,266 queries since launch, 700 of them in 2025 (IND-18, IND-19).

### Cluster 7: Farm fertilisation plans and records
- **Pain IDs:** IND-20.
- **Problem:**
  - **Who.** Farmers above the exemption thresholds, their registered fertilisation advisers and cooperatives' technical services. The cooperative world counts more than 1M member families in 3,669 cooperatives.
  - **How often (RD 1051/2022)** ([BOE, RD 1051/2022](https://www.boe.es/eli/es/rd/2022/12/27/1051/con)):
    - each fertilisation logged within a month;
    - a fertilisation plan (plan de abonado) per farm;
    - soil analyses every 5 years (irrigated) or 10 years (rainfed) once sampling guides are published.
  - **Exemptions.** Records: farms of 5 ha or less with 1 ha or less irrigated. Plan: rainfed units of 10 ha or less.
  - **Cost.** Time and adviser fees; not quantified.
  - **Sentiment.** Cooperativas Agro-alimentarias calls it "una carga burocrática inasumible" (an unbearable bureaucratic burden) ([Cooperativas, 23 Oct 2026](https://www.agro-alimentarias.coop/posts/cooperativas-agro-alimentarias-de-espana-apoya-la-movilizacion-del-28-de-octubre-dar-de-comer-tiene-que-dar-para-vivir)). Simplification is one of five demands of the 28 Oct 2026 tractor protest ([ASAJA](https://www.asaja.com/gran-tractorada-del-28-de-octubre-en-madrid-dar-de-comer-tiene-que-dar-para-vivir/)).
- **Driver and status:**
  - **Fertilisation (RD 1051/2022), in force.** The plan de abonado applies from 1 Sep 2026, or from 1 Jan 2026 for irrigated units sown between 1 Mar and 30 Jun 2026. Advisers must register in REGFER (the register of fertilisation advisers) from 1 Jul 2026. Agronomic advice becomes mandatory one year after the plan duty in vulnerable zones and two years after elsewhere.
  - **Digital farm notebook (RD 1054/2022): postponed.** The CUE (Cuaderno de Explotación, the digital farm notebook) will be mandatory only in the next CAP programming period, 2028 or later by inference ([BOE, RD 1054/2022](https://www.boe.es/eli/es/rd/2022/12/27/1054/con)). It will cover farms over 30 ha, over 5 ha irrigated or over 0.1 ha of greenhouses. Administrations must offer free software for it.
- **Used today and price:** free public CUE software, the "Cuaderno de Campo Cooperativo" (cooperative field notebook) being rolled out, advisers, and private farm apps (prices not verified).

### Cluster 8: EU product and packaging compliance for manufacturers and food firms
- **Pain IDs:** IND-12 (core), IND-13, IND-14, IND-25.
- **Problem:**
  - **Who.** Manufacturers and food and drink SMEs that place packaged goods on the market: more than 27,300 food and drink companies with 483,300 jobs ([FIAB](https://fiab.es/), reference year not shown). Also SME importers of CBAM goods (count unknown), EUDR operators (furniture, coffee, chocolate, feed and leather are inferred examples; count unknown), and food firms with 10+ staff or more than €2M turnover (count unknown).
  - **(a) Packaging EPR (IND-12)** ([BOE, RD 1055/2022](https://www.boe.es/eli/es/rd/2022/12/27/1055/con)):
    - Producers register in the packaging section of the Registro de Productores (the producers' register).
    - They file annual data before 31 March, in simplified form below 15 t.
    - Collective-system fees must appear separately on invoices, and marking has applied since 1 Jan 2025.
    - Commercial and industrial packaging has had EPR systems since end-2024. Separate collection of industrial packaging must reach 75% in 2027.
  - **(b) The EU PPWR (IND-12)** ([EC packaging](https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en)). It has applied since 12 Aug 2026: recyclability by 2030, PFAS limits in food-contact packaging, and reuse and deposit-return targets. Fees and sanction amounts are not verified.
  - **(c) CBAM (IND-13)** ([EC CBAM](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)). The definitive regime has applied since 1 Jan 2026. Importers need authorisation and file declarations, and buy and surrender certificates priced off the EU ETS. Default values were corrected in July 2026 (IR 2026/1740). The 50-tonne de minimis threshold and the number of Spanish importers are **unverified**.
  - **(d) EUDR (IND-14)** ([EC EUDR](https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en)). It applies from 30 Dec 2026 for large and medium operators and from 30 Jun 2027 for micro and small ones. It was amended in Dec 2024 and Dec 2025 and postponed twice.
  - **(e) Food waste (IND-25)** ([BOE, Ley 1/2025](https://www.boe.es/eli/es/l/2025/04/01/1/con)). Covered firms need a prevention plan; having none is a serious infraction (€2,001–60,000). They must also follow a donation priority and sign donation agreements.
- **Driver and status:**
  - RD 1055/2022 is in force, and the PPWR has applied since 12 Aug 2026. The Environmental Omnibus amendment is a proposal (IND-12).
  - CBAM is in force; its downstream extension is a proposal (IND-13).
  - EUDR is upcoming and timing-sensitive (IND-14).
  - Ley 1/2025 is in force. Its art. 6 duties apply about a year after publication (around Apr 2026), but the BOE extract's dates are inconsistent (IND-25).
- **Used today and price:**
  - Collective-system membership, consultants and spreadsheets (IND-12); customs brokers and consultants for CBAM (IND-13); nothing verified for EUDR (IND-14); consultants and food-bank agreements for food waste (IND-25). No prices verified.
  - ERP is already widespread: 60.38% of Spanish firms with 10+ staff against 46.45% in the EU ([Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_enterprises)). Add-on modules fit better than a new ERP (IND-16 inference).

### Cluster 9: Repeat-disaster recovery paperwork (Valencia region)
- **Pain IDs:** CITY-01, CITY-02.
- **Problem:**
  - **The 2024 DANA (CITY-01)** ([La Moncloa, 19 Oct 2026](https://www.lamoncloa.gob.es/info-dana/Paginas/2026/191026-datos-seguimiento-actuaciones-gobierno.aspx)). Businesses faced parallel aid and insurance channels, each with its own forms and evidence:
    - AEAT direct aid: 27,466 applications with a payment order (16,035 autónomos, 11,431 companies) and €347.5M paid. That is about €23,400 per company and €5,000 per autónomo (the notes' arithmetic).
    - ERTE de fuerza mayor (force-majeure furlough): 4,169 companies covering 33,642 workers.
    - ICO guarantees: 3,470 operations.
    - CDTI loan lines: 70 applications, of which 31 approved, 13 still pending and 26 rejected.
    - Consorcio de Compensación de Seguros (the state disaster insurer): 251,940 claims and €4.66bn paid.
    - Reinicia Auto+ vehicle scheme: 43,707 applications.
  - **Uneven recovery.** In 2026Q2 employer units fell 3.50% in Algemesí and 2.39% in Benetússer, against +0.79% for Valencia province ([INE 82132](https://www.ine.es/jaxiT3/Tabla.htm?t=82132)).
  - **A second flood (CITY-02).** The "dana Adam" of 18–19 Oct 2026 hit 27 municipalities (15 in Safor, 12 in Marina Alta).
    - The first €23.5M package covers households and town councils; business aid is deferred with no amounts ([elDiario.es, 21 Oct 2026](https://www.eldiario.es/comunitat-valenciana/gobierno-valenciano-aprueba-paquete-ayudas-23-5-millones-euros-afectados-dana-adam_1_13603195.html)).
    - The Consorcio received 6,528 claims in three days, 2,760 of them from Oliva ([elDiario.es, 22 Oct 2026](https://www.eldiario.es/comunitat-valenciana/consorcio-compensacion-seguros-recibe-6-500-solicitudes-indemnizacion-dana-adam_1_13605957.html)).
- **Driver and status:** extreme weather. The 2024 lines are still paying (852 Consorcio claims and 13 CDTI files pending). For dana Adam a "zona catastrófica" (disaster zone) declaration has been announced and business aid is still to be designed.
- **Used today and price:** government portals (AEAT, SEPE, ICO, Consorcio), gestorías, the Generalitat's single online application, and free legal and notarial help. No prices.

### Conflicts between the notes (validation must resolve)
1. **Valencia ZBE.**
   - *Cities track:* citing valencia.es (21 Oct 2025), it says an ordinance is in force from 1 Dec 2025 and exempts economic-activity vehicles.
   - *ZBE track:* the Pleno (city council) rejected final approval on 28 Oct 2025, with no new vote by Sep 2026, so no ZBE is in force ([ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/)). The ZBE track's sources are later and multiple.
   - Either way, SME vans face little pain in Valencia.
2. **Málaga.**
   - *Cities track:* lists a label-B step on 30 Nov 2026 (Motor16, Sep 2026).
   - *ZBE track:* the ZBE chapter was annulled, fines stopped on 14 Oct 2026, the city will not appeal and the ruling should become final around 25 Nov 2026. The B step is moot.
   - The legal reasoning also conflicts: discrimination or market unity (Motorpasión, elDiario.es) against the domicile challenge being rejected (ecomovilidad).
3. **Zaragoza.**
   - *Cities track:* not operational until at least 2030, with sanctions possibly limited to episodes (the regional audit office, via elDiario.es, 14 Sep 2026).
   - *ZBE track:* the Casco Histórico zone has been in force with fines since 12 Dec 2025 (ecomovilidad).
4. **Vigo label B.** From 2029 (Atlántico, local and more detailed) or from 2027 (Motor16).
5. **Catalonia label B before 2028.**
   - *ZBE track:* required by Decree 132/2024, but municipal ordinance amendments had not started by Oct 2026.
   - *Cities track:* "a plan, not yet law". The official Barcelona ZBE page lists no future B restriction.
6. **Barcelona suspension start.** 22 Jan 2026 (ZBE track) or 28 Jan 2026 (cities track, from the publication of Resolució TER/194/2026 in the DOGC).
7. **Madrid van rules.**
   - *Cities track (RACE, Dec 2025):* unlabelled vehicles not registered in Madrid have been restricted since 2025.
   - *ZBE track (madrid.es FAQ, after Ordenanza 2/2026):* unlabelled vans and trucks may circulate outside the special zones regardless of domicile while NO2 limits hold.
   - Use the ZBE track for vans.
8. **Active ZBE count.** 56 (Feb 2026) against 68 (Sep 2026), with different definitions. 149 or 151 obliged municipalities.
9. **Odoo price.** US$31.10/user/month on annual billing in the transport notes, against €19.90/user/month in the software table.
10. **Ley 1/2025 dates.** Published 02/04/2025, but the extract says "entrada en vigor 02/01/2025" (IND-25).

---

## 4. Noise log

| Pain ID | Title | Code | Justification |
|---|---|---|---|
| IND-03 | Driver shortage, ageing workforce, slow and expensive licensing | N2 | Root causes are demographics, pay and conditions (average age 55, 3% under 25). Software only touches recruitment paperwork, which overlaps LAB-08, ADM-10 and EXP-13 (section 7) |
| IND-05 | Tachograph on 2.5–3.5 t vans in international transport | N5 | Covers only vans doing paid international or cabotage work; no Spanish count. Hardware-bound and served by workshops and telematics. Surveys are trade-press and not representative |
| IND-07 | Cargo theft and insecure rest stops | N1 | "About 20,000 robberies a year" comes from a single source whose underlying data is unnamed. The fix is physical infrastructure |
| IND-08 | Last-mile city-rule patchwork, peaks and new EU customs data | N7 | The city-rule part duplicates ZBE-01 and ZBE-16 (evidence folded into clusters 2 and 3). The €3-per-item customs duty and product-ID sub-pain is single-source and passed to the retail and e-commerce track |
| IND-09 | Mobility plans for logistics employers with over 200 workers | N5 | SMEs are exempt by law (Ley 9/2025 art. 104), leaving a narrow large-employer market |
| IND-10 | Energy volatility and supply reliability | N2 | Price shocks and grid reliability are macro. Spanish industrial electricity is cheaper than the EU average (€0.1336 vs €0.1800/kWh). The software slivers (contract-volume flexibility window, tax relief) expire at end-2026 |
| IND-11 | Shortage of skilled technical trades | N2 | A labour-market problem. A 0.9% vacancy rate against the EU's 2.8% means trade-specific shortages. Overlaps LAB-07 |
| IND-15 | EU Machinery Regulation from 20 Jan 2027 | N5 | Narrow buyer group with no Spanish count or burden data. The technical-file workflow is served by notified bodies and consultants. Revisit if validation finds scale |
| IND-16 | Compliance-ready ERP for small manufacturers | N4 | Basic ERP is crowded: 60.38% ERP use among firms with 10+ staff; Odoo, Cegid Ekon, Sage, a3 and the free FacturaScripts. Compliance add-ons are covered by G5-I01, I05 and I07 |
| IND-17 | US tariff turbulence for exporters | N2 | Policy-driven. Spanish exposure is not quantified and the source is secondary (Wikipedia) |
| IND-22 | Fishing fleets: fuel spike, fewer fishing days, digital controls | N5 | Small population (CEPESCA: more than 700 companies). The core pains (fuel, days) are not software. The EU's own CATCH IT tool is mandated, and the small-vessel deadline is unverified |
| IND-23 | Water scarcity and the Tajo-Segura transfer | N2 | Political and infrastructure allocation. A single interest-group source |
| IND-24 | Animal-disease trade bans | N2 | Diplomatic and sanitary decisions. Software only helps at the edges (traceability) |
| ZBE-08 | Foreign-registered vehicles and cross-border partners | N5 | Buyers are mainly foreign hauliers, tourists and foreign-plated rentals, not Spanish SMEs. The Euro-class-to-label mapping survives through ZBE-18 |
| ZBE-11 | Refund and appeal limbo after court rulings | N3 | Arises from annulled ordinances (Madrid, Málaga). Transient and heavy on legal services, which is the notes' own verdict |
| ZBE-21 | Municipal capacity gap | N5 | The buyer is municipalities through public tenders, outside the SME scope. At most a data-partnership channel for G5-I09 |
| ZBE-22 | Funding conditionality drives "paper" ZBEs | N2 | A policy and political problem; the notes rate it not software-solvable |
| CITY-03 | Madrid ZBE fines on unlabelled out-of-town vehicles | N7 | Duplicates ZBE-10 and ZBE-04. Its H1 2025 counts are folded into cluster 4. Its van rules predate Ordenanza 2/2026 |
| CITY-04 | Barcelona ZBE Rondes: van ban, day passes, stop-start enforcement | N7 | Duplicates ZBE-07 and ZBE-02. The suspension resolution is folded into cluster 3 |
| CITY-05 | Housing costs undermine staff recruitment | N2 | The housing deficit is structural. Recruitment tools belong to the HR and hospitality tracks (HOS-26, LAB-07) |
| CITY-06 | Extreme seasonality in the Balearics | N7 | The software angle (rehiring fijos discontinuos, the permanent seasonal staff, and seasonal planning) duplicates HOS-26 and LAB-14 |
| CITY-07 | Island freight and fuel surcharges, plus the de minimis cap | N1 | One association interview plus one op-ed. The shipping fuel-surcharge (BAF) pass-through could become a G5-I02 add-on if validated |
| CITY-08 | Data-centre boom and grid capacity in Aragón | N1 | No SME-specific evidence (the notes rate it low confidence as an SME pain). The decree is a draft |
| CITY-09 | Zaragoza's municipal SME aid mis-executed and cut | N5 | One city's €400,000 call. The general grant-discovery angle belongs to ADM-16 |
| CITY-10 | Bizkaia stagnation and industrial distress | N2 | Structural, macro industrial restructuring |
| CITY-11 | Weak net business formation in five cities | N2 | A diagnostic indicator, not a pain, per the notes |
| CITY-12 | ZBE patchwork across municipalities | N7 | Duplicates ZBE-01. "68 of 149 active" is folded into cluster 2 |
| CITY-13 | Municipal waste-fee rollout, annulments and refunds | N1 | Evidence is about households; business amounts and impact were not found. Free appeal templates exist. The business angle sits in HOS-11 |
| CITY-14 | 2026 energy and input-cost shock | N2 | A macro shock. Generic pass-through tools are not tied to any obligation; the software-shaped slice is IND-02. Used in the macro weighting |
| CITY-15 | Policy and regulatory uncertainty | N7 | The general phenomenon is covered by ADM-05, LAB-25 and TAX-02. Sector-specific monitoring lives in G5-I03 and I09. Used in the macro weighting |
| CITY-16 | Labour and skills shortage | N2 | Structural. The HR angle is in LAB-07, HOS-01 and CON-01. Used in the macro weighting |
| CITY-17 | Rising cost of credit, tighter finance | N7 | Duplicates FIN-10 in the finance track. Used in the macro weighting |
| CITY-18 | Late payment affects 38% of autónomos | N7 | Duplicates FIN-01. The haulage instance, IND-04, is kept |
| CITY-19 | Administrative time sink for autónomos | N7 | Duplicates TAX-09 and ADM-05. Its advocacy-source figures are used only in the macro weighting |
| CITY-20 | Absenteeism cost | N7 | Duplicates LAB-05 |
| CITY-21 | Fragile young micro-employers | N2 | A diagnostic indicator with macro drivers. Informs churn assumptions in the macro weighting; overlaps FIN-18 |
| CITY-22 | Micro-firm digital gap | N7 | Duplicates RET-07 (web presence). Used as the adoption-capacity weight |
| CITY-23 | Regional laggards on CRM and ERP | N4 | Basic ERP and CRM are crowded markets (same as IND-16), and there is no specific trigger |

---

## 5. Candidate SaaS ideas

Eight ideas follow. The ninth, G5-I09 (the reshaped U3 data layer that G5-I03 and G5-I04 build on), is written out in section 6. None is ranked; that happens after validation.

### G5-I01: DeCA evidence vault and pre-departure check for small hauliers
- **Type:** C (primary): set up once and every trip is archived automatically. B secondary: carrier-side evidence capture that issuance tools are not described as offering.
- **Buyer:**
  - **Who pays:** the owner or office manager of a road-freight carrier with 1–20 vehicles (autónomos and small fleets) doing domestic public haulage.
  - **How many:** 152,871 road-freight companies at the start of 2026, 61,716 of them in heavy transport (IND-01, [trans.info](https://trans.info/es/espana-pierde-miles-de-transportistas-498338)).
  - **Secondary:** SME shippers (cargadores), which are jointly liable and also keep the document for a year; count unknown, validate.
- **Pains addressed:** IND-01. Its trip record also feeds IND-02, IND-04 and IND-06 in G5-I02.
- **Problem:** Since 5 Oct 2026 every domestic haulage service needs a compliant DeCA before departure. Drivers are fined €401–600 when a QR will not load, data is missing or the shipper's document is wrong, and the haulier is "el eslabón más débil de la cadena" (the weakest link in the chain) (IND-01). Issuance is cheap. But carriers who receive documents from shippers keep no proof of what they were given, cannot check completeness before leaving, and have nothing to appeal with. The Ministry waived only the download failures of 5–19 Oct (IND-01).
- **Product:**
  - *What it does:*
    1. Issues a compliant DeCA when the carrier is the issuer: native PDF of at most 5 MB with metadata, a QR to a unique public HTTPS URL, a timestamp before departure, and a copy to the driver.
    2. When the shipper issues it, the driver scans the shipper's QR before leaving. The app fetches the PDF and stores a hashed, timestamped copy. It then checks the mandatory fields, separating shipper data (the shipper's responsibility) from vehicle data (the carrier's).
    3. Shows a "ready to leave" or "missing X" status and alerts the office.
    4. Keeps the one-year archive.
    5. Inspection mode: the stored copy opens offline on the driver's phone, and a one-click "appeal pack" (capture log, timestamps, field check, who was responsible) supports fine appeals.
  - *MVP (4–6 weeks):* a mobile web app with QR scan and PDF capture, a generator for carrier-issued DeCAs, storage with retention, field validation against the published technical rules, and an office dashboard.
  - *Deliberately not:* a TMS or freight exchange, eCMR contracts or e-signature, validating shippers' "provisional DeCAs" on the driver's behalf, or legal representation.
- **Why now:**
  - The rule has been in force since 5 Oct 2026, with live roadside fines.
  - The Ministry admitted DeCA and HeRU failures from 5 to 19 Oct but still prosecutes other infractions (Fenadismer, 22 Oct 2026).
  - Fenadismer warned on 10 Sep 2026 about non-compliant and overpriced tools (IND-01).
  - No superseding mandate is close: authorities must accept eFTI only from 9 Jul 2027, and mandatory use will not be evaluated before 2029 (IND noise list).
- **Alternatives today:**
  - DeCA tools "desde 5 euros al mes" (from €5/month), with other offers up to 1,000% higher and some non-compliant (Fenadismer). No homologated software is required (IND-01).
  - eCMR and e-signature vendors Fieldeas, Viafirma and Edicom, with no public prices.
  - Shippers' private platforms, which shift liability to drivers. UNO's Guía DeCA.
  - *Weakness:* all are centred on issuance. None in the notes keeps the carrier's own proof of shipper-issued documents.
- **Price hypothesis:** €6 per vehicle per month (€59/year), with an association discount to about €4. Bundle with G5-I02 at €19/month for small fleets.
- **Channels:**
  - Fenadismer (32,000+ companies, 60,000 vehicles) and CETM (31,000+ companies, 129,000 vehicles) as endorsers or resellers; regional associations (Astac Condal, ASTRAME); UNO's DeCA guide.
  - Transport gestorías: the software-market notes say compatibility with the gestoría "pesa más que la lista de funciones" (weighs more than the feature list).
  - Truck dealers and fuel-card issuers.
  - Search terms: "DeCA transportista", "documento de control QR multa", "DeCA 5 euros".
- **Build notes:**
  - Follow the Resolución DGTCF of 5 Jun 2026, Orden TRM/282/2026 and Orden FOM/2861/2012: native PDF, QR, HTTPS with TLS 1.2 or higher, download without credentials, and at least one year's retention.
  - Hosting uptime is the product. Driver data is personal data under GDPR.
  - Whether a qualified timestamp is needed is open.
  - Complexity: low–medium.
- **Moat in an AI-flooded market:** Weak. Issuance is a commodity and the evidence features are easy to copy. The edges are speed during the rollout chaos, becoming the tool an association recommends, and archive lock-in (a year of trip records). Treat it as a wedge into G5-I02, not a stand-alone business.
- **Key risks and kill criteria:**
  - *Risks:* the Ministry or an association launches a free generator or repository; shippers' platforms become the de facto standard; the €5 price anchor makes acquisition cost unrecoverable.
  - *Kill if* Fenadismer or CETM already bundle a free tool with evidence capture, or if fewer than 1 in 5 interviewed carriers has had a DeCA incident or fine since 5 Oct 2026.
- **Evidence strength:** Strong. Official texts, association incident reports, a 750-respondent readiness survey and a ministry climb-down all support the pain. Willingness to pay for evidence beyond issuance is unproven.
- **Validation questions:**
  1. Which DeCA tools sell at about €5/month (the offers in Fenadismer's 10 Sep 2026 article), and does any capture and timestamp shipper-issued documents?
  2. Do Fenadismer, CETM or UNO provide or endorse a free or member-priced DeCA tool?
  3. Has the Ministry or DGTCF published an official free generator or repository?
  4. How many DeCA fines have been issued since 5 Oct 2026, by type (download failure vs missing data), and how are appeals going?
  5. Would a carrier's timestamped copy count as evidence in an appeal (transport lawyer's opinion)? Is a qualified timestamp required?
  6. What share of carriers receive DeCAs from shippers rather than issuing them? This sizes the evidence use case.
  7. What do Fieldeas, Viafirma and Edicom charge for DeCA?

### G5-I02: Haulier revenue recovery: automatic fuel-revision lines, detention claims and late-payment interest
- **Type:** B (primary). C secondary: the fuel-line generator alone could run as a low-touch add-on.
- **Buyer:**
  - **Who pays:** the owner or administrator of a carrier with 1–50 vehicles, from the 152,871 road-freight companies (IND-02).
  - **Resellers:** transport gestorías.
- **Pains addressed:** IND-02, IND-06, IND-04, using the IND-01 trip record.
- **Problem:** The 2026 diesel shock raised haulage costs by about 30%, and the G index for heavy vehicles rose 44.6% by 1 Oct 2026. The law already makes the fuel revision automatic and itemised and fines payers who block it. Yet many shippers resist or cut base rates, so carriers absorb the cost (IND-02). The same carriers lose statutory detention pay because claiming needs proof (IND-06). They also finance clients for 52 days on average, with 38% of payers beyond 60 days (IND-04).
- **Product:**
  - *What it does:*
    1. Pulls the Ministry's weekly G index, applies coefficient C by vehicle class and diesel-price band, and puts the itemised revision line on each invoice. The line goes to the carrier's invoicing tool or onto a PDF annex, and works both ways when diesel falls.
    2. Records dock arrival and departure through the driver's phone (geofence) and drafts the art. 22 detention (paralización) claim.
    3. Tracks due dates and computes statutory interest and compensation once the 30-day default point passes (Ley 15/2009 art. 41, Ley 3/2004). Then drafts the claim letter.
    4. When a shipper refuses the line or cuts base rates, assembles an evidence file for Fenadismer's complaint channel or an inspection.
    5. Keeps a private shipper scorecard: days to pay, whether the fuel line is accepted, and average wait.
  - *MVP (4–6 weeks):* G-index calculator, invoice-line generator and payment-term tracker with letter templates. Geofenced detention follows in a second release.
  - *Deliberately not:* debt collection, litigation, factoring, freight matching or a full TMS.
- **Why now:**
  - RDL 9/2026, in force since 16 Apr 2026, made the line mandatory and itemised and created infractions for payers.
  - Fenadismer opened its complaint channel on 13 Oct 2026.
  - Aid under RDL 25/2026 changes monthly until 31 Dec 2026 (IND-02).
  - *Status caveats:* convalidation of RDL 9/2026 and RDL 25/2026 is unverified (IND-02). The underlying indexation rule is in Ley 15/2009 art. 38 itself.
- **Alternatives today:**
  - CETM's "Calculadora de Costes e Indexación" (price and access not shown) and the Ministry's historical ACOTRAM cost simulator (IND-02).
  - TMS, ERP or manual invoicing (no prices).
  - For payment: Wtransnet's Coface guarantee (quote-only), CETM's Icired default registry, confirming and factoring (IND-04).
  - Mainstream invoicing tools carriers may use cost about €6.60–29.50/month on annual billing (software table): Billin Básico €6.60, Holded Plus €7.50 to Estándar €29.50, a3factura from €9.95. None in the notes adds the fuel line.
  - *Weakness:* the calculators do not put the line on invoices, keep evidence, or tie the three revenue leaks together.
- **Price hypothesis:** €19/month for up to 3 vehicles, plus €4 per extra vehicle. Test an optional success fee on recovered detention and interest.
- **Channels:**
  - Fenadismer and CETM, which both campaign on indexation and late payment; regional associations; transport gestorías.
  - Integrations or marketplaces of invoicing software; fuel-card issuers.
  - Search terms: "coeficiente G gasóleo", "revisión precio combustible factura transporte", "paralización camión reclamar".
- **Build notes:**
  - Weekly G-index source (format unverified) and the per-vehicle-class formula from RDL 9/2026.
  - Invoice integrations with tools in the software table. Letter templates reviewed by a transport lawyer.
  - Driver geolocation requires informing workers and complying with data-protection rules.
  - Shipper scorecards raise defamation and data-protection questions where shippers are autónomos; CETM's Icired registry is a precedent.
  - Complexity: medium.
- **Moat in an AI-flooded market:** Medium. The formula and templates can be copied in days. The defensible part is an aggregated, anonymised dataset of shipper behaviour (payment days, fuel-line acceptance, waits) that grows with every user. Association distribution and the trip record shared with G5-I01 add to it.
- **Key risks and kill criteria:**
  - *Risks:* carriers may not dare to bill the line or claim detention for fear of losing clients. A diesel slide shrinks or reverses the line, which moves the value to shippers. CETM's calculator may already do this free for members.
  - *Kill if* 60% or more of 15–20 interviewed hauliers would not add the line even if it were automatic, or if CETM's tool already produces invoice lines and evidence.
- **Evidence strength:** Strong for the fuel line and late payment (BOE texts, Fenadismer's payment observatory). Medium for detention (a single 2023 study).
- **Validation questions:**
  1. What does CETM's calculator do, at what price, and is it member-only?
  2. Does the Ministry publish the weekly G index in machine-readable form?
  3. Were RDL 9/2026 and RDL 25/2026 convalidated? With the Cortes dissolved since 6 Oct 2026, how and when was RDL 25/2026 handled?
  4. Do the TMS used by Spanish SME hauliers (identify the top 3–5) already automate the fuel line? Do Holded, Quipu or a3factura expose APIs for adding invoice lines?
  5. How many complaints has Fenadismer's channel received, and have any shippers been sanctioned?
  6. What is the current IPREM, what does a typical detention claim come to, and how often do carriers claim it today?
  7. Get a legal review of shipper scorecards (data protection for autónomo shippers, competition law).

### G5-I03: ZBE alerts and "can my van go there?" checker for autónomos with vans
- **Type:** C.
- **Buyer:**
  - **Who pays:** autónomos and micro firms with 1–5 vans: trades, small couriers, market and food suppliers (ZBE-05 inference).
  - **Fleet:** 2,741,010 vans nationally, 1,084,677 of them aged 20+ (DGT, ZBE-05).
  - **Likely owners:** about 184,800 land-transport and 286,800 specialised-construction autónomos nationally (my arithmetic: 5.8% and 9.0% of 3,186,989 autónomos, INE 82138, cities notes). In the provinces of Madrid and Barcelona alone, about 58,700 and 70,400.
  - Not all have vans or enter ZBEs; validate.
- **Pains addressed:** ZBE-01, ZBE-02, ZBE-04, ZBE-10, ZBE-12, ZBE-13, ZBE-14, ZBE-17, ZBE-23. Data for ZBE-03 and ZBE-19 comes through G5-I09.
- **Problem:** Whether a given van may enter depends on label, category, domicile, time, day type and permits. The answer changed repeatedly in 2026: Madrid on 7 Apr, Málaga on 14 Oct, and Barcelona's suspension (ZBE-01, ZBE-02). Each wrong entry costs €200, and Madrid alone issued 261,115 unlabelled-access fines in H1 2025 (CITY-03, folded into ZBE-10). Known future dates will catch owners who ignored warnings: Palma excludes label B from 1 Jan 2027, Catalonia must restrict B before 2028, and Vigo fines from 10 Sep 2027 (ZBE-14, ZBE-23).
- **Product:**
  - *What it does:* the user registers plates (label, category, MMA, domicile) and the cities or addresses they work in, and gets:
    1. an instant "allowed", "allowed with permit" or "not allowed" answer for a place and time, with the rule's source;
    2. alerts when a rule affecting their vehicles changes: court rulings, suspensions, episode days, switch-on dates;
    3. a personal calendar ("your van stops being compliant in Palma on 1 Jan 2027");
    4. renewal reminders for exemptions and permits: Madrid's yearly 59+ authorisation and night-delivery declaración, Barcelona's near-retirement exemption to 31 Mar 2028, Bilbao's 2-day plate notification;
    5. simple quota counters: Barcelona 24 day-passes a year, Zaragoza 8 accesses a month, Bilbao 6 invitations a month;
    6. a fine tracker that reminds the early-payment deadline.
  - *MVP:* 4–6 weeks of code, but curation is the real work. It covers the nine sanctioning cities plus A Coruña, with email and push alerts, the calendar and the checker.
  - *Deliberately not:* route optimisation, filing permits for the user (possible later), appeals or legal advice.
- **Why now:**
  - 2026 is the year of court whiplash (ZBE-02).
  - New switch-on and phase-out dates cluster around 31 Dec 2026 and 1 Jan 2027: the end of Madrid's resident warnings, Palma's B exclusion and the end of Badalona's moratorium (ZBE-14, ZBE-23).
  - Madrid's NO2-conditional regime for unlabelled vans could end on six months' notice (ZBE-13).
- **Alternatives today:**
  - The ZBE España iOS app (tagged free; maps Madrid, Barcelona, Valencia and Sevilla; checks label compatibility).
  - The Astac/RACC national site; the ecomovilidad, Iberfurgo and RACE guides (free, secondary, sometimes wrong).
  - The DGT label lookup and municipal registries such as AMB's (free) (ZBE-01, ZBE-03).
  - *Weakness:* all are static and not vehicle-specific. None sends alerts or handles domicile, quotas or episodes, and some are stale (Green-Zones).
- **Price hypothesis:** €4.99/month or €39/year for up to 3 vans, with a free single check to acquire users.
- **Channels:**
  - Van-rental and renting firms, bundled at hand-over; fleet insurers, as a risk-reduction add-on.
  - Transport and trades associations (Fenadismer and Astac for van hauliers); gestorías serving autónomos.
  - App stores and search ("ZBE furgoneta sin etiqueta", "puedo entrar ZBE Madrid furgoneta"); partnerships with ZBE information sites.
- **Build notes:**
  - The data layer is shared with G5-I09: NAP DATEX II files and city polygons (CC BY 4.0, attribution required), plus curated ordinance rules and weekly legal monitoring.
  - Whether the DGT allows programmatic label lookups is unverified (ZBE-18).
  - Autónomos' plates are personal data under GDPR. WhatsApp alerts are metered (see RET-10).
  - Complexity: medium, with light code and heavy curation.
- **Moat in an AI-flooded market:** Medium–low. The app is easy to copy. The hard part is keeping a versioned, legally checked rulebook current (2026 shows how often it changes) and being accurate enough to promise it. That cost is shared with G5-I04 and G5-I09.
- **Key risks and kill criteria:**
  - *Risks:* low willingness to pay among owners who are keeping old vans until they exit; churn once they renew or retire; free apps adding alerts; softening enforcement (none in Valencia, disputed in Zaragoza).
  - *Kill if* a 4-week pilot converts fewer than 3% of free checkers to paid, or if ZBE España or the Astac/RACC site already offers vehicle-specific alerts.
- **Evidence strength:** Medium. Fragmentation and volatility are strongly evidenced by official pages and direct parsing of the NAP feed. The business share of fines and willingness to pay are unknown.
- **Validation questions:**
  1. What do ZBE España, the Astac/RACC site and RACE's tools offer and charge? Do any send personalised alerts?
  2. Can the DGT label be looked up programmatically by plate, and on what terms?
  3. What share of Madrid ZBE fines goes to commercial vehicles or companies? Ask Madrid or AEA.
  4. How many vans per label are registered in each target city? Query the DGT fleet panel.
  5. What will 50 trades autónomos with B or unlabelled vans in Madrid, Barcelona and Palma pay?
  6. Resolve the date conflicts: Vigo B (2027 vs 2029), Zaragoza enforcement, Valencia's status, Catalonia's 2028 B rule.
  7. Is there a machine-readable source for pollution-episode declarations in Madrid and Barcelona?

### G5-I04: ZBE-aware dispatch check and permit ledger for SME delivery fleets
- **Type:** B.
- **Buyer:**
  - **Who pays:** the operations or dispatch manager at SME wholesalers and distributors supplying shops, markets and hotels, restaurants and cafés (HORECA); at regional parcel subcontractors; and at multi-city service firms with 3–50 vans.
  - **Upper-bound pool:** about 75,100 wholesale and 60,300 land-transport employer units nationally (my arithmetic: 6.1% and 4.9% of 1,231,358 employer units, INE 82131). The number with vans in enforcing cities is unknown; validate.
- **Pains addressed:** ZBE-06, ZBE-07, ZBE-15, ZBE-16, ZBE-04, ZBE-09 (rented and replacement vans), ZBE-14 (fleet plan).
- **Problem:** For in-zone stops the fine depends on which van goes, at what hour and with which permit, not on the route (ZBE-15). Dispatchers track the rules in their heads or in spreadsheets: Madrid Distrito Centro's label- and MMA-specific windows, per-plate registrations and yearly night-delivery declarations (ZBE-06, ZBE-16), and the quotas in Bilbao, Barcelona and Zaragoza (ZBE-07). No Spanish ZBE-aware dispatch product was found (ZBE-15).
- **Product:**
  - *What it does:*
    - A fleet register: label, category, MMA, domicile, and ownership or rental contract.
    - A permit wallet: registrations, declarations, quotas and expiry dates.
    - A nightly check of tomorrow's stops (CSV or API from the route planner). It flags vehicle, stop and time conflicts and proposes fixes: swap the van, move the window, use a quota, or unload at an exempt car park.
    - It then logs quota use, reminds plate notifications (Bilbao, within 2 days) and builds the yearly Madrid declaración pack from delivery notes.
  - *MVP (6–8 weeks):* Madrid, Barcelona/AMB, Bilbao and Zaragoza rules; CSV import; conflict report; permit and quota ledger.
  - *Deliberately not:* a route optimiser or TMS (it integrates with them); automatic filing in city portals, most of which have no APIs; loading-bay availability.
- **Why now:**
  - Madrid's Ordenanza 2/2026 regime has applied since 7 Apr 2026.
  - Bilbao has restricted label B since Jun 2025, and Barcelona has banned B in episodes since 1 Jan 2026.
  - Palma and Catalonia phase out B in 2027–2028 (ZBE-06, ZBE-14).
  - UNO expects more than 127M shipments over Black Friday and Christmas 2026 (folded from IND-08).
- **Alternatives today:**
  - Dispatcher knowledge and spreadsheets.
  - HERE and TomTom avoidance: based on Euro class, no help for in-zone stops, Spanish coverage and price unknown. Google Routes API, PTV, Sygic Truck and Webfleet were not checked for Spanish ZBE handling (ZBE gaps).
  - Madrid's Mi Carpeta and other city portals; gestorías (no prices) (ZBE-06, ZBE-15).
- **Price hypothesis:** €9 per vehicle per month, minimum €49/month.
- **Channels:**
  - UNO (350+ logistics members); food and drink distributors reached through FIAB's members; HORECA supplier networks.
  - Route-planning and telematics vendors, by white-label or integration.
  - Search terms: "ZBE reparto Distrito Centro", "invitaciones ZBE Bilbao empresas".
- **Build notes:**
  - Rules engine shared with G5-I09; route-planner and telematics integrations.
  - Filing on clients' behalf requires checking the representation rules. Vehicle and driver data fall under GDPR.
  - Complexity: medium–high.
- **Moat in an AI-flooded market:** Medium. Constraint logic, permit workflows and integrations are harder to copy than a rules app. The risk is that route planners add Spanish ZBE semantics.
- **Key risks and kill criteria:**
  - *Risks:* the pain may sit mostly with price-sensitive small operators, since large parcel carriers renewed their fleets early (ZBE inference); enforcement may soften; demand is inferred.
  - *Kill if* fewer than 5 of 20 interviewed distributors in Madrid, Bilbao or Barcelona report ZBE fines or at least 2 hours a week of permit admin.
- **Evidence strength:** Medium. The mechanism is well evidenced (madrid.es, the HERE documentation); demand is inferred.
- **Validation questions:**
  1. Interview 20 SME distributors serving Madrid Distrito Centro, Bilbao and Barcelona: fines per month, permit hours, current tools.
  2. Do Google Routes API, PTV, Sygic Truck, Webfleet/TomTom or HERE handle DGT labels, domicile and quotas for Spain, and at what price?
  3. How many plates are registered in Madrid's Sistema de Gestión de Permisos? File a transparency request.
  4. Do Bilbao, AMB and Zaragoza offer APIs or bulk upload for invitations and passes?
  5. May a SaaS file registrations or declarations on a client's behalf?
  6. What do Spanish fleet-software products charge per vehicle? The notes have no benchmark.

### G5-I05: RCA autopilot: contract generation and registration before delivery for food buyers (wine harvest first)
- **Type:** B.
- **Buyer:**
  - **Who pays:** the purchasing or admin manager at food-industry SMEs that buy from farmers (wineries, fruit and vegetable packers, meat and dairy processors), at origin wholesalers, and at cooperatives buying from non-members.
  - **How many:** more than 27,300 food and drink companies (FIAB), 3,669 agri-food cooperatives and 950+ FEV member wineries (IND-18, IND-19).
- **Pains addressed:** IND-18, IND-19, IND-21 (cost-of-production evidence).
- **Problem:** Every purchase from a farmer needs a signed written contract with minimum terms and a price above the producer's costs, registered in the RCA before delivery (IND-18). In 2025 AICA sanctioned 991 infractions. 506 of them (51%) were failures to register, all by the industry link. 619 (62%) were in wine, 616 of them on wine grapes, where hundreds of grower deliveries arrive within days at harvest (IND-18, IND-19). Fines run from €250–3,000 for minor infractions to €3,001–100,000 for serious ones, and serious fines are published (IND-18).
- **Product:**
  - *What it does:*
    1. Contract templates with all minimum terms, the price and a cost-of-production clause, which the grower signs through a mobile link.
    2. Bulk registration through the RCA API, triggered by a purchase order or weighbridge ticket and confirmed before the load is accepted.
    3. Amendments re-registered automatically; price changes need both parties' agreement (53 infractions).
    4. Payment-term alerts (186 payment breaches).
    5. A per-grower evidence file, including the grower's cost declaration or a reference cost-of-production figure (IND-21).
    6. An inspection pack.
  - *MVP (6–8 weeks):* contract generator, bulk upload through the RCA API, status dashboard, and CSV import from the weighbridge or ERP.
  - *Deliberately not:* farm management, a winery ERP, INFOVI wine-market declarations (possible later), price advice or legal representation.
- **Why now:**
  - AICA's 2025 report, published 24 Sep 2026, shows record enforcement and where it bites.
  - AICA opened consultation on a new inspection decree on 30 Sep 2026. It is a draft and may stall with the 29 Nov election (IND-18).
  - The 2026 input-cost shock makes the "price above cost" clause more contentious (IND-21).
- **Alternatives today:**
  - Manual web uploads with a digital certificate, at most 5 documents and 5 MB each.
  - The RCA API, for high-volume buyers who build their own integration.
  - Gestorías and consultants; winery ERPs (not verified). No prices in the notes (IND-18, IND-19).
  - Generic e-signature is costly at harvest volume: Signaturit Business costs €35/user/month for 5 envelopes and Business+ €57 for 20 (software table).
- **Price hypothesis:** €39/month for up to 300 contracts a year and €99/month for up to 3,000. Alternatively, a €149 harvest-season pass for small wineries.
- **Channels:**
  - FEV, Cooperativas Agro-alimentarias, FIAB, and agri gestorías.
  - Winery and agri ERP vendors (integration or white-label) and weighbridge software vendors.
  - Search terms: "registro contratos alimentarios", "RCA AICA contrato uva", "contrato vendimia ley cadena".
- **Build notes:**
  - RCA API access and documentation.
  - Handling the buyer's digital certificate or delegated access (see ADM-07).
  - Simple e-signature. Growers' personal data falls under GDPR.
  - Contract templates reviewed by a food-chain lawyer.
  - Complexity: medium.
- **Moat in an AI-flooded market:** Medium. Templates can be copied. The RCA integration, weighbridge and ERP connectors, reliability at harvest peaks and association endorsement are real friction, and the contract archive creates switching costs.
- **Key risks and kill criteria:**
  - *Risks:* AICA improves bulk upload; winery ERPs add RCA integration free; many buyers are tiny and seasonal; cooperatives buying from their members are exempt.
  - *Kill if* the leading winery and agri ERPs already integrate the RCA API at no extra cost, or if interviewed buyers spend under an hour per season on the RCA.
- **Evidence strength:** Strong. Official enforcement statistics and legal texts support it. That the wine infractions are mostly unregistered harvest contracts is the notes' inference.
- **Validation questions:**
  1. What are the RCA API's access requirements and documentation? Are third-party integrators already listed?
  2. Which Spanish winery and agri-food ERPs integrate the RCA API, and at what price?
  3. How many distinct buyers register in the RCA, and how many contracts a year?
  4. Ask AICA for the cross-tabulation: how many of the 616 grape infractions were failures to register?
  5. What is the status of the draft AICA inspection decree after the election call?
  6. What do gestorías charge for RCA uploads?
  7. Legal: can a SaaS act through API credentials or a delegated certificate on the buyer's behalf?

### G5-I06: Fertilisation-plan and nutrient-record workspace for advisers and cooperative technical services
- **Type:** B (primary). A secondary if validation finds priced farm-notebook apps it can undercut.
- **Buyer:**
  - **Who pays:** REGFER-registered fertilisation advisers, cooperatives' technical services and larger farms.
  - **How many:** 3,669 agri-food cooperatives with more than 1M member families (IND-20). The number of registered advisers and of non-exempt farms is unknown; validate.
- **Pains addressed:** IND-20.
- **Problem:** Since 1 Sep 2026 non-exempt farms need a plan de abonado, and each fertilisation must be logged within a month. Advisers have had to register in REGFER since 1 Jul 2026, and agronomic advice becomes mandatory one year later in vulnerable zones and two years later elsewhere (IND-20). The digital farm notebook (CUE) is postponed to the next CAP period, so farmers and vendors do not know what to adopt. The sector calls the burden "inasumible" (unbearable) (IND-20).
- **Product:**
  - *What it does:* a multi-farm workspace for one adviser:
    - parcels, crops and soil analyses;
    - a plan generator following RD 1051/2022;
    - farmer-side mobile or WhatsApp logging of each application, with one-month reminders;
    - adviser sign-off;
    - export to SIEX (the national farm-data system) and regional formats;
    - a data model ready for the future CUE.
  - *MVP (6–8 weeks):* plan generator for the main crops, record logging with reminders, and PDF or CSV export.
  - *Deliberately not:* a full farm ERP, phytosanitary records (later), or CAP aid applications.
- **Why now:**
  - The duties have been live since 1 Jul and 1 Sep 2026.
  - Mandatory agronomic advice follows in 2027–2028 (my inference from the one- and two-year lags).
  - Bureaucracy is a headline demand of the 28 Oct 2026 tractor protest (IND-20).
- **Alternatives today:** free public CUE software (administrations must offer it), the Cuaderno de Campo Cooperativo, advisers' spreadsheets, and private farm apps (Agroptima is named; prices not verified) (IND-20).
- **Price hypothesis:** €39/month per adviser for up to 25 farms, plus €1.50 per extra farm per month.
- **Channels:**
  - Cooperativas Agro-alimentarias, UPA, ASAJA and Unió de Pagesos; input distributors; the REGFER adviser list.
  - Search terms: "plan de abonado RD 1051/2022", "REGFER asesor".
- **Build notes:** SIEX and regional formats. The agronomic rule tables need an agronomist. Farm data is moderately sensitive. Complexity: medium.
- **Moat in an AI-flooded market:** Low–medium. The agronomic rules and regional exports take work, but free public tools and cooperative notebooks compete.
- **Key risks and kill criteria:**
  - *Risks:* public or cooperative tools cover plans for free; the eventual CUE design forces a rebuild; advisers are few and price-sensitive.
  - *Kill if* the Cuaderno de Campo Cooperativo or the free public software already generates plans de abonado.
- **Evidence strength:** Medium. The obligations are official, but the burden is described rather than quantified and competitors are unpriced.
- **Validation questions:**
  1. Do the free public software and the Cuaderno de Campo Cooperativo generate plans de abonado?
  2. What do private apps (Agroptima and others) offer and charge?
  3. How many advisers have registered in REGFER since 1 Jul 2026?
  4. How many farms are above the plan thresholds and so not exempt?
  5. What are SIEX's exchange format and API availability, and how do regions differ?
  6. Have there been any inspections or sanctions for missing plans yet?

### G5-I07: Packaging EPR and PPWR declaration assistant for food, drink and small manufacturers
- **Type:** B (primary). C secondary: once the packaging catalogue is set up, the annual declaration runs largely on autopilot.
- **Buyer:**
  - **Who pays:** the quality, compliance or admin manager at food and drink SMEs (27,300+ companies, 483,300 jobs, FIAB).
  - **Also:** other small manufacturers placing packaged goods on the market; count unknown, validate (IND-12).
- **Pains addressed:** IND-12 (core); IND-25 (food-waste plan module); IND-14 and IND-13 (later modules).
- **Problem:** Packaging producers must register, declare tonnes by material every year before 31 March (simplified below 15 t), show collective-system fees separately on invoices and mark their packaging. Commercial and industrial packaging has been under EPR since end-2024, and the EU PPWR has applied since 12 Aug 2026 with recyclability, PFAS and reuse rules (IND-12). Food firms with 10+ staff or over €2M turnover also need a food-waste prevention plan; having none is a serious infraction of €2,001–60,000 (IND-25). Today this runs on consultants and spreadsheets (IND-12).
- **Product:**
  - *What it does:*
    - Builds a packaging bill of materials per SKU (component, material, weight), imported from the ERP or Excel or extracted by AI from supplier spec sheets.
    - Multiplies it by volumes sold to get tonnes by material, split into household and commercial or industrial packaging.
    - Produces the annual declaration report and the fee lines for invoices.
    - Runs a PPWR checklist per pack and keeps a document archive.
  - *Modules:* a Ley 1/2025 food-waste plan and donation log. Later, EUDR supplier geolocation and due-diligence statements, and CBAM supplier-emissions collection, both on the same supplier and product data.
  - *MVP (6–8 weeks):* BOM catalogue, tonnage calculation and declaration export.
  - *Deliberately not:* acting as a collective system, certifying recyclability, lab testing or legal advice.
- **Why now:**
  - The PPWR has applied since 12 Aug 2026, and the next annual declaration is due before 31 Mar 2027.
  - EUDR applies from 30 Dec 2026 for large and medium operators and from 30 Jun 2027 for micro and small ones (IND-12, IND-14).
  - *Caveats:* the Environmental Omnibus is only a proposal, and EUDR has been postponed twice (IND-12, IND-14).
- **Alternatives today:**
  - Collective-system membership, consultants and spreadsheets (prices not verified).
  - ERPs are widespread (60.38% of firms with 10+ staff, Eurostat), but none in the notes has a packaging module (IND-12, IND-16). Odoo lists at US$31.10/user/month in the transport notes or €19.90 in the software table; the notes conflict.
- **Price hypothesis:** €39/month (€390/year) per company; the food-waste module adds €10/month.
- **Channels:**
  - FIAB and sector associations.
  - Collective systems, as data-exchange partners; ERP vendors and consultants, by white-label; packaging suppliers, for spec-sheet data.
  - Search terms: "declaración anual envases", "RD 1055/2022 envases industriales", "PPWR pymes".
- **Build notes:** Declaration formats for the Registro de Productores and for collective systems; PPWR delegated acts. Product data is commercially sensitive. Complexity: medium.
- **Moat in an AI-flooded market:** Medium. The moat would be a growing library of packaging components and supplier specs across customers (proprietary data) plus connectors to collective systems and ERPs. The calculator alone is copyable.
- **Key risks and kill criteria:**
  - *Risks:* collective systems give members free declaration tools; producers below 15 t face a light simplified regime; the PPWR's main obligations are dated 2030, so urgency is low.
  - *Kill if* the main collective systems already offer free BOM-to-declaration tools, or if a typical SME prepares the declaration in under a day.
- **Evidence strength:** Medium. The obligations are official, but the burden, fees and sanction amounts are not in the notes. The retail side corroborates it (RET-15).
- **Validation questions:**
  1. Which collective systems serve household and commercial or industrial packaging in Spain? What tools do they give members, and at what fee?
  2. How many producers are registered in the packaging section of the Registro de Productores?
  3. What are the annual declaration's format and portal, and the sanction amounts under Ley 7/2022?
  4. Which packaging-compliance SaaS products already sell in Spain, and at what price?
  5. Which PPWR duties bite SMEs in 2026–2027, and which only in 2030?
  6. Ley 1/2025: when do the art. 6 duties apply (the BOE extract's dates conflict), and what are the regional infraction rules?
  7. What is the status of the Environmental Omnibus, and how does the Dec 2025 EUDR simplification affect micro and small operators?

### G5-I08: Flood-ready business evidence vault and multi-programme claims tracker
- **Type:** C.
- **Buyer:**
  - **Who pays:** owners of shops, bars, workshops and industrial-estate firms in flood-prone areas, sold through insurers, brokers and gestorías.
  - **Where first:** the provinces of Valencia (186,970 companies) and Alicante (145,106) (DIRCE, cities notes).
  - **Reference point:** 27,466 businesses and autónomos received DANA 2024 aid (CITY-01).
- **Pains addressed:** CITY-01, CITY-02.
- **Problem:** After the October 2024 DANA, businesses faced parallel channels: AEAT aid, ERTE furloughs, ICO, CDTI, the Consorcio (251,940 claims) and Reinicia Auto+. Each had its own forms and evidence, and some files are still pending two years later (CITY-01). A second flood (dana Adam, 18–19 Oct 2026) hit 27 municipalities and produced 6,528 Consorcio claims in three days. Business aid for it is still undefined (CITY-02).
- **Product:**
  - *What it does:*
    - *Before an event:* a guided inventory (photos and video of premises, stock and equipment, serial numbers, purchase invoices), plus insurance policies and key documents, stored off-site with quarterly refresh reminders.
    - *After an event:* a one-click claim dossier for the insurer or the Consorcio, and a tracker of announced aid programmes with deadlines and required documents.
  - *MVP (3–4 weeks):* mobile inventory, vault, dossier PDF and a manually curated aid list.
  - *Deliberately not:* loss adjusting, brokerage or legal claims.
- **Why now:** dana Adam's business aid package is pending, and floods two years apart make the need recurring (CITY-01, CITY-02).
- **Alternatives today:** government portals, gestorías, the Generalitat's single online application, and free legal and notarial help (CITY-02). No prices.
- **Price hypothesis:** €4/month per premises, or bundled free by an insurer or bank.
- **Channels:** insurers and brokers (business-to-business-to-consumer), gestorías, business associations in the affected comarcas (districts), town-hall business services.
- **Build notes:** Storage and invoice OCR. Financial documents need secure hosting. Complexity: low.
- **Moat in an AI-flooded market:** None; speed only. A generic vault is trivially copyable. The only edge would be a distribution deal with an insurer or bank.
- **Key risks and kill criteria:**
  - *Risks:* people rarely pay before a disaster; demand spikes afterwards and public portals absorb it; insurers can build this themselves.
  - *Kill if* no insurer, broker or gestoría network agrees to a pilot, or if pre-event sign-up in Safor or Marina Alta converts below 2%.
- **Evidence strength:** Medium. The 2024 aid and claim volumes are official (La Moncloa), and the 2026 event comes from a single outlet. Willingness to pay for a preventive product is unevidenced, and the idea overlaps the finance track (FIN-19, FIN-20, FIN-21).
- **Validation questions:**
  1. What evidence did the Consorcio and AEAT require in 2024, and what caused delays or rejections? (See the FIN-19 track.)
  2. Do Spanish insurers already offer pre-loss inventory apps?
  3. What share of dana Adam's claims comes from businesses, and what will the second aid package contain?
  4. Will brokers or gestorías distribute a €4 vault?
  5. How many businesses sit in official flood-risk zones in the Valencia region?

---

## 6. User-supplied idea U3 (EcoRoute)

### What the notes support and contradict

| U3 claim | What the notes say | Verdict |
|---|---|---|
| ZBEs are "strict" and "enforced by automated camera tracking" | **True where cities fine:** Madrid (OCR and "foto rojo" red-light cameras), Barcelona (perimeter plate cameras), Bilbao and Zaragoza (plate readers), Sevilla-Cartuja, Palma, Granada, and Málaga until 14 Oct 2026 (ZBE fact-check, claim 1). **False as a generalisation:** probably about 50 of the roughly 150 obliged municipalities fine (inference); 17 of 23 large Catalan municipalities did not fine effectively in 2025; Valencia's cameras only count traffic; Vigo is information-only to 10 Sep 2027; Alicante sends notices only (ZBE-21, ZBE-23). Some cameras check authorisation rather than labels (A Coruña, Alicante's Anillo I) | **Partly supported.** Safe only as "the major ZBEs that fine use plate cameras" |
| Target cities are Valencia, Madrid and Barcelona | Madrid has the largest fine volume: more than 3.4M files and €663M to end-2025 (ZBE-10). Barcelona bans unlabelled vans on weekdays 7–20h (ZBE city table). Valencia has no ZBE in force: final approval was rejected on 28 Oct 2025 and there was no new vote by Sep 2026. Its draft did not restrict vans, and Vox's condition for approving one is "sin régimen sancionador" (without a sanctions regime) ([ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/); [El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html)). The cities notes instead cite an Oct 2025 approval that exempts economic-activity vehicles, which conflicts. Either way SME vans face little or no Valencia pain | **Madrid and Barcelona supported. Valencia contradicted as a market** |
| Connect to Barcelona and Valencia open-data feeds | Both publish **perimeter polygons only** (CC BY 4.0). Barcelona has one 2023 GPKG file covering the city alone, not all Rondes municipalities ([Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/zbe-ambit)). Valencia has a GeoJSON/WFS layer for an ordinance that is not in force ([Valencia open data](https://opendata.vlci.valencia.es/dataset/zona-de-bajas-emisiones)). Neither has labels, hours or exemptions. Rules come only from the DGT NAP, whose Valencia record says "active" from 1 Jun 2026 (ZBE-03) | **Partly supported.** Free geometry yes, usable rules no. Free official geometry also caps the price of any geometry-only product |
| Optimise daily routes to avoid emission penalties | Avoidance routing, already offered by HERE and TomTom, helps only through-traffic. For a stop inside the zone, compliance depends on vehicle choice, time windows, permits and quotas, exempt car parks and standing registrations (ZBE-15). The notes list "route optimisation avoids ZBE penalties" as a dead end for in-zone stops | **Contradicted** for in-zone deliveries, which are the core e-commerce and HORECA case |
| Use Valencia's "Urban Sandbox" to test smart-mobility models | The *Ordenanza reguladora del Sandbox Urbano de València* exists. It rests on Ley 28/2022 art. 16. Procedure AE.IN.100 is permanently open, decisions take at most 3 months and silence counts as rejection. Test protocols run up to 5 years, and municipal spaces are free to use ([ordinance text](https://sede.valencia.es/sede/descarga/doc/DOCUMENT_1_20240006949868); [AE.IN.100](https://sede.valencia.es/sede/registro/procedimiento/AE.IN.100?lang=1)). But it is **cross-sector**, it **cannot waive non-municipal rules** such as DGT and state traffic law (art. 11.3), its final approval and BOP publication are unverified, and no mobility projects are named. In June 2026 the city announced an alliance to bring port logistics into the Sandbox ([Paréntesis.Media](https://www.parentesis.media/valencia-madrid-y-barcelona-convierten-la-ia-en-un-laboratorio-urbano-bajo-control-juridico/)) | **Partly supported.** A plausible pilot channel (city or port), not a legal framework for the product |
| The burden falls on "commercial fleets and local e-commerce delivery partners" | Final-mile parcel delivery is exempt from the DeCA but not from ZBEs (IND-01, IND-08). The ZBE notes infer that large parcel carriers renewed their fleets early and that the pain sits with small autónomos keeping old vans until they exit (ZBE-05) | **Partly supported.** The pain is real but sits with small operators who do not buy APIs, so an API must be sold to the software and rental firms that serve them |
| The regional table casts Valencia as the "open civic data testing capital" for a ZBE logistics API | Valencia's ZBE open data describes a zone that does not exist yet (ZBE-03). Regional digital adoption is close to the national average: in the Comunitat Valenciana 63.1% of firms with 10+ staff use ERP and 34.1% use AI, against 60.9% and 33.6% nationally (INE, cities notes) | **Not supported for revenue.** Supported only as a pilot venue (Sandbox, port) |

### Verdict: reshape (keep the market, change the product)
- **Keep:** ZBE compliance for commercial vans is a real, software-shaped problem. The rules are fragmented and volatile, the free data is stale and thin, and fines run to millions in Madrid (clusters 2–5).
- **Change the product.** Move from a "green routing API" to a **rules and in-zone compliance-check API**: a curated, versioned and legally monitored dataset, plus an endpoint answering "can vehicle X serve stop Y at time T, and if not, what are the options?" Routing stays with partners such as HERE and TomTom, which already avoid zones.
- **Change the launch geography.** Launch in the cities that fine: Madrid, Barcelona/AMB, Bilbao, Palma, Granada, Sevilla-Cartuja, Valladolid, Córdoba, A Coruña, and Zaragoza if its status is confirmed. Use Valencia's Sandbox and the port alliance for a pilot, not for revenue.
- **Build end-user products on the same data layer:** G5-I03 (alerts for autónomos) and G5-I04 (dispatch and permits for SME fleets).
- **Flag:** the paying API market may be small, and HERE, TomTom or a large telematics vendor could add Spanish semantics. These are the main kill risks, and validation should test them first.

### G5-I09: EcoRoute reshaped: Spanish ZBE rules and in-zone compliance-check API
- **Type:** B (primary). A secondary: an SME-affordable alternative to enterprise LEZ data from HERE and TomTom, whose prices are unknown.
- **Buyer:**
  - **Who pays:** software firms serving Spanish fleets (route planners, TMS, telematics and fleet management); navigation and mobility apps; renting, leasing and van-rental firms; fleet insurers; logistics operators with in-house dispatch. Count unknown; validate.
  - **Secondary:** associations and media, through data licensing.
- **Pains addressed:** ZBE-01, ZBE-02, ZBE-03, ZBE-04, ZBE-09, ZBE-15, ZBE-18, ZBE-19, ZBE-20, ZBE-23. Folded: CITY-12, IND-08.
- **Problem:** About 150 obliged municipalities have rules that diverge and change at short notice (ZBE-01, ZBE-02). The free national NAP feed is:
  - incomplete: no Zaragoza, Vigo, Córdoba, Murcia or Las Palmas;
  - stale: Valencia shown "active" with no ZBE in force, and Málaga still "active" after fines stopped;
  - thin: no vehicle category, MMA, domicile, quotas, phase dates or episodes (ZBE-03).

  City portals publish only perimeters. HERE and TomTom model Euro classes, not DGT labels or local exemptions (ZBE-18, ZBE-20). And routing cannot avoid penalties for in-zone stops (ZBE-15).
- **Product:**
  - *What it does:*
    1. A versioned rules dataset. Geometry comes from the NAP and city portals (CC BY 4.0); rule detail is curated from ordinances, official bulletins and rulings. Every rule carries its source, effective dates and legal status: in force, annulled but not final, suspended, or in an information phase.
    2. Endpoints:
       - `zones`: perimeters and status.
       - `check`: vehicle (label, category, MMA, domicile, permits) at a stop (coordinates or address) at time T, returning allowed, allowed with permit, or not allowed, with the reason and legal source.
       - `options`: alternative windows, exempt car parks, quota use.
       - `changes`: a webhook feed of rule changes and upcoming switch-on and phase-out dates.
       - `label`: maps Euro class, fuel and registration date to the DGT label, with per-city equivalence tables for foreign vehicles.
    3. Historical versions, for fine disputes ("which rule applied on date D?").
  - *MVP:* 6–8 weeks of build plus continuous curation. It covers the 10 sanctioning or access-control cities, NAP ingestion, the `check` endpoint and the change webhook.
  - *Deliberately not:* map tiles, general routing or pathfinding (partners do that), legal advice or permit filing.
- **Why now:**
  - Courts reshaped the largest schemes in 2026 (ZBE-02).
  - NAP files are stamped 8 Jul 2026, or 31 Jul 2026 for Valencia, and contain contradictions (ZBE-03).
  - The datos.gob.es request for a national table has gone unanswered since Nov 2025 (ZBE-19).
  - Label-B phase-outs arrive in Palma and Catalonia in 2027–2028 (ZBE-14).
  - Nascent developer tools show demand and a short window: @cargoffer/zbe-mcp was first seen in Jul 2026, and there is an Apify LEZ actor (ZBE-20).
- **Alternatives today:**
  - **Official and free:** DGT NAP DATEX II (CC BY 4.0, thin and stale) and city perimeter files.
  - **Commercial:** HERE Environmental Zones and routing (Euro class; "19 countries"; price unknown); TomTom LEZ (376 cities globally; Spanish coverage unverified; price unknown); urbanaccessregulations.eu (268 LEZs; price unknown); Green-Zones (stale).
  - **Developer tools:** @cargoffer/zbe-mcp (compares Euro class only; no price or licence) and the Apify "EU LEZ Route & Vehicle Checker" (not inspected).
  - **Human-readable guides:** ecomovilidad and RACE (ZBE-01, ZBE-20).
  - *Weakness:* none encodes Spanish legal semantics with legal-status versioning.
- **Price hypothesis:**
  - A free developer tier of 100 checks a day.
  - €149/month for 10,000 checks and €499/month for 100,000, plus an enterprise data licence.
  - For renting firms, €0.20–0.50 per vehicle per month.
- **Channels:**
  - Spanish route-planning, TMS and telematics vendors, through partner integrations; renting, leasing and van-rental firms; fleet insurers.
  - UNO (350+ members) and a data partnership with Fenadismer and Astac, whose national ZBE site already reaches hauliers.
  - Developer marketplaces: MCP directories and Apify.
  - A Valencia Sandbox (AE.IN.100) pilot with the port.
  - Optionally, municipalities that need help publishing to the DGT (ZBE-21).
- **Build notes:**
  - CC BY 4.0 attribution.
  - Ordinance parsing with AI plus human legal review; tracking legal status through court rulings; geocoding.
  - Programmatic DGT label lookup is unverified.
  - Service-level agreements and liability disclaimers.
  - Data sensitivity is low unless plates are processed.
  - Complexity: medium for code, high for ongoing curation.
- **Moat in an AI-flooded market:** Medium. The moat is the curated, versioned legal-status history, the monitoring routine, and integrations inside partners' products. AI lowers the cost of a first scrape but not of staying current and standing behind the answers. The real threats are HERE, TomTom or a Spanish telematics leader adding Spanish semantics, or the DGT enriching the NAP model.
- **Key risks and kill criteria:**
  - *Risks:* few paying integrators; the DGT upgrades its data model; liability for wrong answers, each potentially a €200 fine; enforcement softening; buyers preferring the HERE bundle.
  - *Kill if* fewer than 5 of 20 contacted fleet-software vendors would pay at least €149/month, or if HERE or TomTom confirm DGT-label, domicile and quota semantics for Spain.
- **Evidence strength:** Medium. The data gaps and rule complexity are strongly evidenced by direct inspection of the NAP and city portals. Demand from integrators is inferred from nascent tools.
- **Validation questions:**
  1. Which Spanish LEZs do HERE and TomTom cover, at what price, and do they encode DGT labels, domicile and quotas?
  2. Which Spanish fleet or route software (name 5–10, including Google Routes API, PTV, Sygic Truck and Webfleet) supports ZBEs, and how?
  3. Who is behind @cargoffer/zbe-mcp and the Apify "EU LEZ Route & Vehicle Checker", and what are their pricing and traction?
  4. Does the DGT plan to extend the DGT 3.0 or NAP data model (vehicle category, domicile, quotas)?
  5. Valencia Sandbox: what are its final approval and BOP dates, how many projects has it admitted, is a data-API pilot eligible, and what are the port alliance's terms?
  6. What liability does a compliance answer carry, and is professional-liability insurance needed?
  7. How many ZBE fines a year do renting and leasing firms reassign, and what does reassignment cost them?
  8. On what terms can DGT labels be looked up?

---

## 7. Cross-group links

**Finance, payment and invoicing**
- **Late payment in haulage and the food chain** (IND-04; 186 payment-term breaches in IND-18) ↔ finance FIN-01, FIN-03 (statutory interest and €40 compensation go unclaimed), FIN-25 and TAX-06 (e-invoicing payment-status reporting could feed payment dates automatically). *Merge:* one interest and claims engine, with G5-I02 as the transport vertical.
- **Disaster paperwork** (CITY-01, CITY-02; G5-I08) ↔ FIN-19, FIN-20, FIN-21, FIN-22 (uncompensated blackout losses). *Merge:* G5-I08 is likely to fold into the finance track's claims idea.
- **DeCA, RCA and fuel-line documents as a document of record** (IND-01, IND-02, IND-18) ↔ TAX-05 (B2B e-invoicing). Check whether the e-invoice could carry the fuel line and the payment dates.
- **Island freight surcharges** (CITY-07) ↔ RET-14 (shipping to the Canaries, Ceuta and Melilla) and TAX-25 (IGIC).

**Packaging, product and ESG compliance**
- **Packaging EPR and PPWR** (IND-12; G5-I07) ↔ retail RET-15, RET-16 (plastic-packaging tax) and RET-12. *Merge:* one packaging-compliance idea with two segments, manufacturers and food firms, and e-commerce sellers and retailers.
- **Food-waste law** (IND-25) ↔ hospitality HOS-08. *Merge:* a shared Ley 1/2025 plan and donation-log module.
- **Product master data for EUDR and CBAM** (IND-13, IND-14) ↔ LEG-20 (ESG and VSME data requests). The same supplier data could serve both.
- **EU customs duty of €3 per item line and product IDs from 1 Nov 2026** (IND-08 sub-pain, single source) ↔ retail and e-commerce (RET-06, RET-14).

**Bureaucracy, notifications and grants**
- **Digital certificates** for RCA uploads (IND-18) and permit filings (ZBE-06) ↔ ADM-07 (custody of company certificates).
- **ZBE fines arriving by electronic address** (ZBE-10) ↔ ADM-08 and TAX-18 (electronic-notification traps).
- **Domicile-based ZBE rules** annulled in Málaga, reportedly as discriminatory or contrary to market unity (ZBE-04; cities notes) ↔ ADM-04 (market-unity cases).
- **MOVES III van-renewal aid** (ZBE-05), Zaragoza's SME aid (CITY-09) and the RDL 7/9/25/2026 aid (IND-02, IND-21) ↔ ADM-15 (MOVES III grant justification), ADM-16 (grant discovery) and ADM-14.
- **Regulatory whiplash** (CITY-15, ZBE-02) ↔ ADM-05, LAB-25, TAX-02, HOU-02 and EXP-06. *Merge:* the ZBE legal-monitoring routine in G5-I09 is one instance of a cross-group "regulatory radar"; check whether a shared alerting engine makes sense.
- **Bureaucracy hours** (CITY-19) ↔ TAX-09 and ADM-05.

**Labour and HR**
- **Driver shortage and foreign recruitment** (IND-03) ↔ LAB-08, ADM-10, EXP-13 (driving-licence exchange) and EXP-18 (consular visas).
- **Trade and sector labour shortages** (IND-11, CITY-16, CITY-05) ↔ LAB-07, CON-01, HOS-01 and HOS-26.
- **Seasonality** (CITY-06) ↔ LAB-14 and HOS-26.
- **Absenteeism** (CITY-20) ↔ LAB-05.
- **Credit** (CITY-17) ↔ FIN-10 and FIN-11.

**Costs, digital adoption and channels**
- **Energy shock** (IND-10, CITY-14) ↔ HOS-04 (margin squeeze) and VOX-06 (energy mis-selling).
- **Micro-firm digital gap and ERP laggards** (CITY-22, CITY-23, IND-16) ↔ RET-07, VOX-15, VOX-16 and TAX-07 (lock-in).
- **Municipal waste fee** (CITY-13) ↔ HOS-11.
- **Channels and costs:**
  - WhatsApp alerts in G5-I03 ↔ RET-10 (WhatsApp is now billed per message).
  - Gestoría-led distribution for G5-I01 to I07 ↔ VOX-21 (the gestor decides the software) and TAX-22.
- **Valencia Sandbox** (Ley 28/2022 art. 16, startups law) ↔ the startups track, for sandbox and pilot channels.

---

## 8. Group top 5

Listed in idea-number order. This is a shortlist, not a ranking.

- **G5-I01 DeCA evidence vault.** A live mandate since 5 Oct 2026 with roadside fines and documented rollout failures, a €5 price anchor and fast build. The moat is weak, so it is a speed play best paired with I02.
- **G5-I02 Haulier revenue recovery.** It recovers money the law already grants: the fuel line (G index +44.6%), detention pay and late interest. 152,871 target firms, associations already campaigning, and shipper-behaviour data that can become a moat.
- **G5-I05 RCA autopilot.** The group's best official enforcement data: 506 registration failures among 991 sanctions, 62% of them in wine. An existing API, a clear harvest trigger and association channels.
- **G5-I07 Packaging EPR and PPWR assistant.** Official, recurring obligations (an annual declaration before 31 March; PPWR since 12 Aug 2026) for more than 27,300 food and drink firms. Merging with retail's RET-15 enlarges the market.
- **G5-I09 ZBE rules and in-zone compliance API (U3 reshaped).** The clearest data gap in the notes: a stale national feed with thin rule detail and no national status table. Curated legal versioning is the moat, and it powers I03 and I04.

*Runner-up:* **G5-I03 ZBE alerts.** Strong evidence of fragmentation, but owners keeping old vans until they exit may not pay.
