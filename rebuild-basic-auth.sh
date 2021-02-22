#!/bin/bash
imageName=xx:basic_auth
containerName=stoic_ramanujan

docker build -t $imageName -f Dockerfile .

echo Delete old container...
docker rm -f $containerName

echo Run new container...
docker run -d -p 8500:8500 --name $containerName $imageName