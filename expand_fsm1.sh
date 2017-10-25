#!/bin/sh
#LEX_FSM = "$(python expand_fsm1.py $1)" 
TEMPFILE="$(mktemp)"
python expand_fsm1.py $1 > $TEMPFILE
carmel -d $TEMPFILE $2
#rm $TEMPFILE