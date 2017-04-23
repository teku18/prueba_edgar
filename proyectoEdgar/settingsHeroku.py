from .settings import *

ATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dafv37kjdht035',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'nqywcnppegmafd',
        'PASSWORD': '576fd4962cb947ece851955071f0e0007ace5975e71560eb3453f51a993bcc18',
        'HOST': 'ec2-54-163-224-108.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}