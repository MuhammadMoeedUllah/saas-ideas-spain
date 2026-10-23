# ZBE / LEZ compliance in Spanish cities for commercial fleets, vans, trades and delivery partners — rules, enforcement, data and tools (2024–2026)

Research date: 23 Oct 2026. Scope: ZBE compliance operations, enforcement data, data/tools, and three fact-checks. Overlaps: the city track covers ZBEs as one city issue among many; the transport track covers drivers, tachographs and payment terms. They are mentioned here only where they touch ZBE compliance.

Method and reliability notes for the report writer:
- **Primary sources I read in full:** madrid.es (FAQ and Distrito Centro professional page), the DGT directive on ZBE data (ED MOV 2023/01), the BOIB Palma edict of 24/03/2026, the Valencia Sandbox Urbano ordinance text and its procedure page, the DGT 2024 statistical yearbook, and zbe.barcelona.
- **Raw data I checked myself:** the DGT NAP ZBE files (directory listing and six DATEX II XML files downloaded and parsed on 23 Oct 2026) and the catalogue APIs of the Barcelona, Valencia and Málaga open-data portals.
- **Secondary sources:** many city statuses rely on press and on ecomovilidad.es, an aggregator whose city pages say "actualizado en octubre de 2026". It is useful for currency but it is secondary, and it has corrected its own errors in the past.
- **"(snippet-level)"** marks claims I saw only in search-result summaries and did not open. Treat them as single-source and unverified.
- The session's web-search budget ran out before some items could be checked: Google Routes API, PTV, Sygic, fleet-software prices, and Murcia/Granada official pages. These are listed under Gaps.

---

## 1. Legal basis and rollout: obligation, RD 1052/2022, transport-subsidy link, how many municipalities actually fine, court annulments, postponements

### Takeaway
- **The obligation is national, but enforcement is local and patchy.** Ley 7/2021 art. 14 obliges about 150 municipalities (over 50,000 inhabitants, island territories, and over 20,000 when they exceed pollution limits) to have a ZBE since 2023. RD 1052/2022 sets the minimum content, and the State used public-transport subsidies as the stick in 2025 before relaxing it for 2026.
- **Only a minority of obliged municipalities actually fine.** About 56 cities were described as "fully active" in Feb 2026. Only 6 of 23 large Catalan municipalities effectively fined in 2025.
- **Courts have destabilised the largest schemes in 2026.** The Madrid annulment became final in April 2026, with execution proceedings on old fines from July. Málaga's ZBE was annulled in May and fines stopped on 14 Oct 2026. Valladolid's ordinance was annulled in March, but that ruling is not final.

