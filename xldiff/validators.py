import os


def validate_argvs(argvs):
    args = []
    for arg in argvs:
        _, ext = os.path.splitext(arg)
        if ext in ['.csv', '.xlsx', '.xls']:
            args.append(arg)
    
    if len(args) < 2:
        raise ValueError('Needed two of excel or csv file')
    return args[:2]
