# Validation, batch 8 of 8: startups, web risk, games and creators (IDEA-15, 59, 60, 61, 62, 63 [U4], 64 [U5])

*Validator: batch 8. Work date: 23 October 2026 (Cortes dissolved 6 Oct 2026; general election 29 Nov 2026).*
*Inputs: `stage2_idea_longlist.md` (sections 2, 3, 5, 6.1 and batch 8), `00_user_supplied_ideas.md`, `stage2_G6_expat_startups_gaming.md`, `startups_tech_ecosystem.md`, `gaming_streaming_creators.md`; plus the web checks logged in section 4.*
*Citation format: [new: URL, date seen or published] for anything found in this validation; [notes: PAIN-ID] for stage-1 evidence. "Single source" is marked where it applies.*

*Status: complete (23 Oct 2026). 22 of the 24 allowed WebSearch calls were used.*

## 1. Batch summary table

**How the numbers work.** Sellability is the mean of S1–S8, and Overall is 0.6 × Sellability + 0.4 × P. Overall is computed from the unrounded Sellability and rounded half-up to two decimals. Types: A is a cheaper alternative, B is a new product, C is a low-touch subscription. IDEA-63 and IDEA-64 use the gaming adaptation of the rubric, which is stated in their sections.

| ID | Name | Type | Verdict | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Sellability | P | Overall | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IDEA-15 | Spanish ISP block monitor and evidence log | C | KILL | 2 | 2 | 2 | 3 | 2 | 5 | 1 | 2 | 2.38 | 2 | 2.23 | high |
| IDEA-59 | Ley de Startups benefits keeper | C (B) | KILL | 2 | 2 | 2 | 3 | 3 | 4 | 1 | 2 | 2.38 | 2 | 2.23 | medium |
| IDEA-60 | Public-funding readiness and post-award tracker | B (A) | KILL | 3 | 2 | 3 | 3 | 2 | 4 | 2 | 2 | 2.63 | 3 | 2.78 | medium |
| IDEA-61 | R&D-credit evidence tracker, reshaped to sell through consultancies and certifiers, with a monetisation-compliance tail | B (A) | RESHAPE | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 4 | 3.13 | 4 | 3.48 | medium |
| IDEA-62 | Spanish-language creator matching for indie studios | B (C) | KILL | 2 | 1 | 3 | 3 | 2 | 4 | 2 | 2 | 2.38 | 4 | 3.03 | medium |
| IDEA-63 | Fandango Arena [U4], second reshape: €6.99–7.99 co-op physics game with cross-platform chat chaos | B (game) | RESHAPE, pilot behind a Next Fest wishlist gate | 4 | 5 | 5 | 3 | 2 | 3 | 2 | 3 | 3.38 | 3 | 3.23 | medium |
| IDEA-64 | LigaHub [U5], reshaped: points-only cross-platform companion | B (platform) | KILL | 1 | 1 | 2 | 2 | 2 | 4 | 1 | 2 | 1.88 | 1 | 1.53 | medium |
| IDEA-64 (original) | LigaHub as given: league platform with a real-money-style transfer market | B (platform) | KILL | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 3 | 1.50 | 1 | 1.30 | high |

IDEA-61's founder-subscription version, as specified, scores Sellability 3.00, P 4, Overall 3.40.

