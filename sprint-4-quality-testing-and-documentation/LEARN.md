# Sprint 4: Quality, testing and documentation

Learn to find bugs on purpose, write tests, report problems clearly and document what you built.

## Lesson 4.1: Testing: what and how

Testing is how a team earns the right to change code without fear. Tests come in layers.

- Unit tests check one small piece, such as a function, and run in milliseconds.
- Integration tests check that pieces work together, such as a route reading from a database.
- End-to-end tests walk through the product like a person would. They are the most realistic and the slowest.

Write many unit tests, fewer integration tests and only a few end-to-end tests for the journeys that matter most.

```
test("rejects passwords shorter than 10 characters", () => {
  expect(validPassword("short")).not.toBeNull();
});
```

Test the edges: empty input, very long input, the wrong type, someone who is not signed in. Most bugs live there.

---

## Lesson 4.2: Writing a bug report people can act on

A bug report is useful only if someone else can reproduce the problem. Include:

- A title that says what is wrong: 'Quiz score shows 0 after submitting', not 'Quiz broken'.
- Steps to reproduce, numbered, starting from a known state.
- What you expected and what actually happened.
- Where it happened: browser, device, account type.
- A screenshot or the exact error text.

One bug per report. If you cannot reproduce it every time, say how often it happens.

---

## Lesson 4.3: Documentation that gets read

Good documentation answers the first questions a new teammate asks. Start with these, in this order:

- What this is and who it is for, in two sentences.
- How to run it on a clean machine, step by step. Test these steps by following them yourself.
- How it is organised: the main folders and what each is for.
- Decisions that would surprise a newcomer, and why they were made.

Keep docs next to the code and update them in the same pull request as the change. Out-of-date docs are worse than none.
