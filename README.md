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
![pytest logs jenkins](https://user-images.githubusercontent.com/91483629/144595587-efb11d99-3f7b-47f2-9351-5097f50c5a21.png)
![pytest logs](https://user-images.githubusercontent.com/91483629/144597995-eea88363-c7b7-4ad8-82fa-5771204bd050.jpg)

Unit testing using the pytest framework module in Visual Studio Code, and Jenkins Test Results Logs.
In total, 12/23 tests failed. The frontend unit tests were especially difficult to implement and required the use of the requests_mock module. In future iterations of the application, these tests would ideally be fixed before deployment, and could be done so by correcting code in unit_test.py file.

## Code Coverage
![coverage logs](https://user-images.githubusercontent.com/91483629/144517377-f9896146-2d7e-4d74-b5f2-071916e705a2.png)
![coverage graphs](https://user-images.githubusercontent.com/91483629/144519258-62b4afc4-a767-4a5b-9849-45540c60ccec.png)

Cobertura Plug-in for Jenkins was used to generate coverage report.

## Deployment Logs
![deployment logs](https://user-images.githubusercontent.com/91483629/144519194-611eb2ec-c4ad-4aab-a0ef-191044aea5d9.png)
![deployment services](https://user-images.githubusercontent.com/91483629/144612623-c23539e5-3fc5-4c46-a149-7c7f8d09c9da.png)

The deploy stage initializes and containerises application services. The deployment logs show the two services, frontend and backend, running on the deployment server. These services can also be seen running via Remote SSH through Visual Studio Code by using the command 'sudo docker service ls'.

## Future Improvements
Unit testing.
Unit testing coverage.
Project Tracking Board.
