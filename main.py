from tkinter import *
from dateutil.relativedelta import relativedelta
import datetime

root = Tk()
root.title("Nado GUI")
root.geometry("320x310")  # 가로 * 세로
#root.geometry("1280x720+300+100")  # 가로 * 세로 + x좌표 + y좌표

career_frame = LabelFrame(root, width=300, height=300, text="경력계산기")
Label(career_frame, text="재직기간을 입력하세요. (YYYY.MM)").pack(pady=10)

career_entry_frame = Frame(career_frame)
career_entry1 = Entry(career_entry_frame, width=10)
career_entry1.grid(row=1, column=0, ipady=3, sticky=N+W+S, pady=3)
Label(career_entry_frame, text="~").grid(row=1, column=1, sticky=N+S, pady=3)
career_entry2 = Entry(career_entry_frame, width=10)
career_entry2.grid(row=1, column=2, ipady=3, sticky=N+E+S, pady=3)
#career_entry1.pack(ipady=3, pady=10, side="left")

def cal_career():
    try:
        c1 = career_entry1.get()
        c2 = career_entry2.get()
        if len(c1) == 7 and len(c2) == 7:
            if c1[4] == "." and c2[4] == ".":
                if int(c2[:4]) - int(c1[:4]) >= 0:
                    if int(c1[5:7]) < 13 and int(c2[5:7]) < 13:
                        cal_career_result = relativedelta(years=int(c2[:4]), months=int(c2[5:7]), day=1)\
                            - relativedelta(years=int(c1[:4]), months=int(c1[5:7]))
                        if int(c1[5:7]) > int(c2[5:7]):
                            print(int(c1[:4]), int(c2[:4]))
                            if int(c1[:4]) == int(c2[:4]):
                                print("오류3")
                            else:
                                print("1")
                                career_result.config(text="총 경력은 {0}년 {1}개월 입니다.".format(cal_career_result.years - 1, 12 + cal_career_result.months))
                        else:
                            print("2")
                            career_result.config(text="총 경력은 {0}년 {1}개월 입니다.".format(cal_career_result.years, cal_career_result.months))
                    else:
                        raise
                else:
                    raise
            else:
                raise
        else:
            raise 
    except:
        career_result.config(text="잘못된 입력값입니다.", width=250)

cal_btn = Button(career_frame, text="경력 계산하기", command=cal_career)#, command=versa_cal_fun)

career_result_frame = LabelFrame(career_frame, text="결과", width=250, height=80)
career_result = Label(career_result_frame, text="", width=250)

career_frame.pack(padx=5, pady=5)
career_entry_frame.pack(pady=10)
cal_btn.pack(pady=5)
career_result_frame.pack(padx=10, pady=10, ipady=5)
career_result.pack()

root.resizable(True, True)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()