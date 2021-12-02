# Fantasy Football Flask Application

## Overview

This is a Flask-based fantasy football application. It performs full CRUD functionality and models a one to many relationship between two tables. The `Teams` and `Players` tables are both modelled using SQLAlchemy. The application allows a user to create multiple football teams/clubs, and then assign players to that team/club, using an 'Add Player' button. The teams and players can be given attributes such as 'Team League' and 'Player Position', which can be modified by the user. Both tables have full CRUD functionality, allowing the user to create, read, update and delete Teams and Players from the database. The web application uses an external database hosted within the Cloud, in the form of a MySQL server for Azure. It makes use of a backend API (Application Programming Interface), which interacts with the database via requests to a RESTful API to create, read, update and delete data. A frontend service is uses templating to host and serve the web pages with information from the database. This information is retrieved from the backend API service. All secrets/credentials used throughout the application are stored within the deployment server through the Jenkins Pipeline, and cannot be accessed elsewhere.

![new erd](https://user-images.githubusercontent.com/91483629/144483665-f695f2f4-8492-446b-b399-875feefe21f6.jpg)

## Risk Assessment
![risk assessment](https://user-images.githubusercontent.com/91483629/144489314-69560043-d908-42fc-87b1-529fae3e7af4.png)

## CI/CD Pipeline:
As part of the DevOps approach, a CI/CD Pipeline was implemented to automate the integration and deployment of new code. The `Jenkins` automation server was used as part of the CI/CD Pipeline to Setup, Test, Build, Push and Deploy the application. The setup stage installs/updates apt dependencies. The testing stage runs unit tests using pytest. The build and push stages makes use of docker and docker-compose to build the docker images and push the docker images to a registry (DockerHub). Finally, the deploy stage deploys the application to a Docker Swarm server hosted in the cloud.

![cicdpipieline](https://user-images.githubusercontent.com/91483629/144489962-7aa90bd4-38c3-4a86-930f-dd85943e1d43.png)

## Webhook Logs
![webhook](https://user-images.githubusercontent.com/91483629/144508921-35865c99-a46c-4771-8c00-6cfce353d9fc.png)

## Test Reports
![test results](https://user-images.githubusercontent.com/91483629/144517267-e952404b-5830-4d1c-a1b4-1d58abc6f115.png)

## Code Coverage
![coverage logs](https://user-images.githubusercontent.com/91483629/144517377-f9896146-2d7e-4d74-b5f2-071916e705a2.png)

## Future Improvements
Unit testing.
Unit testing coverage.
Project Tracking Board.
