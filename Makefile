build:
	docker build . --tag raehik/jling-github-scraper:latest

push:
	docker push raehik/jling-github-scraper:latest
