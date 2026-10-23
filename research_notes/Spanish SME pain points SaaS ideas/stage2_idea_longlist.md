# Stage 2 merged idea longlist and validation plan

*Prepared 23 October 2026 (merge step of Stage 2).*

*Inputs, and nothing else:*
- *`stage2_idea_index.md` (75 candidate ideas);*
- *`stage2_noise_log_combined.md` (194 filtered pains);*
- *the six group files: `stage2_G1_money_tax_software.md`, `stage2_G2_labour_legal_admin.md`, `stage2_G3_property_hospitality.md`, `stage2_G4_retail_services.md`, `stage2_G5_mobility_industry_cities.md`, `stage2_G6_expat_startups_gaming.md`;*
- *`00_user_supplied_ideas.md` (U1–U5).*

*Method and conventions:*
- *No web searches or page fetches were made. Every fact comes from the files above; pain IDs (FIN-06, LEG-01 and so on) are the citations.*
- *Pointers have the form `file:line` and lead to the full source block (problem, MVP, alternatives, channels, build notes, risks, validation questions). Validators should read those blocks; this file does not repeat them.*
- *Prices are hypotheses from the group files, in € excluding VAT. They are not facts.*
- *Evidence tags only allocate validation effort. Where a group file splits its tag (for example "strong for the problem, weak for willingness to pay"), the headline tag is the problem-side one and the weaker part is noted.*
- *This is a longlist, not a ranking. No idea is kept, ranked or dropped until it has been searched and analysed from every angle in section 6.*
- *Short codes in tables: G1 = `stage2_G1_money_tax_software.md`, G2 = `stage2_G2_labour_legal_admin.md`, G3 = `stage2_G3_property_hospitality.md`, G4 = `stage2_G4_retail_services.md`, G5 = `stage2_G5_mobility_industry_cities.md`, G6 = `stage2_G6_expat_startups_gaming.md`.*

---

## 1. Summary

### 1.1 Pain points

- **Reviewed:** 395 pain entries from 17 Stage 1 tracks: G1 72, G2 66, G3 76, G4 40, G5 71, G6 70. The groups also assessed the five user ideas and the 18 sub-claims of the user's regional table.
- **Carried forward:** 201 (G1 42, G2 37, G3 39, G4 15, G5 33, G6 35), grouped into 72 clusters (12, 16, 11, 12, 9 and 12).
- **Filtered:** 194, by reason code:
  - N1, weak evidence: 49;
  - N2, not software-solvable: 61, the largest group;
  - N3, regulation postponed, annulled, draft or lapse-prone: 14;
  - N4, already solved cheaply or saturated: 25;
  - N5, too niche or too small: 14;
  - N6, legally risky to automate: 4 (for example appointment-booking bots, ADM-09);
  - N7, duplicate: 27. Their evidence was folded into the surviving cluster, so it is still used.
- **Tracks with the most filtered entries:** CITY 21, RET 17, HOS 16, FIN 15, STA 15, CON 14 and GAM 14.
- **What N2 removed:** many of the loudest pains are market or policy forces, not software problems: energy costs, staff shortages, housing supply, Temu and Shein, frozen insurer fees.
  - G5's macro weighting (`stage2_G5_mobility_industry_cities.md:40`) shows the trade-off. Energy limits 63.2% of firms (Banco de España EBAE, Q3 2026), but software has little leverage over it.
  - Uncertainty and regulation limit 57.6% and are rising, and they are where software has the most leverage.
  - G5 therefore advises boosting compliance ideas tied to rules in force, and discounting ideas that rest on drafts or bills.

### 1.2 Ideas

- **Before merging:** 75 candidates (G1 14, G2 15, G3 11, G4 12, G5 9, G6 14). By primary type: A 7, B 42, C 26.
- **After merging: 64.** Eight merges fold 19 source ideas into 8 (section 2.0). Several other overlapping pairs were checked against the full text and kept apart, and section 2.0 gives the reason for each.
- **By primary type after merging:**
  - A (cheaper alternative): 6;
  - B (new product): 36, including one game and one gaming platform;
  - C (low-touch subscription of about €5/month): 22.

  Secondary types are given per idea and in the index in section 4.
- **Evidence tags after merging:** strong 14, medium 45, weak 5.
- **User ideas:** all five were reshaped, and none survives as given. LigaHub (U5) in its original form is flagged for likely discard.
- **Copyability:** every source idea carries a "moat in an AI-flooded market" note, and 21 of the 75 say the moat is "none", usually "speed only". Section 6 adds a defensibility check (angle g) for each idea.

### 1.3 Strongest themes

1. **Rules already in force that create a recurring, documentable step with live enforcement.** These rules are the least exposed to the 29 Nov 2026 election. Examples:
   - MASC, the mandatory pre-litigation negotiation step, in force since 3 Apr 2025: 179,846 monitorios in Q2 2026, and 49.3% of surveyed Madrid lawyers had trouble proving the attempt (FIN-06, LEG-01).
   - Electronic notifications deemed delivered after 10 days, for about 1.45M legal entities (ADM-08).
   - The DeCA road-freight document since 5 Oct 2026, with €401–600 roadside fines (IND-01).
   - Food-contract registration in the RCA: 506 of the 991 AICA sanctions in 2025 were failures to register (IND-18).
   - RD 723/2026 hiring statements (LAB-15), packaging declarations and the EU packaging regulation (PPWR) since 12 Aug 2026 (RET-15, IND-12), and the Ley 10/2025 complaint clocks (LEG-12).
2. **The 2027–2029 tax-tech wave, and the gestorías that gatekeep it.**
   - VeriFactu is due on 1 Jan and 1 Jul 2027 under the BOE text. The move to October 2028 was announced but was not in the BOE as of 21 Oct 2026 (TAX-02).
   - B2B e-invoicing with payment-status reporting starts on 6 Oct 2027, 2028 and 2029 under Orden HAC/1028/2026 (TAX-05, TAX-06).
   - Gestores choose their clients' software (VOX-21) and are short of staff (PRO-10). That makes them a buyer and a channel for most of the money, tax and labour ideas.
3. **Money the law already grants but owners leave on the table.**
   - About 9 in 10 suppliers never claim statutory interest and the €40 per invoice (FIN-03).
   - Hauliers absorb the fuel-revision line even though the G index rose 44.6% (IND-02), and lose detention pay (IND-06).
   - Loss-making startups drop R&D credits they could cash in (STA-05).
   - Regularisation bills surprise autónomos: 35.1% paid after regularisation (TAX-12).
4. **Rules versioned by date and jurisdiction, the most frequent moat claim.**
   - Rentals under RDL 29/2026 (vote around 12 Nov 2026) and Catalonia's Llei 11/2025 (HOU-01, HOU-02).
   - Regional tourist-rental codes (HOS-19, HOS-24) and Basque and Catalan tourist taxes (HOS-15).
   - About 150 obliged ZBE municipalities, served by a stale national feed (ZBE-01, ZBE-03).
   - Provincial convenios (LAB-21) and at least 20 immigration rule changes in 17 months (EXP-06).
   - The group files agree that AI lowers the cost of a first scrape but not of keeping a dated, legally checked dataset current.
5. **The 2027 immigration renewal wave.**
   - The 2026 regularisation drew 1,174,978 applications, and its permits last one year (EXP-03).
   - Filing is reserved to habilitated professionals (EXP-22), and appointment bots are prosecuted (ADM-09, EXP-02).
   - So the buyers are filers, employers and HR teams, not applicants.
6. **Distribution decides more than features.** The edges that recur across groups are:
   - intermediaries: gestorías, colegios, trade associations, installers, invoicing and POS marketplaces;
   - integrations with official systems: DEHú, RCA, PRESVET, SPFE;
   - outcome datasets that grow with use: court acceptance of MASC files, office queue times, shipper payment behaviour.
7. **Political timing is the main cross-cutting risk.**
   - The Cortes were dissolved on 6 Oct 2026, elections are on 29 Nov 2026 and the new chambers meet on 23 Dec 2026.
   - Three decree-laws failed convalidation in 2026.
   - RDL 29/2026 faces a Diputación Permanente vote around 12 Nov 2026 (single source, forecast 35–34).
   - Drafts such as the digital time-recording decree, and pending bills, may lapse.
   - EU regulations, laws already in force and municipal ordinances are unaffected (G5 macro weighting, rule 4).
8. **The user's ideas point at real markets but mostly at the wrong product, buyer or price.**
   - U1 (ColivEs) and U3 (EcoRoute) keep their markets but change the product.
   - U2 (PermisoFast) changes the buyer.
   - U4 (Fandango Arena) changes the price, to €8.99 against the claimed ~$30.
   - U5 (LigaHub) is legally unworkable as specified: a real-money transfer market needs a gambling licence (GAM-21).

---

## 2. Merged longlist

Ideas are ordered by theme, not by rank. Each entry gives the essentials only; the full source blocks are at the pointers. "[user idea U#]" marks the user's own ideas, which get the same validation as every other idea (section 6).

### 2.0 Merge decisions

**Merged: 8 new ideas from 19 source ideas**

| New ID | Source ideas | Why they are one idea |
|---|---|---|
| IDEA-01 | G1-I01, G2-I02, G3-I03, G4-I09 | **Rule:** all four serve the same mandatory step, the MASC pre-litigation negotiation under LO 1/2025.<br>**Engine:** the same one: template, certified send, timers, court-ready pack.<br>**Difference:** only the claimant segment: B2B creditors, any SME claimant, landlords and owners' communities, law firms.<br>**Source view:** all four groups' cross-link sections ask for one MASC product. |
| IDEA-06 | G1-I06, G4-I08, G2-I15 | **Buyer:** the same (gestorías, asesorías and graduados sociales).<br>**Mechanism:** the same: client list, per-client tags, rules mapped to clients, at-risk list, bulk notices, rule-status feed.<br>**Difference:** tax and e-invoicing coverage against labour and administrative coverage, which become modules.<br>**Source view:** G4-I08 asks to merge with the tax-track idea, and G2 proposes one obligation radar across domains. |
| IDEA-07 | G1-I08, G2-I01 | **What they do:** both watch the DEHú, AEAT and TGSS mailboxes and raise the alarm before a notice is deemed delivered on day 10.<br>**Shared risk:** the same access problem (no lawful route without holding certificates) and the same kill criterion. |
| IDEA-09 | G1-I07, G2-I13 | **What they do:** the same contribution-band forecaster and regularisation alarm for autónomos.<br>**Source view:** G2-I13's own validation questions ask for this merge. |
| IDEA-20 | G2-I07, G3-I06 | **What they do:** both run complaint-response clocks for B2C businesses: the national 15-day rule (Ley 10/2025) and Andalusia's Hoj@ rule of 10 calendar plus 10 working days.<br>**Source view:** G2 asks to check Hoj@ before building, and G3 says Hoj@ works best inside a broader consumer-compliance kit. |
| IDEA-47 | G5-I03, G5-I04 | **What they do:** both answer "can vehicle X serve stop Y at time T?" and keep a permit and quota ledger, on the same rules engine.<br>**Difference:** only fleet size: 1–5 vans against 3–50 vans. |
| IDEA-49 | G4-I03, G5-I07 | **Duties:** the same, RD 1055/2022 and the PPWR.<br>**Workflow:** the same: packaging register per product, tonnage by material, 31 March declaration, declarations of conformity.<br>**Difference:** two segments, online sellers and importers against food firms and manufacturers.<br>**Source view:** both cross-link sections ask for the merge. |
| IDEA-57 | G2-I05, G6-I05 | **What they do:** the same set-and-forget permit-expiry monitor for employers of foreign workers.<br>**Channel:** the same, gestorías and immigration lawyers. |

**Checked against the full text and kept separate**

| Pair | Why it stays separate |
|---|---|
| G3-I01 and G3-I11 (IDEA-30, IDEA-29) | **Source view:** G3 says a later merge "may" combine them.<br>**Why apart:** they differ in buyer (individual long-term landlords against mid-term managers and coliving operators), legal regime (caps and IRAV updates against temporary-cause evidence), price (€4–5/month against €8–12 per contract) and kill test.<br>**Shared:** the versioned rules engine.<br>**Validation:** test them in the same batch, and test whether IDEA-30 is a light tier of IDEA-29. |
| G5-I09 and G5-I03 + G5-I04 (IDEA-48, IDEA-47) | **Shared:** the same data layer.<br>**Why apart:** buyer (software firms, renting firms and insurers against van owners and dispatchers), product form (API against app) and kill test (at least 5 of 20 integrators at €149/month, against pilot conversion).<br>**Validation:** kept apart so that U3 gets its own verdict; same batch. |
| G1-I02 and G5-I02 (IDEA-02, IDEA-46) | **Source view:** G5 suggests one interest-and-claims engine with haulage as a vertical.<br>**Why apart:** the interest calculator is shared, but G5-I02's core is haulage-specific: the fuel-revision invoice line (RDL 9/2026) and detention claims. It also has its own buyer and association channel. |
| G6-I12 and G6-I01 (IDEA-52, IDEA-53) | **Source view:** G6 says they share one document-validation engine as "two wedges".<br>**Why apart:** the wedges are premium UGE talent cases and volume regularisation renewals. Their checks differ (bank-statement reconciliation, insurance clauses and thresholds, against roster import and renewal dates), and so do their prices.<br>**Validation:** kept apart so that U2 gets its own verdict; same batch. |
| G6-I01 and IDEA-57 | **Why apart:** a case manager for habilitated filers against a monitor for employers. The buyer and the job differ. |
| G2-I12 and G6-I08 (IDEA-26, IDEA-60) | **Source view:** G6 sees a possible cross-SME grants product.<br>**Why apart:** G6-I08's core is pre-application readiness for startup loans (own funds; ENISA, CDTI and Neotec rules), while G2-I12's core is justifying grants already awarded. They overlap only in post-award tracking. |
| G2-I12 and G5-I08 (IDEA-26, IDEA-28) | **Source view:** G5 expected G5-I08 to fold into a finance-track claims idea.<br>**Why apart:** G1 filtered FIN-19 to FIN-21, so that idea does not exist. Pre-loss inventory and insurer or Consorcio claims are a different job from grant justification. |
| G1-I12 and G1-I13 (IDEA-12, IDEA-13) | **Why apart:** a monitoring subscription against a hosting and migration service. G1-I12 refers users to G1-I13. |
| G1-I03 and G1-I05 (IDEA-03, IDEA-05) | **Why apart:** receiving and reporting invoices against issuing them. G1-I03 pairs with any issuer. |
| G2-I04 and G4-I12 (IDEA-16, IDEA-19) | **Why apart:** micro employers against households.<br>**Shared:** minimum-wage and time-record rule engines (G4 cross-links). |
| G2-I07 and G2-I09 (IDEA-20, IDEA-22) | **Shared:** both come from Ley 10/2025.<br>**Why apart:** buyer (all B2C SMEs against basic-service providers), duty (15-day complaint clock against the 3-minute human-answer rule and an ENAC audit) and price (€5 against €199–499/month). |
| G4-I01 and G2-I10 (IDEA-24, IDEA-23) | **Why apart:** theft evidence packs against CCTV data-protection compliance.<br>**Link:** LEG-06 is a build constraint for IDEA-24. |
| G3-I07 and the food-waste module of IDEA-49 | **Why apart:** G3 suggests one Ley 1/2025 module across restaurants, retailers and food producers. That is a shared module, not a duplicate product. |
| G6-I02 and the rule feed in IDEA-06 | **Shared:** the same "rule radar" pattern; G5 suggests checking whether a shared alerting engine makes sense.<br>**Why apart:** domain and buyer differ: immigration filers against gestorías. |

---

### Theme A. Getting paid: MASC and late payment

#### IDEA-01 MASC pre-litigation kit and court-ready claim file (unpaid invoices, rent and community arrears)
- **Type:** B (primary). A secondary: cheaper than per-file certified platforms and agency success fees. C secondary: arrears monitoring per lease.
- **Buyer:** autónomos and SMEs claiming unpaid invoices, the small law firms, procuradores and gestorías acting for them, plus landlords, rental agencies and administradores de fincas.
- **Sources:**
  - G1-I01 (`stage2_G1_money_tax_software.md:542`);
  - G2-I02 (`stage2_G2_labour_legal_admin.md:462`);
  - G3-I03 (`stage2_G3_property_hospitality.md:400`);
  - G4-I09 (`stage2_G4_retail_services.md:797`).
- **Problem and product:**
  - Since 3 Apr 2025, most civil claims are inadmissible without proof of a valid negotiation attempt; this includes monitorios and evictions for non-payment. Yet there is still no official channel, and courts apply different proof rules by city (LEG-01, PRO-12, FIN-06, CON-20).
  - Small claims are uneconomic. Certified platforms charge €110–150 + VAT per file and agencies 5–25%, while about 9 in 10 creditors never claim statutory interest (LEG-01, FIN-08, FIN-03).
  - **One engine:** guided intake by claim type and court city; lawyer-reviewed offer templates; sending through a qualified certified-delivery partner; waiting-period timers and a reply log; a court-ready evidence pack and claim paragraph; a fixed-fee hand-off to partner lawyers above €2,000 (FIN-07).
  - **Segment modules:**
    - B2B invoices: interest and €40 calculator, monitorio pre-fill;
    - landlords and communities: arrears alert, the LAU and LPH steps, the community debt certificate;
    - law firms: multi-case workspace and a court-criteria library;
    - a free inbox for SMEs that receive invitations.
