#!/bin/sh

# ENTRYPOINT ["echo"] CMD ["abc"]
docker build -t cmd-and-entrypoint1 -f Dockerfile.cmd-and-entrypoint1 .
docker images --filter=reference='cmd-and-entrypoint*'
docker run cmd-and-entrypoint1
# abc

# ENTRYPOINT ["echo"] CMD ["abc"] + parameter
docker run cmd-and-entrypoint1 def
# def

# CMD ["echo", "abc"] + parameter
docker run cmd1 def 
# docker run cmd1 efg # ERROR!!
# docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "efg": executable file not found in $PATH: unknown.
# ERRO[0000] error waiting for container: context canceled

# ENTRYPOINT ["echo", "abc"] + parameter
docker run entrypoint1 def
# abc def

docker build -t cmd-and-entrypoint1 -f Dockerfile.cmd-and-entrypoint1 .
docker run cmd-and-entrypoint1
docker run cmd-and-entrypoint1 ghi #ignoring CMD

docker build -t cmd-and-entrypoint2 -f Dockerfile.cmd-and-entrypoint2 .
docker inspect cmd-and-entrypoint1 --format=".Config.Cmd"
docker inspect cmd-and-entrypoint2 --format=".Config.Cmd"# 