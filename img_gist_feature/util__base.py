# -*- coding: utf-8 -*-

import os
import sys
import cv2
import shutil
import imghdr
import numpy as np
from PIL import Image


S_NOW_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(S_NOW_DIR)



# Creat Directory
def recur_mkdir(s_path, run_logger=None, b_print=False):  
    if os.path.exists(s_path) and os.path.isdir(s_path):
        s_msg = "%s has been created" % s_path
        run_logger and run_logger.warning(s_msg)
        b_print and print(s_msg)
        return 1
    else:
        try:
            os.makedirs(s_path)
            
            s_msg = "%s create" % s_path
            run_logger and run_logger.info(s_msg)
            b_print and print(s_msg)
            return 0
        except Exception as e:
            s_msg = "%s" % str(e)
            run_logger and run_logger.error(s_msg)
            b_print and print(s_msg)      
            return -1


# Copy a file or directory
def cp_file_dir(s_in_url, s_out_url, run_logger=None, b_print=False):
    if os.path.isfile(s_in_url):
        try: 
            shutil.copyfile(s_in_url, s_out_url) # Copy a old file to tmp dir 
            return 0
        except Exception as e:
            s_msg = 'Err: cant''t copy %s to %s, %s' % (s_in_url, s_out_url, str(e))
            run_logger and run_logger.error(s_msg)
            b_print and print(s_msg)
            return -1
    elif os.path.isdir(s_in_url):
        try:   
            n_ret = 0  
            if os.path.exists(s_out_dir) and os.path.isdir(s_out_dir):
                n_ret = rm_dir(s_out_dir)
            if os.path.exists(s_out_dir) and os.path.isfile(s_out_dir):
                n_ret = rm_file(s_out_dir)
            n_ret == 0 and shutil.copytree(s_in_dir, s_out_dir) # using copytree
            return n_ret
        except Exception as e:
            s_msg = 'Err: cant''t copy %s to %s, %s' % (s_in_dir, s_out_dir, str(e))
            run_logger and run_logger.error("%s" % s_msg)
            b_print and print(s_msg)
            return -1

# Move a file or directory
def mv_file_dir(s_in_url, s_out_url, run_logger=None, b_print=False):
    try: 
        shutil.move(s_in_url, s_out_url) # using shutil.move
        return 0
    except Exception as e:
        s_msg = 'Err: cant''t copy %s to %s, %s' % (s_in_url, s_out_url, str(e))
        run_logger and run_logger.error(s_msg)
        b_print and print(s_msg)  
        return -1
    

# Delete a file
def rm_file_dir(s_in_url, run_logger=None, b_print=False):
    try:
        if os.path.exists(s_in_url): # is a directory
            shutil.rmtree(s_in_url) 
            return 0
        else:
            s_msg = 'Err: not exists %s' % (s_in_url)
            run_logger and run_logger.error(s_msg)
            b_print and print(s_msg)
            return 1
    except Exception as e:
         s_msg = 'Err: cant'' remove %s, %s' % (s_in_url, str(e))
         run_logger and run_logger.error(s_msg)
         b_print and print(s_msg)
         return -1

# Get right string
def get_usable_str(s_in):
    s_tmp = s_in  
    s_unvalid = '<>,\/|,:.,''",*,?\t\r\n'
    for ch in s_unvalid:
        s_tmp = s_tmp.replace(ch,'')
    s_tmp = s_tmp.replace(u'\u3000','')
    
    return s_tmp