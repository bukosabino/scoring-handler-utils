init:
	pip install -r requirements.txt

isort:
	isort --check-only api_model/*

format: isort
	black api_model

isort-fix:
	isort api_model/*

lint: isort
	prospector api_model/
