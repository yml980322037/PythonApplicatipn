import os,datetime,json
from tkinter import *
import tkinter.messagebox as messagebox


def handle():
    log_json = {}
    if len(date_input.get().strip())==0:
        messagebox.showinfo('警告', '时间为空！')
    elif len(title_input.get())==0:
        messagebox.showinfo('警告', '标题为空！')
    #分类可为空
    else:

        log_json['date'] = date_input.get()  # 输入的时间
        log_json['title']=title_input.get()
        log_json['url']=url_input.get()
        log_json['category']=category_input.get()
        print('新增数据：',log_json)
        print()
        all_json=read_json()
        all_json.append(log_json)
        print('全部数据：')
        for i in range(len(all_json)):
            print(str(i),':',all_json[i])
        with open(filePath, "w") as f:
            jjson=json.dumps(all_json,indent=4)#格式化输出
            f.write(jjson)
        print("添加成功...")


class BlogLog(object):
    def __init__(self, date, title,url,category):
        self.date = date
        self.title = title
        self.url = url
        self.category = category



def read_json():
    print('历史数据：')
    with open(filePath, "r", encoding='utf8') as f:
        list=json.load(f)
    for log in list:
        print(log)
    print()
    return list


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    root.geometry(size)


if __name__ == '__main__':

    filePath='log.txt'
    tk = Tk()
    #tk.geometry('286x260')
    center_window(tk, 286, 260)
    tk.title('日志工具')  # 窗口标题
    counter_down = Label(tk)
    counter_down.config(font=("Courier", 12))
    counter_down.grid(row=0,column=2)
    counter_down['text'] = '日志工具'

    Label(tk, text="时间").grid(row=1,column=1)
    Label(tk, text="标题").grid(row=2,column=1)  # 第2行
    Label(tk, text="链接").grid(row=3, column=1)  # 第3行
    Label(tk, text="默认为#").grid(row=3, column=3)  # 第3行
    Label(tk, text="分类").grid(row=4, column=1)  # 第5行
    Label(tk, text="").grid(row=5, column=0)  # 第6行

    #时间控件
    date_input = Entry(tk)
    date_input.grid(row=1, column=2)
    date_input.insert(END,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    #标题控件
    title_input = Entry(tk)
    title_input.grid(row=2, column=2)
    #链接控件
    url_input = Entry(tk)
    url_input.grid(row=3, column=2)
    url_input.insert(END,'#')
    #分类控件
    category_input = Entry(tk)
    category_input.grid(row=4, column=2)

    btn = Button(tk, text='添加日志', command=handle).grid(row=6, column=2)
    # refresh_down = Label(tk)
    # refresh_down.config(font=("Arial", 11),bg='green')
    # refresh_down.grid(row=7, column=2)
    # refresh_down['text'] = '暂无状态...'

    tk.mainloop()
    if tk.quit() is not True:
        os._exit(0)  # 退出






