#!/bin/sh
#LEX_FSM = "$(python expand_fsm1.py $1)" 
# $1 = lexicon file $2 = morphological rules $3 = output file
TEMPFILE="$(mktemp)"
python expand_fsm1.py $1 > $TEMPFILE
carmel $TEMPFILE $2 > $3
#rm $TEMPFILE