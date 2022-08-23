```sh
docker build -t cmd1 -f Dockerfile-cmd1 .
docker images
docker inspect cmd1 --format='CMD {{.Config.Cmd}}'

docker build -t cmd2 -f Dockerfile-cmd2 .
docker inspect cmd2 --format='CMD {{.Config.Cmd}}'
docker images
```
