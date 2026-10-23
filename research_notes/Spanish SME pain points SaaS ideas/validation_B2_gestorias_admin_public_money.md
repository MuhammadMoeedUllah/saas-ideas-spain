# Validation batch 2: gestorías, the public administration and public money

*Validator: batch 2 of 8. Prepared 23 October 2026. Ideas: IDEA-06, IDEA-07, IDEA-08, IDEA-09, IDEA-10, IDEA-25, IDEA-26, IDEA-27, IDEA-28.*

*Status: in progress. Sections are appended idea by idea; the summary table is filled in at the end.*

*Conventions: [new: URL, date] = fetched or searched in this validation, with the date the page was published or seen; [notes: PAIN-ID] = stage-1 evidence. Prices exclude VAT unless stated. "Single source" marks claims with one origin.*

---

## 1. Batch summary

(filled in at the end)

---

## 2. Ideas

#### IDEA-07: Official e-notification watchdog and tax-debt guard — KILL (high)

**Validated definition.** A €4–9/month alert service per company (and a €1–2/client board for gestorías) that watches DEHú, the AEAT and the TGSS, escalates before the day-10 deemed-delivery date, tracks certificates and debts, and searches BOE edicts by NIF. Validation found that every core function except multi-channel escalation is already offered free by the administration or sold cheaply by incumbents to gestorías, and that the "no lawful access" fear is unfounded. As a standalone product it is killed. What survives is a feature: an apoderamiento-based, multi-client notification view inside IDEA-06, for gestorías that do not already run a3, Cegid or Sage tools.

