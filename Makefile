build:
	docker build . -t python-api-ppl:latest

run:
	docker stop python-api-ppl-container
	docker rm python-api-ppl-container
	docker run -p 5000:5000 -d --name python-api-ppl-container python-api-ppl:latest
