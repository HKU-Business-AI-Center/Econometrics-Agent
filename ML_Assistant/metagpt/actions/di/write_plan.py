# -*- encoding: utf-8 -*-
"""
@Date    :   2023/11/20 11:24:03
@Author  :   orange-crow
@File    :   plan.py
"""
from __future__ import annotations

import json
from copy import deepcopy
from typing import Tuple

from metagpt.actions import Action
from metagpt.logs import logger
from metagpt.schema import Message, Plan, Task
from metagpt.strategy.task_type import TaskType
from metagpt.utils.common import CodeParser


class WritePlan(Action):
    PROMPT_TEMPLATE: str = """
    # Context:
    {context}
    # Available Task Types:
    {task_type_desc}
    # Task:
    Based on the context, write a plan or modify an existing plan of what you should do to achieve the goal. A plan consists of one to {max_tasks} tasks.
    If you are modifying an existing plan, carefully follow the instruction, don't make unnecessary changes. Give the whole plan unless instructed to modify only one task of the plan.
    If you encounter errors on the current task, revise and output the current single task only.
    
    Output a list of jsons following the format:
    ```json
    [
        {{
            "task_id": str = "unique identifier for a task in plan, can be an ordinal",
            "dependent_task_ids": list[str] = "ids of tasks prerequisite to this task",
            "instruction": "what you should do in this task, one short phrase or sentence",
            "task_type": "type of this task, should be one of Available Task Types",
        }},
        ...
    ]
    ```
    """

    PROMPT_TEMPLATE_NEW_ROUND: str = """
        # Context:
        {context}
        # Available Task Types:
        {task_type_desc}
        # Task:
        Previous Context, Previous Plan, and Previous Task in the context are the execution plans, corresponding codes, and results based on the User Previous Requirement. 
        Now you need to give a new plan based on the User New Requirement, and the new plan is based on the previous plan to make additions or modifications. 
        If the User New Requirement is a new requirement based on the User Previous Requirement, you need to add a subsequent plan based on the last task of the previous plan. Note that the new "task_id" and "dependent_task_ids" inherit the last "task_id" and "dependent_task_ids" of the Previous Plan. Please output the complete plan after the new requirement is added, please keep the previous plan content, and do not change the previous plan content. 
        If the User New Requirement is a change based on the User Previous Requirement, please keep the reusable part of the previous plan, and continue to make a new plan after the reusable plan. Please output the content of the reusable plan and the complete plan after the change.
        Output a list of jsons following the format(Only output "task_id", "dependent_task_ids", "instruction", "task_type" of the new task):
        ```json
        [
            {{
                "task_id": str = "unique identifier for a task in plan, can be an ordinal",
                "dependent_task_ids": list[str] = "ids of tasks prerequisite to this task",
                "instruction": "what you should do in this task, one short phrase or sentence",
                "task_type": "type of this task, should be one of Available Task Types",
            }},
            ...
        ]
        ```
        """

    async def run(self, context: list[Message], max_tasks: int = 6) -> str:
        task_type_desc = "\n".join([f"- **{tt.type_name}**: {tt.value.desc}" for tt in TaskType])
        prompt = self.PROMPT_TEMPLATE.format(
            context="\n".join([str(ct) for ct in context]), max_tasks=max_tasks, task_type_desc=task_type_desc
        )
        rsp = await self._aask(prompt)
        rsp = CodeParser.parse_code(block=None, text=rsp)
        return rsp

    async def run_new_round_plan(self, context: list[Message], max_tasks: int = 6) -> str:
        task_type_desc = "\n".join([f"- **{tt.type_name}**: {tt.value.desc}" for tt in TaskType])
        prompt = self.PROMPT_TEMPLATE_NEW_ROUND.format(
            context="\n".join([str(ct) for ct in context]), max_tasks=max_tasks, task_type_desc=task_type_desc
        )
        rsp = await self._aask(prompt)
        rsp = CodeParser.parse_code(block=None, text=rsp)
        return rsp


def update_plan_from_rsp(rsp: str, current_plan: Plan):
    rsp = json.loads(rsp)
    tasks = [Task(**task_config) for task_config in rsp]

    if len(tasks) == 1 or tasks[0].dependent_task_ids:
        if tasks[0].dependent_task_ids and len(tasks) > 1:
            # tasks[0].dependent_task_ids means the generated tasks are not a complete plan
            # for they depend on tasks in the current plan, in this case, we only support updating one task each time
            logger.warning(
                "Current plan will take only the first generated task if the generated tasks are not a complete plan"
            )
            # current_plan.add_tasks(tasks)
        # handle a single task
        if current_plan.has_task_id(tasks[0].task_id):
            # replace an existing task
            current_plan.replace_task(tasks[0])
        else:
            # append one task
            current_plan.append_task(tasks[0])

    else:
        # add tasks in general
        current_plan.add_tasks(tasks)


def precheck_update_plan_from_rsp(rsp: str, current_plan: Plan) -> Tuple[bool, str]:
    temp_plan = deepcopy(current_plan)
    try:
        update_plan_from_rsp(rsp, temp_plan)
        return True, ""
    except Exception as e:
        return False, e
