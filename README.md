# Fantasy Football Flask Application

## Overview

This is a Flask-based fantasy football application. It performs full CRUD functionality and models a one to many relationship between two tables. The `Teams` and `Players` tables are both modelled using SQLAlchemy. The application allows a user to create multiple football teams/clubs, and then assign players to that team/club, using an 'Add Player' button. The teams and players can be given attributes such as 'Team League' and 'Player Position', which can be modified by the user. Both tables have full CRUD functionality, allowing the user to create, read, update and delete Teams and Players from the database. The web application uses an external database hosted within the Cloud, in the form of a MySQL server for Azure. It makes use of a backend API (Application Programming Interface), which interacts with the database via requests to a RESTful API to create, read, update and delete data. A frontend service is uses templating to host and serve the web pages with information from the database. This information is retrieved from the backend API service. All secrets/credentials used throughout the application are stored within the deployment server through the Jenkins Pipeline, and cannot be accessed elsewhere.

![new erd](https://user-images.githubusercontent.com/91483629/144483665-f695f2f4-8492-446b-b399-875feefe21f6.jpg)

## CI/CD Pipeline:
As part of the DevOps approach, a CI/CD Pipeline was implemented to automate the integration and deployment of new code. The `Jenkins` automation server was used as part of the CI/CD Pipeline to Setup, Test, Build, Push and Deploy the application. The setup stage installs/updates apt dependencies. The testing stage runs unit tests using pytest. The build and push stages makes use of docker and docker-compose to build the docker images and push the docker images to a registry (DockerHub). Finally, the deploy stage deploys the application to a Docker Swarm server hosted in the cloud.

## Risk Assessment
![risk assessment](https://user-images.githubusercontent.com/91483629/144489314-69560043-d908-42fc-87b1-529fae3e7af4.png)

## Running the Application

These instructions assume you are running your app on an Ubuntu machine.

1.  Install the necessary `apt` requirements:

    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

2.  Create a Python virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the required Python packages with `pip` using the [`requirements.txt`](/requirements.txt) file:

    ```bash
    pip3 install -r requirements.txt
    ```

4.  Define the connection string for your database as an environment variable named `DATABASE_URI`:

    ```bash
    export DATABASE_URI=<your_database_uri_here>
    ```

    If you are connecting to an external database, your connection string will be in the format:

    ```bash
    export DATABASE_URI=mysql+pymysql://<username>:<password>@<db_hostname>:3306/<database>
    ```

    Alternatively, you can use SQLite to store your database data as a file:

    ```bash
    export DATABASE_URI=sqlite:///data.db
    ```

    This will create a file called `data.db` in your [`application/`](/application) directory.

5.  Set the `CREATE_SCHEMA` environment variable.

    ```bash
    export CREATE_SCHEMA=<true_or_false>
    ```

    When this variable is set to `true`, it will generate the table schema in the database you are connecting to (as defined by the `DATABASE_URI` variable).
    
    Any other value will not generate the schema at app start-up.

    >NOTE: if `CREATE_SCHEMA` is not set, it will cause the application to crash at start-up.

6.  Run the application:

    ```bash
    python3 app.py
    ```
