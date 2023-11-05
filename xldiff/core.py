import os
from io import TextIOBase, BufferedReader

from listorm import read_csv, read_excel, diff



def read_file(file, *args, **kwargs):
    if isinstance(file, str):
        _, ext = os.path.splitext(file)
        if ext == '.csv':
            return read_csv(file, *args, **kwargs)
        if ext in ['.xlsx', '.xls']:
            return read_excel(file, *args, **kwargs)
    elif isinstance(file, TextIOBase):
        return read_csv(file, *args, **kwargs)
    elif isinstance(file, BufferedReader):
        return read_excel(file, *args, **kwargs)    
    raise ValueError('Invalid file format or path')
        


def xldiff(pre, post, keys:list, *args, targets=None, **kwargs):
    pre = read_file(pre, *args, **kwargs)
    post = read_file(post, *args, **kwargs)
    if targets:
        return diff(pre, post, pk=keys, targets=targets)
    return diff(pre, post, pk=keys)




