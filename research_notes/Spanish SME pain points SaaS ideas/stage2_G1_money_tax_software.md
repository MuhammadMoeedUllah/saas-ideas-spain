# Stage 2, group G1: money, tax and the SME software market

Noise filtering and candidate SaaS ideas. Prepared 23 October 2026.

- **Inputs (only these):** `tax_invoicing_accounting.md` (TAX-01 to TAX-25), `cashflow_finance_insolvency.md` (FIN-01 to FIN-26) and `voice_of_smes_software_market.md` (VOX-01 to VOX-21, plus its software price table).
- **No web research was done at this stage.** Anything that needs checking is listed as a validation question.
- **Conventions:** prices are € per month excluding IVA unless stated. The labels "single-source", "vendor survey" and "advocacy (ATA)" come from the Stage 1 notes. Where the notes conflict, the text says so.

---

## 1. Summary

- **Reviewed:** 72 pain entries (TAX 25, FIN 26, VOX 21).
- **Carried forward:** 42 entries (TAX 21, FIN 11, VOX 10), grouped into 12 clusters.
- **Filtered out:** 30 entries. By code: N1 ×7, N2 ×7, N3 ×1, N4 ×7, N5 ×1, N6 ×2, N7 ×5. The five N7 duplicates were merged into the cluster of the entry they duplicate, so their evidence is still used.
- **Strongest themes:**
  1. Structural late payment, and the mandatory MASC pre-litigation step that has made collections harder. About 90% of suppliers never claim statutory interest.
  2. The 2027–2029 compliance wave. VeriFactu is due in 2027 under the BOE text, but Hacienda has announced a move to October 2028 that is not yet law. B2B e-invoicing with payment-status reporting has fixed dates in the BOE.
  3. Automated enforcement aimed at manual micro-businesses: monthly card and Bizum data sent to the AEAT, notifications deemed delivered after 10 days, overnight bank embargos, and fixed fines of €100–600.
  4. Contributions based on real income, and the regularisation bills that follow, for about 3.48M autónomos.
  5. Gestorías are both the bottleneck and the gatekeeper for software choice.
  6. Unfair SaaS terms in a consolidating market: caps, silent renewals, lock-in at exit, and support only on premium tiers.
- **14 candidate ideas:** 2 of type A, 5 of type B, 7 of type C.
  - Most are easy to copy at the feature level.
  - Where an idea can be defended, the defence comes from legal know-how (MASC, AEAT and TGSS procedures), integrations with official systems or devices, and the gestoría channel.
  - Each idea says plainly whether it has a moat.
- **Main cross-cutting risk is regulatory timing:**
  - The VeriFactu postponement is not in the BOE.
  - The Cortes are dissolved until the new chambers meet on 23 December 2026.
  - Three decree-laws failed convalidation in 2026.

---

## 2. Pain clusters

### C1. Late payment, collections and the MASC step
- **Pain IDs:** FIN-01, FIN-02, FIN-03, FIN-05, FIN-06, FIN-07, FIN-08, TAX-20.

**Problem**

Spanish B2B suppliers, above all autónomos and micro firms selling to large companies, finance their customers.

