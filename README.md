# simple-site-requester

Simple project which uses Celery & Django REST to periodically requests sites.
Elapsed response time & codes are being saved to database.
Sites can be loaded from YAML file (look [here](https://github.com/pikulak/simple-site-requester/blob/develop/simple_site_requester/simple_site_requester/config.yml)).
This app shares simple API endpoint.

### Requirements:
  * docker-compose
  * docker

### Tested on:
  * docker-compose==*1.14.0*
  * docker==*17.06.0-ce*
  
## Using:
  ### Start whole app
    ./manage.sh up
  ### Start whole app in the background
    ./manage.sh up-background
  ### Look into logs
    ./manage.sh logs -f
  ### Start API only
    ./manage.sh up ssr_api
  ### Start Celery worker only
    ./manage.sh up ssr_celery
  ### Stop whole app
    ./manage.sh down
  ### More
  For more commands type:
   `./manage.sh`
   
 ## API
 Whole API will be available on `http://127.0.0.1:8000`
  ### Endpoints
   * `127.0.0.1:8000/requested_sites/`
  

 
