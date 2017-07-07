用Python2.7爬取网站的图片


首先调用ullib2的urlopen方法打开博客网址，获取网址代码


接着运用正则表达式搜索含有图片的网址并筛选出来


用for循环将图片的网址用open方法打开并用二进制写入，命名文件名，保存到与Test.py同级目录中


用BeautifulSoup方法获取博客指定文字，没有成功（WARNING:root:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.）



