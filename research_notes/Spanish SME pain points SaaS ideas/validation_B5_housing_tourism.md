# Validation batch 5: housing, short-term rentals and property (IDEA-29 to IDEA-35)

*Validator: batch 5 of 8. Date of work: 23 October 2026. Status: IN PROGRESS (sections are appended as each idea is finished).*

*Conventions: [new: URL, date seen or published] = fetched or searched in this validation; [notes: PAIN-ID] = stage-1 evidence. "Single-source" marks claims with one source. Prices exclude VAT unless stated. Today is 23 Oct 2026: the Diputación Permanente vote on RDL 29/2026 (expected ~12 Nov 2026) and the 29 Nov 2026 general election have NOT happened yet, so they are treated as scenarios, not outcomes.*

## 1. Batch summary table

(to be filled when all ideas are done)

## 2. Ideas

(appended below as each idea is finished)


#### IDEA-29: ColivEs reshaped: Catalonia-first mid-term lease compliance file (INCASÒL-ready; national module gated on the RDL 29/2026 vote) [user idea U1] — RESHAPE (medium)

**Validated definition (after reshape).** A per-contract compliance file for professional mid-term managers, coliving operators, company landlords and the agents or administradors who file deposits for them. It launches in Catalonia, where the rules are regional law in force since January 2026 and the INCASÒL deposit filing already demands the cause document. It does five things: (1) triage of the tenant profile (tourist stay of 31 days or fewer, temporary lease, or habitual lease); (2) a guided contract with a written cause and a request for matching evidence, kept in a timestamped vault; (3) an INCASÒL filing pack (Model 2 data, the "document que acrediti la finalitat", and the SERPAVI report where needed), prepared for the filer to sign; (4) duration and chaining counters, the end-of-lease condition record and a repair-request timer; (5) a regime stamp on every contract with an automatic re-check when the rules change. The national module (RDL 29/2026: cause, the 12-month and two-contract limits, the one-month extra guarantee, art. 17.8/17.9 caps) is built only once the Diputación Permanente vote (expected ~12 Nov 2026) is known. Dropped from U1: dynamic pricing, eIDAS, and "convert flats into coliving hubs". The light rent-cap and update calculator (IDEA-30) becomes a feature of this product, not a separate product. Price: €8–12 per active contract per month, or €2–3 per bed for coliving, sold to firms rather than to one-flat owners.

**(a) Problem reality and regulation status (23 Oct 2026)**
- **RDL 29/2026 text, verified in the BOE.**
  - **Cause:** art. 7.2 LAU: the cause "deberá ser real y acreditable, recayendo sobre el arrendador la carga de la prueba"; without it the lease loses its temporary nature "con efectos retroactivos a la formalización del contrato".
  - **Duration and chaining:** art. 9 bis: "superior a treinta y un días, y no exceder como regla general de doce meses"; more than two consecutive contracts converts the lease.
  - **Tenant exit and rent:** art. 11.2 allows the tenant to leave after one month. Art. 17.8 caps rises between successive temporary contracts at the IRAV, and art. 17.9 caps the sum of simultaneous room rents.
  - **Guarantees, record and repairs:** art. 36.5 bans requiring rent-default insurance; art. 36.7 presumes good condition without a signed end-of-lease document; art. 21 bis covers repairs.
  - **Transition and regions:** DT 8ª keeps pre-decree contracts as "uso distinto" until they expire. DA 12ª preserves regional civil law. Entry into force: day after publication (DF 11ª), i.e. 8 Oct 2026.
  - **Missing rule:** the decree has **no transitional rule on what happens if it lapses**. [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20823, seen 23 Oct 2026]
