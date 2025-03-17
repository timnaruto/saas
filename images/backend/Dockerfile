# Set the Python version as a build-time argument
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}


# Install Pipenv
RUN pip install --no-cache-dir pipenv

# Create and set the working directory
RUN mkdir -p /backend
WORKDIR /backend

# Copy Pipenv files and project code
COPY images/backend/Pipfile images/backend/Pipfile.lock ./
COPY images/backend/ ./images/backend/
COPY .env .gitignore LICENSE Makefile railway.json README.md saas.code-workspace ./

# Install dependencies into a Pipenv-managed virtual environment
RUN pipenv install --deploy --system

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the Django default project name
ARG PROJ_NAME="saas"

# Create a bash script to run the Django project
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "pipenv run python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "pipenv run gunicorn ${PROJ_NAME}.wsgi:application --bind \"[::]:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# Grant execute permission to the script
RUN chmod +x ./paracord_runner.sh

# Command to run the script
CMD ["./paracord_runner.sh"]
