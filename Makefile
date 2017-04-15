.PHONY: help
help: ## Display callable targets.
	@echo "Reference card for usual actions in development environment."
	@echo "Here are available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build package to upload.
	python setup.py bdist_wheel

.PHONY: upoad
upload: ## Upload to pypi
	twine upload dist/*
