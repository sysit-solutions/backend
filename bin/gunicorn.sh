#!/bin/sh

BIN_DIR=`dirname $0`
WORKERS=1
export FREENIT_ENV="deploy"
PIDFILE=$1

if [ -z "${PIDFILE}" ]; then
  echo "Usage: $0 <pidfile>" >&2
  exit 1
fi


. ${BIN_DIR}/common.sh
setup

gunicorn --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker --workers "${WORKERS}" --daemon --pid "${PIDFILE}" main:app
