#! /bin/bash

#EXIBE MENU DE ESCOLHA
OPC=$(dialog --menu "Programs essencials: " 0 0 0 \
1 "RECORD AUDIO" \
2 "PLAY AUDIO" \
3 "MELSPECTOGRAM" \
4 "MFCC" \
5 "EXIT FROM PROGRAM"  --stdout)

case $OPC in

	1)
	
	python record.py
	bash audio.sh;;

	2)

	python play.py
	bash audio.sh;;

	3)

	python melspec.py
	bash audio.sh;;

	4)

	python mfcc.py
	bash audio.sh;;

	5)
	cd ..
	bash menu.sh;;

	*)
	clear

esac
