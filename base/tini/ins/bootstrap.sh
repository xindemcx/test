#!/bin/bash

set -eu

SUPERVISOR_PARAMS='-c /etc/supervisor.conf.d/supervisor.conf'

bootpath=${BOOTSTRAP_PATH:-/}/init.d
if [ "$( ls $bootpath 2>/dev/null )" ]; then
	for script in $bootpath/*.sh; do
		. $script
	done
fi

# We have TTY, so probably an interactive container...
if test -t 0; then
# Run supervisord detached...
	supervisord $SUPERVISOR_PARAMS

# Some command(s) has been passed to container? Execute them and exit.
# No commands provided? Run bash.
	if [[ $@ ]]; then
		eval $@
	else
		export PS1='[\u@\h : \w]\$ '
		/bin/bash
	fi

# Detached mode? Run supervisord in foreground, which will stay until container is stopped.
else
# If some extra params were passed, execute them before.
# @TODO It is a bit confusing that the passed command runs *before* supervisord,
#       while in interactive mode they run *after* supervisor.
#       Not sure about that, but maybe when any command is passed to container,
#       it should be executed *always* after supervisord? And when the command ends,
#       container exits as well.
	if [[ $@ ]]; then
		eval $@
	fi
	supervisord -n $SUPERVISOR_PARAMS
fi
