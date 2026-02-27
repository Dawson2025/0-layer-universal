"""
Gunicorn configuration for Language Tracker production deployment
"""
import multiprocessing
import os

# Server socket
bind = f"0.0.0.0:{os.getenv('PORT', '5000')}"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = 'logs/gunicorn-access.log'
errorlog = 'logs/gunicorn-error.log'
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'lang-trak'

# Server mechanics
daemon = False
pidfile = 'gunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (if needed)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'

# Application
chdir = os.getenv('APP_ROOT', '/home/dawson/code/lang-trak-in-progress')
wsgi_app = 'app:app'

# Restart workers gracefully
max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 30

# Pre/post hooks
def on_starting(server):
    """Called just before the master process is initialized."""
    print("🚀 Starting Language Tracker production server...")

def on_reload(server):
    """Called to recycle workers during a reload via SIGHUP."""
    print("🔄 Reloading workers...")

def when_ready(server):
    """Called just after the server is started."""
    print(f"✅ Language Tracker ready on {bind}")
    print(f"👷 Workers: {workers}")

def worker_int(worker):
    """Called just after a worker exited on SIGINT or SIGQUIT."""
    print(f"⚠️  Worker {worker.pid} interrupted")

def on_exit(server):
    """Called just before exiting gunicorn."""
    print("👋 Language Tracker shutting down...")

