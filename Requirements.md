# Employee Shift Management App

## Overview

As a small restaurant owner, managing employee schedules can be time-consuming, often requiring several hours each week. To streamline this process, I propose a web-based application designed specifically for small hospitality businesses to efficiently manage staff shifts.

### The platform will allow owners or designated shift managers to:

- Allocate shifts to employees with a user-friendly interface  
- View staffing schedules by day, week, or month  
- Make real-time edits to individual employee rotas  
- Receive and respond to time-off requests directly within the system  
- Be alerted when employees request emergency time off, with the ability to approve or deny such requests  
- Check and update employee details like telephone number  

### Employees will have secure login access to:

- View their upcoming shifts for the week or month  
- Submit time-off requests, even for assigned shifts (e.g., in case of emergencies)  
- Receive notifications if their shifts are updated  
- View who else is working each shift, enabling them to initiate shift swap requests with colleagues (subject to manager approval and availability)  

Overall, the app will improve communication, reduce scheduling errors, and save time for both managers and employees, while ensuring better shift coverage and operational efficiency.

---

## Non-Functional Requirements

### 1. Usability
The app should be simple, intuitive, and easy to use, especially for users with limited technical experience. Most users will be employees or small team managers who need to quickly check or manage their schedule. The design should prioritize clarity and minimal friction for basic tasks like viewing a rota or submitting a time-off request.

**Rationale**: If the system is too complex, users will avoid it and revert to asking the manager manually. A clean, accessible interface encourages consistent usage and saves time overall.

---

### 2. Security
User information (e.g., names, contact info, hashed passwords) must be stored securely. Passwords will be hashed using a modern, secure algorithm like bcrypt. Basic security practices (e.g., HTTPS, input validation, access control) should be implemented.

**Consequence of Failure**: While the data isn't highly sensitive or critical (e.g., no financial or medical info), a breach could still cause reputational harm or user discomfort. Secure-by-default practices should be followed without overengineering.

---

### 3. Scalability / Capacity
The system is expected to support a maximum of 10–15 concurrent users at any given time, which is sufficient for a small restaurant team. The backend should be lightweight and optimized for low usage without requiring complex load balancing or autoscaling infrastructure.

**Rationale**: This is not a high-traffic application, and performance under modest load is acceptable. There's no need to design for hundreds of users when 10–15 is the realistic max.

---

### 4. Reliability
The system should aim for high availability, but short-term outages are acceptable. In case the app is temporarily down, staff can fall back on calling or texting the shift manager to confirm shifts.

**Consequence of Failure**: A temporary outage (e.g., a few hours) is an inconvenience but not a critical failure. Shift management can still continue manually in the short term. Maximum acceptable downtime is 24 hours, with a target of recovery within a few hours during working hours.

---

### 5. Performance
Core operations like logging in, viewing shifts, or submitting requests should typically respond within 1 second. Real-time performance is not essential — users are usually checking schedules or making occasional updates, not interacting in high-frequency bursts.

**Rationale**: Since most usage is passive (just viewing rotas), speed is important but not critical. It needs to feel responsive, but optimizing beyond that would be unnecessary complexity.

---

## MoSCoW Analysis

### Must Have

- Secure login system for employees and managers  
- Ability for managers to allocate shifts to employees  
- Calendar view of shifts by day, week, and month (for both employees and managers)  
- Employees can request time off  
- Managers can accept or reject time-off requests  

### Should Have

- Transparent view of who else is working (shared rota)  
- Shift swapping between employees (with approval logic)  

### Could Have

- Push or email notifications for shift changes and approvals  
- Real-time updates (e.g., via WebSocket or polling)  

### Would Have (Nice-to-Have / Future Enhancements)

- Offline mode for accessing schedules  
- Two-factor authentication (2FA) for added security  
- Basic payroll calculator based on hours worked
- AI assited rota creation tool.
