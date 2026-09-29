# Time Management: Project Statement

## The problem

Most of us have plenty to do and no clear idea of where to begin. I used to write long to-do lists and then lose an hour just deciding which task to pick up first. Deadlines crept up, easy tasks got done before important ones, and by evening I usually felt like I'd been busy all day without getting the right things finished.

The problem isn't a lack of tasks or even a lack of time. It's that we don't plan how the time will actually be spent.

## What I wanted to build

A simple tool that takes the thinking out of planning. I wanted something I could open in a terminal, type in my tasks, and get back a clear answer to one question: "What should I do right now?"

It also had to be quick to use. If a planner takes longer to set up than the work itself, nobody will keep using it.

## How this project solves it

Time Management is a command-line planner written in Python. For every task you enter:

- a name
- a priority (high, medium or low)
- how many minutes it will take
- how many days are left until it's due

The program then sorts everything by deadline first and priority second, so the most urgent work always sits at the top. When you give it a start time, it builds a full day plan using the Pomodoro method: 25 minutes of focused work followed by a 5 minute break. Longer tasks are split across several sessions automatically.

As you finish things, you can mark them as done and check a progress summary that shows how many tasks are complete, how much time is left, and a small progress bar.

## Who it's for

Mainly students, like me, who have assignments, exams and projects all landing at once. But anyone who wants a no-fuss way to plan their day can use it.

## Scope and limits

This is a first version, so it does a few things well and leaves others out:

- It runs in the terminal only, with no graphical interface.
- Tasks are kept in memory, so they disappear when the program closes.
- The schedule doesn't work around fixed commitments like classes or meetings.

## Where it can go next

- Saving tasks to a file so they carry over between sessions
- Editing and deleting tasks
- Custom focus and break lengths
- A longer break after every four sessions
- A simple graphical or web version

## Tools used

- Python 3 (standard library only, no extra packages)

## Author

Devanshu Daksha
VIT Bhopal University
