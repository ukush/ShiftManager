API design


What are the functionlities and how would these translate into the endpoints?
- Manager registers user (creates an account for employee) --> POST /users/:id
- User logs in --> ?
- Fetch user details --> GET /users/:id
- employee checks upcoming shifts for a specifc employee (e.g. for the week) --> GET /users/:id/shifts?<filter> e.g. /users/:id/start=2025-08-10&end=2025-08-16
- manager wants to create a new shift --> POST /shifts
- manager wants modify a shift (maybe swap the employees or the time) --> PUT /shits/:id
- manager wants to delete a shift --> DELETE /shifts/:id

