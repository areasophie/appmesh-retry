import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 5000))
proc_name = 'App Mesh Retry Client App'
workers = 1
