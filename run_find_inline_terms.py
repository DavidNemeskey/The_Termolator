#!/usr/bin/env python3
import os
import sys

from find_terms import *

def main(args):
    global special_domains
    file_list = args[1]
    if len(args)>2:
        outfile_prefix = args[2]
    else:
        outfile_prefix = False
    if (len(args)>3) and (args[3].lower() != 'false'):
        special_domains.extend(args[3].split('+'))
    initialize_utilities()
    find_inline_terms_for_file_list(file_list,dict_prefix=outfile_prefix)

if __name__ == '__main__': sys.exit(main(sys.argv))
