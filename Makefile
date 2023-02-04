SHELL  = /bin/sh
PYTHON = python3
BUILD  = $(PYTHON) -m build
TWINE  = $(PYTHON) -m twine

.PHONY: release release_test

release:
	$(BUILD)
	$(TWINE) upload dist/*

release_test:
	$(BUILD)
	$(TWINE) upload --repository testpypi dist/*
