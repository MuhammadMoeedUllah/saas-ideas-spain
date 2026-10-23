# Stage 2, group G4: retail, e-commerce, personal services, clinics, professional services, education and care

*Noise filtering and idea generation. Status date: 23 October 2026.*

*Inputs:*
- *`retail_ecommerce_services.md` (RET-01 to RET-22).*
- *`health_professional_education_care.md` (PRO-01 to PRO-18).*
- *Prices from the software-market table in `voice_of_smes_software_market.md` ("software table").*

*How this was done:*
- *No web searches or page fetches were made.*
- *Other track files were only keyword-checked to map overlaps for section 5. None of their facts are used as evidence for G4 ideas.*
- *Price hypotheses, MVP scopes and kill thresholds are my proposals, not findings.*
- *"Inference" marks an interpretation (the researcher's or mine), not a sourced fact.*
- *"Snippet" and "search summary" mark claims that Stage 1 saw only in search results.*

---

## 1. Summary

- **40 pains reviewed** (22 RET, 18 PRO). **15 carried forward** into 12 clusters. **25 filtered**:

  | Code | Reason | Count |
  |---|---|---|
  | N1 | Weak evidence | 11 |
  | N2 | Not software-solvable | 8 |
  | N3 | Draft or pending rule | 1 |
  | N4 | Already solved cheaply | 2 |
  | N5 | Too niche | 1 |
  | N6 | Legally risky | 0 |
  | N7 | Duplicate | 2 |

- **Kept:** RET-04 (C1), RET-11 (C2), RET-15 and RET-16 (C3), RET-19 (C4), PRO-01 and PRO-02 (C5), PRO-09 (C6), PRO-05 (C7), PRO-10 and PRO-11 (C8), PRO-12 (C9), PRO-14 (C10), PRO-17 (C11), PRO-18 (C12).
- **12 candidate ideas:** 2 type A, 7 type B, 3 type C (primary type).
- **Strongest theme:** rules already in force that create recurring, document-heavy work, which today's tools cover partly or not at all:
  - proving the MASC attempt (out-of-court negotiation step) before a civil claim, since 3 Apr 2025;
  - packaging declarations, the EU packaging regulation (PPWR) since 12 Aug 2026, and the plastic tax;
  - staff files for health centres under RD 239/2026, due about 1 Jan 2027;
  - household-employer duties under RD 893/2024;
  - PRESVET antibiotic reporting for vets.
- **Second theme:** losses that grow with sales: 25–30% commissions on new salon clients, €13.3bn of online returns, €2.8bn of shop theft.
- **What software cannot fix:** the most severe, best-evidenced pains are market or policy forces: shop closures, rent shocks, Temu/Shein, 21% VAT on hairdressing, and frozen insurer fees. They were filtered, or reshaped into ideas that work around them.
- **Evidence gaps, not noise:** both tracks hit a search cap, so several sub-sectors lack evidence: salon no-shows, gym churn, academies, FUNDAE, and driving-school and clinic software prices. They are listed in section 3 as gaps to re-test.
- **Overlaps to merge later:** MASC (legal, cashflow and real-estate tracks), packaging (industry track) and VeriFactu/e-invoicing (tax track).

---

## 2. Pain clusters

### 2.1 Retail and e-commerce

#### C1. Repeat shoplifting and the evidence burden under LO 1/2026
- **Pains:** RET-04
- **Problem:**
  - Who: all physical retail, nationally. Food retail is most affected.
  - Cost: unknown loss (shrinkage) of €2,817M a year, or 1.1% of turnover, up from 0.74% (about €1,800M). Breakdown: external theft 59%, internal theft 18%, admin errors 15%, supplier fraud 9%.
  - How often: continuously. 51% of thefts are by repeat offenders (3 or more a year), 48% of them under 30.
  - Staff: 74% say aggression towards staff has risen a lot; 65% find security staff harder to hire. Source: [The Objective, 4 Nov 2025](https://theobjective.com/economia/2025-11-04/hurtos-perdida-2817-millones-comercios-espanoles/).
  - Small shops suffer about 30% more thefts ([Última Hora/AECOC, 5 Dec 2025](https://www.ultimahora.es/noticias/comunidades/2025/12/05/2525909/aecoc-celebra-reforma-multirreincidencia-causa-perdidas-comerciales-2800-millones.html)).
  - Conflict: an Ara snippet gives €2,917M for the same barometer.
- **Driver and status (Oct 2026):**
  - LO 1/2026 was published 9 Apr 2026 and has been in force since 10 Apr 2026 ([BOE consolidated text](https://www.boe.es/eli/es/lo/2026/04/08/1/con)). It applies the art. 234.1 prison penalty once the offender has three prior final convictions under the same title (at least one a delito leve). It also adds LECrim art. 105.3 (local authorities may prosecute theft) and art. 544 bis (bans on going to specified places).
  - AECOC says the €400 cumulative-value threshold is gone. A LegalToday snippet claiming it still applies contradicts the BOE; rely on the BOE.
  - Cross-track conflict: `cities_macro_surveys.md` could not verify the reform and suggested it might lapse with the dissolution. RET-04's BOE citation is stronger.
- **Used today and price:**
  - Electronic article surveillance (EAS) tags, CCTV and guards. Checkpoint Systems, a tag vendor, co-authors the barometer. No prices in the notes.
  - No incident-logging software was researched.
  - The idea that reporting every incident pays off under the new law is the researcher's inference.
- **Feeds:** G4-I01

#### C2. Online returns, serial and late returners
- **Pains:** RET-11
- **Problem:**
  - Who: online SMEs in fashion, footwear and electronics, nationally.
  - Cost: €13,300M of online returns by end-2025.
  - How often: 23.7% of non-food orders come back (clothing 31%, footwear 27%, electronics 23%).
  - Serial returners are 11% of shoppers but 23% of returns (about €2,600M), with a return rate near 48%. Late returners are 14% of shoppers and 24% of returns.
  - The average return takes 9.1 days, and 32% come back after 10 days. Source: [Law&Trends, 28 Oct 2025](https://www.lawandtrends.com/noticias/consumidores/las-devoluciones-online-en-espana-superan-los-13-300-millones-en-2025-1.html); data from ZigZag, a returns-software vendor, with Retail Economics.
  - Pressure to keep returns free:
    - 35% might stop buying from shops that charge for returns (idealo via [Forbes](https://forbes.es/ultima-hora/255575/tres-de-cada-diez-espanoles-podrian-dejar-de-comprar-en-tiendas-que-cobren-por-las-devoluciones-online/), snippet).
    - Only 21% would pay, and never more than 10% of the price (Veepee/IESE 2022 via [Modaes](https://www.modaes.com/entorno/las-devoluciones-siguen-frenando-el-online-solo-el-21-esta-dispuestos-a-pagarlas), snippet).
  - Handling cost per return: not found.
- **Driver and status (Oct 2026):** consumer expectations, plus the 14-day withdrawal right (general knowledge, not re-verified). In force. No regulatory change.
- **Used today and price:**
  - ShippyPro Professional: €207.20/month for 4,000 labels.
  - Outvio: about €375/month (a competitor's estimate). Source for both: [ShippyPro, Apr 2026](https://www.shippypro.com/es/shippypro-vs-outvio).
  - Sendcloud: free plan, and Lite at €28/month billed annually ([Hackceleration](https://hackceleration.com/es/labs/sendcloud-precio), snippet).
  - Label tools are commoditised. The open needs are at the edges: returns abuse, damage claims (RET-12) and the islands (RET-14). This is RET inference.
- **Feeds:** G4-I02

#### C3. Packaging EPR, the EU packaging regulation (PPWR) and the plastic tax
- **Pains:** RET-15, RET-16
- **Problem:**
  - Who: anyone who packs goods, or first places packaged goods, on the Spanish market. This includes online shops shipping their own products, importers and intra-EU buyers. Marketplaces and couriers carry duties in some cases.
  - Yearly cycle under RD 1055/2022 ([BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22690)):
    - register as a producer; the number goes on invoices (art. 15);
    - join a collective scheme;
    - file data by material before 31 March, in simplified form under 15 t a year (art. 16).
  - Distributors may only sell products from registered producers (arts. 28–30). Producers based outside Spain need a Spanish authorised representative (art. 17).
  - Since 12 Aug 2026 the PPWR adds a Declaration of Conformity, plus marking that links the packaging to it ([Interempresas/GENCI, 22 Jul 2026](https://www.interempresas.net/PrimeraPagina/652360-El-envase-profesional-ante-el-Reglamento-europeo.html)).
  - Plastic tax (Ley 7/2022, [BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5809); [AEAT](https://sede.agenciatributaria.gob.es/Sede/impuestos-especiales-medioambientales/impuesto-especial-sobre-envases-plastico-reutilizables.html)):
    - €0.45 per kg of non-recycled plastic;
    - imports or intra-EU purchases above 5 kg a month must register, keep a stock ledger and file modelo 592;
    - recycled content needs UNE-EN 15343 certification by an ENAC-accredited body;
    - fines: €1,000 for not registering; €75 per incorrect invoice or certificate.
  - Not captured: number of producers, scheme fees and EPR fines.
- **Driver and status (Oct 2026):**
  - RD 1055/2022 in force since 29 Dec 2022. The deadlines for schemes (31 Dec 2024) and marking (1 Jan 2025) have passed.
  - PPWR applies since 12 Aug 2026; most substantive rules come from 2030.
  - Plastic tax in force; the AEAT page was updated 20 Oct 2026.
  - The industry track (IND-12) reports a December 2025 Omnibus proposal to suspend the authorised-representative duty for direct cross-border sellers. It is a proposal only.
- **Used today and price:** collective schemes (GENCI; Cartón Circular, which has published a 2026 tariff (snippet); Ecoembes for household packaging), consultants, gestorías, ERP systems and certification bodies. No prices found.
- **Feeds:** G4-I03

#### C4. Salons' dependence on booking marketplaces
- **Pains:** RET-19, with RET-10 (filtered) used as a cost input
- **Problem:**
  - Who: hair salons, barbers, beauty and nail centres (autónomos and micro firms) and boutique studios, nationally.
  - How many: about 72,300 hairdressing and beauty establishments ([DBK 2021](https://dbk.es/en/estudios/16575/summary), snippet), against about 35,000 salons ([sector figure, Jun 2021](https://www.elindependiente.com/?p=1801776)). The definitions probably differ (RET-19, RET-20).
  - Treatwell ([pricing](https://www.treatwell.es/partners/precios/)):
    - 25% of a new marketplace client's first booking;
    - 2% + IVA on prepayments;
    - 12-month minimum contract.
  - Booksy ([Booksy](https://biz.booksy.com/es-es/blog/cuanto-cuesta-un-software-de-reservas-para-salones); [Pabau](https://pabau.com/es/blog/booksy-precio/)):
    - €34.99 + IVA a month, plus €8 per extra staff member (about €66.99 for five staff);
    - Boost takes 30% of a new client's first visit, capped at €50 + IVA;
    - payments 2% + €0.15.
  - Complaints:
    - commissions charged even when the client doesn't show ([Capterra](https://capterra.com/p/181827/Treatwell/reviews/?page=2), snippet);
    - unreachable support, weak Boost results and hard data export (Pabau, a competitor).
  - Cost illustration: 25–30% of a €40 first visit is €10–12.
  - How often: every new marketplace client.
  - No Spanish no-show data exists in the notes.
- **Driver and status (Oct 2026):**
  - Market forces.
  - Incumbents bundle payments (about 2%) and VeriFactu/TicketBAI invoicing to deepen lock-in (RET inference; Treatwell Advanced). VeriFactu is legally due in 2027; a move to October 2028 has been announced but is not in the BOE (PRO-11).
  - Since 1 Oct 2026, WhatsApp Business Platform utility messages inside the 24-hour service window are charged ([Meta](https://developers.facebook.com/docs/whatsapp/pricing/), RET-10).
- **Used today and price:**
  - Booksy and Treatwell, as above.
  - Koibox from €40/month; Flowww from €59/month ([Capterra](https://www.capterra.es/compare/145261/179541/koibox/vs/flowww), snippets).
  - Bewe: no price found.
  - Payments: SumUp at 1.49%, or Pagos Plus at €19/month (0.75%) (software table).
- **Feeds:** G4-I04

### 2.2 Health and veterinary

#### C5. Insurer fee squeeze on self-employed health professionals
- **Pains:** PRO-01, PRO-02
- **Problem:**
  - Who: self-employed specialists and micro clinics on Adeslas, Asisa, DKV, Sanitas and Mapfre panels, plus allied professionals (psychology, physiotherapy, podiatry, nutrition, speech therapy, dentistry). Nationally.
  - How often: every insured consultation, every day.
  - Doctors' fees:
    - Adeslas raised its specialist consultation fee from €18 to €19 in 2025, for private policies only; Asisa raised all acts by 6.5% ([The Objective, 6 May 2025](https://theobjective.com/economia/2025-05-06/adeslas-asisa-suben-tarifa-medicos/)).
    - Asisa's 2022 scales: €17.06 for ophthalmology and €20.71 for rheumatology ([The Objective, 15 Feb 2025](https://theobjective.com/economia/2025-02-15/medicos-autonomos-ofensiva-judicial-muface/)).
    - Follow-up consultations pay about €7–8.
  - Allied professionals:
    - €5–20 a session, capped at 20–30 minutes;
    - 88.76% of surveyed psychologists say insurers impose terms ([Infocop, 13 Jun 2023](https://www.infocop.es/?p=50249)).
  - Market:
    - the top five insurers hold 71% of health premiums;
    - 24% of Spaniards had private health insurance in 2022;
    - 43,200 self-employed psychologists (2021).
  - About 1,900 Sevilla doctors stopped seeing four insurers' patients in Sept 2023 (single source, search summary).
- **Driver and status (Oct 2026):**
  - Insurer concentration, plus competition law (Art. 101 TFEU), which blocks collective bargaining. Unipromel cites the European Commission's 29 Sep 2022 guidelines on collective agreements by solo self-employed people.
  - Unresolved:
    - the MUFACE 2025–2027 contract is in force;
    - Unipromel's Audiencia Nacional case is pending;
    - the CNMC was asked for help in March 2026 ([Redacción Médica, 24 Mar 2026](https://www.redaccionmedica.com/profesionales/20260324/fisioterapia-eleva-competencia-las-demandas-del-colegiado-autonomo/260131_0.html)); outcome unknown.
  - Caveat: most fee figures come from interested parties (Unipromel, ATA), and some date from 2020–23.
- **Used today and price:**
  - Leaving panels, private-pay patients and litigation. Unipromel suggests patients pay up front and claim reimbursement. No software is documented.
  - Practice software: Clinni at €12.95/month (PRO-03). Doctoralia: prices unpublished (PRO-04).
- **Feeds:** G4-I05

#### C6. Staff qualification records for health centres (RD 239/2026)
- **Pains:** PRO-09
- **Problem:**
  - Who: every authorised health centre, public or private, including dental, physiotherapy, psychology, aesthetic, podiatry and nutrition clinics.
  - Duty: keep up-to-date information and a personal file for every health professional (employee, autónomo or partner), showing their official qualification and specialty, and inform new staff about safe practices. Centres have six months to comply ([BOE RD 239/2026](https://www.boe.es/eli/es/rd/2026/03/25/239)).
  - How often: a one-off build-up, then updates at every hire.
  - How many centres: unknown. Doctoralia alone is present in 5,000 private clinics ([descubre.vc/El Economista, Feb 2026](https://www.descubre.vc/noticia/doctoralia-factura-20m-en-espa-a-y-consolida-su-expansi-n-tecnol-gica-en-latam-y-europa-2026-02-20); PRO-03, PRO-04).
  - Cost: not documented. Exposure comes through regional inspections; centres need prior regional authorisation (RD 1277/2003 art. 3.2).
- **Driver and status (Oct 2026):**
  - In force since 1 Jul 2026.
  - Staff files due about 1 Jan 2027 (the researcher's calculation).
  - Regions adapt the annexes by about July 2027.
  - It also rewrites units U.11 (nutrition and dietetics) and U.36 (pain treatment).
- **Used today and price:**
  - No evidence. The likely practice is folders and spreadsheets (inference).
  - Generic HR tools charge per employee (software table):
    - Sesame from €4.75 per employee per month, with a 15-employee minimum;
    - Factorial Core from 8 USD per user per month, plus modules by quote;
    - Kenjo Starter at €6 per employee.
- **Feeds:** G4-I06

#### C7. Veterinary antibiotic prescribing compliance (PRESVET)
- **Pains:** PRO-05
- **Problem:**
  - Who: companion-animal vet clinics (micro and small), nationally. MAPA (May 2026, search summary; the page returned 503) counts about 16,460 clinicians and about 3.22M antibiotic prescriptions since Jan 2025, with 80% reported automatically through web services ([MAPA PRESVET](https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/Higiene-de-la-produccion-primaria-ganadera/medicamentos-veterinarios/Presvet.aspx)).
  - How often: every antibiotic prescribed or administered must be reported at least every 15 days. Antibiotics are grouped A–D, with antibiogram (lab-test) prerequisites.
  - Fines: €600 to €1.2M ([Hipertextual, Feb 2025](https://hipertextual.com/2025/02/paren-veterinario-espana)). The Castilla y León vets' council says a delay or omission is "muy grave", with a €60,000 minimum fine; this reading was not checked ([Colvet, Mar 2025](https://colvet.es/files/reportajes/informacionveterinaria_marzo_2025.pdf)).
  - Vets say the platform is "difícil de usar" (hard to use), "a veces se cae" (sometimes goes down) and rejects digital certificates.
  - The 2025 protests drew about 2,000 vets (EFE) to nearly 5,000 (OCV, the vets' collegiate body). The counts differ by source.
- **Driver and status (Oct 2026):**
  - RD 666/2023 art. 39, which implements EU Regulation 2019/6. The duty has applied since 2 Jan 2025.
  - RD 767/2025 (in force since 4 Sep 2025) kept PRESVET and requires establishments to document antibiotic-reduction measures ([BOE](https://www.boe.es/eli/es/rd/2025/09/02/767); [Uría Menéndez](https://www.uria.com/es/publicaciones/9470-principales-novedades-en-materia-de-medicamentos-de-uso-veterinario)).
  - The government said repeal "no tendría sentido" (would make no sense).
  - A change to the sanctions regime was reported "en trámite" (going through the Cortes) in March 2025; its status is unverified. If it was still pending on 6 Oct 2026, it lapsed with the dissolution.
- **Used today and price:** about 80% report through practice-software web services (vendors such as Qvet are named but not verified; no prices). The rest type data into the PRESVET website.
- **Feeds:** G4-I07

### 2.3 Professional services

#### C8. Gestorías: staff shortage while invoicing rules keep moving
- **Pains:** PRO-10, PRO-11
- **Problem:**
  - Who: gestorías and asesorías (tax, labour and accounting advisers; micro and small) serving more than 3M SMEs and autónomos.
  - Staff:
    - 7 in 10 firms struggle to hire;
    - 98.4% of professionals are over 30, most over 45 ([Merca2/EDASE, 4 Aug 2025](https://www.merca2.es/2025/08/04/los-despachos-y-gestorias-se-quedan-sin-personal-crisis-en-el-sector-espanol-2219718/); EDASE is an interested party).
  - Context from a vendor blog ([Copilot Gestoría](https://copilotgestoria.com/blog/no-encuentras-personal-asesoria-2026-automatizacion)):
    - Hays expects finance/admin salaries to rise 7% in 2026;
    - INE: 8.7% of firms with 10–49 staff use AI, against 49.2% of large firms;
    - an anecdote of about 30 h a month typing invoices in a 4–8 person firm.
  - How often: each rule change means re-planning for every client and answering "¿me afecta y cuándo?" ("does this affect me, and when?") again. Hours were never measured.
- **Driver and status (Oct 2026):**
  - VeriFactu (RD 1007/2023), dates under RDL 15/2025 ([Legal Today](https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/nueva-prorroga-verifactu-no-sera-obligatorio-hasta-2027-para-sociedades-y-otros-contribuyentes-2025-12-04/)): 1 Jan 2027 for corporate-tax payers and 1 Jul 2027 for everyone else. In force.
  - A move to October 2028 was announced on 5 Oct 2026. No legal instrument exists yet, and it needs a norm with the rank of law ([CMS](https://cms.law/en/esp/publication/factura-electronica-b2b-arranca-la-cuenta-atras-y-veri-factu-se-aplaza-a-2028); [TeamSystem](https://teamsystem.es/magazine/verifactu-se-aplaza-2028/)).
  - B2B e-invoicing: RD 238/2026 (in force since 20 Apr 2026) and Orden HAC/1028/2026 (BOE 5 Oct 2026). Turnover above €8M is obliged from 6 Oct 2027, everyone else from 6 Oct 2028 ([Garrigues](https://www.garrigues.com/es_ES/noticia/comienza-computo-plazos-aplicacion-factura-electronica-obligatoria-empresarios.md)).
  - Draft dates ([Consejo General de Gestores](https://www.consejogestores.org/?p=14916)): the public solution (SPFE) goes online on 1 Aug 2027; invoice-status reporting for firms up to €8M starts on 1 Oct 2029.
  - The Basque Country and Navarra run their own foral systems (TicketBAI).
- **Used today and price:**
  - Client-side tools (software table):

    | Product | Price per month |
    |---|---|
    | AEAT VERI*FACTU app | free |
    | FacturaScripts | free |
    | Billin | free to €20 |
    | Contasimple | free to €15.95 |
    | a3factura | from €9.95 |
    | Holded | €7.50–99.50 on annual billing (about double if billed monthly) |
    | Quipu | €17–59 |
    | Sage Active | from €25 |
    | Sage 50 | from €45 |
    | A3ERP | about €600 a year |

  - Gestoría automation tools: Copilot Gestoría, a3, Sage, ContaPlus. No prices.
  - The software table notes a3 is "la opción obligada si tu asesor externo lo usa" (the obligatory option if your adviser uses it): the gestor's choice drives clients' software.
- **Feeds:** G4-I08

#### C9. The MASC pre-litigation requirement for civil claims
- **Pains:** PRO-12
- **Problem:**
  - Who: small law firms and autónomo lawyers in civil and commercial work, plus landlords and administradores de fincas (property managers) in eviction cases.
  - What they must do before filing ([PwC, Jan 2025](https://periscopiofiscalylegal.pwc.es/wp-content/uploads/2025/01/Retos-derivados-de-los-MASC-como-requisito-de-procedibilidad.pdf)):
    - send a negotiation invitation (MASC: an approved out-of-court dispute-resolution step);
    - prove receipt at an address that belongs to the counterparty;
    - record the outcome and describe it in the claim, "so pena de inadmisión" (or the claim is rejected).
  - Penalties: refusing to negotiate risks costs (arts. 245, 394 and 395 LEC) and fines for abuse (art. 247).
  - Courts apply it unevenly:
    - Las Palmas rejects claims that ignore it ([criteria](https://confilegal.com/wp-content/uploads/2025/04/UNIFICACION-CRITERIOS-MASC-INSTANCIA-LPGC.pdf), search summary);
    - Collado Villalba excludes some procedures;
    - case law requires proving the address belongs to the defendant ([Economist & Jurist](https://www.economistjurist.es/?p=231084)).
  - Scale ([InDret 2/2026](https://indret.com/wp-content/uploads/2026/04/2006.pdf)): 3,563,038 new civil cases in 2024 (about +20%) and 2,688,606 pending. Before the reform, court-referred mediation was negligible: 647 referrals, 70 agreements.
  - How often: almost every civil claim, subject to exclusions.
  - Not found: inadmission statistics and time cost.
- **Driver and status (Oct 2026):** LO 1/2025. MASC required since 3 Apr 2025. In force.
- **Used today and price:**
  - Burofax (certified letter) and certified-email services, mediators, and lawyers' own templates.
  - Practice software with LexNET (court e-filing) integration: MN Program from €1 a day; SuDespacho from €35.95/month ([Upliora, 21 Oct 2026](https://www.upliora.es/blog/ia-despachos-procuradores-abogados-lexnet-software-gestion-2026), vendor blog). Kmaleon, Aranzadi Fusión and Tirant do not publish prices.
  - E-signature: Signaturit Business at €35 per user per month on annual billing, 5 envelopes (software table).
- **Feeds:** G4-I09

### 2.4 Education and care

#### C10. The driving-school practical-exam bottleneck
- **Pains:** PRO-14
- **Problem:**
  - Who: driving schools, mostly micro and small, plus chains (Autoescuela Lara has 65 centres in Madrid).
  - Where: hotspots in Andalusia, Catalonia, Madrid, Murcia, Valencia and Alicante, Baleares, Navarra, Tenerife and Aragón.
  - Volume and capacity: more than 1M practical tests a year; 12 tests per examiner per day; 46% fail their first practical ([Xataka, Sep 2025](https://www.xataka.com/movilidad/se-frustran-dejan-autoescuelas-denuncian-que-lista-esperar-para-examen-conducir-interminable-dgt-niega)).
  - Waits: 1.5–5 months in Madrid; 2–3 months for a retest in Valencia.
  - Conflict on queue size:
    - the sector claims 82,000 students queuing in Andalusia ([El Español, Jul 2026](https://www.elespanol.com/invertia/20260717/autoescuelas-pie-guerra-alumnos-esperan-practico-andalucia-faltan-examinadores/1003744322825_0.amp.html)) and 63,000 in Barcelona;
    - when the DGT (traffic authority) offered unlimited extra exams, under 10% were presented (Navarra 275 of more than 6,000; Barcelona 1,450 of 63,000) ([DGT, 16 Jun 2026](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/2026/20260616-nota-de-prensa.pdf));
    - the DGT's head says "solo un 8 %" (only 8%) are ready ([Motor.es](https://www.motor.es/noticias/pere-navarro-dgt-enfurece-autoescuelas-listas-espera-2026114254.html)).
  - Cost: extra lessons, cars and instructors tied up, and students who give up. No euro figures.
- **Driver and status (Oct 2026):**
  - Examiner capacity: 130 new posts, reaching 21 examiners per million inhabitants; about 50 new examiners a year.
  - CAPA allocation, which splits each office's slots by schools' theory pass rates and candidate numbers ([Vozpópuli 2021](https://www.vozpopuli.com/economia/lista-espera-carne-conducir.html), dated).
  - The DGT's PRO reinforcement plan ran as a pilot in May–June 2026 and is being extended (Barcelona from 13 Jun 2026, Tenerife from late June). Ongoing.
- **Used today and price:** Saturday PRO sessions, sending students to smaller centres, and protests. Driving-school software was not researched.
- **Feeds:** G4-I10

#### C11. Home-help (SAD) providers squeezed by hourly caps that include travel
- **Pains:** PRO-17
- **Problem:**
  - Who: home-help (SAD) companies, from small regional operators to large groups, plus not-for-profits, working under municipal tenders. Documented in Vigo, El Puerto de Santa María, Orihuela, Granada and Catalonia.
  - Cost evidence:
    - Vigo: €49.5M over 3 years, with the hourly price rising from €16.70 to €22 because of wage increases ([Vigo e, Mar 2025](https://vigoe.es/vigo/local/vigo-pone-en-marcha-uno-de-sus-megacontratos-y-caballero-exige-que-lo-pague-la-xunta)).
    - A Catalan tender's hourly price "incluye todos los costes organizativos como desplazamientos, coordinación, supervisión y formación" (includes all organisational costs such as travel, coordination, supervision and training) ([TED](https://ted.europa.eu/es/notice/92082-2025/pdf), search summary).
    - Orihuela capped the price at €17/h (2020, dated).
    - El Puerto: more than €5.6M over 2 years for about 400 users (2023).
  - Staffing rule: at least 50% of SAD contracts must be full-time (2022 accreditation agreement, [Público](https://www.publico.es/sociedad/seran-partir-residencias-mayores.html)).
  - How often: every visit day. Loss figures not found.
- **Driver and status (Oct 2026):** public procurement (LCSP) and dependency-law funding. Ongoing.
- **Used today and price:** re-tendering at higher prices and lobbying regions. Scheduling and route software was not researched.
- **Feeds:** G4-I11

#### C12. Households as employers of domestic and care workers
- **Pains:** PRO-18
- **Problem:**
  - How many: about 348,000 registered domestic workers ([INSST, May 2025](https://www.insst.es/documents/d/portal-insst/yolanda-diaz-presenta-la-herramienta-para-evaluar-los-riesgos-laborales-de-las-trabajadoras-del-hogar-nota-de-prensa)) to more than 378,000 ([El Español, May 2026](https://www.elespanol.com/mujer/estilo-vida/20260520/asesora-financiera-nueva-ley-limpiadoras-hogar-unico-consigue-nadie-contrate/1003744249353_0.amp.html)), and roughly as many employing households. The EPA labour-force survey counts about 540,000.
  - Workforce facts:
    - about 38,000 live-in workers;
    - average salary about €1,014 a month;
    - the sector lost 53,000 workers in a year;
    - the minimum wage (SMI) has risen 61% since 2018 (AESPD, the employers' association).
  - Duties:
    - an online risk assessment through Prevencion10;
    - putting the measures in place and informing the worker;
    - keeping the signed plan at home; the deadline was 14 Nov 2025 ([El Salto](https://www.elsaltodiario.com/trabajo-domestico/prevencion10-herramienta-evaluacion-riesgos-empleo-hogar));
    - on top of these, Social Security registration and monthly contributions, including unemployment contributions since 2022.
  - The tool collapsed at launch (about 50M access attempts in 24 h).
  - The guide, harassment protocol and training platform promised for early 2026 were still pending in May 2026.
  - How often: monthly payroll, yearly minimum-wage updates.
- **Driver and status (Oct 2026):**
  - RD 893/2024 in force since 13 Sep 2024; the household deadline has passed.
  - RDL 16/2022 in force.
  - ILO Convention 189 in force in Spain since 24 Feb 2024.
  - The unions UGT and CCOO asked inspectors not to be punitive at first.
  - Fine amounts not found.
- **Used today and price:**
  - Prevencion10: free, covers the risk assessment only.
  - Gestorías and advisers (Dancausas Asesores is quoted). No prices.
  - Household-payroll platforms were not researched.
- **Feeds:** G4-I12

---

## 3. Noise log

| Pain ID | Title | Code | One-line justification |
|---|---|---|---|
| RET-01 | Steady attrition of neighbourhood shops | N2 | Strong evidence (UPTA about 13.6k net closures in 2025; Madrid −14% in 2020–24), but the drivers are structural (rent, succession, costs, platforms, now also energy); software only trims admin at the margin. |
| RET-02 | Commercial rent shocks at lease renewal | N2 | Real-estate pressure under freely negotiated leases; case evidence only (+31% up to 4×) with no national scale; at most a rent-benchmark or renewal-alert feature. |
| RET-03 | No successor for retiring owners | N1 | Qualitative cases from two outlets with no scale; the core problem (many shops are no longer attractive to buy) is also not software-solvable. |
| RET-05 | Card-acceptance fees and Bizum at the till | N7 | Same pain as FIN-13 (cashflow track) and VOX-07 (voice track). Merge RET-05's evidence there: Bizum in-store since 18 May 2026, SumUp at 1.49%, and conflicting fee ranges (0.3–1.5% vs 0.5–2%). Acquirers set the fees. |
| RET-06 | Ultra-low-cost cross-border platforms | N2 | A trade-policy and market force. The EU €3 duty has applied since 1 Jul 2026; sources conflict on whether it is per category or per item. Impact on Spanish shops not quantified. |
| RET-07 | Thin or decaying web presence after Kit Digital | N1 | Reported INE figures contradict each other (29.6% / 33.2% / 37.0%). Abandonment evidence is a LinkedIn opinion and a 2023 article. Crowded market (also N4). Kit Digital's 2026 status unverified. |
| RET-08 | Sunday and holiday trading rules, ZGAT fights | N2 | Regional politics; software could offer only a calendar lookup; cost not quantified. |
| RET-09 | 30-day "precio anterior" rule on discounts | N1 | The rule is verified (Ley 7/1996 art. 20; fines up to €900,000), but there is no enforcement or complaint data, and existing POS and e-commerce price-history features were not researched. If validation finds enforcement, a trivially copyable plugin at about €5/month is possible. |
| RET-10 | WhatsApp per-message pricing | N1 | One official source. Affects only API users, whose number is unknown; Spain's rates not captured. Used as a cost input in G4-I04. |
| RET-12 | Parcels damaged in transit | N1 | A single study sponsored by a packaging maker (DS Smith, via Alimarket), uncorroborated. Possible later module of G4-I02 if validated. |
| RET-13 | Amazon fee stacks and opaque margins | N1 | Fees verified only on Amazon's own page; no seller complaints or seller counts captured. Fees eased for low-price items (Dec 2025–Jan 2026) while a 1.5% FBA surcharge arrived (Apr 2026). Profit tools not researched (likely N4). |
| RET-14 | Selling to Canarias, Ceuta and Melilla | N1 | Key figures date from 2021–22 (over 60% of shops do not ship); the only 2026 signal is a 3-signature petition. Re-test: with current data it could become a type B landed-cost and customs idea (IGIC 7%, AIEM 5%, DUA waived under €150). |
| RET-17 | Web accessibility (EAA / Ley 11/2023) | N7 | Duplicate of LEG-16 (legal track). Covers only non-micro online shops; no enforcement data; scanners solve it only in part. |
| RET-18 | Product-safety information on listings (GPSR) | N1 | No Spain-specific pain or enforcement evidence (an Irish regulator source, vendor blogs, a toy-association snippet); marketplaces already enforce it. |
| RET-20 | 21% VAT on hairdressing and beauty | N2 | Tax policy. Cuts were rejected or vetoed in 2021 and 2022; no change found for 2025–26. |
| RET-21 | Independent gyms squeezed by low-cost chains | N2 | The evidenced pain is price competition from consolidating chains (the top 10 hold 54%). The software-solvable part (churn, dunning) has no Spanish data; see gaps below. |
| RET-22 | Pet shops under Ley 7/2023 | N5 | The ban on selling dogs, cats and ferrets in shops (since about Sept 2024) is not software-solvable. The remaining contract and record duties are a small market, and the registry duties depend on implementing regulations of unverified status (also N3). |
| PRO-03 | No-shows and front-desk work in clinics | N4 | Cheap tools exist (Clinni at €12.95/month with email, SMS and Telegram reminders; Doctoralia reminders). The 12–19% and €2,500–7,500/month figures come from a vendor via one wire story (also N1). |
| PRO-04 | Dependence on Doctoralia/Docplanner | N1 | Prices unpublished; complaints thin (one Capterra summary); no evidence on Top Doctors; a small tool cannot attack the two-sided network. |
| PRO-06 | Vets cannot dispense full treatments | N2 | A regulatory barrier (RD 666/2023, RDL 1/2015), only partly relieved by RD 767/2025; software could only route prescriptions. |
| PRO-07 | Pharmacy shortage management | N4 | Served by the profession's own tools (CisMED with 13,483 pharmacies; FarmaHelp) and improving (27% fewer medicines with incidents in 2025). The 11–12 h/week figure is an EU average. |
| PRO-08 | Health-data protection exposure | N1 | One documented fine (€16,000, a pharmacy using Excel); no 2024–26 fines against clinics found; AEPD totals conflict (€40M vs €48.1M); patient-record software at about €13/month already covers records (also N4). Kept as a build constraint for G4-I04 to I07. |
| PRO-13 | Court reorganisation and LexNET notification load | N1 | Vendor (Upliora) and 2018/2020 sources; no 2025–26 outage evidence; LexNET has no public API; practice software with LexNET exists (MN Program, SuDespacho). |
| PRO-15 | 0–3 nurseries: ratio cut and free-place schemes | N3 | The ratio cut is only a proposal (no BOE text and no ratio figures as of 23 Oct 2026); closure numbers are ACADE projections; subsidy administration is region-specific (also N5). |
| PRO-16 | Residences: 2029 accreditation vs low concert prices | N2 | The core pain is funding (concert prices of €54/day or less against an estimated €75) and building works. Sources are from 2021–22, regional transposition is unverified, and the rostering angle was not researched. |

### Evidence gaps to re-test (not noise)
The search cap left these without evidence. Missing evidence is not proof that the pain is absent.

| Gap | Where it would plug in | What to look for |
|---|---|---|
| Salon no-show rates and losses; legality of deposits | G4-I04 | Spanish statistics (only uncited vendor claims exist); consumer-law position on deposits and no-show fees |
| Gym churn and failed direct debits | RET-21, as a possible retention or dunning idea | Churn rates; AimHarder, Trainingym and Bewe prices |
| Academies (languages, tutoring, oposiciones exam prep); returned SEPA direct-debit receipts; parent-communication apps (Dinantia, Additio, TokApp); extracurricular providers | Possible new education cluster | Evidence of pain; tool prices |
| FUNDAE-subsidised training paperwork | Possible new cluster for training providers | Justification and inspection burden |
| Driving-school software and prices | G4-I10 | Vendors and prices |
| Clinic software prices (Gesden, Clinic Cloud, Qvet); Top Doctors | G4-I05 to I07 | Prices and features |
| Household-payroll platforms; cleaning and childcare agencies | G4-I12 | Competitors and prices |
| Chargebacks and friendly fraud in Spain; carrier rates; ad costs; Miravia and eBay fees | E-commerce | Spanish data |
| Tattoo sanitary rules and the REACH tattoo-ink restriction; right to repair; laundries; pet groomers | Personal services | Rules and their status |
| Architects, engineers, translators, marketing agencies | Professional services | Any evidence |

---

## 4. Candidate SaaS ideas

### G4-I01: Shop theft incident log and police-ready report pack
- **Type:** B (primary), secondary C (set up once per shop, then a low-touch subscription)
- **Buyer:**
  - Owners or managers of independent physical shops, starting with food and convenience retail, the most affected segment.
  - Also local retail associations buying for members, and city councils, which may now prosecute theft themselves (RET-04).
  - How many: unknown as a number of shops; validate. Proxies in the notes (RET-01): 716,637 retail affiliates in Dec 2025 (UPTA; a Social Security affiliation count, not shops), and 43,769 neighbourhood shops in the Comunidad de Madrid in 2024 (INE via [Madrid Informa](https://madridinforma.es/?p=38863)).
- **Pains addressed:** RET-04
- **Problem:** Spanish retail loses €2,817M a year to unknown loss (1.1% of turnover). 51% of thefts are by repeat offenders, and small shops suffer about 30% more thefts (RET-04). Since 10 April 2026 a repeat thief faces prison only once three prior final convictions exist, so consequences depend on shops reporting every incident in a form that can be prosecuted, which costs staff time they do not have (the link is the researcher's inference).
- **Product:**
  - Does:
    - lets staff log an incident from a phone in about a minute: time, items scanned or picked with their value, description, witness, and a CCTV clip reference with an automatic retention limit;
    - produces a draft police report (denuncia) and an evidence pack (PDF with item list, values and a hash of the clip), in the form each police force accepts;
    - tracks report numbers, court dates and outcomes;
    - sends a monthly loss report (what is stolen, and when) for staffing and insurance.
  - MVP (a few weeks): incident form, barcode and value capture, PDF pack, case tracker, clip upload with auto-deletion. Covers one city (Madrid or Barcelona) and its police force's filing route.
  - Deliberately not: facial recognition; shared offender lists or "wanted" boards between shops; public naming; hardware (tags, cameras); representation in court.
- **Why now:**
  - LO 1/2026 has been in force since 10 April 2026 (BOE consolidated text). It brings the prison penalty after three prior final convictions, and removes the €400 cumulative-value threshold (per AECOC).
  - Local authorities may now prosecute theft (new LECrim art. 105.3), and courts can ban offenders from specified places (art. 544 bis) (RET-04).
  - Staff aggression (74% say it rose a lot) and guard shortages (65%) push shops towards options other than guards.
  - Status caveat: the cities track could not verify the reform. RET-04's BOE citation is the stronger source.
- **Alternatives today:**
  - EAS tags (Checkpoint Systems co-authors the theft barometer), CCTV and security guards. No prices in the notes.
  - No incident-reporting software was researched (RET-04).
  - Weakness: hardware deters thieves but does not build the record of reported, prosecuted incidents that the new law relies on. Guards are increasingly hard to hire.
- **Price hypothesis:**
  - €9–15/month per shop, flat.
  - €3–5 per shop per month in association bulk deals.
  - A yearly district licence for councils.
- **Channels:**
  - Associations: COCEM (Madrid retail confederation), UPTA, AECOC (food retail; runs the barometer), neighbourhood traders' associations (e.g., Raval).
  - Councils' commerce departments, police community-liaison units, shop insurers.
  - Searches such as "denuncia hurto tienda" and "multirreincidencia comercio".
- **Build notes:**
  - CCTV images are personal data: retention limits, signage, legitimate interest, and probably a DPIA (see LEG-06 in the legal track). EU hosting.
  - Online filing routes differ by force (Policía Nacional, Mossos d'Esquadra, Ertzaintza, Policía Foral, Guardia Civil, local police), and some may not accept attachments.
  - Optional POS link for item values.
  - Complexity: low–medium.
- **Moat in an AI-flooded market:** low. A form plus a PDF can be copied in days. Harder to copy:
  - partnerships with associations and councils;
  - templates refined per police force and court;
  - an anonymised loss dataset by district and product that insurers and councils may pay for.
- **Key risks and kill criteria:**
  - Risks:
    - the bottleneck may be police and court capacity, or owners' reluctance to testify, rather than paperwork;
    - sharing suspects across shops is off-limits under data protection;
    - associations or councils may offer a free tool.
  - Kill if:
    - fewer than about a third of interviewed owners say they would report more with a one-minute flow; or
    - the main police forces will not accept prepared packs; or
    - a free association or council tool already exists.
- **Evidence strength:** medium. Loss figures and the law are strong (barometer, AECOC, BOE), but demand for reporting software is an inference that no source states.
- **Validation questions:**
  1. Re-check on the BOE that LO 1/2026 is in force in October 2026, and settle the conflict with `cities_macro_surveys.md`.
  2. For Policía Nacional, Mossos d'Esquadra and Ertzaintza: can a shop file a theft (hurto) report online with attachments? What evidence do prosecutors need to convict for a delito leve de hurto?
  3. Interview 15–20 food and convenience shops in Madrid and Barcelona: share of incidents reported today, time per report, court burden, willingness to pay €9–15/month.
  4. Look for existing incident-reporting tools or programmes in Spain (AECOC, COCEM, local associations, police-run shop-safety schemes) and abroad (e.g., Auror; not in the notes), with prices.
  5. Check AEPD guidance on handing CCTV clips to police and on retention periods (cross-check LEG-06).
  6. Has any council used LECrim art. 105.3 since April 2026 (Madrid, Barcelona, Valencia), and would it fund a district tool?
  7. Get the Barómetro del Hurto breakdown by shop size and the loss per shop (Checkpoint Systems/AECOC), and resolve €2,817M vs €2,917M.

### G4-I02: Returns and exchange portal with serial-returner rules for small online fashion shops
- **Type:** A (primary: cheaper and narrower than ShippyPro and Outvio for the returns job), secondary B (rules for serial and late returners)
- **Buyer:** online SMEs selling clothing, footwear or electronics (micro to medium); the owner or e-commerce manager. How many: unknown; validate. CNMC e-commerce data were not consulted (RET gaps).
- **Pains addressed:** RET-11. Possible later modules: RET-12 (transit-damage claims) and RET-14 (island shipping), both filtered N1.
- **Problem:** 23.7% of non-food online orders were returned in 2025 (clothing 31%), worth €13.3bn. Serial returners (11% of shoppers) generate 23% of returns, and late returners another 24% (RET-11). Shoppers punish return fees (35% might stop buying; only 21% would pay), so small shops need targeted rules rather than a blanket charge.
- **Product:**
  - Does: an app for Shopify, WooCommerce or PrestaShop with:
    - a branded returns portal;
    - an exchange-first flow (size swap or store credit before a refund);
    - capture of return reasons;
    - a return score per customer, built only from the shop's own orders, with rules (e.g., a paid return, or inspection before refund, for serial returners);
    - automatic enforcement of the return window;
    - return-rate dashboards by product and size.
  - MVP: one platform; labels through one existing aggregator or carrier API; exchange-first flow; per-shop returner score; reason analytics.
  - Deliberately not: blacklists of consumers shared across shops (profiling risk); own carrier contracts; warehouse handling; AI fit prediction (later).
- **Why now:** there is no regulatory trigger. Volumes are high, and returns are slow (9.1 days on average; 32% after 10 days), so stock and cash sit idle (RET-11). Label tools are commoditised, which leaves returns abuse as the open edge (RET inference).
- **Alternatives today:**
  - ShippyPro Professional: €207.20/month for 4,000 labels.
  - Outvio: about €375/month (a competitor's estimate).
  - Sendcloud: free plan, and Lite at €28/month billed annually (snippet).
  - ZigZag sells returns software (price not in the notes) (RET-11).
  - Weakness: the mid-market suites are priced on shipping volume, and it is unknown whether any entry tier offers exchange-first flows and returner rules.
  - Sendcloud's free and €28 tiers are cheaper than this idea, so the reason to switch must be the returns logic, not price.
- **Price hypothesis:** €19–39/month by order volume, with no per-label fee; or about €0.50 per processed return for very small shops.
- **Channels:**
  - Shopify App Store, WooCommerce and PrestaShop marketplaces.
  - Spanish e-commerce agencies; Adigital and Confianza Online member networks; label aggregators as partners.
  - Searches such as "gestión de devoluciones tienda online" and "cambio de talla Shopify".
- **Build notes:**
  - Platform and carrier APIs (Correos, SEUR, GLS and MRW were not researched).
  - Consumer-law rules on the 14-day withdrawal right and refunds (general knowledge, not re-verified), plus any Ley 10/2025 changes (LEG-12).
  - Transparency for customer scoring under GDPR.
  - Complexity: medium.
- **Moat in an AI-flooded market:** none — speed only. App-store reviews and integrations with Spanish carriers give a short head start.
- **Key risks and kill criteria:**
  - Risks: Sendcloud's or Outvio's low tiers, or the platforms' own returns features, may already do this; very small shops may lack the volume to care.
  - Kill if any plan under about €30/month already offers exchange-first flows and returner rules, or if interviews show the cost is logistics rather than abusive returners.
- **Evidence strength:** medium. Volume figures come from a returns-software vendor (ZigZag with Retail Economics), with two survey snippets supporting the pressure to keep returns free. The cost per return is unknown.
- **Validation questions:**
  1. Check entry plans at Sendcloud (free, Lite), Outvio and ShippyPro for returns portals, exchanges and returner rules. Confirm €207.20, about €375 and €28 on the vendors' own pages.
  2. Find returns apps active in Spain and their € prices: ZigZag, and international examples such as Loop Returns, AfterShip Returns and ReturnGO (not in the notes).
  3. Find the handling cost per return for Spanish fashion SMEs.
  4. Legal: may a Spanish shop charge return shipping only to serial returners, or inspect before refunding, under the consumer law as amended by Ley 10/2025 (LEG-12)?
  5. Size the buyer pool: Spanish online fashion and footwear SMEs (CNMC, INE, platform store counts).
  6. Interview 10 small fashion e-shops on return rates, current tools and willingness to pay €19–39/month.

### G4-I03: Packaging EPR, PPWR and plastic-tax compliance kit for small online sellers and importers
- **Type:** B (primary), secondary C (records kept once, then reminders and yearly packs)
- **Buyer:** SMEs that pack goods or first place packaged goods in Spain: online shops shipping their own products, importers and intra-EU buyers. The owner, operations or finance lead pays. How many: unknown; validate (producer numbers not found, RET-15). The industry track's IND-12 cites more than 27,300 food and drink companies as an adjacent pool.
- **Pains addressed:** RET-15, RET-16
- **Problem:** Sellers must register as packaging producers (the number goes on invoices), join a collective scheme, and file packaging data by material before 31 March each year. Since 12 August 2026 they must also issue PPWR declarations of conformity and marking; importers above 5 kg a month of non-recycled plastic must register, keep a stock ledger and file modelo 592 with certified proof of recycled content (RET-15, RET-16). Distributors may only sell products from registered producers, so a gap can cut a seller out of retail channels. The duty is mostly invisible until a marketplace, distributor or inspector asks (RET inference).
- **Product:**
  - Does:
    - a packaging register per product (material, weight, recycled-content certificate, supplier), built from templates and supplier data;
    - yearly tonnage by material for the 31 March declaration (simplified form under 15 t);
    - a plastic-tax calculator working from purchase or import lines, with a check of the 5 kg/month exemption, a stock-ledger export and a modelo 592 worksheet;
    - a PPWR declaration-of-conformity generator per packaging item;
    - a supplier tracker that collects and checks producer registration numbers.
  - MVP: CSV or Shopify product import; packaging templates; tonnage calculation; 31 March pack; modelo 592 worksheet; supplier registration tracker.
  - Deliberately not: acting as a collective scheme or authorised representative; filing for the user (except through partner gestorías); redesigning packaging for the 2030 recyclability rules.
- **Why now:**
  - The PPWR has applied since 12 August 2026.
  - RD 1055/2022's deadlines for schemes (31 Dec 2024) and marking (1 Jan 2025) have passed.
  - The next yearly declaration is due before 31 March 2027 (computed from art. 16).
  - The AEAT updated its plastic-tax page on 20 October 2026 (RET-15, RET-16).
  - A December 2025 EU Omnibus proposal would suspend the authorised-representative duty for direct cross-border sellers (a proposal only, reported in IND-12).
- **Alternatives today:**
  - Collective schemes (GENCI; Cartón Circular, with a published 2026 tariff; Ecoembes for household packaging), consultants, gestorías, ERP systems and certification bodies. No prices in the notes (RET-15, RET-16).
  - Weakness: unknown. Validate whether schemes give members free declaration tools.
- **Price hypothesis:** €19–49/month by number of products, or €149–299 a year for the declaration season. White-label for schemes or gestorías.
- **Channels:**
  - Collective schemes (as a member onboarding tool), packaging suppliers, gestorías, e-commerce app stores, customs agents.
  - Marketplaces, since platforms carry duties for third-party sellers (art. 17).
  - Searches such as "registro de productores de envases", "declaración anual envases 31 de marzo" and "modelo 592".
- **Build notes:**
  - Rules for household versus commercial and industrial packaging.
  - Access to the MITECO producer registry (whether it can be looked up publicly is unverified).
  - AEAT modelo 592 format; PPWR declaration details (validate).
  - Low data sensitivity.
  - Complexity: medium for the rules, low technically.
- **Moat in an AI-flooded market:** moderate. The calculator is easy to copy. Harder to copy:
  - regulatory know-how;
  - partnerships with schemes or gestorías;
  - a growing dataset of verified supplier registration numbers and packaging specs, useful to distributors who must check their suppliers.
- **Key risks and kill criteria:**
  - Risks:
    - the burden and scheme fees are unquantified;
    - many small sellers may sit in simplified regimes or below 5 kg a month;
    - enforcement is unknown;
    - schemes may give tools away.
  - Kill if schemes already offer free tools covering the declaration and PPWR paperwork, or if small sellers report no checks from marketplaces, distributors or inspectors.
- **Evidence strength:** medium. The rules are strong (BOE, AEAT, a scheme's commentary on the PPWR), but cost and pain intensity were not captured.
- **Validation questions:**
  1. How many producers are in the packaging section of the Registro de Productores de Producto (MITECO), and how many businesses file modelo 592 (AEAT)?
  2. Scheme fees and member tools at Ecoembes, GENCI and Cartón Circular: do they include free declaration software?
  3. Sanctions for breaching RD 1055/2022 (referred to Ley 7/2022), and any enforcement in 2025–26, including marketplaces or distributors refusing unregistered producers.
  4. Which PPWR declaration and marking duties bind SMEs since 12 August 2026? What is the status of the Omnibus proposal (IND-12)?
  5. Can registration numbers be checked through a public registry or API?
  6. Existing EPR software in Spain or the EU and its prices (e.g., consultancy portals, Lizenzero-type services; not in the notes).
  7. Interview 10 small online sellers and importers: are they aware of these duties, who handles them today, and at what cost?

### G4-I04: Commission-free direct booking for salons, with deposits and client-data import
- **Type:** A (primary: a cheaper, simpler alternative to Booksy and Treatwell for repeat clients), secondary C (low-touch once set up)
- **Buyer:** hair salons, barbers, beauty and nail centres, mostly autónomos and micro firms (60% of salons had a single worker in 2021). The owner pays (RET-19, RET-20). How many: about 72,300 hairdressing and beauty establishments (DBK 2021, snippet) against about 35,000 salons (sector figure, June 2021). The definitions probably differ; validate.
- **Pains addressed:** RET-19, with RET-10 as a cost input
- **Problem:** Treatwell takes 25% of a new marketplace client's first booking under a 12-month minimum contract. Booksy charges €34.99/month plus €8 per extra staff member, and takes 30% of a new client's first visit through Boost, capped at €50 (RET-19). Owners complain of commissions charged even when the client does not show, of support that doesn't answer and of difficulty exporting client data; most of their software spend is fees that grow with sales.
- **Product:**
  - Does:
    - a booking page linked from Google Business Profile, Instagram and WhatsApp;
    - a calendar for 1–5 staff;
    - deposits or card-on-file through a payment provider at cost, with no platform commission;
    - reminders by email or SMS, and free WhatsApp click-to-chat links that avoid per-message API fees;
    - one-click import of client lists exported from Booksy, Treatwell or Koibox;
    - prompts to rebook.
  - MVP: booking page, calendar, deposits, reminders, CSV import.
  - Deliberately not: a marketplace that finds new clients (salons can keep Booksy or Treatwell for discovery); payroll; stock; its own VeriFactu invoicing (use a partner instead).
- **Why now:**
  - Incumbents bundle payments (about 2%) and VeriFactu/TicketBAI invoicing to deepen lock-in (Treatwell's Advanced plan; RET-19).
  - VeriFactu is legally due in 2027, with a move to October 2028 announced but not in the BOE (PRO-11), so salons may review their stack in 2027 (my inference).
  - Since 1 October 2026, WhatsApp API utility messages inside the 24-hour window are charged, which raises the cost of API-based reminders (RET-10).
- **Alternatives today:**
  - Booksy: €34.99 + IVA a month plus €8 per extra staff member (about €66.99 + IVA for five staff); Boost 30% capped at €50; card payments 2% + €0.15.
  - Treatwell: 25% of first bookings; 2% + IVA on prepayments; 12-month minimum.
  - Koibox from €40/month; Flowww from €59/month (snippets); Bewe (no price) (RET-19).
  - For payments, SumUp charges 1.49%, or €19/month at 0.75% (software table).
  - Weakness: commissions on new clients, lock-in, and complaints about support and data export (Pabau, a competitor; Capterra snippets).
- **Price hypothesis:** €9–15/month flat for 1–3 staff, plus €3 per extra staff member. 0% commission; card fees passed through at cost.
- **Channels:**
  - Salon and beauty associations (e.g., the Valencian salon groups behind the VAT protests).
  - Stanpa (the cosmetics industry association) and hair-product distributors; beauty wholesalers and schools.
  - Instagram and TikTok.
  - Searches such as "alternativa a Booksy", "comisión Treatwell" and "exportar clientes Booksy".
- **Build notes:**
  - A payment provider with strong customer authentication for card-on-file.
  - Google booking integration (validate).
  - Client data under GDPR, possibly health-adjacent for aesthetic treatments.
  - Whether no-show deposits and fees are legal under Spanish consumer law is unverified (a PRO-03 gap).
  - VeriFactu-compliant invoicing through a certified partner.
  - Complexity: low.
- **Moat in an AI-flooded market:** none — speed only. The researcher already calls the market crowded; distribution partners (distributors, associations) are the only edge.
- **Key risks and kill criteria:**
  - Risks:
    - salons may stay on marketplaces for discovery;
    - free booking tools that earn on payment fees may already be common in Spain;
    - willingness to pay and retention are low in micro salons.
  - Kill if a free tool with the same features is widely used, or if interviews show repeat clients already book by WhatsApp or phone at no cost and owners see no gain.
- **Evidence strength:** medium. Prices and terms come from vendor pages and a competitor's blog, and complaints from Capterra snippets. There is no data on no-show losses or on salons' intent to switch.
- **Validation questions:**
  1. List free and low-cost booking tools used by Spanish salons, with their fees: e.g., Fresha and Reserve with Google (not in the notes), Bewe, AgendaPro.
  2. Confirm Treatwell's and Booksy's current terms: 12-month minimum, Boost cap, export options.
  3. Interview 20 salons in Madrid and Valencia: share of bookings from marketplaces versus repeat clients, monthly commissions paid, interest in moving repeat clients to their own channel.
  4. Legal: may salons charge no-show deposits or fees under the consumer law as amended by Ley 10/2025 (LEG-12)?
  5. Find Spanish no-show data for salons (none in the notes).
  6. Resolve the salon count with INE DIRCE data (CNAE 96.02).
  7. Get Spain's WhatsApp Business Platform rates for utility messages, and check whether click-to-chat reminders work at scale.

### G4-I05: Private-pay and reimbursement-claim kit for self-employed health professionals
- **Type:** B
- **Buyer:** the professional: self-employed psychologists, physiotherapists, podiatrists, dietitian-nutritionists, speech therapists, dentists and specialist doctors on insurer panels, plus micro clinics. How many: 43,200 self-employed psychologists on 31 March 2021 (Ministry of Labour via Infocop) (PRO-02); other professions unknown; validate.
- **Pains addressed:** PRO-01, PRO-02
- **Problem:** Insurers pay €5–20 for an allied-health session and about €17–19 for a specialist consultation (follow-ups about €7–8), with sessions capped at 20–30 minutes; 88.76% of surveyed psychologists say the terms are imposed. The top five insurers hold 71% of premiums, and competition law blocks collective bargaining (PRO-01, PRO-02). Unipromel suggests patients pay up front and claim reimbursement, but small practices have no tool to model leaving panels or to prepare the paperwork.
- **Product:**
  - Does:
    - a payer-mix calculator: imports appointment and billing history (CSV from practice software) and shows net € per hour by insurer and for private patients, including session caps;
    - a reimbursement pack for each private session: the invoice plus the report fields each insurer requires, with a step-by-step guide for the patient;
    - message templates for moving panel patients to private sessions.
  - MVP: payer-mix dashboard, reimbursement templates for the five largest insurers, patient guide generator.
  - Deliberately not: filing claims for patients; clinical records; fee negotiation; any feature that helps professionals coordinate prices (competition-law risk).
- **Why now:**
  - The CNMC was formally asked for help in March 2026 and has not ruled.
  - 2025 rises were marginal: Adeslas went from €18 to €19 on private policies; Asisa +6.5%.
  - The 2025–2027 MUFACE contract raised premiums paid to insurers by 41% while doctors were left out of the negotiation, and doctors in small provinces talk of leaving panels (PRO-01, PRO-02).
- **Alternatives today:**
  - No software for payer-mix analysis or reimbursement was documented.
  - Litigation through Unipromel.
  - Practice software such as Clinni (€12.95/month + taxes) covers booking, reminders and invoicing (PRO-03).
  - Doctoralia sells visibility at unpublished prices (PRO-04).
  - Weakness: none of them address the decision to leave a panel.
- **Price hypothesis:** €9–19/month per professional; member-benefit deals with colegios.
- **Channels:**
  - Colegios and councils: Consejo General de la Psicología and the regional COPs; CGCFE and the physiotherapy colegios; the podiatry, dietetics and speech-therapy colegios.
  - ATA (self-employed association), Unipromel, and the readers of Infocop and Redacción Médica.
  - Searches such as "reembolso seguro médico factura psicólogo".
- **Build notes:**
  - Avoid storing clinical content (health data under GDPR art. 9).
  - Invoices must follow invoicing rules (VeriFactu legally due in 2027; October 2028 announced but not enacted).
  - Each insurer's requirements must be researched.
  - Complexity: low–medium.
- **Moat in an AI-flooded market:** low to moderate. The analytics are easy to copy. Harder to copy: a maintained dataset of what each insurer requires and accepts for reimbursement, and distribution through colegios.
- **Key risks and kill criteria:**
  - Risks: few patients may hold reimbursement-type policies; patients may refuse to pay up front; professionals may fear losing referrals.
  - Kill if reimbursement cover is held by only a small minority of insured patients, or if colegio interviews show members will not leave panels.
- **Evidence strength:** medium. The squeeze is well documented across outlets and reached the CNMC in 2026. But fee figures come mostly from interested parties (Unipromel, ATA), some date from 2020–23, and no source shows demand for this tool.
- **Validation questions:**
  1. What share of Spanish private health policies include reimbursement cover, and what documents do Adeslas, Sanitas, Asisa, DKV and Mapfre require?
  2. Status of the CNMC request (March 2026) and of Unipromel's challenge to the MUFACE contract at the Audiencia Nacional.
  3. Counts of self-employed physiotherapists, podiatrists, dietitians and speech therapists (colegio censuses, RETA).
  4. Interview 15 panel professionals: insurers' share of revenue, € per session, appetite for private-pay.
  5. Do Clinni, Doctoralia/Docplanner, Gesden or Clinic Cloud already offer payer-mix analytics or reimbursement invoices?
  6. Legal and deontological limits on advertising private sessions as reimbursable.

### G4-I06: Staff qualification file for private health centres (RD 239/2026)
- **Type:** C (primary), secondary B
- **Buyer:** owners or managers of authorised private health centres: dental, physiotherapy, psychology, aesthetic, podiatry and nutrition clinics. How many: no national count; validate. Doctoralia alone is present in 5,000 private clinics, which gives a floor (PRO-03, PRO-04).
- **Pains addressed:** PRO-09
- **Problem:** RD 239/2026, in force since 1 July 2026, requires every health centre to keep up-to-date information and a personal file for every health professional (employee, autónomo or partner), showing official qualification and specialty. Centres must also inform new staff about safe practices, and have six months to comply, so until about 1 January 2027 (PRO-09; the date is the researcher's calculation). The duty is new and little noticed, and clinics probably rely on folders and spreadsheets (inference).
- **Product:**
  - Does:
    - a register of professionals per centre (qualification, specialty, colegio and number, type of contract), with document upload;
    - checks of colegiación (registration with the professional college) against public colegio registers where available;
    - reminders for expiring items;
    - a safe-practice onboarding pack with e-acknowledgement;
    - a one-click inspection dossier per centre;
    - rule updates as regions adapt the annexes (due about July 2027), including the rewritten units U.11 (nutrition and dietetics) and U.36 (pain treatment).
  - MVP: register, document vault, PDF dossier, onboarding acknowledgement, email reminders.
  - Deliberately not: payroll, rotas, clinical records, or any claim to certify compliance.
- **Why now:** the deadline of about 1 January 2027 is ten weeks away; regional adaptation follows around July 2027 (PRO-09).
- **Alternatives today:**
  - No dedicated tool found (PRO-09).
  - Generic HR tools charge per employee, with minimums that fit micro clinics poorly (software table):
    - Sesame from €4.75 per employee per month with a 15-employee minimum (about €71/month, my calculation);
    - Factorial Core from 8 USD per user per month, plus modules by quote;
    - Kenjo at €6 per employee.
  - Clinic software such as Clinni (€12.95/month) has no documented credential module.
- **Price hypothesis:** €5/month per centre for up to five professionals, plus €1 per extra professional; or €49 a year.
- **Channels:**
  - Colegios (dentists, physiotherapists, psychologists, podiatrists, dietitians) and clinic associations.
  - Clinic-software vendors (white-label or integration) and gestorías serving clinics.
  - Searches such as "RD 239/2026" and "registro de personal sanitario centro".
  - A free pre-deadline checklist as a lead magnet.
- **Build notes:** personal data, but not health data; access to colegio registers is unverified; 17 regional inspection regimes; no certification needed. Complexity: low.
- **Moat in an AI-flooded market:** none — speed only, to beat the deadline. Colegio distribution and region-by-region inspection know-how add a thin edge, and clinic-software vendors could add the feature quickly.
- **Key risks and kill criteria:**
  - Risks: regions may never inspect the files; a folder may be enough; vendors may bundle the feature free.
  - Kill if regional inspectorates say there is no set format and no check, or if the main clinic-software vendors add it free before January 2027.
- **Evidence strength:** weak. The obligation is official (BOE), but there is no evidence yet on how clinics comply, how inspectors will check, or what clinics would pay.
- **Validation questions:**
  1. Confirm on the BOE the deadline (six months from 1 July 2026) and the scope: all centres authorised under RD 1277/2003, and both existing and new staff.
  2. Ask the inspectorates of Madrid, Catalonia, Andalusia and Valencia how they will check, and whether they will publish a format.
  3. Count authorised private health centres by type (REGCESS and regional registers).
  4. Check Clinni, Doctoralia, Gesden, Clinic Cloud, Flowww and Koibox for staff-credential features.
  5. Do colegios offer online lookups or APIs for colegiación status?
  6. Interview 10 clinic managers about awareness and plans.

### G4-I07: Antibiotic-stewardship and PRESVET compliance file for small vet clinics
- **Type:** C (primary), secondary B
- **Buyer:** companion-animal veterinary clinics (micro and small); the owner vet pays. How many: about 16,460 companion-animal clinicians registered in PRESVET (MAPA, May 2026, search summary). Number of clinics unknown; validate (PRO-05).
- **Pains addressed:** PRO-05
- **Problem:** Since 2 January 2025, every antibiotic prescribed or administered must be reported at least every 15 days (drug, species, quantity, days, share of the pack used), under A–D categories with lab-test (antibiogram) prerequisites, and fines run from €600 to €1.2M. Vets call the platform hard to use and unstable (PRO-05). About 80% of reporting is automated through practice software, so what remains is checking the category rules, keeping evidence for inspections, and RD 767/2025's new duty to document antibiotic-reduction measures.
- **Product:**
  - Does:
    - a prescription rule-checker that flags the category and asks for antibiogram evidence or a justification before saving;
    - an evidence store per prescription;
    - a register of antibiotic-reduction measures, with templates (RD 767/2025);
    - a 15-day monitor that reconciles practice-software exports with PRESVET submissions;
    - simple submission through PRESVET web services for clinics that still type data in by hand.
  - MVP: rule-checker, evidence store, 15-day monitor, reduction-measures template.
  - Deliberately not: full practice management; dispensing workflows (PRO-06 is a regulatory limit); routing prescriptions to pharmacies.
- **Why now:**
  - The PRESVET duty has applied since 2 January 2025. RD 767/2025 (in force since 4 September 2025) kept it and added the reduction-measures duty (PRO-05).
  - A change to the sanctions regime was reported "en trámite" in March 2025; its status is unverified. If it was still pending on 6 October 2026, it lapsed with the dissolution, so the current fines probably stand.
- **Alternatives today:**
  - Practice-software integrations through web services (vendors such as Qvet are named but not verified; no prices).
  - Manual entry on the PRESVET website (PRO-05).
  - Weakness: it is unknown whether integrations check categories or keep audit evidence.
- **Price hypothesis:** €9–15/month per clinic.
- **Channels:**
  - The Organización Colegial Veterinaria (OCV) and provincial colegios (Colvet's journal; COVIB in Baleares).
  - Veterinary distributors and the diagnostic labs that run antibiograms.
  - Practice-software vendors as integration partners.
  - Searches such as "PRESVET" and "categorías antibióticos veterinaria".
- **Build notes:**
  - Third-party access to PRESVET web services (validate).
  - Category rules from RD 666/2023 and EU Regulation 2019/6 (validate the exact logic).
  - Owners' personal data.
  - No medical-device claim.
  - Complexity: medium.
- **Moat in an AI-flooded market:** moderate. Rule logic, a working PRESVET integration and colegio distribution are harder to copy. But practice-software vendors could add rule-checks, and the market is small.
- **Key risks and kill criteria:**
  - Risks: a small market; little remaining pain if integrations already work; few inspections.
  - Kill if the leading practice-software products already check categories and keep evidence, or if colegios report no inspections or fines since 2025.
- **Evidence strength:** medium. The burden is well documented (official texts, colegio statements, national protests of 2,000 to 5,000 vets depending on the source). But the remaining gap for software is unclear, and the MAPA figures come from a search summary.
- **Validation questions:**
  1. Confirm the MAPA figures: 16,460 clinicians; does "80% automated" refer to clinicians or to prescriptions?
  2. Is there a public PRESVET web-service specification for third-party software, and what does onboarding require?
  3. Which practice-software vendors integrate with PRESVET (Qvet and others), at what price, and do they check categories and antibiograms?
  4. Was the sanctions reform passed, or did it lapse with the dissolution? Any inspections or fines in 2025–26?
  5. What format and frequency does RD 767/2025 set for documenting antibiotic-reduction measures?
  6. Number of companion-animal clinics in Spain (OCV census).

### G4-I08: Client compliance cockpit for gestorías (VeriFactu and B2B e-invoicing)
- **Type:** B (primary), secondary C (rules update themselves; clients are notified automatically)
- **Buyer:** gestorías and asesorías (micro and small); a partner or the office manager. How many: unknown; validate. Together they serve more than 3 million SMEs and autónomos (PRO-10).
- **Pains addressed:** PRO-11, PRO-10
- **Problem:** Gestorías prepared clients for VeriFactu in 2025 and then had to re-plan twice. The legal dates are 1 January and 1 July 2027, a move to October 2028 was announced on 5 October 2026 without a legal instrument, and B2B e-invoicing is now fixed for 6 October 2027 (turnover above €8M) and 6 October 2028 (everyone else) (PRO-11). Clients keep asking "¿me afecta y cuándo?" while 7 in 10 firms struggle to hire, so every re-planning round eats scarce staff time (PRO-10).
- **Product:**
  - Does:
    - imports the client list (CSV, or exports from a3 or Sage);
    - records per client the tax regime (corporate tax or IRPF), turnover band, territory (common or foral: TicketBAI, Navarra), current invoicing software and its declared compliance;
    - computes each client's deadlines and readiness;
    - updates the rules when the BOE changes;
    - sends personalised notices by email or WhatsApp, in Spanish, Catalan or Basque;
    - tracks answers and lists clients at risk.
  - MVP: CSV import, rule engine for the current calendar, personalised notices, status tracker.
  - Deliberately not: invoicing software, tax filing, bookkeeping.
- **Why now:**
  - Orden HAC/1028/2026 (BOE 5 October 2026) started the e-invoicing countdown.
  - The VeriFactu postponement is announced but not law, and the Cortes are dissolved (elections on 29 November 2026).
  - Draft dates for the public e-invoicing solution (1 August 2027) and for payment-status reporting by firms up to €8M (1 October 2029) may still move (PRO-11).
  - The idea gains value from this uncertainty. But its VeriFactu part rests on a postponed rule whose final dates are not settled, and that risk travels with it.
- **Alternatives today:**
  - Client-side tools (software table): AEAT VERI*FACTU app (free); FacturaScripts (free); Billin (free to €20); Contasimple (free to €15.95); a3factura (from €9.95); Holded (€7.50–99.50 on annual billing, about double if billed monthly); Quipu (€17–59); Sage Active (from €25); Sage 50 (from €45); A3ERP (about €600 a year).
  - Gestoría automation such as Copilot Gestoría, a3, Sage and ContaPlus. No prices (PRO-10).
  - Weakness: each vendor sees only its own product, while one gestoría's clients use many (inference). The gestor's software choice already weighs heavily ("opción obligada" for a3, software table).
- **Price hypothesis:** €29–79/month per gestoría by number of clients (e.g., tiers at up to 100, 300 or 1,000).
- **Channels:**
  - The Consejo General de Gestores Administrativos and the colegios de gestores.
  - Asesores' associations and accounting-software partner programmes.
  - Webinars on the 2027–2028 calendar.
  - Searches such as "aplazamiento VeriFactu 2028 gestoría".
- **Build notes:**
  - A rule engine covering the state and foral systems.
  - A source for each product's compliance declaration (validate).
  - Client data under a processor agreement (GDPR).
  - Integrations with a3 and Sage exports.
  - Complexity: low–medium.
- **Moat in an AI-flooded market:** moderate. Big vendors could build it, but they are tied to their own products. Harder to copy:
  - a vendor-neutral position;
  - know-how in keeping rules current;
  - a maintained database of which invoicing products are compliant;
  - distribution through gestores' bodies.
- **Key risks and kill criteria:**
  - Risks: gestorías may not pay for "information"; vendors may give dashboards away; the rules may settle.
  - Kill if gestorías say a spreadsheet handles it in a couple of hours per change, or if a3 or Sage already show cross-vendor readiness for all clients.
- **Evidence strength:** medium. The regulatory churn is very well documented (law firms, the Consejo de Gestores, AEAT). The staff shortage comes from interested parties, and the hours spent were never measured.
- **Validation questions:**
  1. Has the move of VeriFactu to October 2028 been published in the BOE since 5 October 2026? Which instrument can enact it while the Cortes are dissolved?
  2. Number of gestorías and asesorías (Consejo General de Gestores; INE CNAE 69.20).
  3. Interview 10 gestorías on hours spent communicating VeriFactu and e-invoicing to clients, and on how they track clients' software.
  4. Check a3 (Wolters Kluwer), Sage Despachos, TeamSystem and Copilot Gestoría for client-readiness dashboards and their prices.
  5. Is there an official list of software with a VeriFactu declaración responsable (self-certification) that could feed the database?
  6. Compare with tax-track ideas built on TAX-01, TAX-02, TAX-04 and TAX-05, and merge.

### G4-I09: MASC pre-litigation workflow and evidence bundle
- **Type:** B
- **Buyer:**
  - Small law firms and autónomo lawyers in civil and commercial work.
  - Administradores de fincas and landlords in eviction cases.
  - SMEs chasing unpaid invoices, as a later segment (FIN-06).
  - How many: unknown; validate. Demand proxy: 3,563,038 new civil cases in 2024 (PRO-12).
- **Pains addressed:** PRO-12
- **Problem:** Since 3 April 2025, most civil and commercial claims must attach proof of a prior negotiation attempt (a MASC), "so pena de inadmisión": proof that the other party received the invitation, when, and could read it. Refusing to negotiate can make a party pay the costs (PRO-12). Courts apply the rule unevenly (Las Palmas rejects claims that ignore it; Collado Villalba excludes some procedures), and case law requires proving that the address belongs to the defendant.
- **Product:**
  - Does: a guided workflow per case:
    - choose the method;
    - generate the invitation from templates by claim type (unpaid invoice, eviction, community arrears, consumer claim);
    - send it by certified email or SMS, or by burofax through a partner, and capture evidence of delivery and access;
    - work through a checklist to prove the address belongs to the counterparty;
    - run a deadline timer, and log offers and replies;
    - at the end, generate the claim paragraph describing the MASC, plus an indexed evidence bundle.
  - It also keeps a library of criteria by court district, seeded with published criteria and grown from users.
  - MVP: templates, one certified-delivery integration, evidence bundle, claim paragraph, criteria library.
  - Deliberately not: legal advice to non-lawyers on the merits; filing through LexNET; acting as mediator.
- **Why now:**
  - The requirement has applied since 3 April 2025, without uniform criteria.
  - 2025 case law tightened what counts as proof of address.
  - Civil filings rose about 20% in 2024, and court mediation was negligible before the reform (647 referrals, 70 agreements) (PRO-12).
- **Alternatives today:**
  - Burofax and certified-email services (no prices in the notes), mediators, lawyers' own templates.
  - Practice software with LexNET, such as MN Program (from €1 a day) and SuDespacho (from €35.95/month), as reported by a vendor blog. Kmaleon, Aranzadi Fusión and Tirant publish no prices (PRO-12).
  - E-signature for a document signed by both parties, e.g., Signaturit Business at €35 per user per month on annual billing, with 5 envelopes (software table).
  - Weakness: no MASC-specific workflow appears in the notes.
- **Price hypothesis:** €19–39/month per lawyer, or €9–15 per MASC case for landlords and administradores.
- **Channels:**
  - Colegios de abogados (e.g., ICAM, the Madrid bar).
  - Colegios de administradores de fincas (CAF Madrid has published MASC guidance) and procuradores' colegios.
  - Integrations with practice software.
  - Legal-subscription providers (Legálitas plans at €16.92–45.50/month on promo pages, software table).
  - Searches such as "requisito de procedibilidad MASC modelo" and "burofax MASC".
- **Build notes:**
  - Qualified trust service providers for certified delivery under eIDAS (validate which).
  - Evidence integrity (hashes, timestamps).
  - Confidentiality of negotiation content.
  - Lawyering is a reserved profession: when selling to non-lawyers, the product must stay a document tool, not advice.
  - Complexity: medium.
- **Moat in an AI-flooded market:** moderate. Templates alone are easy to copy. Harder to copy: a court-criteria database that grows with use, certified-delivery integrations and colegio partnerships.
- **Key risks and kill criteria:**
  - Risks:
    - practice-software vendors may add a MASC module;
    - the new Cortes after 29 November 2026 may amend LO 1/2025;
    - lawyers may be content with burofax and Word.
  - Kill if MASC-related inadmissions turn out to be rare and interviews show no time saved.
- **Evidence strength:** strong. A national rule in force, its proof standard, divergent court criteria and case law are all documented; only inadmission numbers and time costs are missing.
- **Validation questions:**
  1. Find statistics on MASC-related inadmissions and on civil filings since April 2025 (CGPJ 2025–26).
  2. Collect published MASC criteria for the courts of Madrid, Barcelona, Valencia, Sevilla, Málaga, Zaragoza and Bilbao.
  3. Look up existing MASC tools and prices: legal-tech startups; certified-delivery providers (Correos online burofax, Logalty, eGarante; not in the notes); MASC modules in MN Program, SuDespacho and Aranzadi Fusión.
  4. Legal: can landlords or administradores run a direct-negotiation MASC with the tool without a lawyer, and what do eviction claims require?
  5. Check for any pending bill to amend LO 1/2025 (it would have lapsed with the dissolution).
  6. Interview 10 small firms and 5 administradores de fincas on time spent per MASC and how they prove address ownership.
  7. Merge with ideas from LEG-01, FIN-06, CON-20 and CON-23.

### G4-I10: Exam-readiness tracker and slot planner for driving schools
- **Type:** B
- **Buyer:** driving schools (autoescuelas), mostly micro and small, plus chains such as Autoescuela Lara (65 centres in Madrid); the owner or manager pays. How many: unknown; validate. Activity proxy: more than 1 million practical tests a year (PRO-14).
- **Pains addressed:** PRO-14
- **Problem:** The DGT rations practical-exam slots through its CAPA allocation, which splits each office's capacity according to schools' theory pass rates and candidate numbers. Examiners do 12 tests a day, 46% of students fail their first practical, and waits run 1.5–5 months in Madrid (PRO-14). When the DGT offered unlimited extra exams in 2026 pilots, schools presented under 10% of the students they had claimed, and the DGT says only 8% are ready, so readiness is a binding constraint alongside slots.
- **Product:**
  - Does:
    - an instructor app to score each practical lesson against a rubric based on the DGT's exam criteria;
    - a readiness score and pass estimate per student;
    - a dashboard to choose whom to present, so pass rates and slots are protected;
    - scheduling of lessons, cars and instructors;
    - automatic updates to waiting students;
    - an exportable list of ready students for DGT reinforcement sessions.
  - MVP: rubric app, readiness dashboard, student messaging.
  - Deliberately not: theory-test training; booking DGT slots (there is no API); payments; fleet management.
- **Why now:**
  - Protests in 2026, at every DGT office in Andalusia on 17 July.
  - The DGT's reinforcement plan is being extended (Barcelona from 13 June 2026, Tenerife from late June), while the DGT publicly blames unready students.
  - 130 new examiner posts (PRO-14).
- **Alternatives today:**
  - Driving-school management software was not researched; no names or prices in the notes.
  - Paper lesson records (inference).
  - Saturday reinforcement sessions, and sending students to smaller exam centres (PRO-14).
- **Price hypothesis:** €29–59/month per school, plus €5 per instructor.
- **Channels:**
  - CNAE (the national driving-schools confederation) and provincial associations (e.g., the Sevilla schools that protested).
  - Driving-school software vendors and instructor-training centres.
  - Searches such as "software gestión autoescuela" and "CAPA DGT".
- **Build notes:** the DGT's assessment criteria (check they are public); students' personal data (GDPR); no DGT API; start rule-based, and add predictions once outcome data exist. Complexity: low–medium.
- **Moat in an AI-flooded market:** moderate if outcome data (lesson scores matched to exam results) accumulate across schools; otherwise copyable. Distribution through associations helps.
- **Key risks and kill criteria:**
  - Risks:
    - schools earn money from extra lessons, so faster readiness may not suit them;
    - CAPA rules may be opaque or may change;
    - incumbent software may already do this.
  - Kill if schools say readiness is not their problem, or if CAPA turns out not to reward pass rates.
- **Evidence strength:** medium. The bottleneck is documented by the DGT, the press and protests, but its size is disputed (sector versus DGT), and demand for readiness software is an inference.
- **Validation questions:**
  1. Number of driving schools by province (DGT registry, CNAE).
  2. The current CAPA formula: does a higher pass rate raise a school's allocation?
  3. Driving-school software vendors and prices in Spain.
  4. Are the DGT's practical-exam assessment criteria public and usable for a rubric?
  5. Interview 10 schools in Sevilla, Madrid, Barcelona and Valencia on how they choose whom to present, and on willingness to pay.
  6. What readiness evidence or lists does the DGT ask schools for in reinforcement sessions?

### G4-I11: Route planning, visit verification and hours reporting for home-help (SAD) providers
- **Type:** B
- **Buyer:** home-help (servicio de ayuda a domicilio, SAD) companies, from small regional operators to large groups, plus not-for-profits; the operations or coordination manager pays. How many: unknown; validate.
- **Pains addressed:** PRO-17
- **Problem:** Municipal SAD tenders cap the hourly price and fold travel, coordination, supervision and training into it, while wage rises under collective agreements push costs up. In Vigo the price rose from €16.70 to €22 an hour because of wages, in a €49.5M three-year contract (PRO-17). Unpaid travel between homes and admin time come straight out of the margin, and at least 50% of SAD contracts must be full-time under the 2022 accreditation agreement.
- **Product:**
  - Does:
    - daily route planning for carers within visit windows;
    - mobile check-in and check-out for visit verification;
    - monthly hours reports in each council's format;
    - a rota builder that checks the full-time share.
  - MVP: route optimiser, check-in app, hours export.
  - Deliberately not: care plans or clinical notes; payroll; tender writing.
- **Why now:** tenders are being re-priced for wage rises (Vigo, 2025). The accreditation targets run to 2029, and their regional transposition is unverified (PRO-16, PRO-17).
- **Alternatives today:** scheduling and route software was not researched; no names or prices in the notes. Providers re-tender at higher prices and lobby the regions (PRO-17).
- **Price hypothesis:** €3–6 per carer per month, or €99–299/month per company.
- **Channels:**
  - SAD employers' associations (names to find).
  - Councils' social services, via tender clauses on verification systems.
  - Regional dependency agencies.
  - Searches such as "software servicio de ayuda a domicilio".
- **Build notes:**
  - Routing APIs.
  - Tracking workers' location raises labour-law and privacy issues (works councils; see LAB-01).
  - Data on dependent people is health-adjacent (GDPR art. 9).
  - Council formats differ.
  - Complexity: medium.
- **Moat in an AI-flooded market:** moderate. Routing itself is a commodity; integrations with council formats and know-how of tender requirements are harder to copy.
- **Key risks and kill criteria:**
  - Risks: large operators already have systems and small ones may not pay; unions may resist tracking; councils may impose their own apps.
  - Kill if tenders mandate systems supplied by the council, or if specialised SAD software already does this cheaply.
- **Evidence strength:** weak. The price squeeze rests on a handful of tenders (some from 2020–23) and one summary of a TED notice. There is no data on the number of providers or on their software use.
- **Validation questions:**
  1. Number of SAD providers and SAD hours in Spain (IMSERSO and dependency statistics).
  2. Do SAD tenders in Madrid, Barcelona, Valencia and Sevilla require visit verification or specific reporting formats?
  3. Existing SAD software vendors and their prices.
  4. Share of carers' paid time lost to travel (sector or union studies).
  5. Labour-law limits on location-based check-in (cross-check LAB-01).
  6. Interview five small SAD operators.

### G4-I12: Household-employer autopilot for domestic and care workers
- **Type:** C (primary), secondary B (no all-in-one tool found; the free government tool covers one step)
- **Buyer:** households that employ domestic or care workers (B2C), and the gestorías that run their payroll (B2B2C). How many: about 348,000 (INSST, May 2025) to more than 378,000 (El Español, May 2026) registered workers, and roughly as many employing households. The EPA labour-force survey counts about 540,000 workers (PRO-18).
- **Pains addressed:** PRO-18
- **Problem:** Each employing household had to complete the Prevencion10 risk assessment by 14 November 2025, put measures in place, inform the worker and keep the signed plan for inspectors. That sits on top of Social Security registration, monthly contributions (including unemployment since 2022) and pay updates as the minimum wage rises (+61% since 2018, per AESPD) (PRO-18). The free tool covers only the assessment and collapsed at launch, and the promised guide, harassment protocol and training platform were still pending in May 2026.
- **Product:**
  - Does:
    - a set-up wizard (contract type, hours, pay against the minimum wage, live-in or not) with a contract template;
    - monthly payslips;
    - a contribution calendar and estimate;
    - alerts and recalculation when the minimum wage changes;
    - storage of the Prevencion10 output, with reminders to redo it when conditions change;
    - a simple time record, if one is required;
    - a document vault for inspections;
    - a year-end summary.
  - MVP: wizard, payslips, minimum-wage alerts, vault, reminders.
  - Deliberately not: filing with Social Security for the household (except through a partner gestoría); recruiting or matching workers; legal advice on dismissals.
- **Why now:**
  - RD 893/2024 duties have been enforceable since the November 2025 deadline.
  - More pieces are pending (guide, harassment protocol, training platform).
  - Unions asked inspectors not to be punitive "at first", which suggests enforcement could tighten (my inference; PRO-18).
- **Alternatives today:**
  - Prevencion10: free, but covers the assessment only.
  - Gestorías and advisers (Dancausas Asesores is quoted). No prices.
  - Household-payroll platforms were not researched (PRO-18).
  - A price signal from the software table: Declarando, an autónomo platform, was criticised for an undisclosed "60 € + IVA por cada alta de trabajador" (€60 + IVA for each worker registered).
- **Price hypothesis:** €5/month or €49 a year per household; €1–2 per household per month as a white-label for gestorías.
- **Channels:**
  - Search: "contrato empleada de hogar", "nómina empleada de hogar", "Prevencion10".
  - Home-care agencies and elder-care communities.
  - Gestorías (white-label), home insurers and banks.
  - AESPD.
- **Build notes:**
  - Yearly minimum-wage and contribution tables (auto-update).
  - Social Security rules for the special domestic-worker scheme, and the authorisations needed to act for households (validate).
  - Workers' personal data, possibly including immigration status.
  - Limits on who may represent employers (validate).
  - Complexity: low–medium.
- **Moat in an AI-flooded market:** low. The software is easy to copy. The edges are search ranking and trust, automatic updates, the gestoría channel and, if allowed, a direct Social Security integration.
- **Key risks and kill criteria:**
  - Risks:
    - low willingness to pay;
    - churn when the worker leaves;
    - a large informal segment (about 540,000 in the EPA against about 378,000 registered);
    - Social Security already calculates contributions;
    - enforcement may stay light.
  - Kill if free tools dominate, or if fewer than about 1 in 10 surveyed employing households would pay €5/month.
- **Evidence strength:** strong. An official INSST release and two independent press sources document the duties, the market size and the tool's failures. Willingness to pay is untested.
- **Validation questions:**
  1. Existing domestic-employer apps and agencies in Spain, and their prices.
  2. Must households keep working-time records for domestic workers today (cross-check LAB-01)?
  3. Labour-inspection actions and fines under RD 893/2024 since November 2025.
  4. Status of the pending guide, harassment protocol and training platform.
  5. Can a third-party app register workers and manage contributions on a household's behalf (Social Security authorisations)?
  6. Survey about 200 employing households on what they pay a gestoría today, and on willingness to pay €5/month.

---

## 5. Cross-group links
Overlaps were found by keyword checks of the other Stage 1 files. Entry IDs are given so the merge stage can combine them.

| G4 item | Overlapping entries (file) | Overlap | Merge note |
|---|---|---|---|
| G4-I09 / PRO-12 | LEG-01, LEG-04 (`legal_disputes_compliance.md`); FIN-06 (`cashflow_finance_insolvency.md`); CON-20, CON-23 (`construction_realestate.md`) | The same MASC requirement, seen by lawyers, creditors chasing unpaid invoices, landlords (evictions) and property managers (community arrears) | Merge into one MASC product with templates per segment; pool the evidence on inadmissions and costs |
| G4-I03 / RET-15, RET-16 | IND-12 (`transport_industry_agrifood.md`) | The same RD 1055/2022 and PPWR duties, for manufacturers and food and drink SMEs. IND-12 adds the Dec 2025 Omnibus proposal on the authorised-representative duty | Merge; IND-12 widens the buyer pool. IND-12 says the plastic tax overlaps the tax researcher, but a keyword check of `tax_invoicing_accounting.md` found no plastic-tax entry, so RET-16 may be the only Stage 1 entry on it |
| G4-I08 / PRO-10, PRO-11 | TAX-01, TAX-02, TAX-04, TAX-05, TAX-06, TAX-08 (`tax_invoicing_accounting.md`); FIN-25 (`cashflow_finance_insolvency.md`); VOX-12, VOX-21 (`voice_of_smes_software_market.md`) | VeriFactu whiplash; B2B e-invoicing and payment-status reporting; the gestor choosing clients' software | Merge with any tax-track idea for gestorías or readiness; G4-I08 is the vendor-neutral, gestoría-side variant |
| G4-I04 / RET-19 | HOS-02, HOS-10 (`hospitality_tourism.md`); TAX-01; VOX-09, VOX-10, VOX-11 | Card guarantees against no-shows in restaurants; a fragmented tech stack under fiscal deadlines; VeriFactu forcing software changes; hard cancellation, data held at exit and support gaps as reasons to switch | One deposit and reminder engine could serve salons, clinics and restaurants. The voice-track complaints support the switching story |
| G4-I01 / RET-04 | LEG-06 (legal); `cities_macro_surveys.md` (note on Barcelona petty theft) | CCTV rules constrain evidence packs. The cities track could not verify the multirreincidencia reform and suggested it might lapse, which conflicts with RET-04's BOE citation | Resolve in favour of the BOE text after a re-check; take the CCTV rules from LEG-06 |
| G4-I12 / PRO-18 | LAB-01, LAB-03, LAB-20, LAB-24 (`labor_hr_litigation.md`) | Time-recording limbo; minimum-wage rises (LAB-03 names domestic employers); occupational-risk duties; payroll software that fits micro employers poorly | Share the rule engines (minimum wage, time records); the gestoría white-label channel is shared with G4-I08 |
| G4-I11 / PRO-17 | LAB-01 | Time recording and location-based check-in for carers | Check the labour-law constraints there |
| G4-I10 / PRO-14 | ADM-09 (`bureaucracy_licensing_funds.md`) | Scarce DGT appointments for driving schools | Combine the evidence on DGT friction |
| G4-I02 / RET-11 | LEG-12 (legal) | Ley 10/2025 consumer-law duties may govern return fees and refunds | Use LEG-12 for the legal validation |
| RET-05 (filtered N7) | FIN-13 (`cashflow_finance_insolvency.md`); VOX-07 | Card and POS fees | Merge RET-05's evidence into FIN-13 |
| RET-17 (filtered N7) | LEG-16 (legal) | EAA web accessibility | Merge into LEG-16 |
| RET-07 (filtered N1) | ADM-12, ADM-13 (bureaucracy); VOX-15, VOX-16 (voice) | Kit Digital aftermath and low-quality subsidised websites | Build any website or Kit Digital idea there |
| PRO-08 (filtered N1) | LEG-05, LEG-08, LEG-09 (legal); VOX-04 (voice) | Data-protection exposure; breaches at booking-software vendors | A build constraint for the G4 clinic and salon ideas; a data-protection product belongs to the legal track |
| Reviews and reputation (no G4 entry) | VOX-01, VOX-02 (voice); HOS-07 (hospitality); LEG-14 (legal) | Salons and clinics depend on reviews and directories | A review-management idea from those tracks could bundle with G4-I04 |
| RET-14 (filtered N1) | Canarias tax regime (IGIC/AIEM), mentioned in several other tracks | Distance sales to the islands | Look for fresher evidence during the merge |

---

## 6. Group top 5
Listed in ID order, not ranked; ranking happens after validation.

1. **G4-I01, shop theft incident log.** A €2.8bn problem (1.1% of turnover), and a law in force since April 2026 that rewards systematic reporting. No comparable tool was found, and associations and councils give a route to market. Demand is still an inference.
2. **G4-I03, packaging EPR/PPWR/plastic-tax kit.** In force, recurring (31 March) and data-heavy, with a new PPWR layer since August 2026. Regulatory know-how and supplier data make it harder to copy than most. Merge with IND-12.
3. **G4-I08, gestoría compliance cockpit.** The best-documented regulatory-churn story in the group. One gestoría sale reaches many SMEs, and the vendor-neutral position is defensible. Merge with the tax track.
4. **G4-I09, MASC workflow.** A national rule in force, with a documentary burden and inadmission risk, across about 3.56M civil cases a year. A court-criteria database gives a real moat. Merge with the legal, cashflow and real-estate tracks.
5. **G4-I12, household-employer autopilot.** About 350,000–380,000 employing households with recurring official duties, and a free government tool that covers only one step. A natural €5/month product, though willingness to pay is untested.

Runner-up: **G4-I06 (RD 239/2026 staff file).** The fastest to ship against a hard deadline (about 1 January 2027), but it has no moat and no evidence of enforcement.
