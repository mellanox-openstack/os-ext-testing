def set_log_path(item, job, params):
    path = "%s/%s" % (params['ZUUL_CHANGE'], params['ZUUL_PATCHSET'])
    params['LOG_PATH'] = '/'.join([path, job.name])
