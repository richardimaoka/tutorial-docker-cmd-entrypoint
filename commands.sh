#!/bin/sh
# # CMD ["echo", "abc"]
# docker build -t cmd1 -f Dockerfile.cmd1 .
# docker images --filter=reference='cmd*'
# docker run cmd1
# docker inspect cmd1 --format='CMD {{.Config.Cmd}}'

# # CMD ["echo", "abc", "def"]
# docker build -t cmd2 -f Dockerfile.cmd2 .
# docker images --filter=reference='cmd*'
# docker run cmd2
# docker inspect cmd2 --format='CMD {{.Config.Cmd}}'

# # CMD echo "abc" 
# docker build -t cmd3 -f Dockerfile.cmd3 .
# docker images --filter=reference='cmd*'
# docker run cmd3
# docker inspect cmd3 --format='CMD {{.Config.Cmd}}'

# # CMD echo "abc" "def"
# docker build -t cmd4 -f Dockerfile.cmd4 .
# docker images --filter=reference='cmd*'
# docker run cmd4
# docker inspect cmd4 --format='CMD {{.Config.Cmd}}'

# # CMD echo "$HOME"
# docker build -t cmd5 -f Dockerfile.cmd4 .
# docker images --filter=reference='cmd*'
# docker run cmd5
# docker inspect cmd5 --format='CMD {{.Config.Cmd}}'

# # CMD [ "sh", "-c", "echo $HOME" ]
# docker build -t cmd6 -f Dockerfile.cmd6 .
# docker images --filter=reference='cmd*'
# docker run cmd6
# docker inspect cmd6 --format='CMD {{.Config.Cmd}}'

docker build -t cmd7 -f Dockerfile.cmd7 .
docker run -d --name cnt-cmd7 cmd7
docker exec -it cnt-cmd7 /bin/sh
ps -eaf
# # ps -eaf
# UID        PID  PPID  C STIME TTY          TIME CMD
# root         1     0  0 21:27 ?        00:00:00 tail -f /dev/null
# root         7     0  0 21:28 pts/0    00:00:00 /bin/sh
# root        14     7  0 21:28 pts/0    00:00:00 ps -eaf
docker stop cnt-cmd7

docker build -t cmd8 -f Dockerfile.cmd8 .
docker run -d --name cnt-cmd8 cmd8
docker exec -it cnt-cmd8 /bin/sh
ps -eaf
# # ps -eaf
# UID        PID  PPID  C STIME TTY          TIME CMD
# root         1     0  0 21:29 ?        00:00:00 /bin/sh -c tail -f /dev/null
# root         8     1  0 21:29 ?        00:00:00 tail -f /dev/null
# root         9     0  0 21:29 pts/0    00:00:00 /bin/sh
# root        15     9  0 21:29 pts/0    00:00:00 ps -eaf
docker stop cnt-cmd8