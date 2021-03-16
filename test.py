# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
from fnmatch import fnmatch, fnmatchcase
import os
import shutil


# 在PDF文件中找到指定字符串的函数
def find_pdf_string(strings):
    # 找到当前py脚本的根目录
    path = os.getcwd()
    files = os.listdir(path)
    have_find_cnts = 0
    if os.path.exists("output.txt") == 1:
        os.remove("output.txt")
    # 遍历查找
    for file in files:
        if file.find(".pdf") != -1:
            find_flag = 0
            fp = open(file, 'rb')
            # 来创建一个pdf文档分析器
            parser = PDFParser(fp)
            # 创建一个PDF文档对象存储文档结构
            document = PDFDocument(parser)
            # 检查文件是否允许文本提取
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
            else:
                # 创建一个PDF资源管理器对象来存储共赏资源
                rsrcmgr = PDFResourceManager()
                # 设定参数进行分析
                laparams = LAParams()
                # 创建一个PDF设备对象
                # device=PDFDevice(rsrcmgr)
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释器对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                # 处理每一页
                for page in PDFPage.create_pages(document):
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    for x in layout:
                        if isinstance(x, LTTextBoxHorizontal) and x.get_text().find(strings) != -1:
                            have_find_cnts += 1
                            with open('output.txt', 'a', encoding ='utf-8') as f:
                                if find_flag == 0:
                                    # 在输出文档里写文件名并且复制一份到新文件夹中
                                    find_flag = 1
                                    f.write(fp.name + '\n')
                                    pathnew = path + "//new"
                                    path_find = pathnew + "//" + strings
                                    if os.path.exists(pathnew) != 1:
                                        os.makedirs(pathnew)
                                    if os.path.exists(path_find) != 1:
                                        os.makedirs(path_find)
                                    # 复制文件到FORMQL里面
                                    shutil.copy(file, path_find + "//" + file)
                                # 写找到的数据
                                f.write("   " + x.get_text() + '\n')
    return have_find_cnts


if __name__ == '__main__':
    input_str = input("请输入想要搜索的文字（请不要输入标点符号）按回车键确定\n")
    print("finding......\n")
    output_str = find_pdf_string(input_str)
    print("查找完成，共找到" + str(output_str) + "个，具体结果可见output.txt，如果找到的结果大于1个，在new文件夹中对应名字的文件夹中已复制完成\n")
