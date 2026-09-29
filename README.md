# Daily Planner

This is a small command-line planner I wrote in Python. You type in your tasks, tell it how long each one will take and when it's due, and it works out a Pomodoro-style schedule for your day (25 minutes of focus, then a 5 minute break).

I built it because I kept making to-do lists and then never knowing where to start. Now the program just tells me.

## What it does

- Lets you add tasks with a priority, time estimate and due date
- Shows all your tasks in a table, with the most urgent ones on top
- Builds a schedule for the day starting from whatever time you give it
- Lets you tick off tasks when you finish them
- Shows a quick progress summary with a little bar

It only uses built-in Python, so there's nothing to install.

## Running it

You need Python 3.6 or newer. Then just:

```
python planner.py
```

You'll get this menu:

```
1. Add task  2. View tasks  3. Schedule day
4. Mark done 5. Progress     6. Exit
```

Type the number and hit enter.

## Adding a task

Option 1 asks you four things:

- **Name**: whatever you want to call it
- **Priority**: 1 is high, 2 is medium, 3 is low
- **Minutes needed**: anywhere from 5 to 600
- **Days until due**: 0 means it's due today

If you type something invalid (like a letter, or a number out of range), it just asks again instead of crashing.

## How the ordering works

Tasks are sorted by due date first, and then by priority if two tasks are due on the same day. So something due today always comes before something due next week, even if the later one is high priority. That's how I wanted it, but it's easy to change in `get_sorted()` if you'd rather go by priority first.

## Example

Say I add one task called "Study Python", high priority, 60 minutes, due today, and ask for a schedule starting at 9:00. I get:

```
--- Work Plan (25m focus + 5m break) ---
09:00 - 09:25 | Focus: Study Python
09:25 - 09:30 | Break
09:30 - 09:55 | Focus: Study Python
09:55 - 10:00 | Break
10:00 - 10:10 | Focus: Study Python
--- Finished around 10:10 ---
```

The last session is only 10 minutes because that's all that was left of the task. There's no break added after the very last task either.

The progress screen looks like this once half my tasks are done:

```
Progress: 1/2 tasks (50%)
Time    : 60m done | 30m remaining
Bar     : [##########----------]
Over halfway there!
```

## Things to know

- Nothing is saved. When you close the program, your tasks are gone. I haven't added file saving yet.
- The schedule assumes you're free from your start time onwards, so it won't work around meetings or classes.
- If the schedule runs past midnight, the clock wraps back to 00:00.

## Ideas for later

- Save tasks to a JSON file so they stick around
- Edit and delete tasks
- Let the user choose their own focus and break lengths
- A longer break after every four sessions, like real Pomodoro
- A live timer

## About

Made by Devanshu Daksha, VIT Bhopal University.
