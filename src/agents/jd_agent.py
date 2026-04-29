def parse_jd(text:str):
    kws=['Python','API','MySQL','Linux','Flask']
    return [k for k in kws if k.lower() in text.lower()]
