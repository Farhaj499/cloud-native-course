## Created docker container file to run the app
 
 1. First we need to install the extension of "Dev Container"
 It will give you a tab of "Remote Explorer"

 2. Click on Remote Explorer and 
    a. Click Select Folder
    b. Select workspace
    c. Select Docker file if created to give instructions.
    d. Select OK.
it will create a dev container and create two folders named ".devcontainer" with "devcontainer.json" and ".github" with "dependabot.yml"

3. In remote explorer you can see if the container is running or not.

4. In terminal you will be able to make changes to the container directly.

5. To run the container on your machine, first run
    a. poetry install
    b. poetry run uvicorn main:app --reload

6. If you want to install an extension, right click on extension and select "Add to dev container", It will add the extension as well as change the devcontainer.json file.
So whenever someone uses this container, they will be able to use the extension by default.






