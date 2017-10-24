#!/bin/sh
#LEX_FSM = "$(python expand_fsm1.py $1)" 
carmel -sli $(python expand_fsm1.py $1) $2