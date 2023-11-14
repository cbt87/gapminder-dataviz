#make everything
all: make_data q1 q2 q3 q4

make_data:
	python -B make_data.py

q1:
	python -B q1.py

q2:
	python -B q2.py	

q3:
	python -B q3.py

q4:
	python -B q4.py