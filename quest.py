# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
# ONLY FOUR BASIC OPS!!!
from rapid_latex_ocr import LatexOCR

def getquestion():
    model = LatexOCR()

    question_array = []
    for i in range(1, 7):
        img_path = "tests/test_files/" + str(i) + ".png"
        with open(img_path, "rb") as f:
            data = f.read()

        res, elapse = model(data)

        while "\\times" in res:
            res = res.replace("\\times", "*")

        while "\\div" in res:
            res = res.replace("\\div", "/")

        # print(res)
        # print(eval(res))
        question_array.append(str(eval(res)))

    print("-- calculated result --")
    print(question_array)
    return question_array