连接github服务器

c盘用户.ssh目录下config内容如下。
host只写github，不用写用户名，连接到哪个github用户，由源码.git中config的url指定。私钥文件存储在同目录下。公钥中的文本全拷贝后粘贴在github的新建ssh中。
# 加两个密钥。
# Host github
Host github
  User git
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa_oucwy
  IdentityFile ~/.ssh/id_rsa_markwy

开发目录.git下的config:
# 可通过url = git@github_oucwy:oucwy/py.git来区分连接到github哪个用户。
# 根据@后的主机名查找.ssh/config中的Host，匹配则连接。
[remote "origin"]
	# url = git@github.com:oucwy/py.git
	url = git@github:oucwy/py.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
[user]
	email = wangyong@ouc.edu.cn
	name = oucwy