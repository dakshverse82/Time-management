# planner.py - simple task manager & pomodoro scheduler

tasks = []
PRIO = {1: "High", 2: "Med", 3: "Low"}


def fmt(m):
    """Convert total minutes to HH:MM format."""
    return f"{(m // 60) % 24:02d}:{m % 60:02d}"


def num(prompt, lo, hi):
    """Prompt until a valid integer in [lo, hi] is entered."""
    while True:
        v = input(prompt).strip()
        if v.isdigit() and lo <= int(v) <= hi:
            return int(v)
        print(f"  Enter a number between {lo} and {hi}.")


def add_task():
    name = input("Task name: ").strip()
    if not name:
        return print("  Name can't be empty.")

    p = num("Priority (1=High, 2=Med, 3=Low): ", 1, 3)
    m = num("Minutes needed (5-600): ", 5, 600)
    d = num("Days until due (0=today): ", 0, 365)

    tasks.append({"name": name, "p": p, "m": m, "d": d, "done": False})
    print(f"  Added '{name}'!")


def get_sorted():
    return sorted(tasks, key=lambda x: (x["d"], x["p"]))


def show_tasks():
    if not tasks:
        return print("\nNo tasks saved yet.")

    print(f"\n{'#':<3} {'Task':<20} {'Prio':<8} {'Mins':<6} {'Due':<8} Status")
    print("-" * 55)
    for i, t in enumerate(get_sorted(), 1):
        st = "Done" if t["done"] else "Pending"
        print(
            f"{i:<3} {t['name'][:18]:<20} {PRIO[t['p']]:<8} {t['m']:<6} {t['d']:<8} {st}"
        )


def finish_task():
    pending = [t for t in get_sorted() if not t["done"]]
    if not pending:
        return print("\nAll caught up! No pending tasks.")

    print("\nPending tasks:")
    for i, t in enumerate(pending, 1):
        print(f"  {i}. {t['name']}")

    idx = num("Which one did you finish? ", 1, len(pending)) - 1
    pending[idx]["done"] = True
    print(f"  Nice! Marked '{pending[idx]['name']}' as done.")


def make_schedule():
    pending = [t for t in get_sorted() if not t["done"]]
    if not pending:
        return print("\nNo pending tasks to schedule.")

    h = num("Start hour (0-23): ", 0, 23)
    m = num("Start minute (0-59): ", 0, 59)
    now = h * 60 + m

    print("\n--- Work Plan (25m focus + 5m break) ---")
    for t in pending:
        left = t["m"]
        while left > 0:
            step = min(25, left)
            print(f"{fmt(now)} - {fmt(now + step)} | Focus: {t['name']}")
            now += step
            left -= step

            if left > 0 or t is not pending[-1]:
                print(f"{fmt(now)} - {fmt(now + 5)} | Break")
                now += 5

    print(f"--- Finished around {fmt(now)} ---")


def show_stats():
    if not tasks:
        return print("\nNo task data yet.")

    tot = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    tot_m = sum(t["m"] for t in tasks)
    done_m = sum(t["m"] for t in tasks if t["done"])

    pct = (done * 100) // tot
    bar = "#" * (pct // 5) + "-" * (20 - (pct // 5))

    print(f"\nProgress: {done}/{tot} tasks ({pct}%)")
    print(f"Time    : {done_m}m done | {tot_m - done_m}m remaining")
    print(f"Bar     : [{bar}]")

    if pct == 100:
        print("All done for today! 🎉")
    elif pct >= 50:
        print("Over halfway there!")
    else:
        print("Keep going! Knock out high priority items first.")


def main():
    print("=== Daily Planner ===")
    menu = {
        "1": add_task,
        "2": show_tasks,
        "3": make_schedule,
        "4": finish_task,
        "5": show_stats,
    }

    while True:
        print(
            "\n1. Add task  2. View tasks  3. Schedule day"
            "\n4. Mark done 5. Progress     6. Exit"
        )
        opt = input("Choice: ").strip()

        if opt == "6":
            print("See ya later!")
            break
        elif opt in menu:
            menu[opt]()
        else:
            print("  Invalid choice, try 1-6.")


if __name__ == "__main__":
    main()

print("made by : Devanshu Daksha")
print("Vit bhopal university")