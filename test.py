def toTxtFile(fn):                     # 函数定义
    with open(fn, 'a') as fp:          # 函数体开始，相对def缩进4个空格
        for i in range(10):            # with块开始，相对with缩进4个空格
            if i%3==0 or i%7==0:       # 选择结构开始，再缩进4个空格
                fp.write(str(i)+'\n')  # 语句块，再缩进4个空格
            else:                      # 选择结构的第else分支，与if对齐
                fp.write('ignored\n')
        fp.write('finished\n')         # for循环结构结束
    print('all jobs done')             # with块结束
toTxtFile('/writetest/text.md')
