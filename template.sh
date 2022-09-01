#!/bin/sh

if [ -z "$PARAM" ] 
then
  echo "ERROR: PARAM is not defined"
  exit 1
fi

cat << EOF
docker build -t $PARAM -f Dockerfi.$PARAM
EOF
