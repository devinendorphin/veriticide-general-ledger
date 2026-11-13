# Sources (retrieved 2026-11-12 from this container; hashes in SOURCES.sha256)

Policy texts are not stored here: they are public documents on the universities' own sites, re-fetchable at
these URLs. A changed hash on re-fetch means the document changed.

| School | Document | URL |
|---|---|---|
| Illinois | HR-79, rev. 2026-04-16 | https://policies.illinois.edu/ (policy hr-79) |
| Indiana | UA-03 Discrimination, Harassment, and Sexual Misconduct | https://policies.iu.edu/ (UA-03) |
| Iowa | Operations Manual ch. 4, Sexual Harassment and Sexual Misconduct (rev. 2025-07-01) | https://policy.uiowa.edu/community-policies/sexual-harassment-and-sexual-misconduct |
| Michigan | Employee Procedures, eff. 2025-09-02 (*procedures*, not the policy) | ECRT site PDF |
| Minnesota | Board of Regents policy, amended 2020-07-30 | https://regents.umn.edu/sites/regents.umn.edu/files/2024-05/policy_sexual_harassment_sexual_assault_stalking_and_relationship_violence.pdf |
| Nebraska | RP-2.1.8 Sexual Misconduct Policy | https://docs.nebraska.edu/unop/docs/Board%20of%20Regents/Policies/policies/rp-218--sexual-misconduct-policy.pdf |
| Northwestern | Policy on Discrimination, Harassment, and Sexual Misconduct 2025–26 | https://www.northwestern.edu/civil-rights-office/policies-procedures/policies/policy_on_discrimination_harassment_and_sexual_misconduct_2025-2026_final.pdf |
| Ohio State | Non-Discrimination, Harassment, and Sexual Misconduct (file dated 2026-05) | https://policies.osu.edu/sites/default/files/documents/2026/05/Policy-NDH-Sexual-Misconduct.pdf |
| Rutgers | 60.1.33 Title IX Policy and Grievance Procedures, version 2021-12-07 (currency not verified) | https://uec.rutgers.edu/wp-content/uploads/60.1.33_Title-IX-Policy-and-Grievance-Procedures_version12072021.pdf |
| Washington | Executive Order 81 | https://policy.uw.edu/directory/po/executive-orders/eo-81-prohibiting-discrimination-harassment-and-sexual-misconduct/ |

Federal text: `https://www.ecfr.gov/api/versioner/v1/full/<date>/title-<n>.xml?part=<p>[&subpart=|&section=]`
— 34 CFR 106 at 2024-07-15 and 2025-06-01; 34 CFR 668 Subpart D at 2025-06-01; 29 CFR 1604.11 at 2025-06-01.

Scripts in `tools/` (run with `python3 -I`): `totext.py` (PDF/HTML → text), `trace.py` (as-registered pass,
level A), `trace2.py` (levels A/B/C per Deviation 1), `attrib.py` (loose 6-word source tracing of level-C
clusters), `classify.py` (Claude's category reading of the non-federal clusters; the reading is in the script).
