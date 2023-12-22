#! /bin/sh

### BEGIN INIT INFO
# Provides:          temp.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# CONFIG VALUES
LATEST_VERSION="1.0.6 (25/09/2021)"
FILE_NAME="Temp-Check"
PATH_NAME=/usr/local/bin/temp

echo "Latest Version: $LATEST_VERSION"

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting $FILE_NAME..."
    $PATH_NAME &
    ;;
  stop)
    echo "Stopping $FILE_NAME..."
    pkill -f $PATH_NAME
    ;;
  *)
    echo "Usage: /etc/init.d/temp.sh {start|stop}"
    exit 1
    ;;
esac

exit 0