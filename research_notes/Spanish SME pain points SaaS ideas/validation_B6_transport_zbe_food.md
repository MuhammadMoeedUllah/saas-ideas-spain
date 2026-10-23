# Validation batch 6: transport, low-emission zones (ZBE), packaging and the food chain

*Validator: batch 6. Prepared 23 October 2026. Ideas: IDEA-45, IDEA-46, IDEA-47, IDEA-48 (user idea U3, EcoRoute, full treatment), IDEA-49, IDEA-50, IDEA-51.*

*Method: [F] direct fetches of official, vendor and press pages (unlimited) first, then at most 24 web searches (log in section 4). Citations: [new: URL, date seen or published] for evidence gathered in this batch; [notes: PAIN-ID] for stage-1 evidence. "Single source" marks claims seen in one place only. Political context: Cortes dissolved 6 Oct 2026; general election 29 Nov 2026.*

*Status: work in progress. Sections are appended as each idea is finished.*

---

## 1. Batch summary table

(filled in at the end)

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
- **ZBEs are not top of mind.** The same 35-page Spanish fleet report never mentions ZBEs; its only "bajas emisiones" hit is about EV logistics. That is weak disconfirming evidence.
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
- **City statuses:** as settled in IDEA-48 (a). Nine cities sanction by label or access, and Valencia, Málaga (from 14 Oct 2026), Murcia, Las Palmas, Alicante and Vigo (to 10 Sep 2027) do not [new: sources in IDEA-48 (a); notes: ZBE city table].
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
- **Value at stake (my arithmetic, illustrative).** With C ≈ 0.4 for heavy trucks and a G variation of 44.6%, the revision is about 18% of the base price. A carrier that cannot bill it loses that share of revenue.
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

