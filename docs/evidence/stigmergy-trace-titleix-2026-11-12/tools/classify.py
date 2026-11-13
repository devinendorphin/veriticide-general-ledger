import json,sys,collections
R=[r for r in json.load(open(sys.argv[1])) if r["cat"]=="none"]
# Claude's reading of each non-federal cluster, keyed by text prefix. Categories:
# BOILER = names of laws, contact details, generic notices/aspirations; FEDSOFT = federal wording or federal guidance edited past the matcher;
# PROC = procedural drafting choices; SUBST = substantive definitions of prohibited conduct / consent.
K={"in evaluating whether coercion":"SUBST","a decision not to participate":"SUBST","university policy and can be subject":"BOILER",
"consent to engage in sexual activity with one":"SUBST","purpose of sexual degradation":"SUBST","any person or group within":"BOILER",
"retaliation is subject to a separate":"PROC","to comply with title ix":"BOILER","allowing others to view":"SUBST","consent of all parties involved engaging":"SUBST",
"for any purpose including sexual":"SUBST","from the perspective of a reasonable":"FEDSOFT","800 421":"BOILER","based on an assessment of whether the previous":"PROC",
"law with respect to alcohol":"SUBST","consent cannot be assumed":"SUBST","unable to understand the facts":"SUBST","faculty member university official":"BOILER",
"employees and other members":"BOILER","reasonably believes that the actor":"SUBST","in fear of death":"SUBST","consent cannot be coerced":"SUBST",
"an individuals status in":"BOILER","respondent is not a member":"PROC","when there is not enough":"PROC","is initiated including when":"PROC",
"subjective belief that behavior":"FEDSOFT","the context nature scope":"FEDSOFT","resolution if a complaint is later":"PROC","notify the other party":"PROC",
"the jeanne clery":"BOILER","vii of the civil rights":"BOILER","all members of the university community are expected":"BOILER",
"this policy defines expectations":"BOILER","consent e g to understand":"SUBST","harassment and sexual misconduct preventing":"FEDSOFT",
"members of the university community have the right":"BOILER","including third parties when":"PROC","cannot make rational":"SUBST",
"complainant does not wish":"PROC","names of additional witnesses":"PROC","the availability of information":"PROC","discuss any technology":"PROC",
"repairing harm to the extent":"PROC","including the number of witnesses":"PROC","who has no affiliation":"PROC","the department of educations":"BOILER",
"unreasonably interferes with":"FEDSOFT","a an employee of the university":"FEDSOFT","this means that the investigation":"BOILER",
"sanctions imposed on the respondent":"PROC","university is committed to fostering":"BOILER","consent can be given by words":"SUBST"}
out=collections.defaultdict(lambda:{"clusters":0,"words":0,"pairs":collections.Counter()}); miss=[]
for r in R:
    c=[v for k,v in K.items() if r["text"].startswith(k)]
    if len(c)!=1: miss.append(r["text"][:60]); continue
    o=out[c[0]]; o["clusters"]+=1; o["words"]+=r["words"]; o["pairs"]["+".join(r["schools"])]+=r["words"]
print("unmatched:",miss)
res={k:{"clusters":v["clusters"],"words":v["words"],"by_schools":dict(v["pairs"].most_common())} for k,v in out.items()}
json.dump(res,open(sys.argv[2],"w"),indent=1); print(json.dumps(res,indent=1))
