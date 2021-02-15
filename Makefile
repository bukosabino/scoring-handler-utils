init:
	pip install -r requirements.txt

isort:
	isort --check-only scoring_handler_utils/*

format: isort
	black scoring_handler_utils

isort-fix:
	isort scoring_handler_utils/*

lint: isort
	prospector scoring_handler_utils/
