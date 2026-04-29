from src.agents.jd_agent import parse_jd
from src.agents.resume_agent import score_resume
from src.agents.interview_agent import build_questions

def run_demo():
    jd='Python后端开发，熟悉API、MySQL、Linux'
    resume='熟悉Python、Flask、MySQL，具备Linux部署经验'
    tags=parse_jd(jd)
    score=score_resume(tags,resume)
    qs=build_questions(tags)
    print('岗位标签:',tags)
    print('匹配分:',score)
    print('面试题:',qs)
