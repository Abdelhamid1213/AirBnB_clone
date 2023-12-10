#!/usr/bin/python3
"""Initialize the models directory with a FileStorage instance."""

from models.engine.file_storage import FileStorage

# Create a FileStorage instance for handling storage operations
storage = FileStorage()

# Reload existing data from storage
storage.reload()
