import sys
import json

def read_env_file(filename):
    f = open(filename, "r")
    values = {}
    for line in f:
        v = line.split('=', 1)
        if len(v) > 1:
            values[v[0].strip().lower()] = v[1].strip()
    return values

def init():
    settings = {'config_file': None}

    argv = list(sys.argv)
    argv.pop(0)

    while(len(argv) > 0 and argv[0].startswith("--")):
        param = argv.pop(0)
        if param == "--config":
            settings['config_file'] = argv.pop(0)
            continue
        if param.startswith("--config="):
            settings['config_file'] = param.split('=', 1)[1]
            continue
        print("unknown argument {}".format(param), file=sys.stderr)
        pass

    if settings['config_file']:
        settings.update(read_env_file(settings['config_file']))

    return settings, argv

