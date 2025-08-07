Architectural Design
--

Based on the requirements of the application, teh app will follow a monoloithic architectural model. The application will only handle simple read/write requests and will only have a 10-15 concurrent users at one time, therefore a microservices architecture would not be needed.
It will also simplify deployment and maintenance of the application. 
This will however mean that changes to the application will mean the entire application needing to be shipped again, which needs to be taken into consideration.

The application will have 3 components:
- Front-End Client --> Built with React JS
- Back-End API App --> Built with Node/Express
- SQL Database --> Postgres

I am using JavaScript as the primary programming language due to a number of reasons:
  1. Simpify development by using a single language for both front and back end
  2. The business logic is not particularly complex, and so it does not need to be coded in a language that is ideal for highly performant systems.


The Architecture of the app is shown in the diagram below:

<img width="1225" height="555" alt="image" src="https://github.com/user-attachments/assets/6dcad25b-ee37-4749-b3ea-e27425bc1244" />

Now, I understand that this is not needed, however, I wanted to implement this for my own experience. I will implement this as a later addition.