- **Key pains:** FIN-06, FIN-07, FIN-08, FIN-03, FIN-01, FIN-02, TAX-20, LEG-01, LEG-02, LEG-04, PRO-12, CON-20, CON-23 (HOU-14 is CON-20's duplicate).
- **Why now:**
  - LO 1/2025 has been in force since 3 Apr 2025. As an enacted law it does not lapse with the dissolution, but the new Cortes could amend it, and ICAM wants MASC made voluntary.
  - The official MASC services foreseen in additional provision 3 were still pending on 6 Oct 2026.
  - Monitorios fell 20.7% in Q2 2026 while Madrid's backlog grew 10.4% (FIN-06, FIN-07).
  - The Supreme Court has not unified the case law (LEG-01).
  - The eviction-suspension regime was re-created by RDL 29/2026, which faces a vote around 12 Nov 2026 (CON-20).
- **Price hypothesis:**
  - €19–39 per claim self-serve (G1-I01), or €29–39 per file (G2-I02);
  - €99/month for law firms, gestorías and collection agencies, including 10 files, then €8 per file (G2-I02); or €19–39 per lawyer per month (G4-I09);
  - €29–49 per landlord case plus €3–5/month of monitoring per lease, and €1 per community per month for administradores (G3-I03);
  - the cost of a certified send is still to be validated.
- **Evidence:** strong. The rule is in the BOE, the volumes are official (CGPJ), local judges' agreements and appeal decisions are documented, and an ICAM survey of 1,164 lawyers (one outlet) agrees. Inadmission and success rates are unknown.
- **Moat:** moderate. Templates are trivially generated by AI. The defensible parts are:
  - a city-by-city admissibility and court-criteria dataset that grows with user outcomes;
  - certified-delivery partnerships;
  - a lawyer and procurador hand-off network;
  - placement inside invoicing tools and administradores' software.
- **Top risks:**
  1. A free official MASC channel appears, or a post-election reform makes MASC voluntary.
  2. Courts refuse private certificates, or the rules on what a valid attempt contains stay unsettled.
  3. Price pressure from RedClaimer (€99.90 per file), Legal Pigeon and burofax providers. And fear of upsetting customers suppresses use: 89% never claim interest.

#### IDEA-02 Receivables autopilot (reminders, statutory interest, payment-date forecasts)
- **Type:** C (primary); B secondary.
- **Buyer:** B2B autónomos and micro and small firms that invoice on credit, usually the owner or the one admin person; gestorías in bulk.
- **Sources:** G1-I02 (`stage2_G1_money_tax_software.md:632`).
  - It escalates to IDEA-01.
  - Its interest engine overlaps with IDEA-46.
- **Problem and product:**
  - Only 41.51% of invoices were paid on time in Q3 2026, and about 9 in 10 suppliers never claim the statutory interest or €40 per invoice that Ley 3/2004 grants (FIN-05, FIN-03).
  - The product reads issued invoices and the bank feed and sends escalating reminders by email or WhatsApp.
  - It shows accrued interest and the €40 as an optional settlement lever, and forecasts each customer's payment date in a 13-week cash view.
  - It also flags terms beyond the 60-day legal cap, alerts VAT base-modification deadlines for insolvent debtors (TAX-20), and escalates to IDEA-01 in one click.
- **Key pains:** FIN-05, FIN-03, FIN-01, FIN-02, TAX-20.
- **Why now:**
  - No late-payment sanctions regime or EU cap can arrive before 2027: the Cortes are dissolved and the EU regulation is blocked (FIN-01).
  - E-invoice payment-status data arrive in 2027–2029 (TAX-06).
  - The H2 2026 statutory rate of 10.40% is single-source.
- **Price hypothesis:** €5–9/month; gestoría bulk at about €2 per client.
- **Evidence:** strong for the problem (PMcM, Cepyme and Informa agree); medium on whether users will act on interest and the €40.
- **Moat:** low to medium. Integrations, accumulated payment-behaviour data and the MASC escalation path; mostly speed and distribution.
- **Top risks:**
  1. Invoicing vendors bundle reminders and interest for free.
  2. Fear for the customer relationship leaves the interest features unused.
  3. Sharing payer scores across users may be legally constrained.

### Theme B. Invoicing, VeriFactu and e-invoicing

#### IDEA-03 E-invoice inbox and payment-status reporter for small firms
- **Type:** B.
- **Buyer:** micro and small companies that receive supplier invoices, with the owner or a gestoría handling accounts payable; asesorías filing in bulk.
- **Sources:** G1-I03 (`stage2_G1_money_tax_software.md:701`); FIN-25 is merged as a duplicate.
- **Problem and product:**
  - Under RD 238/2026 and Orden HAC/1028/2026, a recipient must reject an invoice within the window or it counts as accepted, and must report its due date and the date of full payment (TAX-06). Accounts payable becomes regulated, deadline-bound reporting.
  - The free public platform (SPFE) handles exchange but not the matching of bank payments to invoices (TAX-05, inference).
  - The product is an inbox connected to the SPFE and private platforms that reads all four formats. It offers one-tap approval or rejection and reports payment dates automatically by matching the bank feed.
  - It also provides a deadline queue, a bulk mode for asesorías, and a "my payment period" report that doubles as the art. 13.3 bis LGS self-certificate for subsidies above €30k (FIN-26).
- **Key pains:** TAX-06, TAX-05, FIN-26 (FIN-25 merged).
- **Why now:**
  - Orden HAC/1028/2026 has been in force since 6 Oct 2026.
  - The dates (6 Oct 2027, 2028 and 2029) are fixed in the BOE and do not depend on Parliament.
  - The SPFE must be live two months before 6 Oct 2027.
  - When companies at or below €8M must report statuses is in conflict (section 5).
- **Price hypothesis:** €5–12/month per company; asesoría bulk at €1–3 per client per month.
- **Evidence:** strong on the regulation (BOE); weak on compliance cost and willingness to pay.
- **Moat:** medium. Format and platform interoperability, accurate bank matching, the asesoría channel and payment-date data. Incumbents (TeamSystem, Visma/Holded, Wolters Kluwer) will add status features, and the free SPFE caps the price.
- **Top risks:**
  1. The SPFE ships a good free interface, or third-party software gets no programmatic access (a kill criterion).
  2. The small-firm obligation slips, or reporting stays voluntary until 2029.
  3. Registration as a private exchange platform may be required.

#### IDEA-04 VeriFactu retrofit adapter for legacy tills and scales
- **Type:** B.
- **Buyer:** shop and bar owners whose existing tills or scales issue tickets (fruterías, carnicerías, bars with older POS, personal services), reached through POS and scale installers.
- **Sources:** G1-I04 (`stage2_G1_money_tax_software.md:775`).
- **Problem and product:**
  - Tickets are simplified invoices, so tills and scales are invoicing systems under VeriFactu.
  - ATA (single source) says adapting a digital scale can cost more than €2,500, and a bar cash register up to €1,800 (TAX-01).
  - The product is a capture device on the printer line, or a driver, plus a cloud invoicing-system layer.
  - It turns each legacy ticket into a VeriFactu record (hash chain, event log, QR on the existing printer) and submits it to the AEAT, with a dashboard for owner and gestoría. It is sold with installer partners.
- **Key pains:** TAX-01, TAX-02, TAX-03 (partly).
- **Why now:**
  - The BOE still sets 1 Jan and 1 Jul 2027.
  - The move to October 2028 was announced but is not in the BOE (TAX-02). It gives time to build but weakens urgency.
- **Price hypothesis:** €150–300 one-off for device and installation, plus €5–8/month.
- **Evidence:** medium. The hardware costs are a single advocacy source (ATA); the scope is well sourced.
- **Moat:** high if it is legal and works. Device integrations, producer liability and an installer network cannot be cloned by software alone.
- **Top risks:**
  1. The AEAT or the DGT rules that external capture cannot meet the integrity and inalterability requirements.
  2. Producer duties: a declaración responsable, and sanctions of up to €150,000 per year and system type.
  3. Vendor upgrade quotes come in below about €300, or the 2028 move removes urgency.

#### IDEA-05 Fair-terms invoicing and e-invoicing for micro businesses
- **Type:** A.
- **Buyer:** autónomos and micro firms that invoice, both those on Excel or Word and those unhappy with an incumbent.
- **Sources:** G1-I05 (`stage2_G1_money_tax_software.md:842`); VOX-12 is merged in.
- **Problem and product:**
  - Cheap invoicing exists. The complaints are about terms: invoice caps and yearly price rises, forced upgrades, obstructed cancellation, lost history at exit, phone support only on paid tiers, and VeriFactu bugs (VOX-08 to VOX-11).
  - The product is a flat €6/month tool with VeriFactu, Facturae and UBL e-invoicing, the SPFE copy and unlimited invoices.
  - It offers one-click cancellation and a free six-year read-only archive after cancelling.
  - It also has an Excel/Word importer that keeps the numbering, a free gestor seat with exports to a3, Contasol and Sage, and human WhatsApp support.
- **Key pains:** VOX-08, VOX-09, VOX-10, VOX-11, TAX-07, TAX-03, TAX-01.
- **Why now:** switching windows around VeriFactu (2027 in the BOE) and the 2027–2028 e-invoicing upsells (TAX-02, TAX-05).
- **Price hypothesis:** €6/month or €60/year; archive-only plan at €1/month or free.
- **Evidence:** medium. Unverified reviews are consistent across at least six vendors, and saturation is equally well evidenced.
- **Moat:** none, speed only. Gestoría distribution is the only edge, and Cuéntica already sells "sin permanencia" with export at any time.
- **Top risks:**
  1. A saturated market, with €0–10 plans and the AEAT's free app.
  2. Human support at €6/month destroys the margin.
  3. Gestores are locked into a3 or TeamSystem.

### Theme C. Gestorías, official mailboxes and owner-manager duties

#### IDEA-06 Gestoría client-obligation cockpit ("which rule hits which client, and is it in force?")
- **Type:** B (primary). C secondary: rules update themselves and clients are notified automatically, plus a €5/month "what changed for me" digest for SMEs.
- **Buyer:** small gestorías, asesorías and graduados sociales (1–9 staff, 25–200+ clients each); SMEs without an adviser as a second tier.
- **Sources:**
  - G1-I06 (`stage2_G1_money_tax_software.md:932`);
  - G4-I08 (`stage2_G4_retail_services.md:744`);
  - G2-I15 (`stage2_G2_labour_legal_admin.md:1253`).
- **Problem and product:**
  - Every rule change forces a client-by-client review in Excel: VeriFactu re-planned twice, e-invoicing dates by turnover band, societario bases, módulos limits, RD 723 statements, the time-recording decree.
  - Meanwhile 72% of asesorías must re-educate clients and 7 in 10 firms struggle to hire (TAX-23, TAX-04, PRO-10, PRO-11, LAB-25).
  - **Client import:** from CSV or a3, Contasol and Sage exports.
  - **Per-client tags:** regime, turnover band, territory (common, foral, Canarias), invoicing software and whether that software declares VeriFactu compliance, employer status, and flags such as "sells by phone", "has CCTV" or "employs non-EU staff".
  - **Outputs:**
    - per-client deadlines and readiness;
    - a curated rule-status feed (in the BOE, announced, draft or lapsed);
    - personalised notices in Spanish, Catalan or Basque, with replies tracked.
  - It is also the distribution base for IDEA-03, IDEA-07, IDEA-09 and IDEA-10.
- **Key pains:** TAX-23, TAX-22, VOX-21, TAX-02, TAX-04, TAX-14, TAX-13, TAX-09, PRO-10, PRO-11, LAB-25, ADM-05 (VOX-13 merged).
- **Why now:**
  - VeriFactu is in the BOE for 2027, with October 2028 announced but no instrument published while the Cortes are dissolved.
  - E-invoicing starts on 6 Oct 2027 and 2028 (Orden HAC/1028/2026, in force).
  - The societario regularisation lands in 2027–2028, and the MEI rises to 1% in 2027.
  - The dissolution makes rule status a weekly question: bills lapse and decree-laws await convalidation, but the Government can approve regulations until it becomes caretaker (LAB-25).
- **Price hypothesis:** per gestoría, by client count:
  - €29–79/month (G4-I08);
  - €39–79/month (G1-I06);
  - €49–149/month (G2-I15);
  - €5/month for SMEs.

  No asesoría software prices appear in the notes.
- **Evidence:** medium. The vendor surveys (Cegid, Quipu) are consistent and the rule calendar is documented in the BOE and by the AEAT; the hours spent were never measured.
- **Moat:** medium. A maintained rules engine, a vendor-neutral position, switching costs once client tags live in the tool, and the client-communication layer. Wolters Kluwer (a3), TeamSystem or Sage could bundle it, and AI makes summaries nearly free.
- **Top risks:**
  1. Gestorías will not pay for "information": they are Excel-heavy, and only 41% of individual advisers are up to date.
  2. Incumbents add client-readiness dashboards.
  3. The rules settle and the urgency fades.

#### IDEA-07 Official e-notification watchdog and tax-debt guard
- **Type:** C (primary); B secondary, as a multi-client board for gestorías.
- **Buyer:** owners and administrators of SLs and other legal entities (about 1.45M), autónomos obliged to or opted in, colegiado professionals, and gestorías monitoring clients.
- **Sources:**
  - G1-I08 (`stage2_G1_money_tax_software.md:1085`): adds debt and deferral tracking and BOE edict search;
  - G2-I01 (`stage2_G2_labour_legal_admin.md:396`): adds certificate-expiry tracking and an MVP that needs no certificate.
- **Problem and product:**
  - A notice left unopened for 10 days counts as delivered (or rejected). Enforcement orders and account embargoes follow, and embargoes now execute overnight; the courts are split on missing email alerts (ADM-08, TAX-18, TAX-19).
  - Notices are spread over DEHú and, per a vendor, more than 9,000 sedes. The representative certificate costs €14 + tax, expires every 2 years and is often shared among staff (ADM-07).
  - **Phase 1, an "alert amplifier":** official alert emails are redirected and parsed, with multi-channel escalation on days 5 and 8, a weekly "nothing pending" heartbeat, a diligence log and certificate-expiry tracking.
  - **Phase 2, if lawful:** active polling of DEHú, the AEAT and the TGSS through representation or collaborator status. It classifies notices (requerimiento, apremio, embargo, sanction), computes deadlines, tracks debt and deferral instalments, and searches BOE edicts by NIF.
- **Key pains:** ADM-08, ADM-07, TAX-18, TAX-19, TAX-10, VOX-17 (FIN-24 merged).
- **Why now:**
  - The Ley 39/2015 duty and 10-day rule are in force.
  - There was no Supreme Court ruling on missing alerts as of Nov 2025, and Audiencia Nacional ruling 489/2026 backs deemed delivery.
  - The 24-hour embargo roll-out runs to Nov 2026 (single source).
  - The AEAT fines post-campaign Renta corrections at €100 (Oct 2026).
  - Demand is perennial, and the rules are not exposed to the election.
- **Price hypothesis:**
  - €4–6/month per NIF (G1-I08);
  - €5/month, or €9/month with active polling (G2-I01);
  - gestorías at €1–2 per client.
- **Evidence:** strong. The rules are in the BOE and the case law is split. How often harm occurs is not quantified, and the 24-hour embargo rests on a single source.
- **Moat:** medium at best. Reliable coverage of many sedes, a security posture customers trust with certificates, and gestoría distribution. The alert amplifier alone is trivially copyable.
- **Top risks:**
  1. No lawful programmatic access without holding clients' private keys; both sources make this a kill criterion.
  2. The official apps start pushing reliable alerts.
  3. The value stays invisible if few notices arrive: kill if under half of pilot companies receive one in six months.

#### IDEA-08 Hacienda letter shield (pre-filing cross-check and evidence pack)
- **Type:** B (primary); C secondary.
- **Buyer:** B2C autónomos and micro firms that take cards or Bizum, and professionals in estimación directa; gestorías resell.
  - Sectors named: hospitality, dental and vet clinics, hairdressers, retail (including recargo de equivalencia) and taxis.
- **Sources:** G1-I09 (`stage2_G1_money_tax_software.md:1151`).
- **Problem and product:**
  - Since Jan 2026 banks report card and Bizum collections monthly (modelo 170). Mismatches with the VAT return (303) trigger letters.
  - Letters after the Renta target unproven expenses, and owners reconcile transaction by transaction under short deadlines (TAX-15, TAX-16, TAX-17).
  - Before each quarterly filing, the product ingests acquirer, POS and Bizum exports plus the bank feed. It reconciles them against tickets, invoices and the draft 303/130 bases, and explains gaps by the five known causes.
  - It flags risky expense lines when they are captured and assembles a response pack when a letter arrives.
- **Key pains:** TAX-15, TAX-16, TAX-17, TAX-09.
- **Why now:**
  - Monthly modelo 170 reporting has applied since 1 Jan 2026, with no minimum (RD 253/2025 and Orden HAC/747/2025, to verify).
  - Letter waves run from September.
  - The Consejo para la Defensa del Contribuyente report appeared in Oct 2026.
- **Price hypothesis:** €7–12/month or about €20 per quarter; gestoría bulk plans.
- **Evidence:** medium. The letters come from a single press source, and their frequency is unknown.
- **Moat:** medium. Acquirer and bank integrations, and know-how about AEAT matching; accounting suites could copy it.
- **Top risks:**
  1. Letters are too rare: kill if under about 5% of B2C businesses receive one a year.
  2. Taxpayers cannot see the modelo 170 data their bank filed.
  3. Acquirer data cannot be obtained without manual work.

#### IDEA-09 Autónomo cuota and regularisation tracker
- **Type:** C.
- **Buyer:** autónomos in the real-income system (3,483,645 in the RETA at end-Sep 2026), societarios and family collaborators (about 1.2M), and gestorías and graduados sociales in bulk.
- **Sources:**
  - G1-I07 (`stage2_G1_money_tax_software.md:1015`);
  - G2-I13 (`stage2_G2_labour_legal_admin.md:1151`).
- **Problem and product:**
  - Choosing a tramo is a forecast that is settled a year later. In the ENA survey, 35.1% paid after regularisation, they rated the process 2.2/10, and 15% did not know their tramo (TAX-12).
  - Societarios who did not update their base face about €135/month more and a lump-sum back-charge in 2027–2028 (TAX-13). The Ombudsman says the TGSS method wrongly excludes months such as birth leave (ADM-11).
  - The product pulls income from invoicing or bank data, or a monthly entry, and estimates net income and the tramo. It shows the regularisation exposure and a monthly amount to set aside.
  - It reminds the user of the six base-change windows and the end of the €80 tarifa plana, checks the €1,424 societario minimum, checks the TGSS resolution, and provides a claim template and an Import@ss guide.
- **Key pains:** TAX-12, TAX-13, ADM-11.
- **Why now:**
  - The 2026 tables are frozen (Orden PJC/297/2026, single source).
  - The MEI rises to 1% in 2027, and the 2027 bases are pending.
  - The societario regularisation lands in 2027–2028.
  - The Junts bill on societario bases may have lapsed with the dissolution.
- **Price hypothesis:** €3–4/month or €29/year, with a free one-off check as a lead magnet; gestoría bulk at €0.50–1 per client per month.
- **Evidence:** strong for the pain (the ENA survey of 878 responses, ATA data and the official tables); medium for software fit. On its own, the G2 track's evidence is weak: a single Ombudsman source.
- **Moat:** low to none. The formula is public and free calculators exist; continuous automation through integrations and gestoría distribution are the only edges.
- **Top risks:**
  1. Invoicing vendors and online asesorías add it free; Cuéntica's calculator is in its €19 plan.
  2. The TGSS ships its own simulator with alerts.
  3. Retention collapses after one regularisation: kill if under 1 in 10 trial users pay €2/month or more.

#### IDEA-10 SL director guard (dissolution-trigger and accounts-deposit alerts)
- **Type:** C.
- **Buyer:** owner-managers of micro and small SLs, who are often societarios, sold through their asesoría.
- **Sources:** G1-I10 (`stage2_G1_money_tax_software.md:1218`).
- **Problem and product:**
  - When losses push net equity below half of share capital, directors have two months to convene the shareholders, or they risk personal liability for new debts (STS 1477/2026, a single press source).
  - Only 52 of 1,427 micro insolvency procedures aimed at continuation, and a missed accounts deposit brings a registry block and ICAC fines of €1,200–60,000 (FIN-16, FIN-17, TAX-21).
  - The product reads the trial balance monthly or quarterly and shows net equity against capital, and the cash runway, as a traffic light.
  - When the trigger is hit, it starts a two-month countdown with a template notice and keeps a dated log. It also reminds the user of the accounts deposit.
- **Key pains:** FIN-17, FIN-16, TAX-21.
- **Why now:** STS 1477/2026 (Oct 2026) reinforces directors' personal liability, and company insolvencies rose 15.5% year on year in Q4 2025. The LSC is in force.
- **Price hypothesis:** €5/month per SL; asesoría bulk at €1–2 per SL.
- **Evidence:** medium.
- **Moat:** none, speed only.
- **Top risks:**
  1. Owners of struggling firms ignore the alerts.
  2. Asesorías treat it as a free feature.
  3. Ledgers are updated only quarterly, or accounting suites already alert.

### Theme D. Fraud, contracts and online presence

#### IDEA-11 Supplier bank-detail change guard (anti-IBAN-fraud payment check)
- **Type:** C (primary); B secondary.
- **Buyer:** micro and small firms where an owner or admin pays suppliers by transfer, and autónomos with recurring suppliers.
- **Sources:** G1-I11 (`stage2_G1_money_tax_software.md:1279`); VOX-03 is merged in.
- **Problem and product:**
  - Fraudsters email fake IBAN changes or pose as the boss, and the transfers cannot be reversed (FIN-12, VOX-03). The figures:
    - BEC losses above €15,000 per incident (a secondary source);
    - 22% of SMEs hit by invoice or payment fraud in 12 months (a vendor survey);
    - online fraud up 19% (INCIBE).
  - The product keeps a register of verified supplier IBANs and watches invoices, emails and SEPA payment files.
  - It flags new or changed IBANs, country mismatches, look-alike domains and urgent "CEO" requests. It then requires a call-back and a second approver, and logs evidence for a bank claim.
- **Key pains:** FIN-12 (VOX-03 merged).
- **Why now:**
  - INCIBE incidents rose 26% and helpline queries 44.9% in 2025, and attackers now steal session cookies from autónomos (an Oct 2026 headline).
  - B2B e-invoices from 2027–2028 can tie each IBAN to a verified invoice.
  - Verification of Payee may already be in force (section 5).
- **Price hypothesis:** €5–9/month per company.
- **Evidence:** medium. The trend data are official; SME losses come from a vendor survey and a secondary source.
- **Moat:** low.
- **Top risks:**
  1. Verification of Payee already does the name–IBAN check for free.
  2. SMEs do not invest until they are hit.
  3. Banks bundle the feature.

#### IDEA-12 B2B subscription and contract guard
- **Type:** C.
- **Buyer:** autónomos and micro firms with several SaaS, telecom, web and service contracts, especially former Kit Digital beneficiaries (more than 860,000 grants).
- **Sources:** G1-I12 (`stage2_G1_money_tax_software.md:1334`).
- **Problem and product:**
  - Small firms lose money to forgotten auto-renewals, cancellations that only "request" cancellation, and telecom permanencias that consumer protection does not cover.
  - Kit Digital leftovers cost about €22–66/month for a website, against about €8/month for hosting (VOX-05, VOX-09, VOX-16).
  - The product detects recurring charges from bank and card feeds and from invoice emails. It builds a renewal calendar with notice periods and alerts 30 and 7 days ahead.
  - It flags price rises, sends cancellation requests by certified email and tracks the replies, and suggests cheaper equivalents (IDEA-13).
- **Key pains:** VOX-09, VOX-16, VOX-05, VOX-08, TAX-07.
- **Why now:** the subsidised Kit Digital years have ended, the VeriFactu and e-invoicing upsell wave is coming, and price-creep complaints recur.
- **Price hypothesis:** €3–5/month, or free with a share of first-year savings.
- **Evidence:** medium. Cancellation complaints are consistent across six or more vendors, but there are no data on contract counts or willingness to pay.
- **Moat:** none, speed only.
- **Top risks:**
  1. Savings are one-off, so users churn: kill if under about 40% are retained after three months.
  2. The typical micro firm may hold too few contracts: kill if the median is under three.
  3. Banks add subscription views.

#### IDEA-13 Kit Digital website rescue and low-cost managed hosting
- **Type:** A.
- **Buyer:** former Kit Digital beneficiaries still paying for website upkeep after the subsidised year.
- **Sources:** G1-I13 (`stage2_G1_money_tax_software.md:1392`).
- **Problem and product:**
  - Post-subsidy upkeep runs from €21.98/month (Arsys) to €66/month (a forum figure). Hosting costs about €8/month and a domain about €10/year, and some contracts carry exit fees (VOX-16).
  - The product offers a free audit of what the owner pays and owns, then a guided migration (content export, domain transfer).
  - It finishes with managed hosting, with basic updates, at €8–10/month and no minimum term.
- **Key pains:** VOX-16 (VOX-15 is background; it was filtered as N4).
- **Why now:** the last calls closed in Oct 2025, so most subsidised years end during 2026 (an inference). The programme is closed (ADM-12 and ADM-13 were filtered as N3), so the window is time-limited.
- **Price hypothesis:** €8–10/month all-in, with free migration on annual plans.
- **Evidence:** medium.
- **Moat:** none, speed only.
- **Top risks:**
  1. Sites on proprietary builders may not export.
  2. Owners do not value their site, and margins are thin and service-heavy.
  3. The window closes.

#### IDEA-14 Review-attack alarm and evidence kit for local businesses
- **Type:** C.
- **Buyer:** restaurants, bars and local service businesses with Google or Tripadvisor listings.
- **Sources:** G1-I14 (`stage2_G1_money_tax_software.md:1450`).
- **Problem and product:**
  - Attackers post bursts of fake one-star reviews (one bar received about 20 in under an hour), and extortion offers follow. Google's reporting tool "rara vez funciona" (rarely works) (VOX-01), and owners are pitched illegal paid reviews (VOX-02).
  - The product monitors listings every few minutes, detects bursts, new accounts and copied text, and alerts at once.
  - It captures timestamped evidence through a certification partner and pre-fills the platform report and a police or lawyer file. Legitimate review requests with no incentive are optional.
- **Key pains:** VOX-01, VOX-02. LEG-14 (the duty to say whether reviews are verified, art. 20.4) was filtered as N1 and could be folded in.
- **Why now:** attacks were still reported in April 2026, and fake reviews have been illegal since May 2022, with fines of up to €100,000.
- **Price hypothesis:** €5–9/month per location.
- **Evidence:** weak. The source tag is "weak to medium": press and opinion pieces, mostly from Catalonia, with no scale data.
- **Moat:** low.
- **Top risks:**
  1. Platform terms restrict automated monitoring; Tripadvisor access is unknown.
  2. Attacks may be too rare per business: kill if under about 1 in 20 restaurants is hit a year.
  3. Google improves its own detection.

#### IDEA-15 Spanish ISP block monitor and evidence log for websites and online shops
- **Type:** C.
- **Buyer:** startups and SMEs whose websites or shops sit on shared CDNs (SaaS, e-commerce, media), and the agencies that run those sites.
- **Sources:** G6-I10 (`stage2_G6_expat_startups_gaming.md:486`).
- **Problem and product:**
  - Since Feb 2025, ISPs have blocked IP addresses used by pirate streams during LaLiga broadcasts, and must apply the lists within 30 minutes. A Barcelona commercial-court order extends blocking to other sports, films and series.
  - Legitimate sites on the same shared IPs go dark at peak hours, and startups lack the evidence to claim compensation (STA-16).
  - The product runs probes on home and mobile lines at Movistar, O2, MásOrange, Vodafone, Digi and smaller ISPs. They test the customer's domains every few minutes, detect DNS, IP or SNI blocks and send alerts.
  - It keeps a timestamped evidence log that exports for claims, and shows which CDN setting restored access.
- **Key pains:** STA-16.
- **Why now:** blocking continued from Apr to Aug 2026 and now covers more than football, and AES is pushing for evidence. The driver is court orders, so the election does not affect it.
- **Price hypothesis:** €5/month per domain; €19/month for 10 domains; agency plans.
- **Evidence:** medium. One detailed news report plus a headline tracked by AES; no count of affected sites.
- **Moat:** moderate-low. A network of probes inside the ISPs plus a historical archive of block events.
- **Top risks:**
  1. Blocking stops, or CDNs fix the collateral damage.
  2. Free community trackers exist, or the ISPs block the probes.
  3. The legality of probing and publishing evidence is unconfirmed.

### Theme E. Employers and labour

#### IDEA-16 Labour compliance pack for micro employers, white-labelled for gestorías
- **Type:** A (primary), against Sesame, Factorial and Kenjo for micro firms; C secondary.
- **Buyer:** owners of micro employers (1–10 staff) and autónomos with employees in hospitality, retail, care, cleaning and building services. Gestorías' labour departments resell it.
- **Sources:** G2-I04 (`stage2_G2_labour_legal_admin.md:603`).
- **Problem and product:**
  - From the first employee, an employer needs daily time records kept for 4 years, and since 5 Oct 2026 an RD 723/2026 written statement before day one. It also needs harassment protocols and prevention documents, all producible when the Labour Inspectorate (ITSS) asks.
  - The ITSS proposed €858M of sanctions in 2025. Without a record, a worker's concrete overtime claim can be taken as true (STS 372/2026) (LAB-01, LAB-02, LAB-12, LAB-15, LAB-18, LAB-20).
  - HR suites fit micro firms poorly. Sesame's 15-employee minimum makes a 3-person firm pay for 15 (LAB-24).
  - **The pack:**
    - clock-in by app, WhatsApp link or QR code, with a tamper-evident log and an inspection export shaped to the draft decree;
    - overtime and part-time drift alerts, and a fijo-discontinuo call-up log;
    - an RD 723 statement generator with e-delivery and change notices;
    - harassment and LGTBI templates, and self-managed prevention documents;
    - an inspection vault and a gestoría console.
- **Key pains:** LAB-01, LAB-02, LAB-14, LAB-15, LAB-18, LAB-20, LAB-12, LAB-24.
- **Why now:**
  - RD 723/2026 has applied to all employers since 5 Oct 2026 (in force).
  - The digital time-recording decree is still a draft: the Consejo de Estado's opinion was unfavourable (23 Mar 2026), approval was postponed on 24 Jul, and it was absent from the October agendas.
  - Because it is a regulation, it could still be approved before 29-N. A 6- or 12-month transition for SMEs is under discussion. This is an N3 risk for the time-recording module only.
- **Price hypothesis:** €6/month flat for up to 3 employees, then €1.5 per extra employee; gestoría white-label at €1 per employee per month wholesale.
- **Evidence:** strong on obligations and enforcement (BOE, ITSS, Supreme Court); willingness to pay is the open question.
- **Moat:** none on the product. Gestoría distribution and compliance content kept current are the only edges.
- **Top risks:**
  1. Woffu Lite and Holded's HR add-on already sit at €1.5 per employee.
  2. If the decree dies, demand stays trigger-based, because paper records remain legal.
  3. a3innuva or another payroll suite gives gestorías an equivalent client portal for free.

#### IDEA-17 Guided dismissal and termination workflow for owner-managers and their advisers
- **Type:** B (primary). A secondary, against ad hoc adviser hours.
- **Buyer:** owner-managers of micro and small employers without HR staff, and the gestorías, graduados sociales and labour lawyers who prepare terminations.
- **Sources:** G2-I03 (`stage2_G2_labour_legal_admin.md:541`).
- **Problem and product:**
  - Dismissal claims hit a record 45,230 in Q2 2026 (+11.2%), and labour trials in Madrid and Barcelona are being set for 2029–2030.
  - Recent rulings turned routine steps into traps (LAB-09, LAB-11, LAB-06):
    - a hearing before a disciplinary dismissal;
    - nullity for dismissing someone days after they objected (STS 526/2026);
    - contributions on notice pay under CRA code 0054 (RED 8/2026);
    - the Ley 2/2025 permanent-incapacity procedure, with its 10-day and 3-month clocks.
  - **The workflow:** one guided flow per termination type.
    - A risk screen for possible retaliation, and the mandatory steps.
    - Generated documents: the letter, the hearing summons, a settlement draft and the final settlement.
    - Calculators for tariff severance, notice-pay coding and back pay.
    - SMAC conciliation preparation and an export pack for the adviser, plus a sibling flow for art. 41 schedule changes.
- **Key pains:** LAB-11, LAB-09, LAB-06.
- **Why now:**
  - Litigation hit a record in 2026, and the TGSS changed its criterion in Jul 2026.
  - Tariff-fixed compensation (STS 1350/2024; STS 736/2025) makes the money side predictable enough to automate.
  - The drivers are statutes and case law already in place, so there is no lapse risk.
- **Price hypothesis:**
  - €49 per termination for owners;
  - €79/month for advisers, with unlimited cases and their own branding;
  - an optional fixed-fee review by a partner graduado social at €90–150 (hypothesis).
- **Evidence:** medium. Claim volumes and rulings are well sourced; the share of dismissals lost on fixable defects and adviser fees are not quantified.
- **Moat:** low to medium. A rules engine kept current, a network of graduados sociales and outcome data.
- **Top risks:**
  1. Owners act on impulse and call the adviser afterwards.
  2. Advisers already have templates.
  3. Liability if a tool-built dismissal is ruled null, and limits on activities reserved to professionals.

#### IDEA-18 Machine-readable database and API of collective-agreement (convenio) rules
- **Type:** B.
- **Buyer:**
  - HR, time-tracking and payroll vendors: Factorial, Sesame, Woffu, Kenjo, Holded HR, Timu, PayFit;
  - labour gestorías and asesorías;
  - employers operating in several provinces.
- **Sources:** G2-I06 (`stage2_G2_labour_legal_admin.md:746`).
- **Problem and product:**
  - Pay, hours, leave and sick-pay top-ups depend on convenios that are often provincial, and courts keep reinterpreting them: TS 753/2026 on care leave, a May 2026 ruling on shift length, and two Audiencia Nacional rulings that disagree.
  - The minimum-wage absorption test must be re-run every year, and gestorías absorb the churn at €15–20 per payslip (LAB-21, LAB-22, LAB-03, LAB-05).
  - **The product:** a versioned rules dataset, with effective dates and source links for each rule; an API that answers entitlement queries; and change alerts.
  - **MVP:** the 30–50 convenios covering hospitality, retail, cleaning, construction and metalworking in six provinces, extracted by AI with legal review.
- **Key pains:** LAB-21, LAB-22, LAB-03, LAB-05.
- **Why now:**
  - RD 723/2026 statements must name the convenio and the pay items, which pushes HR tools towards structured convenio data (inference).
  - The 2026 minimum wage was retroactive, and RED 8/2026 and the 2026 rulings add churn.
- **Price hypothesis:** for vendors, €0.10–0.20 per covered employee per month through the API; for gestorías, €49–149/month.
- **Evidence:** medium. The notes do not count convenios or show that vendors lack the data.
- **Moat:** strong if achieved. A validated, versioned dataset with vendor integrations; accuracy and update speed are the real barrier.
- **Top risks:**
  1. Incumbents (Wolters Kluwer a3, Sage, DELSOL) already maintain convenio tables.
  2. Vendors build their own, or a public source publishes structured convenios.
  3. Liability for wrong rules.

#### IDEA-19 Household-employer autopilot for domestic and care workers
- **Type:** C (primary); B secondary.
- **Buyer:** households employing domestic or care workers (about 348,000 to more than 378,000 registered workers, with roughly as many employing households), and the gestorías that run their payroll (white-label).
- **Sources:** G4-I12 (`stage2_G4_retail_services.md:941`).
- **Problem and product:**
  - Each employing household had to complete the Prevencion10 risk assessment by 14 Nov 2025, inform the worker and keep the signed plan for inspectors (PRO-18).
  - That comes on top of Social Security registration, monthly contributions and pay updates as the minimum wage rises (+61% since 2018, per AESPD). The free tool covers only the assessment, and it collapsed at launch.
  - **The product:** a set-up wizard with a contract template, monthly payslips, a contribution calendar, and alerts and recalculation when the minimum wage changes.
  - It also stores the Prevencion10 output with re-do reminders, keeps a time record if one is required, and provides an inspection vault and a year-end summary.
- **Key pains:** PRO-18.
- **Why now:**
  - The RD 893/2024 duties have been enforceable since the Nov 2025 deadline.
  - The guide, the harassment protocol and the training platform were still pending in May 2026.
  - Unions asked inspectors not to be punitive "at first", which suggests enforcement could tighten (inference).
- **Price hypothesis:** €5/month or €49/year per household; gestoría white-label at €1–2 per household per month.
- **Evidence:** strong. An official INSST release and two independent press sources; willingness to pay is untested.
- **Moat:** low.
- **Top risks:**
  1. Low willingness to pay, and churn when the worker leaves.
  2. A large informal segment: about 540,000 workers in the EPA against about 378,000 registered.
  3. Social Security already calculates contributions, and enforcement may stay light.

### Theme F. Consumer-facing duties, sales calls, premises and shops

#### IDEA-20 B2C complaint-clock and consumer-duty kit, with Hoj@ (Andalusia) and Catalan modules
- **Type:** C.
- **Buyer:** owners and managers of B2C SMEs (shops, bars, gyms, academies, clinics, beauty, accommodation, e-commerce and subscription businesses), including every consumer-facing business in Andalusia and managers with Andalusian units.
- **Sources:**
  - G2-I07 (`stage2_G2_labour_legal_admin.md:803`), which also folds in LEG-22 on official regional complaint forms;
  - G3-I06 (`stage2_G3_property_hospitality.md:551`).
- **Problem and product:**
  - **National duties since 28 Dec 2025 (LEG-12):** every trader must give each complaint an ID key and a written receipt and answer within 15 days. Traders must also show full final prices, notify customers 15 days before a renewal opt-out deadline, and state whether reviews are verified. Most small businesses log complaints nowhere, so they cannot prove they complied.
  - **Andalusia, Hoj@ (HOS-17):** businesses must register by 20 May 2027 (20 Nov 2026 for large firms) and display a QR poster. Each e-complaint must be answered within 10 working days, and it counts as received after 10 calendar days even if unopened.
  - **Catalonia (LEG-15):** signs, menus and documents must also be available in Catalan; language sanctions average €2,240.
  - **One kit:**
    - complaint intake by QR, web, WhatsApp or email, with automatic ID keys and receipts;
    - deadline clocks on local working-day calendars, reply templates, an export for inspectors, and renewal notices;
    - a Hoj@ onboarding module that parses its notification emails;
    - a Catalan module that checks menus and price lists.
- **Key pains:** LEG-12, LEG-15, HOS-17 (LEG-22 folded in).
- **Why now:**
  - The Ley 10/2025 amendments are law and in force, so the dissolution does not affect them. It is unclear whether the 12-month adaptation period also covers them.
  - Large firms face their own 28 Dec 2026 deadline (LEG-13).
  - The Hoj@ dates come from an Order of 24 Apr 2026, known only through a single vendor source; the BOJA was not checked.
- **Price hypothesis:** €5/month per location, or €9 with renewal notices and the Catalan module (G2-I07); €3–5/month or €39/year for Hoj@ (G3-I06). Bundles through gestorías, associations, and POS, booking and PMS vendors.
- **Evidence:** medium. The duties are in the BOE and Catalan enforcement is documented. The Hoj@ module is weak: a single vendor source, BOJA unchecked.
- **Moat:** none, speed only. The only lever is distribution as a module inside POS, booking, PMS and gym software.
- **Top risks:**
  1. Weak enforcement means weak willingness to pay.
  2. POS or booking vendors, or Hoj@ itself, add reminders.
  3. Few complaints per SME, so low visible value and high churn.

#### IDEA-21 Call-consent ledger and 400-prefix compliance layer for SMEs that sell by phone
- **Type:** B (primary); C secondary, as a light per-agent plan.
- **Buyer:** sales managers and owners at energy and telecom resellers, insurance agents and brokers, solar installers, estate agencies, training providers, B2B sales teams and small call centres.
- **Sources:** G2-I08 (`stage2_G2_labour_legal_admin.md:858`).
- **Problem and product:**
  - Since 17 Oct 2026, operators have blocked commercial calls that do not come from numbers with the 400 prefix (LEG-11).
  - Contracts concluded in calls that break the unsolicited-call rules are presumed to lack consent and are void. Consent must be express and given within the two years before the call, and a vendor puts numbering fines at €50,001–2M.
  - **The product:**
    - a consent ledger recording source, timestamp, scope, proof and two-year expiry;
    - a pre-dial gate on the 400 line and a Lista Robinson check;
    - call-purpose tagging, and a consent pack per contract.
- **Key pains:** LEG-11.
- **Why now:** the numbering resolution took effect on 17 Apr 2026 with six months to adapt, and blocking has been live since 17 Oct 2026. Ley 10/2025 art. 16.3–16.4 adds the separate-prefix duty. Both are in force.
- **Price hypothesis:** €19 per agent seat per month; €5/month "consent vault" for single autónomo agents.
- **Evidence:** medium. The rule and its dates are official; scope, fine range and the number of affected SMEs are unverified.
- **Moat:** medium-low and time-limited.
- **Top risks:**
  1. It is unclear whether B2B calls, and calls involving autónomos, are covered.
  2. Cloud-telephony vendors (such as Aircall) or CRMs build consent gating natively.
  3. Small sellers stop cold-calling.

#### IDEA-22 Customer-service compliance kit for small basic-service providers (Ley 10/2025)
- **Type:** B.
- **Buyer:** customer-service or compliance managers at the providers in scope regardless of size:
  - small internet and telecom providers;
  - local water utilities;
  - small electricity and gas retailers;
  - bus, coach and ferry operators;
  - postal and courier firms.
- **Sources:** G2-I09 (`stage2_G2_labour_legal_admin.md:913`).
- **Problem and product:**
  - By 28 Dec 2026 these firms must (LEG-13):
    - answer 95% of requests for a human within 3 minutes on average, and never cut calls because of waits;
    - issue complaint keys and resolve complaints within 15 working days (2 hours for service interruptions, 5 days for billing);
    - serve customers in a co-official language on request;
    - pass an annual audit by an ENAC-accredited body.
  - **The product:** it connects to the provider's cloud PBX and helpdesk, measures the 3-minute and no-dropped-call rules, issues complaint keys and tracks each type of deadline.
  - It also tags co-official-language requests and assembles the auditor's evidence pack.
- **Key pains:** LEG-13.
- **Why now:** a hard deadline on 28 Dec 2026, then a recurring annual audit. Ley 10/2025 is already law.
- **Price hypothesis:** €199–499/month by call volume, plus €1,000 for onboarding and audit preparation.
- **Evidence:** medium. The obligations are in the BOE. The SME count ("a few thousand at most") is an inference, the audit cost is unknown and the €100,000 fine is an unverified vendor snippet.
- **Moat:** medium-low. Know-how, relationships with auditors, and being first before the deadline.
- **Top risks:**
  1. The market is small: kill if fewer than about 500 SME providers remain in scope after the sector-rule carve-outs.
  2. Helpdesks already report these metrics, or auditors accept standard reports.
  3. The deadline is extended, or sector rules take precedence for internet providers.

#### IDEA-23 CCTV compliance kit with a ready response pack for data-protection complaints
- **Type:** C.
- **Buyer:** owners and managers of shops, bars, restaurants, workshops, gyms and offices with cameras; comunidades through administradores de fincas; CCTV installers as wholesale resellers.
- **Sources:** G2-I10 (`stage2_G2_labour_legal_admin.md:968`).
- **Problem and product:**
  - In 2025 video surveillance was the second-largest complaint area at the AEPD (4,050 complaints, +19%) and the area with the most finished procedures (81).
  - Complaints overall rose 64% to 30,931, and 76% of appeals to the Audiencia Nacional fail (LEG-05, LEG-06).
  - **The kit:** a guided set-up with a photo of each camera's view and a checklist. It generates the warning sign, the staff notice and the record-of-processing entry, and sends 30-day retention reminders and an annual re-check.
  - If an AEPD letter arrives, it assembles a response pack from its evidence vault. An installer edition sets up each client at installation.
- **Key pains:** LEG-06, LEG-05.
- **Why now:**
  - AEPD complaints are at a record.
  - Fines in commerce, transport and hospitality rose 1,653% to €10.76M.
  - The AEPD updated its video-surveillance guide in Feb 2025, and the GDPR and LOPDGDD are in force.
- **Price hypothesis:** €29 one-off set-up plus €2.90/month; installers at €1 per site per month wholesale.
- **Evidence:** medium. The volumes are well sourced; fines for small CCTV cases were not found, and the AEPD totals conflict (section 5).
- **Moat:** none on the software; installer partnerships are the only edge.
- **Top risks:**
  1. Little ongoing value once the sign is printed, so churn is likely.
  2. The AEPD adds a CCTV module to its free tools (Facilita, Gestiona RGPD).
  3. Small cases end in warnings or fines under €500 (a kill criterion).

#### IDEA-24 Shop theft incident log and police-ready report pack
- **Type:** B (primary); C secondary.
- **Buyer:** owners or managers of independent physical shops, starting with food and convenience retail; retail associations buying for members; city councils.
- **Sources:** G4-I01 (`stage2_G4_retail_services.md:393`).
- **Problem and product:**
  - Spanish retail loses €2,817M a year to unknown loss (1.1% of turnover). Repeat offenders commit 51% of thefts, and small shops suffer about 30% more of them (RET-04).
  - Since 10 Apr 2026 a repeat thief faces prison once three prior final convictions exist. So consequences depend on shops reporting every incident in a form that can be prosecuted (the researcher's inference).
  - **The product:** a one-minute mobile incident log (items, values, witness, CCTV clip reference with automatic deletion), a draft police report and evidence pack in each force's accepted form, a case tracker and a monthly loss report.
  - It deliberately has no facial recognition and no shared offender lists.
- **Key pains:** RET-04.
- **Why now:**
  - LO 1/2026 has been in force since 10 Apr 2026, per the BOE consolidated text. The cities track could not verify the reform (section 5).
  - Local authorities may now prosecute theft (LECrim art. 105.3).
  - Staff aggression is rising and guards are hard to hire.
- **Price hypothesis:** €9–15/month per shop; €3–5 per shop in association bulk deals; a yearly district licence for councils.
- **Evidence:** medium. The loss figures and the law are strong, but demand for reporting software is an inference that no source states.
- **Moat:** low. Association and council partnerships, templates per police force, and an anonymised loss dataset.
- **Top risks:**
  1. The bottleneck is police and court capacity, or owners' reluctance to testify, rather than paperwork.
  2. Police forces will not accept prepared packs.
  3. A free association or council tool exists, and data protection rules out shared suspect lists.

#### IDEA-25 Pre-lease "can I open here?" check and file builder for premises (Madrid first)
- **Type:** B (primary). A secondary: a cheap first pass before paying €500–1,000 for an ECU compatibility certificate.
- **Buyer:** entrepreneurs opening premises (hospitality, retail, personal services, clinics), franchise expansion managers, commercial estate agents, and the architects and engineers who prepare licensing files.
- **Sources:** G2-I11 (`stage2_G2_labour_legal_admin.md:1026`).
- **Problem and product:**
  - Businesses sign leases and start works before knowing whether their activity is allowed at the address.
  - Madrid's own service standards set 109 days to check a declaración responsable and 137 days to grant a licence.
  - Certainty costs €500–1,000 for an ECU certificate, or €600–1,250+ for an ECU-managed file, plus inspection visits, fees and the 4% ICIO tax (ADM-01, ADM-03).
  - **The check:** the user enters address, activity and floor area, and gets a preliminary verdict (allowed, conditional, needs a licence, not allowed) based on the planning rules and Ordenanza 6/2022.
  - With the verdict come the procedure, the documents, a cost estimate from the regulated ECU price table and standard timelines, plus a referral to one of Madrid's 19 ECUs or an architect. In the MVP an expert reviews each AI-drafted answer.
- **Key pains:** ADM-03, ADM-01.
- **Why now:** Madrid approved its 2027 ECU prices on 15 Oct 2026. València has been drafting a new licensing ordinance since May 2025 (status unknown). Municipal rules do not depend on the election.
- **Price hypothesis:** €49 per address check; €149 with the full file checklist and cost and timeline estimate; €199/month for agents and franchise teams (10 checks a month).
- **Evidence:** medium. The standards and regulated prices are official; actual delays and the size of the problem are not quantified.
- **Moat:** medium. A city-by-city rules dataset, reviewing professionals and ECU partnerships.
- **Top risks:**
  1. Liability for a wrong preliminary verdict.
  2. Free city assistants such as Málaga's ALU spread, or ECUs answer free as lead generation.
  3. One-off purchases make acquisition expensive, and planning data may be unavailable in usable form.

### Theme G. Public money and procurement

#### IDEA-26 Grant justification and repayment-risk workspace
- **Type:** B.
- **Buyer:**
  - finance leads or owners at SMEs and autónomos with direct grants (energy efficiency, EV charging, hiring, digitalisation, strategic projects);
  - grant consultancies, as white-label users;
  - installers who justify grants as participating firms.
- **Sources:** G2-I12 (`stage2_G2_labour_legal_admin.md:1091`).
- **Problem and product:**
  - The Recovery Facility's milestone deadline (31 Aug 2026) has passed and Spain has filed its final €25,861M payment request, so the risk shifts to justification and repayment (ADM-14).
  - Firms cite "excesiva carga administrativa" (excessive administrative burden). Payments reached only 18.7% of available credits in 2025, and MOVES III files stall when the installer stops responding (ADM-14, ADM-15).
  - **The workspace:** the user uploads the award resolution and the call's rules, and AI extracts obligations, deadlines, eligible costs and evidence requirements into a checklist and calendar.
  - An evidence vault maps invoices, payments, contracts and publicity photos to each obligation. The workspace builds the justification package, flags repayment risks, and lets beneficiaries see files that an installer or consultant manages.
- **Key pains:** ADM-14, ADM-15.
- **Why now:** justification continues through 2026–2028. CEOE asks for execution until 2028, earlier guides, easier corrections and no repayment for delays the administration caused.
- **Price hypothesis:** SMEs €19/month per active grant; consultancies €149/month for up to 20 active grants.
- **Evidence:** medium. The macro figures come from CEOE (citing EsadeEcPol and Funcas) and the official recovery-plan site; the SME-level pain rests on qualitative complaints and the Ombudsman.
- **Moat:** medium-low.
- **Top risks:**
  1. The NGEU wave fades after 2026–2028.
  2. Few beneficiaries justify grants themselves, since Kit Digital agents did the paperwork. Kill if under a quarter manage it themselves.
  3. Consultancies keep their own processes, and programmes vary too much for templates to scale.

#### IDEA-27 Small public-contract radar, including contratos menores
- **Type:** B (primary). A secondary, only if incumbents' tender alerts prove expensive.
- **Buyer:** owners and sales leads at micro and small suppliers of services, supplies and works: cleaning, maintenance, IT, consulting, events.
- **Sources:** G2-I14 (`stage2_G2_labour_legal_admin.md:1203`).
- **Problem and product:**
  - Spain's 206,242 tenders in 2024 drew 2.94 bidders on average, and 40.69% of awarded lots had a single bidder (ADM-17).
  - Tenders sit on PLACSP plus seven regional platforms whose data do not match. There is no aggregated data at all on contratos menores (minor contracts), the natural entry point for micro firms: below €15,000 for services and supplies, €40,000 for works (ADM-18).
  - **The radar:** one feed of small tenders, filtered by activity code, region and size.
  - It adds a minor-contract database (who buys what, from whom, how often, at what price) and alerts for recurring purchases and expiring contracts.
- **Key pains:** ADM-18, ADM-17.
- **Why now:** the OIReScon report approved on 22 Dec 2025 confirms the data gap, and the 2023–2026 national procurement strategy is ending.
- **Price hypothesis:** €19/month for one region; €39/month nationwide.
- **Evidence:** medium. OIReScon is an official source; micro-firm demand and incumbents' coverage are unknown.
- **Moat:** medium. A normalised minor-contract dataset would be hard to copy; plain tender alerts are commoditised.
- **Top risks:**
  1. Minor contracts are published too patchily: kill if under half of sampled municipalities publish supplier and amount.
  2. Micro firms avoid public clients because of late payment (FIN-04).
  3. licitaciones.es already covers them.

#### IDEA-28 Flood-ready business evidence vault and multi-programme claims tracker
- **Type:** C.
- **Buyer:** owners of shops, bars, workshops and industrial-estate firms in flood-prone areas, sold through insurers, brokers and gestorías. The provinces of Valencia (186,970 companies) and Alicante (145,106) come first.
- **Sources:** G5-I08 (`stage2_G5_mobility_industry_cities.md:661`).
- **Problem and product:**
  - After the Oct 2024 DANA, businesses faced parallel channels, each with its own evidence rules: AEAT aid, ERTE furloughs, ICO, CDTI, the Consorcio (251,940 claims) and Reinicia Auto+. Some files are still pending (CITY-01).
  - dana Adam (18–19 Oct 2026) hit 27 municipalities and produced 6,528 Consorcio claims in three days; business aid is still undefined (CITY-02).
  - **Before an event:** a guided inventory of premises, stock and equipment (photos, video, serial numbers, purchase invoices), plus policies and key documents, stored off-site with refresh reminders.
  - **After an event:** a one-click claim dossier and a tracker of announced aid programmes.
- **Key pains:** CITY-01, CITY-02.
- **Why now:** dana Adam's business aid package is pending, and two floods two years apart make the need recurring.
- **Price hypothesis:** €4/month per premises, or bundled free by an insurer or bank.
- **Evidence:** medium. The 2024 volumes are official; the 2026 event comes from a single outlet, and willingness to pay for prevention is unevidenced.
- **Moat:** none, speed only. A distribution deal with an insurer or bank would be the only edge.
- **Top risks:**
  1. People rarely pay before a disaster.
  2. Insurers build this themselves.
  3. Demand spikes after events, and public portals absorb it.

### Theme H. Housing, short-term rentals and property management

#### IDEA-29 ColivEs reshaped: mid-term lease compliance file for landlords, managers and coliving operators [user idea U1]
- **Type:** B (primary); C secondary, as per-contract monitoring after signature.
- **Buyer:** managers of furnished flats and rooms let for 32 days to 12 months, coliving operators and small company landlords (the most exposed, since a re-classified lease runs 7 years). Barcelona and Catalonia first, then Madrid and Málaga.
- **Sources:**
  - G3-I11 (`stage2_G3_property_hospitality.md:783`);
  - the U1 assessment (`stage2_G3_property_hospitality.md:759`);
  - U1 as given (`00_user_supplied_ideas.md:14`).
- **Problem and product:**
  - Every temporary lease must now be backed by a file the landlord can produce in court:
    - a written, proven cause;
    - duration and chaining within limits;
    - a lodged deposit and a signed condition record;
    - repairs answered within 5 working days;
    - room sums and charges within the caps.

    Without it, the lease becomes a 5–7-year habitual lease retroactively, and courts are already ruling this way (HOU-01, HOU-04, HOU-05, HOU-12, HOU-13, HOU-15, HOU-16, HOU-24).
  - The applicable rules depend on the signing date and the region, and may change again in November 2026 (HOU-02).
  - **The product:**
    - tenant-profile triage (tourist stay, temporary lease or habitual lease);
    - a guided contract builder that requests matching cause evidence into a timestamped vault;
    - a regime stamp on every contract (Llei 11/2025, the RDL 29/2026 version, or the pre-8 Oct regime under DT 8ª), with an automatic re-check after the vote;
    - lifecycle counters and deadlines, a re-classification risk score, a conversion feasibility check for tourist flats, and commodity KYC.
  - **Dropped from U1:** dynamic pricing, eIDAS wallet integration, and coliving planning or licensing.
- **Key pains:** HOU-01, HOU-02, HOU-04, HOU-05, HOU-12, HOU-13, HOU-15, HOU-16, HOU-17, HOU-19, HOU-23, HOU-24.
- **Why now:**
  - RDL 29/2026 has applied since 8 Oct 2026. Its Diputación Permanente vote is around 12 Nov 2026 (single source, forecast 35–34); the elections follow on 29 Nov and the new Cortes on 23 Dec.
  - Llei 11/2025 has been in force since Jan 2026. It is under Constitutional Court review but not suspended.
  - Pre-8 Oct seasonal contracts expire without extension (DT 8ª).
  - Courts re-classify under art. 6.4 Código Civil whatever happens to the decree, and Barcelona's tourist-flat licences end in Nov 2028.
- **Price hypothesis:** €8–12 per active contract per month, or €49/month for up to 10 units; €2–3 per bed per month for coliving operators; an optional onboarding fee.
- **Evidence:** strong. Verbatim BOE text, Catalonia's law and court rulings; willingness to pay and landlord counts are unknown.
- **Moat:** moderate. Regulatory know-how, rules versioned by date and region, a risk model built from rulings and a law-firm partnership are harder to copy than templates. Shipping before the November regime change is part of the edge.
- **Top risks:**
  1. If RDL 29/2026 is not convalidated, the national rules fall away, leaving Catalonia plus case-law risk. A new government could also repeal or replace the rules.
  2. Owners leave mid-term letting rather than comply (Barcelona's seasonal offer is down 37%).
  3. Template liability and unknown willingness to pay. Kill if Catalan operators will not pay €8 or more per contract, or if a law firm or legal-tech tool already sells the same file.

#### IDEA-30 Rent-cap, update and deadline autopilot for landlords and rental agencies
- **Type:** C (primary); A secondary.
- **Buyer:** individual landlords with 1–10 homes, and small agencies or rental managers, who can also resell it.
- **Sources:** G3-I01 (`stage2_G3_property_hospitality.md:286`). It shares its rules engine with IDEA-29 (section 2.0).
- **Problem and product:**
  - Every lease carries recurring legal calculations that depend on region, zone and date (CON-17, CON-18, HOU-02, HOU-03, HOU-12, HOU-22):
    - the first-rent cap in tensioned zones, set from the previous rent or the SERPAVI index, with ad disclosure;
    - the annual update (IRAV), capped at 2% until 31 Dec 2027;
    - regional deposit-lodging deadlines, with fines of up to €90,000 in Madrid.
  - The rules changed three times in two weeks of October 2026.
  - **The autopilot:** set up once per lease, it computes the legal maximum first rent and the ad text, and the anniversary update with a draft notice.
  - It also tracks deposit deadlines and the RDL 29/2026 extension windows, and sends "rule changed" alerts naming the leases affected.
- **Key pains:** CON-17, CON-18 (RDL 29/2026 parts only), HOU-03, HOU-22, HOU-12, HOU-02.
- **Why now:**
  - Catalonia declared 53 more tensioned municipalities on 19 Oct 2026, pending BOE publication; Asturian zones started on 30 Jul 2026.
  - The 2% cap in RDL 29/2026 has applied since 8 Oct, with the vote around 12 Nov. If the decree is not convalidated, the 2% cap and the art. 17.8 ceiling lapse, while the Ley 12/2023 caps and Catalonia's rules remain.
- **Price hypothesis:** €4–5/month for up to 3 leases; €1–1.50 per lease per month white-label for agencies; annual billing.
- **Evidence:** medium. The rules are well documented; landlord counts and time cost are not.
- **Moat:** thin. Speed, rules upkeep and agency distribution.
- **Top risks:**
  1. Portals (idealista, Fotocasa) or Homming give equivalent calculators away.
  2. Small landlords will not pay: kill if under about 1 in 10 would pay €5/month.
  3. Official zone and index data cannot be obtained reliably, and wrong calculations carry liability.

#### IDEA-31 Landlord-paid tenant screening and trust pack for foreign and mid-term tenants
- **Type:** B.
- **Buyer:** rental agencies, property managers, and mid-term and coliving operators; the landlord or the agency pays.
- **Sources:** G3-I02 (`stage2_G3_property_hospitality.md:346`).
- **Problem and product:**
  - Listings draw 135 contacts in 10 days (462 in Barcelona), and agencies must screen without charging tenants. Consumo proposed a €3.6M fine on Alquiler Seguro over an "estudio de solvencia" among other disguised fees (CON-13, CON-11).
  - Foreign tenants lack Spanish payslips and credit files, while the usual fallbacks (6-month avales, tenant-paid insurance) are now capped or banned (HOU-06, HOU-07). Newcomers are also targeted by fake listings (HOU-09).
  - **Applicant link:** commodity KYC, cross-border income evidence, an affordability check, a standard scorecard and an anti-discrimination audit log.
  - **Landlord side:** a "verified landlord" ownership check that tenants can open.
- **Key pains:** CON-13, CON-11, HOU-06, HOU-07, HOU-09; HOU-23 as a triage input.
- **Why now:**
  - RDL 29/2026 removed avales above one or two months and tenant-paid insurance from 8 Oct 2026, pending convalidation.
  - The Ley 12/2023 fee ban is being enforced.
  - About 60% of Barcelona coliving tenants are foreign.
- **Price hypothesis:** €9–15 per screened applicant, landlord-paid, or an agency seat at €39–79/month; later, a revenue share from a guarantee partner.
- **Evidence:** medium.
- **Moat:** moderate, but only with data partnerships and a guarantee underwriter; the KYC layer alone has none.
- **Top risks:**
  1. Agencies refuse to pay for something they used to bill tenants for.
  2. If RDL 29/2026 lapses, avales return and urgency drops.
  3. Discrimination complaints and GDPR enforcement: the AEPD fined a hotel €2,000 for scanning guests' IDs.

#### IDEA-32 Short-term-rental listing compliance and eligibility monitor for property managers
- **Type:** B (primary); C secondary, as a self-serve alert tier for owners.
- **Buyer:** tourist-rental managers with 10–500 units across regions, individual VUT owners, and buyers or agents checking eligibility before a purchase.
- **Sources:** G3-I04 (`stage2_G3_property_hospitality.md:445`).
- **Problem and product:**
  - Since the national registry was annulled, compliance means matching each listing to a regional code and register, and to municipal zoning: Madrid's Plan Reside, Málaga's 43 barrios, the Valencia and Alicante moratoria, Palma, Canarias.
  - Enforcement now arrives through platforms and consumer law (HOS-19 to HOS-24):
    - the €64M Airbnb fine over 65,122 listings;
    - Consumo proceedings against managers;
    - Mallorca's 146 sanction files;
    - Balearic daily coercive fines.
  - **The monitor:** it checks continuously that displayed codes match active register entries and that trader status is disclosed, and checks zone eligibility for new units.
  - It alerts on delistings and rule changes, and keeps an inspection evidence pack.
- **Key pains:** HOS-19, HOS-20, HOS-21, HOS-22, HOS-24 (context: HOU-19).
- **Why now:**
  - TSJ Madrid denied Airbnb interim relief in Mar 2026.
  - EU 2024/1028 has applied since 20 May 2026.
  - Balearic daily fines have applied since 14 Jun 2026 (the law number is single-source), and Canarias' Ley 6/2025 fines apply.
  - The platform sanctions in RDL 29/2026 are pending convalidation.
- **Price hypothesis:** €2–3 per listing per month for managers (minimum €49/month); €5/month per unit self-serve.
- **Evidence:** strong on enforcement; the final status of some city rules and managers' demand are unverified.
- **Moat:** moderate. Register pipelines and zoning maps for 6+ regions and many municipalities.
- **Top risks:**
  1. Supply is shrinking (−10.7% listings year on year), and Barcelona's licences end in 2028.
  2. Platforms make the tool redundant under EU 2024/1028.
  3. The registers cannot be queried at scale, or platform terms forbid scraping.

#### IDEA-33 Tourist-tax and regional traveller-reporting engine (Basque Country and Catalonia first)
- **Type:** B (primary). A secondary: more complete or cheaper than Chekin and PMS modules in these regions.
- **Buyer:** hotels, hostales, hostels, campsites, rural houses and VUT owners or managers in the Basque Country and Catalonia; PMS vendors and gestorías as API customers.
- **Sources:** G3-I05 (`stage2_G3_property_hospitality.md:500`).
- **Problem and product:**
  - The establishment collects tourist tax from each guest as "sustituto del contribuyente". Rates vary by category, municipality and season, with exemptions, night caps and surcharges.
  - From 1 Jan 2027 every Basque lodging must do this, and in Gipuzkoa the establishment files quarterly. Catalan rates outside Barcelona double from 1 Apr 2027 (HOS-15).
  - Both regions also run police reporting outside SES, through the Ertzaintza and the Mossos (HOS-12).
  - **The engine:**
    - a rates database: Gipuzkoa's Norma Foral 3/2026 bands, cap and surcharges, plus Bizkaia, Álava and Catalonia's Ley 2/2026;
    - a per-booking calculation API with a guest receipt, and a ledger per property;
    - draft quarterly returns, and optional traveller-report transmission.
- **Key pains:** HOS-15, HOS-12.
- **Why now:** the Basque tax starts on 1 Jan 2027, and municipalities have six months to adapt their surcharges. The Catalan step comes on 1 Apr 2027. These are regional laws, unaffected by the national election.
- **Price hypothesis:** €3–6 per unit per month; €0.10–0.20 per booking through the API; €29/month per gestoría seat.
- **Evidence:** medium. The rules are official, but Chekin's claimed coverage leaves the unmet need unproven.
- **Moat:** low to moderate. Being first before 1 Jan 2027 helps, but Chekin or a PMS could match it within a quarter.
- **Top risks:**
  1. Incumbents cover it by January: Chekin includes tourist-tax handling in all plans at €3.95–7.95 per property.
  2. The regional market is small, and free calculators may come from the Basque treasuries or associations.
  3. EU infringement case INFR(2026)4005 could reshape the reporting module.

#### IDEA-34 Building-compliance calendar and owners'-vote module for administradores de fincas
- **Type:** B (primary); A secondary, as a lighter alternative to full administradores' ERPs.
- **Buyer:** administradores de fincas (about 16,000, micro offices with 50–60 communities each, about 1M communities in all) and the consolidators buying them, such as inmho.
- **Sources:** G3-I09 (`stage2_G3_property_hospitality.md:680`).
- **Problem and product:**
  - Each building generates deadlines: supplier CAE, data protection, accessibility works, renovation grants, certifications and maintenance. Administradores track them across "correos electrónicos, documentación física, múltiples plataformas independientes" (CON-24).
  - Since Apr 2025, tourist-flat requests need votes and minutes under the 3/5 rule (CON-22).
  - **The module:**
    - a per-building obligations calendar, auto-filled from building data;
    - supplier compliance intake, linked to IDEA-36;
    - owner notices with proof of receipt;
    - a 3/5 majority calculator with minutes and certificate generation;
    - export to the administradores' ERPs.
- **Key pains:** CON-24, CON-22.
- **Why now:** inmho bought 50 firms in a year, and many owners have no succession plan. The 3/5 rule has applied since 3 Apr 2025.
- **Price hypothesis:** €1–2 per community per month (€50–100/month for a typical 50-community office).
- **Evidence:** medium. The scale is solid; the burden is described qualitatively by a vendor.
- **Moat:** moderate. The obligations database, ERP integrations and consolidator contracts.
- **Top risks:**
  1. Gesfincas, Fincas Pro, Comunidad Feliz or Fynkus already include this.
  2. An ageing profession is slow to adopt new tools.
  3. The scope of building obligations by region is unverified.

#### IDEA-35 AML compliance kit for small real-estate agencies ahead of the EU AMLR (July 2027)
- **Type:** C.
- **Buyer:** real-estate agencies and small developers that broker sales.
- **Sources:** G3-I10 (`stage2_G3_property_hospitality.md:722`).
- **Problem and product:**
  - Agencies brokering sales already have AML duties under Ley 10/2010 (identify clients and beneficial owners, assess risk, report), and many small ones do not know it (CON-14).
  - From July 2027, the EU AMLR requires evidence-based risk self-assessments, sanctions and adverse-media screening, and a compliance officer.
  - **The kit:** a guided set-up of the self-assessment, manual and procedures; a per-deal KYC and beneficial-owner checklist with commodity screening; a record vault; training reminders; and rule updates.
- **Key pains:** CON-14.
- **Why now:** the AMLR applies from July 2027. As an EU regulation, it is unaffected by the election. SEPBLAC has flagged deficiencies in the sector (snippet-level).
- **Price hypothesis:** €9–19/month per agency, plus per-check fees.
- **Evidence:** weak. The obligations are verified, but the pain and the enforcement are weakly evidenced; the notes call it "a future pain".
- **Moat:** low.
- **Top risks:**
  1. Without enforcement against small agencies there is little urgency.
  2. CRMs such as Inmovilla or Witei add AML modules.
  3. The AMLR may ease duties for small entities.

### Theme I. Construction

#### IDEA-36 Subcontractor CAE document wallet with platform sync and subcontracting-chain checks
- **Type:** B (primary); A secondary, as a flat-fee module for small main contractors.
- **Buyer:** subcontractors and autónomos in construction, installation and industrial maintenance; small main contractors; suppliers to owners' communities.
- **Sources:** G3-I08 (`stage2_G3_property_hospitality.md:633`).
- **Problem and product:**
  - Each client picks its own CAE platform, so subcontractors pay each one and upload the same prevention paperwork again and again. Reviews cite €300 to €1,400+ a year, and €2,000 a year for 15 workers on Nalanda (CON-02).
  - An expired document can block site access or payment. Main contractors must also check REA registration, staff quotas and chain levels, and keep the Libro de Subcontratación, or become jointly liable (CON-03).
  - **The wallet:** one store of company and worker documents, with expiry alerts and a map of which platform needs what.
  - **Assisted sync:** a browser extension or RPA that fills Nalanda, Dokify, Ctaima, e-coordina, Obralia and Metacontratas, plus share-links for clients with no platform.
  - **For small principals:** a digital Libro with REA, quota and chain-level checks.
- **Key pains:** CON-02, CON-03, CON-04.
- **Why now:** Oct 2026 reviews complain of Nalanda fee rises from "300 y pico" to "más de 1400 euros", and construction deaths rose 21.5% in 2025. Ley 32/2006 is in force.
- **Price hypothesis:** per subcontractor, €9/month for 1–5 workers, €19 for 6–20 and €39 for 21–50; principal module €49–99/month.
- **Evidence:** strong. An OCU complaint, a review pattern (unverified reviews), published competitor prices and the law in force; subcontractor counts and hours lost are missing.
- **Moat:** moderate. Integrations with 6+ platforms, and network effects if principals accept share-links; the platforms could block access.
- **Top risks:**
  1. Platforms forbid automated uploads and principals refuse share-links (the kill criterion).
  2. Subcontractors' willingness to pay is untested.
  3. DocuPRL or others already sell the same wallet cheaply. Medical-fitness certificates are special-category data.

### Theme J. Hospitality, retail and personal-service operations

#### IDEA-37 Digital APPCC, allergen and food-waste logbook for bars and restaurants
- **Type:** C (primary). A secondary: a cheaper substitute for consultancy paper systems and apps.
- **Buyer:** owners and managers of bars, restaurants, cafés, small hotel kitchens and caterers. There are more than 300,000 hospitality companies.
- **Sources:** G3-I07 (`stage2_G3_property_hospitality.md:590`).
- **Problem and product:**
  - Kitchens must keep daily food-safety records and an allergen record for every dish, updated at every menu change. Fines reach €600,000, with closure of up to five years (HOS-09).
  - Since April 2026, larger venues also need a food-waste prevention plan and donation agreements (HOS-08). Many kitchens still keep paper logbooks.
  - **The logbook:** phone checklists for temperatures, cleaning, pests, maintenance and deliveries, with photo evidence and timestamps.
  - An allergen matrix built from recipes regenerates the allergen sheet and signage (RD 126/2015) at every menu change.
  - It adds a Ley 1/2025 food-waste module, an inspection-ready PDF export and optional sensors. It works offline, in Spanish, Catalan and English.
- **Key pains:** HOS-09, HOS-08.
- **Why now:**
  - The article 6 duties of Ley 1/2025 apply from about 3 Apr 2026; the law's dates conflict (section 5).
  - RD 1021/2022 has replaced the old rules.
  - AI makes extracting allergens from recipes cheap.
- **Price hypothesis:** €5–9/month per venue; sensors as a one-off add-on; multi-site discount.
- **Evidence:** medium. The legal duties are certain; inspection frequency and incumbent prices are unknown.
- **Moat:** none, speed and distribution only. The consultancy channel and sensor partnerships add a little stickiness.
- **Top risks:**
  1. The incumbent field is unpriced and may be crowded: kill if apps sell for €5/month or less, or if POS suites include it free.
  2. Inspectors rarely ask for records.
  3. Regional acceptance of digital records is unverified.

#### IDEA-38 Returns and exchange portal with serial-returner rules for small online fashion shops
- **Type:** A (primary): cheaper and narrower than ShippyPro and Outvio. B secondary: rules for serial and late returners.
- **Buyer:** online SMEs selling clothing, footwear or electronics; the owner or e-commerce manager pays.
- **Sources:** G4-I02 (`stage2_G4_retail_services.md:454`).
- **Problem and product:**
  - 23.7% of non-food online orders were returned in 2025 (clothing 31%), worth €13.3bn (RET-11).
  - Serial returners (11% of shoppers) generate 23% of returns, and late returners another 24%.
  - Shoppers punish blanket return fees: 35% might stop buying, and only 21% would pay.
  - **The app** (Shopify, WooCommerce or PrestaShop): a branded returns portal, an exchange-first flow, return-reason capture and automatic enforcement of the return window.
  - A per-customer return score built only from the shop's own orders drives rules such as a paid return or inspection before refund. There are no cross-shop blacklists.
- **Key pains:** RET-11. Possible later modules: RET-12 and RET-14, both filtered as N1.
- **Why now:** no regulatory trigger. Volumes are high, and slow returns (9.1 days on average) tie up stock and cash.
- **Price hypothesis:** €19–39/month by order volume with no per-label fee, or about €0.50 per processed return for very small shops.
- **Evidence:** medium. The figures come from a returns-software vendor (ZigZag with Retail Economics); the cost per return is unknown.
- **Moat:** none, speed only.
- **Top risks:**
  1. Sendcloud (free plan; Lite at €28/month), Outvio or the platforms' own features already cover this.
  2. Very small shops lack the volume to care.
  3. Consumer law may limit charging only serial returners, or inspecting before refund (LEG-12).

#### IDEA-39 Commission-free direct booking for salons, with deposits and client-data import
- **Type:** A (primary): a cheaper, simpler alternative to Booksy and Treatwell for repeat clients. C secondary.
- **Buyer:** hair salons, barbers, and beauty and nail centres, mostly autónomos and micro firms (60% had a single worker in 2021). The salon count conflicts (section 5).
- **Sources:** G4-I04 (`stage2_G4_retail_services.md:555`).
- **Problem and product:**
  - Treatwell takes 25% of a new marketplace client's first booking, under a 12-month minimum contract.
  - Booksy charges €34.99/month plus €8 per extra staff member, and takes 30% of a new client's first visit through Boost (capped at €50) (RET-19).
  - Owners complain of commissions charged even when the client does not show, of unresponsive support and of difficult data export.
  - **The product:** a booking page linked from Google, Instagram and WhatsApp, and a calendar for 1–5 staff.
  - Deposits or card-on-file run at cost, with reminders plus free WhatsApp click-to-chat links.
  - It offers one-click import of Booksy, Treatwell or Koibox client exports, and rebooking prompts. It is not a marketplace.
- **Key pains:** RET-19, with RET-10 as a cost input.
- **Why now:**
  - Incumbents bundle payments and VeriFactu/TicketBAI invoicing to deepen lock-in.
  - VeriFactu is legally due in 2027 (October 2028 announced, not in the BOE), so salons may review their stack (inference).
  - WhatsApp API utility messages have been charged since 1 Oct 2026 (RET-10).
- **Price hypothesis:** €9–15/month flat for 1–3 staff, plus €3 per extra staff member; 0% commission; card fees passed through at cost.
- **Evidence:** medium. Prices come from vendor pages and a competitor's blog, and complaints from Capterra snippets; there are no no-show data.
- **Moat:** none, speed only. The researcher already calls the market crowded.
- **Top risks:**
  1. Salons stay on the marketplaces for discovery.
  2. Free booking tools that earn on payment fees are already common.
  3. Whether no-show deposits are legal under consumer law is unverified, and willingness to pay is low.

### Theme K. Health, care and education

#### IDEA-40 Private-pay and reimbursement-claim kit for self-employed health professionals
- **Type:** B.
- **Buyer:** micro clinics and self-employed health professionals, including:
  - psychologists (43,200 self-employed in Mar 2021);
  - physiotherapists, podiatrists, dietitians and speech therapists;
  - dentists and specialists on insurer panels.
- **Sources:** G4-I05 (`stage2_G4_retail_services.md:610`).
- **Problem and product:**
  - Insurers pay €5–20 per allied-health session and about €17–19 per specialist consultation, with sessions capped at 20–30 minutes; 88.76% of surveyed psychologists say the terms are imposed.
  - The top five insurers hold 71% of premiums, and competition law blocks collective bargaining (PRO-01, PRO-02).
  - **The kit:** a payer-mix calculator that imports practice-software exports and shows net € per hour by insurer and for private patients.
  - It adds a reimbursement pack for each private session, carrying the fields each insurer requires, with a patient guide.
  - It also provides templates for moving panel patients to private sessions. Nothing in it coordinates prices.
- **Key pains:** PRO-01, PRO-02.
- **Why now:**
  - The CNMC was formally asked for help in Mar 2026 and has not ruled.
  - The 2025 fee rises were marginal (Adeslas from €18 to €19; Asisa +6.5%).
  - The 2025–2027 MUFACE contract raised premiums by 41% while doctors were left out.
- **Price hypothesis:** €9–19/month per professional; member-benefit deals with colegios.
- **Evidence:** medium. The fee figures come mostly from interested parties, and no source shows demand for this tool.
- **Moat:** low to moderate. A maintained dataset of each insurer's reimbursement requirements, plus colegio distribution.
- **Top risks:**
  1. Few patients hold reimbursement-type policies.
  2. Patients refuse to pay up front.
  3. Professionals fear losing referrals, and deontological rules may limit the advertising.

#### IDEA-41 Staff qualification file for private health centres (RD 239/2026)
- **Type:** C (primary); B secondary.
- **Buyer:** owners or managers of authorised private health centres (dental, physiotherapy, psychology, aesthetic, podiatry, nutrition). Doctoralia's presence in 5,000 private clinics gives a floor.
- **Sources:** G4-I06 (`stage2_G4_retail_services.md:655`).
- **Problem and product:**
  - RD 239/2026, in force since 1 Jul 2026, requires every health centre to keep a personal file for every health professional, showing official qualification and specialty, and to inform new staff about safe practices.
  - Centres have six months to comply, so until about 1 Jan 2027 (the researcher's calculation) (PRO-09).
  - **The file:** a register of professionals with document upload, colegiación checks against public registers where available, and expiry reminders.
  - It adds safe-practice onboarding with e-acknowledgement, a one-click inspection dossier, and rule updates as the regions adapt the annexes (due about Jul 2027).
- **Key pains:** PRO-09.
- **Why now:** the deadline of about 1 Jan 2027 is ten weeks away. The royal decree is in force, so it is not lapse-prone.
- **Price hypothesis:** €5/month per centre for up to five professionals, plus €1 per extra; or €49 a year.
- **Evidence:** weak. The obligation is official, but there is no evidence on how clinics comply, how inspectors will check, or what clinics would pay.
- **Moat:** none, speed only, to beat the deadline.
- **Top risks:**
  1. The regions never inspect the files, or a folder is enough.
  2. Clinic-software vendors add it free before January.
  3. There are 17 different regional inspection regimes.

#### IDEA-42 Antibiotic-stewardship and PRESVET compliance file for small vet clinics
- **Type:** C (primary); B secondary.
- **Buyer:** companion-animal veterinary clinics (micro and small). About 16,460 companion-animal clinicians are registered in PRESVET (MAPA, May 2026, a search summary).
- **Sources:** G4-I07 (`stage2_G4_retail_services.md:698`).
- **Problem and product:**
  - Since 2 Jan 2025, every antibiotic prescribed or administered must be reported at least every 15 days, under A–D categories with antibiogram prerequisites. Fines run from €600 to €1.2M, and vets call the platform hard to use and unstable (PRO-05).
  - About 80% of reporting is automated through practice software. What remains is checking the category rules, keeping inspection evidence, and RD 767/2025's new duty to document antibiotic-reduction measures.
  - **The file:** a prescription rule-checker, an evidence store, a register of reduction measures and a 15-day reconciliation monitor.
  - Clinics that still type data in by hand can submit through the PRESVET web services.
- **Key pains:** PRO-05.
- **Why now:**
  - The PRESVET duty has applied since 2 Jan 2025, and RD 767/2025 (in force since 4 Sep 2025) added the reduction-measures duty.
  - A sanctions reform was reported "en trámite" in Mar 2025. If it was still pending on 6 Oct 2026, it lapsed with the dissolution, so the current fines probably stand.
- **Price hypothesis:** €9–15/month per clinic.
- **Evidence:** medium. The burden is well documented; the gap left for software is unclear, and the MAPA figures come from a search summary.
- **Moat:** moderate. Rule logic, a working PRESVET integration and colegio distribution.
- **Top risks:**
  1. The leading practice software (Qvet and others) already checks categories and keeps evidence.
  2. The market is small.
  3. There are few inspections or fines.

#### IDEA-43 Exam-readiness tracker and slot planner for driving schools
- **Type:** B.
- **Buyer:** autoescuelas, mostly micro and small, plus chains such as Autoescuela Lara (65 centres in Madrid).
- **Sources:** G4-I10 (`stage2_G4_retail_services.md:856`).
- **Problem and product:**
  - The DGT rations practical-exam slots through its CAPA allocation, which splits each office's capacity by schools' theory pass rates and candidate numbers (PRO-14).
  - Examiners do 12 tests a day, 46% of students fail their first practical, and waits run 1.5–5 months in Madrid.
  - When the DGT offered unlimited extra exams in 2026, schools presented under 10% of the students they had claimed, and the DGT says only 8% are ready.
  - **The tracker:** an instructor app scores each lesson against a rubric based on the DGT's exam criteria, and gives each student a readiness score and pass estimate.
  - It adds a dashboard for choosing whom to present, scheduling of lessons, cars and instructors, updates to waiting students, and an exportable list of ready students.
- **Key pains:** PRO-14.
- **Why now:** protests took place at every Andalusian DGT office on 17 Jul 2026, and the DGT's reinforcement plan is being extended (Barcelona from 13 Jun 2026). There are 130 new examiner posts.
- **Price hypothesis:** €29–59/month per school, plus €5 per instructor.
- **Evidence:** medium. The bottleneck is documented, but its size is disputed (section 5), and demand for readiness software is an inference.
- **Moat:** moderate, if outcome data accumulate across schools; otherwise copyable.
- **Top risks:**
  1. Schools earn money from extra lessons, so faster readiness may not suit them.
  2. CAPA may not reward pass rates, or may change.
  3. Driving-school software (not researched) may already do this.

#### IDEA-44 Route planning, visit verification and hours reporting for home-help (SAD) providers
- **Type:** B.
- **Buyer:** home-help (servicio de ayuda a domicilio, SAD) companies, from small regional operators to large groups, plus not-for-profits; the operations or coordination manager pays.
- **Sources:** G4-I11 (`stage2_G4_retail_services.md:901`).
- **Problem and product:**
  - Municipal SAD tenders cap the hourly price and fold travel, coordination, supervision and training into it, while collective-agreement wage rises push costs up (PRO-17).
  - In Vigo the price rose from €16.70 to €22 an hour, in a €49.5M three-year contract.
  - Unpaid travel and admin time come straight out of the margin, and at least 50% of SAD contracts must be full-time.
  - **The product:** daily route planning within visit windows, mobile check-in and check-out, monthly hours reports in each council's format, and a rota builder that checks the full-time share.
- **Key pains:** PRO-17.
- **Why now:** tenders are being re-priced for wage rises (Vigo, 2025). The accreditation targets run to 2029, and their regional transposition is unverified.
- **Price hypothesis:** €3–6 per carer per month, or €99–299/month per company.
- **Evidence:** weak. A handful of tenders, some from 2020–23, and one summary of a TED notice; no provider counts or software data.
- **Moat:** moderate. Council report formats and tender know-how.
- **Top risks:**
  1. Large operators already have systems, and small ones may not pay.
  2. Unions resist location tracking, and labour law limits it (LAB-01).
  3. Councils impose their own apps.

### Theme L. Transport, logistics and low-emission zones (ZBE)

#### IDEA-45 DeCA evidence vault and pre-departure check for small hauliers
- **Type:** C (primary). B secondary: carrier-side evidence capture, which issuance tools are not described as offering.
- **Buyer:** owners or office managers of road-freight carriers with 1–20 vehicles. There were 152,871 road-freight companies at the start of 2026, 61,716 of them in heavy transport. SME shippers, which are jointly liable, are a secondary buyer.
- **Sources:** G5-I01 (`stage2_G5_mobility_industry_cities.md:325`).
- **Problem and product:**
  - Since 5 Oct 2026, every domestic haulage service needs a compliant DeCA before departure (IND-01).
  - Drivers are fined €401–600 when a QR will not load, data are missing or the shipper's document is wrong. The haulier is "el eslabón más débil de la cadena" (the weakest link in the chain).
  - **When the carrier issues:** the product generates a compliant DeCA.
  - **When the shipper issues:** the driver scans its QR before leaving, and the app stores a hashed, timestamped copy and checks the fields by who is responsible for them.
  - It shows a "ready to leave" status, keeps the one-year archive, and offers an offline inspection mode and a one-click appeal pack.
- **Key pains:** IND-01. Its trip record also feeds IND-02, IND-04 and IND-06 in IDEA-46.
- **Why now:**
  - The rule has been in force since 5 Oct 2026, with live roadside fines (Ley 9/2025; Orden TRM/282/2026; Resolución DGTCF of 5 Jun 2026).
  - The Ministry waived only the download failures of 5–19 Oct.
  - Fenadismer warned about non-compliant and overpriced tools.
  - Authorities must accept eFTI only from 9 Jul 2027, so no superseding mandate is close.
- **Price hypothesis:** €6 per vehicle per month (€59/year), with an association discount to about €4; a bundle with IDEA-46 at €19/month.
- **Evidence:** strong. Official texts, association incident reports, a 750-respondent readiness survey and a ministry climb-down. Willingness to pay for evidence beyond issuance is unproven.
- **Moat:** weak. Treat it as a wedge into IDEA-46.
- **Top risks:**
  1. The Ministry or an association launches a free tool with evidence capture.
  2. The "desde 5 euros al mes" (from €5/month) price anchor makes acquisition cost unrecoverable.
  3. Shippers' platforms become the de facto standard.

#### IDEA-46 Haulier revenue recovery: automatic fuel-revision lines, detention claims and late-payment interest
- **Type:** B (primary). C secondary: the fuel-line generator alone could run as a low-touch add-on.
- **Buyer:** owners or administrators of carriers with 1–50 vehicles; transport gestorías as resellers.
- **Sources:** G5-I02 (`stage2_G5_mobility_industry_cities.md:377`).
- **Problem and product:**
  - The 2026 diesel shock raised haulage costs by about 30%, and the G index for heavy vehicles rose 44.6% by 1 Oct 2026.
  - The law makes the fuel revision automatic and itemised and fines payers who block it, yet many shippers resist or cut base rates (IND-02).
  - Carriers also lose statutory detention pay for lack of proof (IND-06), and finance clients for 52 days on average, with 38% of payers beyond 60 days (IND-04).
  - **Fuel line:** it pulls the weekly G index and puts the itemised revision line on each invoice.
  - **Detention:** geofenced dock arrival and departure records, with art. 22 detention claims drafted from them.
  - **Late payment:** due-date tracking with statutory interest, compensation and claim letters.
  - It also assembles evidence files for Fenadismer's complaint channel, and keeps a private shipper scorecard.
- **Key pains:** IND-02, IND-06, IND-04, using the IND-01 trip record.
- **Why now:**
  - RDL 9/2026, in force since 16 Apr 2026, made the line mandatory and itemised. Whether it and RDL 25/2026 were convalidated is unverified; the underlying indexation rule sits in Ley 15/2009 art. 38 itself.
  - Fenadismer opened its complaint channel on 13 Oct 2026.
- **Price hypothesis:** €19/month for up to 3 vehicles, plus €4 per extra vehicle; test a success fee on recovered detention and interest.
- **Evidence:** strong for the fuel line and late payment (BOE texts, Fenadismer's payment observatory); medium for detention (a single 2023 study).
- **Moat:** medium. An anonymised dataset of shipper behaviour that grows with every user, plus association distribution.
- **Top risks:**
  1. Carriers dare not bill the line for fear of losing clients: kill if 60% or more of interviewed hauliers would not add it even if automatic.
  2. A fall in diesel prices shrinks or reverses the line.
  3. CETM's calculator already does this free for members. Shipper scorecards also raise data-protection and defamation questions.

#### IDEA-47 ZBE vehicle checker, alerts and fleet permit ledger (from autónomo vans to SME delivery fleets)
- **Type:** C (primary): the autónomo tier at €4.99/month. B secondary: the fleet dispatch check; no Spanish ZBE-aware dispatch product was found.
- **Buyer:**
  - autónomos and micro firms with 1–5 vans: trades, small couriers, market and food suppliers;
  - dispatch managers at SME wholesalers and distributors, regional parcel subcontractors and multi-city service firms with 3–50 vans.
- **Sources:**
  - G5-I03 (`stage2_G5_mobility_industry_cities.md:429`);
  - G5-I04 (`stage2_G5_mobility_industry_cities.md:481`).

  Both build on IDEA-48's data layer.
- **Problem and product:**
  - Whether a van may enter depends on label, category, MMA, domicile, time, day type and permits. The answer changed repeatedly in 2026: Madrid on 7 Apr, Málaga on 14 Oct, and Barcelona's suspension (ZBE-01, ZBE-02).
  - Each wrong entry costs €200, and Madrid issued 261,115 unlabelled-access fines in H1 2025 (ZBE-10).
  - For in-zone stops the fine depends on which van goes, when and with which permit, not on the route. Dispatchers track Madrid Distrito Centro windows, per-plate registrations, night-delivery declarations and the quotas in Bilbao, Barcelona and Zaragoza by hand (ZBE-06, ZBE-07, ZBE-15, ZBE-16).
  - **Autónomo tier:**
    - instant "allowed / with permit / not allowed" answers per plate, with the rule's source;
    - change alerts and a personal phase-out calendar;
    - permit renewal reminders, quota counters and a fine tracker.
  - **Fleet tier:**
    - a fleet register (including rented vans) and a permit wallet;
    - a nightly check of tomorrow's stops from the route planner, with proposed fixes;
    - a quota log, plate-notification reminders and the yearly Madrid declaration pack.
- **Key pains:** ZBE-01, ZBE-02, ZBE-04, ZBE-06, ZBE-07, ZBE-09, ZBE-10, ZBE-12, ZBE-13, ZBE-14, ZBE-15, ZBE-16, ZBE-17, ZBE-23 (CITY-03 folded into ZBE-10).
- **Why now:**
  - Courts reshaped the largest schemes in 2026, and Madrid's Ordenanza 2/2026 regime has applied since 7 Apr 2026.
  - Switch-on and phase-out dates cluster around 31 Dec 2026 and 1 Jan 2027: Palma excludes label B, Madrid's resident warnings end, and Badalona's moratorium ends.
  - Catalonia must restrict label B before 2028, and Vigo fines from 10 Sep 2027.
  - Madrid's NO2-conditional regime for unlabelled vans could end on six months' notice.
  - Ordinances do not lapse with the election, but courts keep annulling them.
- **Price hypothesis:** autónomos €4.99/month or €39/year for up to 3 vans, with a free single check; fleets €9 per vehicle per month, minimum €49/month.
- **Evidence:** medium. Fragmentation and volatility are strongly evidenced by official pages and direct parsing of the NAP feed; the business share of fines and willingness to pay are unknown, and fleet demand is inferred.
- **Moat:** medium-low for the app. The hard part is the versioned, legally checked rulebook (shared with IDEA-48) and route-planner integrations.
- **Top risks:**
  1. Owners keeping old vans until they exit will not pay: kill if a 4-week pilot converts under 3% of free checkers.
  2. Route planners (HERE, TomTom, PTV, Webfleet) add Spanish ZBE semantics, or free apps (ZBE España, the Astac/RACC site) add alerts.
  3. Enforcement softens: none in Valencia, disputed in Zaragoza.

#### IDEA-48 EcoRoute reshaped: Spanish ZBE rules and in-zone compliance-check API [user idea U3]
- **Type:** B (primary). A secondary: an SME-affordable alternative to enterprise LEZ data from HERE and TomTom, whose prices are unknown.
- **Buyer:**
  - software firms serving Spanish fleets: route planners, TMS, telematics and fleet management;
  - navigation and mobility apps;
  - renting, leasing and van-rental firms, and fleet insurers;
  - logistics operators with in-house dispatch;
  - associations and media, through data licences.
- **Sources:**
  - G5-I09 (`stage2_G5_mobility_industry_cities.md:715`);
  - the U3 assessment and verdict (`stage2_G5_mobility_industry_cities.md:694` and `:708`);
  - U3 as given (`00_user_supplied_ideas.md:32`).
- **Problem and product:**
  - About 150 obliged municipalities have rules that diverge and change at short notice (ZBE-01, ZBE-02).
  - The free national NAP feed is (ZBE-03):
    - incomplete: no Zaragoza, Vigo, Córdoba, Murcia or Las Palmas;
    - stale: Valencia is shown "active" with no ZBE in force, and Málaga is still "active" after fines stopped;
    - thin: no vehicle category, MMA, domicile, quotas, phase dates or episodes.
  - City portals publish only perimeters. HERE and TomTom model Euro classes, not DGT labels or local exemptions, and routing cannot avoid penalties for in-zone stops (ZBE-15, ZBE-18, ZBE-20).
  - **The API:** a versioned rules dataset in which every rule carries its source, effective dates and legal status (in force, annulled but not final, suspended, information phase).
  - **Endpoints:**
    - zones;
    - check: vehicle at stop at time T, returning allowed, allowed with permit or not allowed, with the reason and the source;
    - options;
    - a changes webhook;
    - label mapping;
    - historical versions, for fine disputes.
  - **MVP:** the 10 sanctioning or access-control cities.
  - **Dropped from U3:** "green routing avoids penalties", and Valencia as a launch market. Valencia stays only as a Sandbox or port pilot.
- **Key pains:** ZBE-01, ZBE-02, ZBE-03, ZBE-04, ZBE-09, ZBE-15, ZBE-18, ZBE-19, ZBE-20, ZBE-23 (CITY-12 and IND-08 folded in).
- **Why now:**
  - Courts reshaped the largest schemes in 2026, and the NAP files (stamped 8 Jul 2026, or 31 Jul for Valencia) contain contradictions.
  - A datos.gob.es request for a national table has gone unanswered since Nov 2025.
  - Label-B phase-outs arrive in Palma and Catalonia in 2027–2028.
  - Nascent developer tools suggest demand and a short window: @cargoffer/zbe-mcp (first seen Jul 2026) and an Apify LEZ actor.
- **Price hypothesis:**
  - a free developer tier of 100 checks a day;
  - €149/month for 10,000 checks and €499/month for 100,000, plus an enterprise data licence;
  - €0.20–0.50 per vehicle per month for renting firms.
- **Evidence:** medium. The data gaps are strongly evidenced by direct inspection of the NAP and city portals; demand from integrators is inferred from nascent tools.
- **Moat:** medium. The curated, versioned legal-status history, the monitoring routine and integrations inside partners' products. AI lowers the cost of a first scrape but not of staying current and standing behind the answers.
- **Top risks:**
  1. Few paying integrators: kill if fewer than 5 of 20 fleet-software vendors would pay €149/month or more.
  2. HERE, TomTom or a Spanish telematics leader adds DGT-label, domicile and quota semantics, or the DGT enriches the NAP model (a kill criterion).
  3. Liability for wrong answers, each potentially a €200 fine.

### Theme M. Packaging, food-chain and farm compliance

#### IDEA-49 Packaging EPR, PPWR and plastic-tax compliance kit (online sellers, importers, food and drink firms, small manufacturers)
- **Type:** B (primary). C secondary: once the catalogue is set up, the yearly declaration runs largely on autopilot.
- **Buyer:**
  - SMEs that pack goods or first place packaged goods in Spain: online shops, importers and intra-EU buyers (G4-I03);
  - the compliance or admin manager at food and drink SMEs (27,300+ companies, FIAB) and other small manufacturers (G5-I07);
  - white-label partners: collective schemes, gestorías and ERP vendors.
- **Sources:**
  - G4-I03 (`stage2_G4_retail_services.md:500`);
  - G5-I07 (`stage2_G5_mobility_industry_cities.md:618`).
- **Problem and product:**
  - Producers must register, join a collective scheme, declare packaging tonnes by material before 31 March each year (simplified below 15 t), show scheme fees on invoices and mark their packaging. Commercial and industrial packaging has been under EPR since end-2024, and since 12 Aug 2026 the PPWR adds declarations of conformity (RET-15, IND-12).
  - Importers above 5 kg a month of non-recycled plastic must also keep a stock ledger and file modelo 592 (RET-16), food firms with 10+ staff or over €2M turnover need a food-waste plan (IND-25), and distributors may only sell registered producers' goods.
  - **The kit:** a packaging bill of materials per SKU, built from templates, an ERP or Shopify import, or AI extraction from supplier spec sheets. From it the kit produces tonnage by material (household against commercial or industrial), the 31 March declaration and invoice fee lines, PPWR declarations of conformity, a modelo 592 worksheet and a supplier registration-number tracker.
  - **Modules:** a Ley 1/2025 food-waste plan now; EUDR and CBAM supplier data later.
- **Key pains:** RET-15, RET-16, IND-12, IND-25 (later IND-13 and IND-14).
- **Why now:**
  - The PPWR, an EU regulation, has applied since 12 Aug 2026.
  - The RD 1055/2022 deadlines for schemes (31 Dec 2024) and marking (1 Jan 2025) have passed, and the next declaration is due before 31 Mar 2027.
  - The AEAT updated its plastic-tax page on 20 Oct 2026.
  - EUDR applies from 30 Dec 2026 for large and medium operators and from 30 Jun 2027 for micro and small ones, after two postponements.
  - The Dec 2025 Environmental Omnibus is only a proposal.
- **Price hypothesis:** €19–49/month by number of products, or €149–299 per declaration season (G4-I03); €39/month (€390/year) per company, with the food-waste module at +€10/month (G5-I07).
- **Evidence:** medium. The rules are strong (BOE, AEAT, a scheme's commentary); the burden, fees and sanctions were not captured.
- **Moat:** moderate. Regulatory know-how, scheme or gestoría partnerships, and a growing library of verified supplier registration numbers and packaging specs.
- **Top risks:**
  1. Collective schemes (Ecoembes, GENCI, Cartón Circular) give members free declaration tools (a kill criterion).
  2. Many small sellers sit in the simplified regime or below 5 kg a month.
  3. Enforcement is unknown, and the PPWR's main obligations are dated 2030, so urgency is low.

#### IDEA-50 RCA autopilot: food-contract generation and registration before delivery (wine harvest first)
- **Type:** B.
- **Buyer:** purchasing or admin managers at food-industry SMEs that buy from farmers (wineries, fruit and vegetable packers, meat and dairy processors), at origin wholesalers, and at cooperatives buying from non-members. The pool: 27,300+ food and drink firms, 3,669 cooperatives and 950+ FEV wineries.
- **Sources:** G5-I05 (`stage2_G5_mobility_industry_cities.md:527`).
- **Problem and product:**
  - Every purchase from a farmer needs a signed written contract with minimum terms and a price above the producer's costs, registered in the RCA before delivery (IND-18).
  - In 2025 AICA sanctioned 991 infractions; 506 were failures to register, and 619 were in wine, 616 of them on wine grapes. Fines reach €100,000, and serious fines are published (IND-18, IND-19).
  - **The autopilot:** contract templates with a cost-of-production clause, signed by mobile link.
  - Bulk registration runs through the RCA API, triggered by a purchase order or weighbridge ticket and confirmed before the load is accepted.
  - It re-registers amendments automatically, alerts payment terms, and keeps a per-grower evidence file and an inspection pack.
- **Key pains:** IND-18, IND-19, IND-21.
- **Why now:**
  - AICA's 2025 report (24 Sep 2026) shows record enforcement. Ley 12/2013 is in force.
  - AICA opened consultation on a new inspection decree on 30 Sep 2026; it is a draft and may stall with the election.
  - The 2026 input-cost shock makes the price-above-cost clause more contentious.
- **Price hypothesis:** €39/month for up to 300 contracts a year and €99/month for up to 3,000, or a €149 harvest-season pass for small wineries.
- **Evidence:** strong. Official enforcement statistics and legal texts. That the wine infractions are mostly unregistered harvest contracts is the notes' inference.
- **Moat:** medium. The RCA integration, weighbridge and ERP connectors, reliability at harvest peaks, association endorsement and the contract archive.
- **Top risks:**
  1. Winery and agri ERPs already integrate the RCA API at no extra cost (a kill criterion).
  2. AICA improves its own bulk upload.
  3. Many buyers are tiny and seasonal (kill if buyers spend under an hour per season on the RCA), and cooperatives buying from their members are exempt.

#### IDEA-51 Fertilisation-plan and nutrient-record workspace for advisers and cooperative technical services
- **Type:** B (primary). A secondary, if validation finds priced farm-notebook apps to undercut.
- **Buyer:** REGFER-registered fertilisation advisers, cooperatives' technical services and larger farms (3,669 cooperatives with more than 1M member families).
- **Sources:** G5-I06 (`stage2_G5_mobility_industry_cities.md:578`).
- **Problem and product:**
  - Since 1 Sep 2026, non-exempt farms need a plan de abonado and must log each fertilisation within a month. Advisers have had to register in REGFER since 1 Jul 2026 (IND-20).
  - Agronomic advice becomes mandatory one year later in vulnerable zones and two years later elsewhere.
  - The digital farm notebook (CUE) is postponed to the next CAP period, and the sector calls the burden "inasumible" (unbearable).
  - **The workspace:** a multi-farm space for one adviser, with parcels, crops and soil analyses, and a plan generator following RD 1051/2022.
  - Farmers log each application by mobile or WhatsApp, with reminders, and the adviser signs off.
  - It exports to SIEX and regional formats, on a data model ready for the CUE.
- **Key pains:** IND-20.
- **Why now:**
  - The duties have been live since 1 Jul and 1 Sep 2026; RD 1051/2022 is in force.
  - Mandatory advice follows in 2027–2028 (an inference).
  - Bureaucracy is a headline demand of the 28 Oct 2026 tractor protest.
- **Price hypothesis:** €39/month per adviser for up to 25 farms, plus €1.50 per extra farm per month.
- **Evidence:** medium. The obligations are official; the burden is described rather than quantified, and competitors are unpriced.
- **Moat:** low to medium.
- **Top risks:**
  1. The free public software or the Cuaderno de Campo Cooperativo already generates plans (a kill criterion).
  2. The eventual CUE design forces a rebuild.
  3. Advisers are few and price-sensitive.

### Theme N. Immigration and relocation

#### IDEA-52 PermisoFast reshaped: co-pilot for UGE talent cases, for immigration law firms and their agency partners [user idea U2]
- **Type:** B (primary). A secondary: it cuts paralegal hours per case and lets agencies buy fixed-price filing from partner firms.
- **Buyer:** immigration law firms and gestorías that handle UGE cases; the roughly 110 relocation agencies that need a partner filer; EOR and mobility providers.
  - Firms named in the notes: Lexidy, Klevvera, Polaris Extranjería, Platinum Legal Spain, Latitude Law and Lexmovea.
- **Sources:**
  - G6-I12 (`stage2_G6_expat_startups_gaming.md:558`);
  - the U2 assessment (`stage2_G6_expat_startups_gaming.md:542`);
  - U2 as given (`00_user_supplied_ideas.md:23`).
- **Problem and product:**
  - The UGE decides in 20 days, with silence counting as approval, but only if the evidence holds: company age and prior relationship, bank statements that match payslips or invoices, insurance with no copayments, income thresholds that reset with SMI and INE data, and ENISA's report for founders (EXP-08, EXP-09, STA-09).
  - Mismatches trigger document requests or denials, on cases where clients pay €900–3,900 for law-firm packages and €2,940–7,850 in first-year costs (EXP-08).
  - **The co-pilot:** a multilingual client intake portal, a month-by-month reconciliation of deposits against payslips or invoices, an insurance-clause checker, a threshold calculator, and an indexed file and cover memo for the lawyer, with alerts from IDEA-54's rule feed.
  - **It does not** file, book appointments, scrape portals or advise applicants without the firm. **Dropped from U2:** anything near appointment booking, "regional portals" (the sources are national), and HR teams or agencies as the filing buyer.
- **Key pains:** EXP-08, EXP-09, EXP-07, EXP-06, EXP-05, EXP-22, STA-09 (STA-10 merged).
- **Why now:**
  - UGE practice tightened in 2025–26 (Polaris; Anchorless, a single commercial source).
  - Thresholds were updated in June 2026 after INE's release of 28 May, and the 2026 minimum wage (RD 126/2026, per Anchorless) moves the DNV income line to €2,849 a month.
  - The DNV stock is growing. The rules are regulations and ministerial criteria, which a new government could amend.
- **Price hypothesis:** €30 per case, or €199/month per firm for 15 cases; an agency hand-off fee shared with partner firms.
- **Evidence:** medium. The stock data are official; the evidence-scrutiny pain comes from law-firm and vendor sources.
- **Moat:** low-moderate. The rules plus an outcome dataset (which evidence gaps led to document requests), and integration into firms' intake. GestoLab or Cicerai could extend into UGE cases.
- **Top risks:**
  1. There are few law firms, and they may see file preparation as their own value. Kill if fewer than five run a paid pilot, or if reconciliation does not measurably cut document requests.
  2. Financial and identity data are highly sensitive, so security due diligence, processor agreements and EU hosting are needed.
  3. It must stay a professional's tool, because representation is reserved, and pre-checks offered directly to applicants may raise legal-advice questions.

#### IDEA-53 Renewal-wave case manager for immigration filers (2027 regularisation renewals)
- **Type:** B (primary). A secondary: narrower and possibly cheaper than general co-pilots for high-volume, low-fee files.
- **Buyer:** the habilitated filers who carried the 2026 regularisation:
  - law firms (58% of 977,876 e-filings), gestores administrativos (8.4%) and graduados sociales (3.6%);
  - union and NGO collaborators (5.1%).

  Known counts: 5,925 ICAM lawyers on Mercurio, about 2,000 immigration lawyers in Catalonia, and 495 third-sector and union entities.
- **Sources:** G6-I01 (`stage2_G6_expat_startups_gaming.md:217`). It shares its document-validation engine with IDEA-52.
- **Problem and product:**
  - The regularisation brought 1,174,978 applications in ten weeks, and every initial permit lasts one year (EXP-03).
  - Renewals therefore bunch up in 2027 (up to about 1M, by the notes' inference) on the same offices, police units and fragile Mercurio platform (EXP-23).
  - Filers earn €100–400 per file, and data errors trigger 10-working-day correction requests or break the TIE stage (EXP-07).
  - **The case manager:** it imports a filer's 2026 client roster and receipts, computes each client's renewal date and window, and sends clients multilingual upload links.
  - It extracts and cross-checks data from passports, TIEs, contracts, payslips and Social Security records against the 2026 file, and flags outdated form versions.
  - It outputs an editable EX form and a numbered package for manual upload to Mercurio.
- **Key pains:** EXP-03, EXP-07, EXP-22, EXP-23.
- **Why now:**
  - RD 316/2026 is in force. Filing closed on 30 Jun 2026 and resolutions are still being issued, so the first renewals fall due from mid-2027 (to confirm).
  - The election slows new decrees, but DGGM criteria keep arriving, and a new government could change the renewal rules.
- **Price hypothesis:** €3–5 per active renewal case, or €49/month (solo) to €149/month (office) with case quotas; an at-cost tier for NGOs.
- **Evidence:** medium. The surge, the filer shares and the one-year validity are official; the 2027 volume is an inference, and error rates are not published.
- **Moat:** low to moderate. Switching costs once a filer's roster lives in the tool, colegio distribution, and an outcome dataset.
- **Top risks:**
  1. Renewal of the DA 20/21 permits turns out to be simplified or automatic.
  2. GestoLab ships bulk renewals at around €1 per case (pivot to the NGO tier).
  3. Filers on €100–400 fees refuse per-case pricing, and processing criminal-record data creates liability.

#### IDEA-54 Extranjería rule and form-version radar, tagged by procedure
- **Type:** C (primary). B secondary: a knowledge base of each office's practice.
- **Buyer:** immigration lawyers, extranjería gestorías, graduados sociales, about 110 relocation companies, and corporate mobility teams.
- **Sources:** G6-I02 (`stage2_G6_expat_startups_gaming.md:254`). It is a free wedge and data feed for IDEA-52 and IDEA-53.
- **Problem and product:**
  - At least 20 rule and practice changes hit expat procedures between May 2025 and Oct 2026 (EXP-06), through:
    - BOE decrees and orders;
    - DGGM criteria and SEM instructions;
    - UGE threshold notes and two Supreme Court rulings;
    - a police pilot that surfaced only as a bar-association PDF.
  - Outdated EX forms cause correction requests, and offers below the June 2026 thresholds (€41,356.36 / €33,085.09) lead to denials (EXP-05, EXP-09).
  - **The radar:** it watches a fixed list of national sources and turns each change into a three-line note tagged by procedure, province, effective date and type.
  - It sends instant or weekly alerts and runs a threshold watch. Later, it adds office-practice notes from verified professionals.
- **Key pains:** EXP-06, EXP-05, EXP-09.
- **Why now:** the Supreme Court annulments were published on 22 Sep 2026. With the Cortes dissolved, decrees pause, but DGGM criteria and police practice keep changing; a new government in 2027 may amend the Reglamento (inference).
- **Price hypothesis:** a free weekly digest; €9/month per seat; €29/month per team.
- **Evidence:** strong for the pace of rule changes; weak for willingness to pay.
- **Moat:** none, speed only. The only lasting assets would be a curated office-practice archive and a professional community.
- **Top risks:**
  1. Free newsletters and colegio circulars are enough: kill if under 5% of free subscribers convert within three months.
  2. Ministry pages returned 403 to automated fetching, so source access is at risk.
  3. Liability for wrong summaries; DGGM criteria "carecen de valor normativo" (have no normative force), so they must be presented as practice, not law.

#### IDEA-55 Expected-decision-time tracker for each Extranjería office and procedure
- **Type:** B (primary). C secondary: a €3/month alert on a personal file.
- **Buyer:** HR and mobility teams setting start dates, about 110 relocation companies, immigration law firms, individuals and families with pending files, and university international offices.
- **Sources:** G6-I03 (`stage2_G6_expat_startups_gaming.md:281`).
- **Problem and product:**
  - The same procedure takes 12 days in one office and 232 in another: an initial employee permit in Baleares against Valencia, Oct 2026 (EXP-04, EXP-16, EXP-19).
  - Barcelona, the biggest talent hub, publishes nothing, and neither do Málaga, Alicante and the two Canarias offices.
  - **The tracker:** it turns the monthly resolution-date PDFs of Madrid, Valencia and Baleares into time series.
  - For offices that publish nothing, it collects anonymised data points, give-to-get for professionals and through a free tracker for applicants.
  - It shows an expected decision window and alerts on filing dates and legal deadlines, flagging the reunification-deadline conflict (section 5). HR teams get dashboards and an API.
- **Key pains:** EXP-04, EXP-16, EXP-19.
- **Why now:** queues swing with the regularisation load and with Catalonia's emergency plan, and the 2027 renewal wave will move them again. Only 3 of the 8 target offices publish data.
- **Price hypothesis:** HR or agency plans at €29–49/month, or €5 per tracked employee per month; personal alerts at €3/month or €19/year; public charts free.
- **Evidence:** medium. The source tag is "medium-high": official PDFs (through one compiler) show the spread, but HR demand is inferred.
- **Moat:** the group's best data moat if seeded early: a crowdsourced dataset with network effects. The PDF part alone could be copied in a weekend.
- **Top risks:**
  1. Too few contributions: kill if there are fewer than 200 Barcelona data points in three months.
  2. The official file-status service already shows expected dates.
  3. HR does not plan offers or start dates around office timing (a kill test from 15 interviews).

#### IDEA-56 Spain relocation orchestrator for HR teams and relocation agencies
- **Type:** B (primary). A secondary: lets HR do the simple steps in-house instead of buying €1,200–3,500 relocation packages.
- **Buyer:** People and HR teams hiring non-EU staff, about 110 relocation companies, and EOR and mobility providers. The employer-sponsored stock is about 58,000 permits, concentrated in Barcelona (53,700 UGE permits) and Madrid (41,680).
- **Sources:** G6-I04 (`stage2_G6_expat_startups_gaming.md:311`).
- **Problem and product:**
  - After the permit comes a chain of appointments: the padrón, TIE fingerprints (weeks to months), the card 30–45 days later, and the FNMT certificate only once the TIE exists.
  - Meanwhile personal clocks run: modelo 149 within six months, the six-month driving-licence clock, blocked travel while an initial application is pending, and family files that take 62–184 days.
  - HR stitches together agencies, lawyers, tax advisers and translators at about €2,000–6,000 of admin per move, by the notes' synthesis (EXP-01, EXP-10, EXP-12, EXP-13, EXP-16, EXP-17, EXP-21, EXP-22).
  - **Per-employee case:** Spain-specific step templates by route.
  - **Deadline engine:**
    - the Beckham clock, counted from the Social Security registration date;
    - the driving-licence clock by country;
    - the 20-day TIE auto-assignment window;
    - an EX-13 check before trips, and renewal dates.
  - **Supporting tools:** a document vault, family sub-cases, a fixed-price vendor panel, a hand-off package for the chosen habilitated filer, and an English view for the employee.
- **Key pains:** EXP-01, EXP-10, EXP-12, EXP-13, EXP-16, EXP-17, EXP-21, EXP-22.
- **Why now:** since 8 Oct 2026 the police auto-assign fingerprint appointments for 10% of resolved files in six provinces, with a 20-day window. The Instrucción 1/2026 travel relief expired on 30 Sep 2026, and UGE thresholds changed in June 2026.
- **Price hypothesis:** for HR, €39 per active case per month or €249 per completed move; for agencies, €199/month white-label plus €15 per case.
- **Evidence:** medium.
- **Moat:** moderate-low. A Spain-specific step graph kept current, office timing data from IDEA-55, and agency distribution.
- **Top risks:**
  1. HR prefers to outsource everything to an agency.
  2. Too few companies have recurring volume: kill if fewer than 10 HR teams in Barcelona and Madrid make at least five non-EU moves a year.
  3. Jobbatical or Deel is good enough.

#### IDEA-57 Work-permit expiry and renewal monitor for employers of foreign workers
- **Type:** C (primary). B secondary: a multi-client board for gestorías and immigration lawyers.
- **Buyer:** employers of non-EU workers in agriculture, hospitality, care (including domestic employers), construction and logistics, especially SMEs that hired regularised workers; and the gestorías laborales, graduados sociales and immigration lawyers who handle their files.
- **Sources:**
  - G2-I05 (`stage2_G2_labour_legal_admin.md:688`);
  - G6-I05 (`stage2_G6_expat_startups_gaming.md:351`).
- **Problem and product:**
  - In 2025 the Labour Inspectorate found 18,655 foreign workers without authorisation (+53.1%) and proposed €187.7M in fines, about €10k per worker by inference (LAB-08).
  - Every regularisation permit lasts one year, so the hundreds of thousands of workers hired in 2026 must renew in 2027 through saturated offices. A late renewal can take a worker off the rota (EXP-03, EXP-01, ADM-10).
  - **Register:** each worker's authorisation type, expiry and conditions, from a list import or a photo of the TIE (read by OCR).
  - **Alerts:** multilingual reminders to worker and employer at 120, 90, 60 and 30 days; renewal-receipt (resguardo) upload, with flags for workers who have none.
  - **Evidence:** office-specific checklists kept with partner professionals, and a log of the employer's checks as inspection evidence.
  - **Gestoría board:** one view across all clients.
- **Key pains:** LAB-08, ADM-10, EXP-03, EXP-01, EXP-22.
- **Why now:**
  - RD 1155/2024 has applied since about 20 May 2025, with challenges pending at the Supreme Court.
  - The RD 316/2026 window closed on 30 Jun 2026, and its permits last one year.
  - There were 3,038,158 foreign Social Security affiliates in Jan 2026, and 337,917 regularised affiliates by end-Aug 2026.
- **Price hypothesis:**
  - €5/month for up to 5 foreign workers, then €1 per extra worker (G2-I05); or €2 per worker per month with a €5 minimum (G6-I05);
  - a gestoría or lawyer board at €29/month for up to 100 workers, or white-label at €1 per worker per month.
- **Evidence:** medium. The fine and regularisation figures are official; the employer-side pain is inferred, and employer counts are unverified (section 5).
- **Moat:** none to low. Office checklists and distribution through professionals.
- **Top risks:**
  1. Employers see renewal as the worker's problem. Kill thresholds: under a third report a lapse or worry (G2), or under 20% track expiries at all (G6).
  2. HR and payroll suites add expiry alerts.
  3. A lawful basis is needed for holding TIE copies and contacting workers, and the product must stay clear of representation.

#### IDEA-58 Beckham-regime filing kit and six-year tracker
- **Type:** A (primary): a guided, much cheaper alternative to adviser filings at €500–1,500. C secondary: a tracker at about €5/month for the annual modelo 151.
- **Buyer:**
  - relocating employees and executives (47,190 executives and highly qualified, 6,083 Blue Card holders, 4,592 intra-company transfers);
  - founders (4,818 entrepreneur permits) and eligible digital nomads;
  - HR teams paying for it as a relocation benefit, and agencies as white-label.
- **Sources:** G6-I06 (`stage2_G6_expat_startups_gaming.md:378`).
- **Problem and product:**
  - The regime taxes employment income at a flat 24% up to €600,000, for the year of the move plus five, but only if modelo 149 is filed within six months of Social Security registration. Vendors describe late filings as final (EXP-10).
  - Advisers charge €500–1,500 for one person or €800–2,200 for a family, and newcomers often lack the certificate or Cl@ve needed to file themselves (EXP-12).
  - **The kit:** an eligibility check (five-year non-residence look-back, employment or startup route, the 40% rule), a deadline clock from the registration date, and modelo 149 pre-filled from the contract.
  - It adds a filing guide or a fixed-price hand-off to a partner adviser, a withholding letter for the employer's payroll, and five years of modelo 151 reminders.
- **Key pains:** EXP-10 (STA-11 merged), EXP-12.
- **Why now:**
  - Ley 28/2022 widened eligibility.
  - The DNV stock grew from 27,875 (Dec 2024) to 44,966 (Sep 2025), an indicative comparison only.
  - A TEAC criterion now requires imputing deemed rental income on the main home.
  - There was no legislative change in 2025–26, so the rules are stable enough to encode.
- **Price hypothesis:** €149 per person for the kit (+€99 for an optional adviser review); €4.99/month or €49/year for the tracker; €99 per employee in bulk for employers.
- **Evidence:** medium. "No extension" and rising rejections are vendor claims, and the market size (about 37,000 users over a decade) is single-source.
- **Moat:** none.
- **Top risks:**
  1. A small market: kill if AEAT data show fewer than about 3,000 new 149 filings a year.
  2. TaxDown or another app already offers guided filing at €99 or less (a kill criterion).
  3. Tax-advice liability and the rules on filing for someone else; newcomers without a TIE may be unable to file.

### Theme O. Startups

#### IDEA-59 Ley de Startups benefits keeper (certification, angel certificates, ESOP clock)
- **Type:** C (primary). B secondary: certificate generation.
- **Buyer:** certified startups (2,046 held the status on 11 Oct 2026; 2,529 have ever been certified) and startups that could qualify (more than 5,000 active), reached through founders or finance leads, with advisers and gestorías as a channel.
- **Sources:** G6-I07 (`stage2_G6_expat_startups_gaming.md:405`).
- **Problem and product:**
  - Every Ley de Startups perk depends on keeping a certification that 483 of 2,529 companies (about 19%) have already lost (STA-01). The perks:
    - 15% corporate tax instead of 25%;
    - a 50% angel deduction on a €100,000 base;
    - a €50,000 ESOP exemption;
    - relief from forced dissolution, and points in council calls.
  - Each angel needs a certificate from the company and must hold the shares for 3–12 years. ESOP tax falls due after 10 years even without an exit, and online guidance contradicts the BOE (STA-02, STA-20).
  - **The keeper:** an eligibility checker, plus monitoring of the age limit, the €10M turnover cap, the 60% Spanish-contract rule and dividend events, fed from accounting and payroll exports.
  - It generates an angel certificate for each investor from an imported cap table, and tracks holding windows and each ESOP grant's 10-year tax date.
- **Key pains:** STA-01, STA-02, STA-20.
- **Why now:** about 600 new certifications in the eight months to Oct 2026, and ENISA says investors increasingly ask for it. The law is unchanged since 22 Dec 2022 with no reform bill, so the rules are stable to encode.
- **Price hypothesis:** €9/month or €90/year per company; an adviser plan at €49/month for 20 client companies.
- **Evidence:** medium. The facts are high-confidence (BOE, ENISA); demand is inferred.
- **Moat:** none.
- **Top risks:**
  1. Low willingness to pay, since ENISA's guide is free.
  2. Most status losses may be unavoidable ageing-out, so monitoring adds little.
  3. ENISA adds monitoring to its portal (a kill criterion), and the market is small.

#### IDEA-60 Public-funding readiness and post-award tracker for startups (ENISA, CDTI, regional agencies)
- **Type:** B (primary). A secondary: cheaper than consultants' preparation and fractional-CFO hours.
- **Buyer:** pre-seed to Series A startups and spin-offs, with accelerators and startup gestorías as resellers. By end-2024 ENISA had made about 9,000 loans to 7,800 companies.
- **Sources:** G6-I08 (`stage2_G6_expat_startups_gaming.md:432`).
- **Problem and product:**
  - ENISA loans (€25k–€1.5M) require own funds at least equal to the loan, the main reason for refusal, and take 3–6 months (STA-04).
  - Neotec runs one call a year with capital and budget minimums and pays after 6–9 months. CDTI loans are often refused because the technical report is weak.
  - Lines keep changing, so founders pay advisers, or a fractional CFO at €750–2,000 a month.
  - **The tracker:** it imports the accounts and computes own funds against the target loan (including accumulated losses) and the capital increase needed.
  - It checks each line's rules and keeps a calendar of ENISA, CDTI, Neotec, EIC and regional agency lines.
  - It provides application checklists and templates and, after an award, tracks reporting and justification dates.
- **Key pains:** STA-04.
- **Why now:** ENISA restructured its offer into five lines in 2026, and the €303M FEPYME fund's window closed on 31 Aug 2026. The next Neotec call is around May–June 2027, and a caretaker government after 29 Nov may delay new calls.
- **Price hypothesis:** €29/month, or €149 per application pack.
- **Evidence:** medium. Several sources agree, but the timings come mainly from advisers.
- **Moat:** low. A user-contributed dataset of outcomes by line would be the only defensible asset.
- **Top risks:**
  1. Companies apply at most once a year, so churn is high.
  2. Consultants bundle preparation into success fees.
  3. ENISA or consultants start offering free pre-checks: kill if there are fewer than 50 paying startups after six months.

#### IDEA-61 R&D-credit evidence tracker and cash-refund pack for loss-making startups
- **Type:** B (primary). A secondary: potentially cheaper than R&D tax consultancies, whose fees are not in the notes.
- **Buyer:** R&D-intensive startups (deeptech, biotech, AI), especially loss-making ones. In Catalonia, about 2,100 of 2,403 startups invest in R&D (inferred from 89%).
- **Sources:** G6-I09 (`stage2_G6_expat_startups_gaming.md:459`).
- **Problem and product:**
  - R&D credits of 25–42% (12% for technological innovation, plus 17% for researcher staff, up to 59% in total) can be paid out in cash at a 20% discount when no tax is due (STA-05; the rules come from a single source).
  - Yet a common mistake is to drop the credits because the company is losing money. Claims need project documentation, staff-time records and ideally a binding R&D certificate.
  - **The tracker:** a register of R&D projects with weekly time-allocation prompts (Slack or email at first, later Jira or GitHub), and a payroll import to compute the eligible base.
  - It estimates the cash refund, and produces evidence packs and a technical-report outline. It reminds the user before the July corporate-tax deadline.
- **Key pains:** STA-05.
- **Why now:** seed funding fell three years in a row and Series A is flat (STA-03, context), so non-dilutive cash matters more. The credits can be cashed in without competing in a call.
- **Price hypothesis:** €79/month, or €49/month plus a small fee per evidence pack; a partner plan for consultants.
- **Evidence:** medium. The rule details are single-source; R&D intensity is well sourced (ACCIÓ).
- **Moat:** moderate. Know-how on the binding-certificate process, integration data and consultant partnerships.
- **Top risks:**
  1. Consultants already do the evidence work for a success fee.
  2. The rules differ from the single source.
  3. Liability if a claim fails.

### Theme P. Games, creators and streaming

#### IDEA-62 Spanish-language creator matching and key-campaign tracker for indie game studios
- **Type:** B (primary): a SaaS tool for game studios, not a game. C secondary: always-on detection of streams of a studio's titles.
- **Buyer:** Spanish micro-studios that self-publish on Steam: about 440 of 815 studios bill under €200k (inference), 55% self-publish and 82% of PC-focused studios rely on Steam. Later, Latin American studios.
- **Sources:** G6-I11 (`stage2_G6_expat_startups_gaming.md:513`).
- **Problem and product:**
  - Steam receives about 19–20k releases a year. Half of 2025's releases got fewer than 10 reviews, and 40% earned under $100 (GAM-24).
  - Streamers made the 2024–26 breakout hits (GAM-10).
  - Spanish is Twitch's fifth language, at 19.5M hours a week, but 90% of streams average three or fewer viewers, so finding the right mid-tier creators is the hard part (GAM-06, GAM-09). Kick's Spanish audience is mostly Latin American (GAM-08).
  - **The tool:** a searchable index of Spanish-language Twitch and Kick creators, by categories streamed, average viewers (with viewbot flags), country and schedule.
  - It handles outreach and Steam-key distribution, then tracks who streamed, for how many hours, peak viewers and clicks to the Steam page, and produces campaign reports. Creators sign up free.
- **Key pains:** GAM-24, GAM-03, GAM-06, GAM-08, GAM-09, GAM-10.
- **Why now:** in 2026, hours watched on indie-tagged Twitch channels grew 51% and Drops campaigns 20% (global figures). Kick opened a public API in 2025, and Spanish studios are under pressure.
- **Price hypothesis:** €29/month per studio, or €99 per launch campaign; free for creators.
- **Evidence:** medium. The discoverability pain is strong and well sourced; willingness to pay is not.
- **Moat:** low-moderate. A curated Spanish-language creator graph with quality signals.
- **Top risks:**
  1. Studio budgets are tiny: 39% need €50k–150k for their whole next project.
  2. Global key-distribution tools add Spanish filters; Keymailer, Lurkit and Woovit are named in the validation questions, not in the notes.
  3. Limits on API access; Kick's developer terms were not found.

#### IDEA-63 Fandango Arena reshaped: a cheap streamer-vs-chat co-op physics party game [user idea U4]
- **Type:** B: a game (PC and Steam first), with a chat-interaction layer that could later be licensed to other studios.
- **Buyer:** players on Steam worldwide, with Spain and Latin America as the launch community.
  - In Spain, 28% of 22.8M players prefer PC, about 6.4M people as a generous upper bound (an inference).
  - Streamers get free keys, and revenue comes from unit sales.
- **Sources:**
  - G6-I13 (`stage2_G6_expat_startups_gaming.md:613`);
  - the U4 assessment (`stage2_G6_expat_startups_gaming.md:598`);
  - U4 as given (`00_user_supplied_ideas.md:43`).
- **Problem and product:**
  - Indie games drown on Steam. The proven way out is a cheap co-op game that is funny to watch and spreads through streamers (GAM-24, GAM-10).
  - The user's version misreads the market on two points (GAM-11, GAM-13):
    - Spain did not move away from shooters: its top Twitch games for Jan–Sep 2026 are League of Legends, Valorant and Fortnite;
    - the genre's hits sell for €5–10, not about $30.
  - **The game:** a 2–4-player online co-op physics comedy.
  - **"Chat chaos" mode:** Twitch chat or Channel Points (and Kick chat) vote on rule cards. There is no wagering, no paid randomness and no item with money value.
  - **Defaults:** friends-only proximity voice, a clip button and a streamer overlay, in Spanish and English.
  - **First playable** (about 8–12 weeks): one map, five rule cards, and a Steam page with a Next Fest demo.
- **Key pains:** GAM-10, GAM-11, GAM-13, GAM-18, GAM-24, GAM-06, GAM-08, GAM-03.
- **Why now:**
  - The genre is still producing hits and new entrants in 2026, and indie-tagged Twitch hours rose 51%.
  - Kick's API makes Latin American integrations possible.
  - Developers are available after the 2025–26 layoffs (51 at Ubisoft Barcelona, more than 50 at King Barcelona).
  - Regulatory exposure: the minors' digital protection bill is pending or has likely lapsed, and an EU draft on age verification is circulating.
- **Price hypothesis:** €8.99 list price (€7.19 at launch), with a four-pack priced near the cost of three copies.
- **Evidence:** medium. Genre sales and Spanish prices are well documented; demand specific to Spain is unknown.
- **Moat:** none. A hit-driven product: only execution, timing and creator relationships matter.
- **Top risks:**
  1. The genre is saturating and no top creator picks it up. Kill if the Steam page and demo miss a wishlist target set before Next Fest, or if fewer than three Spanish creators averaging 1,000+ viewers stream the demo.
  2. It must sell abroad, where English-language creators drive the genre: only 44% of Spanish studios' revenue comes from Spain. Netcode makes the build complexity high.
  3. Voice chat with minors: 86% of 12–17-year-olds play.

#### IDEA-64 LigaHub reshaped: a points-only, cross-platform prediction and draft companion for simulcast creator events [user idea U5]
- **Type:** B: a gaming platform (B2B2C). Brands and event producers pay, and viewers play free.
- **Buyer:** producers of creator-led events and community tournaments, creator agencies and the brands that sponsor them; mid-tier creators on a free tier.
- **Sources:**
  - G6-I14 (`stage2_G6_expat_startups_gaming.md:661`);
  - the U5 assessment (`stage2_G6_expat_startups_gaming.md:647`);
  - U5 as given (`00_user_supplied_ideas.md:52`).
- **Original form: flagged for likely discard.** U5 as given is an automated white-label platform for mid-tier streamers to build their own leagues, with community drafts, viewer predictions, dynamic leaderboards and transfer-market tools "mirroring real money transactions". It fails on four counts:
  - staking transferable objects of economic value is "juego" under Ley 13/2011 art. 3.a, and operating without a licence is prohibited (art. 9.2) (GAM-21);
  - Twitch Extensions ban exchanging items for money (5.2) and Bits wagering (6.2.x) (GAM-18);
  - mid-tier demand to run leagues is unsupported (GAM-17);
  - drafts and predictions are saturated or free natively: Biwenger, Comunio, LaLiga Fantasy, Twitch Predictions (GAM-19, GAM-20).
- **Problem and product (reshaped):**
  - Big creator events are now simulcast on Twitch, YouTube and TikTok. La Velada VI's Twitch peak fell to about 8M from 9.2–9.33M, which one outlet puts down to simulcasting (GAM-07).
  - Native interactivity is tied to one platform, Kick's API has no predictions endpoint, and any real-money mechanic is gambling (GAM-18, GAM-21).
  - **The companion:** a web app opened from a link or QR code in every stream. Viewers play with free points that cannot be bought, cashed out or transferred.
  - **What viewers do:** predictions for each match, a pre-event "draft your card", and one cross-platform leaderboard.
  - **What sponsors get:** sponsor-branded rounds, an audience report, chat bots and overlays.
  - **MVP:** one fight-card template.
- **Key pains:** GAM-07, GAM-18, GAM-21, GAM-09.
- **Why now:**
  - Simulcasting is becoming the norm, and Kick's API arrived in 2025.
  - The Kings League's 2026 retrenchment (a dismissal plan, and the Spanish league paused for six months) suggests that full creator leagues are capital-heavy, which favours lighter single-event formats (inference).
- **Price hypothesis:** €500–1,500 per sponsored event, or €49/month for creators who run regular events.
- **Evidence:** weak. Mid-tier demand is unproven, and the simulcast effect is single-source.
- **Moat:** none, speed only. Native tools are free, and top events build their own.
- **Top risks:**
  1. No paying producers or brands: kill if fewer than three commit to paid pilots.
  2. Sponsor prizes could turn it into a regulated contest or game: kill if a gaming lawyer finds no prize-free design that sponsors would find attractive.
  3. Platform terms could restrict links out of the stream.

---

## 3. User-supplied ideas

None of the five survives as given. The reshaped versions are full candidates and go through the same validation as every other idea (section 6, batches 5 to 8).

### 3.1 Status of U1–U5

| User idea | Claims supported | Claims contradicted | Claims unverified or weak | Reshaped version | IDEA |
|---|---|---|---|---|---|
| **U1 ColivEs** (`00_user_supplied_ideas.md:14`; assessed at `stage2_G3_property_hospitality.md:759`) | **Housing shortage:** supported, but structural (HOU-20, CON-12).<br>**Licence crackdowns:** supported. Barcelona's 10,101 HUT licences end in Nov 2028; Madrid Plan Reside fines reach €190,000; Málaga bans new VUT in 43 barrios.<br>**Regional legal compliance:** strongly supported; the core to keep (HOU-01, HOU-02, HOU-05, HOU-12, HOU-13).<br>**Local rent caps:** supported as a need, but a Barcelona and Catalonia feature. | **eIDAS identity as a differentiator:** contradicted. Landlords are not obliged to accept it, so keep commodity KYC only (HOU-10).<br>**Dynamic pricing on nomad movements:** contradicted while RDL 29/2026 art. 17.8 caps rises (HOU-22).<br>**Flats converting to coliving:** partly contradicted. Real in Madrid, narrow in Málaga, largely closed in Barcelona (seasonal offer −37%) (HOU-19). | **"Constant influx" of high-earning nomads:** weak. One unverified count (27,875 including dependants at end-2024); rankings are indices, not volumes; the cause rule may exclude part of the demand (HOU-07, HOU-23).<br>**Coliving hubs:** legally constrained, since this is planning law (HOU-18, filtered N2). | **Mid-term lease compliance file** (G3-I11). Anchor in Barcelona and Catalonia, then Madrid. Málaga depends on RDL 29/2026. | IDEA-29 |
| **U2 PermisoFast** (`00_user_supplied_ideas.md:23`; assessed at `stage2_G6_expat_startups_gaming.md:542`) | **Target cities:** the three largest UGE stocks (Barcelona 53,700, Madrid 41,680, Málaga 19,056).<br>**Cita previa backlog:** a real pain, but not usable as a feature, since bots and resale are prosecuted.<br>**Rule tracking:** supported in substance (20+ changes in 17 months), but aimed at the wrong sources; they are national, not regional.<br>**Document pre-fill and error-catching:** supported needs (EXP-07), not novel (GestoLab). | **Beckham Law "backlog":** contradicted. The problem is a hard six-month modelo 149 deadline, not a backlog (EXP-10).<br>**HR teams and agencies as filing buyers:** partly contradicted. They cannot file for others; filers are lawyers, gestores and graduados sociales (EXP-22). | **NIE backlog:** partly supported. The binding bottleneck is the TIE fingerprint appointment (EXP-01).<br>**A gen-AI suite handling the whole file:** risky as scoped. GDPR art. 10 and the AI Act classification were not researched. | **Co-pilot for UGE talent cases**, sold to habilitated filers and their agency partners (G6-I12). Related: IDEA-53, IDEA-54, IDEA-56. | IDEA-52 |
| **U3 EcoRoute** (`00_user_supplied_ideas.md:32`; assessed at `stage2_G5_mobility_industry_cities.md:694`) | **Madrid and Barcelona as targets:** supported. Madrid has 3.4M+ files and €663M of fines to end-2025; Barcelona bans unlabelled vans on weekdays.<br>**"Strict, camera-enforced" ZBEs:** true only where cities fine.<br>**Open-data feeds:** perimeters only.<br>**Burden on small operators:** real, but they do not buy APIs.<br>**Valencia Sandbox:** exists, as a pilot channel only. | **Routing that avoids penalties:** contradicted for in-zone deliveries (ZBE-15).<br>**Valencia as a market:** contradicted; no ZBE in force per the ZBE track, though the notes conflict (section 5).<br>**Valencia as the "open civic data testing capital" for this API:** not supported for revenue. | **Sandbox status:** final approval and BOP publication unverified, and no mobility projects named.<br>**Enforcement coverage:** about 50 of roughly 150 obliged municipalities fine (an inference). | **Spanish ZBE rules and in-zone compliance-check API** (G5-I09). End-user apps on the same data: IDEA-47. | IDEA-48 |
| **U4 Fandango Arena** (`00_user_supplied_ideas.md:43`; assessed at `stage2_G6_expat_startups_gaming.md:598`) | **Co-op rise:** supported globally only (4 of Steam's top 10 by units in 2025; GAM-10).<br>**Proximity voice chat:** a genre trait.<br>**Twitch and Kick integration:** feasible, though Kick has no rewards or predictions endpoints.<br>**Real-time viewer votes:** allowed with no stake and no prize (GAM-18, GAM-21). | **"Shift away from shooters":** contradicted for Spain (GAM-11).<br>**About $30 "premium" price:** contradicted. Hits sell for €4.99–9.99, and four copies at €30 cost €120 (GAM-13). | **Ibai Llanos and AuronPlay:** partly supported; AuronPlay is not in the notes.<br>**"National" market:** partly supported. Spain is only the launch market, since 44% of Spanish studios' revenue comes from Spain.<br>**Paid Bits votes:** to verify. | **Cheap streamer-vs-chat co-op physics party game at €8.99** (G6-I13). | IDEA-63 |
| **U5 LigaHub** (`00_user_supplied_ideas.md:52`; assessed at `stage2_G6_expat_startups_gaming.md:647`) | **Kings League appetite:** partly supported. €51M revenue and 150M hours, but loss-making, about 90% sponsor-funded, Spanish audience −54%, and a 2026 dismissal plan (GAM-14, GAM-15).<br>**"Rigid esports declining":** partly supported; true for Spain's national tier only. | **Transfer market "mirroring real money transactions":** prohibited without a licence (Ley 13/2011 arts. 3.a and 9.2; Twitch rules 5.2 and 6.2) (GAM-21, GAM-18). | **Mid-tier streamers wanting to run leagues:** unsupported (GAM-17).<br>**Drafts and predictions:** saturated or free natively (GAM-19, GAM-20).<br>**White-label league platform:** weak; incumbents build in-house (GAM-16). | **Original: flagged for likely discard.**<br>**Reshaped:** a points-only, cross-platform prediction and draft companion for simulcast creator events, paid by brands and producers (G6-I14); a weak candidate. | IDEA-64 |

### 3.2 Regional claims (the user's city table)

The verdicts come from `stage2_G6_expat_startups_gaming.md:688`, which drew on the G6 notes plus the ZBE and cities files. **Of the 18 sub-claims: 2 supported, 6 partly supported, 8 unverified, and 2 weak or contradicted.**

| City | Persona claims | Best-fit product claims | What the notes support instead |
|---|---|---|---|
| Madrid | **Enterprise capital:** partly supported. Most large companies (1,605 against Barcelona's 973) and the highest CRM use (41.4%).<br>**Heavy AI focus:** unverified. AI use is 40.1%, against Cataluña's 40.5%.<br>**Deep VC liquidity:** partly supported, and the notes conflict. H1 2026 brought €738M, but €500M of it came from four megarounds. | **GovTech automation:** weak, and contradicted as an easy fit. 45.8% of central-government contracts went to the only bidder, and startups are largely locked out (STA-13).<br>**B2B enterprise productivity SaaS:** unverified. | Relocation and startup compliance: 41,680 UGE permits and 509 certified startups (IDEA-52, IDEA-56, IDEA-59). Also the largest ZBE fine volume (IDEA-47, IDEA-48) and Madrid-first licensing (IDEA-25). |
| Barcelona | **Deep tech:** supported. 89% of Catalan startups invest in R&D; 308 spin-offs.<br>**International startup hub:** supported. 28% have a foreign founder; it has the largest UGE stock.<br>**High tourist friction:** unverified in the G6 notes. G3 documents the licence phase-out (HUT licences end Nov 2028). | **PropTech compliance:** unverified in G6; G3 rates mid-term lease compliance as its best-evidenced idea, anchored in Catalonia.<br>**Nomad housing platforms:** partly supported, on the demand side only (15,073 DNV permits). | IDEA-29, IDEA-30, IDEA-33 (Catalan tax step on 1 Apr 2027) and IDEA-61 (R&D credits). Also IDEA-55 and IDEA-56, since Barcelona publishes no office timings. |
| Valencia | **Sustainability node:** unverified. The largest 2025 rounds were in biotech, health, AI and fintech; climate exposure is a resilience need.<br>**Open civic data testing capital:** partly supported. The Sandbox ordinance exists but its approval is unverified, and the open data cover only ZBE perimeters. | **ClimateTech:** unverified.<br>**ZBE logistics API:** contradicted for Valencia, and the notes conflict. | Flood resilience (IDEA-28, after DANA 2024 and dana Adam). A Sandbox or port pilot channel for IDEA-48. Published office timings for IDEA-55. |
| Málaga | **Cybersecurity anchor:** unverified.<br>**International talent hub:** partly supported. 19,056 UGE permits including 4,916 DNV, and TechPark has 700+ companies; but VC is thin (under €8M in 2023) and incomes are the lowest of the big seven cities. | **Nomad relocation apps:** partly supported. The products are national, and the police auto-assignment pilot covers Málaga.<br>**Community sandbox games:** unverified. | Málaga's 43-barrio tourist-flat ban (IDEA-32). Mid-term lets, which hinge on RDL 29/2026 (IDEA-29). The UGE talent co-pilot (IDEA-52). Its ZBE chapter was annulled, with fines stopped on 14 Oct 2026. |

---

## 4. Index tables

### 4.1 By type

| Type | Primary type (count) | Also as secondary type |
|---|---|---|
| **A**, cheaper alternative | **6:** IDEA-05, 13, 16, 38, 39, 58 | IDEA-01, 17, 25, 27, 30, 33, 34, 36, 37, 48, 51, 52, 53, 56, 60, 61 |
| **B**, new product | **36:** IDEA-01, 03, 04, 06, 08, 17, 18, 21, 22, 24, 25, 26, 27, 29, 31, 32, 33, 34, 36, 40, 43, 44, 46, 48, 49, 50, 51, 52, 53, 55, 56, 60, 61, 62, 63 (a game), 64 (a gaming platform) | IDEA-02, 07, 11, 19, 38, 41, 42, 45, 47, 54, 57, 59 |
| **C**, low-touch subscription | **22:** IDEA-02, 07, 09, 10, 11, 12, 14, 15, 19, 20, 23, 28, 30, 35, 37, 41, 42, 45, 47, 54, 57, 59 | IDEA-01, 06, 08, 16, 21, 24, 29, 32, 39, 46, 49, 55, 58, 62 |

Some type C ideas are priced at about €5/month or less per unit in their source hypothesis: IDEA-07, 09, 10, 12, 15, 19, 20, 23, 28, 30, 41, 47 and 57. Others sit at €5–9: IDEA-02, 11, 14, 37 and 45 (€6 per vehicle). The rest are priced higher: IDEA-35 (€9–19), 42 (€9–15), 54 (€9 per seat) and 59 (€9).

### 4.2 By buyer segment

An idea can appear in more than one row.

| Buyer segment | Ideas |
|---|---|
| Autónomos and micro firms, any sector | IDEA-02, 05, 08, 09, 11, 12, 13 |
| SMEs and company owner-managers (finance, admin, legal duties) | IDEA-01, 03, 07, 10, 11, 26, 27 |
| Gestorías, asesorías and graduados sociales, as buyer or white-label reseller | IDEA-06 (core buyer), 03, 07, 09, 16, 17, 18, 19, 57 |
| Law firms, procuradores and habilitated immigration filers | IDEA-01, 17, 52, 53, 54, 57 |
| Employers and HR | IDEA-16, 17, 18, 44, 56, 57; households as employers: IDEA-19 |
| Shops, e-commerce and B2C services | IDEA-14, 15, 20, 21, 23, 24, 38, 39, 49 |
| Hospitality and lodging | IDEA-14, 20, 23, 32, 33, 37 |
| Landlords, rental agencies, property managers and administradores de fincas | IDEA-01, 29, 30, 31, 32, 34, 35 |
| Construction, installation and maintenance subcontractors | IDEA-36 (also as suppliers in IDEA-34) |
| Health, veterinary, care and education providers | IDEA-40, 41, 42, 43, 44 |
| Hauliers, distributors and van fleets | IDEA-45, 46, 47 |
| Software vendors and integrators (data or API buyers) | IDEA-18 (HR and payroll vendors), 48 (fleet software, renting, insurers); API tiers in IDEA-33 (PMS) |
| Food, drink, agri and manufacturing firms | IDEA-49, 50, 51 |
| Telecom, energy and basic-service providers; phone-sales teams | IDEA-21, 22 |
| Startups and founders | IDEA-15, 58, 59, 60, 61 |
| Relocating talent, HR mobility teams and relocation agencies | IDEA-52, 55, 56, 58 |
| Flood-prone businesses, through insurers and brokers | IDEA-28 |
| Game studios, players, creators, event producers and brands | IDEA-62, 63, 64 |

### 4.3 By geography

| Scope | Ideas | Where it bites |
|---|---|---|
| **National:** the rules and buyers are national | IDEA-01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24, 26, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 49, 50, 52, 53, 54, 56, 57, 58, 59, 60, 61 | **Common-territory caveats:** IDEA-04 and IDEA-05 must handle the Basque TicketBAI regime; IDEA-06 tags common, foral and Canarias clients; IDEA-58 excludes the Basque and Navarre foral regimes.<br>**MVP or launch city:** IDEA-24 (one city and its police force), IDEA-43 (DGT hotspots).<br>**Concentration:** IDEA-52 in Barcelona, Madrid and Málaga; IDEA-41 faces 17 regional inspection regimes. |
| **National, with regional rule layers** | IDEA-18 (provincial convenios; MVP in six provinces), 20 (Andalusia Hoj@ and Catalan modules), 27 (PLACSP plus seven regional platforms), 30 (tensioned zones by region; Catalonia first), 51 (regional export formats) | Regional variation is part of the product. |
| **Regional launch markets** | IDEA-28 (provinces of Valencia and Alicante), 29 (Catalonia first, then Madrid and Málaga), 33 (Basque Country and Catalonia) | Each depends on a regional law or event. IDEA-29's national half depends on RDL 29/2026. |
| **City- or office-specific data layers** | IDEA-25 (Madrid first, then city by city), 32 (regional registers plus municipal zoning: Madrid, Málaga, Palma, Valencia, Alicante), 44 (council tender formats), 47 and 48 (the sanctioning ZBE cities: Madrid, Barcelona/AMB, Bilbao, Palma, Granada, Sevilla-Cartuja, Valladolid, Córdoba, A Coruña, and Zaragoza if confirmed), 55 (office by office) | Each city or office must be modelled separately. That is the cost, and the moat. |
| **International or Spanish-language** | IDEA-62 and 64 (Spanish-language creators, Spain and Latin America), 63 (global Steam sales; Spain and Latin America launch) | Spain is a launch market, not the whole market. |

**The user's four cities in the notes:**

| City | Ideas with city-specific evidence |
|---|---|
| Madrid | IDEA-01 (backlog +10.4%; ICAM survey), 24 (MVP city), 25 (Madrid-first licensing), 29 (60% of operating flex-living beds; seasonal offer +52%), 32 (Plan Reside), 43 (waits of 1.5–5 months), 47 and 48 (3.4M+ ZBE files and €663M of fines to end-2025), 52 and 56 (41,680 UGE permits), 55 (publishes resolution dates) |
| Barcelona and Catalonia | IDEA-20 (Catalan language duty), 29 (Llei 11/2025 anchor), 30 (53 new tensioned municipalities), 32 (HUT licences end in 2028), 33 (Catalan tourist tax step on 1 Apr 2027), 47 and 48 (Rondes van ban and the suspension), 52, 55 and 56 (53,700 UGE permits; no published office timings), 61 (R&D-intensive startups) |
| Valencia | IDEA-25 (draft licensing ordinance), 28 (DANA 2024, dana Adam), 32 (moratorium), 48 (Sandbox or port pilot only; ZBE status conflict), 55 (publishes resolution dates) |
| Málaga | IDEA-01 (Audiencia Provincial de Málaga MASC ruling), 25 (ALU, a free licensing assistant, competes), 29 (seasonal lets are 37% of the rental offer), 32 (43-barrio ban), 47 and 48 (ZBE chapter annulled; fines stopped on 14 Oct 2026), 52 (19,056 UGE permits) |

---

## 5. Conflicts to resolve in validation

These are the factual conflicts the group files flag. They are listed, not resolved: validators should settle each one from the primary source and record which side was right. The IDs are used in section 6.

### 5.1 Factual conflicts

| ID | Conflict | What the notes say | Flagged in | Ideas affected |
|---|---|---|---|---|
| C-01 | **Valencia's ZBE status** | **Cities track** (valencia.es, 21 Oct 2025): an ordinance is in force from 1 Dec 2025 and exempts economic-activity vehicles.<br>**ZBE track:** the Pleno rejected final approval on 28 Oct 2025, with no new vote by Sep 2026, so no ZBE is in force.<br>**Also:** the DGT NAP shows Valencia "active" from 1 Jun 2026. Either way, SME vans face little pain in Valencia. | G5 conflicts, item 1 (`stage2_G5_mobility_industry_cities.md:249`); G6 conflicts (`stage2_G6_expat_startups_gaming.md:154`) and regional table | IDEA-48 (U3), IDEA-47; the regional claim "Valencia: ZBE logistics API" |
| C-02 | **Status of LO 1/2026 on repeat shoplifting** | **RET-04 (BOE consolidated text):** in force since 10 Apr 2026, with prison after three prior final convictions; AECOC says the €400 cumulative-value threshold is gone.<br>**Cities track:** could not verify the reform, and suggested it might lapse with the dissolution.<br>**LegalToday snippet:** says the €400 threshold still applies.<br>**Loss figure:** €2,817M (barometer) against €2,917M (Ara snippet). | G4 cluster C1 (`stage2_G4_retail_services.md:52`); G4-I01, validation questions 1 and 7; G4 cross-links | IDEA-24 |
| C-03 | **MEI rate** | The 2026 intergenerational equity surcharge is 0.80% (official) or 0.90% (secondary source). G1 states that it rises to 1% in 2027. | G2 noise log, LAB-04; G1 cluster C6 | IDEA-09; IDEA-06 (rule feed); IDEA-19 (contribution estimates) |
| C-04 | **Number of employers** | **1.35M** employer companies (Consejo de Estado, LAB-01).<br>**About 1.51M** businesses with employees: 45.6% of DIRCE's 3,310,824 (G2's arithmetic).<br>**1,231,358** employer units (INE CODEM, 2026Q2, G5's macro anchors).<br>The bases differ, and the micro share is not given. | G2-I04 buyer (`stage2_G2_labour_legal_admin.md:608`); G5 macro (`stage2_G5_mobility_industry_cities.md:60`) | IDEA-16, IDEA-17 (market size); IDEA-57 (employers of foreign workers, count unknown); IDEA-06 (client base) |
| C-05 | **When small firms must report invoice statuses** | **AEAT (7 Oct 2026; TAX-05, TAX-06):** legal entities at or below €8M report from 6 Oct 2028, and personas físicas from 6 Oct 2029.<br>**Law-firm sources (FIN-25):** reporting stays voluntary for everyone below €8M until 6 Oct 2029.<br>**Consejo General de Gestores draft dates:** SPFE online on 1 Aug 2027, and status reporting for firms up to €8M from 1 Oct 2029 (PRO-11).<br>**Single-source:** the 4-calendar-day reporting window and the €10,000 sanction. | G1 cluster C2 (`stage2_G1_money_tax_software.md:92`); G1-I03; G4 cluster C8 (`stage2_G4_retail_services.md:231`); G4-I08 | IDEA-03, IDEA-06; IDEA-02 (payment-date data); IDEA-11 (IBAN–e-invoice link); IDEA-01 (later triggers) |
| C-06 | **Whether Verification of Payee is in force** | Regulation (EU) 2024/886 requires it "from 9 October 2025 according to the researcher's background knowledge". The notes did not verify this, or what Spanish banks show business customers. | G1 cluster C10 (`stage2_G1_money_tax_software.md:413`); G1-I11 | IDEA-11 (its main kill risk) |
| C-07 | **AEPD fine totals** | **G2 (LEG-05):** the 2025 total is €33.9M (Lawwwing) against €48.1M elsewhere, and the fine count is 325, 326 or 299.<br>**G4 (PRO-08):** €40M against €48.1M.<br>**Sector fines:** commerce, transport and hospitality went from €0.61M to €10.76M. | G2 cluster C8 (`stage2_G2_labour_legal_admin.md:196`); G4 noise log, PRO-08 | IDEA-23; the data-protection risk framing in IDEA-24, IDEA-31 and IDEA-40 to IDEA-42 |
| C-08 | **VeriFactu dates** | **BOE** (RD 1007/2023, as amended by RDL 15/2025): 1 Jan 2027 for corporate-tax payers and 1 Jul 2027 for everyone else.<br>**Hacienda's announcement (5 Oct 2026):** a move to October 2028, including the QR. It was not in the BOE as of 21 Oct 2026, and the AEAT FAQ still shows 2027.<br>**Infoautónomos:** October 2027 for firms above €8M, against a single October 2028 date in the official note. | G1 cluster C3 (`stage2_G1_money_tax_software.md:103`) | IDEA-04, IDEA-05, IDEA-06, IDEA-39; IDEA-40 (invoice rules) |
| C-09 | **RETA cotización tables** | The 2026 tables rest on a single source (Orden PJC/297/2026), and the maximum base conflicts: €4,909 against the table (TAX-12). | G1-I07, validation question 1 | IDEA-09 |
| C-10 | **Invoicing software prices** | **TS Facturas/Billin:** two price lists.<br>**Holded:** three sources (annual billing, against about double monthly).<br>**Anfix:** €4.99 against "from €15".<br>**Contasimple:** owned by Shine or by Cegid. | G1-I05 | IDEA-05; price anchors for IDEA-02 and IDEA-46 |
| C-11 | **Odoo price** | US$31.10/user/month on annual billing (transport notes) against €19.90/user/month (software table). | G5 conflicts, item 9 | IDEA-49 (ERP alternative) |
| C-12 | **Ley 1/2025 (food waste) dates** | **Dates:** the law was published on 02/04/2025, but the BOE extract says "entrada en vigor 02/01/2025" (IND-25). G3 dates the art. 6 duties from about 3 Apr 2026.<br>**Fines:** press stories of fines for not offering free containers look overstated, since art. 20 lists no such infraction (HOS-08). | G5 conflicts, item 10; G5-I07, validation question 6; G3 cluster C8 (`stage2_G3_property_hospitality.md:181`) | IDEA-37; IDEA-49 (food-waste module) |
| C-13 | **ZBE status in other cities** | **Málaga:** a label-B step on 30 Nov 2026 (cities track), against a ZBE chapter annulled with fines stopped on 14 Oct 2026 and the ruling final around 25 Nov 2026 (ZBE track). The legal reasoning also conflicts: discrimination and market unity, against the domicile challenge being rejected.<br>**Zaragoza:** not operational until at least 2030, against the Casco Histórico zone fining since 12 Dec 2025.<br>**Vigo label B:** from 2029 or from 2027.<br>**Catalonia label B before 2028:** required by Decree 132/2024 with no ordinance amendments started, against "a plan, not yet law".<br>**Barcelona suspension start:** 22 or 28 Jan 2026.<br>**Madrid van rules:** RACE against the madrid.es FAQ after Ordenanza 2/2026; G5 says to use the ZBE track.<br>**Active ZBEs:** 56 (Feb 2026) or 68 (Sep 2026), and 149 or 151 obliged municipalities. | G5 conflicts, items 2–8 | IDEA-47, IDEA-48 |
| C-14 | **Rental rules** | **Fianza for temporary leases outside Catalonia:** one month or two; no official guidance (HOU-12).<br>**Canarias fines for unlodged deposits:** 35–100% or 5–75%.<br>**Basque tensioned municipalities:** 17 to 19.<br>**Coliving and the Catalan cap:** whether coliving is inside the cap is disputed (3Cat). | G3 clusters C1 and C2 (`stage2_G3_property_hospitality.md:48`, `:70`); G3-I11, validation question 6 | IDEA-29, IDEA-30 |
| C-15 | **Arrears and eviction figures** | **Debt growth:** +16.5% year on year, against about +6.7% implied by the 2024 average.<br>**CGPJ evictions:** the parts add up to 24,540 against a stated total of 25,540; G3 says to use 25,540. | G3 cluster C4 (`stage2_G3_property_hospitality.md:104`) | IDEA-01 (landlord module) |
| C-16 | **Lodging duties** | **SES card data:** one vendor FAQ says card number and expiry are not mandatory, but the BOE annex lists the card expiry date.<br>**Barcelona tourist tax:** Forbes and DonPorqué give different amounts.<br>**Chekin minimum unit counts:** stated as 3, 10 or 20. | G3 cluster C6 (`stage2_G3_property_hospitality.md:153`); G3-I05, validation question 5 | IDEA-33 |
| C-17 | **Construction deaths** | El Español's "29 deaths" misreads INSST's "+29"; the figure to use is +21.5% (CON-04). | G3 cluster C9 (`stage2_G3_property_hospitality.md:203`) | IDEA-36 (why-now claim) |
| C-18 | **Working-time fines** | €15.7M for 2025 (one unsourced article) against €17.2M for 2024; the scope may differ (LAB-02). | G2 cluster C1 (`stage2_G2_labour_legal_admin.md:53`) | IDEA-16 |
| C-19 | **Catalan-language complaints** | 1,873 in 2023 (3Cat, Vozpópuli) against more than 2,000 (NacióDigital, which counts more case types) (LEG-15). | G2 cluster C9 (`stage2_G2_labour_legal_admin.md:219`) | IDEA-20 (Catalan module) |
| C-20 | **Driving-test queue size** | **Sector:** 82,000 students queuing in Andalusia and 63,000 in Barcelona.<br>**DGT:** when it offered unlimited extra exams, under 10% were presented (Navarra 275 of more than 6,000; Barcelona 1,450 of 63,000), and its head says "solo un 8 %" (only 8%) are ready. | G4 cluster C10 (`stage2_G4_retail_services.md:285`) | IDEA-43 |
| C-21 | **Number of salons** | About 72,300 hairdressing and beauty establishments (DBK 2021, snippet) against about 35,000 salons (sector figure, June 2021); the definitions probably differ. | G4-I04 | IDEA-39 |
| C-22 | **Domestic workers** | About 348,000 registered (INSST, May 2025), more than 378,000 (El Español, May 2026), and about 540,000 in the EPA. | G4-I12 | IDEA-19 |
| C-23 | **PRESVET figures** | **Vet protests:** 2,000 to 5,000 vets, depending on the source.<br>**"80% automated":** unclear whether it refers to clinicians or to prescriptions.<br>**16,460 clinicians:** from a search summary. | G4-I07 | IDEA-42 |
| C-24 | **Card-acceptance fees** | 0.3–1.5% against 0.5–2% (RET-05, filtered as N7 and merged into FIN-13). | G4 noise log | IDEA-08 (acquirer data); IDEA-39 (payments) |
| C-25 | **Immigration procedure facts** | **TIE waits:** only commercial or anecdotal figures exist (EXP-01).<br>**Cl@ve and the NIE:** Migralis and the FNMT disagree (EXP-12).<br>**Reunification deadline:** two months with negative silence, or three months or 45 working days with positive silence (EXP-04, EXP-16).<br>**June 2026 thresholds:** whether they cover the national highly qualified permit (EXP-09).<br>**UGE fee:** €73.26 against €70.40 initial / €75.60 renewal.<br>**Madrid padrón:** batch appointment releases or walk-ins (EXP-15). | G6 conflicts (`stage2_G6_expat_startups_gaming.md:154`) | IDEA-52, IDEA-54, IDEA-55, IDEA-56, IDEA-58 |
| C-26 | **ENISA and startup-law facts** | **Certified startups:** 275 in Valencia against "en torno a 200"; nationally 2,527 against 2,529.<br>**ENISA's silence:** approval (BOE) or rejection (Legalitas).<br>**Angel deduction cap:** €100k (BOE) or €250k (Venza).<br>**AES membership:** 1,500 to 2,000. | G6 conflicts; G6-I07 | IDEA-59, IDEA-60; the regional claim for Valencia |
| C-27 | **Venture-capital figures** | **2025 growth:** +63% (Dealroom), −3% (Bankinter) or +59% (Valencia Plaza).<br>**2025 ranking:** Madrid €1.2B and Barcelona €1.1B (Dealroom), against Barcelona €1,374M and Madrid above €800M (Bankinter).<br>**Valencia 2025:** €160M+ or €229–237M. | G6 conflicts | The regional claims for Madrid and Valencia; context for IDEA-60 and IDEA-61 |
| C-28 | **Gaming and creator facts** | **Kings League funding:** €110M or more than $160M raised.<br>**Kings League dismissal plan:** 40 of 125, 41 of 83, or about 30% of 124 staff.<br>**Twitch subscription in Spain:** €3.99 or €4.99 (GAM-09). | G6 conflicts | IDEA-64; IDEA-62 and IDEA-63 (creator-income context) |

### 5.2 Rule status and single-source facts to confirm first

These are not conflicts between sources, but several ideas stand or fall on them. The status is as given in the notes on 23 Oct 2026.

| Rule or fact | Status in the notes | Lapse or change risk around the 29 Nov 2026 election | Ideas |
|---|---|---|---|
| **RDL 29/2026** (housing) | **What it covers:** mid-term lease rules, the 2% update cap, limits on avales, platform sanctions and the eviction-suspension regime. Also VAT on stays of 30 nights or fewer, and the payment-method rule for renovation VAT.<br>**Status:** in force since 8 Oct 2026. The Diputación Permanente vote is around 12 Nov 2026 (single source, forecast 35–34), and its sister decree RDL 26/2026 already failed. | **High.** It lapses if not convalidated, and a new government could repeal or replace it. | IDEA-29, 30, 31, 32; 01 (landlord module); filtered TAX-24 and HOU-17 |
| **VeriFactu move to October 2028** | Announced on 5 Oct 2026; not in the BOE as of 21 Oct 2026. | It is unknown which instrument can enact it while the Cortes are dissolved. If it is a decree-law, it carries convalidation risk. Three decree-laws failed in 2026. | IDEA-04, 05, 06, 39 |
| **Digital time-recording royal decree** | A draft. The Consejo de Estado's opinion was unfavourable, and approval was postponed. | It could still be approved before 29-N as a regulation; otherwise it stalls. | IDEA-16, 19 |
| **RDL 9/2026 and RDL 25/2026** (haulage fuel line and aid) | In force; convalidation unverified. | If they lapse, the indexation rule remains in Ley 15/2009 art. 38. | IDEA-46 |
| **Draft AICA inspection decree** | Public consultation opened on 30 Sep 2026. | It may stall with the election. | IDEA-50 |
| **Junts bill on societario bases** | Pending in May 2026; outcome unverified. | Bills lapse with the dissolution. | IDEA-09 |
| **PRESVET sanctions reform** | Reported "en trámite" in Mar 2025. | If still pending on 6 Oct 2026, it lapsed, and the current fines stand. | IDEA-42 |
| **Minors' digital protection bill** | Pending or likely lapsed; an EU draft on age verification is circulating. | Lapse. | IDEA-63 |
| **Ley 10/2025 adaptation period** | It is unclear whether the 12-month period covers the consumer-law amendments. | The law is in force; no lapse. | IDEA-20 |
| **400-prefix numbering resolution** | In force, with blocking since 17 Oct 2026; whether it covers B2B calls and autónomos is unclear. | No lapse. | IDEA-21 |
| **Andalusian Hoj@ Order of 24 Apr 2026** | Known only from a single vendor source; the BOJA was not checked. | A regional rule; no lapse. | IDEA-20 |
| **Statutory late-payment rate for H2 2026 (10.40%)** | Single source (via Novicap). | n/a | IDEA-01, 02, 46 |
| **24-hour embargo roll-out** (AEAT resolution of 4 Jun 2026) | Single source. | n/a | IDEA-07 |
| **STS 1477/2026** (directors' liability) | Single press source. | n/a | IDEA-10 |
| **Modelo 170 letter waves** | Single press source. | n/a | IDEA-08 |
| **R&D credit cash-refund rules** | Single source, with no article numbers. | n/a | IDEA-61 |
| **Tighter UGE practice** (Criterio de Gestión 2/2025; outright rejections) | Single commercial source (Anchorless; Polaris). | A new government may amend the immigration Reglamento. | IDEA-52 |
| **EU rules:** PPWR, EUDR, AMLR, EU 2024/1028 | **PPWR:** since 12 Aug 2026.<br>**EUDR:** 30 Dec 2026 or 30 Jun 2027 by firm size, after two postponements.<br>**AMLR:** from July 2027.<br>**EU 2024/1028:** since 20 May 2026.<br>**Environmental Omnibus:** only a proposal. | Unaffected by the Spanish election. | IDEA-49, 35, 32 |

---

## 6. Validation plan

### 6.1 Rules for all eight batches

**Batches**
- There are 8 batches of related ideas, one validator each, and every IDEA is in exactly one batch.
- Batches 1–4 hold 9 ideas each. Batches 5–8 hold 7 each, because each contains at least one user idea.
- Every user idea gets full treatment: checks on all eight angles and a third or more of its batch's searches (U1 8, U2 8, U3 8, U4 7, U5 5).

**Search budget**
- Each batch has 24 web searches per turn (8 × 24 = 192 of the roughly 200 shared). Each batch states its allocation per idea.
- Fetching a known official or vendor page directly is unlimited and does not count against the budget.

**Marks on each check**
- **[F]:** fetch a known page directly (unlimited). The URL is given where it appears in the group files; otherwise the page is named, for example "BOE consolidated text" or "vendor pricing page".
- **[S]:** needs a web search, which counts against the 24.
- **[S\*]:** search only if budget is left after the [S] checks.
- **[I]:** needs interviews, a pilot or outreach, which desk research cannot do. Record the test, look for a published proxy, and leave it open.

**Angles**
- (a) problem reality and regulation status as of October 2026, including lapse risk from the 29 Nov 2026 elections;
- (b) competitors in Spain and abroad, by name, with prices;
- (c) buyers and market size;
- (d) willingness to pay and pricing anchors;
- (e) distribution channels;
- (f) build feasibility and legal constraints;
- (g) defensibility against fast AI-built copies;
- (h) kill criteria.

**Order of work in every batch**
1. The [F] rule-status checks, since one answer can kill several ideas.
2. The competitor scans.
3. Market size and price anchors.
4. Writing down the [I] kill tests.

**Shared checks.** One batch owns each cross-cutting check; the others reuse its answer and do not spend searches on it.

| Cross-cutting check | Owner |
|---|---|
| VeriFactu status and e-invoicing dates (C-05, C-08) | Batch 1 |
| Gestoría and asesoría counts; rules for third-party access to e-notifications | Batch 2 |
| Employer counts (C-04); the time-recording decree | Batch 3 |
| Ley 10/2025 transitional period; consumer-law limits on return fees and no-show deposits | Batch 4 |
| The RDL 29/2026 vote and its aftermath | Batch 5 |
| ZBE city status (C-01, C-13); HERE and TomTom coverage; DGT label lookup | Batch 6 |
| RD 316/2026 renewal rules (DA 20 and 21); UGE grant counts; immigration conflicts (C-25) | Batch 7 |
| Twitch and Kick API terms; the Spanish share of streams; the minors' bill | Batch 8 |

Each owner also records the 29 Nov 2026 election result wherever it changes a rule's status: caretaker government, convalidations, lapsed bills.

**What each validator returns, per idea**
- the answer to each check, with source URL and date;
- the status of each kill criterion: met, not met or open;
- the conflicts it settled.

---

### Batch 1. Getting paid, invoicing and the SME software bill (9 ideas, 24 searches)

**Ideas:** IDEA-01, IDEA-02, IDEA-03, IDEA-04, IDEA-05, IDEA-11, IDEA-12, IDEA-13, IDEA-36.

**Why together:**
- MASC claims, interest recovery and e-invoice payment data form one "money owed" workflow.
- The invoicing, contract and hosting ideas share the evidence on SME software terms (VOX-08 to VOX-16).
- The CAE wallet shares the pattern of imposed SaaS fees, plus the subcontractor late-payment link (CON-05, FIN-02).

**Search allocation:** IDEA-01 5; IDEA-02 2; IDEA-03 3; IDEA-04 3; IDEA-05 2; IDEA-11 2; IDEA-12 2; IDEA-13 2; IDEA-36 3. Total 24.

**Known pages to fetch:**
- BOE:
  - LO 1/2025, https://www.boe.es/buscar/act.php?id=BOE-A-2025-76;
  - RD 1007/2023, https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840;
  - Orden HAC/1028/2026, https://www.boe.es/boe/dias/2026/10/05/pdfs/BOE-A-2026-20587.pdf;
  - LGS, https://www.boe.es/buscar/act.php?id=BOE-A-2003-20977;
  - Ley 32/2006, https://www.boe.es/buscar/act.php?id=BOE-A-2006-18205.
- AEAT and Hacienda:
  - VeriFactu FAQ, https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html;
  - Hacienda's VeriFactu note, https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf;
  - AEAT SPFE news of 7 Oct 2026, https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/octubre/7/solucion-publica-facturacion-electronica.html.
- MASC and courts:
  - Moncloa.com on MASC, https://www.moncloa.com/2026/10/06/requisito-masc-lo-1-2025-juzgados-3443197;
  - Intercobros, https://www.grupointercobros.com/masc-y-reclamacion-de-deudas/;
  - the Las Palmas MASC criteria, https://confilegal.com/wp-content/uploads/2025/04/UNIFICACION-CRITERIOS-MASC-INSTANCIA-LPGC.pdf;
  - PwC on MASC, https://periscopiofiscalylegal.pwc.es/wp-content/uploads/2025/01/Retos-derivados-de-los-MASC-como-requisito-de-procedibilidad.pdf;
  - CGPJ 2025, https://www.poderjudicial.es/cgpj/es/Poder-Judicial/En-Portada/Los-organos-judiciales-recibieron-en-2025-un-3-2---menos-asuntos-que-el-ano-anterior-y-aumentaron-en-un-2---su-capacidad-de-resolucion.
- E-invoicing: B2Brouter prices, https://www.b2brouter.net/es/precios/, and deadlines, https://www.b2brouter.net/es/plazos-obligatoriedad-factura-electronica-b2b/.
- Fraud:
  - INCIBE 2025, https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025;
  - Banco de España complaints report 2025, https://www.bde.es/f/webbe/Secciones/Publicaciones/PublicacionesAnuales/MemoriaServicioReclamaciones/25/MSR2025_Resumen.pdf.
- Kit Digital: https://espanadigital.gob.es/lineas-de-actuacion/programa-kit-digital; Arsys, https://www.arsys.es/kit-digital.
- CAE: DocuPRL's comparison, https://docuprl.es/blog/mejores-plataformas-cae-2026.html; Nalanda reviews, https://es.trustpilot.com/review/www.nalandaglobal.com.
- Support costs: WhatsApp pricing, https://developers.facebook.com/docs/whatsapp/pricing/.

**IDEA-01 MASC kit** (5 searches)
1. (a) [F] Read LO 1/2025:
   - the valid MASC methods and art. 10.2 (proof content);
   - art. 17 (the one-month rule) and art. 7 (interruption of limitation);
   - art. 5.2 (evictions for non-payment);
   - additional provision 3 (official services).

   Also check whether a party may send a valid attempt without a lawyer.
2. (a) [S] Supreme Court or Audiencia rulings since Oct 2026 on:
   - MASC proof standards;
   - whether courts accept qualified electronic delivery from a private provider;
   - whether MASC applies before a community monitorio (LPH art. 21) and before evictions.

   Also: do the parties' 29-N programmes propose making MASC voluntary? This is the lapse and reform check.
3. (a)(h) [S] Status, dates and budgets of the official MASC services (Ministry of Justice, regions). A free channel with court-accepted certificates announced for 2027 is a kill criterion.
4. (b)(g) [S]×2 Competitors and prices:
   - **Search 1:** the eIDAS platform at €110–150 + VAT named by Moncloa.com [F]; Legal Pigeon's prices; RedClaimer at €99.90 [F]; Debitura, Absolut, Recobrarte and Intercobros [F]; and any "plataforma MASC online".
   - **Search 2:** per-send prices for burofax, BuroMail, BuroSMS, Correos online burofax, Logalty and eGarante; MASC modules in MN Program, SuDespacho and Aranzadi Fusión; dunning or MASC flows in Holded, Quipu and Anfix.
   - **(g):** does anyone publish court-by-court acceptance criteria?
5. (c) [F] CGPJ data:
   - monitorios per quarter and the share under €2,000;
   - civil filings since Apr 2025, and any statistics on MASC-related inadmissions;
   - evictions, using 25,540 (C-15).
6. (f) [S] The monitorio threshold (€2,000) for acting without a lawyer and procurador; reserved-activity limits on generating offers for non-lawyers; and GDPR for debtor data.
7. (d)(e)(h) [I] Kill tests:
   - fewer than about 1 in 4 creditors would pay €20 or more per claim;
   - a valid certified send costs more than about €15;
   - more than 10% of pilot files are inadmitted.

   Desk proxy: the certified-send prices from check 4. Channel test: would invoicing tools host a "start MASC" button?

**IDEA-02 Receivables autopilot** (2 searches)
1. (b)(g) [F] Pricing and feature pages of Holded, Quipu, TS Facturas, Anfix, Contasimple, FacturaDirecta and Cuéntica: automatic reminders and late-payment interest, and on which tier. If an entry tier ships both, that is a kill criterion.
2. (a) [S] The BOE resolution setting the H2 2026 statutory interest rate (10.40% is single-source), plus Ley 3/2004 arts. 7–8 on the €40 [F, BOE consolidated text].
3. (b) [F] Banktrack, Agicap, Embat and Qonto: per-customer payment-date prediction, and prices.
4. (f) [S] Licensed bank-aggregation providers in Spain and their prices, and whether a partner licence is enough. Also GDPR and credit-information limits on sharing payer scores.
5. (d)(e)(h) [I] Would B2B autónomos switch on interest notices framed as "waived if paid by a date"? Kill if fewer than half of trial users keep reminders on after 60 days. Channel: invoicing-software marketplaces [F].

**IDEA-03 E-invoice inbox and status reporter** (3 searches)
1. (a) [F] Orden HAC/1028/2026 and RD 238/2026:
   - which statuses are mandatory;
   - the real reporting deadline (is it 4 calendar days?);
   - who reports in 2028 and who in 2029, which resolves C-05;
   - the sanctions (€10,000 is single-source).
2. (a)(f)(h) [F] The AEAT's SPFE pages: is there an interface for third-party software, and when are the technical specifications due? Must a receive-and-report tool register as a private exchange platform under RD 238/2026? No programmatic access is a kill criterion.
3. (b)(g) [S]×2 Status-reporting roadmaps of B2Brouter [F prices], TS Facturas, Holded, Quipu, Anfix, a3 and Sage, and the list of Spanish Peppol access points.
4. (c) [S] How many firms have turnover above €8M, and how many suppliers do they have? This is a TAX-05 gap.
5. (f) [F] The LGS art. 13.3 bis self-certificate: when it applies, and the 10-working-day deadline.
6. (d)(h) [I] Asesoría bulk price of €1–3 per client. Kill if the SPFE's own app covers receiving, reporting and bank matching for free.

**IDEA-04 VeriFactu retrofit adapter** (3 searches)
1. (a) [F] The AEAT FAQ, Hacienda's note and the BOE: has the move to October 2028 been published, and by which instrument (C-08)? Batch 1 owns this check for batches 2 and 4.
2. (f)(h) [S] DGT binding rulings and AEAT criteria on middleware that makes legacy tills or scales compliant. Producer duties under Orden HAC/1177/2024 (the declaración responsable) [F, BOE]. A ruling against external capture is a kill criterion.
3. (b)(d) [S] Leading scale and POS brands in Spain and their VeriFactu upgrade quotes, to test ATA's €1,800–2,500. Quotes below about €300 are a kill criterion.
4. (b)(g) [S] TicketBAI-era retrofit products in the Basque Country, and how they were certified.
5. (c) [F] INE DIRCE counts of retailers using scales and of hospitality businesses, by city.
6. (e) [I] Will POS and scale installers partner?

**IDEA-05 Fair-terms invoicing** (2 searches)
1. (b)(d) [F] Vendor pricing pages, to settle C-10:
   - Holded's 250-invoice cap and its three conflicting prices;
   - TS Facturas/Billin, Contasimple, Anfix, FacturaDirecta, Cuéntica, Declarando VeriFactu Plus.
2. (b) [F] The guide to the AEAT's free VERI*FACTU app: limits on volume, simplified invoices and export.
3. (b)(g) [S] Who owns Contasimple (Shine or Cegid)? Which vendors already offer a free archive after cancellation, or one-click cancellation?
4. (b) [S] An "alternativa a Holded" scan: new cheap entrants in 2026.
5. (a) [F] Record-keeping periods, and whether the copies the SPFE holds satisfy them.
6. (e)(h) [I] Would 10 gestorías accept or promote a new tool if it exports to their a3 or Contasol? Kill tests:
   - acquiring a customer through gestorías costs more than 12 months of revenue;
   - fewer than 1 in 5 users who complained about an incumbent would switch.

   Also benchmark the support cost with WhatsApp pricing [F].

**IDEA-11 IBAN-change guard** (2 searches)
1. (a)(h) [S] Regulation (EU) 2024/886: Verification of Payee duties and dates, and what Spanish banks show business customers (C-06). Kill if VoP already makes IBAN-change fraud rare.
2. (b)(g) [S] Existing Spanish SME tools for IBAN checks and payment control, including banks' own offers.
3. (c) [F] Spanish loss figures for CEO/BEC and IBAN-change fraud, from the INCIBE 2025 release and the Banco de España report.
4. (f) [F] Does the RD 238/2026 e-invoice format carry a payee IBAN field?
5. (d)(e) [I] SME cyber-insurance prices and any premium discount for payment controls. Will SMEs pay €5/month before suffering a loss?

**IDEA-12 B2B contract guard** (2 searches)
1. (b)(g) [S] Spendbase and Spanish B2B subscription-management tools, and subscription detection in Qonto and the banks.
2. (c)(h) [S] How many software and telecom contracts does a micro firm hold (ONTSI, INE)? Kill if the median is under three.
3. (a)(f) [F] Protections for autónomos against auto-renewals and permanencias (https://www.infoautonomos.com/blog/internet/como-reclamar-un-servicio-de-telefonia-o-internet-siendo-autonomo), and the Kit Digital terms on post-subsidy obligations [F, programme page].
4. (d)(h) [I] A landing-page test aimed at former Kit Digital beneficiaries. Kill if under 40% are retained after three months.

**IDEA-13 Kit Digital website rescue** (2 searches)
1. (c) [S] Red.es and Acelera Pyme data: how many grants included a website, and the renewal rate after the subsidised year.
2. (b)(d)(g) [F] Arsys's post-subsidy prices and exit clauses [F]; whether hosting companies already market Kit Digital migrations (the offer is copyable overnight); other agentes digitalizadores' terms [S\*].
3. (f)(h) [S] Which site builders the agents used, and whether sites and domains can be exported, plus low-cost hosting prices in Spain. Kill if most sites cannot be exported, or if median upkeep is under about €15/month.
4. (a) [F] How long beneficiaries had to keep the subsidised solution, and when they became free to cancel (programme page).

**IDEA-36 CAE document wallet** (3 searches)
1. (b)(d) [F] Competitor offers and prices:
   - DocuPRL's comparison and its own offer;
   - Dokify (€490/year for the principal; contractors from €102.90/year plus €15.44 per employee);
   - DocAcces, UCAE and PlayCAE pricing pages;
   - Nalanda's reviews.
2. (b)(g) [S] Does an "upload once, sync" wallet or a shared CAE credential already exist (Dokify's contractor network, Obralia, others)?
3. (f)(h) [F] What the terms of Nalanda, Dokify, Ctaima, e-coordina, Obralia and Metacontratas say about automated uploads or APIs. Kill if automation is forbidden and principals refuse share-links.
4. (c) [S] Subcontractors registered on the main platforms (vendor claims), how many platforms a typical subcontractor uses, and firm counts.
5. (f) [S] Is an electronic Libro de Subcontratación valid (regional habilitación), and can regional REA registries be queried? Also the rules on storing "apto" medical-fitness certificates.
6. (d)(e) [I] Interview 10 installers on monthly CAE hours and annual platform fees. Channel test: FENIE, CNC and external prevention services (SPAs) as resellers.

### Batch 2. Gestorías, the administration, owner-manager duties and public money (9 ideas, 24 searches)

**Ideas:** IDEA-06, IDEA-07, IDEA-08, IDEA-09, IDEA-10, IDEA-25, IDEA-26, IDEA-27, IDEA-28.

**Why together:**
- The gestoría is the buyer or the channel for IDEA-06 to IDEA-10, so the gestoría-economics checks are run once.
- IDEA-25 to IDEA-28 concern dealing with public bodies: licensing, grants, procurement, and disaster aid and claims.

**Search allocation:** IDEA-06 4; IDEA-07 4; IDEA-08 2; IDEA-09 3; IDEA-10 2; IDEA-25 3; IDEA-26 2; IDEA-27 2; IDEA-28 2. Total 24.

**Known pages to fetch:**
- Gestorías: Consejo General de Gestores, https://www.consejogestores.org/?p=14916.
- Tax and company law: LGT, https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186; LSC, https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544.
- Autónomos: Infoautónomos cuota page, https://www.infoautonomos.com/seguridad-social/cuota-de-autonomos-cuanto-se-paga/; the ENA 2025 survey, https://www.infoautonomos.com/club-cursos/wp-content/uploads/sites/2/2025/11/ESTUDIO-NACIONAL-DEL-AUTONOMO-INFOAUTONOMOS-ENA-2025.pdf.
- SL director duties: AyE on STS 1477/2026, https://www.autonomosyemprendedor.es/articulo/pymes/supremo-confirma-que-autonomos-societarios-pueden-asumir-deudas-sl-actuan-tiempo/20261022150439056494.html; Registradores yearbook, https://www.registradores.org/documents/d/guest/anuario-concursal-2025.
- Madrid licensing:
  - Agencia de Actividades service charter 2026, https://www.madrid.es/UnidadesDescentralizadas/Calidad/CARTAS%20SERVICIOS/SistemaCartasServicio/41%20CS_de%20la%20Agencia%20de%20Actividades/DEFINITIVA/CS_ADA_2026.pdf;
  - ECU prices 2026, https://www.madrid.es/UnidadesDescentralizadas/AgenciaActividades/ECUs/ficheros/AnexosI_II_III_IV_PreciosECU2026.pdf.
- Grants and procurement:
  - https://planderecuperacion.gob.es/;
  - the CEOE fund-execution report, https://www.ceoe.es/sites/ceoe-corporativo/files/content/file/2026/06/26/104/informe-ejecucion-fondos-europeos-junio-2026.pdf;
  - the OIReScon summary, https://www.hacienda.gob.es/rsc/oirescon/informe-anual-supervision-2025/ias2025-resumen-ejecutivo-es.pdf.
- Disaster aid:
  - La Moncloa DANA tracking, https://www.lamoncloa.gob.es/info-dana/Paginas/2026/191026-datos-seguimiento-actuaciones-gobierno.aspx;
  - eldiario.es on dana Adam claims, https://www.eldiario.es/comunitat-valenciana/consorcio-compensacion-seguros-recibe-6-500-solicitudes-indemnizacion-dana-adam_1_13605957.html, and aid, https://www.eldiario.es/comunitat-valenciana/gobierno-valenciano-aprueba-paquete-ayudas-23-5-millones-euros-afectados-dana-adam_1_13603195.html.

**IDEA-06 Gestoría client-obligation cockpit** (4 searches)
1. (c) [S] The number of gestorías, asesorías and graduados sociales (Consejo General de Gestores Administrativos, colegios, INE CNAE 69.20). Batch 2 owns this check.
2. (b)(g)(h) [S] Do a3 (Wolters Kluwer), TeamSystem/DELSOL, Sage Despachos, Cegid, Copilot Gestoría or Kabilio offer multi-client readiness dashboards or client-level obligation alerts, and at what price? Kill if a3 or Sage already shows cross-vendor readiness for all clients.
3. (b)(d) [S] What gestorías pay for legal-update services today, and whether any maps changes to client lists ("alertas normativas gestorías", "monitorización BOE IA").
4. (a) [F] Feed the rule-status board from batch 1's answers on VeriFactu and e-invoicing, plus the Consejo's draft-dates page (C-05, C-08). Record the MEI rate (C-03).
5. (f) [S] Is there an official list of software with a VeriFactu declaración responsable? Do a3 and Contasol export client master data in a usable form?
6. (d)(e)(h) [I] Interview 10–15 gestorías on hours per rule change, how they track clients' software, and willingness to pay. Kill tests:
   - fewer than 1 in 5 would pay €30/month or more;
   - "a spreadsheet handles it in a couple of hours per change";
   - fewer than 3 of 10 trial gestorías convert.

**IDEA-07 E-notification watchdog** (4 searches; batch 2 owns the access rules)
1. (f)(h) [S] Third-party access to the AEAT, DEHú and TGSS mailboxes:
   - the types of apoderamiento and colaboración social;
   - any recipient-side API, app push or SMS channel;
   - whether automated reading is allowed, and whether viewing the pending list counts as access;
   - whether a cloud service may hold an FNMT representative certificate.

   If access needs certificate custody that fewer than 30% of owners would accept, that is a kill criterion.
2. (b)(g) [S] IvNeos (Ivnosys): price, minimum size and coverage claim. Also other aggregators ("gestor de notificaciones electrónicas", "DEHú multiempresa"), and what gestorías charge to monitor notifications.
3. (a) [S] The AEAT resolution of 4 Jun 2026 on 24-hour embargoes and its roll-out; any Supreme Court ruling on missing alerts since Nov 2025; Audiencia Nacional 489/2026.
4. (c) [S] AEAT and TGSS figures on electronic notifications, deemed deliveries, enforcement surcharges and embargoes after unopened notices.
5. (a) [F] Ley 39/2015 (who must receive electronically; the 10-day rule) and the LGT. How do legal persons receive first court summonses?
6. (f) [F] Can BOE edictal notices be monitored automatically by NIF (BOE open data)?
7. (d)(h) [I] Pilot: kill if fewer than half of companies receive any notice within six months.

**IDEA-08 Hacienda letter shield** (2 searches)
1. (a) [F] RD 253/2025 and Orden HAC/747/2025 in the BOE: monthly modelo 170, with no minimum, and Bizum in scope.
2. (f)(h) [S] Can taxpayers or their representatives download the modelo 170 data reported about them?
3. (c)(h) [S] AEAT or Gestha figures on letters over card and Bizum mismatches. Today the only source is AyE's articles [F]. Kill if letters reach fewer than about 5% of B2C businesses a year.
4. (f) [F] Settlement exports or APIs at SumUp, Stripe, Redsys-based bank terminals and Bizum for business (vendor documentation).
5. (b)(g) [F] Reconciliation features of Holded, Quipu, Anfix, Declarando and TaxDown.
6. (d)(e) [I] Ask gestorías how many requerimientos they handle a year, and the hours each takes.

**IDEA-09 Cuota tracker** (3 searches)
1. (a) [F] Orden PJC/297/2026 for the 2026 tables, which settles the maximum-base conflict (C-09); the MEI for 2026 and 2027 (C-03); and the RDL 13/2022 net-income rules [F, BOE].
2. (a) [S] Did the Junts bill on societario bases lapse? What is the status of the 2027 bases? Has the TGSS corrected the method the Ombudsman criticised?
3. (c) [S] TGSS totals for the 2023–2025 regularisations (how many demands, and their average amount), and RETA membership.
4. (b)(g)(h) [S] Do Cuéntica, Infoautónomos, Declarando, TaxDown, Quipu or Holded track the tramo continuously or warn of band changes, and on which plans? Does Import@ss offer a simulator with alerts? Either would be a kill criterion.
5. (f) [F] Base-change windows and their effective dates, and which authorisation lets a third party view or change bases (Import@ss, RED).
6. (d)(h) [I] Kill if fewer than 1 in 10 trial users pay €2/month or more, or if retention collapses after one regularisation.

**IDEA-10 SL director guard** (2 searches)
1. (a) [F] Read STS 1477/2026 (through AyE) and the LSC articles on the dissolution cause, the two-month duty and directors' liability.
2. (c) [S] The number of SLs, the share filing abbreviated accounts, and how many fail to deposit accounts (Registradores, INE).
3. (b)(g)(h) [S] Do a3, Contasol, Holded, Quipu or Anfix alert on the half-capital trigger? Any accounting vendor could add the ratio, so this is also the copy-risk test. If so, that is a kill criterion.
4. (c) [F] The Registradores insolvency yearbook, for data on liability claims.
5. (e)(h) [I] Would asesorías pay for it or distribute it? Kill if they will not distribute it.

**IDEA-25 Pre-lease "can I open here?" check** (3 searches)
1. (f)(h) [S] Is Madrid's planning and land-use data available as open GIS data, and is the same true for Barcelona, Valencia, Sevilla and Málaga? Unusable data is a kill criterion.
2. (a)(c) [F] Madrid's service charter and its 2026 ECU price annex: actual 2025 performance against the 109-day and 137-day standards, and the share of files handled by ECUs. Also confirm the 2027 prices approved on 15 Oct 2026.
3. (b)(g)(h) [S] Competitors: "informe viabilidad local comercial online", "consulta compatibilidad urbanística online", ECUs' own pre-checks, and how much Málaga's free ALU is used. Kill if ECUs or architects answer free as lead generation.
4. (a)(d) [S] The cost and speed of Madrid's paid urban-planning consultation, and the status of València's new licensing ordinance.
5. (d)(e) [I] Would franchise expansion teams and commercial agents pay €199/month?
6. (f) Note the liability and professional-liability insurance a preliminary verdict needs.

**IDEA-26 Grant justification workspace** (2 searches)
1. (c)(h) [S] How many SME beneficiaries outside Kit Digital justify grants themselves (BDNS), and which five programmes have the most of them in 2026–2027. Kill if under a quarter manage justification themselves.
2. (a) [F] planderecuperacion.gob.es and the CEOE June 2026 report: any extension to 2028, and the status after 31 Aug 2026.
3. (b)(d)(g) [S] Competitors ("software justificación subvenciones", "gestión de subvenciones pymes"), Fandit's roadmap and €56–600 pricing [F, vendor page], and consultancy fee models.
4. (c) [S\*] Repayment proceedings opened in 2025–2026 (IGAE, Tribunal de Cuentas).
5. (e)(h) [I] Would consultancies pay €149/month?

**IDEA-27 Small public-contract radar** (2 searches)
1. (a)(f)(h) [S] What share of contracting bodies publish their minor contracts (object, amount, supplier), where and in what format, and what the law requires. Kill if fewer than half of sampled municipalities publish supplier and amount.
2. (b)(d)(g)(h) [S] Since plain tender alerts are commoditised, the copy-risk test is whether anyone already holds a normalised minor-contract dataset. licitaciones.es pricing and whether it covers minor contracts (if so, a kill criterion); other tools ("buscador contratos menores", "alertas licitaciones pymes precio"); PLACSP's free alerts.
3. (c) [F] The OIReScon summary: the SME share of public contracts and the data gaps.
4. (d)(e) [I] Interview 20 micro suppliers in cleaning, maintenance and IT on willingness to pay and late-payment fears (FIN-04).

**IDEA-28 Flood-ready evidence vault** (2 searches)
1. (a)(c) [F] The La Moncloa and eldiario.es pages: the evidence the Consorcio and the AEAT required in 2024, the causes of delay, the share of dana Adam claims from businesses, and the contents of the second aid package.
2. (b)(g) [S] Do Spanish insurers already offer pre-loss inventory apps?
3. (c) [S] How many businesses sit in official flood-risk zones in the Valencia region?
4. (e)(h) [I] Will brokers or gestorías distribute a €4 vault? Kill if no insurer, broker or gestoría network agrees to a pilot, or if pre-event sign-up converts below 2%.

### Batch 3. Employers, care and regulated professions (9 ideas, 24 searches)

**Ideas:** IDEA-16, IDEA-17, IDEA-18, IDEA-19, IDEA-40, IDEA-41, IDEA-42, IDEA-43, IDEA-44.

**Why together:**
- They share labour-law and Social Security sources: the time-recording decree, RD 723/2026, the minimum wage, LAB-01 limits on location tracking, and employer counts (C-04).
- Each sells to a regulated profession through its colegio or association: graduados sociales, health colegios, the OCV, driving-school bodies, SAD employers.

**Search allocation:** IDEA-16 3; IDEA-17 3; IDEA-18 3; IDEA-19 3; IDEA-40 2; IDEA-41 2; IDEA-42 3; IDEA-43 3; IDEA-44 2. Total 24.

**Known pages to fetch:**
- BOE:
  - RD 723/2026, https://www.boe.es/eli/es/rd/2026/09/09/723;
  - RD 239/2026, https://www.boe.es/eli/es/rd/2026/03/25/239;
  - RD 767/2025, https://www.boe.es/eli/es/rd/2025/09/02/767.
- Labour sources:
  - INE DIRCE 2025, https://www.ine.es/dyngs/Prensa/DIRCE2025.htm;
  - El Español on the Consejo de Estado opinion, https://www.elespanol.com/invertia/economia/empleo/20260323/consejo-critica-tumba-registro-horario-yolanda-diaz/1003744181041_0.html;
  - El Derecho on ITSS working-time fines, https://elderecho.com/inspeccion-de-trabajo-elevo-un-9-las-multas-por-infracciones-por-tiempo-de-trabajo-en-2024;
  - Law&Trends on record dismissal claims, https://www.lawandtrends.com/noticias/laboral/las-demandas-por-despido-marcan-record-en-el-segundo-trimestre-con-45-230-procedimientos-1.html;
  - PwC on the SMI, https://periscopiofiscalylegal.pwc.es/se-fija-la-cuantia-del-smi-el-problema-ahora-es-como-aplicarlo/.
- Household employers: INSST on Prevencion10, https://www.insst.es/documents/d/portal-insst/yolanda-diaz-presenta-la-herramienta-para-evaluar-los-riesgos-laborales-de-las-trabajadoras-del-hogar-nota-de-prensa; El Salto, https://www.elsaltodiario.com/trabajo-domestico/prevencion10-herramienta-evaluacion-riesgos-empleo-hogar.
- Health professions: Infocop, https://www.infocop.es/?p=50249.
- Veterinary: MAPA PRESVET, https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/Higiene-de-la-produccion-primaria-ganadera/medicamentos-veterinarios/Presvet.aspx; Colvet, https://colvet.es/files/reportajes/informacionveterinaria_marzo_2025.pdf.
- Driving tests: DGT note of 16 Jun 2026, https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/2026/20260616-nota-de-prensa.pdf; Motor.es, https://www.motor.es/noticias/pere-navarro-dgt-enfurece-autoescuelas-listas-espera-2026114254.html.
- Home help: TED notice, https://ted.europa.eu/es/notice/92082-2025/pdf; the Vigo contract, https://vigoe.es/vigo/local/vigo-pone-en-marcha-uno-de-sus-megacontratos-y-caballero-exige-que-lo-pague-la-xunta.

**IDEA-16 Labour compliance pack** (3 searches)
1. (a) [S] Was the digital time-recording decree approved after 23 Oct 2026, and with what transition period and technical requirements? Will it stall under a caretaker government after 29 Nov? Batch 3 owns this check.
2. (a) [F] RD 723/2026: did SEPE publish the model document, and do LISOS sanctions apply to missing statements?
3. (b)(g)(h) [S] Do a3innuva (Wolters Kluwer), Sage or Nominasol (DELSOL) give gestorías a client portal with time recording and RD 723 statements, and at what price? If one does so at no extra cost, that is a kill criterion.
4. (b)(d) [F] Vendor pricing pages: Woffu Lite (€1.5 per user for up to 10), Holded's HR add-on (€1.50), Timu, Sesame (15-employee minimum), Factorial and Kenjo. Free time-recording apps [S\*].
5. (c) [S] INE DIRCE counts of businesses with 1–2, 3–5 and 6–9 employees, which settles the employer-count conflict (C-04) for all batches. Also the share still recording hours on paper.
6. (e)(d)(h) [I] Would gestorías resell at €1 per employee per month? Kill if a 10-gestoría pilot converts fewer than 15% of employer clients within three months. Note C-18 on working-time fines.

**IDEA-17 Guided dismissal workflow** (3 searches)
1. (d) [S] What gestorías, graduados sociales and labour lawyers in Madrid, Barcelona and Valencia charge to prepare a dismissal and attend SMAC.
2. (b)(g) [S] Competitors: "software despidos graduados sociales" and "generador carta de despido"; termination workflows in a3innuva, Sage, Factorial and Sesame; free severance calculators.
3. (a) [S] Verify the pre-dismissal hearing ruling (reported as an STS of 18 Nov 2024) and any 2026 refinements, plus STS 526/2026 and the CRA 0054 coding under RED 8/2026.
4. (f) [I] Reserved activities: may software generate dismissal letters for employers without a licensed professional? Ask the Consejo General de Graduados Sociales and a bar association.
5. (c) [F] SMAC volumes and settlement rates (MITES statistics; the 2025 PDF returned an error); claim volumes from Law&Trends.
6. (h) [I] Kill if fewer than 1 in 5 advisers would pay €79/month, or if owners convert at under 2% at the moment of need.

**IDEA-18 Convenio rules API** (3 searches)
1. (c) [S] How many convenios are in force, how many are provincial, and how many workers the top 50 cover (Ministry of Labour statistics, REGCON).
2. (b)(g)(h) [S] Does REGCON or any official source publish convenio content in structured form? Are there convenio databases or APIs ("API convenios colectivos", "tablas salariales convenios actualizadas"), or legal publishers' convenio products? A public structured source is a kill criterion.
3. (b)(h) [S] Do a3innuva, Sage, Nominasol and PayFit ship convenio pay tables and leave and sick-pay rules, and do Factorial, Sesame and Woffu rely on manual set-up? Kill if 3 of the 5 largest HR vendors already hold this data.
4. (a) [S\*] The status of the announced decree-law barring the absorption of certain supplements (LAB-03), and its lapse risk.
5. (d)(e) [I] Seek letters of intent from 2–3 HR vendors and 10 gestorías at the proposed prices.
6. (f) Note the cost of an accuracy commitment and of professional-liability insurance.

**IDEA-19 Household-employer autopilot** (3 searches)
1. (b)(g) [S] Domestic-employer apps, payroll platforms and agencies in Spain, with prices.
2. (a) [S] Labour-inspection actions and fines under RD 893/2024 since Nov 2025, and the status of the pending guide, harassment protocol and training platform.
3. (a) [F] Must households keep time records for domestic workers? Reuse IDEA-16's decree answer and the INSST release.
4. (f) [S] Can a third-party app register workers and manage contributions on a household's behalf? Which Social Security authorisations does that need?
5. (c) [F] Settle C-22 (348,000, 378,000 or 540,000) from the INSST release and Social Security affiliation data.
6. (d)(h) [I] Survey about 200 employing households on what they pay a gestoría today. Kill if fewer than about 1 in 10 would pay €5/month.

**IDEA-40 Private-pay kit for health professionals** (2 searches)
1. (c)(h) [S] What share of private health policies include reimbursement cover, and what documents Adeslas, Sanitas, Asisa, DKV and Mapfre require. Kill if only a small minority holds such cover.
2. (a) [S] The status of the CNMC request of Mar 2026 and of Unipromel's MUFACE challenge at the Audiencia Nacional.
3. (b)(g) [F] Do Clinni, Doctoralia/Docplanner, Gesden or Clinic Cloud offer payer-mix analytics or reimbursement invoices (vendor pages)?
4. (c) [F] Colegio censuses of self-employed physiotherapists, podiatrists, dietitians and speech therapists; Infocop for psychologists.
5. (f) [F] Colegio deontological codes on advertising private sessions as reimbursable.
6. (d)(e) [I] Interview 15 panel professionals on insurers' share of revenue, € per session, and appetite for private pay.

**IDEA-41 RD 239/2026 staff file** (2 searches)
1. (a) [F] RD 239/2026: the deadline (six months from 1 Jul 2026?) and the scope (all centres authorised under RD 1277/2003; existing and new staff).
2. (a)(h) [S] How the inspectorates of Madrid, Catalonia, Andalusia and Valencia will check, and whether they will publish a format. Kill if there is no format and no check.
3. (b)(g)(h) [S] Staff-credential features in Clinni, Doctoralia, Gesden, Clinic Cloud, Flowww and Koibox. Kill if the main vendors add it free before January 2027.
4. (c)(f) [F] REGCESS and the regional registers of authorised centres; colegio online lookups or APIs for colegiación status.
5. (d) [I] Interview 10 clinic managers about awareness and plans.

**IDEA-42 PRESVET file for vet clinics** (3 searches)
1. (c) [F] The MAPA PRESVET page: confirm the 16,460 clinicians, and whether "80% automated" refers to clinicians or prescriptions (C-23).
2. (f) [S] Is there a public PRESVET web-service specification for third-party software, and what does onboarding require?
3. (b)(g)(h) [S] Which practice-software vendors (Qvet and others) integrate PRESVET, at what price, and do they check categories and antibiograms? If they already do, that is a kill criterion.
4. (a)(h) [S] Was the sanctions reform passed, or did it lapse with the dissolution? Any inspections or fines in 2025–26? Kill if the colegios report none.
5. (a) [F] RD 767/2025: the format and frequency for documenting antibiotic-reduction measures.
6. (c)(e) [S\*] The number of companion-animal clinics (OCV census) and the colegio channels (Colvet).

**IDEA-43 Driving-school readiness tracker** (3 searches)
1. (c) [S] The number of driving schools by province (DGT registry; CNAE, the driving-schools confederation).
2. (a)(h) [S] The current CAPA formula: does a higher pass rate raise a school's slot allocation? If not, that is a kill criterion.
3. (b)(d)(g) [S] Driving-school management software in Spain, with prices, and whether any already scores lessons. The scoring is copyable unless outcome data accumulate.
4. (a) [F] The DGT note of 16 Jun 2026 and Motor.es: settle the queue-size conflict (C-20), and find what readiness evidence the DGT asks for in reinforcement sessions.
5. (f) [S\*] Are the DGT's practical-exam assessment criteria public and usable for a rubric?
6. (d)(e) [I] Interview 10 schools in Sevilla, Madrid, Barcelona and Valencia on how they choose whom to present, and on willingness to pay.

**IDEA-44 SAD route planning and visit verification** (2 searches)
1. (c) [S] The number of SAD providers and of SAD hours in Spain (IMSERSO, dependency statistics).
2. (b)(g)(h) [S] Existing SAD software vendors and prices, and whether SAD tenders in Madrid, Barcelona, Valencia and Sevilla require visit verification or specific formats; the TED notice [F]. Kill if tenders mandate council-supplied systems or specialised software is already cheap.
3. (a) [F] The Vigo contract, and the regional transposition of the 2029 accreditation targets.
4. (f) Note the labour-law limits on location-based check-in, reusing IDEA-16's LAB-01 findings.
5. (d) [I] Interview five small SAD operators.

### Batch 4. Consumer-facing shops, hospitality and personal services (9 ideas, 24 searches)

**Ideas:** IDEA-14, IDEA-20, IDEA-21, IDEA-22, IDEA-23, IDEA-24, IDEA-37, IDEA-38, IDEA-39.

**Why together:**
- They share Ley 10/2025 consumer law: complaint clocks, verified reviews, return fees, deposits and phone sales.
- They share the AEPD and CCTV evidence used by IDEA-23 and IDEA-24.
- They have the same buyers (shops, bars and salons) and the same channels (POS, booking and PMS vendors; trade associations).

**Search allocation:** IDEA-14 2; IDEA-20 4; IDEA-21 3; IDEA-22 3; IDEA-23 2; IDEA-24 3; IDEA-37 2; IDEA-38 2; IDEA-39 3. Total 24.

**Known pages to fetch:**
- BOE:
  - Ley 10/2025, https://www.boe.es/eli/es/l/2025/12/26/10;
  - LO 1/2026, https://www.boe.es/eli/es/lo/2026/04/08/1/con;
  - Ley 1/2025, https://www.boe.es/eli/es/l/2025/04/01/1/con;
  - RD 126/2015, https://www.boe.es/eli/es/rd/2015/02/27/126;
  - Ley 17/2011, https://www.boe.es/eli/es/l/2011/07/05/17.
- Ley 10/2025 and phone sales:
  - the KPMG alert on Ley 10/2025, https://assets.kpmg.com/content/dam/kpmgsites/es/pdf/2026/01/legal-alert-regulacion-servicios-atencion-clientela-ley-10-2025.pdf.coredownload.inline.pdf;
  - La Moncloa on the 400 prefix, https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/Paginas/2026/160426-prefijo-400-llamadas-comerciales.aspx.
- Data protection: BDO AEPD 2025, https://es-admin.bdo.global/getattachment/29fdc619-d1c8-40fd-af4f-57757c6ceb21/AEPD-2025.pdf?lang=es-ES; Lawwwing, https://lawwwing.com/aepd-sanciones-2025/.
- Consumer complaints: NacióDigital, https://naciodigital.cat/societat/nomes-7-denuncies-vulnerar-drets-linguistics-consumidors-han-acabat-en-sancio.html; Chekin on Hoj@, https://chekin.com/blog/boja-andalucia-nuevo-sistema-hoj-de-quejas-y-reclamaciones/.
- Shop theft: The Objective, https://theobjective.com/economia/2025-11-04/hurtos-perdida-2817-millones-comercios-espanoles/; Última Hora on AECOC, https://www.ultimahora.es/noticias/comunidades/2025/12/05/2525909/aecoc-celebra-reforma-multirreincidencia-causa-perdidas-comerciales-2800-millones.html.
- Returns: ShippyPro vs Outvio, https://www.shippypro.com/es/shippypro-vs-outvio; Sendcloud pricing, https://hackceleration.com/es/labs/sendcloud-precio.
- Salons:
  - Treatwell partner prices, https://www.treatwell.es/partners/precios/;
  - Booksy's price blog, https://biz.booksy.com/es-es/blog/cuanto-cuesta-un-software-de-reservas-para-salones;
  - Pabau on Booksy, https://pabau.com/es/blog/booksy-precio/;
  - DBK, https://dbk.es/en/estudios/16575/summary;
  - WhatsApp pricing, https://developers.facebook.com/docs/whatsapp/pricing/.
- Reviews: Merca2 on review attacks, https://www.merca2.es/2026/04/28/resenas-bar-google-2373862/.

**IDEA-14 Review-attack alarm** (2 searches)
1. (c)(h) [S] Spanish data on how often review extortion and review bombing happen (police, OCU, hospitality associations). Kill if fewer than about 1 in 20 restaurants is attacked a year.
2. (f)(h) [F] Google Business Profile and Tripadvisor terms and quotas for automated monitoring (platform developer pages). If listings cannot be monitored within the terms, that is a kill criterion.
3. (b)(d)(g) [S] OnbrandinG and other Spanish reputation tools, with prices.
4. (a) [F] The legal basis and fines for fake reviews, and the Ley 10/2025 duty to say whether reviews are verified (art. 20.4).

**IDEA-20 B2C complaint-clock kit with Hoj@ and Catalan modules** (4 searches; batch 4 owns the Ley 10/2025 transitional-period check)
1. (a) [F] Ley 10/2025: does the 12-month adaptation period (transitional provision 1) cover the art. 21 TRLGDCU amendments?
2. (a)(h) [S] Read the Andalusian Order of 24 Apr 2026 (BOJA nº 82, 30 Apr 2026), Decreto 82/2022 and the fines in art. 71.8.3ª of Ley 13/2003. Does Hoj@ send reminders, or offer an API or delegated users? Kill if the Order does not impose these duties, or if Hoj@ already sends reminders.
3. (a)(c)(h) [S] Inspections or fines in 2026 for missing ID keys or late answers; complaint volumes at municipal consumer offices (OMIC); sanction ranges in the consumer laws of Madrid, Andalucía, the C. Valenciana and Cataluña. Kill if no regional authority has enforced the new duties by mid-2027.
4. (b)(g) [S]×2 Competitors and the threat of bundling:
   - **Search 1:** "software gestión reclamaciones clientes pyme" and "libro de reclamaciones digital".
   - **Search 2:** complaint or Hoj@ modules in POS, booking, PMS, gym and helpdesk tools, and gestoría offers.
5. (c) [F] INE DIRCE counts of B2C SMEs by sector, and of consumer-facing firms in Andalusia.
6. (d) [F] Settle C-19 on Catalan-language complaints from NacióDigital. [I] Would Catalan businesses pay for the module?
7. (f) Note whether AI-drafted replies are acceptable, and who is liable for mistakes.
8. (h) [I] Kill if fewer than 1 in 5 of 30 interviewed B2C owners has faced a consumer-office case or worries about the 15-day rule.

**IDEA-21 Call-consent ledger** (3 searches)
1. (a)(h) [S] Find the BOE reference and text of the 400-prefix resolution (La Moncloa [F]). Does it cover B2B calls and calls involving autónomos? A B2B exclusion combined with a collapse of B2C cold-calling is a kill criterion.
2. (a) [F] The two-year consent window in TRLGDCU art. 62.1 as amended, and how it applies to existing customers.
3. (f) [S] The Lista Robinson's access terms and fees for companies (run by ADigital).
4. (b)(g)(h) [S] Consent-management features in Aircall and in the other cloud-telephony and CRM tools used in Spain ("software consentimiento llamadas comerciales"). Kill if the two largest cloud-telephony vendors in Spain ship consent gating by Q1 2027.
5. (c) [F] Counts from the DGSFP register of insurance agents and brokers, and the CNMC list of energy retailers.
6. (a) [S\*] What has happened since 17 Oct 2026: blocked-call statistics, SME complaints, voided-contract cases.

**IDEA-22 Customer-service kit for basic-service providers** (3 searches)
1. (c)(h) [S] How many firms fall under art. 2.1 regardless of size (CNMC registers, transport-operator registers, municipal water companies), and how many are SMEs? Kill if fewer than about 500 SME providers remain in scope.
2. (a) [F] The KPMG alert and Ley 10/2025: do internet providers follow Ley 10/2025, or their own sector rules first? Is there any sign the 28 Dec 2026 deadline will be extended?
3. (f)(d)(h) [S] Which standard or method ENAC-accredited auditors will apply, what the annual audit costs, and how the 95%-within-3-minutes rule will be measured. Kill if auditors accept standard helpdesk reports.
4. (b)(g) [S] Competitors ("software cumplimiento Ley 10/2025", "auditoría atención al cliente ENAC"), and whether the cloud PBXs sold to small ISPs already report these metrics.
5. (e) [I] Will accredited auditors act as referral partners?

**IDEA-23 CCTV compliance kit** (2 searches)
1. (a)(h) [S] Typical AEPD outcomes and fine amounts in small-business video-surveillance cases, from a sample of 2025–2026 resolutions. Settle the AEPD totals (C-07) from BDO and Lawwwing [F]. Kill if typical cases end in warnings or fines under €500.
2. (b)(g) [F] Does Facilita, or another free AEPD tool, already generate CCTV signs and records (AEPD tool pages)?
3. (b) [S] Competitors ("kit RGPD videovigilancia", "cartel zona videovigilada descargar") and CCTV modules in data-protection SaaS, such as Lawwwing at €9.9–79/month [F].
4. (c) [S\*] How many businesses and comunidades run CCTV (security-industry or AEPD data)?
5. (e)(h) [I] Would installers bundle the kit? If not, that is a kill criterion.
6. (f) Note whether a software provider can prepare an AEPD response pack without that counting as legal representation.

**IDEA-24 Shop theft incident log** (3 searches)
1. (a) [F] LO 1/2026 consolidated text: is it in force, has the €400 threshold gone, and what does LECrim art. 105.3 now allow? This settles C-02.
2. (f)(h) [S] Can a shop file a theft report online with attachments with the Policía Nacional, the Mossos d'Esquadra and the Ertzaintza, and what evidence do prosecutors need for a delito leve de hurto? Kill if the main forces will not accept prepared packs.
3. (b)(g)(h) [S] Incident-reporting tools or programmes in Spain (AECOC, COCEM, local associations, police shop-safety schemes) and abroad (for example Auror), with prices. A free association or council tool is a kill criterion.
4. (a)(c) [S] Has any council used LECrim art. 105.3 since April 2026 (Madrid, Barcelona, Valencia)? Get the Barómetro del Hurto breakdown by shop size, and settle €2,817M against €2,917M (The Objective, Última Hora [F]).
5. (f) [S\*] AEPD guidance on handing CCTV clips to police, and on retention periods.
6. (d)(e)(h) [I] Interview 15–20 food and convenience shops on the share of incidents reported, time per report and willingness to pay €9–15/month. Kill if fewer than a third would report more with a one-minute flow.

**IDEA-37 APPCC, allergen and food-waste logbook** (2 searches)
1. (b)(d)(g)(h) [S] Digital APPCC apps and sensor kits sold in Spain, with prices; whether Qamarero sells its own module; whether the Last.app, Qamarero, Revo or Ágora allergen modules comply with RD 126/2015. Kill if several apps sell for €5/month or less, or if POS suites include it free.
2. (a)(h) [S] How often APPCC and allergen records are inspected and sanctioned in Madrid, Catalonia and Andalusia, and whether inspectors accept digital and photo logs. Kill if inspectors rarely ask.
3. (a) [F] Ley 1/2025: the art. 6 dates (C-12) and which establishments are covered; also RD 126/2015 and Ley 17/2011.
4. (d)(e) [I] What APPCC consultancies charge for a plan plus yearly maintenance, and whether they would resell.

**IDEA-38 Returns and exchange portal** (2 searches)
1. (b)(d)(h) [F] Entry plans at Sendcloud (free; Lite at €28), Outvio (about €375) and ShippyPro (€207.20), from the vendor pages and the comparison pages listed above. Kill if a plan under about €30/month already offers exchange-first flows and returner rules.
2. (b)(g) [S] Returns apps active in Spain, with € prices: ZigZag, Loop Returns, AfterShip Returns, ReturnGO.
3. (f) [S] May a Spanish shop charge return shipping only to serial returners, or inspect before refunding, under the consumer law as amended by Ley 10/2025? Batch 4 owns this check.
4. (c) [S\*] The number of Spanish online fashion and footwear SMEs, and the handling cost per return.
5. (d)(h) [I] Interview 10 small fashion e-shops. Kill if the cost turns out to be logistics rather than abusive returners.

**IDEA-39 Salon direct booking** (3 searches)
1. (b)(g)(h) [S] Free and low-cost booking tools used by Spanish salons, and their fees: Fresha, Reserve with Google, Bewe, AgendaPro. Kill if a free tool with the same features is widely used.
2. (b)(d) [F] Treatwell's and Booksy's current terms (12-month minimum, Boost cap, data export), from the Treatwell pricing page, Booksy's blog and Pabau; Koibox and Flowww on Capterra.
3. (f) [S] May salons charge no-show deposits or fees under the consumer law as amended by Ley 10/2025? This shares batch 4's consumer-law check.
4. (c) [S] Settle the salon count (C-21) with INE DIRCE (CNAE 96.02), and look for Spanish no-show data for salons.
5. (f)(d) [F] Spain's WhatsApp Business Platform rates for utility messages, and whether click-to-chat reminders work at scale.
6. (d)(e)(h) [I] Interview 20 salons in Madrid and Valencia on bookings from marketplaces against repeat clients, and on commissions paid. Kill if repeat clients already book by WhatsApp or phone at no cost.

### Batch 5. Housing, short-term rentals and property, with user idea U1 (7 ideas, 24 searches)

**Ideas:** IDEA-29 [U1], IDEA-30, IDEA-31, IDEA-32, IDEA-33, IDEA-34, IDEA-35.

**Why together:**
- All of them hang on RDL 29/2026 (batch 5 owns that check), on regional rental and tourist rules, and on the same channels: agencies, administradores and manager associations.
- IDEA-30 shares its rules engine with IDEA-29 (section 2.0), so the validator should judge whether IDEA-30 is a light tier of IDEA-29.

**Search allocation:** IDEA-29 8 (full treatment); IDEA-30 3; IDEA-31 3; IDEA-32 4; IDEA-33 3; IDEA-34 2; IDEA-35 1. Total 24.

**Known pages to fetch:**
- Mid-term lease rules:
  - RDL 29/2026, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20823;
  - on its convalidation, https://gestionatualojamiento.com/convalidacion-del-decreto-de-vivienda/;
  - idealista on the October decrees, https://www.idealista.com/news/inmobiliario/vivienda/2026/10/13/918359-que-cambia-para-los-propietarios-con-los-decretos-prorrogas-tope-al-alquiler-del-2;
  - idealista on re-classification, https://www.idealista.com/news/inmobiliario/vivienda/2026/07/06/901838-la-clave-no-es-la-duracion-cuando-un-alquiler-de-temporada-pasa-a-ser-de-vivienda;
  - Consumo's seasonal-rental estimate, https://www.idealista.com/news/finanzas/economia/2026/09/07/912998-consumo-estima-que-mas-de-un-millon-de-personas-vive-en-alquiler-de-temporada-o-de;
  - seasonal listing shares, https://www.pressdigital.es/articulo/economia/2026-10-20/6058369-oferta-alquiler-permanente-cae-10-espana-mientras-temporal-crece-7-segun-idealista;
  - Catalonia's first rent-cap sanctions, https://consum.gencat.cat/ca/detalls/noticia/primers-sancionadors-contencio-preu-lloguers;
  - deposit penalties, https://www.elespanol.com/sociedad/20260318/entrado-vigor-penalizara-caseros-no-depositen-fianza-comunidad-autonoma/1003744163850_0.html.
- Caps, screening and insurance:
  - OCU on the new tensioned zones, https://www.ocu.org/fincas-y-casas/gestion/alquiler/analisis/2026/10/nuevas-zonas-tensionadas-cataluna;
  - OCU's rent-default insurance comparison, https://www.ocu.org/fincas-y-casas/gestion/seguros-y-prestamos/analisis/2026/07/comparativa-seguros-impago-rentas;
  - the Alquiler Seguro fine, https://www.noticiasdenavarra.com/economia/2025/10/27/consumo-propone-multar-alquiler-seguro-10269149.amp.html.
- Tourist rentals and taxes:
  - the Airbnb fine, https://www.dsca.gob.es/es/comunicacion/notas-prensa/justicia-obliga-airbnb-pagar-64-millones-euros-previstos-multa-que-le;
  - the BOPV (Gipuzkoa's Norma Foral 3/2026), https://www.euskadi.eus/bopv2/datos/2026/06/2602836a.pdf;
  - Chekin pricing, https://chekin.com/en/pricing/;
  - Forbes on the Catalan tax, https://forbes.es/economia/879865/el-parlament-aprueba-la-ley-que-incrementara-la-tasa-turistica-a-partir-del-1-de-abril/;
  - RD 933/2021, https://www.boe.es/eli/es/rd/2021/10/26/933.
- Owners' communities: LPH, https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906; idealista on inmho, https://www.idealista.com/news/inmobiliario/empresas/2026/07/30/906830-50-empresas-compradas-al-ano-y-menos-del-3-de-cuota-asi-es-inmho-en-el-sector.
- AML: SEPBLAC, https://www.sepblac.es/wp-content/uploads/2024/10/sujetos_obligados_ley_10_2010.pdf; finreg360, https://finreg360.com/el-negocio-inmobiliario-ante-las-novedades-en-la-prevencion-del-blanqueo-de-capitales/.

**IDEA-29 ColivEs reshaped: mid-term lease compliance file [user idea U1]** (8 searches; all eight angles)
1. (a) [F]+[S] Read RDL 29/2026 [F], then search for the result of the Diputación Permanente vote around 12 Nov 2026 [S]. Also:
   - what happens to contracts signed between 8 Oct and the vote;
   - what the 29 Nov results and party programmes imply for repeal or replacement.

   This is the main lapse check, and its answer is shared with IDEA-30, IDEA-31, IDEA-32 and IDEA-01.
2. (a) [S]×2 The durable anchors, which hold even if the decree lapses:
   - **Search 1:** the stage of the Constitutional Court appeal against Llei 11/2025, and whether the Generalitat treats coliving as inside the cap (disputed, C-14). Catalonia's first sanctions [F].
   - **Search 2:** court rulings since Oct 2026 that re-classify temporary leases under art. 6.4 Código Civil, and which indicators they used (idealista, Jul 2026 [F]).
3. (b)(g) [S]×2 Competitors and copy risk:
   - **Search 1:** do Homming, Rentger, Spotahome, Ukio or Blueground offer cause-evidence vaults, chaining counters or regime versioning, and at what price?
   - **Search 2:** do any legal-tech or law-firm products (Captain Legal, Lázaro Amable, Garrigues) or AI contract generators sell a "causa" contract file? This is the AI-copy test.
4. (c) [S] Temporary-lease deposits lodged each year at INCASÒL and the other regional bodies, by contract type. Also cross-check Consumo's figure of more than 1M people in seasonal or room rentals and the seasonal-listing shares [F], and the nomad-visa counts, where 27,875 is single-source.
5. (f) [S] Can INCASÒL Model 2 filing be automated (an API, or authorisation to file for third parties)? Does SES.Hospedajes apply to 32–90-day leases? Is the fianza one month or two outside Catalonia (C-14)? Also note the professional-liability cover a contract builder needs.
6. (d) [S] Desk anchor: what law firms and agencies charge per temporary-lease contract or legal review in Barcelona, Madrid and Málaga.
7. (d)(e) [I] Interview 10 mid-term managers or coliving operators: Be Casa, Cotown, Smart Rental, Node Living, Vandor, plus AICAT members. Cover their process today, legal spend per contract, willingness to pay €8–12 per contract, and whether partner law firms will co-brand the templates.
8. (h) Kill if any of these holds:
   - convalidation fails and Catalan operators will not pay at least €8 per contract;
   - a law firm or legal-tech tool already sells the same file;
   - interviews show courts and landlords do not value documentary cause evidence.

**IDEA-30 Rent-cap autopilot** (3 searches)
1. (b)(g)(h) [S] Do Homming, Rentger, Vivara, Arrenta or Inmostats sell per-lease cap and update calculators with alerts, and at what price? Do idealista or Fotocasa give free calculators? A free portal calculator is a kill criterion.
2. (a) [F] The IRAV value in force in Oct–Nov 2026 and where INE publishes it; which update rules survive if RDL 29/2026 lapses (from IDEA-29's first check); OCU on the tensioned zones.
3. (f)(h) [S] Is there a machine-readable official list of tensioned municipalities and SERPAVI values? Have the 53 new Catalan municipalities been published in the BOE? How many Basque municipalities are tensioned (17–19, C-14)? Unreliable data is a kill criterion.
4. (c) [S] How many individual landlords there are (for example, AEAT rental-income declarants), and how many are in tensioned zones.
5. (f) Note whether an automated cap calculation can be sold without counting as legal advice.
6. (d)(h) [I] Kill if fewer than about 1 in 10 surveyed landlords would pay €5/month.

**IDEA-31 Landlord-paid tenant screening** (3 searches)
1. (b)(d)(g) [S] What GarantíaYa, Spotahome (Spanish rates) and HousingAnywhere (landlord commission) charge, and whether Spanish tenant-scoring startups exist. The KYC layer has no moat, so check whether any of them already has foreign-income data partnerships or a guarantee underwriter.
2. (a) [S] Does the rewritten art. 20.2 LAU also ban tenant-side screening or platform fees? Has Consumo acted against one, beyond the Alquiler Seguro proposal [F]?
3. (f) [S] AEPD guidance on tenant screening, and the legal basis and retention period for verifying income under the GDPR.
4. (e)(h) [I] Will agencies in Barcelona, Madrid and Málaga pay per screening (10 interviews)? Which insurers would back a landlord-paid guarantee for foreign tenants (OCU comparison [F])? Kill if agencies will not pay at least €9, or if no insurer will back the guarantee.
5. (f) [F] The cost of a nota simple from Registradores, and whether it can be automated.

**IDEA-32 Short-term-rental listing compliance monitor** (4 searches)
1. (f)(h) [S] Which regional registers (Andalucía RTA, Catalonia HUT, the C. Valenciana RTV, Madrid, Baleares ETV, Canarias VV) publish open data, an API or a public search, and on what terms? If they cannot be queried at scale, that is a kill criterion.
2. (b)(g) [S] Do Chekin, net2rent, Avantio, Hostaway, Smoobu, AirDNA or Inside Airbnb already offer code validation or compliance monitoring, and at what price?
3. (a) [S] Have Málaga's 43-barrio ban and 3-year suspension been published in the BOP? Has Palma's ban been approved? What are Canarias' Ley 6/2025 transition rules, and the number and date of Baleares' Ley 4/2026 (single-source in the notes)?
4. (f) [S] Do Airbnb's or Booking's partner APIs expose registration fields, and do their terms forbid scraping?
5. (a) [F] The outcome of Consumo's proceedings against large managers (DSCA page); whether RDL 29/2026's platform sanctions survive (from IDEA-29's first check); Spain's penalty regime for EU 2024/1028.
6. (c)(d)(h) [I] Ask Fevitur, Apartur and Aptur CV how many professional managers operate. Kill if managers will not pay at least €2 per listing.

**IDEA-33 Tourist-tax and traveller-reporting engine** (3 searches)
1. (a) [F]+[S] Read Gipuzkoa's Norma Foral 3/2026 in the BOPV [F]. Then search for the Bizkaia and Álava norm numbers, rates and filing periods, and whether San Sebastián, Bilbao and Vitoria have adopted the surcharge [S].
2. (b)(g)(h) [F]+[S] Chekin's pricing page settles its minimum units (C-16) and shows whether it covers the Basque tax [F]. Then search whether Smoobu, Avantio, Hostaway, net2rent, Mews or Cloudbeds support the Basque rates and the quarterly return [S]. If they already do, that is a kill criterion.
3. (f) [S] Do the Ertzaintza and Mossos traveller-reporting systems offer web services, and in what formats? Can software file the self-assessment on the establishment's behalf (apoderamiento)?
4. (a) [F] Barcelona's amounts in the DOGC tables (Forbes against DonPorqué, C-16); RD 933/2021 for the SES duties. The stage of EU infringement INFR(2026)4005 [S\*].
5. (c) [S\*] Lodging establishments and listed tourist homes in Euskadi (INE, Eustat).
6. (h) Kill if the Basque treasuries or associations give out free calculators.

**IDEA-34 Administradores de fincas compliance calendar** (2 searches)
1. (b)(d)(g)(h) [S] The calendar itself is copyable, so the moat test is ERP integration and consolidator contracts. What Gesfincas, Fincas Pro, Comunidad Feliz and Fynkus offer (compliance calendar, supplier CAE, votes), and at what price. If Gesfincas or Fincas Pro already ship a calendar, that is a kill criterion.
2. (a) [S] The recurring legal inspections, certifications and deadlines for residential buildings, by region, including lifts under RD 355/2024.
3. (f) [F] LPH arts. 16–17: do electronic notices and minutes count as "cualquier medio que permita tener constancia de su recepción"?
4. (e)(h) [I] Does inmho build or buy its tooling, and would it run a pilot? What does CGCAFE know about software adoption? Kill if administradores will not pay €1 per community.

**IDEA-35 AML kit for agencies** (1 search)
1. (a)(h) [S] SEPBLAC inspections and sanctions of real-estate agencies in 2023–26 (SEPBLAC and finreg360 [F]). Kill if enforcement against small agencies is negligible and agencies will not pay before July 2027.
2. (a) [S\*] The exact AMLR application date, any eased duties for small entities such as the compliance-officer requirement, and whether rental intermediation above a threshold is covered.
3. (b)(d)(g) [S\*] AML kits for agencies (associations, consultants, Inmovilla or Witei modules), with prices. The content is easy to copy, so check whether CRMs already bundle it.
4. (c) [F] The number of agencies (DIRCE CNAE 6831) and the share that broker sales.

### Batch 6. Transport, ZBE, packaging and the food chain, with user idea U3 (7 ideas, 24 searches)

**Ideas:** IDEA-48 [U3], IDEA-47, IDEA-45, IDEA-46, IDEA-49, IDEA-50, IDEA-51.

**Why together:**
- IDEA-47 and IDEA-48 share one ZBE data layer, and batch 6 owns the ZBE city-status checks (C-01, C-13).
- IDEA-45 and IDEA-46 share the haulage associations and trip records.
- IDEA-49 to IDEA-51 share the food-industry buyers (FIAB, cooperatives) and the EU product rules.

**Search allocation:** IDEA-48 8 (full treatment); IDEA-47 3; IDEA-45 3; IDEA-46 3; IDEA-49 3; IDEA-50 2; IDEA-51 2. Total 24.

**Known pages to fetch:**
- ZBE status and data:
  - ecomovilidad on Valencia, https://ecomovilidad.es/zonas-de-bajas-emisiones/valencia/valencia/;
  - El Español on Valencia, https://www.elespanol.com/valencia/20260307/vox-rechaza-valencia-zona-bajas-emisiones-aprobo-castellon-pone-riesgo-millones/1003744158258_0.html;
  - Valencia open data, https://opendata.vlci.valencia.es/dataset/zona-de-bajas-emisiones;
  - Open Data BCN, https://opendata-ajuntament.barcelona.cat/data/en/dataset/zbe-ambit;
  - the DGT NAP feed, https://nap.dgt.es/datex2/v3/dgt/zbe/ControledZonePublication/;
  - the datos.gob.es data request, https://datos.gob.es/es/solicitud-de-datos/zonas-de-bajas-emisiones;
  - the DGT ZBE document, https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/MOV-gestion-trafico/ED1_2023-ZBE-en-DGT30.pdf.
- Valencia Sandbox: the ordinance, https://sede.valencia.es/sede/descarga/doc/DOCUMENT_1_20240006949868; procedure AE.IN.100, https://sede.valencia.es/sede/registro/procedimiento/AE.IN.100?lang=1; Paréntesis on the port alliance, https://www.parentesis.media/valencia-madrid-y-barcelona-convierten-la-ia-en-un-laboratorio-urbano-bajo-control-juridico/.
- City rulings and fines:
  - the Supreme Court on Madrid, https://www.infobae.com/espana/2026/04/21/el-tribunal-supremo-confirma-la-anulacion-parcial-de-la-zona-de-bajas-emisiones-en-madrid-al-rechazar-el-recurso-del-ayuntamiento/;
  - the TSJM enforcement piece, https://www.eldiariodemadrid.es/articulo/tribunales/tsjm-pieza-separada-ejecucion-sentencia-zonas-bajas-emisiones-madrid/20260715165846137443.html;
  - Málaga, https://www.motorpasion.com/industria/oficial-zbe-malaga-no-multara-a-coches-etiqueta-b-justicia-tumba-ayuntamiento-devolvera-dinero;
  - the Barcelona area, https://www.metropoliabierta.cat/gran-barcelona/20260910/nomes-sis-municipis-larea-barcelona-apliquen-multes-forma-eficac-zona-baixes-emissions/1003742793528_0.html;
  - Motor16, https://www.motor16.com/las-ultimas-noticias/zbe-ciudades-multas-coches/ and https://www.motor16.com/las-ultimas-noticias/zonas-bajas-emisiones-68-ciudades/;
  - Madrid fines, https://www.hibridosyelectricos.com/coches/191347190-en-multas-madrid-logra-record-historico-en-espana-por-acceso-sin-etiqueta-zbe_83375_102.html;
  - UNO on mobility ordinances, https://unologistica.org/proyectos-e-informes/ordenanzas-de-movilidad/;
  - the BOIB notice on Palma's ZBE (only C, ECO and Cero from 1 Jan 2027), https://www.caib.es/eboibfront/pdf/ca/2026/37/1215590;
  - the madrid.es ZBEDEP Distrito Centro page for businesses (full URL in G5's sources).
- Haulage:
  - Ley 9/2025, https://www.boe.es/buscar/act.php?id=BOE-A-2025-24545;
  - RDL 9/2026, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8283;
  - Ley 15/2009, https://www.boe.es/eli/es/l/2009/11/11/15/con;
  - GA-P's DeCA guide, https://ga-p.com/publicaciones/guia-para-no-perderte-con-el-nuevo-deca/;
  - Fenadismer's pages: https://www.fenadismer.es/ojo-ofertas-abusivas-para-el-nuevo-documento-electronico-de-control/, https://www.fenadismer.es/deca-transportes-reconoce-fallos-tecnicos-y-no-tramitara-las-multas-impuestas/, https://www.fenadismer.es/deca-sanciones-injustas-a-transportistas-por-errores-de-sus-cargadores-o-de-las-inspecciones-en-carretera/ and https://www.fenadismer.es/canal-de-denuncias-contra-los-cargadores-que-no-indexen-el-combustible-a-sus-transportistas/;
  - trans.info on payment days, https://trans.info/es/los-transportistas-espanoles-esperan-52-dias-para-cobrar-la-reforma-europea-se-atasca-504049.
- Packaging and EU rules:
  - RD 1055/2022, https://www.boe.es/eli/es/rd/2022/12/27/1055/con;
  - Ley 1/2025, https://www.boe.es/eli/es/l/2025/04/01/1/con;
  - the AEAT plastic-tax page, https://sede.agenciatributaria.gob.es/Sede/impuestos-especiales-medioambientales/impuesto-especial-sobre-envases-plastico-reutilizables.html;
  - the EU packaging page, https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en;
  - EUDR, https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en.
- Food chain and farms:
  - Ley 12/2013, https://www.boe.es/eli/es/l/2013/08/02/12/con;
  - the AICA RCA FAQ, https://www.aica.gob.es/servicios-en-linea/Registro%20de%20Contratos%20Alimentarios/preguntas-frecuentes-rca;
  - AICA's 2025 report, https://www.aica.gob.es/content/dam/aica/docs/publicaciones/memorias/Memoria_Anual_de_Actividades_2025.pdf;
  - RD 1051/2022, https://www.boe.es/eli/es/rd/2022/12/27/1051/con;
  - RD 1054/2022, https://www.boe.es/eli/es/rd/2022/12/27/1054/con.

**IDEA-48 EcoRoute reshaped: ZBE rules and in-zone compliance-check API [user idea U3]** (8 searches; all eight angles)
1. (a) [F]+[S] Valencia's ZBE status (C-01): ecomovilidad, El Español, the Valencia open-data layer and the NAP record [F]. Then search for any Pleno vote after Sep 2026 [S]. This settles the conflict for all batches and for the regional-claims verdict.
2. (a) [S] The status, in Oct–Nov 2026, of the other contested schemes (C-13):
   - whether the Málaga ruling became final around 25 Nov 2026;
   - Zaragoza's enforcement;
   - Vigo's label-B date;
   - Catalonia's label-B rule before 2028;
   - Madrid after the Supreme Court's partial annulment [F].
3. (b)(g)(h) [S] Which Spanish LEZs HERE and TomTom cover, at what price, and whether they encode DGT labels, domicile and quotas. Confirmed Spanish semantics would be a kill criterion.
4. (b)(g) [S]×2 Other competitors and copy risk:
   - **Search 1:** which fleet and route software supports Spanish ZBEs, and how: Google Routes API, PTV, Sygic Truck, Webfleet, and 5–10 Spanish TMS and telematics vendors.
   - **Search 2:** who is behind @cargoffer/zbe-mcp and the Apify "EU LEZ Route & Vehicle Checker", and what are their pricing and traction?
5. (a)(f) [F]+[S] Read the DGT ZBE document and the datos.gob.es request [F]. Then search whether the DGT plans to extend the DGT 3.0 or NAP data model, and on what terms DGT labels can be looked up programmatically [S]. Batch 6 owns the label lookup. Also record what liability a compliance answer carries, and whether professional-liability insurance is needed [S\*].
6. (e) [F]+[S] Read the Sandbox ordinance, the AE.IN.100 procedure and Paréntesis [F]. Then search for the final approval and BOP dates, the projects admitted, whether a data-API pilot is eligible, and the port alliance's terms [S].
7. (c)(d) [S] How many ZBE fines a year renting and leasing firms reassign, and what that costs them, plus per-vehicle price benchmarks for Spanish fleet software.
8. (d)(h) [I] Contact 20 fleet-software vendors about €149/month. Kill if fewer than 5 would pay.

**IDEA-47 ZBE vehicle checker and fleet permit ledger** (3 searches)
1. (b)(g)(h) [S] What the ZBE España app, the Astac/RACC site and RACE's tools offer and charge, and whether any sends vehicle-specific alerts. If one does, that is a kill criterion.
2. (c) [S] What share of Madrid's ZBE fines goes to commercial vehicles or companies (Madrid, AEA; the Madrid fine-record page [F]), and how many vans of each label are registered in each target city (DGT fleet panel).
3. (f) [F]+[S] Do Bilbao, AMB and Zaragoza offer APIs or bulk upload for invitations and passes? Read the city portals, the madrid.es ZBEDEP page and UNO's ordinances page [F]. Then search for a machine-readable source of pollution-episode declarations in Madrid and Barcelona [S].
4. (f) [S\*] May a SaaS file registrations or declarations on a client's behalf?
5. (d)(h) [I] Two interview sets:
   - 50 trades autónomos with label-B or unlabelled vans in Madrid, Barcelona and Palma, on willingness to pay. Kill if a 4-week pilot converts under 3% of free checkers.
   - 20 SME distributors serving Madrid Distrito Centro, Bilbao and Barcelona, on fines and permit hours. Kill if fewer than 5 report fines or at least 2 hours a week of permit work.
6. (g) Reuse IDEA-48's third and fourth checks: do route planners already add Spanish semantics?

**IDEA-45 DeCA evidence vault** (3 searches)
1. (b)(d)(g) [F]+[S] Read Fenadismer's 10 Sep 2026 warning about offers [F]. Then search which DeCA tools sell at about €5/month, whether any capture and timestamp shipper-issued documents, and what Fieldeas, Viafirma and Edicom charge [S].
2. (b)(h) [S] Do Fenadismer, CETM or UNO provide or endorse a free or member-priced DeCA tool? Has the Ministry or the DGTCF published a free generator or repository? Either would be a kill criterion.
3. (a)(c) [S] How many DeCA fines have been issued since 5 Oct 2026, by type, and how appeals are going. Fenadismer's incident pages [F].
4. (f) [F] Ley 9/2025, the Resolución DGTCF of 5 Jun 2026 and GA-P's guide. [I] Ask a transport lawyer whether a carrier's timestamped copy counts as evidence, and whether a qualified timestamp is required.
5. (c)(h) [I] What share of carriers receive DeCAs from shippers rather than issuing them? Kill if fewer than 1 in 5 interviewed carriers has had a DeCA incident or fine.

**IDEA-46 Haulier revenue recovery** (3 searches)
1. (b)(h) [S] What CETM's "Calculadora de Costes e Indexación" does, what it costs and whether it is member-only. If it already produces invoice lines and evidence, that is a kill criterion.
2. (a) [F]+[S] Read RDL 9/2026 and Ley 15/2009 art. 38 [F]. Then search whether RDL 9/2026 and RDL 25/2026 were convalidated, and how RDL 25/2026 was handled with the Cortes dissolved [S].
3. (f) [F] Does the Ministry publish the weekly G index in machine-readable form? Also the Holded, Quipu and a3factura developer pages on adding invoice lines.
4. (b)(g) [S] Do the top 3–5 TMS used by Spanish SME hauliers already automate the fuel line?
5. (a)(c) [F] Fenadismer's complaint-channel page and trans.info on payment days: complaints received, and any shippers sanctioned.
6. (f)(d)(h) [I] Get a legal review of shipper scorecards (data protection, competition law). Ask 15–20 hauliers whether they would add the line if it were automatic; kill if 60% or more would not.

**IDEA-49 Packaging EPR and PPWR kit** (3 searches)
1. (b)(h) [S] What collective schemes charge and give their members: Ecoembes, GENCI, Cartón Circular, and the schemes for commercial and industrial packaging. Free declaration software from the schemes is a kill criterion.
2. (c) [S] How many producers are registered in the packaging section of the Registro de Productores de Producto (MITECO), and how many businesses file modelo 592.
3. (a) [F] RD 1055/2022, the AEAT plastic-tax page (updated 20 Oct 2026), and the EU packaging and EUDR pages: which PPWR duties bind SMEs now and which only in 2030, the Omnibus status, and the EUDR date for micro and small firms. Also the Ley 1/2025 dates (C-12).
4. (b)(g)(d) [S] Packaging-compliance SaaS in Spain and the EU (Lizenzero-type services, consultancy portals), with prices.
5. (f) [F] Can registration numbers be checked through a public registry or API (MITECO)? Also the sanctions under Ley 7/2022, with enforcement cases [S\*].
6. (d)(e)(h) [I] Interview 10 online sellers and importers and 10 food SMEs on awareness, who handles the duty today, and the cost. Kill if a typical SME prepares the declaration in under a day.

**IDEA-50 RCA autopilot** (2 searches)
1. (f) [F] The AICA RCA FAQ and the 2025 report: RCA API access and documentation, any listed integrators, and the number of buyers and contracts. [I] Ask AICA how many of the 616 grape infractions were failures to register.
2. (b)(g)(h) [S] Which Spanish winery and agri-food ERPs integrate the RCA API, and at what price. Integration at no extra cost is a kill criterion.
3. (a) [S] The status of the draft AICA inspection decree after the election call.
4. (f)(d) [I] Can a SaaS act through API credentials or a delegated certificate? What do gestorías charge for RCA uploads? Kill if buyers spend under an hour per season on the RCA.

**IDEA-51 Fertilisation-plan workspace** (2 searches)
1. (b)(g)(h) [S] Do the free public CUE software and the Cuaderno de Campo Cooperativo already generate plans de abonado? If so, that is a kill criterion.
2. (b)(d) [S] What private farm apps (Agroptima and others) offer and charge.
3. (f) [F] RD 1051/2022 and RD 1054/2022. SIEX's exchange format and API [S\*].
4. (c)(a) [S\*] REGFER registrations since 1 Jul 2026, the number of farms above the plan thresholds, and any inspections so far.
5. (e) [I] Will Cooperativas Agro-alimentarias, UPA or ASAJA distribute it?

### Batch 7. Immigration and relocation, with user idea U2 (7 ideas, 24 searches)

**Ideas:** IDEA-52 [U2], IDEA-53, IDEA-54, IDEA-55, IDEA-56, IDEA-57, IDEA-58.

**Why together:**
- They share the same sources: RD 316/2026 and RD 1155/2024, the UGE, the police appointment pilot, Beckham rules and the C-25 conflicts. Batch 7 owns all of these.
- They share the same buyers: habilitated filers, employers, HR teams and relocation agencies.
- IDEA-52 and IDEA-53 share a document-validation engine, IDEA-54 feeds both, and IDEA-55 feeds IDEA-56.

**Search allocation:** IDEA-52 8 (full treatment); IDEA-53 3; IDEA-54 2; IDEA-55 3; IDEA-56 3; IDEA-57 3; IDEA-58 2. Total 24.

**Known pages to fetch:**
- Government figures and rules:
  - La Moncloa on the regularisation, https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/020726-balance-regularizacion-extraordinaria.aspx;
  - La Moncloa on the foreign resident population, https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/200326-poblacion-extranjera-con-residencia.aspx;
  - the ICAB note on the police pilot, https://www.icab.es/export/sites/icab/.galleries/documents-noticies/2026-INICIO-PROYECTO-PILOTO-ASIGNACION-AUTOMATICA-DE-CITA-PARA-TOMA-DE-HUELLA.pdf;
  - the June 2026 thresholds, https://infoextranjeria.org/2026/06/11/actualizacion-del-umbral-salarial-para-profesionales-altamente-cualificados/;
  - the FNMT on NIE problems, https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-5-problematica-del-uso-del-nie;
  - the Defensor del Pueblo's 2025 report, https://www.defensordelpueblo.es/wp-content/uploads/2026/03/Defensor-del-Pueblo_Informe-anual-2025.pdf.
- Office timings and appointments: España Abogados, https://espanaabogados.com/fechas-de-resolucion-de-tramites-de-extranjeria-en-espana/; citaex, https://citaex.com/disponibilidad-citas.
- Competitors and prices: GestoLab, https://www.gestolab.com/blog/formulario-ex-03-que-es-cuando-se-usa-y-como-rellenarlo-paso-a-paso; Klevvera's DNV costs, https://www.klevvera.com/blog/spain-digital-nomad-visa-cost-breakdown/.
- Context: Mercurio outages, https://www.lawandtrends.com/noticias/administrativo/largas-colas-en-los-consulados-y-las-caidas-de-la-plataforma-mercurio-protagonistas-de-la-primera-jornada-de-1.html; DNV holders in Barcelona, https://www.elnacional.cat/oneconomia/es/economia/barcelona-ya-supera-15000-nomadas-digitales-extracomunitarios-con-permiso-residencia_1549862_102.html.

**IDEA-52 PermisoFast reshaped: UGE talent-case co-pilot [user idea U2]** (8 searches; all eight angles)
1. (a)(c) [S] Annual UGE grants by type in 2025, which Stage 1 did not find, against the stock of 174,357 (Sep 2025) [F, La Moncloa]. Batch 7 owns this check for IDEA-56.
2. (a) [S]×2 Two checks on UGE practice:
   - **Search 1:** confirm Criterio de Gestión 2/2025, and whether the UGE now rejects outright more often (today a single commercial source).
   - **Search 2:** the published reasons for document requests and denials in DNV and highly qualified cases (law-firm blogs, colegio notes).
3. (a) [F]+[S] The June 2026 thresholds [F]. Then search for the 2026 minimum wage and the DNV income line of €2,849 a month (RD 126/2026) [S]. Settle the UGE fee (€73.26 against €70.40/€75.60) and whether the thresholds cover the national highly qualified permit (C-25).
4. (b)(g) [S]×2 Competitors and copy risk:
   - **Search 1:** do GestoLab [F] and Cicerai cover UGE procedures, and does any UGE-specific tool exist?
   - **Search 2:** myspanishdnv.com, Nomadlex, Deel's US$250 documentation fee, and the immigration pricing of Jobbatical and Localyze (shared with IDEA-56).

   The copy-risk question: could GestoLab extend into UGE cases?
5. (d) [F] Law-firm package prices as anchors for €30 per case: Klevvera [F], and the Lexidy, Platinum Legal and Latitude Law pages.
6. (c)(e) [S] How many immigration law firms and gestorías handle UGE cases (ICAM and ICAB extranjería sections), how many relocation agencies need a partner filer (about 110), and EOR partner networks.
7. (f) [S] The legal limits on a non-law-firm platform offering pre-checks directly to applicants. Also GDPR art. 10 and the AI Act classification for automated document review. There is no UGE platform API.
8. (d)(h) [I] How many hours a DNV case spends on reconciling evidence, and what firms would pay per case. Kill if fewer than five firms run a paid pilot, or if reconciliation does not measurably cut document requests.

**IDEA-53 Renewal-wave case manager** (3 searches)
1. (a)(h) [S] RD 316/2026, DA 20 and 21: permit validity, renewal route, renewal window and documents, and whether any renewal is automatic. An automatic renewal is a kill or pivot trigger. La Moncloa's balance page [F]. Batch 7 owns this check for IDEA-57.
2. (b)(g)(h) [S] GestoLab's real pricing beyond "from 1€", its support for renewals and batch work, and its client count; whether Cicerai is active in Spain. Bulk renewals at about €1 per case trigger the pivot to the NGO tier.
3. (a) [F] The ICAB pilot PDF: does auto-assignment cover renewal TIEs, and who receives the notices?
4. (f) [S] AEPD guidance for processors that handle criminal-record certificates and passports for law firms.
5. (c) [S\*] How many gestorías and graduados sociales filed regularisation files (DGGM, Consejo General de Gestores)?
6. (d)(h) [I] Interview 20–30 filers on their renewal book, hours per file, correction-request share and willingness to pay per case. Kill if fewer than 10 of 30 report a 2027 renewal book above 100 clients, or more than one hour of work per renewal file.

**IDEA-54 Extranjería rule and form radar** (2 searches)
1. (b)(d) [S] The readership and any paid tiers of Infoextranjeria, Machelin Díaz, Parainmigrantes and Extranjería Legal; extranjería alerts in vLex, Aranzadi and Lefebvre, with prices.
2. (f)(g) [S] Is there a machine-readable feed for DGGM criteria and SEM instructions, or must the ministry site be scraped (it returned 403 in Stage 1)?
3. (a) [F] Use the Supreme Court annulments (published 22 Sep 2026) and the ICAB pilot note as test cases of how late changes reach professionals.
4. (e)(h) [I] What ICAM and ICAB send members, and how fast. Price test at €9 per seat per month with 30 professionals; kill if fewer than 5% of free-digest subscribers convert within three months.

**IDEA-55 Expected-decision-time tracker** (3 searches)
1. (f) [F]+[S] The España Abogados table [F]. Then search for the format, frequency and history of the Madrid, Valencia and Baleares resolution-date PDFs, and whether past months can be recovered [S].
2. (b)(g) [S] Does the official file-status service (consulta de expedientes) show queue position or expected dates? Does Extranjería App show office timings, and what are its price and real user numbers?
3. (a)(f) [S] Settle the conflicting legal deadlines under RD 1155/2024 (art. 68.6 and others) for the alert logic, including the reunification deadline (C-25).
4. (a) [S\*] Have the Barcelona, Málaga or Alicante Delegaciones said they will publish resolution dates?
5. (c)(d)(h) [I] Interview 15 HR and mobility teams: would an expected decision window change offers, start dates or relocation spending? Kill if there are fewer than 200 Barcelona data points in three months, or if HR does not plan around office timing.

**IDEA-56 Relocation orchestrator** (3 searches)
1. (b)(d)(g) [S] Spain pricing at Jobbatical, Localyze and Deel immigration (shared with IDEA-52's fourth check), and how deep their Spain-specific steps go, since global platforms could add the same depth. Agency packs on vendor pages [F]: Locallista at €400, Relocation Angel at €1,200–3,500.
2. (a) [S] The DGT's current list of licence-exchange agreement countries, and the six-month rule in the Reglamento General de Conductores.
3. (a) [F]+[S] The ICAB pilot PDF: does auto-assignment go beyond 10%, and which cases are excluded [F]? Then search how the EX-13 travel authorisation is handled now that Instrucción 1/2026 has expired [S].
4. (a) [F] The Beckham six-month rule (art. 119.4 RIRPF, BOE), shared with IDEA-58.
5. (c)(e)(h) [I] Interview 10 relocation agencies on tooling spend and margins. Kill if fewer than 10 HR teams in Barcelona and Madrid make at least five non-EU moves a year, or if agencies will not pay for tooling.

**IDEA-57 Work-permit expiry monitor** (3 searches)
1. (a) [S] What protects an employer while a renewal is pending: is the resguardo enough for the worker to keep working, and how do inspectors treat it (LOEX and RD 1155/2024 texts [F])? Reuse IDEA-53's first check for the DA 20/21 renewal windows.
2. (c) [S] Employers with non-EU employees, by sector and size (Social Security affiliation by nationality), and regularised affiliates by sector (La Moncloa [F]). Confirm the 14.1% share. This also contributes to C-04, which batch 3 owns.
3. (b)(g) [S] Document-expiry alerts in A3, Sage, Factorial, Sesame, Woffu and Holded HR, and immigration case software for law firms ("software extranjería despachos").
4. (f) [F] Can employers check a worker's authorisation through an official online service? The GDPR basis and retention period for TIE copies [S\*].
5. (d)(e)(h) [I] Gestorías' renewal fees (€90 at gestoriadeextranjeria.es) and whether they would resell at €1 per worker per month. Kill tests:
   - fewer than a third of employers with 5+ non-EU staff report a lapse, a near miss or worry about inspections;
   - fewer than 20% track expiries at all;
   - fewer than three gestorías want to resell.

**IDEA-58 Beckham filing kit** (2 searches)
1. (c)(h) [S] AEAT statistics on modelo 149 filings and rejections, 2023–2025. Kill if there are fewer than about 3,000 new filings a year.
2. (b)(d)(g)(h) [S] Does TaxDown file modelos 149 and 151, and at what price; does any other app? Guided filing at €99 or less is a kill criterion.
3. (a)(f) [F] The wording of art. 119.4 RIRPF [BOE]. Can an apoderado or colaborador social file modelo 149, and can newcomers without a TIE get the credentials they need? Use the FNMT NIE FAQ and the Cl@ve conflict (C-25).
4. (a) [S\*] Are digital nomads employed by foreign companies eligible, compared with autónomos?
5. (e)(d) [I] Would partner advisers review a case for €99, and would HR teams pay €99 per employee?

### Batch 8. Startups, web risk, games and creators, with user ideas U4 and U5 (7 ideas, 24 searches)

**Ideas:** IDEA-63 [U4], IDEA-64 [U5], IDEA-62, IDEA-15, IDEA-59, IDEA-60, IDEA-61.

**Why together:**
- The two user gaming ideas and the creator-matching tool share the Twitch and Kick API checks and the Spanish-language stream data. Batch 8 owns both.
- The startup ideas share the ENISA, CDTI and AEAT sources, and AES and accelerators as channels. IDEA-15 shares the startup and e-commerce audience.

**Search allocation:** IDEA-63 7 (full treatment); IDEA-64 5 (full treatment, including the check on the original form); IDEA-62 3; IDEA-15 3; IDEA-59 2; IDEA-60 2; IDEA-61 2. Total 24.

**Known pages to fetch:**
- Gaming and streaming:
  - Twitch Extensions guidelines, https://dev.twitch.tv/docs/extensions/guidelines-and-policies/;
  - Ley 13/2011, https://www.boe.es/buscar/act.php?id=BOE-A-2011-9280;
  - Steam earnings data, https://mp1st.com/news/40-of-steam-games-in-2025-earned-less-than-100;
  - streaming in Spain, https://www.que.es/2026/01/09/fenomeno-streaming-espana-videojuegos/;
  - Kolsquare's Twitch guide, https://www.kolsquare.com/es/informes-y-guias/guia-marketing-influencers-twitch;
  - Steam store pages of the comparable games.
- ISP blocking: https://www.que.es/2026/04/17/bloqueos-futbol-operadoras/.
- Startups:
  - Economía 3 on ENISA certification, https://economia3.com/2026/10/15/762915-certificado-de-empresa-emergente-2-529-startups-lo-tienen-pero-no-garantiza-el-visado/;
  - Tetuan Valley on public funding, https://tetuanvalley.com/blog-financiacion-publica-para-startups/;
  - Premoney on fractional CFOs, https://www.premoney.es/blog/cfo-externo;
  - ACCIÓ's 2026 startup analysis, https://www.accio.gencat.cat/web/.content/bancconeixement/documents/pindoles/ACCIO-analisi-ecosistema-startup-catalunya-2026-pindola-en.pdf.

**IDEA-63 Fandango Arena reshaped: cheap streamer-vs-chat co-op physics game [user idea U4]** (7 searches; all eight angles)
1. (c) [S] What share of streams of R.E.P.O., PEAK and Chained Together is in Spanish, and Spanish creators' track record with indie co-op games. Streams Charts returned 403 in Stage 1, so use other sources. Batch 8 owns this check for IDEA-62.
2. (c)(h) [S]×2 Two market checks:
   - **Search 1:** any Spain-level unit data for co-op games on Steam.
   - **Search 2:** how the 2026 genre entrants performed (Meccha Chameleon, Yapyap, BOMBANANA!), which sets the wishlist target for the kill test.
3. (b)(d) [F] Spanish Steam store pages for R.E.P.O., PEAK, Lethal Company, Content Warning, RV There Yet?, Chained Together, Human Fall Flat, Gang Beasts, Party Animals and Ultimate Chicken Horse. This confirms the €8.99 anchor (GAM-13). Also Crowd Control's pricing page.
4. (f) [F]+[S] Twitch Extensions rule 6.2 on Bits used for votes that change gameplay [F]. Then search for Kick's developer terms and rate limits [S]. Batch 8 owns these checks.
5. (a)(f) [S] The status of the minors' digital protection bill after the dissolution, how PEGI treats voice chat, and the EU draft on age verification in online games.
6. (f)(d) [S] The budget for a 6–9-month build with 4–6 developers in Spain, and eligibility for the 2026/2027 national grant (up to €80k, single source) and the Comunidad de Madrid call.
7. (e) [S\*] Steam bundle and gifting options that make it easier for friends to buy together (Steamworks documentation [F]). Channels: Next Fest, Mad Games Show, GAMERGY, DEV.
8. (g)(h) Moat: none, because the product is hit-driven. Record the creator-relationship test as the only edge. [I] Kill if the Steam page and demo miss the wishlist target set from the second check before Next Fest, or if fewer than three Spanish creators averaging 1,000+ viewers stream the demo.

**IDEA-64 LigaHub reshaped: points-only companion for simulcast creator events [user idea U5]** (5 searches; all eight angles)
1. (a)(f)(h) [F]+[S] Read Ley 13/2011 arts. 2.2.a, 2.2.c, 3.a, 9.2 and Title VII [F]. Then search DGOJ or gaming-lawyer commentary: are free points with sponsor prizes a "juego", a "concurso" or a promotional draw [S]? This also confirms whether the original real-money transfer market must be discarded.
2. (f) [F]+[S] Twitch Extensions rules 5.2 and 6.2.x [F]. Then search whether third-party apps can use Twitch Predictions, and what the YouTube and TikTok live APIs allow for prompts and results [S].
3. (c) [S] How many Spanish creator events a year are simulcast; cross-check La Velada VI's peak figures, which come from a single source.
4. (b)(d) [S] Engagement tools for creator events and their prices: start.gg's 6%, Toornament at $5 or $15, Battlefy at $10 and Crowd Control at $7.99 [F, vendor pages]. Would brands pay for unified engagement metrics at Spanish-language events?
5. (a) [S] The Kings League's 2026 status: the size of its dismissal plan and the pause of its Spanish league (C-28).
6. (e)(h) [I] Interview the producers of five Spanish creator events: TBS, the Kings League, Squid Craft Games, Tortillaland. Kill if fewer than three producers or brands commit to paid pilots, or if no prize-free design attracts sponsors.
7. (g) Moat: none. Native tools are free, and top events build their own.

**IDEA-62 Spanish-language creator matching for indie studios** (3 searches)
1. (b)(d)(g) [S] The pricing and Spanish-creator coverage of Keymailer, Lurkit, Woovit and other key-distribution tools. Kill if global tools already filter Spanish creators well.
2. (c) [S] How many Spanish and Latin American studios release on Steam each year. Reuse IDEA-63's first check for the share of indie streams in Spanish.
3. (f) [F] Twitch API terms for third-party analytics. Kick's terms come from IDEA-63's fourth check.
4. (f)(d) [S] Can grant money from the Ministerio de Cultura or the Comunidad de Madrid be spent on such a tool?
5. (d)(e)(h) [I] Ask 15 Spanish indie studios about their marketing budget per launch and how they reach creators. Kill if there are fewer than 30 paying studios after six months.

**IDEA-15 ISP block monitor** (3 searches)
1. (a)(h) [S] The status of the blocking orders in late 2026: appeals, extension to films and series, any settlement with CDNs (que.es [F]). Kill if block frequency drops sharply in the 2026–27 season.
2. (b)(g) [S] Free community trackers of LaLiga blocks and which ISPs they cover, and whether UptimeRobot, Pingdom or Checkly offer per-ISP vantage points in Spain.
3. (c)(d) [S] How many Spanish e-commerce sites sit behind shared CDNs (technology surveys), and whether any business has used block evidence to obtain compensation, through which legal route.
4. (f) [I] Get a legal view on the lawfulness of running probes and publishing block evidence, and assess the operations of keeping probes alive inside each ISP.
5. (h) [I] Kill if there are fewer than 100 paying domains after three months of matches.

**IDEA-59 Ley de Startups benefits keeper** (2 searches)
1. (c) [S] Why the 483 certifications were lost (ENISA data, or a transparency request), and whether ENISA's list of certified startups is public (Economía 3 [F]).
2. (a) [F] Ley 28/2022 in the BOE: the angel deduction cap (€100k against €250k, C-26), what ENISA's silence means, and how the 60% rule counts EOR staff.
3. (b)(d)(g) [S] Pricing and Spain-specific features of Ledgy, Carta and Spanish equity tools, and consultants' fees (Premoney, Managora).
4. (f) [F] What the angel certificate must contain for the AEAT, and how regional top-up deductions work (AEAT pages).
5. (d)(e)(h) [I] Run a price test through AES or accelerator cohorts. Kill if fewer than 30% of certified startups issue angel certificates or track the thresholds, or if ENISA adds monitoring.

**IDEA-60 Startup public-funding readiness** (2 searches)
1. (a) [S] ENISA's five 2026 lines and their exact requirements; its budget after FEPYME; the Neotec 2027 call dates and conditions; changes to CDTI's PID and LIC loans; how a caretaker government affects the 2027 calls (Tetuan Valley [F]).
2. (c)(b)(g) [S] ENISA's application and approval counts per year, and whether its client portal already offers pre-checks. Content and calculators are easy to copy, so check whether anyone publishes outcome data by funding line, the only defensible asset. Free pre-checks would be a kill criterion.
3. (d) [F] Fractional-CFO prices (Premoney [F]). [I] Ask five consultants about their fee models.
4. (h) [I] Kill if there are fewer than 50 paying startups after six months.

**IDEA-61 R&D-credit evidence tracker** (2 searches)
1. (a) [F] Verify in the BOE the R&D credit, the cash refund at a 20% discount and the researcher rebate, with their conditions (Ley 27/2014, RD 1432/2003, RD 475/2007). The notes give no article numbers.
2. (b)(d)(g) [S] The main R&D tax consultancies and their fee models, and whether accounting tools such as Holded already compute R&D credits.
3. (c) [S] AEAT statistics on how many small companies claim and cash in R&D credits, and how long the binding certificate takes and what it costs.
4. (c) [F] The ACCIÓ 2026 analysis, for R&D intensity.
5. (d)(h) [I] Interview 15 founders of loss-making deeptech startups. Kill if consultants already cover the evidence work for free and founders will not pay a subscription.

---

### 6.2 Budget check

| Batch | Ideas | User ideas | Searches |
|---|---|---|---|
| 1. Getting paid, invoicing and the SME software bill | IDEA-01, 02, 03, 04, 05, 11, 12, 13, 36 (9) | none | 24 |
| 2. Gestorías, the administration, owner duties and public money | IDEA-06, 07, 08, 09, 10, 25, 26, 27, 28 (9) | none | 24 |
| 3. Employers, care and regulated professions | IDEA-16, 17, 18, 19, 40, 41, 42, 43, 44 (9) | none | 24 |
| 4. Consumer-facing shops, hospitality and services | IDEA-14, 20, 21, 22, 23, 24, 37, 38, 39 (9) | none | 24 |
| 5. Housing, short-term rentals and property | IDEA-29, 30, 31, 32, 33, 34, 35 (7) | U1 (IDEA-29, 8 searches) | 24 |
| 6. Transport, ZBE, packaging and the food chain | IDEA-45, 46, 47, 48, 49, 50, 51 (7) | U3 (IDEA-48, 8 searches) | 24 |
| 7. Immigration and relocation | IDEA-52, 53, 54, 55, 56, 57, 58 (7) | U2 (IDEA-52, 8 searches) | 24 |
| 8. Startups, web risk, games and creators | IDEA-15, 59, 60, 61, 62, 63, 64 (7) | U4 (IDEA-63, 7 searches), U5 (IDEA-64, 5 searches) | 24 |
| **Total** | **64 ideas** | **5** | **192 of about 200** |

The remaining 8 or so searches in the shared pool are a reserve. Spend them first on the checks that can kill several ideas at once:
- the RDL 29/2026 vote (batch 5);
- whether the VeriFactu move to 2028 has a legal instrument (batch 1);
- the DA 20/21 renewal rules (batch 7);
- Valencia's ZBE status (batch 6).
