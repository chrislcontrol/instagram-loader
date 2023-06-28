PROJECT_NAME := instagram-loader
PYTHON_VERSION := 3.11.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)



setup:
	pip install --upgrade pip
	pip install -r requirements.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup
