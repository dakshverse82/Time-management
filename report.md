# Time Management: A Python Task Planner and Pomodoro Scheduler

**Project Report**

Submitted by: Devanshu Daksha
Institution: VIT Bhopal University
Language used: Python 3

---

## Abstract

This report describes Time Management, a small command-line application written in Python that helps a person plan their day. The user enters tasks along with a priority, an estimated time and a due date. The program sorts the tasks by urgency, builds a timetable using the Pomodoro technique (25 minutes of work followed by a 5 minute break), and keeps track of how much work has been finished. The whole program uses only the Python standard library and runs in a normal terminal.

## 1. Introduction

Students usually have several things to handle at the same time: assignments, lab work, exam preparation and personal projects. The difficulty is rarely the amount of work by itself. It is more often the lack of a clear order in which to do it. A lot of time gets wasted deciding what to start with, and important tasks tend to get pushed back until the deadline is very close.

This project is an attempt to fix that in a simple way. Instead of just storing a list of tasks, the program decides an order for them and turns that order into an actual schedule with clock times.

## 2. Problem Statement

To build a lightweight tool that lets a user record tasks, arranges them by deadline and priority, and produces a realistic, time-boxed plan for the day, without needing any installation, internet connection or special software.

## 3. Objectives

1. Let the user add tasks with a name, priority, time needed and due date.
2. Show all tasks in a clear, sorted table.
3. Generate a daily schedule using focus sessions and short breaks.
4. Allow tasks to be marked as completed.
5. Show progress so the user can see what is done and what is left.
6. Handle wrong input gracefully so the program never crashes because of a typing mistake.

## 4. Tools and Technologies

| Item | Details |
|------|---------|
| Language | Python 3.6 or above |
| Libraries | None (standard library only) |
| Interface | Command line / terminal |
| Storage | In-memory list of dictionaries |

I chose plain Python on purpose. It keeps the project easy to run on any computer and makes the code easy to read and explain.

## 5. System Design

### 5.1 Data structure

Each task is stored as a dictionary inside a global list called `tasks`:

```python
{"name": "Study Python", "p": 1, "m": 60, "d": 0, "done": False}
```

Here `p` is the priority, `m` is the minutes needed, `d` is the number of days until the deadline and `done` tells whether the task is finished. A separate dictionary, `PRIO`, maps the numbers 1, 2 and 3 to the words High, Med and Low for display.

### 5.2 Program flow

The program runs inside a loop in `main()`. It prints a menu, reads the user's choice and calls the matching function. The loop continues until the user picks Exit.

### 5.3 Modules (functions)

| Function | What it does |
|----------|--------------|
| `fmt(m)` | Converts minutes since midnight into HH:MM format. It wraps around after 24 hours. |
| `num(prompt, lo, hi)` | Keeps asking until the user types a whole number inside the allowed range. |
| `add_task()` | Reads task details, validates them and stores the task. |
| `get_sorted()` | Returns tasks ordered by due date first and priority second. |
| `show_tasks()` | Prints all tasks in a formatted table with their status. |
| `finish_task()` | Lists pending tasks and marks the chosen one as done. |
| `make_schedule()` | Builds the Pomodoro timetable for all pending tasks. |
| `show_stats()` | Prints the progress summary and a text progress bar. |
| `main()` | Displays the menu and controls the flow of the program. |

## 6. Working of the Program

### 6.1 Adding a task

The user gives a name and three numbers. The name cannot be empty. The priority must be 1, 2 or 3. The time needed must be between 5 and 600 minutes, and the days until due must be between 0 and 365. If any value is outside its range, the program explains the problem and asks again.

### 6.2 Sorting

Tasks are sorted using Python's `sorted()` with a key of `(due days, priority)`. That means something due today always comes before something due tomorrow, and when two tasks share a deadline, the higher priority one is placed first.

### 6.3 Scheduling

After the user enters a start hour and minute, the scheduler goes through the pending tasks in sorted order. For each task it cuts the required time into blocks of at most 25 minutes. After each block it adds a 5 minute break. The only place where no break is added is after the final block of the final task, since there is nothing left to rest before.

For example, a 60 minute task starting at 09:00 is scheduled like this:

```
09:00 - 09:25 | Focus: Study Python
09:25 - 09:30 | Break
09:30 - 09:55 | Focus: Study Python
09:55 - 10:00 | Break
10:00 - 10:10 | Focus: Study Python
--- Finished around 10:10 ---
```

The last block is only 10 minutes long because that is all that remained of the task.

### 6.4 Progress tracking

The progress screen counts finished tasks, works out the percentage, adds up minutes done and minutes remaining, and draws a 20-character bar. It also prints a short message depending on how far along the user is.

```
Progress: 1/2 tasks (50%)
Time    : 60m done | 30m remaining
Bar     : [##########----------]
Over halfway there!
```

## 7. Testing

I tried the program with normal and abnormal input to make sure it behaves sensibly. The table below lists the main cases and what the program is designed to do in each.

| Test case | Input | Expected behaviour |
|-----------|-------|--------------------|
| Empty task name | (just press Enter) | Message "Name can't be empty" and return to menu |
| Letters in a number field | `abc` for priority | Asks again with the allowed range |
| Number out of range | `9` for priority | Asks again |
| View with no tasks | Option 2 on a fresh start | "No tasks saved yet." |
| Schedule with no pending tasks | Option 3 with nothing added | "No pending tasks to schedule." |
| Finish with no pending tasks | Option 4 when all are done | "All caught up!" message |
| Wrong menu choice | `9` at the menu | "Invalid choice, try 1-6." |
| Long task name | Name longer than 18 characters | Name is cut to fit the table column |
| Task longer than 25 minutes | 60 minutes | Split into several sessions with breaks |

## 8. Results

The program does what it was built to do. It accepts tasks, orders them sensibly, produces a readable timetable and reports progress accurately. Invalid input is handled by re-asking instead of crashing, which makes it comfortable to use even when typing quickly.

## 9. Limitations

- **No saving.** Tasks live in memory only, so everything is lost when the program is closed.
- **Terminal only.** There is no graphical interface.
- **No fixed commitments.** The scheduler assumes the user is free from the start time onward and cannot work around classes or meetings.
- **Fixed session length.** The 25/5 pattern is hard-coded and cannot be changed while the program is running.
- **Midnight wrap.** If a schedule runs past midnight, the clock simply wraps back to 00:00 without showing that it is the next day.

## 10. Future Scope

- Store tasks in a JSON or CSV file so they carry over between sessions.
- Add options to edit and delete tasks.
- Let the user choose their own focus and break lengths.
- Add a longer break after every four focus sessions, as in the original Pomodoro method.
- Build a live countdown timer.
- Create a graphical or web version.

## 11. Conclusion

Time Management shows that a useful planning tool does not have to be complicated. With around 130 lines of plain Python, it turns a pile of tasks into an ordered, time-boxed plan and lets the user see their progress as they go. Working on it also helped me practise input validation, sorting with custom keys, working with dictionaries and structuring a program into small functions. There is plenty of room to grow it, but even in its current form it does the main job: it tells the user what to work on and when.

## 12. References

1. Python Software Foundation, *Python 3 Documentation*, https://docs.python.org/3/
2. Francesco Cirillo, *The Pomodoro Technique*, https://www.francescocirillo.com/pages/pomodoro-technique