*How late payment is*
- The legal maximum is 60 days. The private-sector average payment period (PMP) was 67 days in 2025 per PMcM, and 80.5 days in H2 2025 per Cepyme. Only 15% of large clients pay within the legal period, and 85% of large companies exceed it (FIN-01). Sources: [PMcM 2025 report](https://pmcm.es/wp-content/uploads/2026/04/Informe-Morosidad-2025_PMcM-VF.pdf), [PMcM, 22 Oct 2026](https://pmcm.es/pmcm-cinco-compromisos-contra-morosidad/).
- Only 41.51% of payments arrived on time in Q3 2026. On average, micro firms were paid 16.79 days late and hospitality 23.89 days late (FIN-05). Source: [Informa via Empresa Exterior](https://empresaexterior.com/el-retraso-en-los-pagos-se-enquista-por-encima-de-los-14-dias-y-lastra-al-tejido-empresarial-espanol/).
- Construction is the worst sector: a PMP of 96.5 days (Cepyme). Main contractors pay subcontractors in 87 days (FIN-02).

*What it costs*
- Cepyme puts the financial burden on pymes at €1,957M in 2025 ([Cepyme](https://cepyme.es/el-esfuerzo-financiero-de-las-pymes-como-consecuencia-de-la-morosidad-se-cifra-en-1-957-millones-de-euros/)).
- Informa puts the direct cost at about €3,100M. Unpaid invoices equal 3.3% of sales (FIN-01).

*Rights suppliers do not use*
- 89% never or almost never charge statutory interest, 94% never claim the €40 compensation per invoice, and 30% do not know the law exists (FIN-03).

*The MASC step and court friction*
- Since 3 April 2025, every civil claim needs a documented MASC attempt first. Valid channels include burofax, certified email or SMS, a notary or mediation; WhatsApp and ordinary email are not valid. The creditor waits up to a month, and a missing attempt is an incurable defect (FIN-06). Sources: [BOE LO 1/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-76), [Intercobros](https://www.grupointercobros.com/masc-y-reclamacion-de-deudas/).
- 179,846 monitorios (fast court payment-order claims) were filed in Q2 2026, 20.7% fewer than a year earlier and 31.3% fewer in Madrid. Madrid's court backlog still grew 10.4% (FIN-06, FIN-07). Sources: [Moncloa.com/CGPJ](https://www.moncloa.com/2026/10/16/cgpj-desahucios-lanzamientos-concursos-acreedores-3449594/), [Moncloa.com/TSJ Madrid](https://www.moncloa.com/2026/07/15/tsj-madrid-ley-eficiencia-descenso-asuntos-3399983).
- Collection services charge 5–25% of what they recover, or about €100 per file. That makes invoices of a few hundred euros uneconomic to chase (FIN-08).
- VAT stays payable on an unpaid invoice until the taxable base is formally modified, which has deadlines and needs a corrective invoice (TAX-20).

**Driver and status (October 2026)**
- Ley 3/2004 sets a 60-day cap and grants interest and €40 per invoice. It is in force but carries no sanctions.
- The 2020 sanctions bill died with the dissolution of the Cortes on 6 October 2026, and the EU Late Payment Regulation is blocked in the Council (FIN-01).
- LO 1/2025 (MASC) is in force. Most courts apply it to the monitorio; some authors disagree (FIN-06).
- E-invoice payment-status reporting (2027–2029) will create a national record of real payment dates (FIN-25).
- PMcM is lobbying the parties for automatic sanctions based on that data. That is a possible future tailwind, not a current one (FIN-01).

**What is used today, at what price**
- **Financing:** 71% turn to external finance first; 19% stretch their own payables. Options include credit lines and factoring or confirming (Novicap, priced on quote) (FIN-01).
- **Collection agencies:** Debitura from 6% or 7.5%; Absolut from 5%; RedClaimer €99.90 + IVA per file (it says others charge 10–25%); Recobrarte with a €1,500 minimum per debtor file; Intercobros on success fee only (FIN-08).
- **Lawyers and certified sending:** GW Abogados charges €110 for a first consultation. Certified-communication providers include BuroMail and BuroSMS; burofax prices were not verified (FIN-06).
- **Treasury tools:** Banktrack €59–119, Qonto forecasting €9–19, Agicap on quote (FIN-05).
- **Gap:** no evidence that invoicing tools automate interest or €40 claims (FIN-03).

### C2. Mandatory B2B e-invoicing and payment-status reporting
- **Pain IDs:** TAX-05, TAX-06, FIN-26. FIN-25 is merged here as a duplicate.

**Problem**
- **E-invoicing:** every business that invoices other Spanish businesses must issue, send and receive structured e-invoices in Facturae, UBL, CII or EDIFACT, through a private platform or the AEAT's free SPFE (Solución Pública de Facturación Electrónica). Anyone not issuing through the SPFE must send it a UBL "copia fiel" (true copy) of each invoice (TAX-05). Source: [BOE Orden HAC/1028/2026](https://www.boe.es/boe/dias/2026/10/05/pdfs/BOE-A-2026-20587.pdf).
- **Status reporting:** recipients must report a rejection, the due date and the date of full payment. Invoices count as accepted unless rejected. One vendor gives a reporting window of 4 calendar days ([B2Brouter](https://www.b2brouter.net/es/plazos-obligatoriedad-factura-electronica-b2b/), single-source).
  - This becomes a new, recurring accounts-payable task, run by owners or gestorías.
  - It makes late payers visible to the state (TAX-06).
- **Scale:** 557M B2B e-invoices were already exchanged in 2024, up 21% ([ElDerecho](https://elderecho.com/el-65-de-las-pymes-no-esta-preparada-para-la-entrada-en-vigor-de-verifactu)). There is no official count of affected firms (TAX-05).
- **Related rule already in force:** to receive a subsidy above €30k, a firm must prove it meets the Ley 3/2004 payment periods. Firms filing an abbreviated profit-and-loss account self-certify; the rest need an auditor (FIN-26). Source: [BOE LGS](https://www.boe.es/buscar/act.php?id=BOE-A-2003-20977).

**Driver and status (October 2026)**
- RD 238/2026 took effect on 20 April 2026 and Orden HAC/1028/2026 on 6 October 2026. Neither depends on Parliament. The dates are fixed:
  - **6 October 2027:** firms with turnover above €8M, including status reporting. They may attach a PDF for the first 12 months.
  - **6 October 2028:** everyone else. Legal entities at or below €8M also report statuses.
  - **6 October 2029:** personas físicas and entidades en atribución de rentas report statuses.
  - Source: [AEAT, 7 Oct 2026](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/octubre/7/solucion-publica-facturacion-electronica.html).
- **Conflict in the notes:** law-firm sources under FIN-25 say status reporting stays voluntary for everyone below €8M until 6 October 2029. The AEAT version (TAX-05 and TAX-06) says companies at or below €8M report from 2028. To validate.
- The sanctions figure of up to €10,000 is single-source.
- Private platforms must interconnect free of charge, and the SPFE must be live two months before 6 October 2027.

**What is used today, at what price**
- Experience with public-sector e-invoicing (FACe and Facturae).
- Invoicing SaaS with Facturae or UBL output: TS Facturas, Contasimple Profesional with FACe, Anfix.
- Networks such as B2Brouter (Basic €0 for 24 transactions a year, Professional €110 a year, Business €300 a year + IVA, [prices](https://www.b2brouter.net/es/precios/)) and Peppol.
- The free SPFE, once it is live.
- Status workflows are "not solved yet" (TAX-06). FIN-26 is handled by auditors and gestorías.

### C3. VeriFactu transition and regulatory limbo
- **Pain IDs:** TAX-01, TAX-02, TAX-03, TAX-04, TAX-14. VOX-12 is merged here.

**Problem**

*Scope*
- About 2.5M autónomos and 2.1M companies must use a compliant invoicing system (SIF) or invoice by hand. This is a single-source estimate (TAX-01; [AyE, 4 Mar 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/tributos-aclara-riesgos-autonomos-que-aun-facturen-excel-word-cuando-llegue-verifactu/20260303123152052310.html)).
- Tickets count as simplified invoices, so shop tills and weighing scales are in scope (TAX-01).

*Readiness and confusion*
- 35.4% of autónomos are prepared (ENA 2025, 878 responses). Xolo, a vendor, finds 7% fully compliant, and Quipu reports 65% of pymes not prepared.
- 41% confuse VeriFactu with e-invoicing (TeamSystem/Ipsos, 1,200 interviews) (TAX-01, TAX-04).
- Sources: [ENA 2025](https://www.infoautonomos.com/club-cursos/wp-content/uploads/sites/2/2025/11/ESTUDIO-NACIONAL-DEL-AUTONOMO-INFOAUTONOMOS-ENA-2025.pdf), [MuyPymes](https://www.muypymes.com/2026/10/20/pymes-autonomos-confunde-verifactu-factura-electronica).

*Costs*
- Compliant software costs €0–30 a month.
- Retail and hospitality also face hardware and integration costs. According to ATA (single-source), adapting a digital scale "can exceed €2,500" and a bar or restaurant cash register costs up to €1,800 (TAX-01; [AyE, 17 Sep 2026](https://www.autonomosyemprendedor.es/articulo/info-ata/autonomos-tendrian-que-adaptarse-verifactu-meses-ata-pide-que-sea-vez-que-factura-electronica/20260916172435055901.html)).

*Excel and Word*
- The DGT (Dirección General de Tributos) says invoicing in Excel or Word is "not automatically excluded" (V2045-25).
- Half of autónomos use no invoicing software (ENA), and 6 in 10 asesorías invoice with Excel (Cegid) (TAX-03).

*Early-adopter problems*
- Users report AEAT rejections and outages: a Holded user hit "Error 4124", and Quipu's bulk sending was down for most of January 2026 (VOX-12).

*Módulos*
- Users of módulos (the flat-rate tax regime) face the same "is it in force?" question every winter. Two decrees extending the regime's limits failed in Congress in 2026, and the 2027 limits are pending again (TAX-14).

**Driver and status (October 2026)**
- **The law as published:** RD 1007/2023, as amended by RDL 15/2025, requires compliance by 1 January 2027 for corporate-tax (IS) payers and 1 July 2027 for everyone else. Software producers have been obliged since 29 July 2025. Users of non-compliant systems face sanctions of up to €50,000 a year (art. 201 bis LGT) (TAX-01). Source: [BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840).
- **The announced postponement:** on 5 October 2026 Hacienda announced a move to October 2028, including the QR obligation. As of 21 October 2026 it is not in the BOE, and the AEAT FAQ still shows 2027 (TAX-02). Sources: [Hacienda note](https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf), [AEAT FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html).
- **Secondary sources conflict:** Infoautónomos gives October 2027 for firms above €8M, while the official note sets a single October 2028 date.
- **Convalidation risk is real:** RDL 16/2025, RDL 2/2026 and RDL 26/2026 all failed in 2026 (TAX-02), and the Cortes are dissolved.
- **Excluded:** SII users and Basque foral taxpayers, who use TicketBAI.

**What is used today, at what price**
- **Free:**
  - the AEAT app, which has no simplified invoices and no export (VOX table);
  - FacturaScripts;
  - Contasimple's free tier (12 documents a year).
- **Paid:**
  - TS Facturas €6.6–28;
  - Anfix €4.99–99.99;
  - Quipu €17–59;
  - Declarando VeriFactu Plus €9.90;
  - Cuéntica €9–29;
  - Holded from €7.50 on annual billing.
- **Tills and scales:** POS vendors and gestorías.
- **Information:** asesoría circulars and vendor content (TAX-04).

### C4. Unfair SaaS terms and lock-in in a consolidating market
- **Pain IDs:** TAX-07, VOX-08, VOX-09, VOX-10, VOX-11.

**Problem**

Autónomos and micro firms using invoicing, accounting, HR and autónomo platforms report five kinds of complaint:
- **Price rises and forced upgrades.**
  - Holded's Plus plan is capped at 250 invoices a year, corrective invoices included.
  - Monthly billing costs about twice the annual price.
  - Invoices "go straight to spam" unless the user buys "a plan twice the price".
  - Sources: VOX-08; [Softabase](https://softabase.com/es/guides/best-verifactu-invoicing-software); [Trustpilot Holded](https://es.trustpilot.com/review/holded.com?stars=1&stars=2).
- **Obstructed cancellation.** Cancellations are blocked, or renewals are charged after cancelling, at six or more vendors: Holded, Quipu, Factorial, Billin, Declarando and Legálitas (VOX-09).
- **Lock-in at exit.** Users lose access to their invoice history at exit, or are charged to see it (Quipu, Declarando, Holded), even though records must be kept for 4–6 years (VOX-10, TAX-07).
- **Support only on premium tiers.** Phone support is Premium-only at Holded and starts at €30 at Quipu. Elsewhere support means slow chat or chatbots (VOX-11).
- **Regulatory changes sold as upsells.** One review says new tax obligations are something "te las hace pagar" (TAX-07).

Share of one-star reviews: Holded 8%, Quipu 11%, Factorial 14% (VOX-09).

**Driver and status (October 2026)**
- **Ownership has consolidated:**
  - TeamSystem owns Quipu, Billin/TS Facturas and DELSOL.
  - Visma owns Holded, bought in 2021 for about €120M.
  - Wolters Kluwer owns a3, and Namirial owns Signaturit.
  - Contasimple's owner is disputed in the notes: "by Shine" in the tax notes, "Cegid Contasimple" in the VOX notes.
- **Two forced switching windows are coming:** VeriFactu (2027, or 2028 if the postponement is enacted) and e-invoicing (2027/2028) (TAX-07, inference).
- **Portability:**
  - On 16 September 2026 the CNMC (competition authority) flagged data-extraction costs and portability barriers in cloud services.
  - RD 238/2026 requires format conversion and interconnection, but not migration of program-specific data (TAX-07).
- **Weak recourse:** B2B buyers lack consumer-style cancellation protection (VOX-09, inference).
- **Gaps:** no list-price history is documented, and all reviews are unverified.

**What is used today, at what price**
- Switching to cheaper or free tools:
  - Billin from €6.60;
  - Contasimple €0–15.95;
  - FacturaDirecta €0–40;
  - FacturaScripts €0;
  - the AEAT app.
- Cuéntica is the counter-example: no minimum term ("Sin permanencia") and data export at any time.
- Manual exports before cancelling; chargebacks and disputed SEPA direct debits (VOX-09, VOX-10).

### C5. Advisers: dependence, errors and the asesoría productivity gap
- **Pain IDs:** TAX-22, TAX-23, VOX-21. VOX-13 is merged here.

**Problem**

*Who pays for advice, and what goes wrong*
- About 58% of autónomos are willing to outsource accounting and tax (ENA 2025: 57.9% and 57.2%).
- They pay €25–130/month to online asesorías, or an estimated €60–150/month to a traditional gestor (one guide's estimate) (TAX-22, VOX-19).
- Dissatisfaction is driven by quality, not price:
  - Declarando has 25% one-star reviews out of 4,023; TaxDown has 12% out of 9,914.
  - Complaints cite filing errors that lead to penalties, wrong registrations (altas) and missed notices that an instalment request (fraccionamiento) was refused (TAX-22; [Trustpilot Declarando](https://es.trustpilot.com/review/declarando.es), [Trustpilot TaxDown](https://es.trustpilot.com/review/taxdown.es)).
  - DIY platforms are reported to produce wrong annual VAT returns (modelo 390) and wrong calculations (VOX-13).

*The asesorías themselves (Cegid survey of 8,000 advisers)*
- 71% of asesorías have three or fewer staff, and 30% are sole practitioners.
- 63% run day-to-day management in Excel.
- Only 41% of individual advisers are up to date with the Crea y Crece and anti-fraud rules (TAX-23; [Merca2](https://www.merca2.es/2025/07/20/verifactu-asesorias-excel-2215495/)).

*The workload from each rule change*
- Every regulatory change means reviewing every client: the societario contribution bases in April 2026, then VeriFactu and e-invoicing in 2026–2028.
- 72% of asesorías have to re-educate their clients (TAX-23).

*The gestor chooses the software*
- Compatibility with the gestor "pesa más que la lista de funciones" (weighs more than the feature list), and a3 is "la opción obligada si tu asesor externo lo usa" (the obligatory option if your adviser uses it).
- Otherwise owners export their data and the gestor re-keys it (VOX-21; [GuiaDeSoftware](https://www.guiadesoftware.com/blog/software-contabilidad-pymes-espana)).

**Driver and status (October 2026)**
- Market forces plus the 2026–2028 regulatory wave; ongoing.
- The bookkeeping tools asesorías use are outside VeriFactu. Invoicing on a client's behalf is in scope (DGT V0817-26) (TAX-23).

**What is used today, at what price**
- **Professional suites:** a3 (Wolters Kluwer), TeamSystem/DELSOL and Sage. Their asesoría prices were not retrieved.
- **Add-ons and Excel:** Kabilio for invoice processing (it claims 85% time saved and integrates with a3; promotional claim), plus Excel (TAX-23).
- **Online asesorías** (TAX-22, VOX-19):
  - Infoautónomos from €24.95;
  - TaxDown €29.90 or €59.90;
  - Declarando €29.90–99.90;
  - Cuéntica €59 or €129;
  - Quipu's adviser from €80;
  - Billeo from €65.

### C6. Real-income contributions and regularisation shocks
- **Pain IDs:** TAX-12, TAX-13.

**Problem**

*The system for all autónomos*
- 3,483,645 people were registered in the RETA (the self-employed social-security regime) at the end of September 2026 ([AyE/ATA, 23 Oct 2026](https://www.autonomosyemprendedor.es/articulo/info-ata/septiembre-sumaron-mas-400-autonomos-dia-sigue-sangria-sectores-como-comercio/20261002153557056144.html)); the figure in February 2026 was 3,414,614 (TAX-12).
- Each must forecast their net income and pick one of 15 tramos (income bands), with a cuota of €205–€1,606 a month in 2026 ([Infoautónomos](https://www.infoautonomos.com/seguridad-social/cuota-de-autonomos-cuanto-se-paga/)).
- They can change their contribution base up to six times a year through Import@ss, and the difference is settled later by regularisation (TAX-12).

*How the regularisation went (ENA 2025)*
- 35.1% had to pay and 10.4% got a refund.
- The handling was rated 2.2/10, and 50.3% cite lack of transparency.
- 15% do not know their own tramo (TAX-12; [ENA 2025](https://www.infoautonomos.com/club-cursos/wp-content/uploads/sites/2/2025/11/ESTUDIO-NACIONAL-DEL-AUTONOMO-INFOAUTONOMOS-ENA-2025.pdf)).

*Societarios and family collaborators (about 1.2M)*
- Their minimum base rose from €1,000 to €1,424 in 2026: about 42% more, roughly €135 a month or over €1,600 a year. 500,000–600,000 people notice the impact.
- The TGSS (Social Security treasury) does not update bases automatically, so many face a lump-sum back-charge in 2027–2028.
- Graduados sociales (labour and social-security advisers) worked "a contrarreloj" (against the clock) in April 2026.
- Sources: TAX-13; [AyE, 13 May 2026](https://www.autonomosyemprendedor.es/articulo/info-ata/seguridad-social-empuja-miles-autonomos-cambiar-cuotas-futuras-regularizaciones/20260512112256053643.html); [AyE, 13 Apr 2026](https://www.autonomosyemprendedor.es/articulo/info-ata/ata-pide-gobierno-que-rectifique-paralice-subida-cuotas-directa-mas-medio-millon-autonomos/20260413121353053066.html). The figures come from ATA (advocacy).

**Driver and status (October 2026)**
- The real-income system created by RDL 13/2022 is in force.
- The 2026 tables are frozen at 2025 levels (Orden PJC/297/2026, single-source).
- The MEI (intergenerational equity surcharge) rises to 1% in 2027.
- The 2027 bases are undecided, and the negotiating table has not met "for more than a year".
- A Junts proposición de ley (bill) to stop the societario increase was pending in May 2026; its outcome is unverified. The brief notes that pending bills lapse with the dissolution of the Cortes. To validate.
- RD 643/2026 has eased Social Security deferrals since 1 August 2026.

**What is used today, at what price**
- Gestorías and graduados sociales, within their fees.
- Vendor calculators, such as Cuéntica's autónomo-fee calculator in its €19 plan.
- Manual base changes in Import@ss (TAX-12, TAX-13).

### C7. Official notifications, tax debts and fixed penalties
- **Pain IDs:** TAX-10, TAX-18, TAX-19, VOX-17. FIN-24 is merged here.

**Problem**

*Notifications*
- An electronic notification counts as delivered after 10 days unopened, "even if the email alert never arrived".
- After two failed postal attempts, notice goes out by BOE edict, with 15 days to appear.
- Owners often discover the problem when an account is embargoed (TAX-18; [AyE, 15 Oct 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/autonomos-pueden-acabar-cuenta-embargada-hacienda-domicilio-fiscal-dia/20261015000100056315.html)).

*Embargos*
- Under an AEAT resolution of 4 June 2026, banks must execute embargo orders overnight. An order sent before 20:00 freezes funds before 08:00, and one order can reach up to 10 accounts. Roll-out runs through November 2026; this is single-source (TAX-19; [AyE, 22 Aug 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-podra-embargar-cuentas-bancarias-autonomos-menos-24-horas-partir-septiembre/20260821085621055511.html)).

*Fixed fines and surcharges* (TAX-10; [BOE LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186); [AyE, 23 Oct 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/agencia-tributaria-sancionando-autonomos-rectificar-renta-recuperar-impuestos/20261022170642056497.html))

| Slip | Cost |
|---|---|
| Late return with no tax lost | €200 (€400 for census returns) |
| Correcting the Renta after the campaign | €100 per tax year |
| Change of fiscal address not reported | €400 |
| Ignoring a requerimiento (formal request) | €250–€600 |
| Late filing | 1% plus 1% per month |
| Enforcement-period surcharges | 5–20% |

*Misuse of identity in public procedures*
- "Miles" (thousands) of autónomos may appear as Kit Digital beneficiaries of aid filed with their digital signature without their consent. An investigation is open in Las Palmas (VOX-17; [Vozpópuli](https://www.vozpopuli.com/espana/canarias/el-supremo-zanja-la-disputa-y-las-palmas-asumira-la-investigacion-del-fraude-masivo-del-kit-digital.html), [Merca2](https://www.merca2.es/2026/06/14/fraude-kit-digital-supremo-las-palmas-2397192/)).

*Knock-on cash crunches*
- Deferrals and seized refunds follow (FIN-24, merged; headline-level sources only).

**Driver and status (October 2026)**
- In force: LGT arts. 27, 28, 198 and 203, plus the notification rules (Ley 39/2015).
- In force: the 24-hour embargo resolution (single-source) and RD 643/2026.
- TEAC resolution RG 00/51764/2026 opened a route to challenge embargoed refunds (TAX-19).
- There is no frequency data for letters, fines or embargos.

**What is used today, at what price**
- Gestorías checking official mailboxes on clients' behalf, within their fees.
- Personal vigilance, gestoría calendars and vendor reminders.
- Lawyers or Legálitas once things have gone wrong (TAX-10, TAX-18).
- Checking Acelera Pyme or the sede electrónica by hand (VOX-17).

### C8. Filing load, data cross-checks and AEAT letters
- **Pain IDs:** TAX-09, TAX-15, TAX-16, TAX-17.

**Problem**

*The filing load*
- Autónomos and small firms file four quarterly rounds and a set of annual returns:

  | Frequency | Returns (modelo numbers) |
  |---|---|
  | Quarterly | 303 (VAT), 130/131 (IRPF instalments), 111 and 115 (withholding), 349 (intra-EU sales) |
  | Annual | 390, 190, 180, 347 and the Renta |

- ATA estimates 226 hours and €3,390 a year of bureaucracy per autónomo (advocacy figure, method undisclosed).
- TeamSystem/Ipsos reports 21.5 hours a month spent on manual invoicing tasks.
- Sources: TAX-09; [AyE, 11 Aug 2026](https://www.autonomosyemprendedor.es/articulo/info-ata/ata-denuncia-que-autonomos-pierden-mas-3000-euros-costes-tramites-burocraticos/20260810150741055355.html); [MuyPymes](https://www.muypymes.com/2026/10/20/pymes-autonomos-confunde-verifactu-factura-electronica).

*Card and Bizum data matching*
- Since 1 January 2026, banks report every business card and Bizum collection to the AEAT each month (modelo 170, no minimum).
- Mismatches with the VAT return (modelo 303) trigger letters. The common causes are:
  - refunds that fall in a different quarter;
  - tips;
  - personal Bizum payments into a business number;
  - collections on behalf of third parties;
  - exempt services.
- Ignoring the resulting requerimiento costs €250–€600 (TAX-15; [AyE, 18 Aug 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-enviando-cartas-autonomos-descuadres-bizum-cinco-errores-habituales/20260817095927055443.html), single press source).
- Most exposed: hospitality, dental and vet clinics, hairdressers, retail and taxis (TAX-15).

*Post-Renta letters*
- From September the AEAT sends "miles de cartas" (thousands of letters). They flag client-reported income, retenciones (withholding), unproven expenses and sector-ratio outliers, and the AEAT has four years to review (TAX-16; [AyE, 20 Aug 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-volvera-enviar-miles-cartas-autonomos-partir-septiembre-errores-renta/20260819154220055494.html)).

*Deductible expenses*
- Hacienda's own Consejo para la Defensa del Contribuyente calls the rules "excesivamente restrictivas". Home-office costs are limited to 30% of the floor-area share; vehicle, phone and meals are often disputed.
- 24% of autónomos want legal certainty on deductions (TAX-17; [AyE, 20 Oct 2026](https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-admite-que-autonomos-tienen-demasiadas-trabas-deducir-coche-movil-comidas-suministros/20261019135900056391.html)).

**Driver and status (October 2026)**
- LIVA, LIRPF and LGT, in force.
- Monthly modelo 170 under RD 253/2025 and Orden HAC/747/2025, as reported by the press.
- The Consejo's proposals have not been adopted.
- 42.4% of autónomos want only one or two filings a year, but no reform is pending (TAX-09).

**What is used today, at what price**
- Gestorías and online asesorías at €25–100 a month.
- Software that prepares the returns: Anfix Avanzado from €14.99, Cuéntica Fiscalidad €29.
- Declarando's "recomendador de deducibles" (Pro plan, €69.90 with filings).
- Receipt scanning: TaxDown 30–100 scans a month, Quipu 30–350.
- Owners or gestorías reconcile card and Bizum data by hand (TAX-09, TAX-15, TAX-17).

### C9. Late detection of company distress, and SL formal duties
- **Pain IDs:** FIN-16, FIN-17, TAX-21.

**Problem**

*Micro firms file too late*
- The Ley 16/2022 micro-enterprise insolvency procedure handled 1,427 cases in 2025, 22.5% of company procedures. Only 52 of them aimed at keeping the business going, and the 970 liquidations concluded took a median of 169.5 days (FIN-16; [Registradores, Anuario Concursal 2025](https://www.registradores.org/documents/d/guest/anuario-concursal-2025)).
- In Q4 2025, 61.7% of insolvent companies were eight years old or younger. SLs make up 93.2% of company insolvencies (FIN-16, FIN-17; [Registradores Q4 2025](https://www.registradores.org/documents/d/guest/np-epc-4t-2025b)).

*Directors' personal liability*
- Supreme Court ruling STS 1477/2026 is reported by a single press source.
- The trigger: losses push net equity below half of share capital. Directors who do not convene the shareholders within two months can be personally liable for debts that arise in that period.
- Not knowing about a specific debt does not restart the clock (FIN-17; [AyE, 23 Oct 2026](https://www.autonomosyemprendedor.es/articulo/pymes/supremo-confirma-que-autonomos-societarios-pueden-asumir-deudas-sl-actuan-tiempo/20261022150439056494.html)).

*Annual accounts*
- SLs must deposit their annual accounts within a month of approval.
- Failing to do so blocks the company's registry filings and risks fines from the ICAC (the accounting regulator) of €1,200–€60,000, or up to €300,000 a year for turnover above €6M. The fine is halved if the accounts are filed before proceedings start (TAX-21; [BOE LSC](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544)).

**Driver and status (October 2026)**
- In force: the Ley de Sociedades de Capital (LSC), the insolvency code (TRLC, reformed by Ley 16/2022, in force since 1 January 2023) and STS 1477/2026.
- Unknown: the number of SLs, and how often directors face liability claims.

**What is used today, at what price**
- Gestorías and accountants, "when they notice"; lawyers.
- The Justice Ministry's online forms for the micro procedure.
- Accounting services at €59.95–€129/month; software with corporate-tax returns from €58.33/month (Anfix Empresarial) (FIN-16, FIN-17, TAX-21).

### C10. Payment and invoice fraud
- **Pain IDs:** FIN-12. VOX-03 is merged here.

**Problem**

*What happens*
- The main attacks are fake supplier IBAN changes, CEO or business-email-compromise (BEC) fraud, phishing for bank credentials, and hijacked email sessions.
- Autónomos and the admin staff of small firms are hit hardest (FIN-12, VOX-03).

*How big it is*

| Measure (2025 unless stated) | Value | Source |
|---|---|---|
| INCIBE incidents, all victim types | 122,223 (+26%) | [INCIBE](https://www.incibe.es/incibe/sala-de-prensa/incibe-detecto-mas-de-122000-incidentes-de-ciberseguridad-en-2025) |
| Online-fraud cases | 45,445 (+19%), of which 25,133 phishing | INCIBE |
| Queries to the 017 cybersecurity helpline | 142,767 (+44.9%) | INCIBE |
| SMEs hit by invoice or payment fraud in 12 months | 22% | Kaspersky vendor survey, undisclosed sample ([AyE, 10 Sep 2026](https://www.autonomosyemprendedor.es/articulo/todo-digital/ocho-cada-diez-pymes-espanolas-han-sufrido-ciberataque-muchos-descuidos-empleados/20260909151304055801.html)) |
| Loss per CEO/BEC incident | more than €15,000, recovery "very low" | Secondary source ([euribor.com.es](https://www.euribor.com.es/2026/07/21/los-10-tipos-de-estafa-mas-denunciados-en-espana-en-2025/?amp=1)) |

- INCIBE does not split its figures between companies and citizens (FIN-12).

*Getting money back*
- Fraud is now the Banco de España's main complaint focus.
- Only about a third of complaints are admitted, and refunds across all complaints totalled €6.8M in 2025 (FIN-12; [BdE](https://www.bde.es/f/webbe/Secciones/Publicaciones/PublicacionesAnuales/MemoriaServicioReclamaciones/25/MSR2025_Resumen.pdf)).

**Driver and status (October 2026)**
- Criminal activity, and rising.
- Verification of Payee (VoP) is a bank check that the payee's name matches the IBAN.
  - Regulation (EU) 2024/886 requires it, from 9 October 2025 according to the researcher's background knowledge.
  - The notes did not verify this.
  - If it is in force, it may already blunt fraud that relies on a name–IBAN mismatch. That is the main validation risk.
- PSD3/PSR not verified.

**What is used today, at what price**
- The free INCIBE 017 helpline.
- Banks' strong customer authentication and fraud alerts.
- IT providers.
- Cyber insurance (not priced).
- Kit Digital's subsidised cybersecurity category, now closed (FIN-12, VOX-03).

### C11. Post-subsidy and B2B contract traps
- **Pain IDs:** VOX-16, VOX-05. VOX-09 also feeds the idea built on this cluster.

**Problem**

*Kit Digital leftovers*
- Kit Digital, a public digitalisation voucher, made more than 860,000 grants before closing in October 2025 ([España Digital](https://espanadigital.gob.es/lineas-de-actuacion/programa-kit-digital)). Its vouchers covered 12 months of services.
- Once the subsidised year ends (most had ended by October 2026, an inference), beneficiaries keep paying monthly for little-used services, sometimes with early-exit fees (VOX-16).
- Price points:
  - Arsys's Kit website pack costs "desde 21,98€/mes" after the first year ([Arsys snippet](https://www.arsys.es/kit-digital)).
  - One forum poster cites €66/month of upkeep, against about €8/month for hosting and about €10/year for a domain ([Forocoches](https://forocoches.com/foro//showthread.php?p=495521024)).
  - An established vendor was accused of selling "el mismo servicio a un precio inflado" (the same service at an inflated price) when the voucher paid.

*Telecom contracts*
- Business phone lines fall outside consumer protection. A company can only go to court over a disputed bill or a permanencia (minimum-term) penalty.
- An autónomo qualifies for the consumer routes only if the line is not used professionally (VOX-05; [Infoautónomos](https://www.infoautonomos.com/blog/internet/como-reclamar-un-servicio-de-telefonia-o-internet-siendo-autonomo)).

*Forgotten renewals*
- Annual renewals that owners forget, such as Quipu Premium at €588/year, are a recurring source of anger (VOX-09).

**Driver and status (October 2026)**
- Kit Digital closed to applications in October 2025. Justification, payments and audits are still running, and only about 25% of the budget had been paid by February 2026 (Tribunal de Cuentas, via the press).
- The rule defining who counts as a consumer (art. 3 TRLGDCU) was unchanged as of February 2025 (VOX-05).
- No data on renewal or cancellation rates, and no data on willingness to pay.

**What is used today, at what price**
- Cancelling and moving to cheap hosting or a site builder; freelancers who rebuild sites (one offered €20 plus hosting); lawyers for exit charges (VOX-16).
- For telecom, an in-house complaint, then the ministry's non-binding route (VOX-05).
- Legal subscriptions such as Legálitas at €16.92–45.50/month, though at least one plan excludes business matters (VOX-05).

### C12. Online reputation attacks
- **Pain IDs:** VOX-01, VOX-02.

**Problem**

*Review attacks and extortion*
- Restaurants, bars and local services depend on their Google Maps and Tripadvisor ratings.
- They face review bombing and extortion: "O me pagas tanto o te escribiré comentarios negativos" ("pay me this much or I'll write negative comments").
- Reported cases (VOX-01; [Merca2](https://www.merca2.es/2026/04/28/resenas-bar-google-2373862/); [Ara](https://es.ara.cat/opinion/extorsion-restaurantes_129_5218159.html)):
  - one bar saw about 20 suspicious profiles post one-star reviews in under an hour;
  - a "pack de odio" (hate pack) against a competitor reportedly costs "apenas 200 euros";
  - every restaurant an Ara columnist spoke with had received such offers.
- A law firm quoted by Xataka says Google's reporting tool "rara vez funciona" (rarely works) (VOX-01).

*Pressure to collect reviews*
- Owners also feel pushed to accumulate reviews.
- Fake five-star reviews sell for €1.5–2.5 each, or in €200/month packages.
- Buying them is illegal and risks account suspension and fines of up to €100,000 (VOX-02).

**Driver and status (October 2026)**
- Fake reviews have been illegal since May 2022 under the EU Omnibus rules (per Merca2 and Puro Marketing).
- The practice was still being reported in April 2026.
- No Spain-specific enforcement or scale data.
- Court awards of up to €20,000 are reported but not verified.

**What is used today, at what price**
- Google's free reporting and review-management tools.
- Police cybercrime units; lawyers, using unfair-competition law or the right to honour; certified screenshots as evidence.
- Reputation agencies such as OnbrandinG (prices not captured).
- Manual QR cards to ask for legitimate reviews (VOX-01, VOX-02).

---

## 3. Noise log

These 30 pains were filtered out. The codes mean:

| Code | Meaning | Count |
|---|---|---|
| N1 | Weak evidence | 7 |
| N2 | Not software-solvable | 7 |
| N3 | Regulation postponed, a draft, or likely to lapse | 1 |
| N4 | Already solved cheaply, or saturated | 7 |
| N5 | Too niche or too small | 1 |
| N6 | Legally risky to automate | 2 |
| N7 | Duplicate of another pain; its evidence was merged into that pain's cluster | 5 |

| Pain ID | Title | Code | Justification |
|---|---|---|---|
| TAX-08 | Basque TicketBAI/Batuz: real-time reporting, adaptation costs, technical churn | N4 | The roll-out is complete: Bizkaia's last phase started on 1 Jan 2026. Free official apps (FakturaBAI, FakturAraba, Haz tu factura) and certified vendors exist, and the notes found no evidence of ongoing small-business distress. The leftover multi-regime need is a feature question for G1-I04 and G1-I05. |
| TAX-11 | No small-business VAT franchise | N2 | A policy decision: Spain has not transposed the EU scheme. All the evidence traces back to ATA. Software can only reduce the filing effort, which C8 already covers. |
| TAX-24 | 10% VAT on renovations depends on payment method (from 1 Dec 2026) | N3 | RDL 29/2026 still needs convalidation while the Cortes are dissolved, and its sister decree RDL 26/2026 already failed. The details come from a single press source, and trades are a niche. Passed to the construction track. |
| TAX-25 | Underserved regimes (Canarias IGIC, foral territories, Ceuta/Melilla, módulos) | N1 | The only evidence is one provider's exclusion list (TaxDown) plus facts about the regimes. There is no data on demand, prices or business counts, and these are also small regional markets (N5). |
| FIN-04 | Public-sector late payment in specific regions and cities | N2 | Software cannot make administrations approve invoices faster. Official payment periods are within the limit nationally (regions 27.05 days), which conflicts with the 70-day survey figure. The pain is local: Balears 53.42 days, Palma 51.69, Las Palmas 48.40. |
| FIN-09 | Checking a customer's solvency is fragmented and paid | N1 | Medium-low confidence, with no scale or price data. The registries are controlled by credit bureaus, so this works better as an integration. Scoring payers from the user's own ledger stays as a feature of G1-I02. |
| FIN-10 | Working capital squeezed; short-term finance dearer | N2 | The cost of credit is set by banks and interest rates, which is a macro problem. Its software-solvable root is late collection (FIN-01, FIN-05, in C1). Factoring prices could not be evidenced. |
| FIN-11 | Public guarantee and credit schemes fragmented, routed via banks | N1 | The notes call the evidence of pain weak. Only 3% of Spanish firms report financing obstacles (ECB SAFE survey, Q2 2026). |
| FIN-13 | Card and POS acceptance costs, juggling payment methods | N4 | Commoditised: SumUp 0–1.49%, Qonto 0.8–1.2%, Stripe Terminal 1.4% + €0.10. Cards are already accepted in 94% of small shops. |
| FIN-14 | Bank fees and disputes with banks | N1 | Low confidence. The evidence is mostly about consumers (Banco de España complaints, Asufin's consumer fee data). Switching to a free account or a neobank solves much of it. |
| FIN-15 | Autónomo insolvency and Segunda Oportunidad complexity | N6 | A court process run by specialist lawyers, and discharging public debt is legally contested. Automating the documents would be a tool for law firms, which belongs to the legal track. |
| FIN-18 | Young, tiny firms fail early; autónomos quit for economic reasons | N2 | Structural: weak demand, thin margins, fixed costs. 90% of those leaving the RETA do so for economic reasons. There is no specific software lever beyond generic cash-runway tools. |
| FIN-19 | DANA 2024 recovery: slow business claims, fragmented aid | N5 | Only a residual tail is left: 691 business claims (3%) were pending in June 2026, and 99.7% of all claims were processed by October 2026. Regional and shrinking. |
| FIN-20 | Catastrophes keep recurring in 2026, each with a claims burden | N2 | These are physical events. Payouts depend on policy cover and on loss adjusters, and no complaints are documented. The only software help would be a checklist, which the CCS (the state's catastrophe insurer) already publishes. |
| FIN-21 | Underinsurance and missing business-interruption cover | N1 | Medium-low confidence and no SME statistic. The ratios of about 60% uninsured and about 20% lost-profit claims are the researcher's own calculations. Cover is sold by insurers and brokers. |
| FIN-22 | April 2025 blackout losses left uncompensated | N2 | A one-off grid failure, with the €1.6bn estimate from a single aggregator source. The notes say there is "mostly no" software angle. |
| FIN-23 | Cash forecasting and one view of all bank accounts | N4 | Already sold at SME prices: Banktrack €59–119, Qonto forecasting €9–19, Agicap. Its distinctive part, predicting payment dates, is folded into G1-I02 through FIN-05. |
| FIN-24 | Cash crunches from tax and Social Security debts | N7 | Duplicate of TAX-19: the same deferral and seizure mechanism, from headline-level sources. Merged into C7. |
| FIN-25 | Mandatory B2B e-invoicing with payment-status reporting | N7 | Duplicate of TAX-05 and TAX-06. Merged into C2, where its law-firm dates are flagged as conflicting with the AEAT's. |
| VOX-03 | Phishing, vishing, CEO/BEC fraud aimed at small businesses | N7 | Duplicate of FIN-12. Its evidence (BEC losses above €15,000 per incident, secondary source) is merged into C10. |
| VOX-04 | Breaches at SaaS vendors put notification duties on SME customers | N1 | The official trend is strong (AEPD breach notifications up 163% in Jan–Aug 2026), but there is no SME cost data and no owner voice. The root cause sits with the vendors, and GDPR duties belong to the legal track. |
| VOX-06 | Energy mis-selling by phone; exit penalties | N1 | The data is old (CNMC 2017–2019), plus one 2023 complaint where the complainant's business status is unclear. |
| VOX-07 | Banking and card-acceptance costs; funds held by payment fintechs | N4 | The fee data covers consumer accounts. Free accounts and cheap card acceptance exist, and this is a banking product rather than software. Overlaps FIN-13 and FIN-14. |
| VOX-12 | VeriFactu forces new software amid deadline confusion and rejected invoices | N7 | Duplicate of TAX-01 and TAX-02. Its user reports (Holded error 4124, Quipu's January outage) are merged into C3 and C4. |
| VOX-13 | Errors in automated tax filings by low-cost platforms | N7 | Duplicate of TAX-22 (errors by advisers and platforms). Merged into C5. |
| VOX-14 | HR and time-tracking software minimums for micro-employers | N4 | Cheap per-employee options exist: Holded's HR add-on at €1.50 per employee, Kenjo at €6–10. The status of the time-recording obligation is the labour track's question. |
| VOX-15 | Low-quality Kit Digital deliverables, harassment, pressure to sign | N4 | The programme closed to new applications in October 2025, and fixing a bad site is cheap: hosting about €8/month, rebuilds offered from €20. The part still live is VOX-16, which is kept. |
| VOX-18 | Agentes digitalizadores (registered Kit Digital suppliers) unpaid for months | N2 | An administrative payment process in a closed programme. Software could only help with paperwork. |
| VOX-19 | Gestoría cost and partial substitution by online platforms | N4 | Online asesorías already charge €24.95–€59.90 a month (+IVA). The notes say the remaining dissatisfaction is about accuracy, not price, and that is kept as TAX-22. |
| VOX-20 | Legal-advice subscriptions: coverage disputes, cancellation friction | N6 | Legal advice is a regulated profession, so AI triage would need lawyers behind it. Evidence is medium-low (few reviews). |

---

## 4. Candidate SaaS ideas

The ideas are numbered by cluster, not ranked; ranking happens after validation. All price hypotheses are this stage's own assumptions to be tested. They are not facts from the notes.

### G1-I01: MASC-ready claim kit for unpaid B2B invoices
- **Type:** B (primary), secondary A.
  - B: a new product for a mandatory step that nobody packages end to end.
  - A: cheaper than agency success fees or per-file legal fees.
- **Buyer:** autónomos and micro and small B2B firms with unpaid invoices of a few hundred to a few thousand euros. A secondary buyer is gestorías and small law firms acting for them.
  - More than 2.9M pymes and autónomos (Cámara de Comercio, cited by AyE; FIN-01).
  - 179,846 monitorios were filed in Q2 2026 alone, and each now needs a prior MASC attempt (FIN-06).
  - How many creditors attempt MASC each year: unknown, to validate.
- **Pains addressed:** FIN-06, FIN-07, FIN-08, FIN-03, FIN-01, FIN-02, TAX-20.
- **Problem:**
  - Since April 2025, a creditor must prove a valid MASC attempt before filing a monitorio: a real offer, sent through a certified channel, followed by up to a month's wait. A missing or invalid attempt is incurable and the claim is rejected (FIN-06).
  - Agencies charge 5–25% of what they recover, or about €100 per file, so small invoices get written off (FIN-08).
  - Statutory interest and the €40 per invoice are almost never claimed (FIN-03).
- **Product:**
  - *What it does,* claim by claim:
    1. Import the unpaid invoices, by upload or from the user's invoicing tool.
    2. Calculate principal, statutory interest and €40 per invoice.
    3. Generate a MASC-compliant offer, for example a confidential binding offer with a settlement option such as "interest waived if paid within 10 days".
    4. Send it through a certified-channel partner (certified email or SMS, or burofax).
    5. Track the one-month waiting clock and the one-year validity of a failed attempt, and log the debtor's reply.
    6. Output an evidence pack and a pre-filled monitorio file.
    7. Above €2,000, where the notes say a lawyer and procurador (court representative) are required (FIN-07), hand the file to partner lawyers at a fixed fee.
    8. Optionally, send a VAT-recovery reminder and a draft corrective invoice when the debtor is insolvent (TAX-20).
  - *MVP in weeks:*
    - two or three offer templates reviewed by a litigation lawyer;
    - one certified-email API;
    - an interest calculator and a deadline tracker;
    - the PDF evidence pack;
    - monitorio form pre-fill.
  - *It does not:*
    - advise on disputed debts;
    - represent anyone in court;
    - buy debts or report debtors to registries;
    - use channels that are not valid for MASC (WhatsApp, ordinary email).
- **Why now:**
  - LO 1/2025 has been in force since 3 April 2025, and the courts mostly apply MASC to the monitorio (Audiencia Provincial de Málaga, 6 June 2025) (FIN-06).
  - Monitorios fell 20.7% in Q2 2026 while Madrid's backlog grew 10.4%. That suggests creditors are holding back while the criteria settle, which is demand for a safe, cheap path (FIN-06, FIN-07).
  - No late-payment sanctions can arrive before 2027: the Cortes are dissolved and the EU regulation is blocked (FIN-01). Self-help is the only lever.
- **Alternatives today** (FIN-06, FIN-08):
  - RedClaimer: flat €99.90 + IVA per file; it says other agencies charge 10–25%.
  - Absolut from 5%; Debitura from 6% (EU debtors) or 7.5%.
  - Recobrarte: €1,500 minimum per debtor file.
  - Intercobros: success fee only.
  - GW Abogados: €110 for a first consultation.
  - BuroMail, BuroSMS and burofax: prices not verified.
  - *Weaknesses:* priced for larger claims; success rates are vendor claims only (30–40%, 60–70%, 77%); no self-serve flow tied to the creditor's own invoices.
- **Price hypothesis:**
  - €19–39 per claim, including one certified send (pass-through cost to be validated), or €9–15/month for a bundle of claims.
  - Lawyer hand-off at a fixed fee shared with partner firms.
  - No success fee.
- **Channels:**
  - A "send to MASC" button in invoicing tools (Holded, Quipu, TS Facturas, Anfix, Contasimple), through their integrations or marketplaces.
  - Gestorías, white-labelled for their clients.
  - Associations: PMcM, Cepyme, ATA, construction trade federations.
  - Searches: "MASC reclamación factura", "burofax MASC", "monitorio requisito MASC", "reclamar factura impagada autónomo".
  - Colegios de abogados and procuradores, to build the hand-off network.
- **Build notes:**
  - A certified-communication partner is essential.
  - Templates must be reviewed by litigation lawyers and updated as the Audiencias Provinciales rule.
  - GDPR applies to debtor data.
  - No registry reporting and no debt purchase.
  - Complexity: medium. The legal content is harder than the code.
- **Moat in an AI-flooded market:** moderate.
  - What protects it:
    - legal know-how, meaning templates and evidence packs that courts accept, maintained case by case;
    - certified-channel partnerships;
    - a lawyer and procurador hand-off network;
    - later, triggers fed by e-invoice payment statuses (2027–2029).
  - The interface itself is copyable, and agencies or invoicing vendors could bolt it on.
- **Key risks and kill criteria:**
  - *Risks:*
    - a reform or a higher-court ruling changes MASC for monitorios;
    - flat-fee agencies undercut it (RedClaimer at €99.90 is already close);
    - fear of upsetting customers suppresses use (89% never claim interest);
    - certified-send costs make claims under about €300 uneconomic.
  - *Kill if:*
    - fewer than about 1 in 4 interviewed creditors with unpaid B2B invoices would pay €20 or more per claim;
    - or a valid certified send costs more than about €15;
    - or a free official MASC channel appears.
- **Evidence strength:** strong.
  - The obligation is in the BOE and in force, the volumes are official (CGPJ), and several vendors give price points.
  - Weak points: the effect size and success rates are unproven.
- **Validation questions:**
  1. Confirm in the BOE text of LO 1/2025 the valid MASC methods, the one-month rule (art. 17) and the interruption of limitation (art. 7). Check current Audiencia Provincial and Supreme Court positions on MASC before a monitorio (see the vLex, ETL Ilia and Duplo sources in FIN-06).
  2. Confirm that monitorios of €2,000 or less can be filed and enforced by the creditor without a lawyer and procurador, and exactly what changes above €2,000.
  3. Price the valid channels per send: burofax with acknowledgment of receipt, BuroMail/BuroSMS, and qualified certified email.
  4. Look up RedClaimer, Intercobros, Debitura, Absolut and Recobrarte self-serve offers, and search for any existing "MASC" SaaS. Check whether Holded, Quipu or Anfix already offer dunning or MASC flows.
  5. Find CGPJ or Ministry of Justice data on MASC outcomes (agreement rates) and on monitorio duration; both are gaps in FIN-06 and FIN-07.
  6. Interview 15–20 autónomos and micro firms with unpaid B2B invoices about typical invoice size, the amount below which they write debts off, and their willingness to pay per claim.

### G1-I02: Receivables autopilot (reminders, statutory interest and payment-date forecasts)
- **Type:** C (primary), secondary B.
  - C: a subscription that is set up once and runs on its own.
  - B: no invoicing tool is documented as automating interest and €40 claims (FIN-03).
- **Buyer:** B2B autónomos and micro and small firms that invoice on credit: services, wholesale, industry and construction subcontractors. The user is the owner or the one admin person.
  - More than 2.9M pymes and autónomos (FIN-01).
  - How many of them invoice B2B on credit: unknown, to validate.
- **Pains addressed:** FIN-05, FIN-03, FIN-01, FIN-02, TAX-20. It escalates to G1-I01.
- **Problem:**
  - Fewer than half of invoices are paid on time (41.51% in Q3 2026), so cash planning is guesswork (FIN-05).
  - About 9 in 10 suppliers never claim the statutory interest or €40 that Ley 3/2004 grants them (FIN-03).
  - VAT on unpaid invoices can only be recovered through a formal modification of the taxable base, within deadlines (TAX-20).
- **Product:**
  - *What it does:*
    - Reads issued invoices from the invoicing tool, or from PDFs and email, and matches collections from the bank feed.
    - Sends polite reminders on a schedule by email or WhatsApp, escalating over time.
    - Shows the accrued statutory interest and €40 per invoice and offers them as an optional settlement lever ("pay by Friday and we waive the interest"). The H2 2026 interest rate of 10.40% comes from a single source.
    - Learns each customer's real payment delay and forecasts collection dates in a 13-week cash view.
    - Flags customer contracts with terms beyond the 60-day legal cap.
    - Alerts VAT base-modification deadlines for insolvent debtors.
    - Escalates to G1-I01 in one click.
  - *MVP:* CSV import plus one or two invoicing-tool integrations, a bank feed through a licensed aggregator, the reminder engine, the interest calculator and per-customer delay statistics.
  - *It does not:* lend money, do factoring (it could refer), or make phone calls.
- **Why now:**
  - No sanctions regime or EU cap is coming before 2027 (FIN-01).
  - The e-invoice payment-status data due in 2027–2029 will make real payment dates available, and the product can be built ready to use it (FIN-05, TAX-06).
  - Carrying late customers costs more as finance gets dearer (FIN-10).
- **Alternatives today:**
  - Banktrack €59–119; Qonto forecasting €9–19, but only for Qonto account holders; Agicap on quote (FIN-23).
  - Collection agencies at 5–25% (FIN-08); factoring such as Novicap, on quote (FIN-10).
  - Reminder features in invoicing tools are not documented in the notes.
  - *Weaknesses:* none of these is documented as automating interest and €40 claims, predicting payment dates per customer, or linking to the MASC step.
- **Price hypothesis:**
  - €5–9/month, with paid escalation through G1-I01.
  - Gestoría bulk plans at about €2 per client.
- **Channels:**
  - Invoicing-software marketplaces.
  - Gestorías.
  - Business-account providers such as Qonto, as partners (speculative).
  - PMcM and Cepyme late-payment campaigns.
  - Searches: "calcular intereses de demora factura", "reclamar 40 euros ley morosidad", "recordatorio de pago factura".
- **Build notes:**
  - A licensed bank-account aggregation partner, the invoicing APIs and the WhatsApp Business API.
  - The statutory rate table must be updated each half-year from the BOE.
  - GDPR applies.
  - Complexity: medium.
- **Moat in an AI-flooded market:** low to medium.
  - Invoicing vendors and banks can copy the features.
  - What protects it is the breadth of integrations, the payment-behaviour data it accumulates, and the MASC escalation path.
  - Plainly: mostly speed and distribution.
- **Key risks and kill criteria:**
  - *Risks:*
    - invoicing vendors bundle reminders for free;
    - the behavioural barrier (fear for the customer relationship) keeps the interest features unused;
    - sharing payer scores across users may be legally constrained.
  - *Kill if:*
    - fewer than half of trial users keep reminders switched on after 60 days;
    - or the main invoicing tools already ship reminders plus statutory interest on their entry tiers.
- **Evidence strength:**
  - Strong for the problem: PMcM, Cepyme and Informa agree.
  - Medium for whether users will act on interest and €40 (FIN-03 rates willingness as medium).
- **Validation questions:**
  1. Check which of Holded, Quipu, TS Facturas, Anfix, Contasimple, FacturaDirecta and Cuéntica already send automatic payment reminders or calculate late-payment interest, and on which tier.
  2. Verify the BOE resolution setting the H2 2026 statutory interest rate (10.40% is single-source, via Novicap) and the €40 rule in arts. 7–8 of Ley 3/2004. The consolidated text returned a 404 in Stage 1.
  3. Look up Banktrack, Agicap, Embat and Qonto for per-customer payment-date prediction features.
  4. Price licensed bank-aggregation providers in Spain, and confirm whether a partner licence suffices.
  5. Survey B2B autónomos on whether they would switch on automatic interest notices if framed as "waived if paid by a date".
  6. Legal check: can anonymised payer-behaviour scores be shared across customers under GDPR and the rules on credit information?

### G1-I03: E-invoice inbox and payment-status reporter for small firms
- **Type:** B
- **Buyer:** micro and small companies that receive supplier invoices, usually with the owner or a gestoría handling accounts payable. Asesorías are a second buyer, filing in bulk for their clients.
  - Small firms must receive structured e-invoices from 6 October 2028.
  - The AEAT says companies at or below €8M must report invoice statuses from 2028. Law-firm sources say 2029 (a conflict, see C2).
  - Suppliers of firms above €8M will feel pressure from 6 October 2027.
  - There is no official count of B2B invoicers (TAX-05); this needs validating. As a baseline, 557M B2B e-invoices were exchanged in 2024.
- **Pains addressed:** TAX-06, TAX-05, FIN-26. FIN-25 is merged as a duplicate.
- **Problem:**
  - Accounts payable becomes regulated, deadline-bound reporting. The recipient must reject an invoice within the window or it counts as accepted, and must report its due date and the date of full payment (TAX-06).
  - One vendor gives the window as 4 calendar days (single-source).
  - Nobody serves micro firms here yet. The free SPFE handles the exchange of invoices, but not the matching of bank payments to invoices (TAX-05, inference).
- **Product:**
  - *What it does:*
    - An inbox connected to the SPFE and to private platforms that reads all four formats.
    - Approve or reject in one tap on mobile.
    - Extracts the due date and reports the payment date automatically, by matching the bank feed to invoices.
    - A queue that warns before reporting deadlines.
    - A bulk mode for asesorías.
    - A "my payment period" report that doubles as the art. 13.3 bis LGS self-certificate for subsidies above €30k (FIN-26).
  - *MVP:*
    - parse UBL and Facturae;
    - receive through one partner platform or access point, then connect to the SPFE when its interface is published;
    - bank-feed matching;
    - the reporting queue and mobile approval.
  - *Does not:* issue invoices (it pairs with any issuer, including G1-I05), act as an ERP, or become a registered exchange platform at launch (whether that is needed must be validated).
- **Why now:**
  - Orden HAC/1028/2026 has been in force since 6 October 2026.
  - The dates (6 October 2027, 2028 and 2029) are fixed in the BOE and do not depend on Parliament.
  - The SPFE must be live two months before 6 October 2027.
  - Customers above €8M will push their suppliers from 2027 (TAX-05).
- **Alternatives today:**
  - The SPFE: free.
  - B2Brouter: €0 for 24 transactions a year, then €110 or €300 a year + IVA.
  - Invoicing SaaS with Facturae or UBL output: TS Facturas, Contasimple Profesional, Anfix.
  - ERPs, which are "only starting to build status workflows" (TAX-06).
  - *Weakness:* these focus on exchanging invoices. Status reporting and payment matching are unsolved.
  - *Constraint:* the free SPFE sets a price floor of zero for basic sending and receiving.
- **Price hypothesis:**
  - €5–12/month per company, tiered by invoice volume.
  - Asesoría bulk plan at €1–3 per client per month.
- **Channels:**
  - Asesorías: the notes name bulk reporting by asesorías as a use case (TAX-06).
  - Invoicing vendors that have no receiving or accounts-payable module, as partners.
  - Searches: "recibir factura electrónica pyme", "estado de pago factura electrónica", "Solución Pública de Facturación Electrónica".
  - Trade associations.
- **Build notes:**
  - RD 238/2026 requirements (free interconnection, the copia fiel).
  - Multi-format conversion.
  - Bank feeds through a licensed aggregator.
  - Retention of 4 years for tax and 6 years under the Código de Comercio.
  - Very sensitive data: every supplier invoice the firm receives.
  - Complexity: high.
- **Moat in an AI-flooded market:** medium.
  - The hard parts are format and platform interoperability, accurate bank matching, the asesoría channel, and accumulated payment-date data, which also feeds G1-I02.
  - Incumbents (TeamSystem, Visma/Holded, Wolters Kluwer) will add status features, and the free SPFE caps the price.
- **Key risks and kill criteria:**
  - *Risks:* the SPFE ships a good free interface; incumbents bundle the feature; obligations for small firms slip, or reporting stays voluntary until 2029.
  - *Kill if:* the SPFE's own app covers receiving, status reporting and bank matching for free; or third-party software gets no programmatic access to the SPFE.
- **Evidence strength:**
  - Strong on the regulation (BOE).
  - Weak on cost and willingness to pay: there is no compliance-cost estimate (TAX-05 and TAX-06 rate cost confidence low).
- **Validation questions:**
  1. Read Orden HAC/1028/2026 (BOE-A-2026-20587) and RD 238/2026 and establish:
     - which statuses are mandatory;
     - the actual reporting deadline (is it 4 calendar days?);
     - who reports what in 2028 versus 2029, to resolve the TAX-05 versus FIN-25 conflict.
  2. Check whether the SPFE will offer an interface for third-party software, and when its technical specifications are due.
  3. Does a receive-and-report tool have to register as a private exchange platform under RD 238/2026? What does registration involve?
  4. Check the status-reporting roadmaps of B2Brouter, TS Facturas, Holded, Quipu, Anfix, a3 and Sage. List the Spanish Peppol access points.
  5. Confirm the sanctions for not reporting statuses; the €10,000 figure is single-source.
  6. Estimate how many firms have turnover above €8M and how many suppliers they have (a TAX-05 gap).
  7. Confirm the art. 13.3 bis LGS details: when self-certification applies, and the 10-working-day deadline.

### G1-I04: VeriFactu retrofit adapter for legacy tills and scales
- **Type:** B
- **Buyer:** shop and bar owners (autónomos and micro firms) whose existing tills or scales issue tickets, in three groups:
  - small retailers with digital weighing scales, such as fruterías and carnicerías;
  - bars and restaurants with older POS terminals or cash registers;
  - personal services with cash registers.

  POS and scale installers and distributors are the channel. The number of such businesses is not in the G1 notes and needs validating with the retail and hospitality tracks. For context, VeriFactu applies to about 2.5M autónomos and 2.1M companies (single-source estimate).
- **Pains addressed:** TAX-01, TAX-02, TAX-03 (partly).
- **Problem:**
  - Tickets are simplified invoices, so tills and scales count as invoicing systems under VeriFactu.
  - ATA (single-source) says adapting a digital scale can cost more than €2,500, and a bar cash register up to €1,800.
  - Setups that integrate POS and ordering need more than a software update (TAX-01).
  - In the Basque roll-out of TicketBAI, these segments were phased in last and needed exemptions (TAX-08 context).
- **Product:**
  - *What it does:* a small bridge, either a capture device on the printer line or a driver, plus a cloud SIF (invoicing-system) layer.
    - It receives each ticket the legacy device issues.
    - It generates the VeriFactu record: hash chaining, event log, and a QR code printed on the existing printer.
    - It submits the record to the AEAT in VERI*FACTU mode.
    - A dashboard serves the owner and the gestoría.
  - *MVP:* support the most common scale and POS models in one city, working with one installer partner.
  - *Does not:* replace the POS, manage inventory, or support TicketBAI at launch.
- **Why now:**
  - The BOE still sets 1 January and 1 July 2027.
  - The announced move to October 2028 is not yet in the BOE (TAX-02). It would give time to build, but it also weakens urgency.
- **Alternatives today:**
  - Replacing hardware, at €1,800–€2,500+ per device type (ATA).
  - Upgrades from the POS vendor.
  - The AEAT's free app, which cannot issue simplified invoices (VOX table), so it does not cover tickets.
  - Handwritten tickets, which fall outside VeriFactu.
  - POS SaaS such as SumUp TPV Plus at €49/month.
  - *Weakness:* every option costs capex or a full system switch. The notes document no retrofit option.
- **Price hypothesis:**
  - €150–300 one-off for the device and installation.
  - €5–8/month for the service.
- **Channels:**
  - POS and scale distributors and installers, who know the installed base.
  - ATA and retail and hospitality federations.
  - Gestorías serving módulos shops and bars.
  - Any regional adaptation incentive, as in the Basque precedent of 30–60% deductions. None was found in common territory, so this needs validating.
- **Build notes:**
  - The maker becomes a producer of an invoicing system. It must file a declaración responsable (self-declaration of compliance) and faces sanctions of up to €150,000 per year and per system type (TAX-01).
  - The DGT's position on bridges or middleware is unknown.
  - Drivers are needed model by model, plus hardware logistics.
  - Complexity: high.
- **Moat in an AI-flooded market:** high, if it is legal and works.
  - The protection is device integrations, producer liability and an installer network.
  - Hardware and field work cannot be cloned by software alone.
- **Key risks and kill criteria:**
  - *Risks:*
    - a bridge may not satisfy the integrity and inalterability requirements if the legacy device can still print tickets outside the chain;
    - POS vendors may cut their upgrade prices;
    - the postponement to 2028 reduces urgency;
    - the base of device models is fragmented.
  - *Kill if:* DGT or AEAT criteria rule out capturing tickets externally; or typical vendor upgrade quotes come in below about €300.
- **Evidence strength:** medium.
  - The hardware costs are advocacy figures from a single source (ATA).
  - That tickets and tills are in scope is well sourced (LRB Tax via AyE).
  - The Basque precedent supports how hard this segment is.
- **Validation questions:**
  1. Search the DGT binding rulings (consultas) and the AEAT VeriFactu FAQ for criteria on middleware that makes legacy cash registers or scales compliant.
  2. Identify the leading scale and POS brands in Spain and get VeriFactu upgrade quotes, to test ATA's €1,800–€2,500 figures.
  3. Check whether Basque TicketBAI-era products retrofitted legacy cash registers, and how they were certified.
  4. Count retail businesses using scales, and hospitality businesses, by city (cross-check with the retail and hospitality tracks).
  5. Track the October 2028 postponement: which instrument (RD or RDL) and when it is published.
  6. Confirm producer obligations under Orden HAC/1177/2024 (the declaración responsable and technical specifications) and the producer sanction regime.

### G1-I05: Fair-terms invoicing and e-invoicing for micro businesses
- **Type:** A.
- **Buyer:** autónomos and micro firms that invoice (professionals, trades, small B2B services). Two groups: those still on Excel or Word, and those unhappy with an incumbent tool.
  - There were 3.48M RETA members at the end of September 2026. About half of autónomos use no invoicing software (ENA; TAX-03).
  - Incumbent user bases are vendor claims: Holded more than 80,000, Quipu more than 20,000, Billin more than 180,000 users.
- **Pains addressed:** VOX-08, VOX-09, VOX-10, VOX-11, TAX-07, TAX-03, TAX-01. VOX-12 is merged in.
- **Problem:**
  - Cheap invoicing already exists. The complaints are about terms, not list price (C4):
    - invoice caps and yearly price rises;
    - forced upgrades;
    - cancellation that is obstructed;
    - losing invoice history at exit;
    - phone support only on paid tiers;
    - VeriFactu bugs.
  - Mandatory e-invoicing in 2027–2028 will be a second upsell moment (TAX-07).
- **Product:**
  - *What it does:*
    - VeriFactu, Facturae and UBL B2B e-invoicing, and the SPFE copy, all included at one flat price.
    - Unlimited invoices, sent from the user's own email domain.
    - One-click cancellation.
    - After cancelling, a free read-only archive for 6 years (UBL/Facturae plus PDF/A), with full export.
    - An importer for Excel and Word templates that keeps the numbering series.
    - A free seat for the gestor, with exports to a3, Contasol and Sage.
    - Spanish-speaking human support on WhatsApp in business hours, with AI triage first.
  - *MVP:* a compliant invoicing core, the importer, the archive and WhatsApp support.
  - *It does not do:* accounting, payroll, POS, inventory or tax filing.
- **Why now:**
  - The BOE still sets VeriFactu for 2027. Even if it moves to October 2028, owners face a switching window (TAX-02).
  - E-invoicing in 2027–2028 forces another upgrade (TAX-05).
  - Consolidation and complaints keep rising (C4).
  - Why would customers switch? Only when an incumbent's next price rise, tier change or e-invoicing upsell bites, and only if their gestor accepts the tool. The importer and the archive lower the cost of switching.
- **Alternatives today** (prices from TAX-01, the VOX table and C3):
  - Free:
    - the AEAT app (no simplified invoices, no export);
    - FacturaScripts (open source);
    - Contasimple's free tier (12 documents a year).
  - Paid:
    - Contasimple €10.95–19.95;
    - TS Facturas/Billin €6.60–28 (the notes contain two conflicting price lists);
    - Holded €7.50–99.50 on annual billing, about double that monthly (sources conflict);
    - Quipu €17–59;
    - Anfix €4.99–99.99 (another source says "from €15");
    - FacturaDirecta €0–40;
    - Declarando VeriFactu Plus €9.90;
    - Cuéntica €9;
    - a3factura from €9.95;
    - SumUp Facturas Plus €10.
  - Weaknesses: caps, support behind paid tiers, lock-in at exit. But many are cheap, and Cuéntica already sells "sin permanencia" (no minimum term) with export at any time.
- **Price hypothesis:**
  - €6/month, or €60/year, flat.
  - Archive-only plan at €1/month, or free.
- **Channels:**
  - Gestorías: a free gestor seat and bulk onboarding of clients who invoice in Excel (6 in 10 asesorías invoice with Excel themselves; TAX-03).
  - Searches: "alternativa a Holded", "programa facturas Verifactu exportar".
  - Comparison and review pages where incumbents collect complaints.
  - Associations.
- **Build notes:**
  - As a producer of an invoicing system, it must file a declaración responsable (self-declaration of compliance) and faces producer sanctions of up to €150,000.
  - It needs AEAT VERI*FACTU submission and Facturae/UBL output with the SPFE copy.
  - It must be able to serve Basque customers through TicketBAI (TAX-08 was filtered as a standalone pain).
  - Retention: 4 years for tax, 6 years under the Código de Comercio.
  - Human support is the main cost driver.
  - Complexity: medium.
- **Moat in an AI-flooded market:**
  - None; speed only. Every feature is a product decision any incumbent can copy, and Cuéntica already offers some of them.
  - The only edge is distribution through gestorías.
- **Key risks and kill criteria:**
  - Risks:
    - a saturated market, with €0–10 plans and the state's free app;
    - human support at €6/month destroys the margin;
    - gestores are locked into a3 and TeamSystem;
    - incumbents could add free archives.
  - Kill if:
    - acquiring a customer through gestorías costs more than 12 months of revenue;
    - or fewer than about 1 in 5 users who complained about Holded or Quipu say they would switch for these terms.
- **Evidence strength:** medium.
  - Reviews are unverified but consistent across at least six vendors.
  - Saturation is also well evidenced, and that cuts against the idea.
- **Validation questions:**
  1. Verify current list prices and caps:
     - Holded (the 250-invoice Plus cap; the three conflicting price sources);
     - TS Facturas/Billin (two conflicting lists);
     - Contasimple, Anfix (€4.99 versus "from €15"), FacturaDirecta, Cuéntica, Declarando VeriFactu Plus.
  2. Read the AEAT free app's guide for its limits on volume, simplified invoices and export. The PDF was not read in Stage 1.
  3. Resolve Contasimple's ownership (Shine versus Cegid).
  4. Check which vendors already offer a free archive after cancellation, or one-click cancellation.
  5. Confirm the record-keeping periods and whether the copies the SPFE holds satisfy them.
  6. Interview 10 gestorías: would they accept or promote a new tool if it exports to their a3 or Contasol?
  7. Benchmark the cost per user of human WhatsApp support.

### G1-I06: Asesoría compliance cockpit
- **Type:** B.
- **Buyer:** small asesorías and gestorías with 1–9 staff and 25–200 clients each, plus graduados sociales (labour and social-security advisers).
  - The total number in Spain is unknown and must be validated.
  - Cegid surveyed 8,000 advisers: 71% of firms have three or fewer staff and 30% are sole practitioners. Sole advisers often serve up to 25 clients; firms of 4–9 staff serve 101–200 (TAX-23).
- **Pains addressed:** TAX-23, TAX-22, VOX-21, TAX-02, TAX-04, TAX-14, TAX-13, TAX-09. VOX-13 is merged in.
- **Problem:**
  - Every regulatory change forces a client-by-client review in Excel. Recent and coming examples:
    - societario contribution bases in April 2026;
    - each client's VeriFactu tool and submission mode;
    - the e-invoicing date by turnover band;
    - módulos limits every winter.
  - Asesorías are the default educators: 72% have to re-educate their clients (TAX-23, TAX-04).
  - Errors and missed notices turn into client penalties (TAX-22).
- **Product:**
  - *What it does:*
    - Imports the client list from a3, Contasol or Sage exports, or from CSV.
    - Tags each client by regime: estimación directa or módulos, IS or IRPF, B2B or B2C, turnover band, and territory (common, foral, Canarias).
    - Generates an obligations calendar and a monthly "at-risk clients" list, covering:
      - VeriFactu tool and mode;
      - e-invoicing date and readiness;
      - societario base check (€1,424) and regularisation exposure;
      - módulos limits;
      - filings due.
    - Includes a curated "rule status" feed showing what is in the BOE versus what is only announced (for example, VeriFactu 2027 versus 2028; the convalidation status of decree-laws).
    - Sends plain-language circulars to clients in bulk by email or WhatsApp, with questionnaire links to collect missing data.
  - *MVP:* CSV import, a rules engine for five obligations, bulk messaging, and a weekly curated status feed.
  - *It does not do:* bookkeeping, filing or payroll. It runs alongside a3, TeamSystem or Sage.
  - *Extension:* the rule-status feed could also be sold to SMEs on its own. It was folded in here because free press coverage weakens it as a standalone product.
- **Why now:**
  - The 2026–2028 wave:
    - VeriFactu (2027 in the BOE, 2028 announced);
    - e-invoicing (2027, 2028, 2029);
    - societario regularisation in 2027–2028;
    - the MEI surcharge rising to 1% in 2027;
    - módulos limits for 2027 still pending.
  - Repeated failures to convalidate decree-laws make "is this rule actually in force?" a recurring question (TAX-02, TAX-14).
- **Alternatives today:**
  - a3 (Wolters Kluwer), TeamSystem/DELSOL, Sage (asesoría prices not retrieved).
  - Kabilio for invoice processing (promotional claims).
  - Excel.
  - Free content from AyE, the Infoautónomos blog and vendor blogs.
  - Weakness: the suites centre on bookkeeping and filing. The notes show no cross-client regulatory-readiness tracker.
- **Price hypothesis:**
  - €39–79/month per asesoría, by client count.
  - No asesoría software prices appear in the notes, so this must be validated.
- **Channels:**
  - The Consejo General de Gestores Administrativos and colegios of graduados sociales (not researched in Stage 1).
  - Asesoría events; a3 and Sage marketplaces; LinkedIn.
  - Vendors' asesoría programmes (Quipu has one) as partners or as competitors.
  - Searches: "software asesorías control clientes verifactu".
- **Build notes:**
  - A rules engine maintained by a tax specialist. The editorial work is a recurring cost.
  - Import of a3, Contasol and Sage exports.
  - WhatsApp Business API.
  - GDPR: the tool acts as a data processor for client data held by the asesoría.
  - Complexity: medium.
- **Moat in an AI-flooded market:** medium.
  - The strengths:
    - an accurate, maintained rules engine;
    - switching costs once client tags and history live in the tool;
    - the client-communication layer.
  - It is also a distribution base for G1-I03, G1-I07, G1-I08 and G1-I10.
  - It can be copied by Wolters Kluwer or TeamSystem, which own the installed base.
- **Key risks and kill criteria:**
  - Risks:
    - asesorías are slow to adopt: Excel-heavy, and only 41% of individual advisers are up to date;
    - incumbents could bundle a dashboard;
    - tiny firms have little room to pay.
  - Kill if:
    - fewer than 1 in 5 interviewed asesorías would pay €30/month or more;
    - or a3 or TeamSystem already offer equivalent client-readiness tracking.
- **Evidence strength:** medium.
  - The workload evidence comes from vendor surveys (Cegid, Quipu), but they are consistent.
  - The regulatory calendar is documented in the BOE and by the AEAT.
- **Validation questions:**
  1. Find the number of asesorías, gestorías and graduados sociales in Spain (Consejo General de Gestores Administrativos, colegios); this was a Stage 1 gap.
  2. Check a3 (Wolters Kluwer), TeamSystem/DELSOL, Sage and Cegid asesoría products for multi-client regulatory dashboards, and their prices.
  3. Look up Kabilio and similar asesoría add-ons: prices and integrations.
  4. Interview 15 small asesorías about how they track VeriFactu readiness and societario bases today, and what they would pay.
  5. Confirm that a3 and Contasol export client master data in a usable format.
  6. Test whether asesorías would pay for a white-label rule-status feed for their clients.

### G1-I07: Cuota and regularisation tracker for autónomos
- **Type:** C
- **Buyer:**
  - Autónomos (personas físicas) in estimación directa.
  - Societarios (owner-managers who pay RETA through their own SL) and family collaborators.
  - Gestorías and graduados sociales (labour and social-security advisers), buying in bulk.
  - Scale: 3,483,645 people were registered in the RETA at the end of September 2026. About 1.2M societarios and collaborators had their minimum base changed (TAX-13).
- **Pains addressed:** TAX-12, TAX-13.
- **Problem:**
  - Choosing a tramo is a forecast, and it is settled a year later.
  - In the ENA survey, 35.1% had to pay after regularisation. They rated the handling 2.2 out of 10, and 15% did not know their own tramo (TAX-12).
  - Societarios who do not update their base now face about €135/month more, and a lump-sum back-charge in 2027–2028 (TAX-13).
- **Product:**
  - *What it does:*
    - Pulls income from invoicing and bank data, or takes a monthly manual entry.
    - Estimates year-to-date net income and maps it to a tramo.
    - Shows the "regularisation exposure" in euros, with a suggested monthly amount to set aside.
    - Reminds the user of the six base-change windows a year and of the date the €80 tarifa plana (flat starter rate) ends.
    - In societario mode, checks the €1,424 minimum base.
    - Produces a one-page "how to change your base in Import@ss" guide, or a request to send to the gestor.
  - *MVP:* the calculator, an invoice or bank import, and a monthly alert.
  - *What it does not do (at least in the MVP):*
    - It does not change bases for the user. That needs Seguridad Social authorisation or RED access.
    - It gives no tax or labour advice.
- **Why now:**
  - The 2026 tables are frozen.
  - The MEI (intergenerational equity surcharge) rises to 1% in 2027, and the 2027 bases are still pending.
  - The societario regularisation will land in 2027–2028.
  - Negotiations on contributions have stalled for more than a year (TAX-12, TAX-13).
- **Alternatives today:**
  - Gestorías and graduados sociales, inside fees of €25–150/month.
  - Cuéntica's autónomo-fee calculator, part of its €19 plan.
  - Free published tables and calculators, such as Infoautónomos' cuota page.
  - Changing bases by hand in Import@ss.
  - Weakness: the calculators are one-off. Nothing tracks income continuously or warns of exposure.
- **Price hypothesis:**
  - €3–4/month or €29/year.
  - A gestoría bulk plan at €0.50–1 per client per month.
- **Channels:**
  - Invoicing apps, as an embedded or white-label module.
  - Gestorías and graduados sociales.
  - New-autónomo journeys, with regional "cuota cero" refunds and tarifa plana timing as hooks.
  - Searches: "regularización cuota autónomos", "qué tramo de autónomos me corresponde", "calculadora cuota autónomos 2027".
- **Build notes:**
  - Yearly cotización tables and the RDL 13/2022 net-income rules. The exact deductions are not in the notes; validate them.
  - A bank feed or invoice import.
  - A deep link to Import@ss.
  - Income data is sensitive.
  - Complexity: low.
- **Moat in an AI-flooded market:** low.
  - The formula is public and free calculators exist.
  - The only edges are continuous automation through integrations and distribution through gestorías. In plain terms: speed and distribution.
- **Key risks and kill criteria:**
  - *Risks:*
    - Invoicing vendors and online asesorías add it for free.
    - The system is redesigned.
    - Willingness to pay for a calculator is low.
  - *Kill if:*
    - Fewer than about 1 in 10 trial users pay at least €2/month.
    - Or retention collapses once the user has been through one regularisation.
- **Evidence strength:** strong for the pain; medium for software fit.
  - The pain rests on the ENA survey (878 responses), ATA data and the official tables.
- **Validation questions:**
  1. Confirm the 2026 cotización tables, which rest on a single source (Orden PJC/297/2026), and resolve the conflicting maximum base (€4,909 versus the table) noted in TAX-12.
  2. Confirm how net income for the RETA is computed, including deductions, and how the TGSS calculates and notifies the regularisation.
  3. Check whether the Junts proposición de ley (bill) on societario bases lapsed with the dissolution of the Cortes.
  4. Find official TGSS totals for the 2023 and 2024 regularisations, a TAX-12 gap.
  5. Look up whether Cuéntica, Infoautónomos, Declarando, TaxDown and Quipu offer continuous tramo tracking, and on which plans.
  6. Check what authorisation lets a third party view or change bases (Import@ss, RED).

### G1-I08: Official mailbox and tax-debt guard
- **Type:** C
- **Buyer:**
  - Companies, which must receive electronic notifications.
  - Autónomos who are obliged to, or have opted in.
  - Gestorías that monitor mailboxes for clients.
  - Scale: unknown how many use electronic notification; to validate. VeriFactu-scope estimate: 2.1M companies (single-source).
- **Pains addressed:** TAX-18, TAX-19, TAX-10, VOX-17. FIN-24 is merged in.
- **Problem:**
  - A notification counts as delivered after 10 days unopened, even when no email alert arrives.
  - After failed postal attempts, notice goes to the BOE.
  - Owners often find out only when an account is embargoed. Embargos now execute overnight (TAX-18, TAX-19).
  - Small slips cost €100–€600 in fixed fines (TAX-10).
  - Procedures have been filed in autónomos' names without their consent (VOX-17).
- **Product:**
  - *What it does:*
    - Checks the AEAT sede, DEHú and TGSS mailboxes daily, using the client's power of representation or collaborator status. The aim is to avoid holding their certificate.
    - Classifies each notice: requerimiento (formal request), providencia de apremio (enforcement order), embargo, sanction, or proposed assessment.
    - Computes the deadline and the 10-day deemed-delivery date.
    - Alerts by WhatsApp or SMS well before day 10.
    - Suggests the next step, such as "forward to gestor" or "pay by this date to keep the reduction".
    - Tracks debt and deferral instalments so a deferral is not cancelled by a missed payment.
    - Optionally, searches BOE edictal notices by NIF.
  - *MVP:* read and classify DEHú and AEAT notifications, send alerts, and offer a gestoría multi-client view.
  - *What it does not do:* it does not answer, appeal or represent. Those go to the gestor or a lawyer.
- **Why now:**
  - The 24-hour embargo roll-out runs to November 2026 (single-source).
  - An Audiencia Nacional ruling (489/2026) backs deemed delivery to the designated address.
  - The AEAT is fining post-campaign Renta corrections at €100 (October 2026) (TAX-10, TAX-18, TAX-19).
- **Alternatives today:**
  - Gestorías checking mailboxes by hand, inside their fees.
  - Official email alerts, which sometimes never arrive.
  - Personal vigilance.
  - The notes name no product, so validation must look for one.
- **Price hypothesis:**
  - €4–6/month per NIF.
  - A gestoría bulk plan at about €1 per NIF.
- **Channels:**
  - Gestorías: sold as automation of a job they already do.
  - Banks and neobanks, as an embargo-prevention add-on (speculative).
  - Searches: "notificación Hacienda no la abrí 10 días", "embargo cuenta Hacienda 24 horas", "buzón DEHú avisos".
- **Build notes:**
  - It needs a lawful, programmatic way to read the mailboxes, through representation or collaborator status. The fallback is holding clients' certificates, which carries a severe security and legal risk.
  - The data is highly sensitive and needs a security audit.
  - Complexity: medium to high, driven by access rather than code.
- **Moat in an AI-flooded market:** medium.
  - Integration with official systems and a security reputation are hard to fake.
  - The alerting logic is easy to copy once the access pattern is known.
- **Key risks and kill criteria:**
  - *Risks:*
    - There is no legal or technical access route without storing private keys.
    - The AEAT, DEHú or TGSS could improve their own alerts, for example through app push.
    - Gestorías may see this as their job.
  - *Kill if:* access requires holding clients' certificates, or the official apps already push reliable notices.
- **Evidence strength:** medium-high.
  - The rules are in the BOE (LGT) and the Audiencia Nacional ruling is reported by the press.
  - The 24-hour embargo rests on a single source.
  - There is no frequency data.
- **Validation questions:**
  1. Confirm the mechanisms for third-party access to the AEAT, DEHú and TGSS mailboxes: types of apoderamiento, colaboración social, any interface. Is automated reading allowed?
  2. Verify the AEAT resolution of 4 June 2026 on 24-hour embargos, which rests on a single source, and its roll-out.
  3. Find AEAT figures on electronic notifications, deemed deliveries and embargos, a TAX-18 gap.
  4. Search for notification-monitoring products for gestorías and SMEs in Spain, with prices.
  5. Confirm which taxpayers are obliged to receive electronic notifications.
  6. Check whether BOE edictal notices can be monitored automatically by NIF.

### G1-I09: Hacienda letter shield (pre-filing cross-check and evidence pack)
- **Type:** B (primary), secondary C.
- **Buyer:**
  - B2C autónomos and micro firms that take cards or Bizum: hospitality, dental and vet clinics, hairdressers, retail (including recargo de equivalencia, the special VAT regime for small retailers) and taxis.
  - Professionals in estimación directa whose expenses are at risk of challenge.
  - Gestorías, as resellers.
  - Count: unknown, to validate. Cards are accepted in 94% of small retail and hospitality businesses (FIN-13).
- **Pains addressed:** TAX-15, TAX-16, TAX-17, TAX-09.
- **Problem:**
  - Since January 2026, banks report card and Bizum collections to the AEAT every month (modelo 170). Mismatches with the VAT return (303) trigger letters.
  - Letters after the Renta (annual income-tax return) target unproven expenses and sector-ratio outliers.
  - The deductibility rules are "excesivamente restrictivas" (excessively restrictive).
  - Owners reconcile "operación por operación" (transaction by transaction), and must assemble proof under short deadlines (TAX-15, TAX-16, TAX-17).
- **Product:**
  - *What it does:*
    - Before each quarterly filing, it ingests card-acquirer, POS and Bizum settlement exports plus the bank feed.
    - It reconciles them against issued tickets and invoices and the draft 303/130 bases.
    - It explains each gap using the five known causes: cross-quarter refunds, tips, personal Bizum, third-party collections and exempt services.
    - An expense-risk checker flags vehicle, phone, meals and home-office lines, and asks for proof (a photo and the business purpose) when the expense is captured.
    - When a letter arrives, it assembles a response pack: invoices, bank proofs, the reconciliation and a deductibility rationale.
  - *MVP:* CSV import from SumUp, Stripe and banks, the comparison against 303 bases, and the PDF pack.
  - *It does not:* file returns, represent anyone before the AEAT, or argue disputes.
- **Why now:**
  - Monthly modelo 170 reporting has applied since 1 January 2026, with no minimum.
  - Letter waves run from September.
  - The Consejo para la Defensa del Contribuyente report came out in October 2026.
- **Alternatives today:**
  - Manual reconciliation by owners or gestorías.
  - Declarando's deductible-expense recommender (Pro plan, €69.90 with filings).
  - Receipt scanning in TaxDown and Quipu.
  - Gestorías or Legálitas once a letter has arrived.
  - Weakness: none of these is documented as checking the business's own figures against the third-party data Hacienda holds.
- **Price hypothesis:**
  - €7–12/month per business, or about €20 per quarter.
  - Gestoría bulk plans.
- **Channels:**
  - Gestorías, since letters land on their desks.
  - Acquirer and POS partners (SumUp and similar).
  - Associations of dental and vet clinics and of hairdressers.
  - Searches: "carta Hacienda Bizum descuadre", "modelo 170 datáfono 303".
- **Build notes:**
  - Settlement exports or APIs from acquirers; business-Bizum data through banks; bank aggregation.
  - Rules for VAT bases.
  - The data is highly sensitive.
  - Complexity: medium.
- **Moat in an AI-flooded market:** medium.
  - Data integrations with acquirers and banks, plus know-how about the AEAT's matching patterns.
  - Accounting suites could copy it.
- **Key risks and kill criteria:**
  - *Risks:*
    - The letter wave rests on a single press source, and how often letters arrive is unknown.
    - If taxpayers cannot see the modelo 170 data their bank filed, the product has to rebuild it.
    - Gestorías may already absorb this work within their fees.
  - *Kill if:*
    - Letters reach fewer than about 5% of B2C businesses a year.
    - Or acquirer data cannot be obtained without manual work.
- **Evidence strength:** medium.
  - The modelo 170 letters come from a single press source.
  - The post-Renta letter waves and the Consejo report are known only via the press (Gestha is the source for the letters).
- **Validation questions:**
  1. Verify RD 253/2025 and Orden HAC/747/2025 in the BOE: monthly modelo 170, no minimum, scope including Bizum.
  2. Can taxpayers, or their authorised representatives, download the modelo 170 data reported about them?
  3. Find AEAT or Gestha figures on letters sent over card and Bizum mismatches.
  4. Check whether SumUp, Stripe, Redsys-based bank terminals and Bizum for business offer exports or APIs of settlement data.
  5. Look up the reconciliation features of Holded, Quipu, Anfix, Declarando and TaxDown.
  6. Interview gestorías about how many requerimientos (formal AEAT requests) they handle per year and the hours each takes.

### G1-I10: SL director guard (dissolution-trigger and accounts-deposit alerts)
- **Type:** C
- **Buyer:**
  - Owner-managers of micro and small SLs, who are often autónomos societarios.
  - Sold mainly through their asesoría.
  - Count: the number of SLs is unknown (a TAX-21 gap), to validate. About 1.2M societarios and collaborators (TAX-13) gives a rough proxy for owner-managers.
- **Pains addressed:** FIN-17, FIN-16, TAX-21.
- **Problem:**
  - When losses push net equity below half of share capital, directors have two months to convene the shareholders. Those who miss the window can become personally liable for debts that arise in that period (STS 1477/2026).
  - Micro firms tend to file for insolvency only when it is too late: only 52 of 1,427 micro procedures aimed at continuation.
  - Missing the annual accounts deposit brings a registry block and ICAC fines of €1,200–€60,000 (FIN-16, FIN-17, TAX-21).
- **Product:**
  - *What it does:*
    - Reads the trial balance each month or quarter, from the accounting tool or an asesoría export.
    - Computes net equity against share capital and a cash runway, shown as a traffic light.
    - When the half-capital trigger is hit, starts a two-month countdown and offers a template notice convening the shareholders.
    - Keeps a dated log proving the directors acted in time.
    - Reminds the user of the annual-accounts deposit, due within a month of approval.
  - *MVP:* ledger or CSV import, the ratio check, alerts and lawyer-reviewed templates.
  - *It does not:* give insolvency advice or file anything (it refers to lawyers), or audit accounts.
- **Why now:**
  - STS 1477/2026 (October 2026) reinforces directors' personal liability.
  - Company insolvencies rose 15.5% year-on-year in Q4 2025 (FIN-17, FIN-16).
- **Alternatives today:**
  - Gestorías and accountants, "when they notice"; lawyers.
  - Accounting services at €59.95–€129/month.
  - Software with corporate-tax returns from €58.33/month (Anfix Empresarial).
  - Weakness: nothing in the notes alerts on the dissolution trigger.
- **Price hypothesis:**
  - €5/month per SL.
  - Asesoría bulk plan at €1–2 per SL.
- **Channels:**
  - Asesorías, which hold the books.
  - Accounting-software marketplaces.
  - Directors' liability insurers and brokers (speculative).
  - Searches: "causa de disolución por pérdidas responsabilidad administrador", "depósito de cuentas plazo multa".
- **Build notes:**
  - Imports from a3, Contasol, Holded and Quipu.
  - The LSC articles need confirming, because the press article cites none.
  - Templates reviewed by a commercial lawyer.
  - Complexity: low.
- **Moat in an AI-flooded market:** none; speed only. Any accounting vendor can add the ratio. The value lies in the legal workflow and the evidence log.
- **Key risks and kill criteria:**
  - *Risks:*
    - Owners of struggling firms ignore the alerts.
    - Asesorías treat it as a free feature.
    - Ledgers are often updated only quarterly.
  - *Kill if:*
    - Asesorías will not distribute it.
    - Or the main accounting suites already alert on the half-capital trigger.
- **Evidence strength:** medium.
  - STS 1477/2026 comes from a single press source.
  - The accounts-deposit fines come from the BOE (LSC).
  - The insolvency statistics are strong (Registradores).
- **Validation questions:**
  1. Read STS 1477/2026 and identify the LSC articles on the dissolution cause, the two-month duty and directors' liability.
  2. Count the SLs in Spain and the share that file abbreviated accounts (Registradores, INE).
  3. Check whether a3, Contasol, Holded, Quipu or Anfix alert on the half-capital trigger.
  4. Find data on how often directors face liability claims, and on how many companies fail to deposit accounts (Registradores, ICAC).
  5. Interview asesorías on whether they would pay for or distribute this to SL clients.

### G1-I11: Supplier bank-detail change guard (anti-IBAN-fraud payment check)
- **Type:** C (primary), secondary B.
- **Buyer:** micro and small firms (10–49 staff) where an owner or admin pays suppliers by bank transfer, and autónomos with recurring suppliers. How many such firms exist is unknown and needs validating.
- **Pains addressed:** FIN-12 (VOX-03 merged in).
- **Problem:**
  - Fraudsters email fake IBAN changes or pose as the boss, and the transfers they trigger cannot be reversed.
  - A secondary source puts BEC (business email compromise) losses above €15,000 per incident.
  - A vendor survey says 22% of SMEs were hit by invoice or payment fraud in 12 months.
  - INCIBE, the national cybersecurity institute, reports online fraud up 19% (FIN-12, VOX-03).
- **Product:**
  - *What it does:*
    - Keeps a register of verified supplier IBANs.
    - Watches incoming invoices and emails, and outgoing payment batches or SEPA files.
    - Flags any new or changed IBAN, mismatches between the bank and the supplier's country, look-alike sender domains and urgent "CEO" requests.
    - For any flagged payment, requires a call-back to the phone number on file (never one taken from the email) and approval by a second person.
    - Logs evidence for a later bank claim.
  - *MVP:* an email add-in, the IBAN register and a check on payment files.
  - *Does not:* replace bank security or cyber insurance.
- **Why now:**
  - Fraud is rising: INCIBE incidents +26% and helpline queries +44.9% in 2025.
  - Attackers now hijack autónomos' email sessions by stealing cookies instead of passwords (an October 2026 headline).
  - Structured B2B e-invoices from 2027–2028 offer a chance to tie each IBAN to a verified invoice.
- **Alternatives today:**
  - Banks' strong customer authentication and fraud alerts.
  - Verification of Payee, if it is in force (not verified).
  - INCIBE's 017 helpline (free).
  - Cyber insurance (not priced) and IT providers.
  - Weakness: these are reactive or generic. Nothing in the notes ties supplier identity to payment approval at the SME level.
- **Price hypothesis:** €5–9/month per company.
- **Channels:**
  - Cyber insurers and brokers (possibly as a premium discount), IT managed-service providers, gestorías.
  - Banks, as partners.
  - Searches: "fraude cambio de cuenta bancaria proveedor", "fraude del CEO pyme".
- **Build notes:**
  - Integrations with email suites, the SEPA payment-file format and optional bank aggregation.
  - A Verification of Payee lookup, if banks expose one.
  - GDPR applies.
  - Complexity: medium.
- **Moat in an AI-flooded market:** low.
  - The idea is easy to copy, and banks could bundle it.
  - The only edges are integrations and, later, linking IBANs to e-invoices.
- **Key risks and kill criteria:**
  - *Risks:*
    - Verification of Payee already does the name–IBAN check for free.
    - SMEs under-invest in security until they are hit.
    - Liability perception if a fraud slips through.
  - *Kill if:* Verification of Payee coverage makes IBAN-change fraud rare, or interviews show SMEs will not pay at least €5/month before suffering a loss.
- **Evidence strength:** medium. The trend data is official (INCIBE, Banco de España), but SME euro losses come only from a vendor survey and a secondary source.
- **Validation questions:**
  1. Verify Regulation (EU) 2024/886: Verification of Payee obligations and dates, and what Spanish banks show business customers.
  2. Find Spanish loss figures for CEO/BEC and IBAN-change fraud (INCIBE, Policía Nacional, Banco de España). The notes found none.
  3. Look up existing SME tools for verifying IBANs or controlling payments in Spain, including banks' own offers.
  4. Check whether e-invoices under RD 238/2026 carry a payee IBAN field that could be validated automatically.
  5. Price SME cyber insurance and check whether insurers discount premiums for payment controls.

### G1-I12: B2B subscription and contract guard
- **Type:** C
- **Buyer:** autónomos and micro firms with several SaaS, telecom, web and service contracts, especially former Kit Digital beneficiaries. Kit Digital made more than 860,000 grants (VOX-16). Beyond that, the number of buyers is unknown.
- **Pains addressed:** VOX-09, VOX-16, VOX-05, VOX-08, TAX-07.
- **Problem:**
  - Small businesses lose money to:
    - annual auto-renewals they forget;
    - cancellations that only "request" cancellation;
    - telecom permanencias (minimum-term penalties) that consumer protection does not cover;
    - Kit Digital leftovers (about €22–66/month for a website versus about €8/month hosting).
  - The notes found no one tracking renewal dates for them (VOX-05, VOX-09, VOX-16).
- **Product:**
  - *What it does:*
    - Detects recurring charges and contracts from bank and card feeds and from invoice emails.
    - Builds a renewal calendar with notice periods and permanencia end dates, and alerts 30 and 7 days before each renewal.
    - Flags price rises compared with the last period.
    - Generates cancellation requests sent with proof of delivery (certified email), then tracks the replies.
    - Suggests cheaper equivalents, for example moving a Kit website to €8–10 hosting (see G1-I13).
  - *MVP:* a bank feed, recurring-charge detection, the calendar and cancellation templates.
  - *Does not:* switch energy or telecom suppliers for commission, since that would create a conflict of interest.
- **Why now:**
  - Kit Digital's subsidised years have ended.
  - The VeriFactu and e-invoicing upsell wave is coming (C4).
  - Price-creep complaints are recurring (VOX-08).
- **Alternatives today:**
  - Spreadsheets.
  - Chargebacks and disputed SEPA direct debits.
  - Lawyers.
  - Spendbase: a blog post of theirs appears in the VOX gaps; the product and its Spanish availability are not verified.
- **Price hypothesis:** €3–5/month, or free with a share of first-year savings.
- **Channels:**
  - Business-account providers (neobanks and banks).
  - Gestorías.
  - Searches: "dar de baja kit digital", "cancelar suscripción Holded", "permanencia telefonía empresa".
  - Owner communities, organically (the Forocoches business subforum).
- **Build notes:**
  - Bank aggregation through a licensed partner.
  - Email parsing.
  - A partner for certified email.
  - Light regulatory burden, but medium-high data sensitivity.
  - Complexity: low to medium.
- **Moat in an AI-flooded market:** none; speed only. Banks can add subscription views.
- **Key risks and kill criteria:**
  - *Risks:*
    - The notes found no data on willingness to pay.
    - Savings are mostly one-off, so users may churn after the first clean-up.
    - The typical micro firm may have too few contracts to need this.
  - *Kill if:*
    - fewer than about 40% of users are retained after three months;
    - or the median target user has fewer than three recurring business contracts.
- **Evidence strength:** medium. Cancellation complaints are consistent across six or more vendors, but there are no data on how many contracts SMEs hold or what they would pay.
- **Validation questions:**
  1. Look up Spendbase and any Spanish B2B subscription-management tools, and check the subscription-detection features of business accounts (Qonto and the banks).
  2. Find survey data on how many software and telecom contracts a Spanish micro firm holds (ONTSI and INE pages could not be retrieved in Stage 1).
  3. Check which legal protections autónomos and companies have against auto-renewal and permanencia clauses.
  4. Check the Kit Digital terms on beneficiaries' obligations after the subsidy and on early-exit fees.
  5. Run a landing-page test aimed at former Kit Digital beneficiaries to measure willingness to pay.

### G1-I13: Kit Digital website rescue and low-cost managed hosting
- **Type:** A.
- **Buyer:** former Kit Digital beneficiaries, mostly autónomos and micro firms, who still pay for website upkeep after the subsidised year.
  - Kit Digital made more than 860,000 grants. How many included a website is unknown and must be validated (VOX-16).
- **Pains addressed:** VOX-16 (and the background of VOX-15, which was filtered out).
- **Problem:**
  - After the subsidised year, upkeep for a templated site costs from €21.98/month (Arsys) to €66/month (a forum figure).
  - Hosting costs about €8/month and a domain about €10/year.
  - Some contracts carry early-exit fees (VOX-16).
- **Incumbent and why a cheaper offer can work:**
  - Incumbents are the agentes digitalizadores (registered Kit Digital suppliers) and hosting firms. Arsys charges from €21.98/month after the subsidised year; one forum figure is €66/month.
  - Hosting and templated sites are commodities.
  - The monthly bill makes owners look for alternatives.
  - Trust in agents is damaged by pitches like "gratis, solo firma" ("it's free, just sign"), so a transparent, no-minimum-term offer stands out.
- **Product:**
  - *What it does:*
    - A free audit: what the owner pays, what they own (domain, content, access) and what their contract says (minimum term, exit fees).
    - Guided migration: export the content, transfer the domain, set up managed hosting.
    - Managed hosting with basic updates at €8–10/month, no minimum term.
    - An optional content refresh.
  - *MVP:* migration playbooks for the three to five builders that agents used most, plus a hosting partner.
  - *It does not:* sell SEO services, run ads or offer anything subsidy-dependent.
- **Why now:**
  - The last calls closed in October 2025, so most subsidised years end during 2026 (an inference).
  - Agents' upkeep fees are now charged in full.
- **Alternatives today:**
  - Freelancers (one forum offer was a rebuild for €20 plus hosting).
  - Cheap hosting and site builders (prices not captured in the notes).
  - Staying with the agent at €21.98–66/month.
- **Price hypothesis:** €8–10/month all-in, with free migration on annual plans.
- **Channels:**
  - Searches: "dar de baja web kit digital", "mantenimiento web kit digital precio".
  - Owner forums such as Forocoches.
  - Gestorías, which advised many clients on Kit Digital.
  - Local business associations.
- **Build notes:**
  - Migration tooling and a hosting partner.
  - A domain-transfer workflow.
  - Lawyer-reviewed letters for exit-fee disputes.
  - Complexity: low.
- **Moat in an AI-flooded market:** none; speed only. Any hosting company can copy this overnight.
- **Key risks and kill criteria:**
  - *Risks:*
    - Sites built on proprietary builders may not export.
    - Many owners do not value their site.
    - Margins are thin and the work is service-heavy.
    - The window is time-limited.
  - *Kill if:* most Kit sites cannot be exported, or median upkeep turns out to be below about €15/month.
- **Evidence strength:** medium.
  - The forum evidence is consistent, and there is a vendor price (from a search snippet).
  - There is no aggregate data on renewals or cancellations.
- **Validation questions:**
  1. Find Red.es and Acelera Pyme data on how many Kit Digital grants covered websites, and the renewal rate after the subsidised year.
  2. Collect post-subsidy prices and exit clauses from the main agentes digitalizadores (Arsys and others).
  3. Identify which site builders agents used and whether sites and domains can be exported.
  4. Confirm how long beneficiaries had to keep the subsidised solution, and when they became free to cancel.
  5. Price low-cost hosting and site builders in Spain.

### G1-I14: Review-attack alarm and evidence kit for local businesses
- **Type:** C.
- **Buyer:** restaurants, bars and local service businesses with Google or Tripadvisor listings. Their number is not in the G1 notes and must be validated with the hospitality and retail tracks.
- **Pains addressed:** VOX-01, VOX-02.
- **Problem:**
  - Attackers post bursts of fake reviews; one bar received about 20 one-star reviews from suspicious profiles in under an hour.
  - Extortion offers follow: pay up, or face more negative reviews.
  - Google's reporting tool "rara vez funciona" (rarely works), and owners have no evidence or process to fall back on (VOX-01).
  - Owners are also pitched illegal paid reviews (VOX-02).
- **Product:**
  - *What it does:*
    - Monitors the listings every few minutes.
    - Detects anomalies: bursts, new or empty accounts, copied text.
    - Alerts the owner at once.
    - Captures timestamped evidence through a certification partner.
    - Pre-fills platform reports and a complaint file for the police or a lawyer, then tracks the outcome of each report.
    - Optionally sends legitimate post-visit review requests with no incentive attached, to keep a healthy baseline of reviews.
  - *MVP:* Google listing monitoring, a spike detector, alerts and a PDF evidence pack.
  - *It does not:* remove reviews, buy or sell reviews, or offer incentives for reviews (illegal, VOX-02).
- **Why now:**
  - Attacks were still being reported in April 2026 (Merca2).
  - Fake reviews have been illegal since May 2022, with fines of up to €100,000, which gives evidence packs a legal path.
- **Alternatives today:**
  - Google's free tools.
  - Police cybercrime units and lawyers.
  - Reputation agencies such as OnbrandinG (not priced).
  - Illegal paid reviews at €1.5–2.5 each, or €200/month packages.
- **Price hypothesis:** €5–9/month per location.
- **Channels:**
  - Hospitality associations.
  - Booking and POS vendors, as an add-on.
  - Searches: "extorsión reseñas falsas restaurante", "ataque reseñas negativas Google".
- **Build notes:**
  - Access to listing data under platform terms; Tripadvisor access is unknown.
  - An evidence-certification partner.
  - Anomaly detection.
  - Complexity: low to medium.
- **Moat in an AI-flooded market:** low.
  - The product is easy to copy and depends on the platforms' goodwill.
  - Data on attack patterns across many listings is a slight edge.
- **Key risks and kill criteria:**
  - *Risks:*
    - Platforms restrict automated access.
    - Attacks may be too rare per business to justify a subscription.
    - Google may improve its own detection.
  - *Kill if:* fewer than about 1 in 20 restaurants report an attack a year, or listing data cannot be monitored within platform terms.
- **Evidence strength:** weak to medium. The evidence is press and opinion pieces, mostly from Catalonia, with no Spanish scale data.
- **Validation questions:**
  1. Find Spanish data on how often review extortion and review bombing happen (police, OCU, hospitality associations).
  2. Check the terms and quotas for automated monitoring of Google business listings and Tripadvisor.
  3. Look up OnbrandinG and other Spanish reputation tools, and their prices.
  4. Verify the Spanish legal basis and fines for fake reviews (the Omnibus rules) and whether court awards reach €20,000 (unverified).
  5. Get counts of restaurants and bars by city from the hospitality track.

---

## 5. Cross-group links

These overlaps are flagged so that a later merge can combine them. Track names are the Stage 1 file names.

| G1 pains or ideas | Overlapping track(s) | Why they overlap |
|---|---|---|
| C1, G1-I01, G1-I02 (FIN-06, FIN-07, FIN-08) | `legal_disputes_compliance.md` | MASC is a general civil requirement: monitorio, consumer claims and the lawyer/procurador threshold. Merge the MASC kits from both tracks into one product. |
| C1, G1-I01, G1-I02 (FIN-06, FIN-07, FIN-08) | `construction_realestate.md`, `midterm_housing_coliving.md` | The Málaga ruling (FIN-06) involved a homeowners' association, and rent arrears also pass through MASC. A single MASC engine could serve landlords, comunidades de propietarios and B2B creditors. |
| FIN-02 (subcontracting chains, 87–96.5 days), TAX-24 (filtered: renovation VAT tied to payment method) | `construction_realestate.md` | Subcontractor payment tracking and rule-aware invoicing for trades. The construction track should own TAX-24 and recheck whether RDL 29/2026 is convalidated. |
| C2, G1-I03 (TAX-05, TAX-06; FIN-25 merged) | All sector tracks, especially `transport_industry_agrifood.md` and `retail_ecommerce_services.md` | Every B2B invoicer is affected. Suppliers to firms above €8M feel it first, from 6 Oct 2027. |
| FIN-26 (proving payment periods for subsidies above €30k) | `bureaucracy_licensing_funds.md` | The same subsidy files and grant workflows. The 19% of firms that reportedly avoid public tenders because of late payment (FIN-04, filtered) also belongs there. |
| C3, G1-I04 (TAX-01 tills and scales), TAX-14 (módulos) | `retail_ecommerce_services.md`, `hospitality_tourism.md`, `transport_industry_agrifood.md` | Fruterías, carnicerías and bars with TPVs are where VeriFactu hardware costs land. Módulos users are concentrated in bars, haulage (Fenadismer) and about 800,000 farmers. These tracks should provide business counts per segment for G1-I04. |
| C5, G1-I06 (TAX-22, TAX-23, VOX-21) | `health_professional_education_care.md` | That track covers gestorías and law firms as businesses. Its pain points about asesorías should be merged into the asesoría cockpit, and gestorías should be treated as a shared channel across all groups. |
| C6, G1-I07 (TAX-12, TAX-13) | `labor_hr_litigation.md`, `startups_tech_ecosystem.md`, `bureaucracy_licensing_funds.md` | Graduados sociales and Social Security procedures (RED, Import@ss); founders who are societarios; regional "cuota cero" refunds (subsidies). |
| C7, G1-I08 (TAX-18, TAX-19, VOX-17) | `bureaucracy_licensing_funds.md`, `legal_disputes_compliance.md`, `expat_relocation_bureaucracy.md` | Monitoring official mailboxes (DEHú) and identity misuse in e-government overlap with e-government friction. Appeals against notifications are a legal matter. Foreign founders may also struggle to keep track of official notifications. |
| C8, G1-I09 (TAX-15 card/Bizum letters) | `hospitality_tourism.md`, `health_professional_education_care.md` (dental and vet clinics), `retail_ecommerce_services.md` (hairdressers, shops), `transport_industry_agrifood.md` (taxis) | These are the sectors the notes name as most exposed to card and Bizum mismatch letters. |
| C9, G1-I10 (FIN-16, FIN-17), FIN-15 (filtered, N6) | `legal_disputes_compliance.md`, `startups_tech_ecosystem.md` | Insolvency, Segunda Oportunidad and directors' liability are legal-track topics; most startups are SLs. |
| C10, G1-I11 (FIN-12; VOX-03 merged), VOX-04 (filtered) | `legal_disputes_compliance.md` (GDPR, NIS2), `hospitality_tourism.md` (breach at a booking-software provider) | Cyber-fraud and breach notification duties. A combined "SME cyber hygiene" bundle may be stronger than either track alone. |
| C11, G1-I12, G1-I13 (VOX-16, VOX-05), VOX-15 and VOX-18 (filtered) | `bureaucracy_licensing_funds.md` (Kit Digital), `cities_macro_surveys.md` (telecom and energy costs) | Kit Digital aftermath and B2B telecom contracts. VOX-06 (energy mis-selling) was filtered for old evidence. Given the 2026 energy shock reported in the project brief, other tracks may hold fresher evidence on SME energy contracts that would revive a "contract guard" angle. |
| C12, G1-I14 (VOX-01, VOX-02) | `hospitality_tourism.md`, `retail_ecommerce_services.md` | Review extortion and review dependence for restaurants and local services. Those tracks should provide business counts and any further evidence. |
| VOX-14 (filtered: HR software seat minimums) | `labor_hr_litigation.md` | The labour track owns the status of the time-recording obligation. Recheck micro-employer HR tools against Holded's €1.50-per-employee add-on. |
| FIN-19, FIN-20, FIN-21 (filtered: catastrophes and insurance) | `cities_macro_surveys.md` (Valencia), `bureaucracy_licensing_funds.md` (aid calls) | DANA recovery aid and recurring regional disasters, if another track finds stronger evidence of SME pain. |

---

## 6. Group top 5

These are the five strongest ideas, listed in ID order. They are not ranked; ranking comes after validation.

1. **G1-I01, MASC-ready claim kit.** A mandatory step in force since April 2025 now precedes about 180,000 monitorios a quarter. The legal templates and certified-channel partnerships make it harder to copy than most ideas, and per-claim pricing beats €99.90 per file or 5–25% success fees.
2. **G1-I03, E-invoice inbox and payment-status reporter.** It has the most certain regulatory driver in the group: dates fixed in the BOE that do not depend on Parliament. Status reporting and bank matching are unsolved for micro firms. The free SPFE caps what basic exchange can charge, but not the value of automation.
3. **G1-I06, Asesoría compliance cockpit.** It sells to the people who choose their clients' software (VOX-21) during a 2026–2028 wave that forces client-by-client reviews. It is also the distribution base for G1-I03, G1-I07, G1-I08 and G1-I10.
4. **G1-I07, Cuota and regularisation tracker.** It has the largest addressable base: 3.48M RETA members, 35% of whom paid after regularisation, and who rate the process 2.2/10, plus about 1.2M societarios facing back-charges. It is cheap to build and fits the €3–5 low-touch model, but it is plainly copyable.
5. **G1-I08, Official mailbox and tax-debt guard.** Notifications count as delivered after 10 days, and embargos now execute overnight, so a missed notification is expensive. It delivers visible value once set up. Lawful access to official mailboxes is both its moat and its kill risk.
