#! /bin/sh

script_name=docker-hub-cd-script.sh

for pid in $(pidof -x $script_name); do
    if [ $pid != $$ ]; then
        kill -9 $pid
    fi 
done


docker container stop docker-hub-automated-build-example

docker container rm docker-hub-automated-build-example

docker image rm -f davidwxg/docker-hub-automated-build-example:latest

docker run -p 8000:8000 -d --name docker-hub-automated-build-example davidwxg/docker-hub-automated-build-example:latest
