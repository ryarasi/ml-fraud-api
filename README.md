This is the repo for the Fraud API

Live deployment - https://fl-ml-fraud.herokuapp.com/

# Stack:-

1. Python version 3.8.2
2. FastAPI
3. Postgres 13
4. NGINX Proxy
5. Docker

# Steps to start

1. Make sure that you've got the following installed locally:-
    1. Docker
    2. [Optional] Node JS & NPM [Required to use the automated scripts in the package.json file]
2. Make sure that you're in the `dev` branch when running locally.
3. Run `npm run start` to initialize the repo in the dev environment. If you do not have NPM, just enter `docker compose -f docker-compose-dev.yml up` to start the API locally. The commands are available in the `package.json` file in the scripts section.
4. Once the service starts up, you can visit `http://localhost:8000` to run the API locally.

# Deployment

1. This repo has been deployed to heroku. Pushing to master automatically updates the deployment.