# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.0
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="Plone Foundation <collective@plone.org>" \
      org.label-schema.name="sinap-backend" \
      org.label-schema.description="Sinap backend image." \
      org.label-schema.vendor="Plone Foundation"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN <<EOT
    ./bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    ./bin/mxdev -c mx.ini
    ./bin/pip install -r requirements-mxdev.txt
    chown -R plone: /app
EOT
