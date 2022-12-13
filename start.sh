#!/bin/bash
app="aoc2022"

#remove any running containers
docker rm $(docker stop $(docker ps -a -q --filter ancestor=${app} --format="{{.ID}}"))

docker build -t ${app} .
docker run -d -p 5557:5000 ${app}
#docker run -it --rm -p 5557:5000 ${app} sh