**(a) Problem reality and rule status (Oct 2026).** The rule is in force and is not exposed to the election.
- Legal persons, entities without legal personality, professionals in compulsory colegios and their representatives must deal with the administration electronically (Ley 39/2015 art. 14.2). An e-notice is deemed rejected 10 calendar days after it is made available without access to its *content* (art. 43.2). The alert is sent, but "la falta de práctica de este aviso no impedirá que la notificación sea considerada plenamente válida" (art. 41.6) [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-10565/texto/bloque/a43 and /a41, consolidated text, seen 23 Oct 2026].
- Art. 43.1 defines "comparecencia" as access by the interested party or representative "al contenido de la notificación". Viewing the pending list is therefore not access, and the AEAT's own pending-notices screen separates the list (exportable to CSV) from a signed "Firmar y Enviar" step to open content [new: https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/notificaciones-electronicas-ayuda-tecnica/notificaciones-comparecencia-sede.html, updated 19 Oct 2026]. This settles the batch question "does viewing the pending list count as access": no.
- **DEHú coverage (settles part of the section-5 e-notification question).** RD 203/2021 art. 42.5: every notice from a state-level issuer "se pondrá a disposición del interesado a través de la Dirección Electrónica Habilitada única"; issuers may also notify in their own sede. Art. 44.3 tells all administrations to make their notices reachable through DEHú, but adhesion by regions and councils is voluntary (art. 65). Art. 43 calls the alert "de carácter meramente informativo" [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2021-5032/texto/bloque/a4-4, /a4-5, /a4-6, seen 23 Oct 2026]. The AEAT says all its notices, "no sólo las electrónicas", go to DEHú [new: AEAT, informacion-general-sobre-notificaciones-electronicas.html, updated 19 Oct 2026]. So the "9,000+ sedes" problem (vendor claim, [notes: ADM-08]) is real only for regional, local and judicial issuers.
- **Courts.** Legal persons must receive court communications electronically. A first summons unopened for 3 days goes to home delivery and then to the Tablón Edictal Judicial Único; other court communications are deemed made after 3 days (LEC arts. 155.1 and 162.2, versions in force since 20 Mar 2024 and 3 Apr 2025) [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a155 and /a162, seen 23 Oct 2026]. This confirms the snippet-only claim in [notes: ADM-08]; the judicial e-office is a separate channel from DEHú.
- **24-hour embargoes: confirmed, no longer single source.** Resolución de 4 de junio de 2026 of the AEAT's Directorate-General, BOE-A-2026-13031 (BOE 16 Jun 2026). Orders are made available before 20:00, collected between 20:00 and 07:00, and retained "antes de las 08:00 horas del día siguiente". Embargo extends to up to ten accounts per diligencia at the same entity. It applies to diligencias issued from **2 Nov 2026**, with the REST channel from 1 Mar 2027 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-13031, seen 23 Oct 2026]. The press summary was accurate [new: AyE, 22 Aug 2026, https://www.autonomosyemprendedor.es/articulo/hacienda/hacienda-podra-embargar-cuentas-bancarias-autonomos-menos-24-horas-partir-septiembre/20260821085621055511.html].
- **Case law is still split; no 2026 Supreme Court ruling was found** (1 search):
  - strict line: TS 1927/2017 [notes: ADM-08] and AN 489/2026 [notes: TAX-18];
  - protective line: TS 17 Dec 2024 (Colombo Enterprises SL v Agencia Tributaria de Andalucía). The court annulled an apremio because the switch to electronic notification was unannounced, and said the administration "debió haber tomado medidas alternativas" once it saw the notice had not been accessed [new: https://primeralecturaediciones.com/sentencias/archivo/el-ts-protege-el-derecho-a-la-tutela-judicial-efectiva-en-notificaciones-electronicas, 4 Feb 2025]. Also TSJ Murcia 396/2025 [notes: ADM-08].

  The fear factor that drives demand persists.

**(b) Competitors.**

| Product | Segment | Coverage claim | Price | Source |
|---|---|---|---|---|
| **Official DEHú** | everyone | AGE plus adhered bodies | free: email alerts to up to 5 addresses; push alerts through the official *Notifica App*; "Gran destinatario" web services for automated consultation | [new: AEAT help pages acceso-notificaciones-electronicas-dehu.html and recibir-avisos-nuevas-notificaciones-comunicaciones-dehu.html, updated 16 Oct 2026] |
| **AEAT avisos** | everyone | AEAT | free SMS and email alerts, plus notification alerts in the AEAT app; up to 30 "días de cortesía" a year when no AEAT notice is put in DEHú | [new: AEAT avisos-notificaciones-telefono-movil-correo-electronico.html and dias-cortesia-notificaciones.html, updated 19 Oct 2026] |
| **BOE TEU and TEJU alerts** | everyone | edicts | free same-day email alert when an edict carrying your NIF is published; companies sign up with a certificate. Caveat: some issuers omit the NIF | [new: https://www.boe.es/notificaciones/ciudadanos_y_empresas/index.php, seen 23 Oct 2026] |
| **MsNotifica (Cegid Microdata)** | professional firms reselling to clients | DEHú, AEAT, Seguridad Social, DGT, e-NOTUM, Junta de Andalucía, Euskadi; "más de 9000 organismos" | 50 CIFs €40/month; 100 €50; 250 €90; 500 €120; extra CIF from €0.25/month, i.e. **€0.24–0.80 per client per month** | [new: http://msnotifica.com/ and http://msnotifica.com/precios/, © 2025, seen 23 Oct 2026] |
| **a3ASESOR \| Portal Neos (Wolters Kluwer)** | asesorías | 060/PAG, AEAT, Seguridad Social, DGT, DEH, GENCAT, ORGT Barcelona, Xunta, Comunidad de Madrid NOTE, Basque foral bodies, LexNET; TEU tracking; certificate-expiry control; mass association of the despacho's certificates or apoderamiento; alert manager | pay per use (no list price) | [new: Wolters Kluwer brochure, https://assets.contenthub.wolterskluwer.com/api/public/content/079a0fe3f7f042369c4c1ecb4ee62ade, undated, older vintage] |
| **IvNeos (Ivnosys, Signaturit group, now Namirial)** | large companies (Cepsa, Iberdrola, Abertis testimonials) | "más de 9.000 organismos públicos" | quote only | [new: https://ivnosys.com/gestor-notificaciones-electronicas-ivneos-2/, seen 23 Oct 2026] |
| **EdasNEO (ZeroComa)** | asesorías; said to be included in Sage Despachos | not verified | not verified | [new: edasneo.com, seen 23 Oct 2026] |
| **CopilotGestoria** | gestorías | — | notification module said to be included in its SaaS (from €15/month) | [new: https://copilotgestoria.com/blog/dehu-2026-guia-apoderamiento-protocolo-gestion-notificaciones-electronicas-gestorias, 28 Apr 2026, vendor source] |
| **Online asesorías bundling it** | autónomos and SMEs | DEHú, via the client's apoderamientos | Ayuda T Pymes: "revisión periódica de DEHú" is part of the service, as an "obligación de medios"; liability capped at 2× fees; plans from €29.95/month | [new: https://www.ayudatpymes.com/terminos_y_condiciones, updated 1 Apr 2026] |

- **Gap.** What is left is multi-channel escalation (WhatsApp and phone call to two named people), a heartbeat, a diligence log, and coverage of non-DEHú regional, local and judicial sedes. All are thin and copyable.
- **Review complaints.** One vendor blog cites "una tasa de error del 41%" in DEHú and AEDAF criticism that email alerts were lost when DEHú replaced NEO. Both are second-hand, and the 41% figure is internally inconsistent [new: CopilotGestoria blog above]. If verified, they would be the strongest argument for an independent watchdog.

**(c) Buyers and market size.**
- INE DIRCE (1 Jan 2025):
  - 3,310,824 active companies, of which 1,859,925 are natural persons;
  - so 1,450,899 legal entities and entities without personality, including 1,127,515 SLs, 46,763 SAs and 108,354 comunidades de bienes [new: INE API table 73018, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73018?nult=1, seen 23 Oct 2026].
- Reachable share: the micro firms without an adviser holding apoderamientos. That share is unknown [I].
- Revenue ceiling at €5/month: 1% of 1.45M entities ≈ 14,500 × €60 ≈ €0.87M ARR. The gestoría channel at incumbent prices (€0.25–0.80/client) is far lower.

**(d) Willingness to pay.** Incumbents sell to gestorías at **€0.24–0.80 per client per month**, 2–8× below the hypothesis of €1–2. SMEs that pay an asesoría €25–130/month already get monitoring inside the fee [notes: TAX-22], [new: Ayuda T T&Cs]. Free official push, email and SMS alerts anchor the SME price near zero.

**(e) Distribution.**
- Gestorías are concentrated but are competitors' customers: a3, Cegid and Sage bundle this.
- Banks offering embargo prevention are speculative; no evidence found.
- Notaries and company-formation services at incorporation: unproven.
- Search demand was not measured.

**(f) Build feasibility and legal constraints (settles the cross-cutting access check batch 2 owns).**
- **Lawful access without holding clients' private keys exists.**
  - At the AEAT, the obligated party grants a natural or legal person the **GENERALNOT** power, or a specific power to receive notifications. It is granted online with certificate or Cl@ve, in person, or by notarial document, and the apoderado confirms it. The apoderado then sees the poderdante's notices in DEHú and in the AEAT sede ("En nombre de") with its own credentials [new: AEAT acceso-dehu-mediante-apoderamiento.html, updated 16 Oct 2026].
  - Representation can also be recorded in the State's Registro Electrónico de Apoderamientos (RD 203/2021 arts. 32–33) [new: BOE blocks a3-4, a3-5].
  - DEHú offers **"Gran destinatario"** services "para la consulta automatizada de notificaciones", with published specifications [new: AEAT acceso-notificaciones-electronicas-dehu.html]. Whether a third-party apoderado may use Gran destinatario for many poderdantes was not verified, because the specifications are on dehu.redsara.es, which blocked automated access.
- **Constraints.**
  - The apoderado can open content, which starts deadlines. That is liability (Ayuda T limits it to an "obligación de medios").
  - Non-DEHú regional and local sedes still need per-sede integration.
  - Data are confidential tax data.
  - Holding certificates is not required, but would be needed for sedes without apoderamiento.
- **Time to MVP:** 2–4 weeks for alert parsing and escalation; 1–2 months for an apoderamiento-based DEHú/AEAT reader (subject to the Gran destinatario terms).

**(g) Defensibility.** None for the alert layer. Incumbents own the gestoría base, and the official channels improve for free (Notifica App push, 5 email addresses). Multi-sede coverage is an integration grind that IvNeos, Cegid and Wolters Kluwer have already done.

**(h) Kill criteria.**
1. "No lawful programmatic access without holding clients' private keys" (or certificate custody unacceptable to more than 70% of owners): **not met.** Apoderamiento (GENERALNOT/REA) and Gran destinatario exist.
2. "The official apps already push reliable alerts": **largely met.** DEHú Notifica App push plus up to 5 emails, AEAT SMS/email/app, BOE NIF alerts. Reliability is disputed only by unverified vendor claims.
3. Pilot: under half of pilot companies receive a notice in six months: **open [I].**

Also met: the gestoría board is saturated at prices below the hypothesis.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced, continuous duty; overnight embargo regime from 2 Nov 2026 (BOE-A-2026-13031) |
| S2 Buyers | 5 | About 1.45M legal entities plus colegiados (DIRCE 2025) |
| S3 WTP | 2 | Official alerts are free; gestoría tools cost €0.24–0.80 per client |
| S4 Reachability | 2 | Gestorías already equipped by a3, Cegid and Sage; SMEs without advisers are diffuse |
| S5 Competitive gap | 2 | Several decent tools plus free official push and email; only escalation and non-DEHú sedes are open |
| S6 Build speed | 4 | Alert layer in weeks; apoderamiento reader in 1–2 months |
| S7 Defensibility | 1 | Trivially copyable; incumbents bundle it |
| S8 Retention | 3 | Recurring duty and a diligence log, but invisible value when no notices arrive |

- **Sellability** 2.88 (23/8). **P** 3: severe when it happens (apremio surcharges of 5–20%, embargo), but frequency per firm is unquantified and most firms already have a monitor.
- **Overall** = 0.6 × 2.875 + 0.4 × 3 = **2.93**.

**Open [I] checks.**
- Six-month pilot of notice frequency among micro SLs without an adviser.
- Share of SLs whose gestoría holds GENERALNOT or REA powers.
- Gran destinatario terms for third-party apoderados (download the specification from DEHú).
- Measured DEHú alert failure rate.

**What would change the verdict.**
- Verified evidence that DEHú or AEAT alerts fail often.
- A large set of high-stakes issuers outside DEHú (regional tax agencies, big-city councils, the judicial e-office) that the incumbents do not cover.
- A bank or neobank willing to pay for embargo prevention as a white-label service.

Any of these would justify a RESHAPE to a B2B2C watchdog sold through banks. Otherwise the useful parts become a free feature of IDEA-06.

#### IDEA-09: Autónomo cuota and regularisation tracker — KILL (medium-high)

**Validated definition.** A €3–4/month (or €29/year) subscription for autónomos and societarios. It:
- estimates year-to-date net income for RETA purposes from invoices, bank data or manual entries;
- maps the estimate to one of the 15 tramos;
- shows the coming regularisation in euros;
- reminds the user of base-change windows and checks the societario minimum.

Validation confirms the pain and the formula, but finds the core feature already sold inside the leading autónomo platform and given away as free calculators. Nothing defensible is left for a standalone subscription. It is killed as a product and kept as a free feature (a bulk societario-base check) inside IDEA-06.

**(a) Problem reality and rule status.**
- **2026 parameters (settles C-09).** The 2026 tables are in Orden PJC/297/2026 of 30 March (BOE-A-2026-7296, 31 Mar 2026), art. 18 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-7296, seen 23 Oct 2026]:
  - **Bases:** maximum €5,101.20 for every tramo. Fifteen tramos: three reduced (tramo 1 ≤€670: base €653.59–718.94) and twelve general (tramo 12 >€6,000: minimum base €1,928.10).
  - **Contribution rates:** common contingencies 28.30%, professional 1.30%, MEI 0.90%.

  The "€4,909 maximum base" in [notes: TAX-12] is the 2025 figure; €5,101.20 is correct for 2026. The same table is on the Seguridad Social site [new: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537, seen 23 Oct 2026].
- **MEI (settles C-03).** LGSS DT 43ª (added by RDL 2/2023) sets 0.80 points in 2025, **0.90 in 2026** and **1.00 in 2027**, rising to 1.2 by 2029 [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11724/texto/bloque/dt-14, seen 23 Oct 2026]. Orden PJC/297/2026 confirms 0.90% for 2026 and puts it wholly on the autónomo in RETA. The 0.80% figure in the labour notes came from a page that had not been updated.
- **Net-income rule.** LGSS art. 308.1.c (RDL 13/2022) computes income as IRPF net income plus Social Security contributions, minus a 7% generic-expense deduction (3% for societarios). The TGSS regularises once the tax administration transmits the data the following year [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2015-11724/texto/bloque/a308, seen 23 Oct 2026]. The formula is public and simple.
- **Societarios.** Art. 308.1.a, rule 4ª: societarios and family collaborators cannot choose a base below the Régimen General group-7 minimum, and "en el procedimiento de regularización... la base de cotización definitiva no podrá ser inferior a dicha base mínima". For 2026 that minimum is €1,424.40. Orden PJC/297/2026 art. 18.4 lets them keep their 2025 provisional base during 2026, so a lump-sum back-charge arrives when 2026 is regularised. This confirms [notes: TAX-13].
- **Regularisation calendar.** The 2024 regularisation was notified from January to February 2026. Underpayments are due the month after notification; refunds are automatic [new: Última Hora, 12 Feb 2026, https://www.ultimahora.es/noticias/local/2026/02/12/2568841/pimem-gestores-administrativos-instan-autonomos-revisar-regularizacion-cuotas-2024.html]. Refunds are paid within four months (Seguridad Social page above).
- **Junts bill on societario bases.** No vote or approval was found (1 search). Opponents (PP, Junts, Vox) planned to act through amendments [new: Forbes, https://forbes.es/economia/903587/pp-junts-y-vox-trataran-de-frenar-en-el-congreso-el-sablazo-a-los-autonomos-societarios-y-colaboradores/, 2026]. Under Reglamento del Congreso art. 207 (as amended 22 Jul 2025), "Disuelto el Congreso... quedarán caducados todos los asuntos pendientes" except those for the Diputación Permanente [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1982-5196/texto/bloque/art207, seen 23 Oct 2026]. **Any pending bill lapsed on 6 Oct 2026, so the €1,424.40 floor stands.**
- **2027 bases.** Not set; the 2027 table needs a budget law or decree, and none was found. The MEI rises to 1.0% by law.
- **Pain evidence.** 35.1% paid after regularisation and rated the process 2.2/10 [notes: TAX-12]. Societarios face about +€135/month, and the Ombudsman criticises the method [notes: TAX-13, ADM-11]. National TGSS totals for the 2023 and 2024 regularisations were **not found** (1 search). Only a regional colegio figure exists: in Baleares, 29% of autónomos had well-adjusted bases [new: Última Hora above].

**(b) Competitors.**
- **Declarando Pro** (€39.90/month + VAT on the annual plan without filings; €69.90 with filings) includes "Cuota de autónomo recomendada para evitar reclamaciones de Seguridad Social — Usamos un algoritmo patentado que predice lo que vas a ganar durante el año, para que pagues la cuota adecuada". Declarando also publishes a free "Simulador de la cuota de autónomos" [new: https://declarando.es/precios, seen 23 Oct 2026].
- **Cuéntica** plans: "Calcula la cuota de autónomos y el tramo que te corresponde según tu contabilidad real". It also offers a free public calculator with the 2026 tables [new: https://cuentica.com/precios/ and https://cuentica.com/calculadora-cuota-autonomos/, seen 23 Oct 2026].
- **Import@ss (TGSS)** shows each person's "Regularización anual de cuotas" result and lets them change bases. No simulator with alerts was found on its landing page [new: https://portal.seg-social.gob.es/wps/portal/importass/importass/, seen 23 Oct 2026].
- Not checked: Quipu, Holded, TaxDown and Infoautónomos tool pages (Holded's calculator URL returned 404).
- **Gap.** Only autónomos who use a traditional gestoría or a basic invoicing app lack continuous tracking. Their gestoría already gets the regularisation notices through RED.

**(c) Buyers and market size.**
- 3,483,645 people in the RETA at end-Sep 2026 [notes: FIN-18], and about 1.2M societarios and collaborators [notes: TAX-13].
- Ceiling: at €29/year, 1% of the RETA is about 35k × €29 ≈ €1.0M ARR. The share willing to pay is unknown; ENA shows high outsourcing (57%) [notes: TAX-22].

**(d) Willingness to pay.** The adjacent spend is high (€25–150/month for gestorías and online asesorías [notes: TAX-22]), but this feature is bundled at no marginal price. Free calculators anchor the standalone price at €0. The source's own kill test (at least 1 in 10 trial users paying €2/month) is open [I], but the market anchors are discouraging.

**(e) Distribution.**
- High-intent searches exist ("regularización cuota autónomos", "calculadora cuota autónomos"), but they are dominated by Infoautónomos, Declarando, Cuéntica and TaxDown content (desk observation).
- Gestorías and colegios already campaign on the regularisation: the colegio de gestores and PIMEM did so in Baleares [new: Última Hora].
- Invoicing apps can add the feature themselves.

**(f) Build feasibility.**
- Formula and tables are public (LGSS 308; Orden PJC/297/2026), so an MVP takes under 4 weeks.
- Changing the base for the user requires an Import@ss authorisation or RED access. The six change windows a year are from the notes [notes: TAX-12]; the regulation article was not re-fetched.
- Income data is sensitive, so GDPR applies; no certification is needed.

**(g) Defensibility.** None. The calculation is public and incumbents already market it (Declarando's "algoritmo patentado").

**(h) Kill criteria.**
1. "Declarando, Cuéntica and Quipu already warn users about band changes": **met** for Declarando (continuous recommendation) and Cuéntica (tramo from real accounts); Quipu not checked.
2. "The TGSS portal already offers a reliable simulator with alerts": **not met** (none found).
3. "Fewer than 1 in 10 trial users pay €2/month or more", or retention collapses after one regularisation: **open [I].**

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Annual enforced regularisation; societario back-charge on 2026 income; MEI to 1% in 2027 |
| S2 Buyers | 5 | 3.48M RETA members |
| S3 WTP | 2 | Bundled in paid plans and free calculators; no standalone spend evidenced |
| S4 Reachability | 3 | Search demand is real but owned by incumbents' content; gestorías campaign already |
| S5 Competitive gap | 2 | Declarando and Cuéntica track it; free simulators |
| S6 Build speed | 5 | Public formula; MVP in under 4 weeks |
| S7 Defensibility | 1 | Trivially copyable |
| S8 Retention | 3 | Periodic use; risk of churn after the regularisation |

- **Sellability** 3.13. **P** 3: a lump-sum cash shock (about €1,600/year for societarios) of money owed anyway, with no penalty if paid on time.
- **Overall** = 0.6 × 3.125 + 0.4 × 3 = **3.08**.

**Open [I] checks.**
- Paid conversion at €2–3/month among autónomos who use traditional gestorías.
- Whether gestorías would pay for a bulk societario-base check (about 1.2M affected).
- National TGSS regularisation totals.

**What would change the verdict.** Official data showing that a large share of autónomos (above 30%) receive back-charges above €1,000, plus a distribution deal with a large invoicing app or bank willing to embed and pay per user. Even then the moat stays at zero, so it would be at best a feature, not a business.

#### IDEA-06: Gestoría client-obligation cockpit — RESHAPE (medium)

**Validated definition (after reshape).** A vendor-neutral **client-readiness tracker for small gestorías and asesorías** (1–9 staff), led by the 2027–2029 invoicing wave. The gestoría imports its client list (CSV or a3/Contasol/Sage exports). For each client the tool records:
- regime, turnover band and territory (common, foral, Canarias);
- invoicing software, and whether that product shows a VeriFactu declaración responsable;
- the documented VeriFactu or non-VeriFactu mode choice;
- the e-invoicing date (6 Oct 2027 for turnover above €8M, 6 Oct 2028 for the rest) and the status-reporting date.

It then sends bulk questionnaires and notices (ES/CA/EU), tracks replies, shows a progress board (contacted, diagnosed, needs new tool, ready) and keeps a dated rule-status feed (in the BOE, announced, draft, lapsed).

Three cheap retention modules sit on the same client list:
- the societario €1,424.40 base check (from IDEA-09);
- an apoderamiento-based notification view (from IDEA-07);
- a half-capital ratio check (from IDEA-10).

Price €29–59/month by client count. The €5/month SME "what changed for me" digest is **dropped**: free BOE alerts and vendor content cover it.

**(a) Problem reality and rule status.**
- The job is real and the vendors themselves tell asesorías to do it by hand:
  - TeamSystem's 8-step guide asks asesorías to build "un inventario real de la cartera" by client (entity type, turnover, software, complexity, contact, urgency), segment it and "mide el avance" (clients contacted, diagnosed, needing a tool change) [new: https://teamsystem.es/magazine/verifactu-factura-electronica-asesorias-2027/, 18 May 2026, updated 7 Oct 2026];
  - Sage's checklist asks for a documented per-client choice of VeriFactu mode [new: search summary of https://www.sage.com/es-es/blog/validacion-verifactu-entrada-en-vigor/, 2026; page not opened].
- **No official list of compliant software exists.** The AEAT FAQ says certification is a self-declaration by the producer, and "no se prevé ningún registro previo del producto SIF por parte de nadie" [new: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html, FAQ updated 21 Oct 2026]. A maintained product-declaration database is therefore something only a third party can build. This settles check 5, first part.
- **E-invoicing dates.** Orden HAC/1028/2026 entered into force the day after its BOE publication (5 Oct 2026). That starts the periods in DF 8ª of Ley 18/2022 and in DT 1ª–3ª and DF 4ª of RD 238/2026 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2026-20587, seen 23 Oct 2026]. The Consejo General de Gestores' table puts the periods at 12, 24 and 36 months, with status reporting for firms of €8M or less voluntary until the 36-month date [new: https://www.consejogestores.org/?p=14916, 30 Apr 2026, based on the draft order]. Batch 1 owns C-05 and C-08; the cockpit's value grows with exactly this kind of disagreement.
- **Rule churn under dissolution.**
  - Pending bills lapsed on 6 Oct 2026 (Reglamento del Congreso art. 207 [new: BOE-A-1982-5196 art. 207]).
  - Decree-laws now go to the Diputación Permanente.
  - The 2026 MEI is 0.90% and the 2027 MEI 1.00% (C-03 settled; see IDEA-09).
  - The 2027 módulos limits are again pending [notes: TAX-14].

  These are all rule-status items a gestoría must track per client [notes: TAX-02, LAB-25].

**(b) Competitors.**
- **Single-vendor client panels** cover only clients on that vendor's product:
  - Holded for asesorías: "Verifactu y factura electrónica de serie para todos tus clientes", one panel, partner programme;
  - Quipu: "panel para analizar el estado de tu cartera";
  - Bilky Portal Asesor;
  - CopilotGestoria: "Radar Fiscal" traffic light of clients at risk before filing, VeriFactu remission for clients on its portal, from €15/month, free plan for 5 clients, "100+ gestorías activas".

  CopilotGestoria states that for clients on other programs "el despacho no ve su estado en la pantalla de cartera" [new: search summaries of https://www.holded.com/es/pide-demo-asesorias, https://getquipu.com/es/asesorias and https://copilotgestoria.com/remision-verifactu; https://copilotgestoria.com/ fetched 23 Oct 2026]. That is the cross-vendor gap.
- **Regulatory content and AI Q&A.**
  - TeamSystem Asesor Excelente: training plus AI for regulatory queries; no price [new: TeamSystem article above].
  - a3ASESOR has an alert manager for deadlines and notifications [new: Wolters Kluwer brochure, see IDEA-07].
  - Minsait TaxFinder classifies regulation by client keywords, for large firms [new: search summary of https://www.minsait.com/sites/default/files/06_brochure_tax_finder_v5_1.pdf].
  - BOE a la Carta: free email alerts [new: search summary of datos.gob.es, 6 Nov 2017].
- No product mapping rule changes to a gestoría's client list was found (2 searches).
- Not checked: Sage Despachos and a3 portfolio dashboards (the pages blocked automated access), and Kabilio (invoice OCR only [notes: TAX-23]).

**(c) Buyers and market size (settles the cross-cutting gestoría-count check).**
- INE DIRCE, 1 Jan 2025, CNAE 692 (accounting, bookkeeping, audit and tax advice): **62,234 firms**:
  - 31,840 with no employees;
  - 19,098 with 1–2;
  - 6,557 with 3–5;
  - 2,785 with 6–9;
  - 1,599 with 10–19;
  - 239 with 20–49.

  So about **30,400 have employees** and **28,440 have 1–9 employees** [new: INE API table 73019, https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/73019?nult=1, seen 23 Oct 2026]. CNAE 691 (legal) adds 83,943 firms, some of them labour advisers.
- Practising gestores administrativos: **5,869**, of 7,466 colegiados at 31 Dec 2025, in 22 colegios. The largest are Cataluña (1,006 practising), Madrid (912), Valencia (476), Sevilla (453) and Galicia (432) [new: Consejo General de Colegios de Gestores Administrativos, Memoria 2025, https://www.consejogestores.org/wp-content/uploads/2026/03/Memoria-2025.pdf, Mar 2026].
- Graduados sociales: **17,000 colegiados** in 43 colegios [new: https://www.graduadosocial.org/, seen 23 Oct 2026].
- These groups overlap (many gestores and graduados sociales trade as CNAE 692 firms). A defensible target is **about 30,000 advisory firms with staff**.
- Ceiling: 5% × 30,000 × €40/month ≈ **€0.7M ARR**; 10% ≈ €1.4M.

**(d) Willingness to pay.**
- Adjacent spend:
  - CopilotGestoria from €15/month;
  - MsNotifica €40–120/month (see IDEA-07);
  - Fandit €56–600/month [notes: ADM-16];
  - suites (a3, Sage), prices not published.
- What gestorías pay for legal-update subscriptions was **not found** (Iberley and other pricing pages blocked automated access).
- The original €49–149/month band is above what the visible anchors support; €29–59/month is safer.
- The kill test stays open [I]: fewer than 1 in 5 would pay €30/month or more.

**(e) Distribution.**
- Concentrated professional bodies: the Consejo General de Gestores circulates update bulletins and publishes the draft calendar, and there are 22 colegios de gestores and 43 colegios de graduados sociales.
- Vendor partner programmes: Holded and Quipu. They would be wary of a vendor-neutral tool that exposes migrations.
- Webinars on the 2027–2028 calendar.
- None of these channels is proven for this product.

**(f) Build feasibility and legal constraints.**
- MVP in 1–2 months: CSV import, five rule modules, bulk email/WhatsApp, status feed.
- The tool acts as a GDPR data processor for the gestoría.
- No reserved profession is involved, because the gestoría stays the adviser. The tool gives "status, not advice".
- A tax specialist is needed for the editorial feed, as a recurring cost.
- a3 and Contasol export formats were not verified [F open].

**(g) Defensibility.** Low to medium:
- a dated, accountable rule-status feed;
- a maintained product-declaration database (there is no official list);
- client tags and history as switching cost;
- colegio relationships.

AI makes the summaries nearly free, and each suite vendor can add a readiness panel for its own clients. The cross-vendor position is the only structural edge.

**(h) Kill criteria.**
1. "a3 or Sage already shows cross-vendor readiness for all clients": **not met** (nothing found; single-vendor panels only).
2. Fewer than 1 in 5 interviewed gestorías would pay €30/month or more: **open [I].**
3. "A spreadsheet handles it in a couple of hours per change": **open [I].** TeamSystem's manual checklist suggests the spreadsheet is today's answer.
4. Fewer than 3 of 10 trial gestorías convert: **open [I].**

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | E-invoicing duties 12–24 months out (6 Oct 2027 and 2028); VeriFactu 2027 still in the BOE |
| S2 Buyers | 3 | About 30k advisory firms with staff |
| S3 WTP | 3 | Gestorías already pay €15–120/month for adjacent tools; no direct evidence for rule mapping |
| S4 Reachability | 3 | Colegios and bulletins exist; unproven for this product |
| S5 Competitive gap | 3 | Single-vendor panels and manual checklists; no cross-vendor tool found |
| S6 Build speed | 4 | MVP in 1–2 months |
| S7 Defensibility | 2 | Maintained rules and a product database, but copyable and bundle-able |
| S8 Retention | 3 | Periodic use through the 2027–2029 waves; risk of fading afterwards |

- **Sellability** 3.13. **P** 3: real staff-hours and client-penalty exposure; hours never measured [notes: TAX-23, PRO-10].
- **Overall** = 0.6 × 3.125 + 0.4 × 3 = **3.08**.
- The original broad version would score lower on S3, S5 and S7 because of the free-content risk.

**Open [I] checks.**
- 10–15 gestoría interviews: hours per rule change, how they track clients' software today, WTP at €30/month.
- Five-gestoría concierge pilot on the e-invoicing inventory.
- a3 and Contasol export test.

**What would change the verdict.**
- **To GO:** at least 3 of 10 trial gestorías pay €30/month or more, or a colegio agrees to co-brand.
- **To KILL:** a3 (Wolters Kluwer), TeamSystem or Sage ships a free cross-vendor readiness panel, or interviews show the spreadsheet takes under 2 hours per change.

#### IDEA-08: Hacienda letter shield (pre-filing cross-check and evidence pack) — KILL (medium)

**Validated definition.** A €7–12/month tool for B2C businesses that take cards or Bizum. Before each quarterly VAT and IRPF filing (modelos 303 and 130) it reconciles acquirer, POS and Bizum settlements against invoices and the draft bases. It explains gaps (refunds, tips, personal Bizum, third-party collections, exempt services) and assembles a response pack when a letter arrives.

The reporting rule is confirmed, but three things make a standalone product unattractive:
- there is no data on how often letters arrive;
- a large part of the named target segments cannot have a VAT-return mismatch at all;
- response handling is already bundled by online asesorías.

**(a) Problem reality and rule status.** Confirmed in the BOE; no election exposure.
- **RD 253/2025** of 1 April (BOE-A-2025-6599, 2 Apr 2025) reformulates RGAT art. 38 bis to cover "cualesquiera tipo de tarjetas así como los sistemas de cobro asociados a un número de teléfono móvil" (Bizum). Reporting moves "de ser anual a mensual, desapareciendo el umbral anual neto de 3.000 euros", with effect from 1 Jan 2026. A new art. 38 ter adds an annual report on all cards, excluding cards with under €25,000 a year of charges and credits [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-6599, seen 23 Oct 2026]. The €25,000 threshold that press pieces attach to Bizum belongs to the new modelo 174, not to modelo 170.
- **Orden HAC/747/2025** of 27 June (BOE-A-2025-14600, 15 Jul 2025) approves the monthly modelo 170 for operations of "empresarios o profesionales adheridos al sistema de gestión de cobros a través de cualquier tipo de tarjetas y mediante pagos asociados a números de teléfono móvil". The first return, for January 2026, was filed in February 2026 [new: https://www.boe.es/diario_boe/xml.php?id=BOE-A-2025-14600, seen 23 Oct 2026].
- **Letters.** "La AEAT ha empezado a remitir cartas de requerimiento" by mismatches appears only in press narration, with **no count and no official source** [new: Xataka Móvil, 19 Aug 2026, https://www.xatakamovil.com/movil-y-sociedad/hacienda-bizum-autonomos-envian-cartas-descuadres-pagos]; [notes: TAX-15] (AyE, 18 Aug 2026). Two searches found no AEAT or Gestha figure.
- **Structural limit (desk inference from the VAT regimes).** Mismatches between card data and the VAT return can only arise for businesses whose VAT return reflects actual sales:
  - retailers in recargo de equivalencia do not file 303 returns for those sales;
  - módulos businesses (many bars and taxis) pay VAT by modules;
  - dental and medical services are VAT-exempt.

  For these groups the card data feed income-tax and módulos-limit checks instead. That shrinks the segment named in the source to general-regime B2C firms in estimación directa, SLs, salons and restaurants outside módulos. This is an inference to verify with gestorías [I].

**(b) Competitors.**
- **Declarando Pro with filings (€69.90/month + VAT):** "Gestión de requerimientos de Hacienda (¡ganamos el 75%!)", plus bank connection and an "antisanciones" guarantee [new: https://declarando.es/precios, seen 23 Oct 2026].
- **Bank reconciliation** is standard in Holded, Quipu and Anfix [notes: TAX-07 software table]. CopilotGestoria cross-checks returns against each other (303 against 390, 111 against 190), but not against modelo 170 [new: https://copilotgestoria.com/, seen 23 Oct 2026].
- **Gestorías and Legálitas** handle letters inside their fees [notes: TAX-16].
- **Gap:** no tool found that explicitly reconciles acquirer and Bizum settlements against 303 bases with the five known causes. The gap is narrow, because bank-feed reconciliation already does most of it.

**(c) Buyers and market size.**
- 94% of small retail and hospitality businesses accept cards [notes: FIN-13].
- After removing recargo de equivalencia, módulos and exempt activities, the addressable group is probably 100k–500k firms (inference, no direct count).
- Ceiling at €10/month: 1% of 300k ≈ 3k × €120 ≈ €0.36M ARR.

**(d) Willingness to pay.** Owners pay for help after a letter arrives (asesoría fees, Declarando's requerimiento handling), not for prevention. A €20/quarter prevention price has no observed anchor.

**(e) Distribution.**
- Acquirers: SumUp has a developer platform, but no partner programme was checked.
- Gestorías: letters land on their desks.
- Associations of salons and restaurants.

None is proven.

**(f) Build feasibility.**
- SumUp's API lists transactions, refunds, payouts and receipts [new: https://developer.sumup.com/api/transactions/list and https://developer.sumup.com/api/payouts/list, seen 23 Oct 2026]. Stripe offers balance transactions and a payout-reconciliation report [new: https://docs.stripe.com/reports/payout-reconciliation, seen 23 Oct 2026].
- Bank-acquired (Redsys) terminals and Bizum-for-business collections are reachable only as bank-statement lines or merchant-portal exports. No public merchant API was found, so ingestion is CSV and manual.
- **Can taxpayers download what their bank reported in modelo 170?** Not established (1 search). If not, the tool rebuilds the figures from the same settlements, which is fine for matching but cannot show "what Hacienda sees".
- MVP: 1–2 months for CSV ingestion and a PDF pack.

**(g) Defensibility.** Low. Accounting suites own the bank feeds and invoices and can add a "card data vs 303" check. The AEAT matching know-how is thin and public.

**(h) Kill criteria.**
1. Letters reach under about 5% of B2C businesses a year: **open.** No count exists, and the structural limit above makes high frequency less likely.
2. Taxpayers cannot see the modelo 170 data their bank filed: **open, probably met** (no access route found).
3. Acquirer data cannot be had without manual work: **partly met.** APIs exist for SumUp and Stripe; for bank terminals and Bizum it is manual.

**Scores**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Monthly reporting in force since 1 Jan 2026, but letters are sporadic and uncounted |
| S2 Buyers | 4 | General-regime B2C firms taking cards, plausibly 100k–500k |
| S3 WTP | 2 | Prevention is not bought; response handling is bundled |
| S4 Reachability | 2 | Diffuse micro B2C; acquirer and gestoría channels unproven |
| S5 Competitive gap | 3 | Bank reconciliation exists; no explicit modelo 170 matcher |
| S6 Build speed | 3 | Integration-heavy for bank terminals and Bizum (CSV only) |
| S7 Defensibility | 2 | Suites can copy it |
| S8 Retention | 3 | Quarterly use |

- **Sellability** 2.75. **P** 3: requerimiento non-response fines of €250–600 and possible reassessments, frequency unknown [notes: TAX-10].
- **Overall** = 0.6 × 2.75 + 0.4 × 3 = **2.85**.

**Open [I] checks.**
- Ask 10 gestorías how many card or Bizum requerimientos they handled in 2026, and the hours each took.
- Confirm whether the AEAT "datos fiscales" show modelo 170 amounts to the taxpayer.
- Validate which client types actually get 303-mismatch letters.

**What would change the verdict.**
- AEAT or Gestha data showing letters to more than 5% of general-regime B2C firms a year.
- An acquirer (SumUp, Revolut Business, a bank) willing to embed the check as a merchant feature and pay per merchant.

Either would support a RESHAPE to a white-label module for acquirers or gestorías.

#### IDEA-10: SL director guard (dissolution-trigger and accounts-deposit alerts) — RESHAPE (medium-low)

**Validated definition (after reshape).** A gestoría-run **director-duty screener** rather than a €5/month owner app. Each quarter it bulk-imports trial balances for all of a gestoría's SL clients (a3, Contasol, Holded or Quipu exports, or CSV). It then:
- computes net equity *for dissolution purposes* against half the share capital;
- flags clients that crossed the line, including SLs whose 2020–2021 losses stopped being excluded after the financial year starting in 2024;
- generates a dated warning letter to the directors and a meeting-notice template reviewed by a commercial lawyer;
- logs the two-month clock (convene the meeting, or file for insolvency or restructuring talks);
- tracks the annual-accounts deposit (one month after approval; registry closure; ICAC fines).

Price: €19–39/month per gestoría, or €0.50–1 per SL in bulk, possibly as a module of IDEA-06. Owners can get a read-only alert.

**(a) Problem reality and rule status.** In force; not exposed to the election.
- LSC art. 363.1.e: a company must dissolve "por pérdidas que dejen reducido el patrimonio neto a una cantidad inferior a la mitad del capital social". Art. 365.1: directors must convene the general meeting "en el plazo de dos meses".
- Art. 367.1: directors who miss this "responderán solidariamente de las obligaciones sociales posteriores al acaecimiento de la causa de disolución". Art. 367.2: "Salvo prueba en contrario", claimed debts "se presumirán de fecha posterior". Art. 367.3: filing for insolvency or communicating restructuring talks within two months gives a safe harbour [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2010-10544/texto/bloque/a363, /a365, /a366, /a367, seen 23 Oct 2026].

  The burden of proof sits on the director, which is exactly why a dated evidence log has value.
- **New why-now not in the notes.** Ley 3/2020 art. 13, as last amended by RDL 20/2022, excluded 2020 and 2021 losses from the art. 363.1.e test only "hasta el cierre del ejercicio que se inicie en el año 2024" [new: https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2020-10923/texto/bloque/a1-5, consolidated, seen 23 Oct 2026]. From the 2025 accounts, closed on 31 Dec 2025 and approved in 2026, those losses count again. SLs that survived on the exclusion may now be inside the dissolution cause without knowing it. How many is unknown.
- **STS 1477/2026** (single press source). The court reportedly held that "corregir tarde las pérdidas no elimina esa responsabilidad" and that "desconocer una deuda concreta no da al administrador un nuevo plazo de dos meses". The claim was €42,000. Experts advise owners to ask their accounting firm for "an explicit alert on equity balance and cash position" [new: AyE, 23 Oct 2026, https://www.autonomosyemprendedor.es/articulo/pymes/supremo-confirma-que-autonomos-societarios-pueden-asumir-deudas-sl-actuan-tiempo/20261022150439056494.html]. The ruling's date, chamber and ECLI were not given; CENDOJ was not checked.
- **Accounts deposit.** LSC arts. 279, 282 and 283: deposit within a month, registry closure, ICAC fines of €1,200–60,000 [notes: TAX-21]. The registry sheet closes one year after the year-end without a deposit [new: search summary of https://www.economistjurist.es/noticias-juridicas/el-cierre-registral-de-las-sociedades-mercantiles-que-es-cuales-son-sus-consecuencias-y-como-solucionarlo].
- **Calculation nuance.** Net equity for dissolution purposes includes adjustments, for example participative loans and ICAC criteria [new: search summary of BOICAC 136 commentary, https://primeralecturaediciones.com/documentos_diana/cursos/2025/CIERRE_2024/RESUMENES_BOICAC/BOICAC%20136_5.pdf]. A naive ratio is wrong in edge cases, which is a small rules moat.

**(b) Competitors.** No accounting suite or asesoría tool advertising a half-capital or dissolution alert was found (1 search covering a3, Sage, Holded and Contasol). Today the check is done by gestorías at year-end closing, "when they notice" [notes: FIN-17], or by lawyers. Any accounting vendor could add the ratio.

**(c) Buyers and market size.**
- **SLs:** INE DIRCE 2025 counts **1,127,515 SLs**: 334,941 with no employees, 398,349 with 1–2, 180,169 with 3–5 and 94,717 with 6–9. About 1.0M have fewer than 10 employees [new: INE table 73018, seen 23 Oct 2026].
- **Insolvency context:** SLs are 93.2% of company insolvencies [notes: FIN-17]; 1,427 micro-firm insolvency procedures and 2,656 "sin masa" insolvencies were concluded in 2025 [new: Registradores, Anuario concursal 2025, https://www.registradores.org/documents/d/guest/anuario-concursal-2025, seen 23 Oct 2026]. Counts of art. 367 liability claims and of SLs that fail to deposit accounts were **not found** (1 search).
- **Reshaped buyer:** about 30k advisory firms with staff (see IDEA-06). At €29/month, 5% ≈ €0.5M ARR. At €0.75 per SL in bulk, 5% of SLs ≈ €0.5M ARR.

**(d) Willingness to pay.** No direct anchor. The adjacent spend is accounting services at €59.95–129/month for SLs [notes: TAX-21]. The gestoría's own professional-liability exposure, if it fails to warn a client, is the likely motive, but it was not evidenced [I].

**(e) Distribution.**
- Asesorías, which hold the books.
- Colegios de gestores and economistas.
- Accounting-software marketplaces (Holded and Quipu partner programmes).
- D&O insurers and brokers (speculative).

**(f) Build feasibility.**
- Low complexity: trial-balance CSV import, ratio logic with ICAC adjustments, templates, audit log. MVP in 3–6 weeks.
- The templates need commercial-lawyer review. Output must be "information, not legal advice"; advice on insolvency strategy stays with lawyers.
- No certification is needed; the GDPR processor role applies.

**(g) Defensibility.** Weak. Any suite can add the ratio. The edge is the evidence trail (dated letters, meeting-notice templates, the deposit calendar), cross-vendor bulk import, and bundling with IDEA-06.

**(h) Kill criteria.**
1. The main suites already alert on the half-capital trigger: **not met** (none found).
2. Asesorías will not distribute it: **open [I].**
3. Behavioural risk that owners of struggling SLs ignore alerts: unresolved. The reshape moves the alert to the gestoría, which has an incentive to document its warning.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 4 | Enforced duty with personal liability; 2020–21 losses count again from the 2025 accounts |
| S2 Buyers | 3 | About 30k gestorías as buyers; 1.13M SLs underneath |
| S3 WTP | 2 | No observed spend; motive is liability protection |
| S4 Reachability | 3 | Asesoría channel concentrated but unproven |
| S5 Competitive gap | 4 | Only manual, gestoría or lawyer options found |
| S6 Build speed | 4 | MVP in about 1 month, plus legal review |
| S7 Defensibility | 1 | Trivially addable by accounting vendors |
| S8 Retention | 3 | Quarterly screening plus the annual deposit cycle |

- **Sellability** 3.00. **P** 4: personal liability for company debts is existential for owner-managers, and art. 367.2 puts the burden on them; frequency unquantified.
- **Overall** = 0.6 × 3.0 + 0.4 × 4 = **3.40**.
- The original €5/month owner app scores about S3 1 and S4 2 for a Sellability of about 2.75.

**Open [I] checks.**
- Would 10 asesorías run a quarterly bulk screen, and pay €19–39/month?
- How many SL clients per gestoría are near the line, especially after the 2020–21 reactivation?
- Read STS 1477/2026 in CENDOJ.

**What would change the verdict.**
- **To GO:** gestorías say they already face client claims for not warning, or a D&O insurer wants it as a risk-reduction perk.
- **To KILL:** a3, Sage or Holded ship the alert, or gestorías say they check it at year-end anyway and see no value in quarterly screening.

#### IDEA-25: Pre-lease "can I open here?" check and file builder (Madrid first) — RESHAPE (low)

**Validated definition (after reshape).** A **B2B address pre-screen for people who place businesses into premises**: commercial estate agents, franchise expansion managers and the listing teams of portals, starting in Madrid. For an address plus an activity it returns:
- the planning zone and its use rules (PGOUM norma zonal, plus special plans and acoustic-protection zones; these two layers are background knowledge, not verified here);
- the licensed-activity history of the premises, from the council's open census of premises and licences;
- the likely procedure (declaración responsable or licence), the regulated ECU price and the standard timelines;
- a "needs technician" flag, with a paid referral to an ECU or architect.

Every answer is reviewed by a planning professional during the MVP. The subscription is €99–199/month for 10–30 checks. The €49 one-off check for first-time entrepreneurs is **dropped as a lead product**: it is a one-off purchase with diffuse buyers, so acquisition is expensive.

**(a) Problem reality and rule status.**
- Madrid's service charter (last evaluated 24 Feb 2026) confirms:
  - 13,301 declaraciones responsables and licences, 3,805 inspections and 22,695 people served in 2025;
  - standards (targets, not results) of an average 109 days to check a declaración responsable (40% within 90 days) and 137 days for a licence (40% within 60 days);
  - a paid "Consulta urbanística común y especial para actividades";
  - the 4% ICIO tax.

  Results against the standards are published separately on madrid.es ("Cartas de Servicios"), and **the 2025 results were not retrieved** [new: https://www.madrid.es/UnidadesDescentralizadas/Calidad/CARTAS%20SERVICIOS/SistemaCartasServicio/41%20CS_de%20la%20Agencia%20de%20Actividades/DEFINITIVA/CS_ADA_2026.pdf, read via WebFetch, 23 Oct 2026].
- Municipal rules are not exposed to the election. Not verified here: the 2027 ECU prices approved on 15 Oct 2026 [notes: ADM-01] and the status of València's 2025 draft ordinance, which is unknown.

**(b) Competitors.**
- **Technicians:** viability studies "around 300 €" for a change of use (Habitissimo guide). Technicians on Certicalia offer no-commitment assessments whose fee is deducted if they are later hired for the project. That is lead-generation-like, but not free [new: search summaries of https://www.habitissimo.es/presupuestos/estudio-viabilidad and https://www.certicalia.com/preguntas/p/convertir-local-en-vivienda-en-madrid-18478, 2026].
- **ECUs** (19 in Madrid; e.g. SGS): €500–1,000 for an urban-compatibility certificate [notes: ADM-01]. No ECU was found offering a free pre-check (1 search).
- **The council's paid consulta urbanística:** fee and turnaround not retrieved. Madrid also publishes past planning consultations, e.g. CU 27-18 [new: https://transparencia.madrid.es/UnidadesDescentralizadas/UDCUrbanismo/Consultas Urbanisticas/2018/CU 27-18.pdf, search summary]. They are a free interpretive corpus a product could use, and that users can read themselves.
- **Málaga's free ALU assistant** [notes: ADM-03].
- No online "can I open X at address Y" product for Madrid was found (2 searches).

**(c) Buyers and market size.**
- Madrid: about 13,300 files a year (charter).
- The reshaped buyer (commercial agents, franchise teams) was not counted [I].
- Ceiling for Madrid: 300 agents and teams × €150/month ≈ €0.54M ARR. Each extra city needs its own rules work.

**(d) Willingness to pay.**
- Openers already pay €300 for a technician's viability study, €500–1,000 for an ECU certificate, and €600–1,250+ for an ECU-managed declaración responsable [notes: ADM-01].
- A €49–149 pre-screen sits well under these anchors, but is less authoritative.
- Agents' willingness to pay is unevidenced [I].

**(e) Distribution.**
- Commercial agents and portals.
- Franchise associations.
- ECU and architect referral fees, both ways.
- High-intent searches ("qué licencia necesito para abrir un bar en Madrid"); demand not measured.

**(f) Build feasibility and legal constraints (settles the data-availability kill test for Madrid).**
- Madrid's Geoportal lists "Planeamiento Urbanístico" among its services [new: https://geoportal.madrid.es/IDEAM_WBGEOPORTAL/index.iam, seen 23 Oct 2026]. Services follow OGC standards (WMS, WFS) and data can be downloaded as shapefiles under a commercial-reuse licence. The PGOUM97 building-conditions plan is catalogued as open vector data [new: search summaries of the Ayuntamiento's JIIDE 2019 Geoportal presentations, https://idee.es/resources/presentaciones/JIIDE19/28-JIIDE2019_Ayuntamiento_Madrid_Geoportal.pdf].
- The charter says datos.madrid.es publishes granted licences, declaraciones responsables, the census of premises and activities, and the ECU list "en formatos reutilizables". The portal was "En mantenimiento" on 23 Oct 2026.
- **What is missing:** the *use-compatibility rules* themselves (the PGOUM normative text, and any special plans or acoustic-zone rules) are legal text, not data. They must be encoded and maintained by hand. That is the main build cost (2–4 months for Madrid's top 20 activities, with professional review), and also the moat.
- Barcelona, València, Sevilla and Málaga data were **not checked**.
- **Liability:** a wrong "allowed" verdict can cost a lease and fit-out. The product needs clear disclaimers, review by a técnico competente and professional-liability insurance. Binding certification stays with ECUs and the council.

**(g) Defensibility.** Moderate: a city-by-city encoded rules set plus a licence-history join, reviewer network and ECU partnerships. AI lowers the cost of a first draft, not of a legally reviewed answer. Each city is slow to model.

**(h) Kill criteria.**
1. "Madrid's planning data cannot be obtained in usable form": **not met.** GIS layers and licence and premises data are open; the rules must be hand-encoded.
2. "ECUs or architects answer free as lead generation": **partly met.** Some technicians offer no-commitment assessments credited against later fees; no free ECU pre-check was found.

**Scores (reshaped version)**

| Criterion | Score | Justification |
|---|---|---|
| S1 Urgency | 3 | Strong recurring pain for placement teams; no legal deadline |
| S2 Buyers | 2 | Madrid agents and franchise teams, likely 5k–20k at most |
| S3 WTP | 3 | Openers pay €300–1,000 for adjacent services; agents' spend unknown |
| S4 Reachability | 3 | Agents and portals are concentrated but unproven |
| S5 Competitive gap | 4 | Only technicians, ECUs and the paid council consultation |
| S6 Build speed | 3 | 2–4 months of rules encoding, plus review and insurance |
| S7 Defensibility | 3 | Encoded city rules plus reviewer network |
| S8 Retention | 3 | Subscription for repeat placers |

- **Sellability** 3.00. **P** 3: months of rent and fit-out at risk per wrong premises; scale unquantified [notes: ADM-03].
- **Overall** = 0.6 × 3.0 + 0.4 × 3 = **3.00**.
- The original B2C €49 check scores lower: S2 2, S4 2, S8 1, giving a Sellability of about 2.75 and an Overall of about 2.85.

**Open [I] checks.**
- Will 10 Madrid commercial agents or franchise teams pay €99–199/month?
- Madrid's 2025 results against its charter standards.
- The consulta urbanística fee and turnaround.
- Whether ECUs will pay referral fees.
- Data and rules in Barcelona, València, Sevilla and Málaga.

**What would change the verdict.**
- **To GO:** a portal or franchise network commits to a pilot, or measured search demand is high.
- **To KILL:** Madrid launches a free ALU-style assistant, or reviewers cannot keep turnaround under 48 hours at a viable cost.

