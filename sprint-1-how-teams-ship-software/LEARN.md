# Sprint 1: How teams ship software

Understand the sprint rhythm, the five team roles and the Git habits every later sprint depends on.

## Lesson 1.1: Sprints, roles and ceremonies

A sprint is a fixed block of time, here two weeks, in which the team commits to a small set of outcomes and finishes them. Fixed time and a small scope are what make progress visible and surprises early.

### Your five roles

- Product Owner: decides what is worth building and in what order.
- Scrum Master: keeps the team's process healthy and removes blockers. This role rotates every sprint.
- Lead Developer: guides technical decisions and how the code is organised.
- Designer: shapes how the product looks and feels for the person using it.
- QA and Docs: checks that it works and writes down how it works.

### The ceremonies

- Planning: pick what the team will finish this sprint.
- Daily check-in in team chat: what I did, what I will do, what is blocking me.
- Review: show what is actually done.
- Retrospective: decide one thing to do better next sprint.

Roles describe responsibility, not exclusivity. Everyone builds, everyone tests, everyone reads the board.

---

## Lesson 1.2: Git for teams

Git records the history of your project so a team can work in parallel without overwriting each other. A commit is a saved snapshot with a message; a branch is a line of work that does not disturb the main line until you choose to merge it.

```
git switch -c add-login-form
git add .
git commit -m "Add login form with validation"
git push -u origin add-login-form
```

### Habits that save teams

- Never commit directly to main. Work on a branch and open a pull request.
- Commit small and often, with a message that says why, not just what.
- Pull the latest main into your branch before you open the request, so conflicts are yours to solve, not the reviewer's.
- Never commit passwords, tokens or keys. If one slips in, treat it as leaked and replace it.

---

## Lesson 1.3: Working well in a remote team

Most of your teamwork happens in writing. Good written updates let people work at different times without waiting for each other.

- Say the whole thing in one message: the context, the question, and what you already tried.
- Raise a blocker the same day. A blocker mentioned on day 2 is a nuisance; on day 9 it is a missed sprint.
- Keep decisions where the team can find them: the board card or the team chat, not a private message.
- Assume good intent, and ask before assuming someone ignored you.

Use the sprint board for work and the chat for conversation. If something was decided in chat, put a one-line note on the card.
