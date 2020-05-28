-include env_make

PORTS ?= -p 9001:9001
NAME ?= datacrawler
VOLUME ?= $(PWD)/projects

.PHONY: shell run start stop logs rm

default: run

run:
	docker run --rm -d -v $(VOLUME):/app/data/projects:rw $(PORTS) --name $(NAME) scrapinghub/portia
	$(info VISIT http://localhost:9001 IN THE BROWSER.)

shell:
	docker exec -it -w /app/data/projects $(NAME) /bin/bash

start:
	docker start $(NAME)

stop:
	docker stop $(NAME)

logs:
	docker logs $(NAME)

rm:
	docker rm -f $(NAME)