### Cited Findings
**Legal basis**
- **Ley 7/2021 art. 14:** municipalities over 50,000 inhabitants, island territories and municipalities over 20,000 that exceed pollutant limit values "deberán adoptar medidas de mitigación… entre ellas, el establecimiento de una Zona de Bajas Emisiones" (must adopt mitigation measures, including a ZBE). — [DGT, Escrito Directriz MOV 2023/01, signed 2 Feb 2023](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf)
- **RD 1052/2022 (published 27 Dec 2022), art. 10.2:** municipalities must inform the DGT and the regional traffic authority of the ZBE perimeter, hours and permitted vehicles by environmental label "en el plazo máximo de un mes desde su establecimiento" (within one month of establishing it). The DGT then "pondrá dicha información a disposición de navegadores, vehículos y resto de agentes" (will make it available to navigators, vehicles and other actors) via the Punto de Acceso Nacional. — [DGT ED MOV 2023/01, 2 Feb 2023](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf)
- **When the obligation started and what the State has spent:** the obligation applies since 1 Jan 2023, and the Government has allocated more than €1,500M in aid to local entities to accelerate ZBE implementation. — [Diario de Transporte, 4 Jul 2024, modified 11 Aug 2025](https://www.diariodetransporte.com/general/ministerios-y-leyes/transportes-dice-que-los-ayuntamientos-que-no-cumplan-con-las-zbe-no-tendran-ayudas-al-transporte-publico/)
- **Court-made requirement on process:** RD 1052/2022 requires a prior ZBE project. The TSJ Castilla y León annulled Valladolid's ordinance for lacking one (sentencia 281/2026, 16 Mar 2026). — [ecomovilidad.es Valladolid, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/)

**Link to public-transport subsidies**
- **2025 condition.** For 2025 transport aid (RDL 1/2025, title II chapter I), obliged entities had to have an effective ZBE or commit to one during 2025. "Effective" meant a municipal regulation in force with label-based restrictions, access control and monitoring, and an active sanctions regime. A warning-only system did not count, nor did merely approving an ordinance or running pilots. (snippet-level) — [Astrave](https://astrave.com/noticias/subvenciones-transporte-zbe/); [Zarabanda](https://zarabanda.info/transportes-condiciona-las-ayudas-a-entidades-con-zbe/)
- **2025 uptake.** Transportes admitted applications from 141 regions and municipalities for €355M of public-transport discounts (press-release title, 16 Jun 2025; body not opened, snippet-level). — [Ministerio de Transportes](https://www.transportes.gob.es/ministerio/comunicacion/sala-prensa/lun-16062025-1148)
- **2026 relaxation.** The decree-law extending transport aid through 2026 (Council of Ministers 23 Dec 2025, BOE 24 Dec 2025) lets municipalities over 50,000 without a ZBE still access the aid if they implement one during 2026. Valencia's mayor called this "una grata sorpresa" (a pleasant surprise). — [Valencia Plaza, 24 Dec 2025](https://valenciaplaza.com/valenciaplaza/valencia/el-ministerio-de-transportes-alivia-a-catala-le-permite-acceder-a-las-ayudas-pese-a-no-contar-aun-con-una-zbe)
- **Money at stake in Valencia.** €14M of 2026 aid plus €4M from 2025 depend on approving a ZBE in 2026. To keep the 2025 aid, the city argued that the camera-controlled APR (Área de Prioridad Residencial, a residents-priority zone) of Ciutat Vella was a "provisional ZBE". — [El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html)
- **EU funds at risk.** Compromís warned Valencia could have to return up to €115M of EU funds (€57.8M received plus an equal penalty). — [Valencia Plaza, 24 Dec 2025](https://valenciaplaza.com/valenciaplaza/valencia/el-ministerio-de-transportes-alivia-a-catala-le-permite-acceder-a-las-ayudas-pese-a-no-contar-aun-con-una-zbe)

**How many obliged municipalities enforce with fines (no official count exists)**
- **National press tally.** ZBEs affect 45.5% of the population, potentially 66% in 2026, or about 33M people in 151 municipalities. 56 cities have "fully active" ZBEs and 89 more are in the approval phase. The article does not say how many fine. — [Motor16, 16 Feb 2026](https://www.motor16.com/las-ultimas-noticias/zbe-ciudades-multas-coches/)
- **Transport-sector figure.** Fenadismer and Astac cite 149 affected municipalities, "aunque solo algunas ciudades" (only some cities) have implemented zones. — [Fenadismer, 7 Jul 2024](https://www.fenadismer.es/los-transportistas-ya-pueden-consultar-todas-las-zonas-de-bajas-emisiones-en-una-sola-web/)
- **Catalonia audit.** The Sindicatura de Comptes de Catalunya found that only 6 of 23 municipalities over 50,000 with a ZBE effectively applied fines in 2025:
  - The six are Barcelona, Cerdanyola, El Prat, Sant Boi, Sant Cugat and Viladecans, all in the Barcelona area.
  - Badalona, Granollers, Lleida, Mollet del Vallès and Terrassa imposed none, and Badalona has a sanctions moratorium until 1 Jan 2027.
  - Only 4 of the 23 ZBEs had a fully executed communication plan.
  - Source: [Metrópoli Abierta, 10 Sep 2026](https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html)
- **Comunitat Valenciana audit.** None of the 15 municipalities over 50,000 had a ZBE operating by 31 Mar 2025 (Sindicatura de Comptes valenciana; snippet-level). — [À Punt](https://www.apuntmedia.es/noticies/politica/15-municipis-valencians-50-000-habitants-va-implantar-zona-baixes-emissions-2023_1_1832698.html)
- **Aragón audit.** The Cámara de Cuentas de Aragón warns of a generalised ZBE delay (snippet-level). — [Demócrata](https://www.democrata.es/ca/aragon/la-cambra-de-comptes-d-arago-alerta-d-un-retard-generalitzat-a-les-zones-de-baixes-emissions/)
- **National data feed.** The DGT NAP lists 45 ZBE resources (46 XML files) as of 23 Oct 2026. The list includes zones that do not fine, such as Valencia and Alicante. — [NAP DGT dataset](https://nap.dgt.es/es/dataset/zonas-de-bajas-emisiones); [NAP file index](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/)

**Court annulments (verified)**
- **Madrid.** The TSJM annulled part of the Ordenanza de Movilidad Sostenible (Madrid 360) for an inadequate economic-impact report, after an appeal by Vox.
  - Ruling date: sources disagree between Sept, Oct and Dec 2024.
  - On 15 Apr 2026 the Tribunal Supremo inadmitted the city's cassation appeal (casación 8840/2024), making the annulment final. It did not rule on the merits. One source gives 17 Apr.
  - Sources: [Infobae, 21 Apr 2026](https://www.infobae.com/espana/2026/04/21/el-tribunal-supremo-confirma-la-anulacion-parcial-de-la-zona-de-bajas-emisiones-en-madrid-al-rechazar-el-recurso-del-ayuntamiento/); [ecomovilidad Madrid, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/comunidad-de-madrid/madrid/); [Xataka, 27 Apr 2026](https://www.xataka.com/movilidad/madrid-cobro-650-millones-euros-multas-zbe-supremo-le-da-razon-a-conductores-dinero-no-vuelve)
- **Madrid's replacement ordinance.** Ordenanza 2/2026 was approved by the Pleno on 24 Mar 2026, published 6 Apr 2026, and its new transitional regime applies from 00:00 on 7 Apr 2026. The city says all ZBEs remain in force. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)
- **Madrid execution proceedings (July 2026).** The TSJM opened a separate enforcement proceeding (pieza separada de ejecución) on AEA's motion and gave the parties 20 days to respond.
  - Scope dispute: the city says the annulment covers only Distrito Centro and Plaza Elíptica. Juzgados nº 15, 29 and 34 have annulled €200 fines on any ZBE street.
  - AEA estimates more than 3.4M sanction files worth more than €663M, for complaints up to 31 Dec 2025.
  - The city says "no procede devolver las multas" (refunds are not due).
  - Source: [El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)
  - Vox separately asked for "ejecución forzosa" (forced execution). — [Merca2, 22 Jul 2026](https://www.merca2.es/2026/07/22/anulacion-zbe-multas-tsj-madrid-2422278/)
- **Barcelona.** The 2019 ordinance was annulled by the TSJC in Mar 2022, and the Supreme Court confirmed this in Nov 2023. The current ordinance (approved 27 Jan 2023) was upheld by the TSJC in two rulings of 24 Nov 2025, which can still be appealed in cassation. — [ecomovilidad Barcelona, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [Metrópoli Abierta, 13 Jan 2026 (title)](https://www.metropoliabierta.cat/mobilitat/20260113/justicia-avala-zona-baixes-emissions-barcelona-blinda-implantades-municipis-lamb/1003742722915_0.html)
- **Barcelona-area challenges.** Vox announced appeals against the ZBEs of seven Barcelona-area municipalities and the AMB metropolitan mobility plan. — [Merca2, 22 Jul 2026](https://www.merca2.es/2026/07/22/anulacion-zbe-multas-tsj-madrid-2422278/)
- **Málaga.** TSJA sentencia 896/2026 of 6 May 2026 annulled articles 9–24 of the mobility ordinance, the ZBE chapter. Fines stopped on 14 Oct 2026, the city will not appeal, and finality is expected around 25 Nov 2026.
  - Sources: [ecomovilidad Málaga, 22 Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/); [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
  - Conflict on the reason: Motorpasión says the rules were declared discriminatory because they sanctioned only vehicles not domiciled in the city. Ecomovilidad's summary says the court rejected the challenge to the tax-domicile criterion. Treat the legal reasoning as unverified until the ruling text is read.
- **Valladolid.** The TSJCyL annulled the ordinance on 16 Mar 2026 for procedural reasons. The ruling is not final and the city keeps fining. On 28 Jul 2026 the Junta de Gobierno approved the first step toward a new ordinance. — [ecomovilidad Valladolid, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/)
- **Bilbao.** The RACVN and Liberum appealed the ordinance before the Basque high court (TSJPV), as published in BOB nº 147 of 5 Aug 2025. No ruling had been published as of Oct 2026. — [ecomovilidad Bilbao, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/)
- **Other regions.** Several regional high courts (TSJ of Cataluña, Madrid, Asturias, Extremadura and Castilla y León) have annulled ZBEs in other localities (snippet-level). — [DVuelta](https://www.dvuelta.es/en-los-medios/noticias-sobre-dvuelta/espana-sentencias-contra-zonas-bajas-emisiones)

**Postponements, suspensions and moratoria (2025–2026)**
- **Valencia.** The Pleno rejected final approval of the ordinance on 28 Oct 2025 (19 votes against from Compromís, PSPV and Vox; 13 in favour from PP). No new vote took place between Jan and Sep 2026, so there is no ZBE and no fines. — [ecomovilidad Valencia, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/)
- **Vox's condition in Valencia.** "Aprobaremos… ZBE sin régimen sancionador" (we will approve a ZBE without a sanctions regime). — [El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html)
- **Barcelona emergency suspension.** The Rondes ZBE was suspended from 22 Jan 2026 because of the Rodalies commuter-rail crisis and resumed normal service on Monday 16 Mar 2026 ("El dilluns 16.03.2026 la ZBE entrarà en servei amb normalitat"). — [zbe.barcelona](https://www.zbe.barcelona/); [ecomovilidad Barcelona](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/) (gives 13 Mar as the last suspended day)
  - Cause: the fatal Gelida R4 accident and network shutdown (snippet-level). — [Catalan News](https://www.catalannews.com/society-science/item/rodalies-rail-services-resume-gradually-after-two-day-shutdown)
- **Vigo.** The ordinance is in force from Sept 2026, but phase 1 is information-only until 10 Sep 2027, with no restrictions or fines. — [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)
- **Alicante.** The ordinance is in force but under an open-ended moratorium (art. 4.3): offenders receive only informational notices. — [ecomovilidad Alicante, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/alicante/alicante/)
- **Madrid residents.** The warning period for unlabelled ('A') vehicles not banned before 2025 was extended to 31 Dec 2026, and from 7 Apr 2026 it no longer applies to vehicles covered by the new transitional regime. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD)
- **Molina de Segura.** The sanctions regime is suspended until 3 Jan 2028, per its municipal website (snippet-level). — [Molina de Segura](https://movilidad.molinadesegura.es/zona-de-bajas-emisiones/)

### Inferences
- **Fining municipalities are probably about a third of the obliged ones.** Combining Motor16's 56 "fully active" ZBEs, the Catalan ratio of 6 effective enforcers in 23, and my 16-city tally (about 9 fining by label or access in Oct 2026, see section 2), probably no more than roughly 50 of the about 150 obliged municipalities actually fine. This is an estimate and needs a proper census.
- **The subsidy stick was blunted for 2026.** The 2025 "effective ZBE with sanctions" condition pushed cities to switch on cameras. The 2026 relaxation removes much of that pressure, so expect more "paper ZBEs" without sanctions (Alicante, Valencia's proposed Vox model, and Sevilla's and Castellón's episode-only models).
- **Rules can flip within days.** The dominant legal risks are procedural (missing economic report or prior project) and equality (residence or domicile criteria). Several cities that exempt residents or locally taxed vehicles (Granada, Madrid's resident regime, Palma's resident authorisations) may face the same challenge that sank Málaga's regime. Rules can change at short notice, which argues for a versioned, legally monitored rules database.

### Gaps
- No official national register of which municipalities fine, since when, and how many fines. The Ministry has not answered a public data request (see section 4).
- I could not open the BOE texts of RDL 1/2025 or of the Dec 2025 decree-law to confirm their article numbers. The 2025 "effective ZBE" criteria above are snippet-level.
- The exact date of the TSJM ruling (Sept, Oct or Dec 2024) and the legal reasoning in Málaga's TSJA 896/2026 remain unverified.

---

## 2. City-by-city detail (16 cities): sanctions start, enforcement, fines, labels, vans/trucks, professional exemptions, foreign/exempt vehicle registration, loading and unloading (DUM)

### Takeaway
- **Nine of the 16 cities sanction ZBE access in Oct 2026:** Madrid, Barcelona, Sevilla-Cartuja, Zaragoza, Bilbao, Palma, Valladolid, Granada, Córdoba, plus A Coruña with an access-control (non-label) model.
- **Six do not:** Málaga (stopped 14 Oct 2026 after annulment), Valencia (no ordinance), Murcia (no ordinance), Las Palmas (consultation only), Alicante (moratorium, notices only) and Vigo (information-only until Sept 2027).
- **Rules for vans differ fundamentally between cities.** Madrid lets unlabelled vans and trucks circulate outside its special zones only while NO2 limits hold. Barcelona bans unlabelled vehicles of every type on weekdays 7–20h. Málaga gave N1 vans an extra four-year transition. Valencia's draft restricted only cars and motorcycles.

### Cited Findings

#### Per-city table (status as of 23 Oct 2026)

| City | ZBE status (Oct 2026) | Fines started / will start | Enforcement | Fine | Restricted labels / vehicles | Vans (N1) & trucks (N2/N3) | Professional exemptions / permits (and how) | Open data | Key sources |
|---|---|---|---|---|---|---|---|---|---|
| **Madrid** | In force. OMS amended by Ordenanza 2/2026 (Pleno 24 Mar 2026, in force 7 Apr 2026). TSJM enforcement proceedings over old fines ongoing. | AEA counts fines from Sept 2021 (stage dates not verified) | OCR cameras and "foto rojo" (red-light camera) devices | €200 (€100 early payment) | Unlabelled cars not domiciled in Madrid since 1/1/2022 are banned. Unlabelled cars on Madrid's tax roll continuously since 1/1/2022 may circulate while NO2 limits are met (outside the special zones). Unlabelled vehicles excluded from Distrito Centro and Plaza Elíptica. | Unlabelled non-cars (vans, trucks, motos) may circulate on ZBE roads outside the two special zones regardless of domicile, but only while NO2 limits are met at all stations, and not on pollution-episode days. If limits are breached, the Junta de Gobierno ends the regime and fines start 6 months after BOCM publication. **Distrito Centro:** light (≤3.5t) B banned since 1/1/2024; heavy (3.5–18t) B banned since 1/1/2025; C 7–15h; ECO 7–21h; Cero 24h. | Light vehicles need IAE (business tax) registration and pre-registration in the Sistema de Gestión de Permisos via Mi Carpeta or by appointment at C/ Bustamante 16; heavy vehicles are handled de oficio. Rented or leased vehicles need the contract; replacement vehicles need a repair order. Night window 23–7h in listed pedestrian streets and 5–7h for food supply, both by declaración responsable valid 1 year with proof of deliveries. Exceptional authorisation for unlabelled vans and trucks of autónomos aged 59+ with ≥50% of the fleet unlabelled, renewed yearly. Foreign vehicles follow the same rules. | NAP Madrid.xml (7 MB). Geoportal: WMS/REST only, no vector download. | [FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [DC professionals](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD); [Geoportal](https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/dataset.iam?id=7e9120c8-881e-11ed-8764-34298f78123d); [NAP](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/Madrid.xml) |
| **Barcelona (AMB "ZBE Rondes")** | In force. 2023 ordinance upheld by the TSJC on 24 Nov 2025. Suspended 22 Jan–16 Mar 2026 (Rodalies crisis). | Cars and motos: 15 Sep 2020. Vans: 1 Apr 2021. Trucks: after the 2021 commitments (renew by Jun 2022). | ANPR cameras on the perimeter (commercial source); foreign vehicles checked against a plate registry | €200, €260 during a declared pollution episode | Unlabelled vehicles of all types, Mon–Fri 7–20h. Label B banned during pollution episodes since 1/1/2026 (Iberfurgo). Catalan Decree 132/2024 requires restricting B before 1/1/2028. | Same rule as cars: unlabelled vans and trucks are barred on weekdays 7–20h. | 24 daily passes per year after registering in the AMB Registre metropolità. Low-income households (under 2× IPREM, the public income index): annual authorisation. Professionals within 5 years of retirement: until 31 Mar 2028. Foreign vehicles: prior AMB registry authorisation valid up to 2 years. | Open Data BCN "zbe-ambit" (perimeter GPKG from 2023). NAP files RondasDeBarcelona.xml and Barcelona.xml. | [ecomovilidad BCN](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/); [Ajuntament 15 Sep 2020](https://ajuntament.barcelona.cat/premsa/2020/09/15/entra-en-vigor-el-regim-sancionador-de-la-zona-de-baixes-emissions-per-a-turismes-i-motocicletes/); [17 Mar 2021](https://ajuntament.barcelona.cat/premsa/2021/03/17/el-31-de-marc-finalitza-la-moratoria-de-la-zbe-rondes-bcn-per-a-les-furgonetes-a-les-quals-no-els-correspon-letiqueta-ambiental-de-la-dgt/); [10 Dec 2021](https://ajuntament.barcelona.cat/premsa/2021/12/10/els-transportistes-que-es-comprometin-a-canviar-de-vehicle-en-6-mesos-podran-circular-durant-aquest-temps-sense-distintiu-ambiental-per-la-zona-de-baixes-emissions/); [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/zbe-ambit) |
| **Valencia** | **No ZBE in force.** Final approval rejected 28 Oct 2025; no new vote by Sep 2026. Camera-controlled APR Ciutat Vella (access control, not by label) argued to be a "provisional ZBE". | None. The draft had fines from Dec 2025 for vehicles from outside the province and for all unlabelled vehicles from 2028; both now moot. | Draft: 278 cameras over 27.8 km². Installed cameras only count accesses for statistics. | Draft: €200 | Draft: unlabelled cars, motorcycles and mopeds only. | Draft did **not** restrict vans or trucks (per NAP description). | n/a | Valencia open data "Zona de Bajas Emisiones" (GeoJSON, SHP, WFS, KMZ): perimeter of the provisionally approved ordinance. NAP Valencia.xml says "active" from 1 Jun 2026 (contradicts press, see section 4). | [ecomovilidad VLC](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/); [El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html); [VLC open data](https://opendata.vlci.valencia.es/dataset/zona-de-bajas-emisiones); [NAP](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/Valencia.xml) |
| **Sevilla** | In force for Isla de la Cartuja only, by resolutions rather than an ordinance (BOP 245/2022, 301/2022, 64/2024). Public consultation on a city ordinance opened 8 Jun 2026 (episode-only restrictions proposed). | Camera information phase from 8 Jan 2024; fines from Jul 2024 | Automatic cameras (16 control points per a fleet guide, snippet-level) | €200, no points | Unlabelled vehicles, weekdays 7–19h | No van-specific rule found | Residents (Tipo A) and garage holders (Tipo B) accredited at the Triana district office. Company vehicles located in the ZBE use form Modelo M022. 10 one-off accesses per month via the municipal app (snippet-level). | NAP SevillaCartuja.xml | [ecomovilidad Sevilla](https://ecomovilidad.es/zonas-de-bajas-emisiones/sevilla/sevilla/); [Evenergia](https://evenergia.com/blog/zona-de-bajas-emisiones-sevilla/) |
| **Zaragoza** | In force: ZBE Casco Histórico (BOPZ 192, 21 Aug 2024). ZBE Centro (zone 2) from 1 Jan 2030. | 12 Dec 2025 | Plate readers | €200 (€100) | Unlabelled vehicles, Mon–Fri 8–20h | Vans with B label restricted and need a DUM (goods-distribution) authorisation, per a van-rental site (unverified, snippet-level) | Up to 8 accesses per month for registered unlabelled vehicles. Company vehicles with a resident card. Foreign plates not in the DGT register are on the exemption list. | **Not in NAP.** Municipal ZBE dataset not verified. | [ecomovilidad Zaragoza](https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/); [Somoselectricos, 11 Dec 2025 (title)](https://www.somoselectricos.com/normativa-coches-electricos/zaragoza-zbe-restricciones-multas-excepciones-2025-2026/20251211115000037500.html) |
| **Málaga** | **Annulled** by TSJA 896/2026 (6 May 2026; not yet final). Fines stopped 14 Oct 2026; new ordinance to be drafted. | Fines ran from 30 Nov 2025 until stopped on 14 Oct 2026 | 53 control points, 97 cameras | €200 (€100) | Annulled regime: unlabelled vehicles not fiscally domiciled in Málaga (from 30 Nov 2025). B-labelled non-domiciled vehicles were due from 30 Nov 2026 (moot). 437 ha, 24/7. | N1 vans had a 4-year longer transition | Not found | datosabiertos.malaga.eu perimeter GeoJSON (2024) plus sensor datasets. NAP Malaga.xml still "active". | [ecomovilidad Málaga, 22 Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/); [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero); [Málaga open data](https://datosabiertos.malaga.eu/dataset/sistema-de-informacion-cartografica-zona-bajas-emisiones) |
| **Bilbao** | In force since 15 Jun 2024 (BOB 100, 24 May 2024). TSJPV appeal pending. | 15 Sep 2024 | Plate readers; no visible label needed | €200 (€100) | Unlabelled vehicles banned. B restricted since 15 Jun 2025, with transitional exemptions (garage, resident parking, local commerce, rotation car parks, taxi, invitations) until 31 Dec 2029 at the latest. From 1 Jan 2030 only Cero, ECO and C. Abando and Indautxu, about 2 km², weekdays 7–20h. | No van-specific rules found beyond the invitations and commerce exemptions | Invitations: businesses and residents up to 6 per month (people over 70: 16), plate notified up to 2 days after access. Foreign vehicles must register in the Registro de Vehículos Extranjeros (country, fuel, first-registration date), and foreign B-equivalents need prior registration to use exemptions. | NAP Bilbao.xml (weekday 07:00–20:00). Bilbao Open Data portal (no ZBE dataset verified). | [ecomovilidad Bilbao](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/); [bilbao.eus foreign vehicles](https://www.bilbao.eus/cs/Satellite?c=Page&cid=1279235266667&language=es&pageid=1279235266667&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal); [bilbao.eus ZBE](https://www.bilbao.eus/cs/Satellite?cid=1279231359138&language=es&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal) |
| **Palma** | In force since 22 Dec 2024 (ordinance BOIB 167, 21 Dec 2024). Annex 2 authorisations revised by BOIB 37 of 24 Mar 2026. | 1 Jul 2025, after a sanctions moratorium from 22 Dec 2024 | ANPR cameras (snippet-level: 16 cameras) | €200 (+30% for repeat offences, snippet-level) | Until 31/12/2026: unlabelled banned. From 1/1/2027: only C, ECO, Cero. From 1/1/2030: only ECO, Cero. | Light vans follow the same Euro thresholds as cars. Until 2026: petrol Euro 3+ and diesel Euro 4+. 2027–29: petrol Euro 4+ and diesel Euro 6. Goods-delivery vans reportedly exempt (COPE 2025, unverified). | Foreign vehicles must register **5 calendar days before access** with passport/NIE, a technical sheet showing the Euro norm, registration certificate, proof of ownership (leasing contract if applicable) and a ferry or flight ticket. The permit lasts 30 days; foreign vehicles of ZBE residents get up to 6 months. Fines on foreign plates were the first category of complaints after fines started. | NAP Palma.xml (published 7 Jan 2025, before fines started) | [BOIB 37, 24 Mar 2026](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590); [COPE, 25 Jun 2025](https://www.cope.es/emisoras/illes-balears/baleares/mallorca/noticias/multas-vista-palma-son-vehiculos-seran-sancionados-partir-1-julio-circulan-zbe-20250625_3176002.html) |
| **Murcia** | **No ZBE in force.** Technical project approved by the Junta de Gobierno in Dec 2025; ordinance not approved or published (snippet-level). | None | n/a | n/a | None (only occasional episode or pedestrian-zone measures) | n/a | n/a | Not in NAP | [ecomovilidad Murcia (snippet-level)](https://ecomovilidad.es/zonas-de-bajas-emisiones/region-de-murcia/murcia/) |
| **Alicante** | Ordinance in force since late Jan 2025 (final approval 30 Dec 2024, BOP 5 of 9 Jan 2025), but under an open-ended moratorium | None: informational notices only | Not stated | Up to €200, +30% for repeat offences (once applicable) | Not label-based. Only Anillo I (Casco Antiguo, about 0.16 km²) is restricted, to authorised vehicles. Anillos II and III are monitoring only, with extra restrictions possible in pollution episodes. | Not covered | Residents and owners of homes or garages in Anillo I. City confirmed on 27 Jul 2026 that only the Casco Antiguo regime applies. | NAP Alicante.xml | [ecomovilidad Alicante](https://ecomovilidad.es/zonas-de-bajas-emisiones/alicante/alicante/); [Alicante Plaza (title)](https://alicanteplaza.es/pp-vox-pactan-regulacion-zbe-alicante-sin-multas) |
| **Valladolid** | 2024 ordinance applies. Annulled by the TSJCyL on 16 Mar 2026 (not final); city still fines; new ordinance in preparation. | Unlabelled vehicles barred from 30 Jun 2025, per ecomovilidad. The NAP record start is 28 Feb 2025 (fine-start date unconfirmed). | Not stated | €200 | Unlabelled vehicles. B planned from 31 Dec 2027 and C from 1 Jan 2030 (date-based phases appear only as free text in the NAP). | No van-specific rule found | Companies and autónomos operating inside the zone, repair services, low income (under 1.3× IPREM), funeral, removals and towing | NAP Valladolid.xml | [ecomovilidad Valladolid](https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/) |
| **Vigo** | Ordinance in force from Sept 2026 in 4 areas (Centro, Praza de Portugal, Bouzas, O Calvario; 6.7 km²) | **10 Sep 2027.** Phase 1 is information only. | 74 rear-plate-reading cameras in the ZBEs (plus 12 in tunnels); 7 AI traffic-counting meters | About €200 expected (snippet-level) | From 10 Sep 2027 unlabelled vehicles (about 62,100) barred. B (57,934) restricted from 2029. C (79,740) warnings from 2031. From 10 Sep 2032 only ECO and Cero. | Not covered | Permanent exemption for companies and autónomos based inside the ZBEs; residents, taxis, car parks and hotels | **Not in NAP** | [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html); [Atlántico, 12 Oct 2026 (title)](https://www.atlantico.net/vigo/74-camaras-inteligentes-vigilan-zonas_1_20261012-4447769.html) |
| **A Coruña** | ZBE Centro in force since Oct 2025 (OMS, BOP 185 of 29 Sep 2025): Ciudad Vieja, La Marina, Parrote, Pescadería | Fines for unauthorised access (date not verified) | "Automatic access control" (cameras not named explicitly) | €200, no points | **Not label-based:** only authorised vehicles enter; even Cero or ECO vehicles cannot enter without authorisation | Loading and unloading 6–11h (5–12h for Cero and ECO) | Authorisation regime for residents and services | NAP ACoruña.xml | [ecomovilidad A Coruña](https://ecomovilidad.es/zonas-de-bajas-emisiones/la-coruna/la-coruna/) |
| **Las Palmas de G.C.** | **No ZBE.** Prior public consultation 18 Sep–8 Oct 2026; candidate zone Alcaravaneras. | None | n/a | €200 under traffic law once in force | Not yet defined | n/a | n/a | Not in NAP | [ecomovilidad Las Palmas](https://ecomovilidad.es/zonas-de-bajas-emisiones/las-palmas/las-palmas-de-gran-canaria/) |
| **Córdoba** | In force since 18 Feb 2023 (ordinance BOP 33 of 17 Feb 2023). The ZBE is the ACIRE (restricted-access) historic centre. | Fine regime in force (exact start date not stated) | Not stated | €200, no points | 24h. Cero and ECO enter freely. B and C only to reach car parks. Unlabelled vehicles need an exemption or authorisation. | Home delivery and business suppliers exempt; construction firms working inside exempt | Removals, cash transport, tow trucks, workshops, hotels, PMR (reduced-mobility) card holders. No registration procedure described. | **Not in NAP** | [ecomovilidad Córdoba](https://ecomovilidad.es/zonas-de-bajas-emisiones/cordoba/cordoba/) |
| **Granada** | In force (municipal ordinance). Information phase from 1 Apr 2025. | 1 Oct 2025 | ANPR cameras at all accesses (snippet-level) | €200 (€100) | Unlabelled vehicles **without tax domicile in Granada** (both conditions); B, C, ECO and Cero free; 24/7; 23.55 km² | Unlabelled vehicles doing loading and unloading can be exempt via a standard form unless they hold a city loading card or a Ministry goods-transport authorisation (snippet-level) | Workers earning under the IPREM-based threshold of €16,800, by declaración responsable plus employment contract. Pharmacies, hospitals, workshops, courts by form. Parking over 1 hour in the 36 public car parks counts as exempt. | NAP Granada.xml (465 KB). movilidadgranada.com returned 503. | [Xataka, 2 Oct 2025](https://www.xataka.com/movilidad/granada-multa-hoy-su-nueva-zona-bajas-emisiones-quienes-pueden-acceder-multas-excepciones); [ecomovilidad Granada (snippet-level)](https://ecomovilidad.es/zonas-de-bajas-emisiones/granada/granada/) |

#### Additional city notes
- **Madrid, older-autónomo authorisation.** It covers industrial vehicles over 3,500 kg, buses, vans and trucks with no label. The applicant must be a self-employed person aged 59+ on 1 Jan 2025, or a sole-shareholder company whose owner is 59+. At least 50% of the fleet must be unlabelled and owned before 1 Jan 2025. It is granted per calendar year until retirement. Documents: fleet list with labels, insurance and ITV (roadworthiness test), and a sworn statement of urgent need. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD)
- **Madrid, Distrito Centro night deliveries.** Distribution in listed pedestrian streets (e.g., Montera, Puerta del Sol, Preciados, Fuencarral) at 23:00–07:00 requires a declaración responsable that cites Decreto nº 178 (acoustic protocol for loading and unloading) and attaches proof of deliveries (invoices, delivery notes or route records). It is valid one year. Food supply to markets and fresh-food shops is allowed 05:00–07:00 under the same procedure. Registering in the permits system "no autoriza el acceso fuera de las franjas horarias" (does not authorise access outside the time windows). — [madrid.es DC professionals](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD)
- **Madrid, the earlier van moratorium headline.** A Jan 2026 article described a "moratoria específica para distribución urbana todo 2026" for unlabelled vans and trucks, with no legal citation. — [Autopista, 27 Jan 2026](https://www.autopista.es/noticias-motor/moratoria-vehiculos-sin-etiqueta-en-madrid-plazos-condiciones-ecn_322002_102.html). The official rule since 7 Apr 2026 is the NO2-conditional transitional regime above. Fenadismer had applauded a one-year extension of the moratorium in Dec 2025 (snippet-level). — [Ruta del Transporte](https://www.rutadeltransporte.com/noticias-transporte/fenadismer-aplaude-la-moratoria-de-la-entrada-en-vigor-de-toda-la-zbe-en-madrid.html)
- **Barcelona, fine history.** The 2020 fine schedule under the annulled 2019 ordinance was €100 for cars and vans (€200 during episodes) and €200 or €500 for heavy vehicles. — [Ajuntament, 15 Sep 2020](https://ajuntament.barcelona.cat/premsa/2020/09/15/entra-en-vigor-el-regim-sancionador-de-la-zona-de-baixes-emissions-per-a-turismes-i-motocicletes/). Current sources give €200, or €260 during episodes. — [ecomovilidad, Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/). Treat the current amounts as two-source but secondary.
- **Barcelona, 2028 B-label ban and its scope.** From 1 Jan 2028 B vehicles are to be vetoed from ZBEs of municipalities over 50,000. The affected B group covers petrol cars and vans from 2001–2005, diesel cars and vans from 2006–2013, and goods vehicles registered from 2006. B vehicles are 12% of vehicles in Barcelona (13.7% of cars). — [NacióDigital, 28 Apr 2026, updated 16 Jul 2026](https://naciodigital.cat/impacte/ciutats/les-zbe-de-larea-de-barcelona-senduriran-el-2028.html)
- **Barcelona, rental vehicles.** Rental companies pass ZBE fines to the customer who was driving. — [Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/)
- **Málaga, fines and refunds.**
  - 46,562 fines in total: about 35,450 between Dec and May and 11,105 in Jun–Jul.
  - 13,694 fines already paid (about €1.38M) will be refunded ex officio after the ruling is final, and the remaining 32,868 are suspended.
  - The city says refunds "puede dilatarse hasta cuatro años" (could take up to four years).
  - Source: [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
- **Palma, compliance rate.** Cameras detected only 1.8% of vehicles without a label in 2025 (snippet-level). — [Mallorca Diario](https://www.mallorcadiario.com/palma-activa-multas-zona-de-bajas-emisiones-1-julio-2025)
- **Vigo, the city's stance.** "Seguimos en la línea de que nadie tenga que cambiar su vehículo por las ZBE" (we still aim for nobody having to change their vehicle because of the ZBE). — [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)

### Inferences
- **For a fleet, the decision is not "label X is allowed".** It is a function of label × vehicle category (car vs N1/N2/N3) × MMA × domicile or tax roll × time window × day type (working day, holiday, pollution episode) × permit held (registry entry, invitation, daily-pass quota) × purpose (loading and unloading, access to a car park). No public source encodes all of these. That is the core opening for a rules engine.
- **Two models coexist.**
  - *Label-and-time models:* Barcelona, Bilbao, Zaragoza, Sevilla and Palma.
  - *Authorisation or "whitelist" models:* A Coruña, Alicante Anillo I and Madrid Distrito Centro. In these, even a zero-emission vehicle needs prior registration.
  - A compliance product must handle both kinds of state: vehicle attributes and permit state.

### Gaps
- Official pages for Granada (movilidadgranada.com returned 503), Murcia, Sevilla and Zaragoza were not read directly. Their entries rely on press or ecomovilidad.
- No city-level data on fines broken down by vehicle type (van vs car) or by owner type (company vs individual) was found.
- I found no evidence on DUM or loading-zone apps per city (e.g., Barcelona's loading-zone app) within the ZBE context. I did not check this in-session.

---

## 3. Business impact: commercial vehicles without a label or with label B, fines issued to businesses, fleet-renewal costs and aid, complaints from autónomos and associations

### Takeaway
- **Spain's commercial fleet is old.** The DGT counts 2.74M vans (furgonetas), of which 1.08M (39.6%) are 20 or more years old, and 2.46M trucks (camiones), of which 1.02M (41.5%) are 20 or more years old. Diesel vehicles registered before 2006 carry no DGT label, so much of this stock cannot enter label-restricted zones. The DGT's public yearbook does not break vans or trucks down by label.
- **Fine volumes are large but not split by business vs individual.** Madrid issued about 3.3–3.4M fines (€650–663M) between 2021 and 2025, per AEA. Málaga issued 46,562 in under a year.
- **Renewal aid is uncertain in 2026.** The MOVES III page shows N1 aid of up to €7,000 (€9,000 with scrapping), but its application deadline reads 31 Dec 2024.

### Cited Findings
**Fleet size and age (DGT)**
- **Vans by age (DGT Anuario Estadístico General 2024, table 72).** 2,741,010 vans in total:
  - up to 4 years: 464,811
  - 5–9 years: 508,417
  - 10–14 years: 273,555
  - 15–19 years: 409,550
  - 20 years and over: 1,084,677
  - Source: [DGT Anuario 2024](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)
- **Trucks by age (table 80).** 2,462,425 trucks in total, including 1,566,817 with payload up to 999 kg:
  - 15–19 years: 648,032
  - 20 years and over: 1,021,451
  - Source: [DGT Anuario 2024](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)
- **Fleet by label exists only for cars and motorcycles.** The yearbook publishes label breakdowns only for passenger cars (table 82) and motorcycles (table 83). Cars in 2024: 5,632,122 unlabelled, 7,562,866 B, 9,919,978 C, 1,707,385 ECO and 422,180 Cero, i.e. about 22% unlabelled. — [DGT Anuario 2024](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)
- **An interactive DGT panel exists.** It filters the active fleet by vehicle type and label down to municipality level (not queried here). — [DGT Panel de datos del parque](https://www.dgt.es/menusecundario/dgt-en-cifras/dgt-en-cifras-resultados/dgt-en-cifras-detalle/Panel-de-datos-del-parque-de-vehiculos/)
- **Label thresholds for vans.** Light vans get B if petrol from Jan 2001 or diesel from 2006, and C if petrol from 2006 or diesel from 2014. Vehicles below the B thresholds get no label. — [Umivale safety sheet citing DGT](https://umivale.es/dam/umivale-activa/prevencion-y-salud/seguridad-vial/Ficha-Seguridad-Vial-n-51-Distintivos-ambientales2.pdf); [NacióDigital, 28 Apr 2026](https://naciodigital.cat/impacte/ciutats/les-zbe-de-larea-de-barcelona-senduriran-el-2028.html)
- **Share of vans and trucks without a label.** More than half of registered vans and trucks lack a label in every type of area, and in large cities about 2 in 5 vans still have none. This cites an unnamed DGT analysis, so confidence is low. — [Ecoticias, 24 Jan 2024](https://www.ecoticias.com/co2/etiquetas-ambientales-dgt)
- **Average van age.** 14.8 years in the 2025 IDEAUTO/ANFAC report (snippet-level), up from 14.4 years in the 2023 report. — [ANFAC 2023 note](https://anfac.com/wp-content/uploads/2024/02/20240229-NP-ANFAC-Envejecimiento-del-parque-2023.pdf) (2023 figure); 2025 figure snippet-level via the search summary.
- **Local scale example (Vigo).** About 62,100 unlabelled, 57,934 B and 79,740 C vehicles are affected in successive phases. — [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)

**Fines (no split by business vs individual found)**
- **Madrid (AEA, an interested drivers' association).** More than 3.3M ZBE fines worth more than €650M between Sept 2021 and Nov 2025. — [Xataka, 27 Apr 2026](https://www.xataka.com/movilidad/madrid-cobro-650-millones-euros-multas-zbe-supremo-le-da-razon-a-conductores-dinero-no-vuelve). More than 3.4M files and €663M up to 31 Dec 2025. — [El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)
- **Málaga.** 46,562 fines from 30 Nov 2025 to Oct 2026, with €1.38M of paid fines to be refunded. — [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
- **Standard amount.** €200 nearly everywhere (€100 for early payment), €260 in Barcelona during episodes, no licence points. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [ecomovilidad BCN](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/)

**Renewal aid**
- **MOVES III.** N1 light vans get up to €7,000, or €9,000 with scrapping, for individuals, autónomos and public administrations. The page lists the programme as extended to 31 Dec 2024 by RDL 4/2024, links to a "MOVES III 2025" page, and names no 2026 successor. — [IDAE MOVES III page, accessed 23 Oct 2026](https://www.idae.es/ayudas-y-financiacion/para-movilidad-y-vehiculos/programa-moves-iii)
- **Barcelona 2021 precedent.** Owners of unlabelled trucks and vans could keep circulating after the moratorium if they signed a commitment to renew by June 2022. — [Ajuntament de Barcelona, 10 Dec 2021](https://ajuntament.barcelona.cat/premsa/2021/12/10/els-transportistes-que-es-comprometin-a-canviar-de-vehicle-en-6-mesos-podran-circular-durant-aquest-temps-sense-distintiu-ambiental-per-la-zona-de-baixes-emissions/)

**Complaints from associations and autónomos**
- **Fenadismer on Madrid.** It described the earlier municipality-wide plan as "demasiado restrictiva" (too restrictive), lacking "equilibrio entre lo económico y lo medioambiental" (balance between economy and environment), and asked to negotiate an adaptation policy for road transport (snippet-level). — [El Mercantil, 30 Dec 2025](https://elmercantil.com/2025/12/30/madrid-prorroga-hasta-2026-la-moratoria-de-convertir-todo-el-termino-municipal-en-zbe/); [Ruta del Transporte](https://www.rutadeltransporte.com/noticias-transporte/fenadismer-aplaude-la-moratoria-de-la-entrada-en-vigor-de-toda-la-zbe-en-madrid.html)
- **Press claim on burdens.** Some ordinances impose disproportionate burdens ("trabas desproporcionadas") on autónomos and small businesses (no detail given). — [Merca2, 22 Jul 2026](https://www.merca2.es/2026/07/22/anulacion-zbe-multas-tsj-madrid-2422278/)
- **Transport-sector agenda in 2026.** In March 2026 the sector's protest agenda was about diesel prices (an estimated €250M of extra cost in three weeks), not ZBEs. — [El Estrecho Digital, 22 Mar 2026](https://www.elestrechodigital.com/2026/03/22/fenadismer-y-cetm-coinciden-en-rechazar-las-medidas-del-gobierno-y-no-descartan-movilizaciones-en-el-transporte-por-carretera)

### Inferences
- **A floor estimate of affected vans.** If you assume diesel dominance in old vans, the 1.08M vans aged 20+ (registered 2004 or earlier) are almost all unlabelled. Part of the 410k vans aged 15–19 (2005–2009) is unlabelled too. A conservative estimate is therefore about 1.1–1.3M unlabelled vans nationally. This is an inference, not a DGT figure.
- **The B group matters next.** Vans registered 2006–2013 with diesel engines carry B and are targeted by the 2027–2028 B phase-outs in Palma and Catalonia. Their count is unknown.
- **Who renews and who stops.** ZBE impact is concentrated on small autónomos with old vans who enter dense centres: trades, small couriers, and market and food suppliers. Large parcel carriers renewed early, especially in Madrid and Barcelona. The exemptions for workers aged 59+ (Madrid) and those within 5 years of retirement (Barcelona) show policymakers expect old-van owners to exit rather than renew. A SaaS product must therefore serve "comply-until-exit" users, not only fleet-renewal planning.

### Gaps
- No official count of vans or trucks by DGT label was found. The DGT panel could provide one but was not queried.
- No city publishes fines by vehicle type or owner type.
- I could not verify the 2026 status of MOVES or of any successor plan, nor regional aid for vans (e.g., AMB or Madrid renewal aid). The search budget was exhausted.
- I found no quantified surveys of autónomos (ATA, UPTA) on ZBE costs.

---

## 4. Data and tools: municipal open data, NAP/DGT 3.0, commercial LEZ data and routing, fleet tools, and whether routing can avoid penalties when the destination is inside the zone

### Takeaway
- **The national feed exists but is thin and stale.** The DGT NAP publishes free DATEX II v3 files (45 resources and 46 files, CC BY 4.0) with polygons, allowed labels and weekday/holiday hours. Residency rules, vehicle categories, quotas, exemptions and phase dates appear only as free text or not at all. Some records are stale or contradict reality: Valencia is shown as "active" since 1 Jun 2026 with no ZBE in force, and Málaga is "active" after fines stopped.
- **City portals publish perimeters only.** Barcelona, Valencia and Málaga open-data portals have polygons but no rules. Madrid offers only a WMS map service.
- **Commercial providers are generic.** HERE and TomTom offer LEZ avoidance keyed on Euro class and fuel, not on DGT labels and local exemptions. Spanish coverage and prices could not be verified.
- **Avoidance routing cannot help when the delivery address is inside the zone.** The solvable problems there are vehicle assignment, time windows and permits.

### Cited Findings
**DGT NAP (my direct check, 23 Oct 2026)**
- **Dataset terms and file list.** The dataset is "Zonas de Bajas Emisiones (ZBE)", DATEX II v3, CC BY 4.0, published by the DGT, updated "each time the ZBE restrictions or attributes change", with metadata dated 05/11/2024. It has 45 resources (the five Rondas municipalities share one).
  - Directory listing: 46 XML files, all stamped 08-Jul-2026 13:24 except Valencia.xml (31-Jul-2026).
  - Files include Madrid (7 MB), Barcelona, RondasDeBarcelona, Bilbao, Granada, Málaga, Palma, Valladolid, Alicante, SevillaCartuja, A Coruña and others.
  - **No files exist for Zaragoza, Vigo, Córdoba, Murcia or Las Palmas.**
  - Sources: [NAP dataset](https://nap.dgt.es/es/dataset/zonas-de-bajas-emisiones); [file index](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/)
- **What the six files I parsed contain** (Valencia, Málaga, Bilbao, Palma, Granada, Valladolid):
  - OpenLR polygons, `stickerCondition` values (0/ECO/C/B/"Sin distintivo") with negation logic, weekday (L) and holiday (F) time windows, `status`, `overallStartTime`, and a free-text `controlledZoneDescription`.
  - **Valencia.xml:** publicationTime 2026-07-30; status "active"; start 2026-06-01; description: "restricciones de acceso a los vehículos sin Distintivo Ambiental (Vehículos tipo A), y que sean del tipo turismo, motocicleta o ciclomotor". This contradicts the Oct 2026 status of no ZBE in force.
  - **Málaga.xml:** publicationTime 2025-08-20; "active"; description is only a link to the 2024 ordinance PDF. The non-domicile rule, which was the core of Málaga's regime, is not encoded.
  - **Palma.xml:** publicationTime 2025-01-07, start 2024-12-29. It predates the 1 Jul 2025 start of fines and does not distinguish the moratorium.
  - **Valladolid.xml:** the B and C phase dates appear only in free text: "B (hasta 31/12/2027), C (hasta 01/01/2030)".
  - **Bilbao.xml:** weekday 07:00–20:00 window, published 2025-09-30.
  - Source: [NAP files](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/)
- **DGT 3.0 municipal publishing API (ED MOV 2023/01).**
  - Municipalities authenticate with a certificate (pre-production first, then production).
  - They POST a GeoJSON perimeter (`name`, `city_ine`, `excluded`) and a restriction record (`affected_labels`, free-text `access_conditions`, `information_url`, `timetable` [L/F], `start_time`).
  - Endpoints: `/v1/zbeattr`, `/v1/zberestric`, `/v1/listzbe`, at base `https://cmobility30.es/zbe`.
  - The data is republished on the NAP in DATEX II and UVAR (uvarbox.eu) formats.
  - The model has **no fields** for vehicle category, MMA, residency or tax domicile, permit quotas, phase end-dates or episode rules.
  - Source: [DGT ED MOV 2023/01](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf)
- **Unmet demand for a national dataset.** A public request on datos.gob.es (16 Nov 2025, by an LSE researcher) asks for a national CSV of ZBE approval and implementation dates and boundary shapefiles. It is assigned to the Ministerio de Transportes, status "Asignado" (assigned), 6 followers, no response shown as of 19 Oct 2026. — [datos.gob.es](https://datos.gob.es/es/solicitud-de-datos/zonas-de-bajas-emisiones)

**Municipal open data (catalogue APIs queried 23 Oct 2026)**
- **Barcelona: Open Data BCN "zbe-ambit".** "Area of the low emission zone (LEZ) of the city of Barcelona": one file, `2023_Ambit_ZBE_Barcelona.gpkg`, created 25 Jan 2023, metadata modified 23 Sep 2025, CC BY 4.0. Attributes are area description, perimeter in m and area in m². No labels, hours or exemptions, and only Barcelona city rather than all Rondes municipalities. — [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/zbe-ambit)
- **Valencia: "Zona de Bajas Emisiones".** Created 28 Feb 2026, modified 21 Oct 2026, CC BY 4.0. Formats: GeoJSON (ArcGIS REST query), SHP, KMZ, JSON, PBF and WFS. It describes the "Ámbito de la ZBE… según la Ordenanza aprobada provisionalmente… 25/02/2025", i.e. the perimeter of a ZBE that is not in force. Data model: `objectid` and `zona_zbe` only. — [Valencia open data](https://opendata.vlci.valencia.es/dataset/zona-de-bajas-emisiones); [GeoJSON endpoint](https://geoportal.valencia.es/server/rest/services/OPENDATA/Trafico/MapServer/240/query?where=1=1&outFields=*&f=geojson)
- **Málaga.** Perimeter in GeoJSON, KML, GML, CSV and ZIP (2024 files, metadata 28 Apr 2025), plus datasets of ZBE sound meters, monitoring cabins and station measurements. — [Málaga open data](https://datosabiertos.malaga.eu/dataset/sistema-de-informacion-cartografica-zona-bajas-emisiones)
- **Madrid geoportal.** "Vías con limitaciones de circulación a vehículos sin distintivo ambiental" (13 Mar 2026): ESRI REST MapServer and WMS 1.3.0 only, with layers for the perimeter, access points, OCR cameras and red-light devices. **No GeoJSON, SHP or WFS download.** — [Madrid geoportal](https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/dataset.iam?id=7e9120c8-881e-11ed-8764-34298f78123d)
- **Bilbao.** A general open-data portal is linked from the ZBE page; I did not verify a ZBE dataset. — [bilbao.eus](https://www.bilbao.eus/cs/Satellite?cid=1279231359138&language=es&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal)

**Commercial data and routing**
- **HERE Environmental Zones.** A data product with polygons, zone conditions and an XML "look-aside file" (emission regulations, restricted vehicle types, restriction times), delivered in RDF, FGDB, NAVSTREETS or GDF. "Available in 19 countries and territories globally" (©2023 one-pager; Spain not named). — [HERE one-pager](https://assets.here.com/x7rx8ayph7ee/1hLhgrGc50DT8Wtaos2JO7/f914305bc96941845d38c198e276d4e1/HERE-Environmental-Zone-product-one-pager-2021.pdf)
- **HERE Routing.** Avoidance is enabled with `excludeZoneType=environmental` and uses `emissionType` (Euro I–VI), `fuelType`, `limitedWeight` and `departure`. HERE warns that a zone is avoided if any single specified parameter matches. There is no DGT-label parameter. — [HERE docs](https://docs.here.com/routing/docs/truck-restrictions-env-zones)
- **TomTom Routing API.** It has had LEZ options since early 2023 (`sectionType=lowEmissionZone`, `avoid=lowEmissionZones`). A knowledge-base article reported LEZ data for 376 cities globally without listing them (snippet-level; the page returned 404 on 23 Oct 2026). Spanish coverage is unverified. — [TomTom release notes](https://docs.tomtom.com/routing-api/documentation/tomtom-maps/product-information/release-notes)
- **urbanaccessregulations.eu.** Covers 268 LEZs in Europe plus 14 urban road-charging schemes (snippet-level via Polis Network, date unknown). No price found. — [Polis Network](https://polisnetwork.eu/?p=16859)
- **Green-Zones.** The homepage still describes Barcelona as "one of 7 zones in Spain at the moment" and says the Distintivo Ambiental is valid only for Spanish-registered vehicles. Latest news post 06.01.2026. This suggests stale Spain coverage. No API or price found. — [green-zones.eu](https://www.green-zones.eu/en/)
- **Nascent developer tools.**
  - "@cargoffer/zbe-mcp", a server for AI assistants (MCP), offers five tools including `zbe.checkRoute` for Spain and Portugal. It "compares the vehicle's Euro emission class with each ZBE's minimum requirement"; first observed 11 Jul 2026; no price, licence or source stated. — [Glama](https://glama.ai/mcp/servers/cargoffer/zbe-mcp-server/tools/zbe.checkRoute)
  - An Apify actor "EU LEZ Route & Vehicle Checker" exists (not inspected). — [Apify](https://apify.com/scholarstack/eu-lez-intelligence)
- **Consumer and association tools.**
  - The "ZBE España" iOS app (v1.1.0, first released 2 Dec 2024) maps Madrid, Barcelona, Valencia and Sevilla and checks label compatibility; tagged free. — [app listing](https://mwm.ai/apps/zbe-espaa/6738807819)
  - Astac Condal (a Fenadismer member) and the RACC built a national ZBE information site for hauliers. — [Fenadismer, 7 Jul 2024](https://www.fenadismer.es/los-transportistas-ya-pueden-consultar-todas-las-zonas-de-bajas-emisiones-en-una-sola-web/); [Astac](https://www.astac.info/el-desplegament-de-les-zbes-a-espanya/)
- **Foreign vehicles at plate-reading cameras.** Plate-reading systems compare plates with municipal databases, so foreign vehicles must register even if they carry an EU sticker (snippet-level). — [TCS](https://www.tcs.ch/de/camping-reisen/reiseinformationen/wissenswertes/fahrzeugvorschriften/umweltzonen-spanien.php)

**Destination inside the zone: evidence on what actually avoids penalties**
- **Madrid Distrito Centro.** Time windows by label and MMA (C 7–15h, ECO 7–21h) and night windows by declaración responsable. Pre-registration "no autoriza el acceso fuera de las franjas horarias". — [madrid.es DC professionals](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD)
- **Permit quotas:** Bilbao invitations of 6 per month notified within 2 days ([ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/)); Barcelona 24 daily passes per year ([ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/)); Zaragoza 8 accesses per month ([ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/)).
- **Car-park and loading exemptions:** Granada exempts vehicles parking over 1 hour in its 36 public car parks ([Xataka](https://www.xataka.com/movilidad/granada-multa-hoy-su-nueva-zona-bajas-emisiones-quienes-pueden-acceder-multas-excepciones)); A Coruña's loading window is 6–11h ([ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/la-coruna/la-coruna/)).

### Inferences
- **Route optimisation alone cannot avoid penalties when the stop is inside the zone.** Avoidance routing (HERE, TomTom) only helps for through-traffic. For in-zone stops, compliance requires:
  - (a) assigning a compliant vehicle in dispatch;
  - (b) scheduling inside allowed windows (label- and MMA-specific);
  - (c) using or rationing a permit or quota and notifying the plate where needed (Bilbao, Barcelona, Zaragoza, Sevilla);
  - (d) routing to an exempt car park or hand-off point (Granada car parks, Bilbao rotation car parks);
  - (e) holding the right standing registration (Madrid permits system, AMB registry, Palma 5-day pre-registration).
  This is a constraint-satisfaction and permit-ledger problem, not a pathfinding problem.
- **No vendor yet models the Spanish rule semantics.** The data layer that matters most (domicile, quotas, permits, episodes, phase dates, vehicle category) is missing from the NAP, from city portals, and apparently from HERE and TomTom's Euro-class models. A curated, versioned, legally monitored "Spanish ZBE rules API" built on NAP and municipal polygons plus ordinance parsing is technically feasible. Its main costs are curation and legal monitoring, given 2026's court whiplash, not geometry.
- **Free official data caps the price of geometry-only products.** Value has to come from semantics, freshness guarantees and permit workflows.

### Gaps
- Google Routes API, PTV (developer blog returned 403), Sygic Truck and Webfleet/TomTom Telematics: I could not verify Spanish ZBE handling or prices in-session.
- Prices for HERE, TomTom, urbanaccessregulations.eu and Green-Zones: none found.
- Fleet-management tools used by Spanish SMEs (e.g., local telematics vendors) and their prices: not researched for lack of search budget.
- Whether the NAP is used by in-car navigation makers in practice: no evidence found.

---

## 5. Fact-check of the three claims

### Takeaway
1. **"Enforced by automated city camera tracking"** is **true for the main enforcing cities** (Madrid, Barcelona, Bilbao, Zaragoza, Sevilla-Cartuja, Palma, Granada, and Málaga until 14 Oct 2026). It is **false as a generalisation**: Valencia has cameras but no ZBE, Vigo cameras only count traffic until Sept 2027, Alicante issues notices only, Murcia and Las Palmas have no ZBE, and 17 of 23 Catalan municipalities did not effectively fine in 2025.
2. **Valencia's "Urban Sandbox" exists, under a different description.** It is the *Ordenanza Municipal reguladora del Sandbox Urbano de València*: a municipal, cross-sector controlled-testing framework anchored in Ley 28/2022 art. 16. It is **not mobility-specific** and **cannot waive non-municipal rules** such as state traffic law. It is operational through a permanently open procedure, AE.IN.100. I could not verify its final Pleno approval or BOP publication date.
3. **"Barcelona and Valencia publish open data usable for ZBE routing"** is **partly true**. Both publish **perimeter polygons only**. Valencia's polygon is for a ZBE that is not in force. Rule data (labels, hours) is available only via the DGT NAP, and Valencia's NAP record conflicts with reality.

### Cited Findings
**Claim 1: camera enforcement**
- **Where it is true:**
  - Madrid: "lectores OCR" and "foto rojo" devices. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); OCR access cameras listed in the [Madrid geoportal](https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/dataset.iam?id=7e9120c8-881e-11ed-8764-34298f78123d)
  - Barcelona: perimeter plate cameras. — [Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/)
  - Bilbao: plate readers. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/)
  - Zaragoza: plate readers. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/)
  - Sevilla: automatic cameras since 2024. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/sevilla/sevilla/)
  - Málaga: 97 cameras at 53 points. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/)
  - Palma: plate reading, so no sticker is needed (snippet-level). — [COPE, 25 Jun 2025](https://www.cope.es/emisoras/illes-balears/baleares/mallorca/noticias/multas-vista-palma-son-vehiculos-seran-sancionados-partir-1-julio-circulan-zbe-20250625_3176002.html)
- **Where it is not true or only partly true:**
  - Valencia: installed cameras "only count accesses for statistics"; no ZBE in force. — [ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/)
  - Vigo: 74 cameras plus AI counters, information phase to 10 Sep 2027. — [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)
  - Alicante: notices only. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/alicante/alicante/)
  - Murcia and Las Palmas: no ZBE. — [ecomovilidad Las Palmas](https://ecomovilidad.es/zonas-de-bajas-emisiones/las-palmas/las-palmas-de-gran-canaria/)
  - Catalonia: only 6 of 23 municipalities effectively fined in 2025. — [Metrópoli Abierta, 10 Sep 2026](https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html)
  - Lleida: implemented "with deficiencies", without sufficient control mechanisms (snippet-level). — [Segre, Sep 2026](https://www.segre.com/ca/lleida/260911/la-sindicatura-de-comptes-conclou-que-la-zbe-de-lleida-es-va-implantar-amb-carncies_1327971.html)
  - Córdoba: enforcement method not stated in the sources read. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/cordoba/cordoba/)
- **Nuance: not all camera systems check labels.** A Coruña and Alicante Anillo I run access-control (whitelist) models in which cameras check authorisation, not the label. — [ecomovilidad A Coruña](https://ecomovilidad.es/zonas-de-bajas-emisiones/la-coruna/la-coruna/)

**Claim 2: Valencia "Urban Sandbox"**
- **Name and approval.** The project of the "Ordenanza reguladora del Sandbox Urbano de Valencia" was approved by the Junta de Gobierno Local and announced on 8 Mar 2024 as pioneering in the EU. The city committed to answer and enable tests "en menos de 3 meses" (in under three months). — [Valencia Plaza, 8 Mar 2024](https://valenciaplaza.com/valenciaplaza/valencia-aprueba-el-sandbox-urbano-pionero-en-la-union-europea)
- **Legal basis (ordinance text).**
  - The preamble invokes **Ley 28/2022 (startups law), art. 16**, which allows public authorities to create controlled testing environments for limited periods, and Ley 17/2022 (science law).
  - The competence clause cites art. 25 of the Ley 7/1985 on local government and art. 33.1 of Ley 8/2010 on local government in the Comunitat Valenciana.
  - Tests run under a "Protocolo de pruebas" with an initial duration of up to **5 years**.
  - Use of municipal "Recursos Urbanos" (urban spaces and infrastructure) bypasses the ordinary public-domain authorisation, with a 100% fee reduction.
  - **Art. 11.3:** promoters must still comply with all rules "que no sean de competencia municipal" (outside municipal competence) unless previously exempted.
  - Mobility and transport are listed among many eligible areas (art. 4.2).
  - Entry into force requires final Pleno approval plus publication in the Boletín Oficial de la Provincia (BOP).
  - Source: [Ordinance text, sede.valencia.es](https://sede.valencia.es/sede/descarga/doc/DOCUMENT_1_20240006949868)
- **Procedure.** AE.IN.100 "Sandbox Urbano de la Ciudad de València" is "Procedimiento abierto de forma permanente" (permanently open). Maximum resolution time is 3 months, and silence counts as rejection. Contact: sandboxurbano@valencia.es. — [sede.valencia.es](https://sede.valencia.es/sede/registro/procedimiento/AE.IN.100?lang=1)
- **Port logistics.** In June 2026 the city announced an alliance with the Autoridad Portuaria de Valencia to bring all port logistics activity into the Sandbox, focused on AI, smart logistics, mobility and automation. — [Paréntesis.Media, 28 Jun 2026](https://www.parentesis.media/valencia-madrid-y-barcelona-convierten-la-ia-en-un-laboratorio-urbano-bajo-control-juridico/)
- **Barcelona comparison.** Barcelona is promoting an "Ordenanza de Espacios de Experimentación" (status unconfirmed). — [Paréntesis.Media, 28 Jun 2026](https://www.parentesis.media/valencia-madrid-y-barcelona-convierten-la-ia-en-un-laboratorio-urbano-bajo-control-juridico/)
- **No named mobility projects or project counts were found.** — [Wonderbits, 2025](https://www.wonderbits.net/en/urban-sandbox-of-valencia-the-city-as-a-real-world-environment-for-innovation/)

**Claim 3: open data for routing**
- **Barcelona.** A perimeter GPKG only (2023 file; CC BY 4.0) with area and perimeter attributes. — [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/zbe-ambit)
- **Valencia.** A perimeter (GeoJSON, WFS and others) for the ordinance "aprobada provisionalmente" on 25/02/2025, with no rule attributes. — [Valencia open data](https://opendata.vlci.valencia.es/dataset/zona-de-bajas-emisiones)
- **Rules via the NAP.** NAP DATEX II files exist for RondasDeBarcelona, Barcelona and Valencia. Valencia.xml says "active" from 2026-06-01 while press and aggregators report no ZBE. — [NAP index](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/); [ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/)

### Inferences
- **Claim 1** is safe only as "major Spanish ZBEs that fine use number-plate cameras". Investors and customers should not assume enforcement exists wherever a ZBE is declared.
- **Claim 2** should be reworded to "Valencia has a municipal Sandbox Urbano ordinance enabling time-limited real-world tests using municipal spaces". It is a plausible pilot channel for a ZBE or logistics tool with the city or the port. It offers no exemption from DGT or state traffic rules, so it cannot "legally test" non-compliant vehicle access.
- **Claim 3** should be reworded to "both cities publish free ZBE perimeter polygons (CC BY 4.0). Machine-readable rules come only from the DGT NAP and need curation."

### Gaps
- The Valencia Sandbox ordinance's final approval and BOP publication date, and the number of projects admitted, could not be confirmed.
- Whether Valencia's NAP record reflects an unreported measure, such as an APR or temporary decree, or is an error: unverified.

---

## 6. Pain-point inventory (structured entries)

### Takeaway
I recorded 23 pain points. The most software-relevant cluster is rules fragmentation, legal volatility and the poor national data feed (ZBE-01, -02, -03, -19), combined with the in-zone dispatch problem (ZBE-15) and permit workflows (ZBE-06, -07, -08). The largest economic pain is the old van and truck stock (ZBE-05), and software can only partly address it.

### ZBE-01: A patchwork of about 150 local rule-sets for multi-city fleets
- Who: fleet operators, couriers and delivery partners operating in several cities (from autónomos with one van to national carriers); e-commerce sellers using them.
- Where: national. Examples: Madrid, Barcelona/AMB, Bilbao, Zaragoza, Sevilla, Palma, Granada, Valladolid, Córdoba, A Coruña.
- Day-to-day reality: each city defines its own perimeter, hours, restricted labels, residency or domicile tests, quotas and exemptions. Some are label-based and some are whitelist (access-control) based. A van compliant in Zaragoza (B allowed 8–20h) is not necessarily compliant in Madrid Distrito Centro (B light vans banned since 2024) or Bilbao (B restricted 7–20h since Jun 2025).
- Evidence:
  - 151 municipalities and 33M people; 56 "fully active" ZBEs and 89 in approval. — [Motor16, 16 Feb 2026](https://www.motor16.com/las-ultimas-noticias/zbe-ciudades-multas-coches/)
  - 149 municipalities; the association built a national ZBE info site for hauliers. — [Fenadismer, 7 Jul 2024](https://www.fenadismer.es/los-transportistas-ya-pueden-consultar-todas-las-zonas-de-bajas-emisiones-en-una-sola-web/)
  - Rule diversity across cities: see the section 2 table (madrid.es, ecomovilidad, BOIB).
- Scale: about 150 obliged municipalities and 45 NAP resources ([NAP](https://nap.dgt.es/es/dataset/zonas-de-bajas-emisiones)); 2.74M vans and 2.46M trucks nationally ([DGT Anuario 2024](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)).
- Cost/impact: €200 per infringement (€260 in Barcelona episodes); time spent reading ordinances (no hours data found).
- Driver & status: Ley 7/2021 art. 14 and RD 1052/2022 (in force) plus individual municipal ordinances; status ranges from in force with fines to not yet adopted (section 2).
- How it is solved today:
  - Association websites (Astac/RACC, price unknown), consumer apps (ZBE España, free tag), aggregator blogs (ecomovilidad, Iberfurgo, RACE).
  - HERE and TomTom LEZ layers, which are Euro-class based with unverified Spanish coverage and no prices found.
  - Documented issue: Green-Zones still says "one of 7 zones in Spain" ([green-zones.eu](https://www.green-zones.eu/en/)).
- Software-solvable?: **Yes.** A normalised, versioned rules database and API is the direct fix.
- Confidence: high.

### ZBE-02: Legal whiplash: annulments, suspensions and reinstatements change rules overnight
- Who: all fleets, couriers and autónomos; municipalities.
- Where: Madrid, Málaga, Valladolid, Barcelona (suspension), Bilbao (appeal pending), and other TSJ cases.
- Day-to-day reality: a zone that fined last week may stop (Málaga, 14 Oct 2026), be suspended for an emergency (Barcelona, 22 Jan–16 Mar 2026), be annulled but keep fining (Valladolid), or be replaced by a new ordinance while old fines are litigated (Madrid). Fleets cannot tell from official feeds which state applies today.
- Evidence:
  - Málaga TSJA 896/2026 of 6 May 2026; fines stopped 14 Oct 2026. — [ecomovilidad Málaga, 22 Oct 2026](https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/); [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
  - Madrid: Supreme Court inadmission 15 Apr 2026; new ordinance in force 7 Apr 2026; TSJM enforcement proceedings July 2026. — [Infobae, 21 Apr 2026](https://www.infobae.com/espana/2026/04/21/el-tribunal-supremo-confirma-la-anulacion-parcial-de-la-zona-de-bajas-emisiones-en-madrid-al-rechazar-el-recurso-del-ayuntamiento/); [El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)
  - Barcelona suspension and resumption. — [zbe.barcelona](https://www.zbe.barcelona/)
  - Valladolid annulled 16 Mar 2026 but not final. — [ecomovilidad](https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/)
- Scale: Madrid alone about 3.4M sanction files ([El Diario de Madrid](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)); Málaga 46,562 fines ([Motorpasión](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)).
- Cost/impact: €663M in disputed Madrid fines (AEA estimate); Málaga €1.38M refunds with up to four years' delay.
- Driver & status: Madrid OMS as amended by Ordenanza 2/2026 (in force; old-fine execution pending); Málaga ordinance ZBE chapter (annulled, not final); Valladolid 2024 ordinance (annulled, not final, still fining); Barcelona 2023 ordinance (in force, upheld 24 Nov 2025).
- How it is solved today: press monitoring, lawyers and associations (AEA, OCU). No software alerting product found.
- Software-solvable?: **Partly.** Legal-change monitoring and alerts can be productised, but interpreting rulings needs human legal review.
- Confidence: high.

### ZBE-03: The national NAP feed is incomplete, stale and semantically thin
- Who: fleet-software vendors, navigation and routing providers, fleet operators; municipalities as publishers.
- Where: national (DGT NAP).
- Day-to-day reality: anyone building routing on official data finds missing cities (Zaragoza, Vigo, Córdoba), "active" records for zones not enforcing (Valencia, Málaga), start dates that do not match when fines began (Palma), and rule details in free text or links to PDFs.
- Evidence:
  - My parsing on 23 Oct 2026: Valencia.xml "active" from 2026-06-01; Málaga.xml description is only a PDF link; Palma.xml published 2025-01-07; Valladolid phases in free text. — [NAP files](https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/)
  - The DGT 3.0 model has only labels, free-text conditions and a timetable. — [DGT ED MOV 2023/01](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf)
  - Second source on reality: no ZBE in Valencia. — [ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/)
- Scale: 45 resources and 46 files; at least 3 of the 10 fining or regime cities in section 2 are missing.
- Cost/impact: wrong routing or compliance decisions leading to €200 fines; unquantified.
- Driver & status: RD 1052/2022 art. 10.2 requires notification within one month (in force); DGT ED MOV 2023/01 (in force since Feb 2023).
- How it is solved today: vendors' own curation (HERE, TomTom) and manual research. No complaints on record, but the inconsistencies are documented above.
- Software-solvable?: **Yes.** Curation, validation against ordinances and press, and enrichment of semantics.
- Confidence: high (direct observation).

### ZBE-04: Domicile and residency rules penalise out-of-town fleets and are legally fragile
- Who: fleets and autónomos whose vehicles are registered or taxed outside the city (including vehicles owned by renting or leasing companies), regional delivery partners and commuters' work vans.
- Where: Madrid (cars on the city tax roll since 2022), Granada (tax domicile), Málaga (annulled non-domicile rule), Palma (resident authorisations), Valencia draft (out-of-province first).
- Day-to-day reality: the same unlabelled vehicle is legal for a local and fined for a visitor. For vans the impact varies: Madrid now lets unlabelled non-cars circulate regardless of domicile outside the special zones, while Granada restricts any unlabelled vehicle without local tax domicile.
- Evidence:
  - Madrid unlabelled cars must have been on the tax roll continuously since 1 Jan 2022; non-cars are exempt from that test. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD)
  - Granada requires both no label and no local tax domicile. — [Xataka, 2 Oct 2025](https://www.xataka.com/movilidad/granada-multa-hoy-su-nueva-zona-bajas-emisiones-quienes-pueden-acceder-multas-excepciones)
  - Málaga's non-domicile regime was annulled (reasoning disputed). — [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
- Scale: Málaga's 46,562 fines were all under a non-domicile rule. National scale unknown.
- Cost/impact: €200 per entry; refunds in Málaga.
- Driver & status: municipal ordinances (Madrid in force; Granada in force; Málaga annulled, not final).
- How it is solved today: case-by-case registration; no tool models domicile rules (NAP encodes none).
- Software-solvable?: **Partly.** The rules can be encoded per vehicle and holder. Vehicle domicile data comes from the fleet's own records.
- Confidence: medium.

### ZBE-05: An ageing commercial fleet of about 1.08M vans and 1.02M trucks aged 20+ years
- Who: autónomos with old vans (trades, markets, small couriers), small hauliers.
- Where: national, most acute in Madrid, Barcelona/AMB, Bilbao, Palma and Granada.
- Day-to-day reality: owners of pre-2006 diesel vans (no label) cannot enter label-restricted ZBEs during restricted hours. They choose between buying a newer van, using permits or quotas, sub-contracting, or exiting the zone.
- Evidence:
  - 1,084,677 of 2,741,010 vans and 1,021,451 of 2,462,425 trucks are aged 20+. — [DGT Anuario 2024, tables 72 and 80](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/publicaciones/Anuario_Estadistico_General/Anuario-Estadistico-General-2024.pdf)
  - More than half of vans and trucks are unlabelled (unnamed DGT analysis). — [Ecoticias, 24 Jan 2024](https://www.ecoticias.com/co2/etiquetas-ambientales-dgt)
- Scale: about 1.1–1.3M unlabelled vans is an inference (section 3).
- Cost/impact: MOVES III aid up to €7k/€9k per N1 (status after 2024 unclear) ([IDAE](https://www.idae.es/ayudas-y-financiacion/para-movilidad-y-vehiculos/programa-moves-iii)); no sourced van prices.
- Driver & status: label system per the Reglamento General de Vehículos (unchanged at least to 2027, snippet-level: [motor.es](https://www.motor.es/noticias/confirmado-etiquetas-dgt-quedan-como-estan-2025111050.html)); ZBE ordinances (various).
- How it is solved today: dealers and renting, MOVES aid (uncertain in 2026), city exemptions for older autónomos (Madrid 59+, Barcelona near-retirement until 31 Mar 2028).
- Software-solvable?: **Partly.** Renewal planning, total-cost tools and aid finders help, but the core problem is capital expenditure.
- Confidence: high (fleet age), medium (label share).

### ZBE-06: Madrid Distrito Centro has label × MMA time windows plus per-vehicle registration
- Who: delivery fleets, trades and suppliers serving central Madrid (including rental, replacement and leased vans).
- Where: Madrid (ZBEDEP Distrito Centro).
- Day-to-day reality: a C-label van may only enter 7–15h, and a B-label light van not at all since 2024. Light-vehicle holders must have IAE registration and pre-register each plate in the permits system (Mi Carpeta or appointment). Rented, leased and replacement vehicles need extra documents. Night deliveries need a declaración responsable renewed yearly with proof of deliveries.
- Evidence: [madrid.es DC professionals page](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD) (single official source; primary).
- Scale: unknown number of registered professional vehicles (gap).
- Cost/impact: €200 per entry outside the window; admin hours per vehicle (not quantified).
- Driver & status: Madrid OMS as amended by Ordenanza 2/2026 and Decreto 178 (acoustic loading protocol); in force with fines.
- How it is solved today: manual registration in Mi Carpeta, gestorías (administrative agents) for ownership-change documents, dispatchers' spreadsheets (inference). No prices.
- Software-solvable?: **Yes.** Permit-ledger and dispatch-window constraints.
- Confidence: high.

### ZBE-07: Heterogeneous permit quotas and invitations to ration and notify
- Who: local shops and e-commerce sellers receiving deliveries, trades, autónomos with unlabelled or B vans.
- Where: Bilbao (6 invitations per month), Barcelona (24 daily passes per year), Zaragoza (8 accesses per month), Sevilla (10 per month, snippet-level), Granada (forms), Córdoba (exemption list).
- Day-to-day reality: businesses must track quotas per plate and per month, notify plates within deadlines (Bilbao up to 2 days after access), and re-register vehicles. Errors produce €200 fines.
- Evidence: [ecomovilidad Bilbao](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/); [ecomovilidad Barcelona](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [ecomovilidad Zaragoza](https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/); [ecomovilidad Sevilla](https://ecomovilidad.es/zonas-de-bajas-emisiones/sevilla/sevilla/). Single secondary source per city.
- Scale: unknown.
- Cost/impact: €200 per missed notification or over-quota entry.
- Driver & status: municipal ordinances (in force with fines in all four cities).
- How it is solved today: municipal portals and apps per city; manual.
- Software-solvable?: **Yes.** A permit wallet with quota tracking, though many cities lack APIs.
- Confidence: medium.

### ZBE-08: Foreign-registered vehicles and cross-border partners
- Who: EU hauliers and couriers, foreign-plated rental or relocation vans, seasonal workers and tourism-sector vans.
- Where: Palma, Barcelona/AMB, Bilbao, Madrid, Zaragoza.
- Day-to-day reality: foreign vehicles have no DGT label, so cities require Euro-class-based registration. Palma requires registration 5 days ahead with a ferry or flight ticket for a 30-day permit. AMB authorisations last up to 2 years. Bilbao has its own register. Zaragoza instead exempts foreign plates not in the DGT register.
- Evidence:
  - Palma: fines on foreign plates were the first category of complaints after fines began on 1 Jul 2025. — [BOIB 37, 24 Mar 2026](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590)
  - AMB registry. — [ecomovilidad BCN](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/)
  - Bilbao register. — [bilbao.eus](https://www.bilbao.eus/cs/Satellite?c=Page&cid=1279235266667&language=es&pageid=1279235266667&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal)
  - Madrid: same rules apply. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD)
  - Zaragoza exemption. — [ecomovilidad Zaragoza](https://ecomovilidad.es/zonas-de-bajas-emisiones/zaragoza/zaragoza/)
- Scale: unknown.
- Cost/impact: €200 per fine plus cross-border collection; registration admin.
- Driver & status: municipal ordinances; the Palma resolution of 20 Mar 2026 (BOIB 37) is in force.
- How it is solved today: city web forms; Green-Zones (stale for Spain); TCS and ADAC travel guides (snippet-level).
- Software-solvable?: **Yes.** Euro-class-to-label mapping plus multi-city registration filing.
- Confidence: medium-high.

### ZBE-09: Rented, leased and replacement vans: fines hit the registered holder and documents are needed per vehicle
- Who: renting and leasing companies, van-rental firms, the SMEs and delivery partners who drive their vehicles.
- Where: Barcelona and Madrid documented; likely national.
- Day-to-day reality: camera fines go to the registered holder (the lessor), who re-invoices the customer. Madrid's permits system requires renting or leasing contracts and lessor certificates, and repair orders for replacement vehicles, before the vehicle may enter Distrito Centro.
- Evidence: "Rental companies pass the fine to the customer who was driving" ([Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/)); Madrid document requirements ([madrid.es DC](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD)).
- Scale: unknown.
- Cost/impact: €200 per fine plus admin re-invoicing fees (not quantified).
- Driver & status: municipal ordinances; the traffic law's owner-liability rule (art. 76 z3 classifies ZBE breaches as serious infringements).
- How it is solved today: manual fine-transfer workflows at lessors (inference).
- Software-solvable?: **Yes.** Fine-to-driver matching and pre-trip compliance checks for rental fleets.
- Confidence: medium (thin evidence).

### ZBE-10: Fine exposure at scale
- Who: all vehicle holders; for business, fleets with repeated daily entries.
- Where: Madrid, Málaga, Barcelona, Granada, Bilbao, Palma, Zaragoza, Sevilla.
- Day-to-day reality: each non-compliant entry is a €200 serious infringement. For a van making daily central deliveries, the exposure accumulates quickly. Fines arrive by post or electronic address days later.
- Evidence: Madrid more than 3.3M fines and €650M (Sept 2021–Nov 2025, AEA) ([Xataka, 27 Apr 2026](https://www.xataka.com/movilidad/madrid-cobro-650-millones-euros-multas-zbe-supremo-le-da-razon-a-conductores-dinero-no-vuelve)); more than 3.4M and €663M to 31 Dec 2025 ([El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)); Málaga 46,562 ([Motorpasión](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)).
- Scale: millions of fines (Madrid); business share unknown.
- Cost/impact: €200 per fine (€100 early payment); €260 in Barcelona episodes.
- Driver & status: Ley sobre Tráfico art. 76 z3 plus municipal ordinances (in force).
- How it is solved today: paying, appealing via lawyers or associations, fine-management services (not researched).
- Software-solvable?: **Partly.** Prevention through pre-trip checks and fine centralisation. Appeals still need legal input.
- Confidence: high (volumes), low (business share).

### ZBE-11: Refund and appeal limbo after court rulings
- Who: SMEs and autónomos who paid or appealed ZBE fines.
- Where: Madrid, Málaga, Valladolid.
- Day-to-day reality:
  - Madrid refuses automatic refunds while lower courts annul individual fines.
  - Málaga will refund only after the ruling is final, possibly over 4 years.
  - Valladolid fines continue under a ruling that is not final.
  - Businesses do not know whether to pay early at the 50% discount or appeal.
- Evidence: Madrid: "no procede devolver las multas" ([El Diario de Madrid, 15 Jul 2026](https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html)); OCU says non-final appealed cases have better odds ([Xataka](https://www.xataka.com/movilidad/madrid-cobro-650-millones-euros-multas-zbe-supremo-le-da-razon-a-conductores-dinero-no-vuelve)); Málaga ([Motorpasión](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)).
- Scale: Madrid about 3.4M files; Málaga 13,694 paid and 32,868 suspended.
- Cost/impact: €663M (Madrid, AEA estimate); €1.38M (Málaga).
- Driver & status: TSJM execution proceedings (pending); TSJA 896/2026 (not final, expected about 25 Nov 2026).
- How it is solved today: associations (AEA), lawyers, consumer organisation OCU.
- Software-solvable?: **Partly.** Tracking fines and appeal deadlines; claims processing is legal work.
- Confidence: medium (likely transient).

### ZBE-12: Dynamic pollution-episode restrictions
- Who: fleets and autónomos with B or unlabelled vans.
- Where: Madrid (unlabelled non-cars banned on episode days), Barcelona (B banned in episodes since 1 Jan 2026; €260), Alicante (rings II and III by decree), Castellón and Sevilla episode-only models.
- Day-to-day reality: a vehicle legal yesterday is illegal today because the regional or city government declares an episode, and fleets need same-day alerts. NacióDigital notes no Catalan episode has been declared since 2015.
- Evidence: [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [Iberfurgo, 26 Jun 2026](https://www.iberfurgo.com/zbe-barcelona/); [NacióDigital, 28 Apr 2026](https://naciodigital.cat/impacte/ciutats/les-zbe-de-larea-de-barcelona-senduriran-el-2028.html); [ecomovilidad Alicante](https://ecomovilidad.es/zonas-de-bajas-emisiones/alicante/alicante/); [El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html) (Castellón)
- Scale: B vehicles are 12% of Barcelona's fleet (NacióDigital).
- Cost/impact: €260 per entry in Barcelona episodes; €200 elsewhere.
- Driver & status: Catalan Decree 132/2024 (cited by ecomovilidad; the episode-declaration instrument itself was not verified); Madrid OMS DT 7ª (the transitional provision; in force).
- How it is solved today: official websites and press; no fleet-integrated alerting found. The NAP has no episode field.
- Software-solvable?: **Yes.** Alerts and dispatch blocking, but only if episode declarations are machine-readable or scraped.
- Confidence: medium (rare events in Catalonia).

### ZBE-13: The conditional "NO2 kill-switch" in Madrid's transitional regime
- Who: holders of unlabelled vans and trucks (including non-Madrid fleets) operating in Madrid outside the special zones.
- Where: Madrid.
- Day-to-day reality: unlabelled vans may circulate only while NO2 limits are met at every station. A single breach lets the Junta de Gobierno end the regime, with fines 6 months after BOCM publication. Fleets cannot plan renewal on a fixed date.
- Evidence: [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [ecomovilidad Madrid](https://ecomovilidad.es/zonas-de-bajas-emisiones/comunidad-de-madrid/madrid/)
- Scale: unknown number of unlabelled vans operating in Madrid.
- Cost/impact: potential forced renewal on 6 months' notice; MOVES aid uncertain.
- Driver & status: Ordenanza 2/2026, disposición transitoria séptima; in force since 7 Apr 2026; regime active as of Oct 2026 (no termination found).
- How it is solved today: nothing specific; associations monitor.
- Software-solvable?: **Partly.** Air-quality and legal monitoring with renewal-planning alerts; the underlying cost is capital expenditure.
- Confidence: high (rule), low (probability of trigger).

### ZBE-14: Scheduled B-label phase-outs (2027–2030)
- Who: fleets with diesel vans from 2006–2013 or petrol vans from 2001–2005 (B), and heavy vehicles from 2006 onward.
- Where:
  - Catalonia: municipalities over 50,000 before 1 Jan 2028.
  - Palma: B out from 1 Jan 2027.
  - Bilbao: B exemptions end by 31 Dec 2029; only Cero, ECO and C from 2030.
  - Valladolid: B from end-2027 (ordinance annulled, not final).
  - Vigo: B from 2029.
- Day-to-day reality: vans compliant today become non-compliant on known future dates. Fleet owners must plan renewals city by city.
- Evidence: [NacióDigital, 28 Apr 2026](https://naciodigital.cat/impacte/ciutats/les-zbe-de-larea-de-barcelona-senduriran-el-2028.html); [ecomovilidad BCN (Decree 132/2024)](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [BOIB 37, 24 Mar 2026](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590); [ecomovilidad Bilbao](https://ecomovilidad.es/zonas-de-bajas-emisiones/vizcaya/bilbao/); [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)
- Scale: Barcelona B = 12% of vehicles; Vigo 57,934 B vehicles. Van-specific B count unknown.
- Cost/impact: renewal capex; resale-value loss for B vans (unquantified).
- Driver & status: Catalan Decree 132/2024 (in force; the ordinance amendment had not started as of Oct 2026); Palma ordinance (BOIB 167/2024, in force); Bilbao ordinance (in force); Vigo ordinance (in force, phased).
- How it is solved today: dealer and renting advice; no planning tool found.
- Software-solvable?: **Partly.** Fleet compliance forecasting per city and date.
- Confidence: high (dates), medium (impact).

### ZBE-15: When the destination is inside the zone, avoidance routing does not help
- Who: last-mile couriers and delivery partners, e-commerce sellers' carriers, trades visiting customers.
- Where: every enforcing city; especially Madrid Distrito Centro, Barcelona, Bilbao and Granada.
- Day-to-day reality: route optimisers and LEZ "avoid" flags (HERE, TomTom) route around zones, but a stop inside the zone cannot be avoided. Compliance depends on which vehicle is dispatched, at what hour, with which permit, or on an exempt car park or hand-off.
- Evidence:
  - HERE avoidance is parameter-based (Euro class, fuel, weight, departure) and avoids a zone if any one parameter matches. — [HERE docs](https://docs.here.com/routing/docs/truck-restrictions-env-zones)
  - Madrid windows are label- and MMA-specific. — [madrid.es DC](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD)
  - Granada car-park exemption. — [Xataka, 2 Oct 2025](https://www.xataka.com/movilidad/granada-multa-hoy-su-nueva-zona-bajas-emisiones-quienes-pueden-acceder-multas-excepciones)
- Scale: all in-zone deliveries; no volume data.
- Cost/impact: €200 per wrong dispatch; idle compliant vehicles (unquantified).
- Driver & status: all municipal ordinances (in force where fining).
- How it is solved today: dispatcher knowledge; route optimisers without ZBE semantics (inference). No Spanish ZBE-aware dispatch product found.
- Software-solvable?: **Yes.** Constraint-aware vehicle assignment (vehicle state, permit state and time windows) via an API.
- Confidence: medium. The mechanism is well evidenced; demand is inferred.

### ZBE-16: Loading and unloading (DUM) windows and night-delivery permits
- Who: suppliers to shops, markets and HORECA (hotels, restaurants, cafés); parcel carriers; e-commerce sellers' delivery partners.
- Where: Madrid (night 23–7h and food 5–7h by declaración responsable valid 1 year); A Coruña (6–11h, 5–12h for Cero and ECO); Córdoba (home delivery and supplier exemptions); Granada (loading exemption form, snippet-level); Málaga (N1 4-year transition, now moot); Zaragoza (DUM authorisation claim, unverified).
- Day-to-day reality: loading rules sit outside or alongside label rules, need yearly re-filing with proof of deliveries (Madrid), and differ by city.
- Evidence: [madrid.es DC](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zona-de-Bajas-Emisiones-de-Especial-Proteccion-ZBEDEP-Distrito-Centro-Empresas-y-profesionales-que-presten-servicios-y-entreguen-o-recojan-suministros/?vgnextfmt=default&vgnextoid=f4f085282f8eb710VgnVCM2000001f4a900aRCRD&vgnextchannel=220e31d3b28fe410VgnVCM1000000b205a0aRCRD); [ecomovilidad A Coruña](https://ecomovilidad.es/zonas-de-bajas-emisiones/la-coruna/la-coruna/); [ecomovilidad Córdoba](https://ecomovilidad.es/zonas-de-bajas-emisiones/cordoba/cordoba/); [ecomovilidad Málaga](https://ecomovilidad.es/zonas-de-bajas-emisiones/malaga/malaga/)
- Scale: unknown.
- Cost/impact: €200 per breach; filing hours (unquantified).
- Driver & status: Madrid OMS and Decreto 178 (in force); A Coruña OMS (BOP 185/2025, in force); Córdoba ordinance (BOP 33/2023, in force).
- How it is solved today: manual filings; loading-zone apps not verified.
- Software-solvable?: **Partly.** A filing and evidence pack is feasible; loading-zone occupancy is a physical constraint.
- Confidence: medium.

### ZBE-17: Exemption paperwork for older and low-income autónomos
- Who: self-employed tradespeople and drivers with old vans, near retirement or on low incomes.
- Where:
  - Madrid: 59+ with ≥50% of the fleet unlabelled, renewed yearly.
  - Barcelona: within 5 years of retirement, until 31 Mar 2028; households under 2× IPREM.
  - Granada: workers under €16,800 income.
  - Valladolid: under 1.3× IPREM.
- Day-to-day reality: exemptions exist but require sworn statements, fleet lists, insurance, ITV and income proofs, renewed per calendar year and per city.
- Evidence: [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [ecomovilidad BCN](https://ecomovilidad.es/zonas-de-bajas-emisiones/barcelona/barcelona/); [Xataka Granada](https://www.xataka.com/movilidad/granada-multa-hoy-su-nueva-zona-bajas-emisiones-quienes-pueden-acceder-multas-excepciones); [ecomovilidad Valladolid](https://ecomovilidad.es/zonas-de-bajas-emisiones/valladolid/valladolid/)
- Scale: unknown number of beneficiaries.
- Cost/impact: €200 fines if lapsed; filing time.
- Driver & status: municipal ordinances (in force).
- How it is solved today: gestorías (administrative agents) and municipal offices (prices not found).
- Software-solvable?: **Partly.** Eligibility checks, reminders and document packs. The users are low-digital, price-sensitive autónomos (inference).
- Confidence: medium.

### ZBE-18: Mismatch between DGT labels and Euro classes in routing data
- Who: fleet-software vendors, international carriers, foreign vehicles.
- Where: national.
- Day-to-day reality: Spanish rules use DGT labels (derived from fuel, Euro class and registration date). Commercial engines take Euro class and fuel (HERE, cargoffer MCP). Foreign vehicles have no label and are mapped by Euro class (Palma's equivalence lists). Mis-mapping yields wrong compliance answers.
- Evidence: [HERE docs](https://docs.here.com/routing/docs/truck-restrictions-env-zones); [Glama cargoffer](https://glama.ai/mcp/servers/cargoffer/zbe-mcp-server/tools/zbe.checkRoute); [BOIB 37, 24 Mar 2026](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590); [bilbao.eus](https://www.bilbao.eus/cs/Satellite?c=Page&cid=1279235266667&language=es&pageid=1279235266667&pagename=Bilbaonet%2FPage%2FBIO_contenidoFinal)
- Scale: unknown.
- Cost/impact: €200 per wrong decision.
- Driver & status: Reglamento General de Vehículos label annex (in force); municipal equivalence tables.
- How it is solved today: vendor approximations.
- Software-solvable?: **Yes.** A label-resolution service by plate or vehicle data. Whether the DGT allows programmatic label lookups was not verified in-session.
- Confidence: medium.

### ZBE-19: No consolidated national dataset of ZBE dates, perimeters and status
- Who: fleet-software vendors, insurers and renting firms, researchers, policymakers.
- Where: national.
- Day-to-day reality: no official table answers "which ZBEs fine, since when, for which vehicles". A public request has gone unanswered for almost a year.
- Evidence: data request of 16 Nov 2025, status "Asignado", no response as of 19 Oct 2026 ([datos.gob.es](https://datos.gob.es/es/solicitud-de-datos/zonas-de-bajas-emisiones)); conflicting press counts ([Motor16](https://www.motor16.com/las-ultimas-noticias/zbe-ciudades-multas-coches/) vs [Fenadismer](https://www.fenadismer.es/los-transportistas-ya-pueden-consultar-todas-las-zonas-de-bajas-emisiones-en-una-sola-web/)).
- Scale: about 150 municipalities.
- Cost/impact: research and vendor curation costs (unquantified).
- Driver & status: RD 1052/2022 art. 10.2 (in force, partly complied with).
- How it is solved today: aggregator sites (ecomovilidad, RACE, Iberfurgo) and NAP files.
- Software-solvable?: **Yes.** A data product and API.
- Confidence: high.

### ZBE-20: Commercial LEZ vendors have unverified Spanish coverage and opaque pricing
- Who: SME fleets and software integrators evaluating HERE, TomTom, urbanaccessregulations.eu and Green-Zones.
- Where: national.
- Day-to-day reality: vendors advertise global LEZ coverage (HERE 19 countries; TomTom 376 cities) but do not list Spanish ZBEs. Prices are not public, and some sources are visibly stale (Green-Zones).
- Evidence: [HERE one-pager](https://assets.here.com/x7rx8ayph7ee/1hLhgrGc50DT8Wtaos2JO7/f914305bc96941845d38c198e276d4e1/HERE-Environmental-Zone-product-one-pager-2021.pdf); [TomTom release notes](https://docs.tomtom.com/routing-api/documentation/tomtom-maps/product-information/release-notes); [green-zones.eu](https://www.green-zones.eu/en/); [Polis Network](https://polisnetwork.eu/?p=16859)
- Scale: n/a.
- Cost/impact: unknown prices (gap).
- Driver & status: n/a (market).
- How it is solved today: enterprise contracts with map vendors (large fleets) and manual lookups (SMEs) (inference).
- Software-solvable?: **Yes** (an opportunity), but incumbents could add Spanish semantics.
- Confidence: medium.

### ZBE-21: Municipal capacity gap: obliged towns are not enforcing or communicating
- Who: municipalities over 50,000 (mid-sized cities especially); indirectly, fleets facing uncertainty.
- Where: Catalonia (17 of 23 not effectively fining; only 4 of 23 with communication plans); Comunitat Valenciana (0 of 15 by Mar 2025, snippet-level); Aragón (delays, snippet-level); Murcia and Las Palmas (no ZBE).
- Day-to-day reality: towns approve ordinances but lack cameras, sanction workflows, registries and communication. Audit bodies flag deficiencies, e.g., in El Prat, Rubí, Sant Boi and Lleida.
- Evidence: [Metrópoli Abierta, 10 Sep 2026](https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html); [À Punt](https://www.apuntmedia.es/noticies/politica/15-municipis-valencians-50-000-habitants-va-implantar-zona-baixes-emissions-2023_1_1832698.html) (snippet-level); [Segre](https://www.segre.com/ca/lleida/260911/la-sindicatura-de-comptes-conclou-que-la-zbe-de-lleida-es-va-implantar-amb-carncies_1327971.html) (snippet-level)
- Scale: about 100 of 150 obliged municipalities may not effectively fine (inference, section 1).
- Cost/impact: risk to aid and EU funds (Valencia €14M, €4M and €115M).
- Driver & status: Ley 7/2021 art. 14; RD 1052/2022; transport-aid decree-laws (in force).
- How it is solved today: public tenders for camera and back-office systems, e.g., Valencia's tender for the ZBE management and control system, Dec 2025 (snippet-level). — [TED notice 866909-2025](https://ted.europa.eu/es/notice/866909-2025/pdf)
- Software-solvable?: **Partly.** Municipal SaaS for registries, whitelists and communication is feasible, but sales go through public procurement.
- Confidence: medium.

### ZBE-22: Funding conditionality drives rushed or "paper" ZBEs
- Who: municipalities; indirectly fleets, through unstable rules.
- Where: national (transport-aid decree-laws); Valencia, Málaga and Alicante as examples.
- Day-to-day reality: cities race to qualify for transport subsidies and EU funds. Some adopt minimal or sanction-free zones (Alicante, the Vox-backed model in Valencia, episode-only proposals in Sevilla), which creates rule churn for fleets.
- Evidence: 2025 condition (snippet-level) ([Astrave](https://astrave.com/noticias/subvenciones-transporte-zbe/)); 2026 relaxation ([Valencia Plaza, 24 Dec 2025](https://valenciaplaza.com/valenciaplaza/valencia/el-ministerio-de-transportes-alivia-a-catala-le-permite-acceder-a-las-ayudas-pese-a-no-contar-aun-con-una-zbe)); Valencia €14M plus €4M ([El Español, 7 Mar 2026](https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html)); Málaga EU-funds risk ([Motorpasión](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)).
- Scale: 141 entities applied for €355M of aid in 2025 (snippet-level).
- Cost/impact: €355M national programme (2025); €115M at risk in Valencia (opposition estimate).
- Driver & status: RDL 1/2025 (2025; snippet-level) and the Dec 2025 decree-law extending aid through 2026 (in force).
- How it is solved today: political negotiation.
- Software-solvable?: **No.** A policy and political problem.
- Confidence: medium.

### ZBE-23: Information phases and switch-on dates create surprise-fine risk
- Who: fleets and autónomos currently receiving warnings only.
- Where: Vigo (fines from 10 Sep 2027), Madrid (resident warnings to 31 Dec 2026), Alicante (open-ended), Badalona (moratorium to 1 Jan 2027), Palma (phase 2 from 1 Jan 2027).
- Day-to-day reality: warnings arrive without cost, so behaviour does not change until the switch-on date, when fines start at full rate.
- Evidence: [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html); [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD); [Metrópoli Abierta](https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html); [BOIB 37](https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590)
- Scale: Vigo about 62,100 unlabelled vehicles at the first switch-on.
- Cost/impact: €200 per fine after switch-on.
- Driver & status: municipal ordinances in grace periods (as listed).
- How it is solved today: nothing specific.
- Software-solvable?: **Yes.** Calendar-driven alerts tied to fleet composition.
- Confidence: high (dates), medium (impact).

### Inferences
- **A coherent product could cover ZBE-01, -03, -15, -19 and -23:** a versioned Spanish ZBE rules API (geometry from the NAP and city portals, semantics curated from ordinances), plus a vehicle-state and permit-state model, plus a dispatch-check endpoint ("can vehicle X serve stop Y at time T?") and an alerts feed.
- **Permit-workflow pains (ZBE-06, -07, -08, -16, -17) are real but fragmented across city portals without APIs.** Automation would require integrations or form-filling.

### Gaps
- No quantified surveys of how many SMEs receive ZBE fines or spend hours on permits.
- No direct user complaints about specific tools (app reviews, forums) were collected in-session.

---

## Top pains
1. **ZBE-02, legal whiplash.** Severity and recency are both high. In 2026 alone Madrid's annulment became final, Málaga's ZBE was annulled and stopped fining, Valladolid's ordinance was annulled, and Barcelona was suspended for eight weeks. Any compliance answer must be time-versioned and legally monitored.
2. **ZBE-01, patchwork of about 150 local rule-sets.** It is the most widespread pain: every multi-city fleet faces it. Rules differ on labels, vehicle category, domicile, hours, quotas and permit models.
3. **ZBE-15, destination inside the zone.** It is structural and unsolved by current routing APIs. The fix is dispatch and permit logic, which is where a SaaS product adds value beyond free polygons.
4. **ZBE-05, ageing fleet (about 1.08M vans and 1.02M trucks aged 20+).** It is the largest economic exposure, but only partly software-solvable. It drives demand for "comply-until-exit" permits and renewal planning.
5. **ZBE-03 and ZBE-19, official data gaps.** The NAP is free but stale and semantically thin, and there is no national status table. These are the direct data-product gap; evidence comes from my own inspection plus an unanswered public data request.
6. **ZBE-04 and ZBE-09, domicile rules plus rented or leased vehicles.** Compliance depends on who holds the vehicle and where it is taxed. This hits renting fleets and out-of-town delivery partners, and is legally fragile (Málaga).
7. **ZBE-14, scheduled B-label phase-outs (2027–2030).** The dates are known in Palma, Catalonia, Bilbao and Vigo. This is a near-term planning pain for the large B diesel-van cohort.
8. **ZBE-10, fine exposure.** Volumes are in the millions (Madrid) at €200 each. The business share is unknown, which lowers confidence.

## Noise and dead ends
- **"Valencia's ZBE fines from 1 Dec 2025 or Jan 2026"** (Carwow, Autopista, theocvalencia). False: the ordinance was rejected on 28 Oct 2025 and there is no ZBE in Oct 2026. — [ecomovilidad Valencia](https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/). The NAP "active" Valencia record is also unreliable.
- **"Vigo fines from Nov 2026"** (Radio Lider, NoMasVueltas). Superseded: the information phase runs to 10 Sep 2027. — [Atlántico, 10 Sep 2026](https://www.atlantico.net/vigo/entran-vigor-zonas-bajas-emisiones_1_20260910-4408680.html)
- **"Málaga restricts B-label vehicles from 30 Nov 2026."** Dead: the ZBE regime was annulled and fines stopped on 14 Oct 2026. — [Motorpasión, 22 Oct 2026](https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero)
- **"Murcia activates sanctions in 2026"** (Motor16 general list). No ordinance has been approved (snippet-level, ecomovilidad and Traficoayuda).
- **"The Supreme Court declared Madrid's ZBE illegal" headlines.** Misleading: the court only inadmitted the cassation appeal, with no merits ruling. Restrictions continue under Ordenanza 2/2026. — [ecomovilidad Madrid](https://ecomovilidad.es/zonas-de-bajas-emisiones/comunidad-de-madrid/madrid/)
- **"Madrid: moratorium for urban-distribution vans throughout 2026"** (Autopista, Jan 2026). Superseded: the actual rule is the open-ended, NO2-conditional transitional regime since 7 Apr 2026. — [madrid.es FAQ](https://www.madrid.es/portales/munimadrid/es/Inicio/Movilidad-y-transportes/Zonas-de-Bajas-Emisiones/Madrid-Zona-de-Bajas-Emisiones/Preguntas-frecuentes-sobre-Madrid-Zona-de-Bajas-Emisiones-ZBE-/?vgnextfmt=default&vgnextoid=9dec1d96b08ed710VgnVCM1000001d4a900aRCRD&vgnextchannel=d2d2edf0f70ab710VgnVCM2000001f4a900aRCRD)
- **"National end of label B in ZBEs from 2026"** (okdiario Talent24h headline). No national rule: B restrictions are municipal or regional, and the label system is reportedly unchanged at least to 2027 (snippet-level, [motor.es](https://www.motor.es/noticias/confirmado-etiquetas-dgt-quedan-como-estan-2025111050.html)).
- **Alicante "extra restrictions at pollution peaks and higher fines for repeat offenders".** Effectively an open-ended moratorium with notices only. — [ecomovilidad Alicante](https://ecomovilidad.es/zonas-de-bajas-emisiones/alicante/alicante/)
- **A Coruña "bans unlabelled and B vehicles"** (Jan 2026 guide). Wrong model: the ZBE is authorisation-based, not label-based. — [ecomovilidad A Coruña](https://ecomovilidad.es/zonas-de-bajas-emisiones/la-coruna/la-coruna/)
- **"Sevilla's ZBE covers the Casco Antiguo, Triana and Alameda."** Only Cartuja is in force; expansion is an opposition proposal. — [ecomovilidad Sevilla](https://ecomovilidad.es/zonas-de-bajas-emisiones/sevilla/sevilla/)
- **"Three-year exemption for hauliers in Barcelona's ZBE"** (older autonomosenruta article). The historic moratoria ended in 2021–2022. — [Ajuntament, 17 Mar 2021](https://ajuntament.barcelona.cat/premsa/2021/03/17/el-31-de-marc-finalitza-la-moratoria-de-la-zbe-rondes-bcn-per-a-les-furgonetes-a-les-quals-no-els-correspon-letiqueta-ambiental-de-la-dgt/)
- **Green-Zones as a Spanish data source.** Visibly stale ("7 zones in Spain"). — [green-zones.eu](https://www.green-zones.eu/en/)
- **"Route optimisation avoids ZBE penalties."** A dead end for in-zone stops: only dispatch, permit and time-window logic works (section 4 inference).
- **Valencia "Urban Sandbox" as a mobility-specific legal waiver.** It is overstated: the sandbox is cross-sector and cannot waive state or DGT rules (art. 11.3). It is useful only as a pilot channel. — [ordinance text](https://sede.valencia.es/sede/descarga/doc/DOCUMENT_1_20240006949868)
- **Refund-claims tooling (ZBE-11).** Likely transient and legal-service-heavy (Madrid, Málaga); weak as a SaaS wedge.
- **Municipal funding conditionality (ZBE-22).** Real but not software-solvable.
- **Business-specific fine statistics.** No city publishes them, so "X% of fines go to vans or businesses" cannot be evidenced. Treat any such number as unsupported.
