install:
	pip install -r requirements.txt
	python install.py

run:
	python run.py

debug:
	make install
	make run