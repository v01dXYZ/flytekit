
from flytekit.pattern.cloud_pickle_resolver import CloudPickleResolver
from flytekit import task, workflow


class PickleBuilder(object):
    def __init__(self):
        self.do_fn = None

    def set_do_fn(self, do_fn):
        self.do_fn = do_fn
        return self

    def build(self):
        @task(task_resolver=CloudPickleResolver)
        def my_task_fn(project: str) -> str:
            return self.do_fn(project)

        # Hash or something to create a unique name
        my_task_fn._name = f"my_task_fn_random"

        @workflow
        def my_wf(project: str):
            my_task_fn(project=project)

        return my_wf
