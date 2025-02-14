✅ Use python:slim images instead of full python images.
✅ Always use .dockerignore to exclude unnecessary files.
✅ Leverage multi-stage builds to keep images small.
✅ Avoid running as root (USER 1000 for security).
✅ Use environment variables (ENV VAR=value) instead of hardcoded values.
✅ Persist data using Docker volumes (volumes: in docker-compose.yml).