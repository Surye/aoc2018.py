import re

day = 7

class Step:
    def __init__(self, name):
        self.name = name
        self.pre = []
        self.done = False
        self.time_elapsed = 0
        self.assigned = False

    def __repr__(self):
        return self.name

    def ready(self):
        if self.done:
            return False
        for step in self.pre:
            if not step.done:
                return False

        return True


def build_graph(data):
    steps = {}
    for line in data:  # Build graph
        m = re.match(r"Step (?P<pre>[A-Z]) must be finished before step (?P<post>[A-Z]) can begin.", line)
        pre = m['pre']
        post = m['post']

        if pre not in steps:
            steps[pre] = Step(pre)
        if post not in steps:
            steps[post] = Step(post)

        steps[post].pre.append(steps[pre])
    return steps


def algo1(data):
    steps = build_graph(data)

    order = []

    while len(order) != len(steps.values()):
        step = min([step.name for step in steps.values() if step.ready()])
        order.append(step)
        steps[step].done = True

    return ''.join(order)


def algo2(data, base_time, num_workers):
    steps = build_graph(data)
    total_seconds = 0
    done = []

    workers = {}
    for i in range(num_workers):
        workers[i] = None

    while True:
        steps_ready = [step for step in steps.values() if step.ready()]
        if len(steps_ready) == 0:
            break

        jobs_to_run = [step for step in sorted(steps_ready, key=lambda x: x.name) if not step.assigned]

        for worker_id, job in workers.items():
            if job == None:
                try:
                    job = jobs_to_run.pop(0)
                    job.assigned = True
                except IndexError:
                    continue
                workers[worker_id] = job

            if job.time_elapsed == (base_time + ord(job.name) - ord('A')):
                job.done = True
                done.append(job.name)
                workers[worker_id] = None
            else:
                job.time_elapsed += 1

        total_seconds += 1
        #print(f"{total_seconds: >4} {workers[0] or '.'} {workers[1] or '.'} {''.join(done)}")


    return total_seconds


if __name__ == "__main__":
    test1_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]
    test1_answer = 'CABDFE'
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = test1_input
    test2_answer = 15
    if algo2(test2_input, 0, 2) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data, 60, 5))
