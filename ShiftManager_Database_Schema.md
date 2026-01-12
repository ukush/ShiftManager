# ShiftManager Database Schema

## roles

```sql
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);
```

## users

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  telephone TEXT,
  password_hash TEXT NOT NULL,
  role_id INTEGER REFERENCES roles(id) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## shifts

```sql
CREATE TABLE shifts (
  id SERIAL PRIMARY KEY,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  manager_id INTEGER REFERENCES users(id),
  required_employees INTEGER DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## assignments

```sql
CREATE TABLE assignments (
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  shift_id INTEGER REFERENCES shifts(id) ON DELETE CASCADE,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, shift_id)
);
```

## time_off_requests

```sql
CREATE TABLE time_off_requests (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  start_datetime TIMESTAMP NOT NULL,
  end_datetime TIMESTAMP NOT NULL,
  total_hours NUMERIC,
  status TEXT CHECK (status IN ('pending', 'approved', 'denied')) DEFAULT 'pending',
  requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```