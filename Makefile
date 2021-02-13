init:
	pip install -r requirements.txt

isort:
	isort --check-only api_model_utils/*

format: isort
	black api_model_utils

isort-fix:
	isort api_model_utils/*

lint: isort
	prospector api_model_utils/
