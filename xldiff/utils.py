import os

def order_pre_post(path1, path2, how='name'):
    '''
    :param how: name|created|updated, defaults to 'name'
    '''
    files = [path1, path2]
    if how == 'name':
        files.sort()
    elif how == 'created':
        files.sort(key= lambda f: os.path.getctime(f))
    elif how == 'updated':
        files.sort(key= lambda f: os.path.getmtime(f))
    return files


def make_diff_file_name(f1, f2, ext='.xlsx'):
    f1 = os.path.basename(f1)
    f2 = os.path.basename(f2)
    f1, _ = os.path.splitext(f1)
    f2, _ = os.path.splitext(f2)
    return f'{f1}~{f2}{ext}'