- **Convalidation vote: still in the future, and fragile.**
  - **Date and forecast:** the vote is "prevista para el 12 de noviembre de 2026", with a forecast of "35 votos a favor y 34 en contra" because the PNV announced support. The page itself says these "Son previsiones, no un resultado". Diputación Permanente seats: PP 27, PSOE 25, Vox 6, Sumar 6, and one each for ERC, PNV, Junts, Bildu and Podemos (single source: [new: https://gestionatualojamiento.com/convalidacion-del-decreto-de-vivienda/, published 18 Oct, updated 20 Oct 2026]). idealista also reports PNV support ("el PNV ya ha dicho públicamente que lo apoyará") [new: idealista, 13 Oct 2026, https://www.idealista.com/news/inmobiliario/vivienda/2026/10/13/918359-que-cambia-para-los-propietarios-con-los-decretos-prorrogas-tope-al-alquiler-del-2].
  - **Timing rule:** the 30-day period runs in working days (Reglamento del Congreso art. 90.1: "se computarán en días hábiles") [new: https://www.boe.es/buscar/act.php?id=BOE-A-1982-5196, seen 23 Oct 2026].
  - **My inference on the count:** PP + Vox + Junts = 34 against, so the decree passes only if all 35 others attend and vote yes. A 34–34 tie that persists means rejection: art. 88 says "se entenderá desechado" [same BOE source]. The sister decree RDL 26/2026 fell 172–178 in Congress on 2 Oct [notes: HOU-02].
  - **Verdict on the vote:** convalidation is more likely than not, but it hangs on one vote and full attendance. Search 1 found no reported Junts or Podemos position.
- **If it lapses:** repeal works "pro futuro", not as nullity (LegalToday, L. M. Feito, 8 Oct 2026 [new: https://www.legaltoday.com/opinion/articulos-de-opinion/los-decretos-leyes-de-vivienda-derogacion-reaprobacion-y-convalidacion-en-plena-disolucion-2026-10-08/]).
  - **Contracts signed meanwhile:** contracts signed between 8 Oct and the vote are generally judged under the law at signature, which is "Un buen argumento, no una garantía" (LeaseGuard blog, updated 23 Oct 2026 [new: https://getleaseguard.com/blog/que-pasa-si-no-se-convalida-decreto-vivienda]). gestionatualojamiento says "los efectos producidos mientras el decreto estuvo en vigor se mantienen".
  - **VAT:** the 10% VAT on stays of 30 nights or fewer starts on 1 Dec 2026 (art. 7), so it would never apply.
  - **Product consequence:** a lapse creates exactly the date-versioned regime problem this product sells. Contracts from 8 Oct to ~12 Nov would sit under a dead regime, and pre-8 Oct contracts would stay "uso distinto".
- **Election (29 Nov 2026; not yet held).** The decree debate "se ha aplazado, no se ha cerrado"; the substantive debate belongs to the new Cortes (LegalToday, above). No party programme was checked (budget). This is my inference: a PP/Vox majority could repeal or replace the national seasonal rules by decree-law in 2027. The national module therefore carries 12-month political risk even if convalidated.
- **Catalonia: the durable anchor.**
  - **Constitutional Court:** the Court admitted the PP deputies' appeal against arts. 2.2, 3.8, 5.5, 5.6, 5.8, 5.9, 5.14, 5.15 and 8.1 of Llei 11/2025. No suspension is reported, and an appeal by deputies does not suspend a law automatically [new: search 2 → idealista/ca, 15 Jun 2026, https://www.idealista.com/ca/news/immobiliari/2026/06/15/901949-el-constitucional-admet-el-recurs-del-pp-contra-la-regulacio-del-lloguer-temporal-i-les]. Experts estimate a ruling could take about four years [new: 3Cat, 16 Mar 2026, https://www.3cat.cat/3catinfo/dos-anys-del-topall-als-lloguers-els-preus-sestabilitzen-pero-no-baixen/noticia/3399849/]. Precedent: in March 2022 the Court annulled the key points of Catalonia's 2020 cap law on a PP appeal [search 2 snippet, same 3Cat/Vilaweb results]. That is a medium-term risk, not a 2026–27 one.
  - **INCASÒL filing already enforces the cause document:** "Per als contractes de lloguer d'habitatge temporal formalitzats a partir de l'1 de gener de 2026: cal adjuntar el document que acrediti la finalitat". Habitual leases signed from 26 Mar 2026 must annex the SERPAVI report (FAQ: art. 10.10 Decret llei 3/2026). A third party may file "en nom de la part arrendadora", identifying itself digitally [new: https://incasol.gencat.cat/ca/serveis-i-tramits/fiances-de-lloguers/informacio/diposit-de-fiances, seen 23 Oct 2026]. The INCASÒL FAQ adds that deposit and registration are mandatory for room and fragmented-housing contracts signed from 14 Jul 2026 [new: https://incasol.gencat.cat/ca/serveis-i-tramits/fiances-de-lloguers/informacio/preguntes-mes-frequeents, seen 23 Oct 2026].
  - **Coliving and the cap (C-14): unresolved.** Pisos.com says coliving "queda fora"; the Sindicat de Llogateres says the law applies; the Generalitat is "analitzant com abordar el fenomen del coallotjament" [new: 3Cat, 16 Feb 2026, https://www.3cat.cat/3catinfo/els-habitatges-de-coliving-es-doblen-en-dos-anys-estan-dins-o-fora-del-topall-de-preus/noticia/3394906/]. Search 2 found no later official interpretation. A product must handle both readings.
- **Enforcement: real but thin, so the main penalty is civil, not administrative.**
  - **Administrative files:** Catalonia opened 13 sanction files (7 Consum, 6 Habitatge) plus 132 preliminary inquiries. Fines: €27,000 in total for two serious Consum cases; €1,750 paid for a missing index in an ad; Habitatge two at €30,000 and two at €3,000; range "entre 3.000 i 90.000 euros" [new: https://consum.gencat.cat/ca/detalls/noticia/primers-sancionadors-contencio-preu-lloguers, 3 Feb 2026]. The note does not say whether any case involved seasonal or room lets.
  - **Inspection capacity:** by March 2026 only "3 sancions" had been imposed, and inspectors were "only now" being incorporated (3Cat, 16 Mar 2026, above).
- **Courts keep re-classifying, whatever happens to the decree.**
  - **SAP A Coruña, 26 Feb (2026 per the notes):** an 11-month-15-day lease to a tenant "testing" the city was ruled a "simulación relativa", so the company landlord faces 7 years. Indicators: rent in full months, a deposit lodged on an annual rent of €4,800, utilities and insurance imposed on the tenant, a pre-emption waiver, an extension clause, and no objective event bounding the term ("la duración, por sí sola, no determina la existencia de un verdadero alquiler de temporada") [new: idealista, 6 Jul 2026, https://www.idealista.com/news/inmobiliario/vivienda/2026/07/06/901838-la-clave-no-es-la-duracion-cuando-un-alquiler-de-temporada-pasa-a-ser-de-vivienda].
  - **SAP Cantabria 166/2026, 10 Mar 2026:** a room let as a permanent home falls under the LAU.
  - **Counter-example, SAP Cantabria 69/2026, 14 Jan 2026:** a 15-day term was upheld as seasonal [new: search 3 → search-level summaries of blog.elabogado.com, 15 May 2026, and noticiastrabajo.es; full texts not read; verify in CENDOJ].
  - **Gap:** search 3 found no ruling yet applying RDL 29/2026 itself, which is too recent.
- **SES.Hospedajes for 32–90-day leases: most likely out of scope.** RD 933/2021 defines "actividades de hospedaje" as providing "habitación o espacio para la pernoctación"; its examples are hotels and lodgings "de carácter turístico", and it never mentions the LAU [new: https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461, consolidated text last updated 27/10/2021]. Since RDL 29/2026 makes a temporary lease a LAU housing lease (art. 2.3) and caps tourist lets at 31 days (art. 5.e), my reading is that SES does not apply. That rests on the text, not on official guidance: the Interior page returned 403, and search 7 found nothing. Keep a reporting module out of the MVP.
- **Fianza, one month or two (C-14): mostly settled.** LAU art. 36.1 sets "una mensualidad de renta en el arrendamiento de viviendas" and two for "uso distinto" [new: https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003, consolidated 07/10/2026]. A vivienda temporal is a housing lease (art. 2.3), so the deposit is one month. INCASÒL's FAQ agrees ("contractes d'arrendament temporals per raons professionals, laborals, d'estudis": one month). Lázaro Amable reads it the same way ("Es la lectura literal; antes, como uso distinto, eran dos, y aún no hay jurisprudencia") [new: https://lazaroamable.com/blog/alquiler-temporada-canarias-contrato-temporal, 22 Oct 2026]. INCASÒL's deposit page still cites the old two-month base (Decret 147/1997) for seasonal contracts. **Answer:** one month while RDL 29/2026 stands; two again for contracts that revert to "uso distinto" if it lapses. That is one more versioning rule.

**(b) Competitors (Spain and abroad)**
| Product | URL | Price | Segment | What it covers / gap |
|---|---|---|---|---|
| Homming | https://homming.com/planes-de-precios | Starter €47/month on annual billing (€59 monthly) for 1–10 assets; Advanced €95 (€119); Enterprise €143 (€179); more than 50 assets on quote. **No free tier for managers** (the notes said 1–5 free properties: contradicted) | Landlords and managers, medium and long term, rooms | Contract templates, Signaturit e-signature (120/yr on Starter), rent updates, fianza management, incidents, tenant scoring. Its **October 2026 changelog has nothing on RDL 29/2026**, temporary leases, causes or caps [new: https://help.homming.com/es/articles/12874623-novedades-del-mes, seen 23 Oct 2026]. Best-placed incumbent to add a "cause" field |
| Captain.Legal | https://www.captain.legal/es/inmobiliario/contrato-de-arrendamiento-de-temporada-word-y-pdf/ | "Desde 4,90 € / doc"; unlimited subscription (price not shown) | DIY landlords | Region-aware generator (warnings on cap, documents and deposit body). The tenant's habitual domicile is mandatory, and there is a cause annex ("matrícula, contrato laboral, informe hospitalario") and an inventory with dated photos. **Still framed on art. 3.2 LAU with a two-month fianza; "Actualizado el 24 de julio de 2026"**, so not yet updated for RDL 29/2026. Offers "Captain.Legal en tu IA" (mcp.captain.legal) [new: seen 23 Oct 2026] |
| Vivara (free tools) | https://herramientas.vivara.io/ | Free (lead generation for paid management) | Landlords and tenants | IRAV/IPC rent-rise calculator, tensioned-zone check, clause-by-clause "Revisor de contrato de alquiler", end-of-contract checklist, "Radiografía de alquiler por habitaciones" (already cites the 8 Oct rule) [new: seen 23 Oct 2026] |
| LeaseGuard | https://getleaseguard.com | Free diagnosis; €39 one-off for the report plus burofax | **Tenants** | Clause-by-clause audit against the LAU and Ley 12/2023, plus a burofax. It raises the pressure on landlords' files and shows AI lease-audit tools shipping within days of the decree [new: seen 23 Oct 2026] |
| Spotahome | https://plans.spotahome.com | 8% / 10% / 15% of total contract value, "for properties in UK and Ireland"; Spanish rate not shown | Mid-term marketplace | Solvent-tenant checks, rent guarantee, check-in/out. No cause documentation; it tells landlords to ask their lawyer [new: seen 23 Oct 2026] |
| Law firms and managers (Lázaro Amable/ALY, DiG, fincasbonet, Sepin) | e.g. https://lazaroamable.com | Management 8–12% of monthly rent (long-term), 15–25% (holiday), plus IGIC | Owners | They draft the temporary contract "with the cause and supporting documents" inside a management fee [new: seen 23 Oct 2026] |
| Rentger | https://rentger.com | Not verified (403) | PM software | Unverified, an open check |

- **No landlord-side tool found that combines** a cause-evidence vault, chaining counters and regime versioning. Searches 4 and 5 returned only law-firm explainers. That is absence of evidence from two searches, not proof.
- **The template layer is already commoditised** (€4.90 or free), and AI review tools exist on both the landlord and tenant sides.

**(c) Buyers and market size**
- **Demand-side proxies:**
  - Seasonal lets are 34% of rental listings nationally: Barcelona 57%, Málaga 37%, Madrid 35%, Valencia 35%. Seasonal supply is +7% year on year nationally, Madrid +52%, Barcelona −37% [new: Pressdigital/idealista, 20 Oct 2026, https://www.pressdigital.es/articulo/economia/2026-10-20/6058369-oferta-alquiler-permanente-cae-10-espana-mientras-temporal-crece-7-segun-idealista].
  - Consumo: "1,15 millones de personas" live in seasonal or room rentals, about 422,000 of them against their wishes. No methodology, and no count of contracts or landlords [new: idealista, 7 Sep 2026, https://www.idealista.com/news/finanzas/economia/2026/09/07/912998-consumo-estima-que-mas-de-un-millon-de-personas-vive-en-alquiler-de-temporada-o-de].
- **Supply-side proxies:**
  - About 58,900 temporary-rental NRUA applications by Jan 2026 (14.7% of 400,362), a floor for units [notes: HOS-13].
  - 19,089 operating flex-living beds (JLL), about 20,000 coliving rooms [notes: HOU-04, HOU-18].
  - INCASÒL took 28,079 deposits of all lease types in Q1 2026, 20,141 of them in Barcelona province, with no split by type [new: search 6 → habitatge.gencat.cat lloguers per àmbits geogràfics, Q1 2026].
- **Nomad demand: better than the notes' single source.** UGE teleworker (DNV) permits stood at 44,966 in Sept 2025: Barcelona 15,073, Madrid 8,087, Málaga 4,916 [notes: EXP-08, El Nacional 12 Feb 2026, attributed to the UGE]. That supersedes the 27,875 figure (end-2024).
- **Paying entities (my estimate):** professional mid-term managers, coliving operators, company landlords and agencies with mid-term books, in the low thousands to about 10,000 nationally, with Catalonia a fraction. No official count exists.
- **Revenue ceiling (my calculation):** 20,000–40,000 professionally managed mid-term units × €10/month × 12 = €2.4–4.8M a year in Spain if every unit were captured. At a realistic 10–20% share, that is €0.25–1M ARR. Coliving adds 20,000 beds × €2.5 × 12 = €0.6M at full capture. **This is a niche product, viable for a 1–3 person team, not a large market.**

**(d) Willingness to pay (anchors)**
- **Lawyers and gestorías:** drafting a residential lease costs €120–300 and a review €50–75 (search-level, several law-firm blogs) [new: search 8 → blog.melendos.es, derechojudicial.com, 2026]. ANA puts drafting at "entre 150 y 300 euros" and agency fees at "entre el 50% y el 100% de una mensualidad" [new: https://agencianegociadoradelalquiler.es/cuales-son-los-gastos-del-contrato-de-alquiler-que-debe-asumir-el-propietario/, 11 Oct 2024].
- **Management and software:** management fees are 8–12% of rent (ALY), or 6–10% [notes: CON-12]. Homming starts at €47–59/month.
- **Insurance:** rent-default insurance costs €306–658 a year on €950 rent; Mutua's seasonal product costs €129.78–183.85 [new: OCU, 28 Sep 2026, https://www.ocu.org/fincas-y-casas/gestion/seguros-y-prestamos/analisis/2026/07/comparativa-seguros-impago-rentas].
- **Reading:** €8–12 per active contract per month (€48–72 over a 6-month lease) sits below one lawyer-drafted contract and far below the cost of a 5–7-year re-classification. Adjacent spend is clear. **Direct willingness to pay for software is unproven** [I].

**(e) Distribution (evidence)**
- **Filing intermediaries:** electronic filing at INCASÒL is mandatory for legal persons and for licensed professionals such as administradors (Llei 39/2015 art. 14.2). INCASÒL runs a "Concerts" mailbox (fiances.concerts@gencat.cat) for professional filers [new: INCASÒL FAQ]. The Cambres de la Propietat Urbana take in-person deposits. Together these give concentrated filers and landlord bodies who already handle every Catalan contract. Their partner appetite is unproven [I].
- **Other channels:**
  - AICAT (mandatory Catalan agent register) and the API/COAPI colleges;
  - ICAB courses on RDL 29/2026 [notes: HOU-02];
  - the law firms publishing on the topic, as referral or co-branding partners;
  - coliving operators named by JLL (Be Casa 21%, Livensa 10%, Cotown 8%, Smart Rental 7%, Node Living 7%) [notes: HOU-18].
- **Search demand:** high intent, but the results pages are saturated with law-firm explainers (searches 4, 5 and 7). Content marketing will be contested.

**(f) Build feasibility and legal constraints**
- **MVP for 1–3 people with AI tools: about 6–8 weeks.** It needs a rules engine, templates reviewed by a partner lawyer, a timestamped vault, Signaturit or another e-signature API, counters and alerts, a condition-record app and the INCASÒL pack.
- **INCASÒL filing:** no API or bulk service is published. A third party may file but must identify digitally (above), so the realistic MVP prepares the pack and the filer signs. Holding clients' certificates is a security and liability risk; avoid it.
- **Legal and data constraints:**
  - Selling templates and workflow is lawful (Captain.Legal does it), but the product must not hold itself out as legal advice. Professional-liability insurance and partner-lawyer review are needed.
  - Employer letters, enrolment letters and IDs are personal data, which calls for a DPIA, retention rules and EU hosting.
  - SES is out of scope (above).

**(g) Defensibility against AI copies and incumbents**
- **Weak at the template layer:** €4.90 generators, free AI reviewers, and Homming able to add a cause field.
- **Moderate only if** the product accumulates (i) a rules history versioned by date and region, kept current through one lapse or replacement cycle; (ii) a re-classification risk model built from rulings; (iii) INCASÒL-filer and law-firm channel partners; (iv) each client's evidence vault, which makes switching costly.
- **Speed:** shipping before Captain.Legal and Homming update for RDL 29/2026 is a short window of weeks, not a moat.

**(h) Kill criteria (longlist)**
1. *Convalidation fails and Catalan operators will not pay at least €8 per contract.* **OPEN.** The vote is pending, about 12 Nov 2026, and the Catalan willingness-to-pay interviews have not been run.
2. *A law firm or legal-tech tool already sells the same file.* **NOT MET for the lifecycle file; MET for the template layer.** Captain.Legal sells contract plus cause annex plus inventory for €4.90, and law firms draft per contract. Nobody was found selling the vault, counters and regime stamp.
3. *Interviews show courts and landlords do not value documentary cause evidence.* **Courts: NOT MET.** A Coruña relied on documentary indicators, and INCASÒL requires the cause document at filing. **Landlords: OPEN** [I].

**Scores (reshaped version)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | An enforced duty in Catalonia now and nationally since 8 Oct, with a severe civil penalty (5–7-year re-classification); but the national half may lapse within weeks and Catalan administrative enforcement is thin |
| S2 Buyers | 2 | Professional mid-term managers, coliving operators and company landlords number roughly 5k–20k at most (no official count) |
| S3 Willingness to pay | 4 | Clear adjacent spend: €120–300 per lawyer contract, 8–12% management fees, €47+/month PM software |
| S4 Reachability | 3 | INCASÒL filers, Cambres, AICAT and law firms exist as concentrated channels, but none has a proven partner programme |
| S5 Competitive gap | 4 | Only lawyers, €4.90 templates and generic PM software; no lifecycle cause-evidence tool found |
| S6 Build speed | 4 | 1–2 months; no certification; lawyer review needed |
| S7 Defensibility | 2 | Templates and calculators are already free or €4.90 and AI-generated; the moat is only rules upkeep plus vault lock-in |
| S8 Retention | 4 | A legal duty on every contract plus accumulated evidence; but owners exit mid-term letting (Barcelona −37%) |
| **Sellability** | **3.38** | mean of S1–S8 (27/8 = 3.375) |
| **P** | **4** | Re-classification costs far more than €1k a year per affected unit; frequency is unmeasured (no case counts) |
| **Overall** | **3.63** | 0.6 × 3.375 + 0.4 × 4 |

**Open [I] checks**
- Interview 10 Catalan mid-term managers or coliving operators (Be Casa, Cotown, Smart Rental, Node Living, Vandor, AICAT members) on their current file, legal spend per contract, and €8–12 per contract.
- Ask 3 INCASÒL "concert" filers or administradors whether they would push a filing pack to their clients.
- Ask 2 partner law firms (for example ALY, DiG) whether they would co-brand templates and take escalations.
- Ask Homming and Rentger whether a cause and RDL 29/2026 module is on their roadmap.

**What would change the verdict**
- **Towards GO:**
  - RDL 29/2026 convalidated and not reversed after 29 Nov;
  - at least 5 of 10 interviewed operators commit to a paid pilot at €8 or more per contract;
  - an INCASÒL filer or Cambra agrees to distribute.
- **Towards KILL:**
  - Homming, Rentger or Captain.Legal ship a cause-evidence vault with regime versioning before launch;
  - interviews show operators simply stop letting mid-term or rely on their lawyer's template;
  - the lapse plus a PP/Vox repeal leaves only a shrinking Catalan market.

**User's original ColivEs (U1): claims and features after validation**
| U1 claim or feature | Verdict | Evidence |
|---|---|---|
| Rent-cap and regional legal compliance automation | **SURVIVES (core), narrowed.** Regional compliance (cause, duration, deposit, condition record, regime versioning) is the product. Rent caps matter only in Catalonia among the three target cities (Barcelona is tensioned; Madrid and Málaga are not); outside it, only the art. 17.8/17.9 caps apply, and they lapse with the decree | BOE RDL 29/2026; INCASÒL; Pressdigital/idealista 20 Oct 2026 |
| eIDAS (EU digital identity) verification | **DOES NOT SURVIVE.** Landlords are not obliged to accept the EUDI wallet (private acceptance from 24 Dec 2027 binds only regulated sectors and very large platforms), and Spain's wallet has no launch date. Commodity KYC at about $0.33 a check is enough | [notes: HOU-10] |
| Dynamic pricing based on digital-nomad movements | **DOES NOT SURVIVE** while RDL 29/2026 stands: art. 17.8 caps rises between successive temporary contracts at the IRAV (verified verbatim), and Catalan caps add to it. If the decree lapses it revives outside Catalonia, but as a commodity (PriceLabs at $19.99 per listing) | BOE; [notes: HOU-22] |
| Converting tourist flats into coliving hubs | **DOES NOT SURVIVE as a product.** It is planning law: Madrid requires exclusive buildings; Barcelona enforces against NAD and Vandor; the Barcelona PGM change is pending. Barcelona's seasonal offer is −37%. At most it becomes a feasibility checklist | [notes: HOU-18, HOU-19]; Pressdigital 20 Oct 2026 |
| "Severe housing shortage" | Supported but structural; a demand driver, not a feature | [notes: HOU-20, CON-12] |
| "Strict municipal crackdowns on holiday licences" | Supported (Barcelona's HUT licences end Nov 2028; Madrid Plan Reside; Málaga's 43 barrios) | [notes: HOS-18, HOS-19, HOS-20] |
| "Constant influx of high-earning nomads" | **Partly supported:** 44,966 DNV permits (Sept 2025), Barcelona 15,073, Madrid 8,087, Málaga 4,916. But people "moving their life here" do not fit the temporary cause, which shrinks the lawful mid-term demand | [notes: EXP-08, HOU-23]; Lázaro Amable 22 Oct 2026 |
| Target cities Barcelona, Madrid, Málaga | Barcelona is durable (regional law); Madrid and Málaga depend on the national decree | above |


#### IDEA-30: Rent-cap, update and deadline autopilot for landlords and rental agencies — KILL (high)

**Verdict detail:** KILL as a standalone ~€5/month product; MERGE into IDEA-29 as its light tier, or give it away as a free calculator for lead generation.

**Validated definition.** A set-and-forget service per lease that computes the legal first rent (tensioned zones), the annual update (IRAV, the 2% cap until 31 Dec 2027, and no rise if the rent is above the index), deposit-lodging deadlines and the RDL 29/2026 extension windows, and sends draft notices and "rule changed" alerts. **Reason for the kill as a standalone ~€5/month product:** the calculation layer is already given away free by a portal (Fotocasa), the ministry, managers (Vivara) and INE. The remaining alert layer is an annual event that does not justify a monthly fee. It belongs inside IDEA-29, or in agency and PM software (Homming already bundles rent updates and fianza management), not in a separate subscription.

**(a) Problem reality and regulation status**
- **The 2% cap is binding now.**
  - **Cap rule:** DF 6ª(b) of RDL 29/2026: "el incremento de la renta a aplicar no podrá ser superior al dos por ciento" for updates due from entry into force to 31 Dec 2027. Art. 18 LAU caps updates at the IRAV [new: BOE RDL 29/2026 and consolidated LAU, seen 23 Oct 2026].
  - **IRAV:** 2.54% for Sept 2026, published 14 Oct 2026, "máximos" since INE began publishing it [new: search 9 → elEconomista, Oct 2026, https://www.eleconomista.es/vivienda-inmobiliario/noticias/14020787/10/26/el-indice-de-referencia-del-ine-para-la-actualizacion-del-alquiler-escala-a-maximos-del-254-en-septiembre-aunque-se-mantiene-muy-por-debajo-del-ipc.html; also Fotocasa, 14 Oct 2026].
  - **CPI:** 4.9% for Sept 2026, core 3.1% [new: INE, https://www.ine.es/dyngs/Prensa/es/IPC0926.htm, 14 Oct 2026].
  - **What each regime means:** while the decree stands, the update is the lower of 2% and the IRAV. If it lapses around 12 Nov, the IRAV (2.54%) applies to contracts signed since 26 May 2023, and contracts with an IPC clause revert to their own index.
- **Many sources are already out of date.** Lexway's page says "no existe ningún tope extraordinario" because RDL 8/2026 was rejected [new: https://lexway.es/actualizacion-renta/, seen 23 Oct 2026]. Alquigest (28 Sep 2026) says the 2% cap is "ya no está vigente" [new: https://alquigest.com/noticias/actualizacion-renta-alquiler-irav-ipc/]. Both predate or ignore RDL 29/2026. Confusion is real, but it is fixed with a free, up-to-date calculator, not a subscription.
- **Tensioned zones.** 53 new Catalan municipalities were added by Resolución TER/3740/2026 (DOGC 19 Oct 2026), "Pendiente de publicación en el BOE", with a three-year duration [new: OCU, 20 Oct 2026, https://www.ocu.org/fincas-y-casas/gestion/alquiler/analisis/2026/10/nuevas-zonas-tensionadas-cataluna]. Counts by region conflict (C-14):
  - Basque Country: 15 (Vivara, 9 Sep 2026 [new: https://www.vivara.io/blog/legal/zona-tensionada-alquiler/]); 17 (Inmostats, latest resolution BOE-A-2026-9175 of 27 Apr 2026 adding Pasaia, Zestoa and Arrasate [new: https://inmostats.com/alquiler/zonas-tensionadas]); 17–19 [notes: CON-17].
  - National total: 310 (Inmostats) against 317 (Vivara, whose own regional figures sum to 314).
  - Galicia: Santiago reported as approved by Vivara and as awaiting the BOE by Inmostats.
  - Not settled from official sources: the MIVAU page again returned 403.

**(b) Competitors (free and paid)**
| Product | Price | What it does |
|---|---|---|
| Fotocasa "Calculadora del límite de la actualización del precio del alquiler" (portal) | Free | Updated 14 Oct 2026; cites the IRAV at 2.54%; applies the "máximo del 2%" and "limitada al 0% si la renta actual supera el índice" [new: https://www.fotocasa.es/fotocasa-life/alquiler/como-funciona-la-actualizacion-del-precio-del-alquiler-con-el-nuevo-indice/] |
| Ministry of Housing (MIVAU) calculator; SERPAVI | Free | Official maximum-update calculator and reference index (linked by Fotocasa and Lexway; the MIVAU pages block automated access) |
| INE "Actualización de importes con el IPC" | Free | CPI update calculator [new: https://www.ine.es/calcula/] |
| Vivara free tools | Free | IRAV/IPC rent-rise calculator, tensioned-zone check, contract reviewer, end-of-contract checklist [new: https://herramientas.vivara.io/] |
| EvitaLios, infocontrato.es, gibobs | Free (not verified individually) | IRAV tables and calculators [new: search 9 results] |
| Homming | From €47/month (annual billing) for 1–10 assets | Rent updates, fianza management, contract templates, incidents [new: https://homming.com/planes-de-precios] |
| Managers (Alquigest, Vivara, ALY) | 8–12% of rent (ALY) | Do the update as part of management |

**Kill criterion "a free portal calculator" is met** for the calculation. Gap left: per-lease reminders, a draft notice and rule-change alerts. That is a feature of PM software, not a product.

**(c) Buyers and market size**
- **Declarants:** the AEAT IRPF 2023 statistics show **3,142,656 declarants with "Ingresos íntegros de Capital Inmobiliario"** (partida 102, €29.50bn) and 3,149,849 with net income from "inmuebles arrendados o cedidos a terceros" (partida 156) [new: https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/irpf/2023/jrubik7d01929e1a5abe97cbf3612458d906e34a9bda7.html, seen 23 Oct 2026].
- **Caveats:** these counts are persons (co-owners count separately) and cover all leased property types, not just homes. Coverage is probably common territory only, excluding the Basque Country and Navarra; this is my reading, since the page does not state it.
- **Ceiling:** buyers are clearly over 500k. At €5/month and a 1% paid conversion, about 30,000 payers would give about €1.8M ARR (my calculation). The conversion rate is the unknown, and free tools push it down.

**(d) Willingness to pay**
- **Weak.** Free calculators from a portal and the ministry, gestorías bundling the work, PM software from €47/month, managers at 8–12%.
- **Not viable at ~€5/month as a type C product.** The visible value comes once a year (the anniversary update) plus rare rule changes, and support load rises with every legal change. If kept at all, it should be €19–29 a year as an add-on, or free as lead generation for IDEA-29 or for agencies. That price is unproven.

**(e) Distribution**
- **Channels:** agencies as white-label resellers (Homming already serves them), Cambres de la Propietat, landlord associations, and SEO.
- **Search results are saturated:** search 9 returned nine pages with IRAV calculators and tables, from a portal, managers, a bank-broker (gibobs) and law firms.

**(f) Build feasibility**
- **Time to build:** under 4 weeks.
- **Data:** the IRAV is published monthly by INE. SERPAVI values come per address from the official web tool; no bulk API was found (not verified). Zone lists must be curated from BOE and DOGC resolutions, because the ministry page blocks bots.
- **Liability:** wrong caps carry liability, and Catalan ad-disclosure fines of €1,750–10,000 have been imposed [new: Consum, 3 Feb 2026].

**(g) Defensibility**
- **None.** It is trivially copyable, and Fotocasa had already shipped the 2026 logic within six days of the IRAV release.

**(h) Kill criteria**
1. *Portals or Homming give equivalent calculators away.* **MET** (Fotocasa, MIVAU, Vivara, INE).
2. *Fewer than about 1 in 10 landlords would pay €5/month.* **OPEN** [I], but the free substitutes make a pass unlikely.
3. *Official zone and index data cannot be obtained reliably.* **PARTLY MET.**
   - Obtainable: the IRAV.
   - Fragile: the zones (403 on the ministry page, conflicting secondary counts, 53 Catalan municipalities pending in the BOE) and SERPAVI (per-address web tool only).

**Is IDEA-30 a light tier of IDEA-29? Yes.** Same rules engine (date and region versioning), same buyers on the professional side, and the calculator is the natural free entry point. Recommendation: give the calculator away as lead generation, and charge only inside IDEA-29's per-contract file or as a white-label module for agencies.

**Scores (standalone type C version, as proposed)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | A recurring anniversary update and rules in force (2% cap until Dec 2027), but no hard filing deadline; the cap itself is lapse-prone |
| S2 Buyers | 5 | About 3.1M IRPF rental-income declarants (2023) |
| S3 Willingness to pay | 2 | Free portal and ministry calculators; managers and PM software bundle it |
| S4 Reachability | 2 | Diffuse individual landlords; search results crowded with free tools |
| S5 Competitive gap | 2 | Several decent free calculators; only the per-lease alert layer is thin |
| S6 Build speed | 5 | Under 4 weeks |
| S7 Defensibility | 1 | Trivially copyable; Fotocasa updated in six days |
| S8 Retention | 3 | Periodic (annual) use; churn-prone |
| **Sellability** | **2.88** | 23/8 = 2.875 |
| **P** | **3** | Mis-set updates cost little per year; Catalan ad and cap fines (€1,750–90,000) and Madrid deposit fines (up to €90k) are real but infrequent |
| **Overall** | **2.93** | 0.6 × 2.875 + 0.4 × 3 |

**Open [I] checks**
- Survey 100 landlords: would they pay €19–29 a year for per-lease reminders plus a draft notice? The original test, €5/month with at least 1 in 10 willing, would be replaced.
- Would 3 agencies white-label the tool at €1–1.50 per lease?

**What would change the verdict**
- Evidence that landlords pay for reminders despite free calculators, for example a competitor with thousands of paying small landlords.
- An agency or Cambra white-label deal.


#### IDEA-31: Landlord-paid tenant screening and trust pack for foreign and mid-term tenants — KILL (medium)

**Verdict detail:** KILL as a standalone product. Keep the screening and evidence-intake step as a module of IDEA-29, with a referral to an existing guarantor (SEAG/Garantilo).

**Validated definition.** An agency- or landlord-paid applicant link: commodity KYC, cross-border income evidence, an affordability check, a standard scorecard with an anti-discrimination audit log, plus a "verified landlord" ownership check. **Reason for the kill as a standalone product:** each layer already has a Spanish product.
- **Open-banking score:** SKOR.
- **Guarantee for passport-only foreign tenants:** Garantilo, an agent of SEAG.
- **Scoring bundled into PM software:** Homming.
- **Screening bundled into landlord-paid rent-default policies:** insurers.
- **KYC and document OCR:** Didit, about $0.33 a check with 500 free a month.

The urgency rests partly on RDL 29/2026's guarantee caps, which may lapse. What survives is a **screening and evidence-intake step inside IDEA-29**. There the same documents prove the temporary cause and the tenant's solvency, and a referral fee comes from an existing guarantor instead of a scoring model of our own.

**(a) Problem reality and regulation status**
- **Tenant-side fees: banned and enforced.** Art. 20.2 LAU: management and formalisation costs "no podrán ser repercutidos al arrendatario" [new: BOE RDL 29/2026, verbatim].
  - **Alquiler Seguro fine now final:** Consumo's **€3.6M fine on Alquiler Seguro became final in the administrative route on 8 Apr 2026** ("La resolución deviene firme y agota la vía administrativa"). It comprises six very serious infractions (€1,000,000; €990,900; 3 × €500,000; €100,001) and one serious (€10,001).
  - **Conduct punished:** imposing a "Servicio de Atención al Inquilino" (treated as management and formalisation costs), home insurance for the landlord's benefit, charges for debt and court claims, a blacklisting clause, and excluding the right of withdrawal.
  - **More to come:** a second agency is under investigation [new: https://www.dsca.gob.es/en/comunicacion/notas-prensa/consumo-multa-36-millones-euros-alquiler-seguro-practicas-abusivas-sus, 8 Apr 2026]. Alquiler Seguro will appeal to the courts [new: search 12 → idealista, 9 Apr 2026].
  - **Notes corrected:** the official release does not name an "estudio de solvencia"; that label came from press coverage [notes: CON-11].
  - **Conclusion:** the screening must be paid by the landlord or agency. That is consistent with the idea.
- **Guarantee and insurance limits: lapse-prone.** Art. 36.5: "En ningún caso podrá exigirse al arrendatario la contratación de seguros de impago de renta u otras coberturas análogas"; the additional guarantee may not exceed two months, and one for temporary leases [new: BOE, verbatim].
  - **If the decree lapses around 12 Nov,** avales and tenant-paid insurance come back and most of the "why now" goes. The Ley 12/2023 fee ban stays.
  - **A tenant-paid surety may be caught:** a tenant-paid afianzamiento looks like an "análoga" cover (my reading).
- **Demand.** Listings drew 135 contacts in 10 days, 462 in Barcelona [notes: CON-13]. About 60% of Barcelona coliving tenants are foreign [notes: HOU-07]. There were 44,966 DNV permit holders in Sept 2025 [notes: EXP-08].

**(b) Competitors**
| Product | URL | Price | Model / gap |
|---|---|---|---|
| SKOR | https://www.skortorent.com | Free tenant profile; landlord and agency price not published | AI solvency score from "income, expenses, and payment stability"; "No payslip or guarantor required"; raised >€200k (Apr 2024, search-level) [new: search 11; page seen 23 Oct 2026] |
| Garantilo (agent of SEAG, Sociedad Española de Alquiler Garantizado, no. 14859) | https://www.garantilo.es/perfil-extranjeros.html | "desde el 3% de la renta anual", plus options (+0.25% to +2%); who pays is not stated | Afianzamiento (not insurance); accepts passport-only tenants (deposit of 3 months), foreign income and savings; "sin límite de meses, hasta recuperar el inmueble". **The underwriter for foreign tenants already exists** [new: seen 23 Oct 2026] |
| Homming tenant scoring | https://homming.com/planes-de-precios | Included from €47/month | Scoring "based on personal and employment data" [new] |
| Didit | https://didit.me/es/solutions/tenant-screening/ | 500 free checks a month; $0.33 per applicant (ID, liveness, face match, AML) plus $0.20 proof of address; payslip and bank-statement OCR (price not listed) | Commodity layer [new: seen 23 Oct 2026] |
| Insurers (Mutua de Propietarios, Arag, Allianz, Mapfre…) | OCU comparison | €306–658 a year on €950 rent; Mutua seasonal €129.78–183.85 | Screening by an income ratio of 35–40% is built into a landlord-paid policy [new: OCU, 28 Sep 2026] |
| Spotahome Plus | https://plans.spotahome.com | 10% of contract value (UK/IE) | "verified solvent tenants", rent guarantee [new] |
| HousingAnywhere | https://housinganywhere.com/pricing/landlords | Tenant "Tenant Protection fee of approximately 25%-40% of the first month's rent" (minimum €175); landlord commission undisclosed | "We currently do not offer" a rent guarantee or damage insurance [new: seen 23 Oct 2026]. Whether its tenant fee survives art. 20.2 for Spanish properties is untested (my interpretation) |

Gap left: a standardised scorecard plus an audit log plus cross-border income checks, sold to agencies. Narrow, and adjacent to SKOR's and SEAG's roadmaps.

**(c) Buyers and market size**
- **Agencies:** no official count was retrieved (the INE DIRCE table returned no data). Proxies: agencies take part in about 70% of transactions (FADEI), and Inmovilla alone has more than 3,000 agency clients [notes: CON-11, CON-16].
- **Mid-term managers and coliving operators:** see IDEA-29.
- **Estimate:** paying entities probably number 20k–100k (an inference), but buyers who screen many foreign applicants are concentrated in Barcelona, Madrid, Málaga and Valencia.

**(d) Willingness to pay**
- **Adjacent spend:** landlord-paid insurance (€306–658 a year), guarantor fees from 3% of annual rent, and agency fees of 50–100% of a month's rent [new: ANA, 2024].
- **But buyers expect screening to come free with the policy or the platform.** €9–15 per applicant is untested [I].

**(e) Distribution**
- **Channels:** agent associations (API, COAPI, AICAT, AMADEI, FADEI), franchise networks, insurers and guarantors as partners, relocation agencies.
- **Competitors already hold these channels:** SEAG has an agent network (Garantilo is agent no. 14859), and insurers sell through agencies.

**(f) Build feasibility and legal constraints**
- **Time to build:** 2–3 months, using a KYC API, document OCR, a licensed open-banking provider (PSD2 AIS needs a licence or a licensed partner; SKOR uses this route, per search 11), a manual review queue and a PDF audit report.
- **GDPR:**
  - Legal basis: pre-contractual measures. Duty to inform every applicant: the AEPD fined an agency €2,000 for not informing an applicant who was not given the flat (art. 13 GDPR) [new: Confilegal, 22 Jun 2023, via search 13].
  - No passing data to third parties without a basis: €4,000 AEPD fine (art. 6.1) [new: conecta.unive.es, via search 13].
  - Delete data when no contract follows. Search 13 found no specific AEPD guide on tenant screening.
  - Calling employers to confirm salary without consent risks complaints.
- **Anti-discrimination:** nationality cannot be a factor; criteria must be logged.
- **AI Act (my background knowledge, not verified this session):** an ML creditworthiness score for natural persons may fall under Regulation (EU) 2024/1689 Annex III high-risk uses. That would mean conformity, data-governance and human-oversight duties, and the application date may have been changed by the EU "omnibus". Keep scoring rule-based and human-reviewed, or verify this before building.

**(g) Defensibility**
- **KYC, OCR and scorecards:** none.
- **What would be defensible:** an exclusive underwriter deal or cross-border income data partnerships. SEAG and the insurers already own the underwriting side.

**(h) Kill criteria**
1. *Agencies will not pay at least €9 per screening.* **OPEN** [I]. Free bundling by insurers and PM software makes a pass less likely.
2. *No insurer will back a landlord-paid guarantee for foreign tenants.* **NOT MET**, and the result cuts against the idea: SEAG/Garantilo already back passport-only foreign tenants, and insurers sell landlord-paid cover, so the guarantee is a partner opportunity, not a gap.
3. *Lapse.* If RDL 29/2026 is not convalidated, avales return and urgency drops (**OPEN**, vote ~12 Nov).

**Scores (standalone, as proposed)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Recurring pain (lead overload; the fee ban enforced with a final €3.6M fine), no deadline; the guarantee caps are lapse-prone |
| S2 Buyers | 3 | Agencies plus managers plus coliving operators, plausibly 20k–100k (no official count) |
| S3 Willingness to pay | 3 | Adjacent spend exists (insurance, a 3% guarantor fee), but screening is usually bundled free |
| S4 Reachability | 3 | Associations and franchises exist; unproven; competitors hold the guarantor channels |
| S5 Competitive gap | 2 | SKOR, SEAG/Garantilo, Homming, insurers, Spotahome and Didit cover most layers |
| S6 Build speed | 3 | 2–3 months, integration-heavy (KYC, OCR, licensed open banking), plus GDPR and possibly AI Act design |
| S7 Defensibility | 2 | Commodity without an underwriter or data deals |
| S8 Retention | 3 | Per-vacancy, periodic use |
| **Sellability** | **2.75** | 22/8 |
| **P** | **3** | A defaulting tenant owes €8,489 on average [notes: CON-20], but insurers cover it and screening only mitigates; moderate overall |
| **Overall** | **2.85** | 0.6 × 2.75 + 0.4 × 3 |

**Open [I] checks**
- Interview 10 agencies in Barcelona, Madrid and Málaga: would they pay €9 or more per screened applicant?
- Ask SEAG/Garantilo and SKOR for referral or white-label terms.
- Find out whether HousingAnywhere and Spotahome have changed their Spanish tenant fees after art. 20.2.

**What would change the verdict**
- A guarantor or insurer offering an exclusive landlord-paid product with revenue share for a software distributor.
- Agencies showing they pay per screening today.
- RDL 29/2026 convalidated and enforced against tenant-side platform fees.


#### IDEA-32: Short-term-rental listing compliance and eligibility monitor (PMS add-on, open-data regions first) — RESHAPE (medium)

**Validated definition (after reshape).** A register-matching monitor sold as an add-on through PMS and channel-manager marketplaces. It reads each unit's registration code and address from the manager's PMS, not by scraping platforms, which Airbnb's terms forbid. It checks them daily against the official regional open-data registers where these exist: Andalucía (OpenRTA, daily API), Comunitat Valenciana (daily API), Comunidad de Madrid (weekly) and Canarias (CSV/JSON). It flags inactive or mismatched codes and zone eligibility (Málaga's three-band zoning, Madrid's Plan Reside floor and centre rules), and keeps an inspection evidence pack. Catalonia and Baleares are added only once a data route is confirmed. A secondary buyer is the agent or investor running a pre-purchase eligibility check. Price: €2–3 per listing per month (minimum €49) for managers; a per-check fee for pre-purchase checks.

**(a) Problem reality and regulation status**
- **Platform enforcement is real and final at the interim stage.** Consumo's **€64,055,311** fine on Airbnb (signed Dec 2025) covers 65,122 listings: "sin licencia" ads and untruthful information on hosts' status (€63,980,311, six times the illicit profit), plus minor and serious items. The TSJ de Madrid "ha denegado la solicitud de medidas cautelares" [new: https://www.dsca.gob.es/es/comunicacion/notas-prensa/justicia-obliga-airbnb-pagar-64-millones-euros-previstos-multa-que-le, 22–23 Mar 2026]. The release mentions no proceedings against managers or Booking. Consumo's 2025 files against large managers remain without a published outcome [notes: HOS-24].
- **National registry gone; EU duties stay.** The national registry was annulled (May–June 2026). EU 2024/1028 has applied since 20 May 2026: platforms must ask for and display numbers, run random checks and send data [notes: HOS-13, HOU-11].
- **Spanish penalty regime for platforms is pending.** RDL 29/2026's new LAU Title V fines platforms €1M (very serious: not collecting and transmitting data), €500,000 (serious: incomplete or inaccurate data) and €100,000 (minor) [new: BOE RDL 29/2026, arts. 40–43, verbatim]. It **lapses if the ~12 Nov vote fails**.
- **Regional and municipal rules (verified this pass):**
  - **Málaga:** the BOP published the initial PGOU approval on 13 Jan 2025. "desde mañana, martes 14 de enero, habrá 43 barrios de la ciudad en los que no podrán darse de alta nuevas viviendas turísticas". A further 32 barrios may add units up to the 8% cap, and 328 only with independent entrance and services. The basis is Decreto 31/2024 [new: malaga.eu communiqué, 13 Jan 2025, https://www.malaga.eu/visorcontenido/ANUDocumentDisplayer/176212/COMUNICADO.pdf]. The July 2026 three-year licence suspension remains single-source [notes: HOS-20].
  - **Canarias Ley 6/2025:** in force since the day after BOC publication (BOC 12 Dec 2025). Art. 8.6 requires a registration number "en cualquier publicación o anuncio", including on platforms. A new art. 75.16 of Ley 7/1995 makes advertising "careciendo o sin indicar el preceptivo número de registro" an infraction; the fine band was not in the parts read. Under DT 2ª, existing vacation homes "dispondrán de un plazo de cinco años para continuar con la explotación" [new: https://www.gobiernodecanarias.org/boc/2025/246/4229.html].
  - **Not verified in this pass:** Palma's ban and the number and date of the Balearic "Ley 4/2026" (still single-source) [notes: HOS-22].
- **Supply is shrinking:** 341,001 listed tourist homes in May 2026, −10.7% year on year [notes: HOS-24]. Barcelona's HUT licences end in Nov 2028 [notes: HOS-18].

**(b) Competitors**
| Product | Price | Coverage of code validation |
|---|---|---|
| Chekin | €3.95 / €5.95 / €7.95 per property per month; "Save up to 20%" annually; minimum stated as both 3 and "20 accommodation units" on the same page (C-16 not settled) [new: https://chekin.com/en/pricing/, seen 23 Oct 2026] | "Legal Compliance" in all plans, but its code-checking guide (23 Feb 2026) is a **manual** three-step checklist: check the ad, confirm in the regional register, keep evidence. "cada comunidad gestiona su registro y sus consultas" [new: https://chekin.com/blog/como-comprobar-codigo-registro-turistico-espana/] |
| Avantio, Hostaway (with Chekin), Smoobu, net2rent | PMS pricing (Smoobu €29–55 for the first unit plus €9.60 per extra unit [notes: HOS-16]) | Store and push the code; Avantio's Chekin plan automates police and INE reports; no validation against registers found [new: search 15 → avantio.com/es/check-in-online, hostaway.com/marketplace/chekin] |
| Airbnb and Booking (platform side) | n/a | Must collect, display and randomly check numbers under EU 2024/1028; Airbnb has delisted in Mallorca and Canarias under regional deals [notes: HOS-22]. **This is the main redundancy risk** |
| AirDNA, Inside Airbnb | Data products | Market data, not compliance [notes: HOS-24] |

No automated, manager-side register-matching product was found in searches 15 and 16. That is absence of evidence, not proof.

**(c) Buyers and market size**
- **Units:** 341,001 listed tourist homes (INE, May 2026): Andalucía 90,649; Cataluña 51,300; C. Valenciana 51,268; Canarias 48,356; Baleares 21,304 [notes: HOS-24 and section KQ3].
- **Managers:** no count of professional managers was found [I].
- **Revenue ceiling (my calculation):** if 30–40% of units are professionally managed (an assumption), that is about 100k–135k units. At €2.5 per listing per month the ceiling is about €3–4M ARR. A realistic 5–10% share gives €0.15–0.4M, in a supply that is falling 10% a year.

**(d) Willingness to pay**
- **Adjacent spend:** managers already pay €3.95–7.95 per property for compliance (Chekin) plus a PMS.
- **The cost of failure is high:** delisting means zero platform revenue. Madrid fines escalate to €30,001, €60,001 and €100,001, and up to €190,000 per home [notes: HOS-19]; Canarias and Balearic fines are large.
- **But no spend on code validation as such was found.** Managers may rely on the platform to reject bad numbers.

**(e) Distribution**
- **PMS marketplaces:** Hostaway lists Chekin in its marketplace, a proven integration route for compliance add-ons [new: search 15].
- **Associations:** Apartur, Fevitur, Aptur CV and StayAlliance (unproven).
- **Pre-purchase:** agents and investors.

**(f) Build feasibility and legal constraints**
- **Open data exists:**
  - **Andalucía OpenRTA:** JSON, CSV and OpenAPI (`https://datos.juntadeandalucia.es/api/v0/openrta/openapi.json`); update "Diario"; licence CC BY 4.0 [new: https://www.juntadeandalucia.es/datosabiertos/portal/dataset/openrta].
  - **Comunitat Valenciana:** current and historical tourist-home lists in CSV, JSON and XML with API access, including signatura, address, places and cadastral reference; daily per datos.gob.es [new: search 14 → https://dadesobertes.gva.es/es/dataset/tur-gestur-vt].
  - **Comunidad de Madrid:** "Alojamientos turísticos" in CSV and JSON, "SEMANAL", last updated 19 Oct 2026, CC BY [new: https://datos.comunidad.madrid/dataset/alojamientos_turisticos]. Whether it carries VT codes per unit was not confirmed.
  - **Canarias:** the Registro General Turístico publishes vivienda vacacional in CSV, XLSX and JSON [new: search 14 → datos.canarias.es].
  - **Catalonia (HUT) and Baleares (ETV):** **not found**; the Barcelona open-data page returned 403.
- **Scraping is barred:** Airbnb Terms §11.1: "Do not use bots, crawlers, scrapers, or other automated means to access or collect data" (last updated 5 Feb 2026) [new: https://www.airbnb.com/help/article/2908]. The product must therefore read codes from the manager's PMS or from user-submitted URLs. Booking's connectivity documentation on licences returned 404 (not verified).
- **GDPR:** owners' data in registers is personal data; reuse under CC BY covers the licence, not the GDPR assessment.
- **Time to MVP:** 2–3 months for 4 regions plus 2 PMS integrations.

**(g) Defensibility**
- **Moderate:** normalising 4–6 regional datasets plus municipal zoning layers (Málaga bands, Madrid Plan Reside) is tedious to keep current, and PMS marketplace placement helps.
- **Exposed:** Chekin and the PMSs have the codes and the customers. The platforms' own verification under EU 2024/1028 could absorb the core check.

**(h) Kill criteria**
1. *The registers cannot be queried at scale.* **NOT MET** for Andalucía, Valencia, Madrid and Canarias (open data, some with APIs, daily or weekly). **OPEN** for Catalonia and Baleares.
2. *Platform terms forbid scraping.* **MET** (Airbnb §11.1). It is a design constraint, not a kill: use PMS data.
3. *Managers will not pay at least €2 per listing.* **OPEN** [I].
4. *Platforms make the tool redundant under EU 2024/1028.* **OPEN.** Platforms must check numbers, but cross-checking register status and zone eligibility for a manager's whole portfolio is not their job.

**Scores (reshaped version)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced rules with frequent costly events (delisting, fines from €30k to €190k); EU 2024/1028 in force; the national platform fines are pending |
| S2 Buyers | 3 | Managers plus multi-unit owners plausibly number 20k–100k (no count) |
| S3 Willingness to pay | 3 | Managers already pay €3.95–7.95 per unit for compliance; no spend on validation itself found |
| S4 Reachability | 3 | PMS marketplaces (Hostaway lists Chekin) and associations exist; unproven for this product |
| S5 Competitive gap | 4 | No automated manager-side validator found; Chekin offers a manual guide |
| S6 Build speed | 3 | 2–3 months; several datasets plus PMS integrations |
| S7 Defensibility | 3 | Multi-region data pipelines and zoning layers; exposed to Chekin, PMSs and platforms |
| S8 Retention | 3 | Continuous monitoring while listings exist; shrinking base |
| **Sellability** | **3.25** | 26/8 |
| **P** | **4** | Delisting removes all platform revenue; fines are large; concentrated but widespread in tourist regions |
| **Overall** | **3.55** | 0.6 × 3.25 + 0.4 × 4 |

**Open [I] checks**
- Ask Fevitur, Apartur and Aptur CV how many professional managers there are and their unit counts.
- Run 10 manager interviews on €2 or more per listing.
- Ask Hostaway, Smoobu and Avantio about marketplace terms.
- Check whether Catalonia's RTC and the Balearic register publish data.
- Find out how Airbnb and Booking verify numbers in Spain now (rejection at listing, or random checks).

**What would change the verdict**
- **Towards GO:** managers report delistings caused by stale register status, and a PMS marketplace accepts the add-on.
- **Towards KILL:** platforms reject invalid numbers at entry with live register checks, or Chekin ships automated validation.


#### IDEA-33: Tourist-tax engine reshaped: Basque municipal tourist-tax rates and quarterly-return API for PMS and check-in vendors and gestorías — RESHAPE (medium)

**Validated definition (after reshape).** A rules and rates service for the new Basque impuesto sobre estancias turísticas, from 1 Jan 2027. The tax is municipal: each ayuntamiento sets its rate by ordinance within the foral band, and manages, inspects and collects it. The service provides four things:
1. A database of every Gipuzkoa, Bizkaia and Álava municipality's ordinance: rate by category, bonus or surcharge, filing form and deadline.
2. A per-booking calculation API with the 6-unit cap, exemption logic and capture of the required declarations or documents.
3. A ledger per establishment, keyed to its REATE code.
4. The quarterly autoliquidación data, per municipality, aggregated across establishments where the law allows.

Sold to PMS, channel-manager and online check-in vendors (per booking or per unit) and to Basque gestorías (per seat). **Dropped:** the traveller-reporting module (Ertzaintza and Mossos), which at least six vendors already claim, and Catalonia as a launch market, where the tax has existed since 2012 and incumbents handle it.

**(a) Problem reality and regulation status (verified in the primary text)**
- **Gipuzkoa, Norma Foral 3/2026, de 12 de junio** (BOPV no. 119, 25 Jun 2026) [new: https://www.euskadi.eus/bopv2/datos/2026/06/2602836a.pdf, read in full 23 Oct 2026]:
  - **Rates (art. 9), min–max € per "unidad de estancia":**
    - hotels: 5★ 4.50–6.50; 4★ 3.50–5.50; 3★ 1.50–3.50; 2★ 1.00–2.50; 1★ 0.75–1.75;
    - pensiones, campings, casas rurales and albergues: 0.75–1.75;
    - apartamentos turísticos and other lodgings: 1.50–3.50; agroturismos: 0.50–1.25;
    - VUT, whole or by rooms: 4.50–6.50; cruises: 6.00–7.00.
  - **Cap:** "se computará un máximo de 6 unidades de estancia por contribuyente y por cada estancia continuada" (art. 9.3). The notes' "6 nights" is right; Chekin's "cinco noches" is wrong.
  - **Bonus and surcharge (art. 11):** a bonus of up to 100% (25 or fewer places, or intensity under 1% with 75 or fewer places); a surcharge of up to 50% (750 or more places, or at least 5,000 inhabitants with intensity of 10% or more); the two are incompatible.
  - **Substitute taxpayer and joint liability (arts. 6–7):** the operator is the "sustituto". **Intermediaries that contract or "intervengan en la formalización de la reserva o en el cobro" are jointly liable.** That exposes managers and platforms, and is a reason they will want accurate calculation.
  - **Collection and filing:** the substitute collects before the stay ends (art. 12.3). Filing is a quarterly self-assessment, and multi-establishment operators may pay in one aggregated return (art. 13). The form and deadline are set "mediante la correspondiente ordenanza fiscal". Without an ordinance, the maximum rates apply, and returns are due within the first 25 calendar days after the quarter (DA 1ª).
  - **Identification and records:** establishments are identified by their REATE code (art. 14). The operator keeps stay data and exemption evidence for the limitation period (art. 15).
  - **Exemptions (art. 5)** are each tied to documents or declarations: social programmes; under-18s; disability of 65% or more or dependency of grade II–III, plus one companion; studies, research and talent programmes; health (Osakidetza), plus one companion; force majeure.
  - **Administration:** each **ayuntamiento** manages, inspects and collects (art. 16).
  - **Dates:** effects from **1 Jan 2027**; bookings made before 5 Feb 2026 are exempt (DA 2ª, DF 3ª).
- **Bizkaia, Norma Foral 3/2026, de 17 de junio** (BOB 26 Jun 2026). Same structure: 6-unit cap, municipal ordinances within a band, maximum rates if no ordinance; effects 1 Jan 2027 [new: search 17 → derecholocal.es, fiscal-impuestos.com]. **Álava:** approved by its Juntas Generales on 10 Jun 2026; the norm number was not verified [new: search 17 → eldiario.es, Jun 2026].
- **Municipal ordinances are being written now.** Vitoria-Gasteiz agreed €6.50 per stay-unit (maximum 6) for 5★ hotels and VUT on 22 Sep 2026, with initial approval to follow and **final approval expected in November 2026** [new: https://blogs.vitoria-gasteiz.org/medios/2026/09/22/el-gabinete-etxebarria-cierra-un-acuerdo-con-elkarrekin-para-la-aprobacion-del-impuesto-sobre-estancias-turisticas/]. Bilbao and Donostia were finalising their ordinances [new: search 18 → moncloa.com, 22 Jun 2026; eldiario.es]. Rates and filing therefore differ by town and will keep changing in the first half of 2027. This is the regional-law equivalent of a rules feed, unaffected by the national election.
- **Catalonia (C-16): not settled.**
  - Forbes (25 Feb 2026): Barcelona maximum €4.50 until 31 Mar 2027 and €6 from 1 Apr 2027; "luxury" €7; municipal surcharge up to €8 (from €4); other councils up to €4 [new: https://forbes.es/economia/879865/el-parlament-aprueba-la-ley-que-incrementara-la-tasa-turistica-a-partir-del-1-de-abril/].
  - DonPorqué's combined figures (5★ €11, flat €8.50) probably add regional and municipal parts [notes: HOS-15].
  - The DOGC tables were not retrieved, so the conflict stays open.
- **SES and police reporting.** RD 933/2021 is unchanged; the Basque Country and Catalonia use the Ertzaintza and Mossos systems [notes: HOS-12]. The stage of infringement INFR(2026)4005 was not checked (budget).

**(b) Competitors**
| Product | Price | Basque tax coverage |
|---|---|---|
| Chekin | €3.95 / €5.95 / €7.95 per property per month; minimum stated as both 3 and 20 units (C-16 still unsettled) [new: https://chekin.com/en/pricing/] | "integra el cobro de la tasa turística" in check-in, with "la cantidad calculada según el alojamiento". Filing "sigue correspondiendo al titular". Its guide (10 Jun 2026) states "cinco noches" and €0.75–5, both superseded by the final norm [new: https://chekin.com/blog/tasa-turistica-pais-vasco/] |
| Check-in Scan | Not published; 14-day trial | "Calcula y cobra de forma automática las tasas turísticas"; a record "listo para la autoliquidación foral" is presented as a goal [new: https://www.checkinscan.com/tasa-turistica-pais-vasco/, updated 19 Jun 2026] |
| PMSs (net2rent, Avantio, Smoobu, Mews, Cloudbeds, Hostaway) | Various | Search 18 found **no evidence** either way on Basque tax or returns |
| Traveller reporting to the Ertzaintza and Mossos | — | Chekin, Lodgify, BookCheckin, Hotelgest, GoToCheck and net2rent all claim connections [new: search 19]. **Saturated, so dropped** |
| Gestorías | Per-return fees (not priced) | Will file the returns; buyers or partners |

**(c) Buyers and market size**
- **No Basque count of establishments or listings was retrieved.** The idealista/INE May 2026 article gives no País Vasco figure, and the Open Data Euskadi URL guessed returned 404 [I/F: Eustat, REATE].
- **Inference:** the region is far smaller than Catalonia (51,300 tourist homes) or Andalucía (90,649). Paying vendors and gestorías number tens to low hundreds.
- **Revenue ceiling:** an API at €0.10–0.20 per booking, or €3–6 per unit, gives a ceiling in the low hundreds of thousands of euros a year (my estimate). **A niche.**

**(d) Willingness to pay**
- **Adjacent spend:** Chekin's €3.95–7.95 per unit already includes tourist taxes, and gestorías charge per return.
- **The new spend is for municipal granularity and filing,** which nobody sells today. Willingness to pay for it is unproven [I].
- **Joint liability for intermediaries (art. 7)** gives managers a reason to pay for accuracy.

**(e) Distribution**
- **Channels:** PMS and check-in vendors as API customers (one contract reaches many units), Basque gestorías, and hotel and tourist-flat associations in the three territories (names not validated).
- **Timing:** the first quarterly returns fall in April 2027, which sets the sales window: November 2026 to March 2027.

**(f) Build feasibility and legal constraints**
- **MVP: 6–8 weeks.** It needs a rates database from about 250 municipal ordinances in three territories (the number of municipalities is my background figure, not verified), a calculation API, an exemption-evidence capture flow and a return export.
- **Constraint:** each ayuntamiento's e-filing channel and form is set by its ordinance and is unknown. Direct submission may need apoderamiento per client; the MVP exports, and the substitute or the gestoría files.
- **GDPR:** exemption evidence (disability, health certificates) is special-category data. Collect a declaration rather than the document where the norm allows (art. 5 accepts declaraciones responsables).

**(g) Defensibility**
- **Low to moderate.** The rates are public law, and Chekin or Check-in Scan can add per-municipality tables within a quarter.
- **The edges:** being first, keeping roughly 250 ordinances current, and API contracts with PMSs.

**(h) Kill criteria**
1. *Chekin and the major PMSs already compute the Basque rates and produce the quarterly return.* **PARTLY MET.** Chekin and Check-in Scan claim calculation and collection, but no one was found producing the per-municipality return (as of Jun–Oct 2026). Re-test in December 2026.
2. *The Basque treasuries or associations give out free calculators.* **OPEN.** None found, but the ayuntamientos manage the tax and may publish forms or calculators.
3. *The regional market is too small.* **Effectively MET for a standalone product.** That is why the product is reshaped as an API and data feed for vendors, not an end-user SaaS.

**Scores (reshaped version)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | A legal duty from 1 Jan 2027 (within 12 months); first quarterly returns about April 2027; intermediaries jointly liable |
| S2 Buyers | 2 | Basque lodgings, managers, vendors and gestorías: a small region, probably 5k–20k paying entities at most (unverified) |
| S3 Willingness to pay | 3 | Spend exists on check-in and compliance tools and gestorías; none yet on municipal returns |
| S4 Reachability | 3 | PMS API and gestoría channels exist; unproven |
| S5 Competitive gap | 3 | Calculation and collection are claimed by two tools; municipal rate granularity and return generation are weak or missing |
| S6 Build speed | 4 | 1–2 months; filing formats unknown |
| S7 Defensibility | 2 | Public-law tables; incumbents can match in a quarter |
| S8 Retention | 4 | A quarterly legal obligation plus record-keeping (art. 15) |
| **Sellability** | **3.25** | 26/8 |
| **P** | **3** | The substitute taxpayer bears uncollected tax and sanctions; amounts per business are moderate |
| **Overall** | **3.15** | 0.6 × 3.25 + 0.4 × 3 |

**Open [I] checks**
- Ask 3 PMS or check-in vendors (Chekin, net2rent, Avantio) whether they would buy a municipal rates and return feed.
- Ask 5 Gipuzkoa and Bizkaia gestorías about filing volumes and price.
- Ask 2–3 ayuntamientos (Donostia, Bilbao, Vitoria) for their filing method and form.
- Get the Eustat or REATE counts of establishments and VUT.
- Read the Catalan DOGC rate tables.
- Find the stage of INFR(2026)4005.

**What would change the verdict**
- **Towards GO:** a PMS signs a letter of intent for the feed; the ayuntamientos publish divergent ordinances and filing channels, which raises the pain.
- **Towards KILL:** Chekin ships per-municipality returns before January; the Basque treasuries centralise filing with a free calculator.


#### IDEA-34: Building-compliance calendar and owners'-vote module for administradores de fincas — KILL (medium)

**Verdict detail:** KILL as a standalone product. At most, a maintained building-obligations data feed licensed to ERPs (Gesfincas, Fynkus) or consolidators (inmho).

**Validated definition.** A per-building obligations calendar (lifts, inspections, certifications, data protection, grants), supplier CAE intake, owner notices with proof of receipt, a 3/5 majority calculator with minutes and certificates, and export to the administradores' ERPs. **Reason for the kill:**
- **Votes, minutes and notices already exist in the incumbent ERP.** Gesfincas's iJuntas covers "convocatorias, actas, votaciones, delegaciones y control de asistencia", plus "email certificado" for "validez legal en tus comunicaciones" and "control de agenda, tareas, plazos".
- **Whole ERPs are priced below the proposed module.** Fynkus PRO costs €0.10 per unit per month with a €2.50 minimum per community, so a €1–2 per community calendar would cost 40–80% of an entire ERP.
- **What remains is a data layer for ERPs, not a product.** The one missing piece is a database of building obligations, auto-filled and checked by region.

**(a) Problem reality and regulation status**
- **3/5 rule (LPH):** verified in the BOE.
  - Art. 17.12 requires "el voto favorable de las tres quintas partes del total de los propietarios" plus three-fifths of quotas to approve, limit, condition or prohibit tourist use. Special fees may rise by "no ... superior al 20 %"; there is no retroactive effect. Art. 7.3 requires "la aprobación expresa de la comunidad".
  - Notices go "por cualquier medio que permita tener constancia de su recepción" (art. 9.1.h). Minutes are sent under the same art. 9 procedure, signed within ten days, in a book stamped by the Registrar (art. 19). The law has no express electronic-meeting rule; the PP bill likely lapsed [notes: CON-25].
  - Source: [new: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906, consolidated 03/10/2026].
- **Lifts:** RD 355/2024 (ITC AEM 1) has been in force since 1 Jul 2024.
  - Maintenance is monthly, or every four months for small buildings. Periodic official inspection falls every 2, 4 or 6 years by building type; sources differ, so check the BOE.
  - If the inspection is overdue, the maintenance company must put the lift out of service and notify the owner and the authority. Reforms of up to €40,000 are required when inspections find non-compliance.
  - Source: [new: search 21 → https://www.boe.es/buscar/act.php?id=BOE-A-2024-7258; idealista, 21 Apr 2026, https://www.idealista.com/news/finanzas/laboral/2026/04/21/893970-la-normativa-de-ascensores-que-empieza-a-aplicarse-reformas-obligadas-de-hasta-40-000].
  - **Mitigating factor:** lift maintenance firms and inspection bodies already track these deadlines for their clients.
- **Other recurring duties are unverified in this pass:** municipal ITE/IEE, fire protection (RIPCI), low-voltage and garage ventilation, legionella and pools. The scope by region stays an open check.
- **The burden itself is described only qualitatively**, by a compliance vendor (Conversia) [notes: CON-24].

**(b) Competitors**
| Product | Price | Relevant features |
|---|---|---|
| Gesfincas (via distributor CIAX, since 1991) | "Desde 295 €" (period not stated); modular, on quote | iJuntas (convocatorias, actas, votaciones, delegaciones, asistencia); certified email; e-signature; incidents assigned to suppliers; "control de agenda, tareas, plazos"; arrears; payroll. No CAE or inspection database stated [new: https://www.ciax.es/gesfincas/, seen 23 Oct 2026] |
| Fynkus | PRO: "0,10 €/ + IVA mes por unidad", minimum €2.50 per community and €10 per office per month; or €1 per unit per year (minimum €25 per community); 50% off from unit 51; free version [new: https://www.fynkus.es/presupuesto-administrador-fincas/] | Juntas Generales module, suppliers and supplier contracts, incidents, bank feed, AI invoice OCR, free owner app |
| Cegid Finca3, Comunicasa, Adminet (pay-per-use), Fincasoft (free under 50 components) | Mostly unpublished | Listed in a June 2026 comparison written by a Gesfincas distributor [new: https://www.ciax.es/administracion-de-fincas/mejor-software-administracion-fincas-2026/, 24 Jun 2026] |
| TucomunidApp (IESA) | Through the administrador | Owner voting and proxies [new: search 20 → tusvecinos.es] |
| CAE platforms (Dokify, Nalanda, PlayCAE…) | €102.90 a year and up | Supplier documentation [notes: CON-02] |
| Fincas Pro, Comunidad Feliz | Not verified | — |

**(c) Buyers and market size**
- **Buyers:** about 16,000 administradores and about 1M communities. inmho manages 15,000 communities (under 3% of the market) and bought 50 firms in a year [notes: CON-24].
- **Ceiling (my calculation):** 1M communities × €1 per month × 12 = €12M a year at full capture. A realistic 2–5% share gives €0.24–0.6M.

**(d) Willingness to pay**
- **Weak.** A whole cloud ERP costs about €2.50 per community per month (Fynkus), and Gesfincas bundles juntas and certified notices.
- Administradores' fees per community were not retrieved [I].

**(e) Distribution**
- **Channels:** CGCAFE and the colegios territoriales; ERP vendors (as licensees, not as channels for a competing app); consolidators (inmho, standardising acquired offices).
- **No evidence** that any of them buys third-party compliance tooling.

**(f) Build feasibility**
- **Effort:** 2–4 months for one region's obligations database plus import from ERPs. Gesfincas has no public API in what was seen.
- **Data:** owners' data falls under GDPR.

**(g) Defensibility**
- **Thin.** A calendar is easy to copy, and the ERPs own the workflow.
- **The only defensible asset:** a maintained obligations database by region and building type, licensed to ERPs or consolidators.

**(h) Kill criteria**
1. *Gesfincas or Fincas Pro already ship a compliance calendar.* **PARTLY MET.** Gesfincas ships agenda, tasks, deadlines, juntas, votes, minutes and certified notices. A per-building legal-obligations calendar was not seen. Fincas Pro was not verified.
2. *Administradores will not pay €1 per community.* **OPEN** [I], but likely to fail against Fynkus's €2.50 minimum for a whole ERP.

**Scores (standalone, as proposed)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Recurring inspections (for example lifts, with an out-of-service sanction) and 3/5 votes on request; no new deadline |
| S2 Buyers | 2 | About 16,000 administradores |
| S3 Willingness to pay | 2 | A whole ERP costs about €2.50 per community per month; incumbents bundle juntas and notices |
| S4 Reachability | 3 | Concentrated colegios and consolidators, but no proven partner programme |
| S5 Competitive gap | 2 | Several decent ERPs; only the obligations database is missing |
| S6 Build speed | 3 | 2–4 months; regional obligations research plus integrations |
| S7 Defensibility | 2 | Calendar trivially copyable; the database moat is unproven |
| S8 Retention | 3 | Periodic use; the ERP remains the system of record |
| **Sellability** | **2.50** | 20/8 |
| **P** | **3** | Missed inspections can stop a lift, and gaps in supplier CAE expose communities; burden described qualitatively only |
| **Overall** | **2.70** | 0.6 × 2.5 + 0.4 × 3 |

**Open [I] checks**
- Ask inmho whether it builds or buys its tooling.
- Ask CGCAFE about software adoption.
- Ask Gesfincas and Fynkus whether they would license an obligations data feed.
- Verify the regional inspection schedules (ITE/IEE, RIPCI, REBT, legionella).

**What would change the verdict**
- A consolidator or ERP committing to license a maintained obligations database.
- Evidence of large fines or liability from missed building obligations.


#### IDEA-35: AML starter kit for small real-estate agencies (RD 813/2026 representative deadline and AMLR readiness) — RESHAPE (medium)

**Validated definition (after reshape).** A low-touch annual subscription for agencies and small developers that broker sales, distributed through agency CRMs and associations. It covers:
1. **A guided pack for appointing a SEPBLAC representative and communicating the appointment.** This is newly mandatory for micro agencies under RD 813/2026 and must be done within nine months of 28 Oct 2026.
2. **A simplified per-deal file:** identification, beneficial owner, activity and source of funds, plus sanctions and PEP screening through a commodity API (for example Didit at about $0.20 per AML check).
3. **A 10-year record vault.**
4. **A log of "special examinations"**, including the new duty to assess whether to report a transaction to SEPBLAC.
5. **Annual training reminders and AMLR-readiness updates.**

The reshape **re-anchors the "why now" on a Spanish rule already in force (RD 813/2026) instead of the 2027 AMLR alone.** It drops full internal-control manuals and external-expert reports for micro agencies, which remain exempt from them (art. 31.1 RD 304/2014 as amended). Price: €99–149 a year (about €8–12/month), plus per-check fees.

**(a) Problem reality and regulation status**
- **Who is obliged now:** agencies brokering sales are obliged entities. Ley 10/2010 art. 2.1.l covers "Los promotores inmobiliarios y quienes ejerzan profesionalmente actividades de agencia, comisión o intermediación en la compraventa de bienes inmuebles". The SEPBLAC compilation mentions **sales only, no rentals** [new: https://www.sepblac.es/wp-content/uploads/2024/10/sujetos_obligados_ley_10_2010.pdf, read 23 Oct 2026].
- **New in October 2026 (official): RD 813/2026, de 7 de octubre** (BOE no. 250, 8 Oct 2026, BOE-A-2026-20915), in force "a los veinte días de su publicación", i.e. **28 Oct 2026**.
  - **Representative:** it rewrites art. 35.1 of RD 304/2014: "Los sujetos obligados designarán un representante ante el Servicio Ejecutivo de la Comisión". This **removes the exemption** for entities with fewer than 10 persons and turnover or balance sheet of €2M or less.
  - **Deadline:** DT 2ª gives those entities "un plazo de nueve meses, a contar desde la entrada en vigor", i.e. until about 28 Jul 2027.
  - **Internal-control exemption kept:** art. 31.1 still exempts micro entities from arts. 31, 32, 33, 38 and 39, but adds written policies on "sanciones y contramedidas financieras internacionales".
  - Source: [new: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20915, seen 23 Oct 2026].
  - **Lapse risk:** none. It is a Real Decreto, not a decree-law, so no convalidation is needed and the election does not affect it.
  - **A practitioner's reading** (opinion column, single source): failing to communicate the appointment is a serious infraction with a "multa mínima de 60.000 euros". Basic due diligence (client, beneficial owner, activity, source of funds, 10-year retention) applies to all agencies, and after a special examination the agency must consider reporting [new: InmoDiario, J. M. Baños, 23 Oct 2026, https://inmodiario.com/7826/87429/la-inmobiliaria-pequena-tambien-tendra-que-nombrar-representante-ante-el-sepblac/].
- **EU AMLR (Reg. 2024/1624):** "se aplicará desde julio de 2027" [new: finReg360, 23 Dec 2025, https://finreg360.com/el-negocio-inmobiliario-ante-las-novedades-en-la-prevencion-del-blanqueo-de-capitales/].
  - **What it brings:** due diligence on all parties, beneficial owners in complex structures, a risk self-assessment built on real data ("no ... un ejercicio teórico"), sanctions and adverse-media screening, a board member responsible for AML, and a separate compliance officer.
  - **Not verified this session:** EUR-Lex was not fetchable, so the exact date (10 July 2027, from background knowledge), any proportionality for micro entities, and whether letting intermediation above a monthly-rent threshold (€10,000 in my background knowledge) becomes covered all remain open.
  - **Lapse risk:** none; it is an EU regulation.
- **Enforcement is real but sparse.** Sponsored content using CoreBC data (21 Jun 2024) lists six final sanctions on real-estate entities [new: https://observatorioinmobiliario.es/noticias/inversion-inmobiliaria/inspecciones-sanciones-y-requerimientos-en-materia-de-prevencion-de-blanqueo-de-capitales-y-financiacion-del-terrorismo/]:
  - three of €60,001–103,790 for not producing the external-expert report;
  - **two of €60,001 for failures over the SEPBLAC representative appointment**;
  - one of €103,790 for inadequate internal control.
  - Sector-wide AML inspections rose from more than 400 (2018) to more than 800 (2022), with more than 125 sanctions since 2018 across all sectors.
  - A claim of "more than 40 sanction files in 2024" against developers and agencies (search 22 snippet) is unsourced, so it is not used.
  - **No evidence of enforcement against micro agencies specifically.**

**(b) Competitors**
| Product | Price | Coverage |
|---|---|---|
| Grupo Adaptalia (consultancy) | Not published ("evaluación gratuita") | Manual, risk assessment, training, external technical unit, external-expert report, sanctions and PEP list checks. **No mention of RD 813/2026 or the AMLR** [new: https://grupoadaptalia.es/servicio/prevencion-blanqueo-capitales-inmobiliarias] |
| CoreBC (consultancy) | Not published | Outsourced technical unit and due diligence for large developers and servicers (Aedas, Neinor, Merlin, Hipoges) [new: https://www.corebc.es/] |
| Training providers (Avanforma and others), screening tools (Checklynx), KYC (Didit: $0.20 per AML check, $0.07 per user per year monitoring) | Various | Components [new: search 22; Didit page] |
| Agency CRMs (Inmovilla, more than 3,000 agencies; Witei) | On quote | AML modules **not checked** (budget). An open [S*] check, and the main copy risk |

No cheap self-serve kit for micro agencies was found in one search. That is weak evidence of a gap.

**(c) Buyers and market size**
- **Count:** no official count of agencies retrieved (the INE DIRCE table returned no data). Proxies: Inmovilla's more than 3,000 agency clients, and agencies' 70% share of transactions [notes: CON-11, CON-16].
- **My inference:** paying entities are likely in the 20k–100k band (agencies plus developers), but this is unverified.
- **Ceiling:** 20,000 agencies × €120 a year = €2.4M at full capture; at 5–10%, €120–240k ARR.
- **The rule also hits other micro obliged entities.** RD 813/2026 applies to every micro obliged entity (see the cross-cutting section), which widens the addressable market for a generic "SEPBLAC representative and basic due-diligence kit".

**(d) Willingness to pay**
- **The spend is defensive.** Consultancies sell manuals and expert reports (unpriced), and the €60,001 minimum serious fine is a strong anchor.
- **But micro agencies stay exempt from the costly parts** (manual, expert report, internal control body), so they need little.
- **Type C at about €5/month is not viable.** The value is visible only at deal time, and AML questions generate support. **€99–149 a year** is the realistic price, and it must be validated [I].

**(e) Distribution**
- **Associations:** API, COAPI, AICAT, AMADEI, FADEI. Their newsletters will cover RD 813/2026 in the coming weeks: InmoDiario's column is dated 23 Oct.
- **Agency CRMs:** integration or white-label, via Inmovilla and Witei.
- **Franchise networks:** Tecnocasa, RE/MAX and others.
- **Search:** there will be a demand spike around "representante SEPBLAC inmobiliaria".

**(f) Build feasibility and legal constraints**
- **MVP: 4–6 weeks.** Templates, the appointment pack (SEPBLAC's communication form must be checked), deal checklists, a screening API, a vault and reminders. No certification.
- **Data:** KYC data is high-sensitivity, so EU hosting and retention rules apply.
- **Advice boundary:** do not file suspicious-activity reports automatically, and do not act as the external expert.

**(g) Defensibility**
- **Low.** The content is copyable, and CRMs can bundle a module.
- **The edges:** association partnerships, a CRM integration, and being early on the 28 Jul 2027 deadline.

**(h) Kill criteria**
- *Enforcement against small agencies is negligible and agencies will not pay before July 2027.* **PARTLY ADDRESSED.**
  - A new official duty with a deadline now exists (RD 813/2026).
  - Known sanctions include two at €60,001 specifically for representative failures (CoreBC data, 2024).
  - Enforcement against micro agencies is still unproven, and willingness to pay is **OPEN** [I].
- *CRMs bundle AML.* **OPEN** (not checked).
- *The AMLR eases duties for small entities.* **OPEN** (EUR-Lex not read).

**Scores (reshaped version)**
| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 5 | An enforced duty with a deadline inside 12 months (representative appointment by about 28 Jul 2027 under RD 813/2026), followed by the AMLR in July 2027 |
| S2 Buyers | 3 | Agencies plus small developers, plausibly 20k–100k (no official count) |
| S3 Willingness to pay | 3 | Consultancies and training are sold; a minimum fine of €60,001; micro agencies are exempt from the costliest parts |
| S4 Reachability | 3 | Associations and CRMs are concentrated channels; no partner programme proven |
| S5 Competitive gap | 3 | Consultancies and components exist; no cheap kit for micro agencies found (CRMs unchecked) |
| S6 Build speed | 4 | 1–1.5 months; no certification |
| S7 Defensibility | 2 | Copyable content; CRM bundling risk |
| S8 Retention | 4 | Recurring per-deal duty, 10-year records, annual training |
| **Sellability** | **3.38** | 27/8 = 3.375 |
| **P** | **3** | Fines are large (€60k+), but the probability for micro agencies is low on the evidence |
| **Overall** | **3.23** | 0.6 × 3.375 + 0.4 × 3 |

**Open [I] checks**
- Survey 20 agencies through an association: do they know about RD 813/2026, and would they pay €99–149 a year?
- Check whether Inmovilla and Witei plan an AML module.
- Confirm the SEPBLAC communication form and whether a gestor can file it for the agency.
- Read AMLR arts. 3, 10, 11 and the application article on EUR-Lex.

**What would change the verdict**
- **Towards GO:** an association or a CRM agrees to distribute before Q1 2027, or SEPBLAC announces inspections of micro agencies.
- **Towards KILL:** CRMs bundle AML for free, or the AMLR or Spanish implementation exempts micro agencies from the new duties.

