def score_resume(tags,resume):
    hit=sum(1 for t in tags if t.lower() in resume.lower())
    return round(hit/max(len(tags),1)*100,2)
