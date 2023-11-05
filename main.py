import sys
from xldiff.validators import validate_argvs
from xldiff.utils import order_pre_post, make_diff_file_name
from xldiff.core import xldiff
from listorm import write_excel, insert_excel

keys = ('상품ID',)

if __name__ == '__main__':
    pre, post = validate_argvs(sys.argv)
    pre, post = order_pre_post(pre, post)

    changes = xldiff(pre, post, keys)
    save_to = make_diff_file_name(pre, post)
    created = [added.rows for added in changes.added]
    deleted = [added.rows for added in changes.deleted]
    print(changes.updated)
    # insert_excel(changes.updated, save_to, sheet_name='Updated')
    # insert_excel(created, f'./{save_to}', sheet_name='Created')
    # insert_excel(deleted, save_to, sheet_name='Deleted')
    