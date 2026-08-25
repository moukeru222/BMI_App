import streamlit as st


# 入力された身長と体重が正しいかチェックする関数
def check_input(height, weight):
    return height > 0 and weight > 0


# BMIを計算する関数
def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)


# BMIの数値から判定結果を返す関数
def judge_bmi(bmi):
    if bmi < 18.5:
        return "低体重"
    elif bmi < 25:
        return "普通体重"
    else:
        return "肥満"


# アプリのタイトル
st.title("BMI計算アプリ")
st.write("身長と体重からBMIを計算します。")

# 身長と体重を入力
height = st.number_input("身長（cm）", value=170.0)
weight = st.number_input("体重（kg）", value=60.0)


# 「計算する」ボタンが押されたら処理する
if st.button("計算する"):

    # 入力値をチェック
    if check_input(height, weight):

        # BMIを計算
        bmi = calculate_bmi(height, weight)

        # BMIを表示
        st.write("あなたのBMIは", round(bmi, 1))

        # BMIを判定
        result = judge_bmi(bmi)

        # 判定結果を表示
        st.write("判定：", result)

    else:

        # 入力値が不正だった場合
        st.write("身長と体重は0より大きい値を入力してください。")