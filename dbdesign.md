The database design will start off simple and should accomodate the main functions of the app.

The entities stored in the database are:
1. Users --> stores user data such as name, telephone etc
2. Shifts --> data about the shift including start/end time
3. Assignments --> join table to assign shifts to users
4. Time-off requests --> stores data such as start/end time and status
5. Roles --> separate table to store roles

<img width="795" height="569" alt="erd" src="https://github.com/user-attachments/assets/3cbdd20c-ee43-44d3-b9e8-bdb8911d8a21" />

I have made a number of considerations when designing this ERD.

I have a separate roles table instead of just hardcoding the roles as text inside of the user table so to help ensure data integrity and reduce bugs. Having a separate table allows for each user to be associated with a role through a role_id. 

