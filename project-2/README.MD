# Prerequisite
- docker
- docker-compose
# How to start
`docker-compose up --build`

## Grafana
- endpoint: `localhost:3000`
- username/password: `admin/admin`
![img.png](grafana.png)
We have 2 dashboards visualize total count of requests to service and response
time service finish handle request by time.

## Prometheus
- endpoint: `localhost:9090`
## Service
- trigger 200 status code request: `http://localhost:8080/`
- trigger 404 status code request: `http://localhost:8080/abc` or any endpoint except root `/`
Just trigger those endpoint for mocking traffics

# Explaination
- With grafana I don't have provision dashboard ATM. Using default account admin to access.
It choose datasource from Prometheus and visualize data
- For service server side, it serve request with 200 status code only for root path `/`.
And it expose port 9000 for metrics. 
- For Prometheus, it scraper will collect those metrics with interval time defined on prometheus.yml file
- All storage are binded with docker volumes define on docker-compose.yml file
- Implementation: 3 hours with zero knowledge about prometheus exporter, just lookup around Google for implementation guide
- Optional tasks implementation: implement metrics collect and export HTTP status code of request