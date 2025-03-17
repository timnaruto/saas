# Set the Python version as a build-time argument
# with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # for compilation
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Pipenv
RUN pip install --no-cache-dir pipenv

# Create and set the working directory
RUN mkdir -p /code
WORKDIR /code

# Copy Pipenv files and project code
COPY images/backend/Pipfile images/backend/Pipfile.lock ./
COPY images/backend/ ./images/backend/
COPY .env .gitignore LICENSE Makefile railway.json README.md saas.code-workspace ./

# Install dependencies into a Pipenv-managed virtual environment
RUN pipenv install --deploy

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Since requirements.txt is present, install it as a fallback (optional)
# Uncomment if you need both Pipenv and requirements.txt
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set the Django default project name
ARG PROJ_NAME="saas"

# Create a bash script to run the Django project
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "pipenv run python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "pipenv run gunicorn ${PROJ_NAME}.wsgi:application --bind \"[::]:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# Make the bash script executable
RUN chmod +x paracord_runner.sh

# Clean up to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the Django project via the runtime script
CMD ./paracord_runner.sh