**Headlines**
- **No idea in this batch is a clean GO.**
  - Two survive only as reshapes:
    - IDEA-61: R&D credits, sold through consultancies.
    - IDEA-63: the user's game, as a cheap pilot behind a hard wishlist gate.
  - The other five are killed:
    - IDEA-15 (free tracker and evidence form already exist; the court order expires 20 Jun 2027);
    - IDEA-59 (about 2,000 buyers; Capboard and the ENISA test already cover most of it);
    - IDEA-60 (ENISA's free test and Fandit);
    - IDEA-62 (about 800 Spanish studios; Keymailer and Lurkit);
    - IDEA-64 (illegal as given; no demand once reshaped).
- **The section-5 conflicts for this batch** are settled in the idea sections and in section 3:
  - C-26: €100k angel base; ENISA's silence means approval.
  - C-28: Twitch €4.99; Kings League ERE of 41; the Kings League funding total stays open.
  - The minors' bill lapsed on 6 Oct 2026.
  - The ISP-blocking order expires on 20 Jun 2027.

## 2. Ideas

#### IDEA-15: Spanish ISP block monitor and evidence log for websites and online shops — KILL (high)

**Validated definition.** A €5/domain/month monitor that probes a customer's domains from Spanish residential ISPs (Movistar, Vodafone, Orange, MásMóvil, Digi), alerts when the court-ordered LaLiga/Telefónica IP blocks make the site unreachable, keeps a timestamped evidence log for claims, and suggests the CDN change that restores access. Validation confirms the problem is real and large in aggregate. It also finds that the data layer already exists for free, the per-site impact is small and rotates between sites, no compensation route has been used, and the main court authorisation expires on 20 June 2027. As a standalone paid product it fails. The only part worth keeping is a cross-cutting warning for every SaaS idea in this research (section 3).

**(a) Problem reality and rule status (Oct 2026)**
- **Size of the problem.** OONI measured 554,507 domains blocked at some point between 1 Jan and 1 Jun 2026, about 5.8% of the 9.2M domains it tested; elsewhere in the same report the figure is 554,510. The blocks covered 7,441 unique IPs. Cloudflare (AS13335) accounts for 501,305 of the domains (90.4%) on 2,218 IPs. Blocking is mostly at the IP level; Digi also intercepts TLS with a self-signed certificate. Blocks "begin shortly before kick-off" and end after the final whistle. On Telefónica, 144 one-hour windows had more than 400,000 domains blocked; on Orange, 103 [new: https://ooni.org/post/2026-laliga-collateral/, published 30 Jun 2026]. The report gives no count of .es domains or of Spanish businesses.
- **Still happening in the 2026–27 season.** I downloaded the hayahora.futbol block history and analysed it (24 Aug–23 Oct 2026; my own analysis, data current to 23 Oct 2026 18:38Z) [new: https://hayahora.futbol/estado/data.json, seen 23 Oct 2026]:
  - 3,507 distinct IPs were blocked across the five ISPs, 99% of them Cloudflare. Vercel, Cloudflare R2, Tencent CDN, Lovable, AWS CloudFront and BunnyCDN also appear.
  - On match days, 160–480 IPs were blocked at peak; the maximum was 480 on 10 Oct 2026. Blocks occurred on most weekends from 26 Aug to 18 Oct. None were recorded between 21 Sep and 4 Oct; the reason (a fixture break or a monitoring gap) was not established.
  - At least one IP was blocked during about 318 of the 1,440 hours (about 22%).
  - **Per-site impact is small:** for an IP–ISP pair that was blocked at all, the median total was 4.0 hours over the two months. The 90th percentile was 12.3 hours and the maximum 149.7 hours. Blocks rotate across Cloudflare's shared IPs, so a typical site goes dark for a few hours a month, not every match.
- **Legal basis.** LaLiga's dynamic-blocking authorisation comes from Juzgado Mercantil nº 6 de Barcelona (order of 18 Dec 2024). It covers three seasons from 2024/25, so 2026/27 is the last; coverage expires on 20 June 2027. LaLiga and Telefónica are expected to ask for an extension [new: https://www.xatakamovil.com/movil-y-sociedad/empieza-laliga-vuelven-bloqueos-ips, published 17 Aug 2026; order date from https://www.genbeta.com/actualidad/bloqueos-ip-laliga-amenazan-volver-proxima-temporada-eso-cloudflare-ha-recurrido-al-constitucional, 10 Jun 2025].
- **A second, separate order.** Juzgado Mercantil nº 9 de Barcelona, at Telefónica Audiovisual Digital's request, extends blocking to other sports (tennis, golf) and to films and series. ISPs must apply lists within 30 minutes. The lists are not public, and no formal appeal was reported [new: https://www.que.es/2026/04/17/bloqueos-futbol-operadoras/, published 17 Apr 2026]. Its duration was not found.
- **Challenges.** Cloudflare and RootedCON lost their nullity motions in March 2025 and filed amparo appeals at the Constitutional Court (RootedCON on 16 May 2025). LaLiga says the appeals still have to pass the admission stage, and no admission decision was found [new: Genbeta, above; search 21]. Congress studied proportionality limits but approved none [new: Xataka Móvil, above]. Any such bill lapsed with the dissolution of 6 Oct 2026; I did not trace a specific initiative, so that last point is an inference.
- **Lapse risk.** The election does not affect court orders. The real change point is 20 June 2027.
- **Section-5 conflict (court numbering).** The notes cite "Juzgado Mercantil nº 9" (que.es) for the extension, while OONI, Genbeta and Xataka cite "nº 6" for the LaLiga order. Both are right: nº 6 issued LaLiga's 2024 order and nº 9 the Telefónica extension.

**(b) Competitors and substitutes**

| Product | What it does | Price | Gap left |
|---|---|---|---|
| hayahora.futbol | Volunteer engineers measure from home lines on Movistar, DIGI, Vodafone, Orange and MásMóvil. It publishes per-ISP blocked-IP lists, a history JSON, and a DNS lookup (blocked.dns.hayahora.futbol) that routers can use [new: https://hayahora.futbol/, seen 23 Oct 2026] | Free | No per-domain alerts, evidence PDF or SLA |
| AES "STOP #Laligagate: comparte tu caso" | The startup association collects affected sites' evidence (dates, revenue with and without football, screenshots) and points users to hayahora.futbol [new: https://asociacionstartups.es/laligagate/, seen 23 Oct 2026] | Free | No monitoring; no claim process described |
| OONI Probe / Explorer | Open measurement data; produced the report above | Free | Not a business tool |
| Globalping (jsDelivr) | Free probe network. Its public probe list shows 70 probes in Spain, 26 of them tagged "eyeball" (residential), including Digi (5), Orange (4), Vodafone (3), Telefónica (3) and Xtra Telecom/MásMóvil AS15704 (2) [new: https://api.globalping.io/v1/probes, seen 23 Oct 2026; my count] | Free API | A copier can build the product on it in days |
| Checkly | Monitoring from AWS cloud regions; no Spanish location listed [new: https://www.checklyhq.com/docs/monitoring/global-locations/, seen 23 Oct 2026] | n/a | Data-centre vantage points do not see residential ISP blocks (inference) |
| UptimeRobot | Free (50 monitors, 5-minute checks); Solo $12/month annual; 4 broad regions only [new: https://uptimerobot.com/pricing/, seen 23 Oct 2026] | $0–12/month | No ISP-level vantage points |

There is a narrow packaging gap: per-domain residential alerts plus an evidence PDF. Free tools cover the data and AES covers evidence collection.

**(c) Buyers and market size.** No count of affected Spanish sites exists (OONI has no TLD or country split). If Spanish-owned domains were 1–3% of OONI's 554k, that would be about 5,500–16,600 domains. This is a proportional inference, unverified. AES has 1,500–2,000 member startups [notes: C-26; startups track section 5]. Revenue ceiling: even 2,000 paying domains at €5/month is about €120k a year, and the season-bound value falls to zero if blocking ends in June 2027.

**(d) Willingness to pay.** Weak.
- Generic uptime monitoring costs $0–12/month (UptimeRobot, above).
- The core facts are free (hayahora, AES).
- Neither of two searches (3 and 21) found a compensation award or claim, so the evidence log has no proven monetary use.
- A typical affected site loses about 4 hours over two months (analysis above). Weekend evenings matter to e-commerce, but the loss per site is small.

**(e) Distribution.** AES's #Laligagate campaign and e-commerce agencies are real channels, but AES already sends users to the free tracker. High-intent searches ("web bloqueada fútbol") exist but were not sized.

**(f) Build and legal.** Software MVP in under 4 weeks on Globalping or RIPE Atlas plus hayahora's lists, or on own SIM-card probes. Probing public sites is ordinary monitoring. Publishing block evidence about third parties was not legally checked ([I] below). No certification is needed.

**(g) Defensibility.** None. The data is free and open, and a copier with Globalping and a weekend could match it. Cloudflare could also fix it (dedicated IPs, or leaving blocked ranges).

**(h) Kill criteria**
- *Block frequency drops sharply in the 2026–27 season:* **not met.** Blocks continued on most weekends to 18 Oct 2026, with peaks of 160–480 IPs/day.
- *Fewer than 100 paying domains after three months:* **open** [I].
- *Free community trackers exist:* **met in substance.** hayahora.futbol, AES's form and OONI cover the data; only alerting and evidence-PDF packaging is left.
- **New kill factor:** the LaLiga authorisation expires on 20 June 2027, so the product's value may end with it.

**Scores (rubric as given)**
- S1 Urgency **2**: occasional for any one site (median 4 hours blocked in two months); no legal duty.
- S2 Buyers **2**: about 5k–17k affected Spanish domains by proportional inference; no official count.
- S3 WTP **2**: free substitutes; uptime monitors cost $0–12; no compensation route found.
- S4 Reach **3**: AES campaign and agencies exist, but they already promote the free tool.
- S5 Gap **2**: free tracker, free probes and a free evidence form; only packaging is missing.
- S6 Build **5**: under 4 weeks.
- S7 Defensibility **1**: open data, trivially copied.
- S8 Retention **2**: seasonal, and may end in June 2027.
- **Sellability 2.38. P 2:** real but intermittent losses for most sites. **Overall 2.23.**

**Open [I] checks**
- A lawyer's view on publishing block evidence and on any damages route (civil claim against the rights-holders, or an abnormal-functioning-of-justice claim).
- Whether AES plans collective action.
- How many AES members lost sales. AES's form asks for revenue with and without football, but no aggregate is published.

**What would change the verdict**
- A court or settlement awarding damages to an affected business, which would create demand for evidence.
- A renewed authorisation from June 2027 that blocks more broadly.
- AES or an agency network wanting a white-label paid tool.
- Even then, the better shape is a hosting or failover feature (dedicated or non-shared IPs, or automatic DNS failover during match windows) inside IDEA-13's managed hosting, not a monitor.

#### IDEA-59: Ley de Startups benefits keeper (certification, angel certificates, ESOP clock) — KILL (medium)

**Validated definition.** A €9/month (or €90/year) tool for ENISA-certified startups. It checks eligibility, monitors the art. 3/6 thresholds (age 5/7 years, €10M turnover, 60% of staff on Spanish contracts, no dividends), generates the investor certificate required by art. 68.1 LIRPF for the 50% angel deduction, and tracks holding windows and the ESOP 10-year tax date. The rules are confirmed and stable. The buyer base is about 2,000 companies. The main loss trigger (ageing out) is predictable without software. A Spanish cap-table tool already covers the equity side for about €270 a year. It fails as a product; at most it is a feature for a cap-table tool or a gestoría cockpit (IDEA-06).

**(a) Problem reality and rule status**
- **Law unchanged.** Ley 28/2022 shows "Última actualización, publicada el 22/12/2022" [new: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21739, seen 23 Oct 2026]. Lapse risk is nil, and no reform bill exists to lapse [notes: STA-01].
- **C-26: ENISA's silence means approval.** Art. 4 gives ENISA three months, after which the application is approved by "silencio administrativo positivo" [new: BOE above]. Legalitas's "desestimada" is wrong.
- **What ends the status.** Art. 6 lists the loss triggers: ceasing to meet any art. 3 requirement, in particular at the end of the 5- or 7-year period, and turnover above €10M (art. 6.d). The 60% rule counts staff "con un contrato laboral en España" [new: BOE above]. How EOR staff and contractors count is not addressed in the text: open [I] for a lawyer.
- **Angel deduction, from the LIRPF text (art. 68.1)** [new: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764, seen 23 Oct 2026]:
  - 50% of the amount subscribed, on a maximum base of **€100,000 a year**. This resolves C-26: Venza's €250k is wrong.
  - It applies to any SA or SL with real activity and **own funds of €400,000 or less** at the start of the tax period of acquisition, not only to certified startups.
  - Shares must be bought at incorporation or in a capital increase within 5 years (7 for empresas emergentes) and held for more than 3 and less than 12 years.
  - The investor's stake is capped at 40%; the cap does not apply to the founders of an empresa emergente.
  - Amounts that take a regional deduction are excluded from the state base.
  - The certificate must be issued by the company, "indicando el cumplimiento de los requisitos" of 68.1.2.º for the tax period of acquisition.
  - The useful automatable check is therefore the €400k own-funds test per round, not certification status.
- **Scale.** 2,529 ever certified, 2,046 still certified and 483 lost by 11 Oct 2026 (Economía 3, from ENISA's public search). The article gives the general grounds for loss (failing a requirement, turnover above €10M, acquisition by a non-certified company, a single dividend) but **no breakdown of why the 483 were lost** [new: https://economia3.com/2026/10/15/762915-certificado-de-empresa-emergente-2-529-startups-lo-tienen-pero-no-garantiza-el-visado/, 15 Oct 2026]. ENISA's page shows 2,527 [new: https://www.enisa.es/servicios/certificacion/, seen 23 Oct 2026]. The 2,527/2,529 gap (C-26) is a timing or source difference, and both are "ever certified" counts.

**(b) Competitors**

| Product | Scope | Price | Notes |
|---|---|---|---|
| ENISA portal and FAQ | Free certification; requirements overview; ENISA's homepage invites a "test y verifica si puedes financiarte o certificarte" [new: https://www.enisa.es/, seen 23 Oct 2026] | Free | No monitoring. Kill criterion "ENISA adds monitoring": **not met** |
| Capboard (Spanish) | Cap table, share register (libro de socios), automatic share certificates, ESOP/phantom-share/SAR grants with automated grant letters, data room, shareholder meetings; 450+ companies (search 7) [new: https://capboard.io/precios, seen 23 Oct 2026] | €3/stakeholder/month monthly (minimum €45/month, 15 stakeholders) or €18/stakeholder/year (minimum €270/year), excl. VAT; premium support €50/month [new: https://www.capboard.io/api/unlogged/pricing?fake_country=ES, seen 23 Oct 2026] | No Ley de Startups monitoring or angel-certificate feature on its pricing page. It is the obvious incumbent to add one |
| Carta / Pulley / Ledgy | Global cap-table tools. Carta is free to 25 stakeholders; Pulley from $1,200/year (secondary source) [new: https://resources.rework.com/es/tools/equity-cap-table/best-cap-table-software-2026, via search 7] | — | Ledgy's pricing page returned 404 and Carta's 403 |
| Gestorías, lawyers, Premoney, Managora | Certificates and certification help | No published fees (search 22 found none) | — |

**(c) Buyers and market size.** About 2,046 certified companies, plus young SLs raising from Spanish angels with own funds of €400k or less (uncounted). More than 5,000 active startups [notes: STA-01]. Ceiling: 2,046 × €90/year ≈ €184k a year at 100% penetration. A realistic 10–20% share gives about €18k–37k a year.

**(d) Willingness to pay.** Weak.
- Certification is free [new: ENISA page above].
- Search 22 found no adviser fee data.
- The nearest paid adjacent tool, Capboard, costs €270/year and already issues share certificates and ESOP letters.
- The ESOP 10-year clock only matters to firms with grants above the €50k exemption [notes: STA-02].

**(e) Distribution.** Good targeting exists but no proven partner programme. ENISA publishes a public search of certified companies, filterable by year, sector and region [new: https://www.enisa.es/sobre-enisa/consuta-datos-publicos/, seen 23 Oct 2026]. That gives a ready lead list. AES (1,500–2,000 members), accelerators, and Capboard as a possible partner are the other channels.

**(f) Build and legal.** Rules engine, CSV imports and lawyer-reviewed templates: about 1–2 months. The certificate's content is defined by law (art. 68.1.5.º), so the templates are simple. Liability for wrong certificates would need disclaimers.

**(g) Defensibility.** None. The rules are public and a cap-table vendor or gestoría tool can add them in weeks.

**(h) Kill criteria**
- *Fewer than 30% of certified startups issue angel certificates or track thresholds:* **open** [I].
- *ENISA adds monitoring:* **not met**, though ENISA offers an eligibility test.
- **Added by this validation:** the most common loss trigger (age) is a date known at incorporation, so monitoring adds little value. This weakens the case; the reasons for the 483 losses are not published.

**Scores**
- S1 **2**: rare, predictable events; no penalty deadline.
- S2 **2**: about 2,000 certified, about 5,000 eligible.
- S3 **2**: free official route; Capboard covers the paid adjacent need.
- S4 **3**: ENISA's public list, AES and accelerators; unproven.
- S5 **3**: no dedicated tool, but cheap partial substitutes.
- S6 **4**: 1–2 months with legal review.
- S7 **1**: trivially copied.
- S8 **2**: rare events; status ends at 5–7 years.
- **Sellability 2.38. P 2:** costly only in rare avoidable cases (a dividend, a breach of the 60% rule, an investor losing the 50% deduction). **Overall 2.23.**

**Open [I] checks**
- Why the 483 certifications were lost: a transparency request to ENISA.
- How the 60% rule treats EOR staff.
- A price test with AES members.
- Whether Capboard would partner.

**What would change the verdict**
- Evidence that avoidable losses (dividends, the 60% rule, the €400k own-funds test failing for angels) are common.
- A Ley de Startups reform after the election that adds reporting duties, for example a periodic recertification.
- Either would make it a feature to sell through Capboard-type tools or gestorías (IDEA-06), not a standalone product.

#### IDEA-60: Public-funding readiness and post-award tracker for startups (ENISA, CDTI, regional agencies) — KILL (medium)

**Validated definition.** The idea tested is a €29/month (or €149 per pack) tool for pre-seed to Series A startups:
- an own-funds calculator for ENISA's "fondos propios ≥ préstamo" rule;
- a rules checker and calendar for ENISA, CDTI, Neotec, the EIC and regional lines;
- application checklists, and post-award reporting dates.

The rules are real and verified. But ENISA now advertises its own eligibility test. A Spanish grant-search SaaS (Fandit) already covers the calendar and alerts. Consultants offer free assessments. Use is once a year at most. As a standalone product it fails. The only distinctive part, post-award justification, belongs in IDEA-26 (batch 2).

**(a) Rule status (Oct 2026)**
- **ENISA lines.** ENISA lists five financing lines [new: https://www.enisa.es/servicios/financiacion/, seen 23 Oct 2026]:
  - Startups y Pymes, €25,000–€1,500,000;
  - Innovación x Clima;
  - Emprendedoras Digitales;
  - AgroInnpulso;
  - Audiovisual e Industrias Culturales y Creativas, which includes video games.
- **ENISA conditions** (same page):
  - own funds at least equal to the amount requested ("Debes tener fondos propios que, al menos, igualen la cantidad solicitada");
  - audited accounts above €300k, filed accounts below;
  - 0.5% opening fee, 2 years interest-only, generally up to 7 years.
- **ENISA volumes.** The homepage shows 10,004 loans disbursed, 8,654 companies financed and €1,551M lent, and says answers come in under 2 months [new: https://www.enisa.es/, seen 23 Oct 2026]. That is a newer figure than the notes' "about 9,000 loans to 7,800 companies by end-2024" [notes: STA-04].
- **Accumulated losses.** Tetuan Valley and Premoney say accumulated losses reduce own funds and that the own-funds rule is the most common cause of denial [new: https://tetuanvalley.com/blog-financiacion-publica-para-startups/, 28 Jul 2026]. ENISA's own FAQ does not address accumulated losses.
- **Neotec 2026** [new: https://www.ciencia.gob.es/Convocatorias/2026/NEOTEC2026.html, seen 23 Oct 2026]:
  - closed; applications ran from 14 Apr to 14 May 2026 (12:00);
  - budget €20,383,300;
  - framed in the Plan Estatal 2024–2027.
- **Neotec 2026 details from search 8** (a summary of the CDTI call PDF at https://www.cdti.es/sites/default/files/2026-04/convocatoria_neotec_2026.pdf; the PDF itself was not opened):
  - eligible budget €175k–€750k;
  - advances up to 60%, at most €150k, without guarantees;
  - companies up to 3 years old with at least €20k share capital;
  - at least €5M reserved for women-led projects.
- **Neotec 2027.** It is likely to follow the same April–May pattern under the Plan Estatal 2024–2027. That is an inference; no 2027 date was found.
- **Caretaker effect.** A caretaker government handles routine business. CDTI and ENISA calls are agency-level, so a long delay is unlikely but possible (inference). The new Cortes meet on 23 Dec 2026.
- **New claim, unverified:** Tetuan Valley says empresas emergentes can monetise R&D credits "without discount up to €50,000". This is not in the BOE Corporate Tax Law (see IDEA-61) and is treated as unverified.

**(b) Competitors**

| Product | What | Price |
|---|---|---|
| ENISA website test | "Haz nuestro test y verifica si puedes financiarte o certificarte" [new: https://www.enisa.es/, seen 23 Oct 2026] | Free |
| Fandit (Spanish) | Grant search with daily alerts and an unlimited AI assistant; claims more than 18,000 calls a year (vendor claim, search 9); distributed through Grupo2000 asesorías and Repsol Solred | Pro €56/month on annual billing (€70 monthly), Premium €200, Corporate €480 [new: https://fandit.es/precios/, seen 23 Oct 2026] |
| Premoney (with Tetuan Valley) | Says it has handled more than 400 public-funding files; offers a "sin compromiso" assessment [new: Tetuan Valley, above] | Not published |
| Fractional CFO | Financial models for applications | €750 / €1,250 / €2,000 a month [notes: STA-04] |
| Newsletters (The Startup Oasis) | Calendar and guidance | Free [notes: STA-04] |

Nobody was found publishing outcome data by funding line, which the notes call the only defensible asset. That gap is real, but it would build slowly.

**(c) Buyers and market size.** ENISA has financed 8,654 companies in its history. Neotec 2026 funds roughly 50–100 projects (€20.4M at €175k–€750k; inference). Startup applicants per year are probably in the low thousands (inference, no count found). At €29/month with high churn after each application, the ceiling is roughly €100k–300k a year.

**(d) Willingness to pay.** Founders do pay for help with funding (consultant fees are unpublished; fractional CFOs cost €750–2,000 a month). But they pay for outcomes or for done-for-you work, not for calculators. Fandit's €56–70/month is aimed at consultants.

**(e) Distribution.** Accelerators, The Startup Oasis, ENISA's public certified list, and searches such as "requisitos ENISA fondos propios" [notes: STA-04]. Consultants are competitors, not channels.

**(f) Build.** About 1–2 months. The main running cost is keeping the line rules current, which Fandit already does across 18,000 calls.

**(g) Defensibility.** Low: calculators and calendars are copyable. An outcomes dataset would take years and many users.

**(h) Kill criteria**
- *ENISA or consultants start offering free pre-checks:* **partly met.** ENISA advertises a free test (its contents were not inspected), and Premoney offers free assessments.
- *Fewer than 50 paying startups after six months:* **open** [I].

**Scores**
- S1 **3**: recurring need with call windows, but no legal duty.
- S2 **2**: low thousands of applicants a year.
- S3 **3**: spend exists on consultants and CFOs, not on tools.
- S4 **3**: accelerators and newsletters, unproven.
- S5 **2**: free ENISA test, Fandit and free consultant assessments.
- S6 **4**: 1–2 months.
- S7 **2**: maintained calendar; copyable.
- S8 **2**: at most once a year.
- **Sellability 2.63. P 3:** refusals and delays cost months, but software does not change approval. **Overall 2.78.**

**Open [I] checks**
- What ENISA's test checks.
- Five consultant interviews on fee models (success fee or retainer).
- Whether accelerators would pay for a cohort licence.

**What would change the verdict**
- Accelerators or consultants wanting a white-label own-funds and reporting engine.
- Evidence that post-award reporting failures cause repayments at startups. If so, fold it into IDEA-26 (grant justification) as a startup module rather than building it on its own.

#### IDEA-61: R&D-credit evidence tracker and cash-refund pack for loss-making startups — RESHAPE (medium)

**Validated definition (after reshape).** An evidence and compliance layer for the Spanish R&D tax credit (LIS art. 35) and its cash refund (art. 39.2). It is sold mainly through R&D-tax consultancies and ENAC-accredited certification bodies, which serve R&D-intensive startups and SMEs, with self-serve founders as a second channel.

What it does:
- Captures R&D project records and weekly staff-time allocations from Slack or email first, then Jira or GitHub.
- Imports payroll to build the eligible base.
- Produces a UNE 166001-style project file for the certification body, the input for the binding informe motivado (IMV) that cash monetisation requires.
- Tracks the post-refund conditions that create a clawback risk under art. 39.2 (no fall in average headcount; reinvestment within 24 months), which consultants rarely monitor after filing.

**Price hypothesis (reshaped):** about €300–600 per client company per year through partners, or about €49/month self-serve. The founder-only €79/month subscription is dropped as the main model.

**(a) Rules verified in the BOE.** Corporate tax law consolidated text, "Última actualización publicada el 02/09/2026" [new: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328, seen 23 Oct 2026]:
- **Rates (art. 35.1.c):** R&D 25% of the period's spend, and 42% on the excess over the previous two years' average. An additional 17% applies to the staff cost of qualified researchers assigned exclusively to R&D. 8% applies to fixed assets used exclusively for R&D (not buildings). Technological innovation is 12% (art. 35.2.c). The notes' "25–42% + 17%, 12%" is confirmed [notes: STA-05].
- **Carry-forward (art. 39.1):** unused R&D credits carry forward for 18 years. For new entities, the clock can be deferred to the first profitable year.
- **Cash refund (art. 39.2):** the credit can leave the normal limit "con un descuento del 20 por ciento", and if the tax due is insufficient its "abono" can be requested through the tax return. There is no late-payment interest. The conditions are:
  - (a) at least one year has passed since the end of the period in which the credit arose;
  - (b) average headcount, overall or in R&D, is not reduced until the end of period (c);
  - (c) an equal amount is reinvested in R&D or innovation within 24 months;
  - (d) **an informe motivado or an AEAT advance valuation agreement is mandatory**.
  - Caps: €1M a year for technological innovation and €3M for R&D plus innovation. A further €2M is available when R&D exceeds 10% of turnover.
  - Breaching a condition triggers regularisation (art. 125.3).
- **Single-source issue in the notes.** Tetuan Valley called the binding certificate "recommended" [notes: STA-05]. For monetisation it is **required**.
- **Not found.** Tetuan Valley's line that "empresas emergentes get no discount up to €50,000" does not appear: neither "emergente" nor "Ley 28/2022" occurs in the corporate tax text (my search of the BOE page). Treat it as unverified.
- **Election.** No lapse risk; this is consolidated law.

**(b) Competitors**
- R&D-tax consultancies sell evidence and claim work, and their fee models are not public. Two searches found none; Tecnocim's service pages describe the IMV process without prices [new: https://tecnociminnova.com/es/servicios/deducciones-fiscales/informe-motivado, via search 10]. Industry names such as FI Group, Ayming, Leyton and Kaudal were not checked, so their fees and tooling are unverified.
- ENAC-accredited certification bodies run the step before the Ministry issues the IMV. In a 2014 ACCIÓ/ACIE deck, certification took about 4–6 weeks, with a technical evaluation, an accounting audit and a committee [new: https://www.accio.gencat.cat/web/.content/bancconeixement/altres_documents/documents/ACCIO-seguretat-juridica-incentius-fiscals-idi.pdf, 19 Feb 2014; dated].
- Accounting tools (Holded and others) were not shown computing R&D credits. This is unverified, not a confirmed gap.

**(c) Buyers and market size.** In Catalonia, about 2,100 of 2,403 startups invest in R&D (ACCIÓ, 89%) [notes: STA-05]. National counts of R&D startups and SMEs, and AEAT data on how many claim or monetise, were not found (searches 10 and 11). Plausibly 5k–20k R&D-active small firms nationally (inference). The value per client is high: a startup spending €400k on R&D generates about €100k+ of credit, or about €80k in cash after the 20% discount (arithmetic from art. 35 and 39.2). That supports a few hundred euros a year per client.

**(d) Willingness to pay.** Indirect but real. Firms already pay consultancies (fees unknown) and certification bodies (prices unknown). Consultancies taking success fees have a reason to buy tools that cut their evidence hours; founders paying a subscription for the same evidence is less likely (notes risk 1).

**(e) Distribution.** The reshaped channel is consultancies and certification bodies. Deeptech hubs and accelerators, especially Barcelona (ACCIÓ), and university spin-off programmes are secondary [notes: STA-05, STA-21].

**(f) Build and legal.** About 2–4 months: integrations (Slack/Jira/GitHub, payroll) and a legal review of the rules. Liability is limited by not issuing opinions; the IMV comes from the Ministry. The data is moderately sensitive (payroll).

**(g) Defensibility.** Some: consultant and certifier channel lock-in, plus each client's accumulated evidence history over the 18-year carry-forward and the 24-month reinvestment window. Time tracking itself is copyable.

**(h) Kill criteria**
- *Consultants already do the evidence work for free and founders will not pay:* **open** [I]. This validation sidesteps it by making consultants the buyer.
- *The rules differ from the single source:* **resolved.** The rules are confirmed, with the correction that the IMV or advance agreement is mandatory for monetisation.

**Scores (reshaped version; the founder-subscription version as specified scores 3.00 / P 4 / Overall 3.40, with S7 at 2)**
- S1 **3**: annual cycle, plus dated post-refund conditions (24-month reinvestment, headcount).
- S2 **2**: an estimated 5k–20k R&D-active small firms (no national count).
- S3 **3**: adjacent spend on consultants and certifiers; fees unknown.
- S4 **3**: consultant and certifier channel, unproven.
- S5 **4**: consultants and manual work; no Spanish SaaS found.
- S6 **3**: integration-heavy, 2–4 months.
- S7 **3**: partner lock-in and accumulated evidence.
- S8 **4**: continuous time records, an 18-year carry-forward and a clawback-tracked tail.
- **Sellability 3.13. P 4:** loss-making R&D startups leave five- or six-figure cash on the table. **Overall 3.48.**

**Open [I] checks**
- Five consultancies and two certification bodies: their evidence-gathering hours per client and their fee basis (success fee as a percentage of the credit).
- Whether they already have client portals.
- 15 founder interviews as planned.
- How many firms request the cash refund each year (AEAT statistics not found).
- The cost and lead time of the certification-plus-IMV route in 2026.

**What would change the verdict**
- Toward GO: if consultancies confirm they spend many hours per client on evidence and would pay for a portal.
- Toward KILL: if the large consultancies already give clients a free portal, or if AEAT data shows very few small firms monetise.

#### IDEA-62: Spanish-language creator matching and key-campaign tracker for indie game studios — KILL (medium)

**Validated definition.** A €29/month (or €99 per campaign) SaaS for indie studios that do the following:
- Index Spanish-language Twitch and Kick creators by category, average viewers, country and schedule.
- Distribute Steam keys.
- Detect and report the resulting streams.

The pain (discoverability) is severe and well evidenced. But the paying base in Spain is about 800 studios with tiny budgets. Global tools with free tiers and 90k–275k creators already exist. Language filtering is trivial for any incumbent to add. Grants do not fund this kind of spend. **KILL as a standalone SaaS.** Keep the know-how as a launch capability for IDEA-63.

**(a) Problem reality.** The pain is confirmed [notes: GAM-24, GAM-03]:
- Steam gets about 19–20k releases a year; half of 2025's releases got fewer than 10 reviews and 40% earned under $100.
- 2026's breakout co-op games show the upside. Meccha Chameleon was released 9 Jun 2026 by solo developer lemorion_1224 and has 44,105 English reviews [new: https://store.steampowered.com/app/4704690/, seen 23 Oct 2026].
- No regulation is involved, so the election has no effect.

**(b) Competitors**

| Tool | Scope | Price | Source |
|---|---|---|---|
| Keymailer (publisher side now branded Partnier) | Key distribution to creators; Partnier cites 275,000+ creators and 60,000+ influencers; free for creators | Free tier (10 engagements a month); Indie Special $24.99/month ($249/year); Game Subscription $49/month; Catalog $99/month; managed campaigns from $999 | [new: https://www.keymailer.co/pricing, seen 23 Oct 2026]; prices from a secondary review [new: https://www.influencer-hero.com/kr/blogs/keymailer-pricing, via search 15] |
| Lurkit | Key campaigns, paid "Quests", creator CRM; "90k+" / "100k+ verified creators" on Twitch, YouTube, Shorts and TikTok | Indie/Studio/Publisher plans "Contact for pricing"; 20% commission per paid Quest; "up to 70% discount" | [new: https://lurkit.gg/ and https://lurkit.gg/pricing, seen 23 Oct 2026] |
| Woovit | Was a key-distribution tool | — | The domain now serves unrelated betting content [new: https://www.woovit.com/, seen 23 Oct 2026]. A failed or abandoned player |
| Streamloots | Viewer-paid interactive cards for streamers; 100,000+ creators; Twitch, YouTube and Kick logins | 80–90% revenue share to creators | [new: https://www.streamloots.com/, seen 23 Oct 2026]. An adjacent creator-monetisation network |
| Twitch Drops | Platform-native campaigns | Mostly large publishers | [notes: GAM-18] |

Whether Keymailer and Lurkit filter creators by language could not be seen on their public pages, so that kill criterion stays open. Twitch's Get Streams API takes a language parameter (background knowledge; the Helix docs page could not be fully read in this session). Spanish filtering is therefore an easy feature, not a moat.

**(c) Buyers and market size**
- Spain has 815 studios, about 440 of them micro-studios [notes: GAM-03].
- Latin America and the Caribbean have about 1,800 studios including Brazil, which is Portuguese-speaking; most are micro or small, many informal [new: IDB, https://publications.iadb.org/es/los-videojuegos-no-son-un-juego-los-desconocidos-exitos-de-los-estudios-de-america-latina-y-el, Sep 2025, via search 20]. The Spanish-speaking share was not found.
- The Spanish-speaking audience matters to some games but is a minority. Spanish-language Steam reviews as a share of English reviews (my count from store pages, 23 Oct 2026):

| Game | Spanish reviews vs English | Share |
|---|---|---|
| R.E.P.O. | 25,691 Spain + 5,137 Latin America vs 140,371 | 22% |
| PEAK | 17,648 + 4,382 vs 147,179 | 15% |
| Meccha Chameleon | 4,138 (Spain) vs 44,105 | 9% |
| Gamble With Your Friends | 826 (Spain) vs 12,622 | 7% |
| Chained Together | 1,153 (Spain) vs 20,670 | 6% |
| YAPYAP | 227 (Spain) vs 4,004 | 6% |
| Lethal Company | 13,562 (Spain) vs 276,753 | 5% |

- Ceiling: 440 micro-studios × €29 × 12 ≈ €153k a year at 100%; a realistic share is a fraction of that.

**(d) Willingness to pay**
- Anchors are $0–99/month (Keymailer) or commission (Lurkit 20%).
- 39% of Spanish studios need €50k–150k for their whole next project [notes: GAM-03].
- Grants do not cover a tool like this:
  - Madrid's 2026 call funds only creative development (creation, design, programming) of a single narrative game at prototype stage, up to €25k [new: https://www.bocm.es/boletin/CM_Orden_BOCM/2026/03/19/BOCM-20260319-25.PDF, 19 Mar 2026].
  - The national 2026 internationalisation call (€1M, up to €100k per project) is open only to non-profit legal entities [new: https://www.boe.es/boe/dias/2026/10/07/pdfs/BOE-B-2026-32589.pdf, 7 Oct 2026].

**(e) Distribution.** DEV, Mad Games Show, GAMERGY (63,000+ attendees [notes: gaming track section 1]), Next Fest (Feb and Jun 2027 editions listed by Valve [new: https://partner.steamgames.com/doc/marketing/steamnextfest, seen 23 Oct 2026]) and developer Discords. The community is concentrated but small.

**(f) Build and legal**
- About 1–2 months on the Twitch and Kick APIs.
- Kick's terms (modified 23 Mar 2026) ban scraping and "collecting or harvesting any personally identifiable information, including account names" [new: https://kick.com/terms-of-service, seen 23 Oct 2026]. A Kick creator index must use the official API.
- Kick's docs tell developers to review "Developer Terms and Conditions" but give no link. No rate limits are published [new: https://docs.kick.com/getting-started/kick-apps-setup.md and https://docs.kick.com/apis/faqs.md, seen 23 Oct 2026; search 18 found nothing].
- Twitch's developer agreement page renders by script and could not be read: open.

**(g) Defensibility.** Low. A curated Spanish creator graph is the only asset, and incumbents with 90k–275k creators can add a language facet.

**(h) Kill criteria**
- *Fewer than 30 paying studios after six months:* **open** [I].
- *Global tools already filter Spanish creators well:* **open**, filters not visible publicly.
- **Structural kill factor added:** the paying base (about 440–815 Spanish studios) and their budgets cannot support a SaaS, even at full penetration.

**Scores**
- S1 **2**: occasional; one launch per studio every few years.
- S2 **1**: under 5k Spanish paying entities.
- S3 **3**: some spend on Keymailer-type tools.
- S4 **3**: concentrated small community.
- S5 **2**: several decent global tools, some free.
- S6 **4**: 1–2 months.
- S7 **2**: language facet easily copied.
- S8 **2**: campaign-bound.
- **Sellability 2.38. P 4:** discoverability is existential for indies. **Overall 3.03.**

**Open [I] checks**
- 15 studio interviews (marketing budget per launch; how they find creators).
- Test Keymailer and Lurkit for Spanish-language filters.
- Twitch developer-agreement data-use clauses.

**What would change the verdict**
- A buyer with budget, for example ICEX, DEV or a publisher paying for a Spanish-language creator programme for many studios.
- Or the tool proving itself first as the launch engine of IDEA-63.

#### IDEA-63: Fandango Arena reshaped: a cheap streamer-vs-chat co-op physics party game [user idea U4] — RESHAPE (medium)

**Validated definition (after a second reshape).**
- **The game:** a 2–4-player online co-op physics comedy for PC/Steam, built on the user's "funny physics failures", sold globally from day one in English and Spanish (Spain and Latin America).
- **Price:** a single price of €6.99–7.99 (launch discount allowed). Steam's bundle documentation does not describe multi-copy four-packs, so the four-pack is dropped. Friend-group friction is handled by the low price and, optionally, a free "friend's pass" that can only join an owner's session (the model Hazelight uses; not re-verified here).
- **"Chat chaos" mode:** viewers vote on rule cards through the following channels. There is no wagering, no paid random items and no item with money value.
  - Twitch: chat, Channel Points, polls, and optional Bits votes, which Twitch explicitly permits.
  - Kick: chat plus the new Channel Rewards API.
  - YouTube: live chat.
- **Safety defaults:** proximity voice in friends-only lobbies, with mute, block and report, to stay out of PEGI's "unrestricted communication" (PEGI 18) bucket.
- **Team and scope:** a 2–3-person team on an existing engine with off-the-shelf netcode and voice. The vertical slice and Steam page take about 12 weeks. A demo enters the February or June 2027 Next Fest behind a hard wishlist gate.

**Rubric adaptation (stated).** For this game the dimensions mean:
- S1 = strength of demand;
- S2 = reachable players and streamers in Spain and the Spanish-speaking world;
- S3 = evidence that players pay at this price;
- S4 = reach through streamers, Steam and communities;
- S5 = genre saturation (5 = unsaturated);
- S6 = time to a playable demo or vertical slice;
- S7 = IP, community or network effects;
- S8 = replayability and live-ops;
- P = strength of the unmet demand.

**(a) Demand and rule status (Oct 2026)**
- **Cheap co-op is still producing hits in 2026.** Steam store pages, 23 Oct 2026:
  - MECCHA CHAMELEON (solo developer lemorion_1224, released 9 Jun 2026, €6.15): 44,105 English reviews, 90% positive [new: https://store.steampowered.com/app/4704690/];
  - Gamble With Your Friends (1 May 2026, €7.79): 12,622 English reviews, 89% [new: https://store.steampowered.com/app/3892270/]; a source title cited on Wikipedia says it reached 1 million sales [new: https://en.wikipedia.org/wiki/Friendslop, last edited 27 Sep 2026];
  - YAPYAP (3 Feb 2026, €9.75): 4,004 English reviews, 83% [new: https://store.steampowered.com/app/3834090/];
  - BOMBANANA! (2 Sep 2026, €8.15): 1,255 English reviews and 3,932 in total (most likely all languages), 96%, in seven weeks [new: https://store.steampowered.com/app/4656000/].
- **Hits decay fast.** R.E.P.O. drew 20.2M Twitch hours in the past 365 days, down 64.8% on the previous year [new: https://sullygnome.com/game/R.E.P.O./365, seen 23 Oct 2026].
- **Shooter shift.** No new evidence; contradicted for Spain [notes: GAM-11].
- **Minors' digital protection bill: lapsed.** Congress lists initiative 121/000052 as "Concluido – (Caducado)" from 06/10/2026, still at the committee-report stage, with no plenary or Senate vote [new: congreso.es initiative page, seen 23 Oct 2026; URL in section 4]. The loot-box ban, the default parental controls and the age-verification duties therefore do not exist in Spanish law. A new government would have to reintroduce the bill. The EU "Kids Act" is only a leaked draft [notes: GAM-23].
- **PEGI.** A game with unrestricted communication (no blocking or muting, no moderation) is rated PEGI 18. "Paid random items" make a game PEGI 16 or 18 for submissions since June 2026 [new: https://pegi.info/what-do-the-labels-mean, seen 23 Oct 2026]. Whether Steam requires PEGI in Spain was not checked.
- **Gambling law.** Votes with no stake and no prize are outside "juego" (Ley 13/2011 art. 3.a needs a stake that can be transferred) [new: https://www.boe.es/buscar/act.php?id=BOE-A-2011-9280, last updated 31 Dec 2022, seen 23 Oct 2026].
- **Twitch Bits.** Twitch Extension rule 6.1.4 allows Bits "for voting activities". Rule 6.2 bars Bits for monetary-reward gambling (6.2.3), random loot boxes (6.2.4), sweepstakes or contest entries (6.2.5), wagering (6.2.6) and VOIP features (6.2.7) [new: https://dev.twitch.tv/docs/extensions/guidelines-and-policies/, seen 23 Oct 2026]. The stage-1 item "paid Bits votes: to verify" is resolved: they are allowed.

**(b) Competitors and price anchors**
- **Spanish Steam prices, 23 Oct 2026, all undiscounted** (from the Steam appdetails API with cc=es) [new: https://store.steampowered.com/api/appdetails?appids=3241660,3527290,1966720,2881650,3949040,2567870,477160,285900,1260320,386940&cc=es&filters=price_overview]:
  - R.E.P.O. €9.49, PEAK €7.49, Lethal Company €9.75, Content Warning €7.49, RV There Yet? €7.79, Chained Together €4.99;
  - Human Fall Flat €19.99, Gang Beasts €18.99, Party Animals €17.99, Ultimate Chicken Horse €12.99.
  - This confirms the notes' price table exactly [notes: GAM-13].
- **Chat-vs-streamer competition already exists:**
  - Streamer vs. Chat (Vachyáš; Twitch or Kick connection required; viewers become characters and trigger effects; PvP; planned for 2027, playtest open) [new: https://store.steampowered.com/app/4377330/];
  - Chat is Cooked (Stella De; early access since 21 Oct 2026; €15.49; Twitch only; single-player; 1 review) [new: https://store.steampowered.com/app/5332420/];
  - Vs Chat Pack (KevDK, 2022) [new: search 16];
  - Crowd Control, which adds chat chaos to more than 200 existing games for $7.99 or $19.99 a month [notes: GAM-19];
  - Streamloots, viewer-paid interactive cards with 100,000+ creators [new: https://www.streamloots.com/, seen 23 Oct 2026].
- **The gap:** a multiplayer co-op physics game with chat voting built in across platforms is open but unprotected.

**(c) Players and market size**
- **Spain:** 22.8M players, 28% preferring PC, so about 6.4M as an upper bound; about 10.5M monthly Twitch users [notes: GAM-02, GAM-06].
- **Spain-level unit data does not exist** (Steam publishes no country sales; none found). As a buyer-side proxy I counted Spanish-language Steam reviews against English reviews (store pages, 23 Oct 2026):

| Game | Spanish reviews vs English | Share |
|---|---|---|
| R.E.P.O. | 25,691 Spain + 5,137 Latin America vs 140,371 | 22% |
| PEAK | 17,648 + 4,382 vs 147,179 | 15% |
| Meccha Chameleon | 4,138 vs 44,105 | 9% |
| Gamble With Your Friends | 826 vs 12,622 | 7% |
| Chained Together | 1,153 vs 20,670 | 6% |
| YAPYAP | 227 vs 4,004 | 6% |
| Lethal Company | 13,562 vs 276,753 | 5% |

  - Spanish speakers are a real secondary market. In one case (R.E.P.O.) it reached a fifth of the English base; usually it is 5–10%. The game must sell globally.
- **The share of streams in Spanish** stays open. Streams Charts and TwitchTracker returned 403, and SullyGnome's language filter needs scripts.
- **Revenue scenarios** (heuristic, single calibration point). Gamble With Your Friends' reported 1M sales against 12.6k English reviews implies about 80 sales per English review. On that basis:
  - a BOMBANANA!-level result is about 100k units, roughly €0.8M gross at €8 before Steam's share and VAT;
  - a Meccha Chameleon-level hit is about 3.5M units.
  - The median is far lower: 40% of 2025 Steam games earned under $100 [notes: GAM-24].
- **Wishlist benchmarks for the kill gate.** In the February 2026 Next Fest (survey of 182 developers):
  - games entering with 0–999 wishlists gained a median 322;
  - with 1,000–9,999, a median 1,006 (70th percentile 1,722);
  - with 10,000–99,999, a median 5,215.
  - The advice is "at minimum 2000+ wishlists before SNF" [new: https://howtomarketagame.com/2025/03/26/benchmarks-how-many-wishlists-can-i-get-from-steam-next-fest/, updated 8 Apr 2026].
  - Other analyses put the median across all games at about 200–460 (presskit.gg via Cinevva; a Substack analysis; search 5).
  - The "Gold" tier is 7,000–9,999 wishlists gained during the fest.

**(d) Willingness to pay.** Strong at €5–10, verified above; groups multiply the spend [notes: GAM-10]. Above €12.99 the comparables are older and well-known physics brawlers. A 2026 newcomer at €15.49 (Chat is Cooked) has one review so far. The price should be €6.99–7.99.

**(e) Distribution**
- Next Fest editions in February 2027 and June 2027 are listed by Valve [new: https://partner.steamgames.com/doc/marketing/steamnextfest, seen 23 Oct 2026].
- Twitch is the channel for Spain and Kick for Latin America [notes: GAM-06, GAM-08]; also TikTok clips, Mad Games Show, GAMERGY and DEV [notes: G6-I13 channels; GAM-04].
- Spanish creators' record with these co-op hits is unverified: search 4 found nothing tying Ibai, Rubius or AuronPlay to R.E.P.O., PEAK or Chained Together. Chained Together's launch was led by US streamer caseoh_ [notes: GAM-10].
- Context: Ibai's La Velada del Año signed exclusive Netflix rights for 2027–2029 [new: https://www.vozpopuli.com/deportes/la-velada-del-ano-se-emitira-en-netflix-ibai-llanos-sella-la-exclusividad-del-evento-para-tres-temporadas.html, 19 Oct 2026]. This shows top Spanish creators' biggest formats moving to premium platforms, not toward indie co-op games.

**(f) Build feasibility, cost and legal**
- **Platform APIs** (all seen 23 Oct 2026):
  - Twitch: polls (2–5 choices, with extra votes paid in Channel Points) and Channel Points predictions via its API [new: https://dev.twitch.tv/docs/api/reference/]; EventSub covers poll, prediction and reward-redemption events.
  - Kick: Channel Rewards APIs and a redemption webhook were added on 3 Dec 2025, and redemption accept/reject APIs on 15 Jan 2026. Kick still has no polls or predictions endpoints, and publishes no rate limits or developer terms. Its docs tell developers to review "Developer Terms and Conditions" without linking them [new: https://docs.kick.com/changelog.md; https://docs.kick.com/apis/channel-rewards.md; https://docs.kick.com/getting-started/kick-apps-setup.md].
  - YouTube: `liveChatMessages.insert` "adds a message or a poll" [new: https://developers.google.com/youtube/v3/live/docs/liveChatMessages, page updated 15 Oct 2026].
  - TikTok: no public LIVE API among its developer products [new: https://developers.tiktok.com/products/].
- **Cost.** Spanish game-developer pay comes only from aggregators: an average of about €31–32k gross, juniors €18.5–25k, and one source at €47.5k [new: https://www.laps4.com/preguntas-y-respuestas/cuanto-gana-un-desarrollador-de-juegos-en-espana; https://jobicy.com/salaries/es/game-developer (Jul 2026); via search 17; weak sources]. Gross payroll, before employer contributions:
  - the longlist's plan of 4–6 developers for 6–9 months: about €65k–180k;
  - the user's 2–3-person AI-assisted team for 9 months: about €48k–90k.
- **Public money is thin:**
  - Madrid's 2026 call gives at most €25k (20 awards, €500k in total) for a single narrative, original, unpublished game at prototype stage, from a micro or small firm with a Madrid seat. Games under Ley 13/2011 are excluded, and the eligible period ended on 30 Oct 2026 [new: https://www.bocm.es/boletin/CM_Orden_BOCM/2026/03/19/BOCM-20260319-25.PDF, 19 Mar 2026]. A physics party game may fail the "narrative" condition.
  - The national 2026 internationalisation call (€1M) is open to non-profits only [new: https://www.boe.es/boe/dias/2026/10/07/pdfs/BOE-B-2026-32589.pdf, 7 Oct 2026].
  - No 2026 national "promoción" call (2024: €8M, up to €80k) was found (search 6).
  - ENISA's "Audiovisual e Industrias Culturales y Creativas" line covers video games, but requires own funds at least equal to the loan [new: https://www.enisa.es/servicios/financiacion/].
- **Time to playable.** About 8–12 weeks for a first playable with an existing engine [notes: G6-I13]. A vertical slice with polished netcode and voice is closer to 3–4 months.

**(g) Defensibility.** None structural. The concept is being copied already (Streamer vs. Chat, Chat is Cooked). Only execution, timing and relationships with Spanish and Latin American creators can differentiate it. A licensable chat layer would compete with Crowd Control.

**(h) Kill criteria**
- **Wishlist gate (now quantified):**
  - enter the 2027 Next Fest with at least 2,000 wishlists;
  - **GO to early access** if at least 7,000 are gained during the fest (Gold tier);
  - **KILL** if total wishlists after the fest are under 3,000, which is about median performance for 1k–10k entrants.
  - Status: **open** [I].
- **At least three Spanish-speaking creators averaging 1,000+ viewers stream the demo:** **open** [I].
- Neither is triggered by desk evidence.

**Scores (gaming adaptation)**
- S1 **4**: 2026 is still producing hits at €5–10.
- S2 **5**: millions of Spanish-speaking PC players; Spanish reviews are 5–22% of English on comparables.
- S3 **5**: proven spend at the price point.
- S4 **3**: creators are reachable, but virality is English-led and median Next Fest results are low.
- S5 **2**: crowded €5–10 band, and chat-vs-streamer rivals are emerging.
- S6 **3**: vertical slice in about 3–4 months.
- S7 **2**: no moat beyond a future community.
- S8 **3**: rule cards and chat mode add replay value, but the genre decays fast (R.E.P.O. −65% Twitch hours year on year).
- **Sellability 3.38. P 3:** strong appetite for novelty, but well served by a stream of titles. **Overall 3.23.**

**The user's original claims and features (U4)**

| Claim or feature | Verdict | Evidence |
|---|---|---|
| Players are shifting away from competitive shooters | **Contradicted for Spain.** The cheap co-op rise is real globally and coexists with shooters | Spain's top Twitch games for Jan–Sep 2026 are LoL, Valorant and Fortnite [notes: GAM-11]; 2026 co-op hits above |
| Premium price of about $30 | **Contradicted; drop it** | Spanish Steam, 23 Oct 2026: €4.99–9.75 for the hits, €6.15–9.75 for 2026 entrants, €12.99–19.99 for physics party games [new: Steam API above] |
| Native Twitch and Kick integration | **Survives, and stronger than in stage 1** | Twitch API and EventSub; Kick chat plus a Channel Rewards API since Dec 2025; YouTube polls API. Risk: Kick's terms and rate limits are unpublished |
| Viewers vote on rule changes in real time | **Survives as a feature, not a moat** | Allowed (Twitch rule 6.1.4; no stake, so not "juego"); already offered by Crowd Control, Streamer vs. Chat and Chat is Cooked |
| Custom proximity voice chat for shareable clips | **Survives only with safety defaults; drop "custom"** | A genre trait; PEGI 18 if communication is unrestricted. The minors' bill lapsed on 6 Oct 2026, lowering Spanish legal exposure for now. Use existing voice technology (build-cost judgement), friends-only lobbies, and mute/block/report |
| Audiences shaped by Ibai Llanos and AuronPlay | **Partly supported; AuronPlay unverified** | Spanish-speaking creators matter for Spanish-language reach (R.E.P.O.'s Spanish reviews are 22% of its English ones), but no link between Ibai or AuronPlay and these hits was found, and genre virality was English-led |
| "National" target market (user's framing) | **Partly supported; plan global-first** | Spain is 44% of Spanish studios' revenue [notes: GAM-03]; Spanish reviews are usually 5–10% of English |

**Open [I] checks**
- Build the vertical slice and Steam page, and record pre-fest wishlists.
- Get commitments from 10 Spanish and Latin American creators to stream the demo.
- Playtest the voice-safety defaults with groups of friends.
- Confirm whether a friend's-pass app is feasible on Steam.
- Confirm Kick's developer terms by e-mail (developers@kick.com, given in Kick's docs).

**What would change the verdict**
- **To GO:** a Spanish-speaking creator averaging 1,000+ viewers commits before the fest, and pre-fest wishlists pass 2,000.
- **To KILL:** wishlists after the fest are under 3,000, or a well-funded chat-vs-streamer co-op title launches first and takes the niche.

#### IDEA-64: LigaHub reshaped: a points-only, cross-platform prediction and draft companion for simulcast creator events [user idea U5] — KILL (medium)

**Both versions are killed.**
- The **original** LigaHub is a white-label league platform for mid-tier streamers, with drafts, predictions, leaderboards and a transfer market "mirroring real money transactions". It is **KILL (high confidence)**: legally unworkable without a gambling licence, banned inside Twitch Extensions, demand-less, and duplicating free or incumbent fantasy apps.
- The **reshaped** version is a free-points web companion with predictions and a "draft your card" leaderboard across Twitch, YouTube, Kick and TikTok, paid for by brands or event producers at €500–1,500 per event. It is **KILL (medium confidence)**. It is legally feasible, and even feasible with prizes. But the anchor case has gone: the biggest Spanish simulcast creator event moves to an exclusive Netflix deal from 2027, the Kings League is frozen in Spain and already runs its own fantasy apps, native polls and predictions are free, and well-funded predecessors such as Noice found no visible traction.

**Validated definition of what was tested.** The reshaped companion described in the longlist (IDEA-64), and the original U5 as given [`00_user_supplied_ideas.md:52`].

**(a) Problem reality and rule status**
- **Ley 13/2011, primary text** [new: https://www.boe.es/buscar/act.php?id=BOE-A-2011-9280, last updated 31 Dec 2022, seen 23 Oct 2026]:
  - **Juego (art. 3.a):** any activity staking money or objects of economic value on uncertain outcomes, partly dependent on chance, where the stakes can be transferred between participants. Skill versus chance does not matter.
  - **Concurso (art. 3.e):** only a contest that requires payment (direct or premium-rate calls or messages). A programme with a prize but no payment "is not" a concurso.
  - **Leisure exclusion (art. 2.2.a):** games of pure leisure are excluded if they produce no transfers of economic value. A fee for the means to play is allowed only if it gives no economic benefit to the promoter.
  - **Promotional draws (art. 2.2.c):** random combinations for advertising or promotional purposes are excluded from licensing, but taxed. Art. 48 taxes state-wide promotional combinations at **10% of the market value of the prizes**.
  - **Without a licence (art. 9.2):** any activity in the law's scope run without a licence is prohibited.
  - **Sanctions:** unlicensed organisation is a very serious infringement (art. 39.a), fined **€1M–€50M** with possible closure of the online services (art. 42.3). Serious infringements carry €100k–€1M (art. 42.2).
- **What this means for the original.** A transfer market where users stake items of real-money value that they can transfer is "juego" and needs a DGOJ licence. Without one it falls in the €1M–€50M band. **Discard confirmed.**
- **What this means for the reshaped version.** It is outside the law if points are free, cannot be bought or transferred, and carry no prizes. With sponsor prizes, free entry rules out a "concurso". If prizes are allocated with an element of chance, the sponsor runs a promotional combination that needs published rules and pays 10% of the prize value. That is workable.
  - A free prediction contest offered by a media outlet is common practice: El País publishes bases invoking Ley 13/2011 for free promotional contests [new: https://ep00.epimg.net/descargables/2020/11/20/0a13e106b20703f9ad8cf62a981e62d5.pdf, 2020, via search 1].
  - No DGOJ guidance on prediction contests was found (search 1), so a gaming lawyer is still needed. The longlist's second kill criterion (no attractive prize-free design) is therefore **not triggered on legal grounds**.
- **Twitch rules** [new: https://dev.twitch.tv/docs/extensions/guidelines-and-policies/, seen 23 Oct 2026]:
  - 5.2: items may not be exchanged for money;
  - 6.2.3, 6.2.5, 6.2.6: no monetary-reward gambling, no sweepstakes or contest entries for Bits, no wagering;
  - 4.5: rewarding actions off Twitch must not be an extension's principal use case. This matters if the companion is built as an extension.
- **Demand anchor 1, La Velada.** La Velada VI peaked at about 8M on Twitch on preliminary platform data, below the edition-V record of about 9.1–9.33M. Its YouTube and TikTok simulcast was reported only as plays [new: https://www.que.es/2026/07/27/velada-ano-6-roza-audiencia-twitch/, 27 Jul 2026; search 13]. Vozpópuli independently reports an average of more than 6M for 2026 [new: Vozpópuli, below]. The about-8M peak is therefore still single-source (Que.es), but the second outlet's average is consistent with it. **On 19 Oct 2026, Netflix signed exclusive live rights to La Velada del Año for 2027, 2028 and 2029** [new: https://www.vozpopuli.com/deportes/la-velada-del-ano-se-emitira-en-netflix-ibai-llanos-sella-la-exclusividad-del-evento-para-tres-temporadas.html, 19 Oct 2026]. The flagship simulcast event will no longer run on the open platforms where a third-party companion could sit.
- **Demand anchor 2, the Kings League (C-28):**
  - its collective dismissal plan (ERE) covers **41 workers**, almost half the Barcelona staff. The denominators differ by source and scope: 83 according to the workers' lawyers (Col·lectiu Ronda), 125 according to La Vanguardia, and 230 worldwide according to the company (search 12);
  - **losses of €7.6M** in its last financial year, with €66M revenue projected;
  - the **Spanish competition is frozen until 2027**; France and Germany are suspended; it plans a more compact, Queens-League-style format and a European super-league;
  - its Twitch audience is down by almost 50% from early 2023 [new: https://www.que.es/2026/07/31/kings-league-despidos-nuevo-formato/, 31 Jul 2026; Ara, June 2026, via search 12].
  - On C-28's funding total (€110M against more than $160M), no new evidence was found; it stays open.
- **Platform reach of native interactivity** (all seen 23 Oct 2026):
  - Twitch Predictions and Polls are available to third-party apps through the API, but only on the authorising broadcaster's channel [new: https://dev.twitch.tv/docs/api/reference/];
  - YouTube lets apps insert polls [new: https://developers.google.com/youtube/v3/live/docs/liveChatMessages, updated 15 Oct 2026];
  - Kick has no polls or predictions, only chat, webhooks and, since Dec 2025, channel rewards [new: https://docs.kick.com/changelog.md];
  - TikTok has no public LIVE API [new: https://developers.tiktok.com/products/].
  - So the cross-platform gap is real but narrow, and TikTok can only be reached by QR code or link.

**(b) Competitors**
- **Native and free:** Twitch Predictions and Polls; YouTube polls.
- **Producers' own apps:**
  - *Kings League Fantasy*, built by Kosmos, MARCA and Champion Games, had 50,000 downloads in its first week [new: https://es.soccerway.com/noticias/fantasy-kings-league-arrasa-en-su-primera-semana-con-50-000-descargas/z9wv3iWH, date not shown, via search 19].
  - Kolex's official *Kings League Fantasy* app sells packs from $1.99 to $49.99, lets players trade cards and buy or sell them in an in-app marketplace, and is rated **18+ for "frequent simulated gambling" and loot boxes**: 4.6 stars from 130 ratings [new: https://apps.apple.com/app/id6467652295, seen 23 Oct 2026].
  - In effect, the incumbent already runs the user's "drafts and transfer market" idea, under its own licence and IP.
- **Fantasy football:** Biwenger, Comunio and LaLiga Fantasy, free with premium tiers [notes: GAM-20].
- **Prediction startups:**
  - **Noice** raised $27M in total ($21M round plus a $5M seed) for viewer predictions on livestreams, using virtual currency, paid card bundles and opt-in ads [new: https://gamesbeat.com/noice-reveals-prediction-based-gameplay-for-livestreams/, 21 Nov 2023, updated 18 Jun 2025]. Its current status is unverified, and no Spanish traction was found.
  - **Taunt Live**, an AI-generated live-prediction Chrome extension, has 28 users [new: https://chromewebstore.google.com/detail/dfgalfocgapcbcpfmccnngaccajmdeed, updated 20 Jan 2026].
  - **Simplebet Pick-N-Play** (sports) and **TGS with FansUnite** (esports predictions inside the Pepper tournament platform) are also active (search 14).
- **Tournament tools:** start.gg takes 6% of paid registrations; Toornament costs $5–15 and Battlefy $10 [notes: GAM-19].

**(c) Buyers and market size**
- Paying buyers would be the producers of a handful of Spanish creator events (TBS and Telefónica for La Velada, now Netflix; the Kings League; series such as Squid Craft Games and Tortillaland) and their sponsors. That is well under 100 paying entities a year (inference).
- La Velada's move to Netflix removes the largest of them from the open platforms.
- Mid-tier creators cannot pay. Twitch's Tier-1 subscription in Spain is **€4.99 since 11 Jul 2024**, which resolves C-28's €3.99/€4.99 item [new: https://www.3djuegos.com/industria-gaming/noticias/twitch-cambia-precios-suscripciones-tier-1-cuanto-costara-apoyar-a-tu-streamer-favorito-cuando-se-haran-efectivos-estos-cambios, 5 Jun 2024]. It is split 50/50, and 90% of streams average three or fewer viewers [notes: GAM-09].
- Ceiling at €500–1,500 per event: even 50 sponsored events a year is €25k–75k.

**(d) Willingness to pay.** Sponsors pay for reach. Sponsorship is about 90% of Kings League revenue [notes: GAM-14]. No evidence was found that they pay for engagement companions or unified metrics.

**(e) Distribution.** A relationship sale to fewer than ten producers. The two largest either build their own (the Kings League apps) or sell exclusivity to a closed platform (La Velada to Netflix).

**(f) Build and legal**
- The MVP takes 4–8 weeks: web app, Twitch, Kick and Google sign-in, overlay, chat bots.
- Legal needs: published rules and the 10% tax for any chance-based prize; age gating; no purchasable points.
- The original needs a DGOJ licence (arts. 10–11), so it cannot be built by a small team.

**(g) Defensibility.** None. Native tools are free, and the top producers build in-house or partner with media groups (MARCA).

**(h) Kill criteria**
- *Fewer than three producers or brands commit to paid pilots:* **open** [I], but the desk evidence points strongly toward a fail. The largest event goes exclusive to Netflix, the Kings League is paused in Spain and has its own apps, and no producer was found asking for this.
- *A gaming lawyer finds no prize-free design attractive to sponsors:* **not triggered legally**, because a free-entry promotional design (art. 2.2.c, with the 10% tax) is available. Sponsor appetite is the open question.
- *Platform terms restrict links out of the stream:* partly relevant through Twitch rule 4.5 for extensions; TikTok has no LIVE API.

**Scores, reshaped version (gaming adaptation as for IDEA-63, applied to a B2B2C platform: S2 = reachable paying producers, brands and creators)**
- S1 **1**: no producer demand found; the flagship event is leaving the open platforms.
- S2 **1**: fewer than 100 paying producers or sponsors a year.
- S3 **2**: sponsorship spend exists, but not on companions.
- S4 **2**: a handful of relationship sales.
- S5 **2**: native polls and predictions plus producers' own apps.
- S6 **4**: 4–8-week MVP.
- S7 **1**: none.
- S8 **2**: per event.
- **Sellability 1.88. P 1. Overall 1.53.**

**Scores, original version (for the record)**
- S1 **1**, S2 **2** (many mid-tier streamers, none able to pay), S3 **1**, S4 **2**, S5 **1** (free fantasy apps plus Kings League's own), S6 **1** (DGOJ licence needed), S7 **1**, S8 **3** (leagues recur).
- **Sellability 1.50. P 1. Overall 1.30. KILL (high).**

**The user's original claims and features (U5)**

| Claim or feature | Verdict | Evidence |
|---|---|---|
| The Kings League proves Spanish demand for streamer-led gamified sport | **Contradicted as proof of a market for a platform.** It shows superstar-scale, capital-heavy demand that is now retrenching | ERE for 41 workers, €7.6M loss, Spain frozen until 2027, audience down about 50% [new: Que.es, 31 Jul 2026]; €51M revenue but about 90% from sponsors [notes: GAM-14] |
| Rigid traditional esports are declining | **Partly supported** (Spain's national tier only; no new evidence) | [notes: GAM-12]. Creator formats are fading too (the Kings League above) |
| Draft systems for community-sourced players | **Saturated** | Biwenger, Comunio, LaLiga Fantasy [notes: GAM-20]; Kings League Fantasy (MARCA, 50k downloads in week 1) and Kolex's pack-and-trade app [new: above] |
| Viewer predictions and dynamic leaderboards | **Saturated natively; the cross-platform gap is narrow** | Twitch Predictions/Polls API, YouTube polls API; Kick has none, TikTok has no API; Noice ($27M raised) and Taunt Live (28 users) show weak traction |
| Transfer market "mirroring real money transactions" | **Prohibited without a licence; discard** | Ley 13/2011 arts. 3.a, 9.2, 39.a, with €1M–€50M fines (42.3); Twitch rules 5.2 and 6.2.x [new: BOE and Twitch, above] |
| Mid-tier streamers as buyers | **Unsupported; discard** | No evidence of demand [notes: GAM-17]; €4.99 subscription at a 50/50 split; 90% of streams have three or fewer viewers [notes: GAM-09] |
| Automated white-label league platform | **Weak** | Incumbents build in-house or with media partners [notes: GAM-16; new: Kings League apps above] |

**Open [I] checks**
- Interview five producers (TBS and Telefónica, the Kings League, Squid Craft Games, Tortillaland, ESLAND) and three brands.
- Get a gaming lawyer's opinion on a free-entry prize design (art. 2.2.c, art. 48 tax, possible regional rules).

**What would change the verdict.** Two or more producers of recurring creator events on the open platforms commit to paid pilots, or a brand agency wants Spanish-language cross-platform engagement reporting at scale. Even then, the better form would be a feature sold to an existing engagement company (for example Streamloots) rather than a new platform.

## 3. Cross-cutting findings (rule status and market facts that affect ideas outside batch 8)

**Rule status (batch 8 owns the minors' bill and the Twitch and Kick checks)**
1. **Minors' digital protection bill: lapsed.**
   - Congress initiative 121/000052 shows "Concluido – (Caducado)" from 06/10/2026. It was still at the committee-report (Informe) stage, with no plenary or Senate vote [new: congreso.es initiative page, seen 23 Oct 2026].
   - There is therefore no Spanish loot-box ban for minors, no default parental-control duty and no influencer age-verification duty. A new government would have to reintroduce the bill after the Cortes meet on 23 Dec 2026.
   - This affects any idea that assumed those duties: legal and compliance ideas for platforms, influencers and games.
2. **Ley 13/2011 (gambling) is unchanged since 31 Dec 2022.**
   - Free-entry contests with prizes are not "concursos" (art. 3.e).
   - Promotional prize draws are outside licensing but taxed at **10% of the prizes' market value** when state-wide (arts. 2.2.c and 48).
   - Unlicensed gambling is a very serious infringement fined €1M–€50M (arts. 39.a and 42.3).
   - This matters for any idea using prize draws, raffles or "spin the wheel" incentives (for example review-collection or loyalty mechanics in the retail and hospitality batches): promotional draws carry the 10% tax and need published rules, and paid entry turns them into regulated gambling.
3. **Twitch Extension rules (seen 23 Oct 2026).**
   - Bits may be used for votes (6.1.4) and to enhance free-to-play games (6.1.3).
   - Bits may not be used for monetary-reward gambling, random loot boxes, sweepstakes or contest entries, wagering, VOIP features, or access to pay-to-play games (6.2.1–6.2.8).
   - Items cannot be exchanged for money (5.2).
4. **Kick API status (23 Oct 2026).**
   - Chat, channels, livestreams, KICKs and moderation APIs, plus webhooks.
   - **Channel Rewards APIs since 3 Dec 2025**, and redemption accept/reject since 15 Jan 2026.
   - No polls or predictions endpoints, and no published rate limits.
   - "Developer Terms and Conditions" are referenced but not linked.
   - Kick's terms (modified 23 Mar 2026) ban scraping and harvesting account names.
   - This updates GAM-18, which said Kick had "no rewards endpoints".
5. **YouTube and TikTok.** YouTube's Live API lets an app insert polls (docs updated 15 Oct 2026). TikTok lists no public LIVE API.
6. **PEGI.** Unrestricted communication (no block or mute, no moderation) means PEGI 18. "Paid random items" mean PEGI 16 or 18 for submissions since June 2026. This affects any social or voice feature aimed at teenagers.

**ISP blocking (affects every SaaS idea in the research, not only IDEA-15)**

7. **Blocking from Spanish ISPs is a hosting risk for all the user's SaaS products.**
   - LaLiga and Telefónica blocks hit 554,507 domains in H1 2026, 90% of them on Cloudflare (OONI).
   - They still ran on most weekends through 18 Oct 2026: 3,507 IPs in total, peaks of 480 at once (hayahora.futbol data, my analysis).
   - Any product in this longlist served from Cloudflare (or Vercel, BunnyCDN or CloudFront) shared IPs can be unreachable for Spanish users during matches.
   - That matters most for deadline-critical tools: MASC timers (IDEA-01), the e-notification watchdog (IDEA-07), the complaint clocks (IDEA-20), DeCA roadside checks (IDEA-45), VeriFactu or invoicing tools.
   - **Mitigation for all builds:** avoid shared CDN IPs for Spanish traffic (dedicated IPs, a non-shared origin, or DNS failover during match windows), and monitor through hayahora.futbol's free DNS list.
   - The court authorisation (Juzgado Mercantil nº 6 de Barcelona) **expires on 20 June 2027** unless renewed. A separate Telefónica order (nº 9) covers other sports, films and series.
   - AES runs a free "#Laligagate" evidence form; no compensation case was found.

**Startups and public money (batch 2's IDEA-26 and IDEA-27, and the regional claims)**

8. **ENISA, 23 Oct 2026.**
   - Five lines: Startups y Pymes €25k–€1.5M, Innovación x Clima, Emprendedoras Digitales, AgroInnpulso, and Audiovisual e ICC (which covers video games).
   - Own funds must at least equal the loan; audited accounts above €300k.
   - 10,004 loans, 8,654 companies, €1,551M (ENISA homepage).
   - A free online eligibility test is advertised.
   - 2,527 certifications on ENISA's page, against 2,529 ever certified, 2,046 active and 483 lost by 11 Oct per Economía 3. ENISA's search of certified companies is **public**, a ready lead list for startup-facing products.
9. **Neotec 2026** closed on 14 May 2026 (€20,383,300; Plan Estatal 2024–2027). The 2027 call is expected in spring 2027 (inference).
10. **Video-game grants, 2026.**
    - National internationalisation call: €1M, up to €100k per project, **non-profits only** (BOE-B-2026-32589, 7 Oct 2026).
    - Madrid: €500k for 20 grants of up to €25k, for narrative games at prototype stage only.
    - No 2026 national "promoción" call found.
    - The longlist's "up to €80k national grant" is real for 2024 but **not confirmed for 2026–27**.
11. **Corporate tax R&D rules verified (BOE, updated 02/09/2026).**
    - Rates 25%, 42% on the excess over the two-year average, +17% for exclusive researchers, 8% on assets, 12% for innovation.
    - Cash refund at a 20% discount needs, **mandatorily**, an informe motivado or an AEAT advance valuation agreement. It also needs headcount maintained and an equal amount reinvested within 24 months, with clawback if broken.
    - The claimed "no discount up to €50k for startups" (Tetuan Valley) is not in the text.
    - This matters for any tax-tooling idea in batches 1 and 2.
12. **Angel deduction (LIRPF art. 68.1).**
    - €100k base (Venza's €250k is wrong); own funds of the company ≤ €400k; holding of 3–12 years; 40% stake cap (not for startup founders); certificate issued by the company.
    - It applies to any young SA or SL, not only certified startups.
    - Ley 28/2022 art. 4: ENISA's silence means approval (Legalitas is wrong).
    - This settles conflict C-26.
13. **Tool prices for other batches.**
    - Fandit (grant search SaaS): €56–70, €200–250 or €480–600 a month; sold to asesorías and through Repsol Solred.
    - Capboard (cap tables): €18 per stakeholder a year, with a €270 annual minimum.
    - UptimeRobot: $0–12 a month.
    - Useful anchors for IDEA-26 and IDEA-27 and any startup or equity tool.

**Creator economy and gaming**

14. **Conflict C-28 resolved.**
    - Twitch Tier-1 in Spain is **€4.99 since 11 Jul 2024**.
    - The Kings League's ERE covers **41 workers**, the denominator varying by scope (83 per the workers' lawyers, 125 per La Vanguardia, 230 worldwide per the company); losses of €7.6M; Spain frozen until 2027.
    - The funding total (€110M against more than $160M) stays open.
15. **Netflix has exclusive rights to La Velada del Año for 2027–2029** (Vozpópuli, 19 Oct 2026). The largest Spanish creator event leaves Twitch, YouTube and TikTok, which weakens any idea premised on creator mega-events as an open-platform channel.
16. **Spanish-speaking share of co-op game buyers (Steam review-language proxy, 23 Oct 2026).** Spanish-language reviews equal 5–22% of English reviews on seven comparable co-op games. Spain plus Latin America is a meaningful secondary market, not a primary one.

## 4. Search log

**WebSearch calls: 22 of a hard limit of 24.**

| # | Query | Idea | Outcome |
|---|---|---|---|
| 1 | DGOJ concurso de pronósticos gratuito con premios "combinación aleatoria" promocional Ley 13/2011 porra | 64 | No DGOJ guidance; example of free promotional contest bases (El País) |
| 2 | ley orgánica protección menores entornos digitales disolución Cortes octubre 2026 decae tramitación | 63 / cross | Pointed to Congress records; lapse then confirmed on congreso.es |
| 3 | bloqueos IP LaLiga Cloudflare septiembre octubre 2026 webs legítimas recurso indemnización | 15 | 2026–27 blocks; court order ends 2026–27; no compensation cases |
| 4 | streamers españoles R.E.P.O. PEAK Chained Together Ibai Rubius AuronPlay jugando récord espectadores Twitch | 63 | Nothing linking these creators to the co-op hits |
| 5 | Steam Next Fest 2026 median wishlists gained per game benchmark GameDiscoverCo Zukowski wishlists at launch | 63 | HTMAG, presskit.gg and Substack benchmarks |
| 6 | ayudas promoción sector del videojuego pódcast creación digital 2026 convocatoria Ministerio de Cultura cuantía máxima beneficiarios resolución | 63 / 62 | Found the 2026 internationalisation call; no 2026 promotion call |
| 7 | software gestión cap table España startups stock options phantom shares precio al mes Ley de Startups certificado inversores | 59 | Capboard; Carta and Pulley price notes |
| 8 | convocatoria Neotec 2026 CDTI plazo presupuesto millones resolución empresas | 60 | Neotec 2026 dates and budget |
| 9 | Fandit plataforma ayudas subvenciones startups precio suscripción alternativa buscador ENISA CDTI inteligencia artificial | 60 | Fandit profile; pricing then fetched |
| 10 | informe motivado vinculante I+D coste certificación entidad acreditada ENAC plazo meses honorarios consultora deducciones I+D porcentaje a éxito | 61 | IMV process; no fees found |
| 11 | monetización deducciones I+D+i abono Agencia Tributaria número de empresas millones de euros solicitudes informes motivados al año pymes | 61 | Regime confirmed; no statistics found |
| 12 | Kings League octubre 2026 vuelve España ERE despidos Superliga europea temporada | 64 | ERE of 41; Spain frozen until 2027 |
| 13 | La Velada del Año 6 audiencia pico espectadores Twitch YouTube TikTok simultáneo total 2026 récord | 64 | About 8M Twitch peak; **Netflix exclusivity 2027–29** |
| 14 | free-to-play predictions game for live streams viewers Twitch YouTube TikTok cross-platform leaderboard sponsors creator events platform startup | 64 | Noice, Taunt Live, Simplebet, TGS/FansUnite |
| 15 | Keymailer Terminals.io IMPRESS Lurkit pricing indie developer key distribution creators per month comparison 2026 | 62 | Keymailer prices (secondary source); Lurkit commission |
| 16 | "streamer vs chat" game Steam Twitch chat integration co-op party game 2025 2026 viewers vote chaos | 63 | Streamer vs. Chat, Chat is Cooked, Vs Chat Pack |
| 17 | salario medio desarrollador videojuegos España 2026 programador Unity Unreal junior senior bruto anual estudio indie | 63 | Aggregator salary ranges (weak) |
| 18 | Kick developer terms and conditions API rate limit requests per minute docs.kick.com public API 2026 | 63 / 62 | Nothing found |
| 19 | Kings League app oficial predicciones fantasy votación aficionados interactividad espectadores juego app | 64 | Kings League Fantasy (MARCA; Kolex) |
| 20 | número de estudios de videojuegos México Argentina Colombia Chile 2025 informe asociación industria desarrolladores Steam | 62 | IDB: about 1,800 studios in Latin America and the Caribbean |
| 21 | Tribunal Constitucional amparo Cloudflare RootedCON bloqueos LaLiga inadmite admite 2026 prórroga autorización 2027 | 15 | Appeals pending admission; no decision |
| 22 | precio tramitar certificado empresa emergente ENISA asesoría honorarios euros servicio startups certificación Ley de Startups | 59 | No fee data; certification is free |

**Per-idea use against the plan.** IDEA-63: 7 of 7. IDEA-64: 5 of 5. IDEA-62: 2 of 3. IDEA-15: 2 of 3. IDEA-59: 2 of 2. IDEA-60: 2 of 2. IDEA-61: 2 of 2.

**Steam catalogue lookups (not web searches).** I used Steam's own store-search API four times to get app IDs: `store.steampowered.com/api/storesearch/?term=` for Meccha Chameleon, Yapyap, BOMBANANA and Gamble with your friends. These are site-internal catalogue lookups, listed for transparency. No general search engine was queried through WebFetch, Bash or any proxy.

**Main pages fetched directly (all seen 23 Oct 2026 unless dated)**
- **Law and official pages:**
  - BOE Ley 13/2011: https://www.boe.es/buscar/act.php?id=BOE-A-2011-9280
  - BOE Ley 28/2022: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21739
  - BOE LIRPF art. 68.1: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
  - BOE Corporate Tax Law arts. 35 and 39: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
  - BOE-B-2026-32589 (7 Oct 2026): https://www.boe.es/boe/dias/2026/10/07/pdfs/BOE-B-2026-32589.pdf
  - BOCM Madrid video-game grant (19 Mar 2026): https://www.bocm.es/boletin/CM_Orden_BOCM/2026/03/19/BOCM-20260319-25.PDF
  - Congress initiative 121/000052: https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=121%2F000052
  - ENISA: https://www.enisa.es/ , https://www.enisa.es/servicios/certificacion/ , https://www.enisa.es/servicios/financiacion/ , https://www.enisa.es/sobre-enisa/consuta-datos-publicos/
  - Neotec 2026: https://www.ciencia.gob.es/Convocatorias/2026/NEOTEC2026.html
- **Platform documentation:**
  - Twitch: https://dev.twitch.tv/docs/extensions/guidelines-and-policies/ ; https://dev.twitch.tv/docs/api/reference/ (partly readable); https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/
  - Kick: https://docs.kick.com/ , /llms.txt , /changelog.md , /apis/channel-rewards.md , /apis/faqs.md , /getting-started/kick-apps-setup.md ; https://kick.com/terms-of-service
  - YouTube: https://developers.google.com/youtube/v3/live/docs/liveChatMessages ; TikTok: https://developers.tiktok.com/products/
  - Steamworks: https://partner.steamgames.com/doc/store/application/bundles ; https://partner.steamgames.com/doc/marketing/steamnextfest ; PEGI: https://pegi.info/what-do-the-labels-mean
- **Steam and game data:**
  - Steam appdetails price API (cc=es) and store pages: app IDs 3241660, 3527290, 1966720, 2567870, 4704690, 3834090, 4656000, 3892270, 4377330 and 5332420, with English, Spain-Spanish and Latin American Spanish review counts.
  - SteamSpy API (R.E.P.O., Chained Together; stale for 2026 apps); SullyGnome (R.E.P.O.); Wikipedia "Friendslop".
  - HowToMarketAGame Next Fest benchmarks.
- **ISP blocking:** que.es (17 Apr 2026); OONI report (30 Jun 2026); hayahora.futbol plus its data.json; Xataka Móvil (17 Aug 2026); Genbeta (10 Jun 2025); AES #Laligagate; Globalping probes API; Checkly locations; UptimeRobot pricing.
- **Startups:** Economía 3 (15 Oct 2026); Tetuan Valley (28 Jul 2026); Capboard pricing page plus its pricing JSON; Fandit pricing; ACCIÓ/ACIE 2014 IMV deck.
- **Gaming market:**
  - Que.es Kings League (31 Jul 2026); Vozpópuli Netflix and La Velada (19 Oct 2026); 3DJuegos Twitch price (5 Jun 2024).
  - App Store: Kings League Fantasy (Kolex). GamesBeat on Noice; Chrome Web Store on Taunt Live.
  - Keymailer, Lurkit (home and pricing), Woovit, Streamloots.
- **Failed or blocked fetches:** Ledgy pricing (404); Carta pricing (403); CDTI Neotec page (empty) and its PDF (redirect); TwitchTracker and Streams Charts (403); SullyGnome language filter (scripted); the Steam appreviews API (redirects to the homepage); Twitch developer agreement (scripted); Crowd Control pricing (404); Partnier pricing (403); bandaancha.eu (403); ecosistemastartup.com (403); dev.org.es (403); Kick developer terms (404).

**Checks left open (no budget or not findable)**
- The share of Spanish-language streams per game (a buyer-side proxy was used instead).
- Spain-level Steam unit data (none exists publicly).
- Kick's developer terms and rate limits.
- Twitch developer-agreement data clauses.
- Language filters in Keymailer and Lurkit.
- R&D-consultancy fee models, and AEAT monetisation statistics.
- Reasons for the 483 lost certifications.
- Whether the Constitutional Court admitted the Cloudflare and RootedCON appeals.
- Whether any compensation has been paid for collateral blocking.
- Noice's current status.
- The Kings League funding total (C-28).
