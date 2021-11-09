This is an example of a web application built on the Django framework.

This content-aggregator aggregate contents about technology, from the websites:

https://techcrunch.com/
 
https://mashable.com/
 
https://www.theverge.com/

# Prerequisites

To run the application, you'll need to have the Docker and docker-compose installed on your device.

# Build

Steps to build the application:

1. Clone this repo

   git clone https://github.com/dyogocae/content-agg-system.git

2. Go to the project's root folder and open the terminal
3. Build the containers to run the application

   docker-compose build
 
4. Run the application

   docker-compose up

5. open http://localhost:8000/
