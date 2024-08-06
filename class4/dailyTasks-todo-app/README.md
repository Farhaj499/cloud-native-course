Todo APP Backend Functionality using
1. Python: For programming the app
2. FastAPI: To create the API endpoints for frontend
3. SQLModel: To create a bridge between Python and SQL
4. Oauth2: For authentication
5. Pytest: For testing of the API endpoints
6. Passlib[bcrypt]: For hashing passwords

## Created docker file to run the app

Checking to see if Docker is running:
-> docker version

Building the Image for Dev:
-> docker build -f Dockerfile.dev -t my-dev-image .

Check Images:
-> docker images

Verify the config:
-> docker inspect my-dev-image

Running the Container for Dev:
-> docker run -d --name dev-cont1 -p 8000:8000 my-dev-image

Check in browser:
http://localhost:8000

Container logs
-> docker logs dev-cont1

Test the Container:
-> docker run -it --rm my-dev-image /bin/bash -c "poetry run pytest"

List Running Containers
-> docker ps

List all Containers
-> docker ps -a

Intract with the Container:
-> docker exec -it dev-cont1 /bin/bash

Exit from the container shell
-> exit
