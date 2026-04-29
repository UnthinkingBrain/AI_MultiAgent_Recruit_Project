from app.agents.planner import plan_task
from app.agents.research import research_task
from app.agents.writer import write_task
from app.agents.reviewer import review_task

def run_demo():
    task='为新品手机生成营销推广方案'
    plan=plan_task(task)
    info=research_task(plan)
    draft=write_task(info)
    final=review_task(draft)
    print('任务:',task)
    print('规划:',plan)
    print('研究:',info)
    print('初稿:',draft)
    print('终稿:',final)
