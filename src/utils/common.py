import importlib

def get_lib_func_object(lib_name: str, func_name: str = ''):
    lib = importlib.import_module(lib_name)
    if not str:
        return lib
    return getattr(lib, func_name)

def get_cron_job(job_lib_str: str):
    s = job_lib_str.split('.')
    return '.'.join(s[0: -1]), s[-1]