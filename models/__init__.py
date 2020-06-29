#!/user/bin/python3
"""models module
"""


from models.engine.file_storage import FileStorage
"""
	Create a unique FileStorage instance.
"""

storage = FileStorage()
storage.reload()
