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
