# simple-site-requester

Simple projects which uses Celery & Django REST to periodically requests sites

### Requirements:
  * docker-compose
  * docker

### Tested on:
  * docker-compose==*1.14.0*
  * docker==*17.06.0-ce*
  
## Using:
  ### Start whole app
    `./manage.sh up`
  ### Look into logs
    `./manage.sh logs -f`
  ### Stop whole app
    `./manage.sh down`
 
 ## API
 Whole API will be available on `http://127.0.0.1:8000`
  ### Endpoints
   * `127.0.0.1:8000/requested_sites/`
  

 
