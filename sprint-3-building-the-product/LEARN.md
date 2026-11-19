# Sprint 3: Building the product

Understand how the web fits together, how to read and write APIs, and how to review code well.

## Lesson 3.1: How a web app works

When you open a page, your browser sends a request to a server, and the server sends back a response. The browser then turns the response, usually HTML, CSS and JavaScript, into what you see.

- HTML gives the page its structure and meaning.
- CSS controls how it looks.
- JavaScript makes it respond to the person.
- The server holds the rules and the data, and the database stores it durably.

A useful rule: the browser belongs to the person using it, so never trust anything it sends. Check permissions and validate input on the server, every time.

---

## Lesson 3.2: APIs, status codes and data

An API is an agreed way for one program to ask another to do something. Over HTTP, each request has a method that says the intent.

- GET reads data and must not change anything.
- POST creates something or triggers an action.
- PUT or PATCH changes something that exists.
- DELETE removes it.

### Status codes tell you what happened

- 200 range: it worked.
- 400 range: the request was wrong. 401 means not signed in, 403 means signed in but not allowed, 404 means not found.
- 500 range: the server failed. That is our bug, not the caller's.

```
{ "title": "Add login form", "column": "doing" }
```

---

## Lesson 3.3: Code review that helps

Review exists to share knowledge and catch mistakes, not to judge people. Review the code, never the person.

- Keep pull requests small. Past a few hundred lines, reviews turn into skimming.
- As author, explain what changed and why, and how you checked it.
- As reviewer, ask questions before giving orders: 'What happens if this is empty?'
- Separate must-fix from nice-to-have so the author knows what blocks the merge.
- Check the boring risks: secrets, unvalidated input, missing permission checks, no handling for failure.
