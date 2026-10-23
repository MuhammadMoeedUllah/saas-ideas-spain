# Validation batch 6: transport, low-emission zones (ZBE), packaging and the food chain

*Validator: batch 6. Prepared 23 October 2026. Ideas: IDEA-45, IDEA-46, IDEA-47, IDEA-48 (user idea U3, EcoRoute, full treatment), IDEA-49, IDEA-50, IDEA-51.*

*Method: [F] direct fetches of official, vendor and press pages (unlimited) first, then at most 24 web searches (log in section 4). Citations: [new: URL, date seen or published] for evidence gathered in this batch; [notes: PAIN-ID] for stage-1 evidence. "Single source" marks claims seen in one place only. Political context: Cortes dissolved 6 Oct 2026; general election 29 Nov 2026.*

*Status: complete for desk research, 23 Oct 2026. 22 of the 24 permitted searches were used. Every [I] check is still open and listed per idea.*

---

## 1. Batch summary table

Sellability is the mean of S1–S8. Overall = 0.6 × Sellability + 0.4 × P. Where the verdict is RESHAPE, the scores are for the reshaped version.

| ID | Name | Type | Verdict | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Sellability | P | Overall | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IDEA-45 | DeCA evidence vault for small hauliers | C | **KILL** as stand-alone (keep as a free "DeCA inbox" inside IDEA-46) | 5 | 4 | 3 | 3 | 2 | 5 | 1 | 4 | 3.38 | 3 | 3.23 | medium |
| IDEA-46 | Haulier revenue recovery (fuel line, late interest, detention) | B (C add-on) | **GO** (pilot; scope changes) | 4 | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 3.50 | 4 | 3.70 | medium |
| IDEA-47 | ZBE checker and fleet permit ledger, reshaped fleet-first | C → B | **RESHAPE** (fleet-first permit and dispatch ledger; autónomo tier free or €29–39/year) | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 3 | 3.13 | 3 | 3.08 | low |
| IDEA-48 | EcoRoute reshaped: ZBE rules and compliance API [U3] | B | **KILL** as stand-alone (the dataset becomes IDEA-47's engine) | 3 | 1 | 2 | 3 | 3 | 3 | 2 | 3 | 2.50 | 2 | 2.30 | medium |
| IDEA-49 | Packaging EPR, PPWR and plastic-tax kit | B | **KILL** | 4 | 3 | 2 | 2 | 2 | 4 | 2 | 4 | 2.88 | 3 | 2.93 | medium |
| IDEA-50 | RCA autopilot (food contracts before delivery) | B | **GO** (pilot; fruit, vegetables and citrus first, wine for the 2027 harvest) | 4 | 2 | 3 | 3 | 4 | 3 | 3 | 4 | 3.25 | 3 | 3.15 | medium |
| IDEA-51 | Fertilisation-plan workspace, reshaped to a cooperative channel with the art. 20 route | B | **RESHAPE** | 4 | 2 | 2 | 3 | 3 | 3 | 2 | 4 | 2.88 | 3 | 2.93 | low |

**Reading the table.**
- **IDEA-45's Overall (3.23) is above IDEA-50 (a GO) and both RESHAPE ideas, yet it is killed.** The formula rewards its urgent duty and large buyer count, but near-free incumbents (DecaFirma, Cargoffer) already include the evidence features (S5 = 2, S7 = 1), so it cannot be sold on its own.
- **The user's idea (U3, IDEA-48) does not survive as an API business.** Its curated legal-status dataset survives as the engine of IDEA-47. The claim-by-claim verdict is at the end of the IDEA-48 section.

---

## 2. Ideas

#### IDEA-48: EcoRoute reshaped: Spanish ZBE rules and in-zone compliance-check API [user idea U3] — KILL as a stand-alone product; the rules dataset folds into IDEA-47 (medium)

**Validated definition.**
- **What was tested:** a paid API sold to route-planning, TMS, telematics and renting firms at €149–499 a month. It would offer:
  - a curated, versioned dataset of Spanish ZBE rules. Perimeters come from the DGT NAP and city portals. Rule detail, legal status (in force, annulled but not final, suspended, information phase) and effective dates are curated from ordinances, bulletins and rulings;
  - a `check` endpoint: may vehicle X serve stop Y at time T, and with which permit?
- **What the evidence supports:** the dataset is real work and is missing from the free official sources.
- **What it does not support:** a business that sells it.
  - The paying pool is a few dozen software vendors.
  - No buyer was found paying for Spanish ZBE data.
  - Two suppliers already exist. Cargoffer, a Spanish TMS, ships its own ZBE API with DGT labels and SDKs. Sadler Consultants licenses pan-European access-regulation (UVAR) data with APIs and lists about 115 Spanish schemes.
- **Recommendation:** build the dataset only as the engine of IDEA-47 (reshaped below), and sell data licences or curation opportunistically to the few vendors that ask.

**(a) Problem reality and rule status, October 2026 (batch 6 owns C-01 and C-13)**

The legal base is unchanged and unaffected by the election: Ley 7/2021 art. 14 and RD 1052/2022 oblige about 150 municipalities, and each ordinance is municipal [notes: ZBE-01]. The real risk is local politics softening enforcement, not lapse.

- **C-01 Valencia: settled. No ZBE is in force, and the ZBE track was right.**
  - **Initial approval only.** The Pleno approved the ordinance initially on 25 Feb 2025 [new: https://www.valencia.es/cas/actualidad/-/content/zona-bajas-emisiones-val%C3%A8ncia.-aprobaci%C3%B3n-por-el-pleno, published 25 Feb 2025, seen 23 Oct 2026].
  - **What the cities track cited.** Its valencia.es item of 21 Oct 2025 reports only an approval by the Comisión de Patrimonio. That item says the ordinance "deberá pasar por el Pleno… el próximo 28 de octubre" and "únicamente podrá empezar a funcionar si recibe el respaldo del Ayuntamiento Pleno" [new: https://www.valencia.es/cas/actualidad/-/content/val%C3%A8ncia-aprueba-la-ordenanza-de-zona-de-bajas-emisiones, published 21 Oct 2025, seen 23 Oct 2026].
  - **Final approval rejected.** The Pleno rejected final approval on 28 Oct 2025 by 19 votes (Compromís, PSPV, Vox) to 13 (PP). No Pleno has voted on it again, and a new text has no date (ecomovilidad, "Actualizado en octubre de 2026") [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/, seen 23 Oct 2026].
  - **No new ordinance planned.** On 1 Dec 2025 the Pleno rejected an opposition motion, and the mobility councillor said "ya no hay tiempo de articular una nueva ordenanza de zona de bajas emisiones" [new: https://www.valencia.es/cas/actualidad/-/content/pleno-val%C3%A8ncia.-zona-bajas-emisiones.-tasa-de-basuras.-precio-vivienda., published 1 Dec 2025].
  - **No later vote.** A search for any vote after September 2026 found nothing (search 1).
  - **Vox's condition.** Vox will only approve a "ZBE sin régimen sancionador" (a ZBE without a sanctions regime). €14M of 2026 transport aid plus €4M from 2025 depend on approval during 2026 [new: El Español, https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html, published 7 Mar 2026].
  - **Even the failed draft barely touched business vans.** It exempted label-A vehicles "vinculados a cualquier actividad económica de autónomos o empresas" (valencia.es, 21 Oct 2025 above).
- **The DGT NAP record for Valencia is wrong.** Valencia.xml was republished on 30 Jul 2026 with status `active` from 1 Jun 2026. It restricts unlabelled turismos, motorcycles and mopeds only, and has no field for vehicle category, MMA, domicile, quotas or episodes [new: https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/Valencia.xml, parsed 23 Oct 2026].
- **Málaga (C-13): annulled; fines stopped; finality expected 25 Nov 2026.**
  - TSJA sentencia 896/2026 of 6 May 2026 (ROJ STSJ AND 7366/2026) annulled arts. 9–24 of the mobility ordinance.
  - The city announced on 13 Oct 2026 that it would not appeal, and stopped fining on 14 Oct. Gestrisam suspended the files on 19 Oct.
  - The ruling was not yet published in the BOP on 17 Oct, and finality is expected on 25 Nov 2026.
  - Source: [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/, updated 22 Oct 2026].
  - **Fines and refunds:** 46,562 fines were issued. €1.38M from 13,694 paid fines will be refunded ex officio from the end of November, possibly over up to four years. 32,868 are suspended. The label-B step of 30 Nov 2026 is on hold, and the city is redrafting, with EU mobility aid at stake [new: https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero, published 22 Oct 2026].
  - **Legal reasoning conflict, resolved.** Both sources now say the defect was sanctioning only vehicles not fiscally domiciled in Málaga (Motorpasión: discriminatory, after a clarification at the end of September; ecomovilidad: the court rejected the "domiciliación fiscal del vehículo" criterion). The court dismissed the challenge to the environmental justification. The notes' reading that the domicile challenge was rejected was a misreading.
- **Madrid (C-13).**
  - **The annulment.** TSJM ruling 405/2024 of 17 Sep 2024 partly annulled the 2021 ordinance. This settles the notes' "Sept, Oct or Dec 2024" gap. The Supreme Court inadmission of 15 Apr 2026 (casación 8840/2024) made it final without a ruling on the merits.
  - **The replacement.** Ordenanza 2/2026 (24 Mar 2026) has applied since 7 Apr 2026 [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/comunidad-de-madrid/madrid/, updated Oct 2026].
  - **Vans and trucks.** Unlabelled non-turismos (vans, trucks, motorcycles) may circulate outside the special zones "con independencia del municipio en que esté domiciliado" while NO2 limits hold at every station, but never on episode days. A single breach ends the regime, with fines six months after BOCM publication. Detection is by OCR cameras and "foto rojo" devices, at €200 (€100 if paid early) [new: madrid.es FAQ, https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD, content dated 7 Apr 2026].
  - **Old fines.** The TSJM enforcement proceeding (AEA: 3.4M files, €663M to end-2025) is still pending, and the city says refunds are not due [new: https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html, published 15 Jul 2026].
  - **Notes conflict 7 (van rules): settled for the ZBE track.**
- **Valladolid (C-13): annulled but not final, and still fining.**
  - TSJCyL 281/2026 (16 Mar 2026) annulled the ordinance for lack of the prior project RD 1052/2022 requires.
  - The ruling is not final, and the city confirmed on 18 Sep 2026 that it keeps fining.
  - The Junta de Gobierno started a mobility-plan change on 28 Jul 2026, but there is no new ordinance yet [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/, updated Oct 2026].
- **Zaragoza (C-13): both notes were partly right.**
  - The Casco Histórico zone has fined unlabelled vehicles Mon–Fri 8–20h since 12 Dec 2025, at €200 (€100), with 8 accesses a month for registered vehicles.
  - Zone 2 (Centro) starts only on 1 Jan 2030. That is the source of "not operational until 2030".
  - A proposal to fine only during pollution episodes is tied to the 2027 budget deal with Vox and is "no aprobada" [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/, updated Oct 2026; "a 8 de octubre de 2026 la ordenanza sigue sin cambios"].
- **Vigo (C-13): label B is restricted from 2029.**
  - The ordinance has been in force since 9 Sep 2026 and is information-only to 10 Sep 2027, when unlabelled vehicles are barred.
  - Label B gets warnings from 10 Sep 2028 and restrictions "a partir del año 2029". Label C gets warnings from September 2031, and only ECO and Cero may enter from 10 Sep 2032.
  - Motor16's "2027" is the unlabelled step [new: Atlántico, https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html, published 10 Sep 2026].
- **Catalonia's label-B rule (C-13): binding, but not yet transposed in Barcelona.**
  - Decree 132/2024 bans diesel B during NO2 episodes from 1 Jan 2026 and bans label B permanently in ZBEs of municipalities over 50,000 from 1 Jan 2028. Reus has already scheduled its 2028 B phase (search 21).
  - Barcelona must amend annex 2 of its ordinance, and "a octubre de 2026 no consta que se haya iniciado ese trámite" (as of October 2026 there is no record that the procedure has started) [new: https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/, updated Oct 2026].
  - So "a plan, not yet law" is wrong for the decree, but right that no Barcelona ordinance text yet implements it.
- **Barcelona suspension (C-13): started on 22 Jan 2026.** The suspension ran from 22 Jan to 13 Mar 2026, and service resumed on Monday 16 Mar 2026 [new: ecomovilidad Barcelona, above; https://www.zbe.barcelona/, seen 23 Oct 2026]. The 28 Jan date is the DOGC publication of Resolució TER/194/2026 [notes: CITY-04]. The TSJC rulings of 24 Nov 2025 upholding the 2023 ordinance could be appealed in cassation; the outcome is not shown.
- **The official data is still stale.**
  - The NAP directory still holds 46 XML files, all stamped 8 Jul 2026 except Valencia (31 Jul 2026). There is still nothing for Zaragoza, Vigo, Córdoba, Murcia or Las Palmas, and Málaga is not updated after 14 Oct [new: https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/, listing seen 23 Oct 2026].
  - The datos.gob.es request for a national table is still "Asignado" to the Ministerio de Transportes with 6 followers and no response (page updated 19 Oct 2026) [new: https://datos.gob.es/es/solicitud-de-datos/zonas-de-bajas-emisiones, seen 23 Oct 2026].
  - The trade body UNO still lists Bilbao, Valencia and Zaragoza as "Pendiente Borrador ZBE" [new: https://unologistica.org/proyectos-e-informes/ordenanzas-de-movilidad/, seen 23 Oct 2026].
- **Enforcement trend.** Valencia (none), Málaga (stopped), Alicante (notices only), Vigo (information phase) and Zaragoza's episode-only proposal all point to softer enforcement at the margins. Madrid, Barcelona/AMB, Bilbao, Palma, Granada, Sevilla-Cartuja, Valladolid, Córdoba and A Coruña still sanction [notes: ZBE city table; sources above].

**(b) Competitors**

| Product | What it does for Spain | Price | Segment | Weakness found |
|---|---|---|---|---|
| **Cargoffer ZBE API** (Spanish TMS and freight marketplace, Galicia; "+5.000 profesionales") [new: https://zbe.cargoffer.com/, https://cargoffer.com/, seen 23 Oct 2026] | `POST /api/zbe/check-route` returns the zones a route crosses and a `compliant` flag, from the DGT label (0, ECO, B, C) or Euro class. Also an MCP server (`@cargoffer/zbe-mcp`, v0.1.0 first observed 11 Jul 2026) and TypeScript and Python SDKs [new: https://glama.ai/mcp/servers/c43h6rrgcn, seen 23 Oct 2026] | Not published: an API key is needed and the docs return 401 | Developers, AI agents, TMS users | No MMA, domicile, permits, time windows or legal status. It claims coverage of "Valencia… Málaga, Zaragoza", although Valencia has no ZBE, and says it helps "evita multas de hasta 2.000€" when the fine is €200. Glama marks the MCP "Inactive". **Shows that a Spanish TMS builds rather than buys.** |
| **Sadler Consultants Europe GmbH / urbanaccessregulations.eu** [new: https://urbanaccessregulations.eu/stakeholders/uvar-data-available, HTML parsed 23 Oct 2026] | About 115 Spanish entries (LEZ, LTZ, emergency schemes, superblocks…) in its country menu. It sells a "licence fee for using the data… by or on behalf of commercial organisations", an online dashboard with "machine-readable data", and "APIs for the Dashboard, map and city data" | By quote ("free of charge for private use") | Map and navigation firms, OEMs, fleet software, cities | The Spanish city pages did not render in a static fetch, so the depth of DGT-label, domicile and quota semantics is **unverified**. It is the incumbent European curator. |
| **HERE Routing, environmental zones** [new: https://docs.here.com/routing/docs/truck-restrictions-env-zones, seen 23 Oct 2026] | `excludeZoneType=environmental`, with `emissionType` (Euro I–VI), `fuelType`, `limitedWeight` and `departure` | Not published | Enterprise and developers | No DGT-label, domicile, permit or quota parameter. Spanish coverage is not stated. |
| **TomTom Routing API** [new: https://docs.tomtom.com/routing-api/documentation/tomtom-maps/product-information/release-notes; https://docs.tomtom.com/pricing, seen 23 Oct 2026] | `avoid=lowEmissionZones` and `sectionType=lowEmissionZone` (Jan 2023) | 20K free requests a month per API, then usage-based (rates not shown) | Developers | No mention of Spain or national stickers |
| **PTV Developer Routing** [new: https://developer.myptv.com/en/documentation/routing-api/concepts/low-emission-zones, seen 23 Oct 2026] | Considers LEZs automatically, with `lowEmissionZoneApprovals` (for example DE_GREEN) and `lowEmissionZoneExemptions` | Pricing page 404 | Logistics software | Spanish badges not documented. It does model exemptions, the closest to Spanish permit semantics. |
| **Apify "EU LEZ Route & Vehicle Checker"** (ScholarStack) [new: https://apify.com/scholarstack/eu-lez-intelligence, seen 23 Oct 2026] | 94 zones in 12 countries, 3 of them Spanish; Euro class, fuel and registration country | $0.05 per check | Developers | **2 total users, 0 monthly users**: a traction signal for this kind of tool |
| **Google Maps** [new: https://www.motor.es/practicos/z-google-maps-2025106412.html, published 30 Jan 2025; https://androidguias.com/como-funcionan-las-zbe-en-google-maps/, updated 11 May 2025] | A "Z" icon and voice warnings when a route crosses a ZBE (Madrid and Barcelona fully, elsewhere partially) | Free | Everyone | No label-based avoidance. Third-party guides only. |
| **Official free sources** | NAP DATEX II (CC BY 4.0), city perimeter files, DGT single-plate label lookup | Free | Everyone | Stale and thin (see (a)) |

**Gap.** No product found encodes Spanish legal-status versioning together with MMA windows, domicile, permits and quotas. The gap is narrower than the longlist implied, though: a Spanish TMS already sells a basic ZBE API, and a European curator already licenses Spanish scheme data. The kill criterion on HERE and TomTom is not triggered (see (h)).

**(c) Buyers and market size**
- **Vendor pool.** One commercial directory lists 34 GPS and fleet-software companies based in Spain (refreshed 3 Sep 2026; partial, sign-up wall) [new: https://revenuebase.ai/companies/gps-software-companies/spain]. Add route planners and TMS (Routal, Cargoffer and others) and international telematics firms with Spanish operations, and the plausible pool is about 50–150 software vendors (my estimate). Renting, leasing and insurer counts were not verified.
- **Telematics reach.** Telematics is widespread: 74% of Spanish fleets use GPS tracking (77% of small fleets), so a vendor channel would reach many fleets [new: Geotab/ABI Research, https://www.geotab.com/CMS-GeneralFiles-production/EMEA/connected-fleets/local-2026/Geotab-Connected-Fleets-Report-2026-Local-ES-ES.pdf, 2026 report; vendor survey].
- **ZBEs are not top of mind.** The same 45-page Spanish fleet report never mentions ZBEs; its only "bajas emisiones" hit is about EV logistics. That is weak disconfirming evidence.
- **Revenue ceiling (my arithmetic).** If 20–30 vendors paid €149–499 a month and a handful bought enterprise licences, Spanish revenue would be about €0.1–0.3M a year. Renting firms at €0.20–0.50 per vehicle would add little without large contracts.

**(d) Willingness to pay**
- **Price anchors:**
  - TomTom gives 20K requests a month free.
  - The Apify checker charges $0.05 per check and has 2 users.
  - Routal route planning costs €199 a month for 4 vehicles plus €49 per extra vehicle [new: https://www.routal.com/es/precios, seen 23 Oct 2026], so a ZBE data add-on of €0.20–0.50 per vehicle would be under 1% of the planner's price.
  - Cargoffer's TMS is €0 (up to 5 vehicles), €99 (up to 50) or €299 a month [new: https://cargoffer.com/pricing, seen 23 Oct 2026].
- **Fine handling at lessors is a cost centre that is already outsourced.** A processor (Gesthispania) handles driver identification for Arval, Sixt, Europcar and Hertz. Consumo fined Avis €1M for charging customers fine-management fees, and AEA reports such fees above €60 per file (search 15; single-source snippets, not opened).
- **No buyer was found paying for Spanish ZBE data.** The only Spanish vendor in the space built its own.

**(e) Distribution**
- **Direct sales to software vendors.** This is the only proven-shape channel, and it is unproven here.
- **Developer marketplaces.** MCP directories and Apify show near-zero traction for this category (2 Apify users; the Cargoffer MCP is "Inactive").
- **Associations.** UNO and Fenadismer/Astac are potential data partners, but their own data is stale (UNO) or a 2024 site that was unreachable (503) [new: https://www.fenadismer.es/los-transportistas-ya-pueden-consultar-todas-las-zonas-de-bajas-emisiones-en-una-sola-web/, published 7 Jul 2024].
- **The Valencia Sandbox: a pilot venue, not a channel.**
  - **Status.** The ordinance was approved provisionally and unanimously on 30 Apr 2024 [new: https://www.valencia.es/cas/actualidad/-/content/ple-ordenanza-sandbox, published 30 Apr 2024]; no BOP publication was found.
  - **How it works.** Procedure AE.IN.100 is "abierto de forma permanente", decides in at most 3 months with negative silence, and lists no fee [new: https://sede.valencia.es/sede/registro/procedimiento/AE.IN.100?lang=1, seen 23 Oct 2026].
  - **Track record.** In two years it received 75 requests, authorised 98%, and ran 48 pilots (9 finished) with 48 entities. Energy and mobility were 14.3% of projects, and the average response took 90 days. No ZBE, logistics or port project is named [new: https://valencianews.es/valencia/sandbox-urbano-de-valencia-cumple-dos-anos-con-casi-50-proyectos-desarrollados/, published 24 Sep 2026; single source].
  - **The port alliance.** It was announced in late June 2026 to "incorporar toda la actividad logística del puerto al Sandbox Urbano", with no terms published [new: https://www.parentesis.media/valencia-madrid-y-barcelona-convierten-la-ia-en-un-laboratorio-urbano-bajo-control-juridico/, published 28 Jun 2026].
  - **Limits.** It cannot waive non-municipal (DGT or state) rules (art. 11.3) [notes: ZBE fact-check claim 2], and Valencia has no ZBE to test against.

**(f) Build feasibility and legal constraints**
- **Geometry and base rules.** The NAP DATEX II files and city perimeters are CC BY 4.0 and need attribution [notes: ZBE-03]. The rule detail needs ordinance parsing plus human legal review for the 10 sanctioning cities: 6–8 weeks of build, then continuous curation.
- **No private bulk label lookup.**
  - The DGT's daily file of every plate with its label and the locality of its fiscal domicile is free, but **restricted to ayuntamientos and local entities with a ZBE registered through DGT 3.0**, with named users authorised in the REA [new: https://sede.dgt.gob.es/es/vehiculos/tramites-para-administraciones/descarga-de-fichero-zbe-zona-de-bajas-emisiones/, seen 23 Oct 2026].
  - Private firms get only the single-plate web lookup, with "sin identificación previa" and no API [new: https://sede.dgt.gob.es/es/vehiculos/informacion-de-vehiculos/distintivo-ambiental/, seen 23 Oct 2026]. That page also mentions a "fichero de distintivos ambientales" in DGT en Cifras, which could not be located (conflict noted in section 3).
  - So the `label` endpoint must infer the label from fuel, Euro class and registration date, or trust the customer's declaration. Mass scraping of the plate form would be a terms and legal risk.
- **Liability.** A wrong "allowed" answer can cost the end user €200 per entry [notes: ZBE-10]. Contracts need liability caps and an SLA. The cost of professional-liability insurance was not checked (an [S\*] left unrun).
- **Data sensitivity.** Low, unless plates are processed (GDPR).

**(g) Defensibility**
- **The only distinctive asset** is the legal-status history: annulled but not final (Valladolid), stopped before finality (Málaga), NO2-conditional (Madrid), episode-only proposals (Zaragoza).
- **The evidence cuts against it as a moat.**
  - A Spanish TMS built a ZBE API on its own.
  - A European curator already sells Spanish scheme data with APIs.
  - AI makes a first scrape of ordinances cheap.
- **Integrations inside partners' products** would add switching costs only once won, and none is evidenced.

**(h) Kill criteria**
- **"Fewer than 5 of 20 fleet-software vendors would pay ≥€149/month": open [I].** Every desk proxy points negative: Cargoffer built its own, the Apify actor has 2 users, the Glama listing is inactive, and Geotab's Spanish fleet report is silent on ZBEs.
- **"HERE or TomTom confirm DGT-label, domicile and quota semantics for Spain": not met.** HERE's documentation is Euro-class only; TomTom and PTV document no Spanish stickers (search 2 found nothing). Partial erosion: Cargoffer already accepts DGT labels, though not domicile or quotas.
- **"The DGT enriches the NAP model": not met.** The files have not been updated since July 2026, the DGT 3.0 model is unchanged, and the data request is unanswered.

**Scores (stand-alone API)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | End users face enforced €200 fines and dated switch-ons (Palma 1 Jan 2027, Vigo 10 Sep 2027, Catalonia 2028), but the API buyer has no deadline of its own |
| S2 Buyers in Spain | 1 | About 50–150 software vendors plus renting firms and insurers: well under 5k paying entities |
| S3 Willingness to pay | 2 | No buyer found paying for Spanish ZBE data; the anchors are free tiers and $0.05 checks; a Spanish TMS built its own |
| S4 Reachability | 3 | The buyers are few and identifiable for direct sales, but no partner programme or marketplace traction is evidenced |
| S5 Competitive gap | 3 | Cargoffer's API, Sadler's licensed data and HERE/TomTom/PTV avoidance exist but are thin or unlocalised on legal status and permits |
| S6 Build speed | 3 | 6–8 weeks of code plus continuous legal curation of 10 cities; no bulk label source |
| S7 Defensibility | 2 | The versioned legal-status history is the only asset, and both a Spanish TMS and a European curator compete for it |
| S8 Retention | 3 | Once integrated, use is continuous, but there is no legal obligation or record lock-in for the buyer |
| **Sellability** | **2.50** | |
| P (severity for the paying buyer) | 2 | For vendors it is a feature gap; end-user severity is scored in IDEA-47 |
| **Overall** | **2.30** | 0.6 × 2.50 + 0.4 × 2 |

**Open [I] checks**
- Contact 20 fleet-software vendors (Spanish telematics, route planners, TMS and the Spanish teams of Webfleet and Geotab) and test €149/month. Kill if fewer than 5 would pay.
- Ask Cargoffer whether it would buy or license curated legal-status data instead of maintaining its own.
- Ask Sadler Consultants whether it subcontracts country curation, and at what rate.
- Ask 5 renting or leasing firms (AER members) how many ZBE fines they reassign a year and what it costs.
- Ask the Valencia Sandbox and the port authority whether a port-logistics data pilot is eligible, and what the alliance's terms are.

**What would change the verdict**
- **Back to RESHAPE or GO** if at least 5 of 20 vendors commit at €149/month or more; or if Sadler, Cargoffer or a map vendor contracts the Spanish curation (a data-supplier business, still small); or if the DGT opens bulk label and domicile data to private firms, enabling an authoritative `check`.
- **Firmer KILL** if Sadler's Spanish pages already carry domicile, MMA and quota detail with legal status, or if HERE or TomTom add DGT labels.

**The user's original EcoRoute claims and features** (`00_user_supplied_ideas.md:32`)

| Original claim or feature | Verdict | Evidence |
|---|---|---|
| ZBEs are "strict" and "enforced by automated camera tracking" | **Partly survives**, only as "the roughly 10 ZBEs that fine use plate cameras" | Survives for Madrid (OCR and "foto rojo") [new: madrid.es FAQ], Barcelona/AMB, Bilbao, Zaragoza, Sevilla-Cartuja, Palma and Granada; Valladolid still fines while annulled; A Coruña uses access control [notes: ZBE fact-check]. False as a generalisation: Valencia's cameras only count traffic and it has no ZBE; Málaga stopped on 14 Oct 2026; Vigo is information-only to 10 Sep 2027; Alicante sends notices; 17 of 23 large Catalan municipalities did not fine effectively in 2025 [notes: ZBE-21; new: sources in (a)] |
| Connect to public open-data feeds in Barcelona and Valencia | **Does not survive** as a rules source | Both publish perimeters only. Barcelona has one 2023 GPKG for the city alone; Valencia's GeoJSON/WFS describes an ordinance that was never finally approved [notes: ZBE-03]. Rules exist only in the DGT NAP, whose Valencia record is wrong [new: Valencia.xml]. Free geometry also caps the price of anything geometry-based |
| Optimise daily delivery routes to avoid emission penalties | **Does not survive** | For stops inside a zone, compliance depends on which vehicle, which window, which permit or quota, or an exempt car park, not on the route [notes: ZBE-15]. Avoidance routing already exists, free or bundled, in HERE, TomTom, PTV and Google Maps' "Z" warnings [new: (b)] |
| Use Valencia's "Urban Sandbox" legal framework to test smart-mobility models | **Survives only as a pilot venue** | The ordinance is real and operating (provisional approval 30 Apr 2024; 75 requests, 48 pilots, 90-day average response) [new: valencia.es; valencianews], but it is cross-sector, cannot waive DGT or state rules (art. 11.3) [notes], and Valencia has no ZBE to test. The port alliance has no published terms |
| Target cities: Valencia, Madrid, Barcelona | **Madrid and Barcelona survive; Valencia does not** | Madrid has the largest fine volume (3.4M files, €663M, AEA) and van windows in Distrito Centro; Barcelona bans unlabelled vans on weekdays 7–20h. Valencia has no ZBE, Vox demands no sanctions, and even the failed draft exempted business vehicles [new: (a)]. Better third and fourth cities: Bilbao, and Palma (C, ECO and Cero only from 1 Jan 2027) [notes: ZBE-14] |
| Heavy burden on "commercial fleets and local e-commerce delivery partners" | **Partly survives** | Real for small operators keeping old vans and for in-zone deliveries [notes: ZBE-05, ZBE-15]. Large parcel carriers renewed early, and small operators do not buy APIs. Geotab's 2026 Spanish fleet survey does not mention ZBEs [new: Geotab report] |
| The product form: a "green routing API built on municipal open data" | **Does not survive** | Open data is too thin (above), routing is a commodity, and the paying API market is tiny (c–e). What survives is the curated, versioned rules dataset, as the engine of IDEA-47 |
| Regional claim: Valencia as "open civic data testing capital", with a ZBE logistics API as its best fit | **Contradicted for the API; partly supported as a sandbox venue** | Settles C-01 and the regional-claims row for Valencia |

---

#### IDEA-47: ZBE vehicle checker, alerts and fleet permit ledger — RESHAPE to a fleet-first ZBE permit and dispatch ledger (low)

**Validated definition (after reshape).**
- **Buyer:** operations or dispatch managers at SME distributors, HORECA suppliers, parcel subcontractors and multi-site service firms running 3–50 vans in the cities that sanction:
  - Madrid, Barcelona/AMB, Bilbao and Palma first;
  - then Sevilla-Cartuja, Granada, Zaragoza, Valladolid, Córdoba and A Coruña.
- **What it does:**
  - **Fleet register:** label, category, MMA, fiscal domicile and owned, rented or leased status.
  - **Rules engine:** per city, with legal status and effective dates. This is IDEA-48's dataset.
  - **Nightly check of tomorrow's stops:** from a CSV or API export of the route planner. It flags vehicle, stop and time conflicts and proposes fixes: swap the van, move the window, use a quota or an exempt car park.
  - **Permit and quota ledger:**
    - Madrid Distrito Centro per-plate registrations and the yearly night-delivery declaración;
    - AMB's 24 yearly authorisations;
    - Bilbao's 6 monthly invitations, which must be notified within 2 days;
    - Palma registrations.
  - **Change alerts and dated phase-outs:** Palma on 1 Jan 2027, Vigo on 10 Sep 2027, Catalonia in 2028.
- **Price:** about €49/month for up to 5 vans, plus €6–9 per extra van, sold through route-planner and TMS integrations and logistics associations.
- **Autónomo tier:** no longer a €4.99/month product. It becomes a free single-check and alert page (lead generation), or a €29–39/year plan bundled by van-rental firms, insurers or associations.

**(a) Problem reality and rule status**
- **City statuses:** as settled in IDEA-48 (a). Of the 16 profiled cities, nine sanction by label (Madrid, Barcelona/AMB, Sevilla-Cartuja, Zaragoza, Bilbao, Palma, Valladolid, Granada, Córdoba) and A Coruña by access control. Valencia, Málaga (from 14 Oct 2026), Murcia, Las Palmas, Alicante and Vigo (to 10 Sep 2027) do not [new: sources in IDEA-48 (a); notes: ZBE city table].
- **Dated changes within 12 months:**
  - Palma admits only C, ECO and Cero from 1 Jan 2027 [notes: ZBE-14, BOIB 167/2024].
  - Badalona's moratorium ends on 1 Jan 2027 [notes: ZBE-23].
  - Vigo bars unlabelled vehicles from 10 Sep 2027 [new: Atlántico, 10 Sep 2026].
  - Catalonia's label-B ban follows on 1 Jan 2028 [new: ecomovilidad Barcelona; search 21].
- **Madrid's van regime is conditional.** Unlabelled vans circulate only while NO2 limits hold, are banned on episode days, and lose the regime six months after any breach is published [new: madrid.es FAQ, content dated 7 Apr 2026].
- **In-zone mechanics are documented by the cities themselves** [notes: ZBE-06, ZBE-07, ZBE-16]:
  - Madrid Distrito Centro allows C vans 7–15h and ECO 7–21h, has banned light B vans since 2024, and requires per-plate registration and a yearly declaración responsable for night deliveries.
  - AMB allows 24 authorisations a year [new: ecomovilidad Barcelona] and Zaragoza 8 accesses a month [new: ecomovilidad Zaragoza].
- **Cost:** each wrong entry is €200 (€100 if paid early) [new: madrid.es FAQ]. Madrid issued 261,115 unlabelled-access fines in H1 2025 [notes: ZBE-10, single source citing AEA]. **No city publishes the share that goes to businesses or vans** [notes: ZBE-10].
- **Softening risk is real:** Valencia (none), Málaga (stopped), Alicante (notices), and Zaragoza's episode-only proposal (IDEA-48 (a)).

**(b) Competitors**

| Product | What it does | Price | Gap for fleets |
|---|---|---|---|
| ZBE España (iOS, Pablo Sánchez Bello) [new: https://apps.apple.com/es/app/id6738807819, seen 23 Oct 2026] | Map of ZBEs and a compatibility check by sticker category (Cero, ECO, C, B) for Madrid, Barcelona, Valencia, Sevilla and others; v1.3.0 | Free, no in-app purchases | No plate check, no alerts, no vans or permits. 3.0★ from **2 ratings**, a weak demand signal |
| Google Maps [new: motor.es, 30 Jan 2025; androidguias, 11 May 2025] | "Z" icon and voice warnings when a route crosses a ZBE | Free | Label-blind; no avoidance by label; no permits |
| Bip&Drive app [new: search 16 result summary; its page returned 503, so single source and not opened] | ZBE map with hours, labels, exceptions and sanctions; suggests alternative routes if the vehicle is affected | Not verified | Consumer-oriented; permits and quotas not described |
| Astac Condal and RACC national site [new: Fenadismer, 7 Jul 2024; astac.info returned 503 on 23 Oct 2026] | Per-city access, hours, exemptions and sanctions for hauliers | Not stated | Alerts not verified |
| ecomovilidad.es city guides [new: city pages "Actualizado en octubre de 2026"] | Detailed and current per-city status | Free | Human-readable only |
| Cargoffer ZBE API and free TMS (up to 5 vehicles) [new: https://zbe.cargoffer.com/; https://cargoffer.com/pricing] | Route-against-zone check with DGT label | Not published / €0 | No permits, quotas, windows or legal status |
| Route planners: Routal, HERE, TomTom, PTV [new: https://www.routal.com/es/precios; IDEA-48 (b)] | Planning and zone avoidance | Routal €49 per vehicle per month | No Spanish permit or window logic found (search 14) |

- **Kill criterion "ZBE España or the Astac/RACC site already sends vehicle-specific alerts": not met** for ZBE España, and unverifiable for Astac (site down).
- **No product was found that keeps a Spanish fleet permit and quota ledger or checks in-zone dispatch** (search 14) [notes: ZBE-15].

**(c) Buyers and market size**
- **Fleet tier.** The upper-bound pool is about 75,100 wholesale and 60,300 land-transport employer units [notes: G5-I04, notes' arithmetic from INE]. The subset with vans entering sanctioning ZBEs is unknown; I assume 10,000–30,000 firms.
- **Autónomo tier.** There are 2.74M vans, 1.08M of them aged 20+ [notes: ZBE-05], and about 184,800 land-transport and 286,800 specialised-construction autónomos [notes: G5-I03 arithmetic]. Many are "comply-until-exit" owners [notes: ZBE-05].
- **Revenue ceiling (my arithmetic).** 2% of 10–30k fleets is 200–600 fleets; at €600–1,200 a year each, that is about €0.12–0.72M ARR. An autónomo plan at €39/year would need 10,000 payers to add €0.39M.

**(d) Willingness to pay**
- No direct evidence. Free tools cover awareness, and the users are price-sensitive and often exiting.
- **Anchors:** Routal charges €49 per vehicle per month for planning, so a €6–9 ZBE add-on would be 12–18% of that; Cargoffer's TMS is free up to 5 vehicles; each avoided fine is worth €200.
- **Type C check (€4.99/month autónomo tier): not viable.**
  - Visible value is sporadic: a few rule changes a year.
  - Free substitutes exist (Google Maps, ZBE España, ecomovilidad).
  - Permit questions generate support load.
  - Owners keeping vans until they exit churn.
  - It needs an annual price (€29–39) and a bundling partner, or should stay free as lead generation.

**(e) Distribution**
- **Integrations:** route-planner and TMS integrations (Routal, Cargoffer and others), since 74% of Spanish fleets use GPS tracking [new: Geotab 2026 report].
- **Bundles:** van-rental, renting and insurer bundles.
- **Associations:** UNO (350+ members) [notes: IND-08] and Fenadismer/Astac.
- **Search:** "ZBE reparto Distrito Centro", "invitaciones ZBE Bilbao empresas" (search volumes not measured).
- **App stores:** ZBE España's 2 ratings suggest weak organic demand.

**(f) Build feasibility and legal constraints**
- **No public APIs for permits.** AMB registrations go through a login portal (zberegistre.ambmobilitat.cat) [new: https://www.zbe.barcelona/, seen 23 Oct 2026]. Bilbao handles invitations through web sections for local businesses [new: https://www.bilbao.eus/cs/Satellite?cid=1279231359138&language=es&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal, seen 23 Oct 2026]. Madrid uses Mi Carpeta or appointments [notes: ZBE-06]. So filing stays manual, or needs representation (apoderamiento) checks.
- **Labels:** the DGT bulk label file is municipal-only [new: DGT sede], so users declare labels or the app infers them from vehicle data.
- **Episodes:** no machine-readable source for episode declarations was verified, although Catalonia has declared none since 2015 [notes: ZBE-12].
- **Data protection:** autónomos' plates are personal data (GDPR) [notes: G5-I03].
- **Time to MVP:** about 6–8 weeks for Madrid, AMB, Bilbao and Palma, with CSV import. Then continuous curation, shared with IDEA-48.

**(g) Defensibility**
- **The app layer is copyable.** Cargoffer could extend its API to permits, and Google could make warnings label-aware.
- **Harder to copy:**
  - constraint logic plus permit workflows;
  - planner integrations;
  - a legally monitored rulebook that is right more often than the free sources.

**(h) Kill criteria**
- **A 4-week pilot converts under 3% of free checkers:** open [I].
- **Free apps add vehicle-specific alerts:** not met (see (b)).
- **Fewer than 5 of 20 distributors report fines or at least 2 hours a week of permit work:** open [I].
- **Route planners add Spanish semantics:** not observed. HERE, TomTom and PTV have none for Spain; Routal lists none; Cargoffer has labels only.

**Scores (reshaped, fleet-first)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Fines are enforced now, with dated switch-ons within about 12 months for part of the market (Palma and Badalona on 1 Jan 2027, Vigo in Sep 2027) |
| S2 Buyers in Spain | 3 | An estimated 10k–30k SME fleets entering sanctioning ZBEs (upper bound 135k employer units) |
| S3 Willingness to pay | 2 | No spend on ZBE compliance found; free awareness tools exist; fines are simply paid |
| S4 Reachability | 3 | Planner integrations, van-rental bundles and associations exist but are unproven |
| S5 Competitive gap | 4 | No Spanish permit and quota ledger or in-zone dispatch check found; only spreadsheets and free awareness apps |
| S6 Build speed | 3 | 2–4 months including the curation of 4–10 cities and planner import |
| S7 Defensibility | 3 | A maintained rulebook plus integrations, which an incumbent could still add |
| S8 Retention | 3 | Periodic use (nightly checks, monthly quotas, yearly renewals); no records duty |
| **Sellability** | **3.13** | |
| P | 3 | €200 per wrong entry, recurring for daily in-zone deliveries; the business share of fines is unknown |
| **Overall** | **3.08** | 0.6 × 3.125 + 0.4 × 3 |

**Open [I] checks**
- 50 trades autónomos with B or unlabelled vans in Madrid, Barcelona and Palma: test €39/year. Kill if under 3% convert from a 4-week free pilot.
- 20 SME distributors serving Madrid Distrito Centro, Bilbao and Barcelona: fines a month, permit hours and tools. Kill if fewer than 5 report fines or at least 2 hours a week of permit work.
- Query the DGT fleet panel for vans by label in each target municipality.
- File a transparency request to Madrid for registered plates in the Sistema de Gestión de Permisos.
- Ask 2 planners (Routal, Cargoffer) about a white-label integration.

**What would change the verdict**
- **To GO:** at least 5 of 20 distributors confirm fines or permit hours and 2 or more pilots pay at €49/month or more, or a planner or van-rental firm signs a bundle.
- **To KILL:** pilots convert under 3%, or Google Maps, Cargoffer or a planner adds label-aware, permit-aware checks for Madrid and Barcelona.

---

#### IDEA-45: DeCA evidence vault and pre-departure check for small hauliers — KILL as a stand-alone product; keep a free "DeCA inbox" inside IDEA-46 (medium)

**Validated definition.**
- **What was tested:** a carrier-side DeCA tool at €6 per vehicle per month. It would:
  - issue the DeCA when the carrier is the issuer;
  - when the shipper issues it, scan the shipper's QR before departure and store a hashed, timestamped copy;
  - check the mandatory fields by who is responsible for them;
  - show "ready to leave", offer offline inspection mode, keep the one-year archive and build an appeal pack.
- **Verdict:** the need is real but already commoditised.
  - Issuance plus a "received" inbox is sold from €0 (10–15 documents a month) to €8.33 per vehicle per month.
  - No association endorses any tool.
  - The evidence features can be copied in days.
- **What survives:** a free shipper-DeCA inbox and archive inside IDEA-46, as its acquisition wedge.

**(a) Problem reality and rule status**
- **In force:** since 5 Oct 2026 (Ley 9/2025 transitional provision 8; Resolución DGTCF of 5 Jun 2026; Orden TRM/282/2026) [notes: IND-01]. There is no lapse risk, and eFTI acceptance only starts on 9 Jul 2027 [notes: IND noise list].
- **Retention is a duty for the carrier too.** Files "deben conservarse durante al menos un año por cargador contractual y transportista efectivo". The URL "may be deactivated seven days after the service ends". No signature is required, but creation date and time must be recorded before the service starts [new: GA-P, https://ga-p.com/publicaciones/guia-para-no-perderte-con-el-nuevo-deca/, published 16 Jul 2026].
  - So a carrier that receives a shipper's DeCA needs its own copy for a year. That is a real hook, but saving the PDF in local or cloud storage satisfies it [new: Fenadismer, https://www.fenadismer.es/ojo-ofertas-abusivas-para-el-nuevo-documento-electronico-de-control/, published 10 Sep 2026].
- **Fines:** drivers are fined "más de 400 euros" even when showing the shipper's QR [new: Fenadismer, https://www.fenadismer.es/deca-sanciones-injustas-a-transportistas-por-errores-de-sus-cargadores-o-de-las-inspecciones-en-carretera/, published 15 Oct 2026]. The band is €401–600 [notes: IND-01, single source for the article numbers].
- **The Ministry's climb-down was narrow.** It archives only the reports caused by download failures between 5 and 19 Oct 2026, and "la exención no afecta en ningún caso a otras posibles infracciones" (missing data and the like) [new: Fenadismer, https://www.fenadismer.es/deca-transportes-reconoce-fallos-tecnicos-y-no-tramitara-las-multas-impuestas/, published 22 Oct 2026].
- **No official count of DeCA fines exists** (search 17; trans.info, 20 Oct 2026).
- **Liability shifting:**
  - some shippers impose private platforms and "provisional DeCAs" [new: Fenadismer, https://www.fenadismer.es/primeras-incidencias-del-deca-tras-su-entrada-en-vigor/, published 8 Oct 2026];
  - CETM says some shippers want to charge carriers per DeCA generated [new: trans.info, https://trans.info/es/el-deca-arranca-con-polemica-transportistas-denuncian-costes-fallos-tecnicos-y-cargas-administrativas-impropias-508207, published 9 Oct 2026].

**(b) Competitors**

| Tool | Offer | Price | Notes |
|---|---|---|---|
| **DecaFirma** (Francode Systems, built on Odoo) [new: https://decafirma.com/, seen 23 Oct 2026] | Issuance from a photo, WhatsApp, Excel or API; a QR that stays valid across versions; a 12-month archive; an Android driver app; a **"Recibidos" panel for subcontractors with a matching NIF**; version sealing; a "Comprobar el fichero" integrity check | Free up to 15 DeCA a month. One vehicle: €8.33/month (€100/year) or €15 month to month. 2–5 vehicles €41.67/month; 6–10 €62.50/month | Already covers most of the "vault" when the issuer uses it |
| **Cargoffer** [new: https://cargoffer.com/pricing, seen 23 Oct 2026] | DeCA and eCMR documents, plus a TMS | DeCA free for 10 a month; €29/month for 100; €79/300; €199/1,000; €0.12 per extra | Free TMS up to 5 vehicles |
| **ValenciaportPCS** [new: https://container-news.com/valenciaportpcs-introduces-electronic-administrative-control-document-feature/, published 24 Sep 2026] | DeCA generation in the port community, with a shared environment for shippers and carriers and a public QR repository | Not stated | Port-centric |
| **Fieldeas Smart Docs Hub** [new: https://www.fieldeas.com/en/digital-control-document-normative-characteristics-benefits/, updated 1 Oct 2026] | DeCA within a documents hub; advanced signatures "as evidence in disputes" | Demo only | Enterprise |
| Viafirma, Edicom [notes: IND-01; search 3] | DeCA and eCMR | Not published | Enterprise |
| ICargo (Enroca Digital), shown at Fenaex [new: https://www.interempresas.net/ObrasPublicas/662686-El-sector-se-prepara-para-el-DeCA.html, published 11 Sep 2026] | Working implementation | Not stated | Association demo, not an endorsement |
| Market floor | "opciones viables desde los 5 euros al mes" (viable options from €5 a month), with spreads of up to 1,000% [new: Fenadismer, 10 Sep 2026] | €5+ | — |

**No free Ministry, Fenadismer, CETM or UNO tool was found.** UNO published a 65-question guide, Fenaex "no impondrá ningún software", and Fenadismer tells members to compare offers (search 4).

**(c) Buyers and market size**
- **Buyers:** 152,871 road-freight companies, 61,716 of them in heavy transport [notes: IND-01].
- **Who receives the document:** 25% of 750 surveyed professionals expected the shipper to provide it [notes: IND-01]. The share that actually receives shipper-issued DeCAs is unknown [I].
- **Revenue ceiling at €59 a year per vehicle (my arithmetic):** 5% of firms × 3 vehicles ≈ €1.35M a year. Price competition from issuance tools that already include a receive panel cuts this sharply.

**(d) Willingness to pay**
- Carriers pay €5–15 per vehicle per month for issuance tools, and free tiers cover 10–15 documents a month.
- A vault-only product at €6 per vehicle would cost almost as much as an all-in tool (DecaFirma €8.33). WTP for evidence beyond issuance is not evidenced [notes: IND-01].

**(e) Distribution**
- Fenadismer (32,000+ firms) and CETM (31,000+ firms) [notes: IND-01] neither offer nor endorse a tool.
- Fenadismer's own advice is "compare and consult your association" [new: 10 Sep 2026].
- Search terms ("DeCA transportista") are crowded by vendors and guides (search 3).

**(f) Build feasibility and legal constraints**
- **Time to MVP:** under 4 weeks (QR scan, PDF capture, hash, field check, archive). No certification is needed: "no hace falta ningún programa homologado" [notes: IND-01].
- **Data protection:** driver data falls under GDPR.
- **Open [I]:** whether a carrier-side timestamp has evidential weight in appeals, and whether a qualified timestamp is needed. GA-P mentions none.

**(g) Defensibility**
- None. DecaFirma already ships a receive panel, versioning and integrity checks, and the rest can be built in days.

**(h) Kill criteria**
- **Fenadismer or CETM bundle a free tool with evidence capture:** not met (search 4).
- **The Ministry or DGTCF publish a free generator or repository:** not found.
- **Fewer than 1 in 5 carriers had a DeCA incident or fine:** open [I]. Incidents are documented anecdotally; no counts exist.
- **Additional reason to kill as stand-alone:** S5 and S7 below. Several decent near-free tools already include the receive and evidence features.

**Scores (stand-alone)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | Enforced since 5 Oct 2026, with live €401–600 roadside fines and a one-year retention duty |
| S2 Buyers in Spain | 4 | 152,871 road-freight firms |
| S3 Willingness to pay | 3 | Spend exists at €5–15 per vehicle per month, but for issuance; the vault on its own is unproven |
| S4 Reachability | 3 | Concentrated associations, but they endorse no tool |
| S5 Competitive gap | 2 | DecaFirma, Cargoffer, ValenciaportPCS and others already cover issuance and received documents, some for free |
| S6 Build speed | 5 | Under 4 weeks; no certification |
| S7 Defensibility | 1 | Trivially copyable |
| S8 Retention | 4 | A per-trip duty and a one-year archive, but archives are exportable and switching is cheap |
| **Sellability** | **3.38** | |
| P | 3 | €401–600 per incident; frequency unknown |
| **Overall** | **3.23** | 0.6 × 3.375 + 0.4 × 3. The high urgency and buyer count lift the formula, but S5 and S7 make it unsellable on its own |

**Open [I] checks**
- Ask 20 carriers what share of their DeCAs comes from shippers, and how many incidents or fines they have had since 5 Oct 2026. Kill confirmed if fewer than 1 in 5 had one.
- Ask a transport lawyer whether a carrier's hashed, timestamped copy helps an appeal.

**What would change the verdict**
- An association agreeing to recommend a carrier-side, issuer-agnostic inbox.
- Inspectors routinely fining carriers for shippers' missing data, so that evidence becomes decisive.

In either case, revive it only as a module of IDEA-46.

---

#### IDEA-46: Haulier revenue recovery: automatic fuel-revision lines, detention claims and late-payment interest — GO (pilot, with scope changes) (medium)

**Validated definition (scope for the pilot).**
- **Buyer:** SME hauliers with 1–50 vehicles. Transport gestorías act as resellers.
- **MVP:**
  1. **Fuel line.** It pulls the Ministry's diesel index, applies the RDL 9/2026 coefficient by vehicle mass and diesel-price band, and adds an itemised fuel-revision line to every invoice, through invoicing-tool integration or a PDF annex. It works in both directions.
  2. **Late payment.** Due-date tracking, statutory interest and the €40 compensation after day 30 (Ley 15/2009 art. 41, Ley 3/2004), with claim letters.
  3. **Evidence files.** A file per shipper for Fenadismer's complaint channel or an inspection when the line is refused or base rates are cut.
  4. **Wedge.** A free DeCA inbox and archive (from IDEA-45).
- **Later:** geofenced detention claims (art. 22) in release 2.
- **Dropped from the MVP until a legal review:** shipper scorecards.
- **Price:** €19/month for up to 3 vehicles, plus €4 per extra vehicle.
- **Type C variant:** a fuel-line-only add-on at €5–9/month in invoicing marketplaces. It is automated, its value shows on every invoice, and it needs little support.

**(a) Problem reality and rule status (settles the RDL 9/2026 and RDL 25/2026 item)**
- **RDL 9/2026 is convalidated.**
  - Published in BOE no. 92 on 15 Apr 2026 and in force since 16 Apr 2026 [new: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-8283, seen 23 Oct 2026].
  - Congress "acordó convalidar" it on 30 Apr 2026 [new: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-9793, seen 23 Oct 2026].
- **RDL 25/2026 is convalidated, by the Diputación Permanente during the dissolution.**
  - Published in BOE no. 241 on 30 Sep 2026 and in force since 1 Oct 2026 [new: https://www.boe.es/eli/es/rdl/2026/09/29/25, seen 23 Oct 2026].
  - The Diputación Permanente "acordó convalidar" it on 16 Oct 2026 [new: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-21788, seen 23 Oct 2026].
  - Its measures run to 31 Dec 2026:
    - professional-diesel aid of €0.05/l in October, €0.12/l in November and €0.19/l in December, with safeguard variants;
    - agricultural diesel aid of up to €0.20/l;
    - no crisis-related dismissals for beneficiaries.
- **No lapse risk.** The indexation duty now sits in Ley 15/2009 art. 38 as amended by a convalidated decree-law. The revision is:
  - mandatory and itemised on the invoice;
  - automatic at a variation of 5% or more, unless a lower threshold is agreed in writing;
  - applied every billing period in continuous contracts;
  - binding: "el pacto en contrario… se considerará nulo" (any agreement to the contrary is void).
- **The formula.** Orden FOM/1882/2012 now uses C coefficients by pre-tax diesel price and MMA. Until 30 Jun 2026 the RDL 7/2026 aid could not be counted in the calculation.
- **Payer infractions.** New infractions in Ley 16/1987 arts. 140.43 and 141.31 apply to payers who oppose the line, split at a transport price of €3,000 [new: BOE analysis of BOE-A-2026-8283; https://www.boe.es/eli/es/l/2009/11/11/15/con, consolidated 15 Apr 2026]. Fines reach €18,000 for repeat offences [notes: IND-02].
- **The cost shock and shipper resistance:**
  - The G index rose 44.6% for heavy and 38.4% for light vehicles between January and 1 Oct 2026 [new: Fenadismer, https://www.fenadismer.es/canal-de-denuncias-contra-los-cargadores-que-no-indexen-el-combustible-a-sus-transportistas/, published 13 Oct 2026].
  - Fenadismer accused DIA of "rechazar sistemáticamente la actualización de los precios del transporte" and of leaving the surcharge off March–April invoices [new: trans.info, https://trans.info/es/fenadismer-denuncia-a-cargadores-474170, published 11 May 2026].
  - No figure exists for how often shippers refuse (search 20).
- **Late payment.** The average was 52 days in Aug 2026, with 38% of payers beyond 60 days [notes: IND-04]. The payer is in default after 30 days (art. 41) [new: BOE consolidated].
- **Detention.** Art. 22 applies after a wait of more than one hour, with an IPREM-based hourly indemnity [new: BOE consolidated]. The notes read it as 2×IPREM/day per hour, with surcharges on days 2 and 3 [notes: IND-06]. The evidence on waits is a single 2023 study [notes: IND-06].

**(b) Competitors**
- **CETM "Calculadora de Costes e Indexación"** [new: https://www.cetm.es/cetm-calculadora-de-costes-e-indexacion/, seen 23 Oct 2026]:
  - downloadable full, simplified and construction-vehicle calculators, plus a guide, for "organizaciones y empresas asociadas" (member organisations and companies);
  - versions for indexations from 15 Apr–30 Jun 2026 and from 1 Jul 2026, the latter cited to "RDL 18/2026" (written "182026" on the page, unverified);
  - no invoice lines and no evidence output described. **The kill criterion is not met.**
- **The Ministry's free web calculator.** It takes the contract date, transport date and vehicle type and returns the diesel-variation index and the weighting coefficient [new: trans.info, https://trans.info/es/nueva-formula-para-el-transporte-como-aplicar-la-revision-del-precio-del-gasoleo-con-el-real-decreto-9-2026-471063, published 24 Apr 2026]. Calculation itself is therefore free. The value must be in automation on invoices, evidence and claims.
- **Fenadismer's complaint channel** offers advice and anonymous complaints to inspection [new: 13 Oct 2026].
- **TMS and invoicing:**
  - No Spanish TMS was found automating the fuel line (search 5).
  - Cargoffer's TMS (€0–299/month) includes invoicing, with no fuel-line feature stated [new: https://cargoffer.com/, https://cargoffer.com/pricing].
  - Mainstream invoicing costs €6.60–29.50/month [notes: G5-I02].
- **Payment tools:** Wtransnet (Coface guarantee) and CETM's Icired default registry [notes: IND-04].

**(c) Buyers and market size**
- **Buyers:** 152,871 road-freight companies [notes: IND-01].
- **Revenue ceiling (my arithmetic):** reaching 2–5% gives 3,000–7,600 firms; at €228 a year (€19/month) that is about €0.7–1.7M ARR, before per-vehicle add-ons.

**(d) Willingness to pay**
- **Value at stake (my arithmetic, illustrative).** Take a contract priced in early January 2026. With C ≈ 0.4 for heavy trucks and the G variation of 44.6% to 1 Oct, the revision is about 0.4 × 44.6% ≈ 18% of the base price. A carrier that cannot bill it loses that share of revenue. The exact formula terms were not re-derived from the Orden FOM/1882/2012 text.
- **Adjacent spend:** invoicing software at €6.60–29.50/month, TMS at €99/month (Cargoffer Professional), and DeCA tools.
- **The risk:** carriers may not dare to bill (the DIA case). This is the kill test.

**(e) Distribution**
- **Fenadismer** campaigns on indexation and runs the complaint channel, but **CETM has its own calculator**, so it is a weaker channel.
- **Other routes:** transport gestorías; invoicing marketplaces for the type C add-on; search terms ("coeficiente G gasóleo", "revisión precio combustible factura").

**(f) Build feasibility and legal constraints**
- **Index access.** The Ministry's index page returned **403 to an automated fetch** (https://www.transportes.gob.es/transporte-terrestre/servicios-al-transportista/indice-de-variacion-los-preciosdel-gasoleo-en-espana, cited in Orden TRM/1034/2026's annex [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20744, BOE 6 Oct 2026]). Plan for a weekly manual update or a partner feed.
- **Formula tables:** from RDL 9/2026.
- **Invoicing APIs:** Holded's developer page could not be fetched ("header overflow"), so its invoice-line API is **unverified**.
- **Detention:** geofencing needs driver information under the GDPR.
- **Letters:** need a lawyer's review.
- **Time to MVP:** 4–6 weeks.

**(g) Defensibility**
- **Weak alone.** The formula and templates can be copied in days, and CETM, the Ministry and TMS vendors could close the gap.
- **Some moat** comes from association or gestoría distribution, the trip and invoice history, and the DeCA inbox wedge.

**(h) Kill criteria**
- **60% or more of 15–20 hauliers would not add the line even if automatic:** open [I].
- **CETM's tool already produces invoice lines and evidence:** not met.
- **New risks:**
  - diesel falls and the line turns negative, which shifts the value to shippers;
  - a TMS such as Cargoffer adds the line for free.

**Scores (pilot scope)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | The duty is in force and convalidated and hits every invoice; money is lost monthly, but there is no deadline or fine on the carrier |
| S2 Buyers in Spain | 4 | 152,871 road-freight firms |
| S3 Willingness to pay | 3 | Spend on invoicing and TMS exists; WTP for the line is unproven |
| S4 Reachability | 3 | Associations and gestorías exist; CETM competes with its own calculator |
| S5 Competitive gap | 4 | Only calculators (CETM, Ministry) and manual invoicing; no automated invoice line or evidence file found |
| S6 Build speed | 4 | 1–2 months; index-feed friction |
| S7 Defensibility | 2 | Copyable; the channel and history are only partial moats |
| S8 Retention | 4 | Used on every invoice, with claims history accumulating |
| **Sellability** | **3.50** | |
| P | 4 | Costs up about 30% and an unbilled line worth roughly 18% of price threaten small hauliers' viability; widespread |
| **Overall** | **3.70** | 0.6 × 3.50 + 0.4 × 4 |

**Open [I] checks**
- Ask 15–20 hauliers whether they would add the line if it were automatic. Kill if 60% or more would not.
- Ask 3 transport gestorías whether they would resell it.
- Get a legal review of shipper evidence files and scorecards (data protection, competition law).
- Check whether Holded, Quipu or a3factura expose invoice-line APIs.

**What would change the verdict**
- **Kill** if the interview test fails, if diesel falls below the reference so that lines turn negative for months, or if a free TMS or the Ministry adds automatic invoice lines.
- **Strengthen** if Fenadismer or gestorías agree to distribute it, or if inspections sanction refusing shippers (which would make carriers bolder).

---

#### IDEA-49: Packaging EPR, PPWR and plastic-tax compliance kit — KILL (medium)

**Validated definition.**
- **What was tested:** a packaging bill-of-materials kit for SMEs that pack goods or first place packaged goods in Spain. From the bill of materials it would produce:
  - tonnage by material (household against commercial and industrial);
  - the 31 March MITECO declaration and the scheme declarations;
  - invoice fee lines, PPWR declarations of conformity and a modelo 592 worksheet;
  - a supplier registration-number tracker.
- **Price tested:** €19–49 a month, or €39 a month for food firms plus a food-waste module.
- **Verdict:** the duty is real and is biting through marketplaces. But:
  - the collective schemes already bundle data platforms, declaration and producer-registry services into membership;
  - a Spanish SaaS already sells the RD 1055/2022 declaration at €49–99 a year (gestoría tier €349–599 a year);
  - the PPWR's heavy redesign duties are dated 2030.
  - The remaining gap is a cheap, copyable calculator.

**(a) Problem reality and rule status**
- **The declaration duty.** Producers report each calendar year's packaging to MITECO "antes del 31 de marzo del año siguiente". The window for 2026 data runs from 2 Jan to 31 Mar 2027, with a simplified form below 15 t.
- **The register.** It is published as an Excel file updated "en general cada mes", and a web service for automated queries is "under development".
- **Platforms must check producers.** Online platforms must check producers' NIF, name and registration number against the public list before letting them sell.
- **The PPWR widens who counts as a producer.** The PPWR (applicable since 12 Aug 2026) changes the "productor" definition (MITECO nota interpretativa dated 27/07/2026). [All: new: https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/prevencion-y-gestion-residuos/registro-productores-producto/registro-productores-producto-seccion-envases.html, seen 23 Oct 2026.]
- **Sanctions.** Failing to register in the Registro de Productores, or to report the data, is **grave** under Ley 7/2022 art. 108.3.ac, with fines of €2,001–100,000 (art. 109.1) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2022-5809, seen 23 Oct 2026]. No enforcement cases were found (the [S\*] was not run).
- **PPWR.** It has applied since 12 Aug 2026, but its headline targets (recyclability by 2030) come later. The Dec 2025 Omnibus proposal to suspend the authorised-representative duty "is currently being examined" [new: https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en, seen 23 Oct 2026]. The EC page gives no dates for declarations of conformity or labels, so the DoC timing comes only from the notes [notes: RET-15].
- **EUDR.** 30 Dec 2026 for large and medium operators and 30 Jun 2027 for micro and small ones. Delegated Regulation (EU) 2026/2102 adds products from 30 Dec 2027 [new: https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en, seen 23 Oct 2026].
- **C-12 (Ley 1/2025 dates): settled.**
  - The final provision literally says "entrará en vigor el 2 de enero de 2025", although the law was published on 2 Apr 2025.
  - The art. 6 obligations apply "transcurrido el plazo de un año" from BOE publication, so from April 2026.
  - Having no prevention plan is a grave infraction (art. 20.2.b) of €2,001–60,000 (art. 21.b), defined by the regions. Micro firms are exempt (art. 6.6).
  - [new: https://www.boe.es/eli/es/l/2025/04/01/1/con, seen 23 Oct 2026.]
- **Plastic tax.** €0.45/kg, a 5 kg/month import exemption and modelo 592 [notes: RET-16]; the AEAT page was not re-fetched.
- **No election lapse risk.** The PPWR is EU law, and RD 1055/2022 and Ley 7/2022 are in force.

**(b) Competitors**

| Provider | Offer | Price | Notes |
|---|---|---|---|
| **Ecoembes Comerciales** (Ecoembes' scheme for commercial packaging) [new: https://www.ecoembes.com/sites/default/files/inline-files/corporativo/ecoembes/presentacion-asamblea-general-2026.pdf, deck of 30 Jun 2026] | "Integramos todo el ciclo de cumplimiento": a **"Plataforma del Dato"**, **"Declaración de envases"** and **"Registro de productores"**. Also the "CircularCheck" tool, PPWR anticipation, ecomodulation cost tools and "The Circular Campus". ISO 27001. 1,541,750 t adhered; 80 alliances, including CEPYME and CEOE | 2027 fees per tonne: flexible plastics €164, rigid plastics €173, paper and cardboard €37, steel €132, aluminium €132, wood €20, other €173, plus €2.5/t integral management | **The declaration and registry service is bundled into membership.** This is the kill criterion, largely met |
| **Ecoembes** (household packaging) [new: Grant Thornton alert, https://www.grantthornton.es/contentassets/4fb8a959b6d54b6d89d3e2bf34e43199/nuevos-procedimientos-de-verificacion-para-auditores-en-las-declaraciones-anuales-ordinarias-de-envases-a-ecoembes.pdf, Apr 2026] | The member "Área Privada" gives each firm its declaration type and report model. Members file DAE Domésticos and, since 2025, **DAE Comerciales**, verified by an **auditor's agreed-procedures report** (full or partial). The 2025 data were due on 31 May 2026 | Fees per material (2024: rigid plastic €776/t, paper €190/t; search 6 snippet) | The auditor report is an adjacent spend; its fees were not found |
| Envalora, Cartón Circular, GENCI [new: https://cartoncircular.es/, seen 23 Oct 2026; Envalora's 2026–2027 tariff headlines in search 6; genci.es returned 401] | Commercial and industrial schemes with member declaration areas | Ecomodulated tariffs (2027) | Cartón Circular has a login "Acceso declaraciones" |
| **Envasify** [new: https://envasify.com/planes-y-precios/; https://wordpress.org/plugins/envasify-lite/, seen 23 Oct 2026] | WooCommerce and Shopify packaging data, tonnage by material, MITECO eSIR templates, a SHA-256 audit PDF, and a multi-client gestoría panel with white label | Lite €0 (up to 3 t); Professional **€49/year** (launch price; €99 list from 1 Apr 2027); Enterprise **€349/year** (€599 list) for gestorías, covering 25 NIFs | The WordPress plugin has **fewer than 10 active installations**: weak organic demand. No PPWR or modelo 592 |
| SEIDOR (SAP partner) [search 8 snippet] | Solution to prepare the SCRAP files | Not published | ERP add-on |
| Ecovidrio [search 8 snippet] | "Working on an integral solution for all your packaging" with other schemes | — | The schemes are converging on one-stop tools |

**(c) Buyers and market size**

From my parse of MITECO's public register Excel of 30 Sep 2026 [new: Excel linked from the MITECO page above, downloaded 23 Oct 2026]:
- **66,742 registration numbers for 61,279 unique NIFs.**
- **New registrations rose sharply in 2026.** By the year in the registration number: 9 (2022), 22,980 (2023), 8,999 (2024), 11,405 (2025) and **23,349 (January–September 2026)**. That is consistent with the PPWR and platform checks driving registrations.
- **About 44% are foreign entities.** 27,077 NIFs start with N (foreign entity) and 163 with W.
- **About 34,000 are Spanish legal entities:** B (SL) 24,706, A (SA) 7,025, F (cooperative) 1,447, and others.
- **Natural persons are almost absent:** 3 NIFs outside the letter prefixes. This suggests that sole-trader sellers are largely unregistered, or file through others.

Two other sources:
- **Conflicting counts.** Alimarket reports 43,996 registered firms at the start of 2026, with 13,278 registrations in 2024 and 6,631 in 2025 [new: https://www.alimarket.es/envase/noticia/420353/mas-del-50--de-las-empresas-obligadas-a-gestionar-sus-residuos-de-envase-aun-no-figurarian-en-el-registro-del-miteco]. Its yearly figures differ from my count by number year, but the start-2026 total is consistent with mine (43,393 numbers dated 2025 or earlier).
- **Under-registration.** The packaging cluster estimates that over half of obliged firms are still unregistered (no census exists).

**Revenue ceiling (my arithmetic).** At Envasify-level prices, 5% of about 34,000 Spanish registrants paying €99 a year is about €0.17M. At €39 a month, 1% paying would bring about €0.16M.

**(d) Willingness to pay**
- **Anchors:** Envasify at €49–99 a year for SMEs and €349–599 a year for gestorías. The scheme fees are paid anyway, and the platforms come with them.
- **Adjacent spend:** auditors' agreed-procedures reports for Ecoembes declarations, and consultants (fees not found).
- **Implication:** the longlist's €19–49 a month for online sellers is 2–10 times the market price.

**(e) Distribution**
- **Marketplaces' duty to check registration numbers** is the strongest demand driver [new: MITECO page].
- **Gestorías:** Envasify already has a white-label gestoría tier.
- **Schemes:** they build their own tools; Ecoembes Comerciales has 80 alliances, including CEPYME and CEOE.
- **Other channels:** FIAB (for food firms) and packaging suppliers.

**(f) Build feasibility**
- **Easy.** The register is a public Excel file, eSIR templates exist, and AI extraction from spec sheets is commodity. MVP in 1–2 months.
- **Legal:** low data sensitivity. PPWR conformity documents must track delegated acts.

**(g) Defensibility**
- Low. The schemes own the declaration flow and data, a cheap Spanish competitor exists, and calculators are trivially copied. A verified supplier and packaging library would take years and would compete with the schemes' "Plataforma del Dato".

**(h) Kill criteria**
- **Schemes give members free declaration tools: largely met.** Ecoembes Comerciales integrates the data platform, declaration and producer registry; Ecoembes members declare in the Área Privada.
- **A typical SME prepares the declaration in under a day:** open [I].
- **Small sellers report no checks from marketplaces or inspectors:** contradicted. Platforms must now verify registration numbers.

**Scores (as specified)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | A legal duty with a 31 Mar 2027 deadline and grave-infraction fines, but enforcement beyond marketplace checks is unevidenced |
| S2 Buyers in Spain | 3 | About 34k Spanish registrants plus the unregistered |
| S3 Willingness to pay | 2 | The market price is €49–99 a year, and the scheme platforms are included in fees |
| S4 Reachability | 2 | Gestorías, schemes and marketplaces exist, but the schemes compete and the plugin channel shows fewer than 10 installs |
| S5 Competitive gap | 2 | Several decent tools: the scheme platforms, Envasify and SEIDOR |
| S6 Build speed | 4 | 1–2 months |
| S7 Defensibility | 2 | Copyable; the schemes hold the data |
| S8 Retention | 4 | An annual legal duty plus an accumulated bill of materials, but used once a year |
| **Sellability** | **2.88** | |
| P | 3 | Moderate: scheme fees plus a declaration chore; the fine risk is real but rarely evidenced |
| **Overall** | **2.93** | 0.6 × 2.875 + 0.4 × 3 |

**Open [I] checks**
- Interview 10 online sellers or importers and 10 food SMEs: hours per declaration, auditor fees, who files today. Revive only if a typical food SME spends 2 days or more and pays €1,000 or more a year in consultant and auditor fees that the product could replace.

**What would change the verdict**
- **Revive as a white-label for gestorías or auditors** if the interviews show material hours and fees.
- **Revive for food firms with 10+ staff** if it combined DAE Domésticos and DAE Comerciales, the auditor evidence pack, modelo 592 and the Ley 1/2025 plan in one place.

The 27k foreign registrants point to a cross-border EPR service market (section 3), outside the user's target.

---

#### IDEA-50: RCA autopilot: food-contract generation and registration before delivery — GO (pilot; fruit, vegetables and citrus first, wine for the 2027 harvest) (medium)

**Validated definition (after a scope change).**
- **Buyer:** food buyers that purchase from farmers: fruit, vegetable and citrus packers and origin wholesalers first, wineries next, then olive mills, meat and dairy buyers and cooperatives buying from non-members.
- **What it does:**
  - templates with all minimum terms and a cost-of-production clause, signed by the grower through a mobile link;
  - registration in the RCA through the buyer's own RCA API access, triggered by a purchase order or weighbridge ticket and confirmed before the load is accepted;
  - automatic re-registration of amendments;
  - alerts for the 30-day payment term;
  - a per-grower evidence file and an inspection pack.
- **Price:** €39/month (up to 300 contracts a year) or €99/month (up to 3,000), or a €149 season pass.
- **The change:** the citrus and fruit-and-vegetable season runs October to June, and that is where AICA's registration controls concentrate. Wineries are pre-sold for the August–October 2027 harvest.

**(a) Problem reality and rule status**
- **The rules:** Ley 12/2013 (as amended by Ley 16/2021) and RD 1028/2022 are in force. The RCA has been live since Dec 2022.
- **Who registers, and when** [new: https://www.aica.gob.es/servicios-en-linea/Registro%20de%20Contratos%20Alimentarios/preguntas-frecuentes-rca, seen 23 Oct 2026]:
  - The buyer registers ("el operador que compra"), or the integrator in integration contracts, "antes de la entrega".
  - Amendments are registered before delivery of the affected product. Multi-year contracts without changes are not re-registered.
  - Cooperative–member contracts are exempt; purchases from non-members are not.
- **AICA's 2025 report: what the tables show** [new: https://www.aica.gob.es/content/dam/aica/docs/publicaciones/memorias/Memoria_Anual_de_Actividades_2025.pdf, published 24 Sep 2026; text extracted 23 Oct 2026]:
  - **991 infractions and 109 companies sanctioned.**
  - **506 failures to register in the RCA, all by the "industria" link.** The cumulative table since 2014 also shows 506, so **every RCA sanction to date came in 2025**: enforcement has only just started to bite.
  - **619 infractions in wine (616 on wine grapes)** and 162 in fruit and vegetables (111 in citrus).
  - **Concentration.** The dedicated RCA-registration programme ran 31 controls, all in fruit and vegetables. The general contract programme checked art. 11 bis.2 in 120 actions, only 2 of them on wine grapes and 11 on wine. So the 616 grape infractions probably come from very few wineries, each with hundreds of unregistered contracts (inference: 109 companies sanctioned in total).
  - **Fines:** minor €250–3,000 per infraction (non-registration is minor), serious €3,001–100,000, published if serious or very serious [notes: IND-18]. Since 2014, €27,923,451 in fines.
- **The inspection decree.** The draft royal decree on AICA's inspection regime has been at "trámite de audiencia e información pública" since 30 Sep 2026 [new: https://www.aica.gob.es/, seen 23 Oct 2026]. It is a regulation, not a bill, so it does not lapse. It is likely to slip into 2027, given the hearing stage, a probable Consejo de Estado opinion and the 29 Nov election (inference). The duty to register does not depend on it.
- **Practical friction.** AICA's homepage warns that the Cl@ve login gateway "is unstable and may block access".

**(b) Competitors**
- **AICA's own channels.** A web form with a digital certificate (up to 5 documents and 5 MB per upload), and an **"API de servicios RCA"**, requested by form, with an integration manual for developers and open only to registered buyers [new: RCA FAQ]. The API was built for "operadores con un elevado volumen de contratos" [new: Memoria 2025].
- **Winery ERPs: none found advertising RCA integration** (search 9):
  - eVins, cloud winery ERP "desde 40 €/mes", with no RCA, Ley de la Cadena or weighbridge mention [new: https://www.softwaredoit.es/evins/evins.html];
  - Solmicro ERP Bodegas (Zucchetti), with grape reception linked to the weighbridge [search 9 snippet];
  - Uvatec (Tecon, on Microsoft Business Central) [search 9 snippet].
- **E-signature:** Signaturit costs €35–57 per user per month for 5–20 envelopes [notes: G5-I05].
- **Gestorías and consultants:** no prices found.

**(c) Buyers and market size**
- **Pool:** 27,300+ food and drink firms, 3,669 cooperatives and 950+ FEV wineries [notes: IND-18, IND-19]. The subset that buys directly from primary producers is not published (the RCA "no es un registro de acceso público"). My estimate is 10,000–20,000 buyers.
- **Revenue ceiling (my arithmetic):** 3% of them (300–600) at €468–1,188 a year gives about €0.14–0.71M ARR.

**(d) Willingness to pay**
- **Adjacent spend:** winery ERPs from €40/month, e-signature at €35–57 per user per month, and gestoría filing.
- **Exposure is large for the few who are caught.** A buyer with 300 unregistered grower contracts faces at least 300 × €250 = €75,000 if each contract counts as one infraction, as AICA's counts suggest (my arithmetic). That is a strong insurance argument, against a low probability of inspection.

**(e) Distribution**
- **Associations:** FEV, Cooperativas Agro-alimentarias and FIAB [notes].
- **Farm unions:** COAG and ASAJA run Ley de la Cadena sessions before the harvest (search 18 titles; older items).
- **ERP and weighbridge vendors:** Zucchetti/Solmicro, Doit/eVins and Tecon/Uvatec as integration partners.
- **Agri gestorías.**

**(f) Build feasibility and legal constraints**
- **API access.** It is requested by the buyer once it is registered. A SaaS would operate the buyer's credentials, which needs a legal check [I].
- **Representation.** The legal representative logs in with a representation certificate through Cl@ve and can authorise named natural persons [new: RCA FAQ].
- **Data protection.** Growers' personal data falls under the GDPR.
- **Contract templates** need a food-chain lawyer's review.
- **Time to MVP:** 6–8 weeks, plus reliability at harvest peaks.

**(g) Defensibility**
- Medium. The RCA integration, weighbridge and ERP connectors, harvest-peak reliability and the contract archive create friction. ERP vendors are the main threat, since they could add the same connection.

**(h) Kill criteria**
- **Leading winery and agri ERPs integrate the RCA at no extra cost:** not met on desk evidence (search 9). Confirm with 5 vendors [I].
- **Buyers spend under an hour a season on the RCA:** open [I].
- **New risk: enforcement concentration.** The low probability of inspection (22 wine inspections, 109 firms sanctioned) may leave most buyers feeling no urgency.

**Scores (pilot scope)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | An enforced duty triggered by every purchase, with record 2025 sanctions; no new deadline |
| S2 Buyers in Spain | 2 | An estimated 10k–20k buyers from primary producers |
| S3 Willingness to pay | 3 | Some adjacent spend (ERPs from €40/month, e-signature, gestorías) |
| S4 Reachability | 3 | Concentrated associations and ERP partners, unproven |
| S5 Competitive gap | 4 | Only the manual web form, in-house API builds and gestorías; no SaaS or ERP integration found |
| S6 Build speed | 3 | API, e-signature, templates and harvest reliability: 2–4 months |
| S7 Defensibility | 3 | Integration, archive and partner channels |
| S8 Retention | 4 | A recurring legal duty and a contract archive, though the wine segment is seasonal |
| **Sellability** | **3.25** | |
| P | 3 | Fines are serious when caught, but inspection probability is low |
| **Overall** | **3.15** | 0.6 × 3.25 + 0.4 × 3 |

**Open [I] checks**
- Ask AICA how many of the 616 grape infractions were non-registration, and across how many companies.
- Interview 10 buyers (5 citrus or fruit and vegetables, 5 wineries) on RCA hours per season, who uploads, and gestoría fees.
- Confirm with 5 ERP and weighbridge vendors whether they connect to the RCA.
- Get a legal opinion on a SaaS acting with the buyer's API credentials.

**What would change the verdict**
- **Kill** if ERPs already integrate the RCA, or if buyers report under an hour per season.
- **Strengthen** if an ERP vendor or FEV agrees to pilot, or if AICA's 2026 campaign again targets RCA registration.

---

#### IDEA-51: Fertilisation-plan and nutrient-record workspace — RESHAPE to a cooperative-channel tool aiming at "recognised software" status under RD 1051/2022 art. 20 (low)

**Validated definition (after reshape).**
- **Buyer:** cooperatives' technical services (white-label for member farms), with REGFER advisers as a secondary buyer.
- **What it does:**
  - a plan de abonado for each production unit;
  - fertilisation records within one month, logged by the farmer by mobile or WhatsApp;
  - sign-off by the adviser or technical service;
  - exports to SIEX and the CUE once their formats are defined.
- **The strategic aim:** recognition as a "programa informático" by the regions that use RD 1051/2022 art. 20. That would let farmers meet the advisory duty (from about Sep 2027 in vulnerable zones and Sep 2028 elsewhere) through software instead of a paid adviser.
- **Price:** €1.50–3 per farm per month, paid by the cooperative, or €39 per adviser per month.

**(a) Problem reality and rule status**

RD 1051/2022, consolidated text updated 3 Nov 2025 [new: https://www.boe.es/eli/es/rd/2022/12/27/1051/con, seen 23 Oct 2026]:
- **Who makes the plan.** The **farm holder**, not an adviser, is "responsable de la elaboración y aplicación de un plan de abonado en cada unidad de producción". It applies from 1 Sep 2026, or from 1 Jan 2026 for irrigated crops sown between March and June 2026 (arts. 4.2 and 6).
- **Records.** Each fertilisation must be recorded within one month (art. 4.1).
- **Exemptions.** Farms of 5 ha or less with 1 ha or less irrigated are exempt from records; rainfed units of 10 ha or less are exempt from the plan.
- **Advisory duty.** It starts one year after the plan duty in vulnerable zones and two years after elsewhere (art. 6.6), so about Sep 2027 and Sep 2028 (derived).
- **Advisers** must be registered in REGFER from 1 Jul 2026 (art. 18.6).
- **Art. 20, the software route.** Where the region so provides, "las obligaciones de asesoramiento podrán cumplirse si el titular de la explotación emplea un programa informático" recognised by the authority, as long as the holder keeps a digital farm notebook.
- **Sanctions** refer to the sectoral laws (art. 26).

Other status points:
- **Digital notebook.** The CUE is voluntary until the next CAP period [notes: IND-20; search 10]. An Aug 2025 report notes there was no official clarity on when the plan must go into the notebook [search 10: infoagro, 28 Aug 2025].
- **Political risk.** The duty is a royal decree, so no lapse, but the sector calls it "inasumible" and the 28 Oct 2026 tractor protest demands simplification [notes: IND-20]. A new government could amend it without the Cortes.

**(b) Competitors**
- **FertiliCalc** (Universidad de Córdoba): nutrient requirements and fertiliser amounts for 150 crops; downloads, an app and Python code; updated 23 Nov 2024; free downloads [new: https://www.uco.es/fitotecnia/fertilicalc.html, seen 23 Oct 2026].
- **Agroptima:** the official cuaderno de explotación with fertiliser records. Priced "según hectáreas y usuarios" on quote; no plan de abonado listed [new: https://www.agroptima.com/es/precios/, seen 23 Oct 2026].
- **Cuaderno de Campo Cooperativo:** only a rollout map is visible; its features are unverified [new: https://www.agro-alimentarias.coop/, seen 23 Oct 2026].
- **MAPA's free CUE software and regional tools:** unverified, because the MAPA site returned 503.
- **Kill criterion "free public software or the cooperative notebook generates plans": open.**

**(c) Buyers and market size**
- 3,669 cooperatives with over 1M member families [notes: IND-20]. The number of REGFER advisers and of non-exempt farms is unknown, and the S\* check was not run.
- **Revenue ceiling (illustrative, my arithmetic):** 100 cooperatives × 200 farms × €2 a month is about €0.48M a year.

**(d) Willingness to pay**
- Weak. The calculators are free, the incumbents price by quote, and advisers are price-sensitive [notes: G5-I06].
- The art. 20 route, if it exists in a region, would give a concrete saving: the cost of an adviser.

**(e) Distribution**
- Cooperativas Agro-alimentarias, UPA, ASAJA, Unió de Pagesos and input distributors [notes]. All are unproven [I].

**(f) Build feasibility**
- **Agronomy:** the rule tables need an agronomist, and regional formats differ.
- **Recognition:** whether any region has opened the art. 20 recognition is unknown.
- **SIEX:** the exchange format and API are unverified (the S\* was not run).
- **Time to MVP:** 6–8 weeks for the main crops.

**(g) Defensibility**
- Low, unless regional recognition is obtained. That would be an accreditation-type moat.

**(h) Kill criteria**
- **The CUE software or the cooperative notebook already generates plans:** open.
- **Additional finding against the original idea.** The adviser buyer is not yet compelled, since advice becomes mandatory only in 2027 and 2028, and holders can draft plans themselves with free calculators.

**Scores (reshaped)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | The plan duty has been in force since 1 Sep 2026, and the advisory duty in vulnerable zones starts in about 11 months |
| S2 Buyers in Spain | 2 | Cooperatives (3,669) plus advisers and larger farms: an estimated 5k–20k paying entities |
| S3 Willingness to pay | 2 | Free calculators; quote-only incumbents; price-sensitive advisers |
| S4 Reachability | 3 | Concentrated cooperative federations, unproven |
| S5 Competitive gap | 3 | Free calculators and farm notebooks exist, but plan generation by the public tools is unverified |
| S6 Build speed | 3 | Agronomy tables, regional formats and possible recognition |
| S7 Defensibility | 2 | Low, unless recognised under art. 20 |
| S8 Retention | 4 | An annual plan, monthly records and an accumulated farm history |
| **Sellability** | **2.88** | |
| P | 3 | A described but unquantified burden ("inasumible") |
| **Overall** | **2.93** | 0.6 × 2.875 + 0.4 × 3 |

**Open [I] checks**
- Ask 3 regional agriculture departments (for example Castilla-La Mancha, Andalucía and Cataluña) whether they have opened or plan the art. 20 recognition.
- Test whether MAPA's CUE app and the Cuaderno de Campo Cooperativo generate plans.
- Ask Cooperativas Agro-alimentarias whether it would distribute the tool.
- Count REGFER advisers.

**What would change the verdict**
- **To GO:** a region opens art. 20 recognition and a cooperative federation agrees to pilot.
- **To KILL:** the public CUE app or the cooperative notebook already generates plans, or the duty is postponed by a new government.

---

## 3. Cross-cutting findings (for other batches and the final ranking)

**Rule status and the election**
1. **Decree-laws are being convalidated during the dissolution.**
   - The Diputación Permanente convalidated RDL 25/2026 on 16 Oct 2026 [new: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-21788].
   - Congress had convalidated RDL 9/2026 on 30 Apr 2026 [new: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-9793].
   - Relevance to batch 5 (the RDL 29/2026 vote around 12 Nov) and batch 1 (any VeriFactu decree-law): the mechanism works during the dissolution, and each vote still depends on majorities.
2. **Other decree-laws seen in the BOE.**
   - **RDL 27/2026** of 29 Sep 2026, "por el que se adoptan medidas urgentes para reforzar la estabilidad de los contratos de arrendamiento de vivienda habitual" (BOE 1 Oct 2026, BOE-A-2026-20385) [new: https://www.boe.es/boe/dias/2026/10/01/]. Only the title was seen; its convalidation status was not checked. It is for batch 5, alongside the notes' RDL 26/2026 and RDL 29/2026.
   - **RDL 18/2026** exists. It is cited in Orden TRM/1034/2026 (art. 28, rail aid) and by CETM for the indexation tools dated 1 Jul 2026; its content was not verified.
3. **Caretaker status (background, not fetched).** Under art. 101 CE the Government ceases only after the 29 Nov election, so royal decrees can still be approved until then. Drafts at the hearing stage, such as AICA's inspection decree (since 30 Sep 2026), are unlikely to finish before the election (inference).

**ZBE city status (C-01, C-13), settled for all batches; details in IDEA-48 (a)**
4. **Valencia: no ZBE.** Final approval was rejected on 28 Oct 2025 by 19 votes to 13, there has been no vote since, and Vox requires "sin régimen sancionador". The cities track's valencia.es source was a committee approval.
   - The regional-claims row "Valencia: low-emission-zone logistics API" is **contradicted**.
   - The DGT NAP shows Valencia "active" from 1 Jun 2026, which is wrong.
5. **The other contested schemes:**
   - **Málaga:** annulled; fines stopped on 14 Oct 2026; finality expected on 25 Nov 2026. The defect was the domicile criterion.
   - **Madrid:** TSJM 405/2024 of 17 Sep 2024 became final on 15 Apr 2026; Ordenanza 2/2026 has applied since 7 Apr 2026.
   - **Valladolid:** annulled on 16 Mar 2026, not final, and still fining.
   - **Zaragoza:** fining since 12 Dec 2025; Zone 2 from 2030; an episode-only proposal is pending, tied to the 2027 budget.
   - **Vigo:** label B restricted from 2029.
   - **Catalonia:** a permanent label-B ban from 1 Jan 2028 under Decree 132/2024; Barcelona's ordinance amendment has not started.
   - **Barcelona's suspension:** ran from 22 Jan to 13 Mar 2026.
6. **The NAP has not been updated since July 2026, and the datos.gob.es request is still unanswered (19 Oct 2026).**

**Data access**
7. **DGT label data.**
   - The bulk daily file of every plate with its label and the locality of its fiscal domicile is free but **restricted to municipalities with a ZBE registered in DGT 3.0** [new: https://sede.dgt.gob.es/es/vehiculos/tramites-para-administraciones/descarga-de-fichero-zbe-zona-de-bajas-emisiones/].
   - Private firms get only the single-plate web lookup.
   - **Unresolved conflict:** the DGT's label page also refers to a "fichero de distintivos ambientales" in DGT en Cifras, which could not be located.
   - Any idea that needs plate-level labels or domiciles must collect them from customers.
8. **The MITECO packaging register is a public monthly Excel file**, with a web service under development, and **platforms must check sellers' registration numbers before letting them sell** [new: MITECO page].
   - At 30 Sep 2026 it held 66,742 registration numbers and 61,279 NIFs, with 23,349 new numbers in January–September 2026.
   - About 27,000 are foreign (N-prefix) NIFs, and almost no natural persons appear.
   - Relevant to batch 4 (retail, e-commerce, RET-15/16) and to any marketplace-seller idea.
   - It also points to a cross-border EPR service market (foreign marketplace sellers), outside the user's target.
9. **AICA's RCA.**
   - API access is by request for registered buyers.
   - Representation works through a legal representative's Cl@ve certificate, and the Cl@ve gateway is "unstable".
   - Relevant to ADM-07 (custody of company certificates) in batch 2.

**Packaging and food rules**
10. **C-12 (Ley 1/2025): settled.**
    - The final provision reads "entrará en vigor el 2 de enero de 2025", and the art. 6 duties apply one year after the 2 Apr 2025 publication, so from April 2026.
    - Having no plan is grave (€2,001–60,000; the regions define it), and micro firms are exempt.
    - Affects IDEA-37 in batch 4.
11. **Ley 7/2022: failing to register in the Registro de Productores or to report is grave (€2,001–100,000).**
12. **Ecoembes now requires DAE Comerciales as well as DAE Domésticos**, each with an auditor's agreed-procedures report where Ecoembes requires one (deadline 31 May for the prior year).
    - The scheme platforms bundle declaration and registry services.
    - Relevant to any gestoría or auditor-channel idea.

**Market and price anchors**
13. **Cargoffer**, a Spanish TMS and freight marketplace, prices:
    - TMS: €0 for up to 5 vehicles, €99/month for up to 50, €299/month unlimited;
    - DeCA and eCMR documents: €0 for 10 a month, up to €199 for 1,000;
    - route optimisation: €0–29/month.

    **Routal** route planning costs €199/month for 4 vehicles plus €49 per extra vehicle. These are anchors for any fleet or route product (batch 3, IDEA-44 home-help routing) and for batch 1's SME software bill.
14. **74% of Spanish fleets use GPS tracking (77% of small fleets).** Source: Geotab and ABI Research, 2026 Spanish report, a vendor survey. The report never mentions ZBEs.
15. **Fenadismer publicly accused DIA (11 May 2026) of systematically refusing fuel-cost updates.** This is evidence of shipper resistance, relevant to IDEA-02 (batch 1) as the haulage vertical.
16. **Two Valencia Sandbox metrics** for any idea that wants a city pilot (batch 8): 98% of 75 requests authorised and a 90-day average response, with 48 pilots so far (single source, 24 Sep 2026).

---

## 4. Search log

**Total: 22 WebSearch calls** (the limit was 24). By idea: IDEA-48 8; IDEA-47 2 (search 14 is shared with IDEA-48); IDEA-45 3; IDEA-46 2; IDEA-49 3; IDEA-50 2; IDEA-51 2. IDEA-46's convalidation check was answered by direct BOE fetches instead of a search.

| # | Query | Idea and check | Useful result |
|---|---|---|---|
| 1 | València zona de bajas emisiones nueva ordenanza pleno votación octubre 2026 | 48 (a) C-01 | Yes: no vote after Sep 2026; led to the valencia.es items of 25 Feb and 1 Dec 2025 |
| 2 | routing API Spain low emission zones DGT environmental label "ES" sticker PTV OR HERE OR TomTom OR Sygic ZBE | 48 (b)(g)(h) | Partly: no vendor-side DGT semantics found; led to the Cargoffer MCP listing |
| 3 | DeCA documento electrónico de control app transportista precio "al mes" generar QR repositorio | 45 (b)(d) | Yes: DecaFirma, ValenciaportPCS |
| 4 | DeCA herramienta gratuita asociados CETM OR Fenadismer OR UNO OR Ministerio Transportes generador documento de control gratis | 45 (b)(h) | Yes, a negative: no free official or association tool; UNO guide; ICargo |
| 5 | software gestión transporte factura revisión precio combustible automática fórmula Real Decreto-ley 9/2026 TMS transportistas | 46 (b)(g) | Partly: no TMS automation found; led to trans.info on the Ministry calculator |
| 6 | Ecoembes GENCI declaración anual de envases plataforma online adheridos tarifa 2026 cuota por kilo envases comerciales industriales | 49 (b)(h) | Yes: Grant Thornton alert, Ecoembes Comerciales deck, Envalora tariffs |
| 7 | número de productores inscritos sección envases Registro de Productores de Producto MITECO empresas registradas 2025 2026 | 49 (c) | Yes: Alimarket counts; the MITECO page with the register Excel |
| 8 | software declaración anual envases RD 1055/2022 PPWR SaaS empresas precio plataforma cumplimiento envases pymes | 49 (b)(d) | Yes: Envasify, SEIDOR, Ecovidrio |
| 9 | "Registro de Contratos Alimentarios" integración software bodega ERP API inscripción automática contratos uva | 50 (b)(h) | Yes, a negative: no ERP advertising RCA integration (eVins, Solmicro, Uvatec) |
| 10 | plan de abonado RD 1051/2022 herramienta gratuita MAPA cuaderno digital CUE SIEX generar plan de abonado aplicación cooperativas | 51 (b)(h) | Partly: CUE status; led to RD 1051/2022 art. 20 |
| 11 | software plan de abonado asesor fertilización REGFER programa elaborar plan de abonado precio licencia 2026 | 51 (b)(d) | No: irrelevant results |
| 12 | "Sandbox Urbano" València ordenanza aprobación definitiva pleno BOP proyectos admitidos 2025 2026 | 48 (e) | Yes: Pleno of 30 Apr 2024 (provisional); two-year metrics |
| 13 | API consulta distintivo ambiental por matrícula DGT etiqueta medioambiental servicio web empresas flotas | 48 (a)(f) | Yes: DGT label page; Ganvam for fleets |
| 14 | software gestión de flotas zonas de bajas emisiones ZBE alertas furgonetas etiqueta DGT planificador rutas reparto España Webfleet Movertis Routal | 48 (b), 47 (b) | Negative: no Spanish fleet tool with ZBE semantics found |
| 15 | renting multas ZBE identificación conductor tasa gestión multa cliente flota AER número de multas tramitadas renting furgonetas | 48 (c)(d) | Partly: Gesthispania, the Avis sanction, AEA on fees over €60 |
| 16 | app alertas zona de bajas emisiones matrícula aviso cambios normativa ZBE notificaciones vehículo furgoneta autónomos España | 47 (b)(h) | Yes: Google Maps "Z" warnings, Bip&Drive |
| 17 | DeCA denuncias sanciones número inspecciones transporte primeras semanas octubre 2026 Guardia Civil documento de control cifras | 45 (a)(c) | A negative: no official fine counts; trans.info of 9 Oct |
| 18 | vendimia 2026 contratos uva inscripción Registro de Contratos Alimentarios bodegas viticultores AICA antes de la entrega sanciones | 50 (a) | No: only older items |
| 19 | precio localizador GPS gestión de flotas cuota mensual euros por vehículo España furgonetas empresa 2026 | 47 (d), 48 (d) | Partly: no prices; led to the Geotab 2026 Spain report and a vendor list |
| 20 | transportistas aplican revisión precio gasóleo factura encuesta porcentaje cargadores rechazan indexación combustible 2026 Fenadismer CETM | 46 (h) | Partly: the DIA accusation; no survey share |
| 21 | ZBE etiqueta B 2028 Decret 132/2024 modificació ordenança AMB municipis restricció distintiu B tramitació 2026 | 48 (a) C-13 | Yes: the decree's 2026 and 2028 steps; Reus; no amendment found |
| 22 | API datos zonas de bajas emisiones España normativa ZBE desarrolladores flotas consulta vehículo permitido base de datos ZBE empresas | 48 (b)(f) | Yes: the DGT ZBE file is restricted to municipalities |

**Checks left open for lack of searches or access:**
- [S\*] liability and professional-insurance cost for ZBE answers (48);
- the share of Madrid ZBE fines going to companies (47; no city publishes it);
- a machine-readable source of episode declarations (47);
- modelo 592 filer counts (49);
- MITECO enforcement cases (49);
- REGFER adviser counts and SIEX formats (51; MAPA returned 503);
- whether the Holded, Quipu and a3factura APIs support invoice lines (46);
- the depth of Sadler's Spanish city pages (48; they did not render statically).

**Main pages fetched directly (not counted against the budget), all on 23 Oct 2026**
- **ZBE status:**
  - ecomovilidad city pages: Valencia, Málaga, Madrid, Barcelona, Zaragoza, Valladolid;
  - valencia.es news of 25 Feb 2025, 21 Oct 2025 and 1 Dec 2025, and of 30 Apr 2024 (Sandbox);
  - El Español (7 Mar 2026), Motorpasión (22 Oct 2026), Atlántico (10 Sep 2026), El Diario de Madrid (15 Jul 2026);
  - the madrid.es FAQ;
  - the DGT NAP index and Valencia.xml;
  - the datos.gob.es request;
  - zbe.barcelona and bilbao.eus;
  - UNO's ordinances directory;
  - the BOIB Palma notice (BOIB 37/2026; PDF extracted).
- **Sandbox:** sede.valencia.es AE.IN.100; Paréntesis.Media (28 Jun 2026); valencianews (24 Sep 2026).
- **ZBE competitors:**
  - HERE routing docs;
  - TomTom release notes and pricing;
  - PTV low-emission-zones docs;
  - Glama (two listings);
  - zbe.cargoffer.com, cargoffer.com and its pricing page;
  - the Apify actor;
  - the App Store page for ZBE España;
  - urbanaccessregulations.eu (homepage and the UVAR-data page, HTML parsed);
  - Routal pricing;
  - motor.es and androidguias on Google Maps;
  - the revenuebase.ai vendor list;
  - the Geotab 2026 Spain report (PDF extracted).
- **DGT:** the label-lookup page and the ZBE-file page on sede.dgt.gob.es.
- **Haulage:**
  - BOE: RDL 9/2026 record and analysis; BOE-A-2026-9793; RDL 25/2026 (ELI and analysis); BOE-A-2026-21788; Orden TRM/1034/2026; Ley 15/2009 consolidated; BOE daily summaries of 29–30 Sep and 1 Oct 2026;
  - six Fenadismer articles (7 Jul 2024; 10 Sep, 8 Oct, 13 Oct, 15 Oct and 22 Oct 2026);
  - GA-P's DeCA guide;
  - trans.info (11 May, 24 Apr, 9 Oct and 20 Oct 2026);
  - CETM's homepage and calculator page;
  - DecaFirma, Fieldeas, container-news (ValenciaportPCS), Interempresas (Fenaex).
- **Packaging:**
  - the EC packaging and EUDR pages;
  - the MITECO register page and the register Excel (parsed);
  - Alimarket;
  - Cartón Circular;
  - Grant Thornton's alert and the Ecoembes Comerciales deck (PDFs extracted);
  - Envasify pricing and its WordPress plugin page;
  - BOE: Ley 7/2022 arts. 108–109 and Ley 1/2025 final provisions.
- **Food chain and farms:**
  - the AICA RCA FAQ and AICA homepage;
  - the AICA Memoria 2025 (PDF extracted, tables 6, 20–21, 37–40);
  - eVins;
  - RD 1051/2022 consolidated;
  - FertiliCalc, Agroptima pricing, Cooperativas Agro-alimentarias, Interempresas (CUE), Infoagro.
- **Failed fetches:**
  - Astac (503), RACE (404), the MAPA CUE page (503), La Rioja CUE (503), GENCI (401);
  - Ecoembes empresas (403), the Ministry diesel-index page (403), Holded developers (header overflow), npm (403), PTV pricing (404);
  - Bip&Drive (503), the Webfleet pricing guess (404), the G2 seller page (403).
