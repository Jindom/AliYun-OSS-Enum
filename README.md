# AliYun_OSS_Enum

This tools is for AliYun OSS permission check and enumeration. 
A bucket with inappropriate permission configuration may cause information leakage and economic loss.

## Usage

### Please make sure install aliyun oss python package first:
```
pip3 install oss2
```
### Download this Repo and Run the AliYun_OSS_Enum.py file
### Also don't forget to input your AliYun API Key to the file, you may get your API in 
```https://ram.console.aliyun.com/manage/ak```

```
git clone https://github.com/Jindom/AliYun_OSS_Enum
cd Aliyun_OSS_Enum/

python3 AliYun_OSS_Enum.py http://oss-cn-zhangjiakou.aliyuncs.com example_bucket_name
```


![](https://i.imgur.com/AsMN6xP.png)
