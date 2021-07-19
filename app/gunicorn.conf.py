from multiprocessing import cpu_count

# TODO: possible split between dev/prod gunicorn configuration

reload = True
workers = cpu_count() * 2 + 1
preload_app = True

bind = "0.0.0.0:8000"
timeout = 30
max_requests_jitter = 1000

loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
capture_output = False
errorlog = '-'


def pre_request(worker, req):
    worker.log.info('%s %s', req.method, req.path)
