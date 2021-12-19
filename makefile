compile:
	python compile.py

install: compile
	pip install -r requirements.txt
	python install.py
	make clean

run:
	python run.py

debug:
	make install
	make run

c_binaries = src/bin/python

clean:
	rm -f $(c_binaries)