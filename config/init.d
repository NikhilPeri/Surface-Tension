#!/bin/sh
### BEGIN INIT INFO
# Provides:          surface-tension
# Required-Start:    $remote_fs $local_fs $syslog $time
# Required-Stop:     $remote_fs $local_fs $syslog $time
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Background process for surface-tension runtime
# Description:       surface-tension is a python application to control
#                    the behaviour of the moving wall art installation
#                    at the University of Ottawa.
### END INIT INFO

cd $SURFACE_TENSION_DIR; python -m controller
