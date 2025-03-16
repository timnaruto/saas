.PHONY: runserver migrate makemigrations shell createsuperuser collectstatic test update update-all

# Variables
PYTHON = python3  # Use python3 for consistency; adjust if needed
MANAGE = $(PYTHON) images/backend/manage.py

# Run Django development server
runserver:
	$(MANAGE) runserver

# Apply database migrations
migrate:
	$(MANAGE) migrate

# Create database migrations
makemigrations:
	$(MANAGE) makemigrations

# Open Django shell
shell:
	$(MANAGE) shell

# Create a superuser
createsuperuser:
	$(MANAGE) createsuperuser

# Collect static files
collectstatic:
	$(MANAGE) collectstatic

# Run tests
test:
	$(MANAGE) test

# Update project (e.g., for production deployment)
update:
	git pull
	pip install -r images/backend/requirements.txt
	$(MANAGE) migrate
	$(MANAGE) collectstatic --noinput  # --noinput avoids prompts
	sudo systemctl restart nginx

# Full update for development (excluding runserver)
update-all: makemigrations migrate collectstatic runserver
	@echo "Update complete. Run 'make runserver' to start the server."
