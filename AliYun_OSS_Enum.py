#!/usr/bin/python3
# coding=utf-8

import os
import sys
import json
import oss2
from itertools import islice

"""
AliYun OSS Enumeration Tool
Author: Jindom Jin
Version: v0.0.1
"""

"""
请在下面填入你的阿里云API凭据
获取地址:https://ram.console.aliyun.com/manage/ak
"""
auth = oss2.Auth('API KEY', 'API SERCET')

if len(sys.argv) <= 2:
    print("请提供OSS区域地址和BucketName!")
    sys.exit()


def oss_upload(location, bucketname):
    sample_file = os.path.abspath(os.path.dirname(os.path.abspath(
        __file__)) + os.path.sep + ".") + "/upload_sample.txt"
    bucket = oss2.Bucket(auth, location, bucketname)
    bucket.put_object_from_file('sample_file.txt', sample_file)
    print("\033[1;32m 匿名上传示例文件成功\033[0m")


def oss_list(location, bucketname):
    bucket = oss2.Bucket(auth, location, bucketname)
    for b in islice(oss2.ObjectIterator(bucket), 5):
        print(b.key)
    print("\033[1;32m 匿名尝试列举目录成功，已显示最近的5个文件\033[0m")


def oss_delete(location, bucketname):
    bucket = oss2.Bucket(auth, location, bucketname)
    bucket.delete_object('sample_file.txt')
    print("\033[1;32m 匿名尝试删除示例文件成功\033[0m")


if __name__ == '__main__':
    try:
        oss_upload(sys.argv[1], sys.argv[2])
    except KeyboardInterrupt:
        print("用户退出...")
    except Exception as ex:
        if "The bucket you are attempting to access must be addressed using the specified endpoint" in str(ex):
            print(json.loads(str(ex).replace("\'", "\""))["details"]["Endpoint"])
            print("\033[1;31m 请确认OSS地区是否输入正确\033[0m")
            print("\033[1;34m API返回正确的地区应为\033[0m http://" + json.loads(str(ex).replace("\'", "\""))["details"]["Endpoint"] )
            sys.exit()
        print("\033[1;31m 无匿名上传权限\033[0m")
    try:
        oss_list(sys.argv[1], sys.argv[2])
    except KeyboardInterrupt:
        print("用户退出...")
    except Exception as ex:
        print("\033[1;31m 无匿名列举权限\033[0m")
    try:
        oss_delete(sys.argv[1], sys.argv[2])
    except KeyboardInterrupt:
        print("用户退出...")
    except Exception as ex:
        print("\033[1;31m 无匿名删除权限\033[0m")
