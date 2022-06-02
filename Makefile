.PHONY: help
help:
	@echo "Targets:"
	@echo "  venv"
	@echo "  install"
	@echo "  clean"
	@echo "  test"
	@echo "  wheel"
	@echo "  help"


.PHONY: clean
clean:
	@rm -rf *.egg-info
	@rm -rf build
	@rm -rf dist
	@rm -rf venv


venv:
	python3 -m venv venv
	venv/bin/python -m pip install -U pip
	venv/bin/python -m pip install -U wheel


.PHONY: install
install: venv
	venv/bin/pip install -e .\[dev\]
	

.PHONY: test
test:
	python3 -m unittest discover -s tests -p "test_*.py" -v


.PHONY: wheel
wheel: venv
	venv/bin/python setup.py bdist_wheel
