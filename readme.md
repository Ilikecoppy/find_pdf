本脚本用来根据excel中某一列的名称，在文件夹内查找对应名称的文件，并且将其重新归类，具体注意事项如下：

1、脚本运行需要的环境 python + pdfminer + shutil，其中pdfminer是用来处理pdf文件的，shutil是copy文件的，这个一般默认会带，所以需要安装的是pdfminer
安装步骤：
	1）在windows cmd/powershell（这两个都行）里输入：pip3 install pdfminer来安装pdfminer

2、安装完成以后需要将test.py这个脚本放在所有.pdf的目录下

3、在windows的CMD/POWERSHEEL中找到test.py所在的文件夹下，然后输入：python3 .\test.py  或者 python .\test.py（具体看python版本），然后根据提示输入想要查找的字符即可
