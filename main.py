tasks = [
    {"name": "Logic League Submission", "days_left": 1, "complexity": 5},
    {"name": "Maths Assignment", "days_left": 3, "complexity": 3},
    {"name": "C++ Revision", "days_left": 5, "complexity": 2}
]

def display_tasks():
    tasks.sort(key=lambda x: x['complexity'] / max(x['days_left'], 1), reverse=True)
    print("\n🚀 LogicFlow: Smart Task Prioritizer")
    print("-" * 45)
    for i, task in enumerate(tasks, 1):
        score = task['complexity'] / max(task['days_left'], 1)
        print(f"{i}. [Priority Score: {score:.1f}] {task['name']} (Due: {task['days_left']} days)")

if __name__ == "__main__":
    display_tasks()
