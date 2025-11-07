import streamlit as st
import random

def generate_question():
    # 1부터 20까지의 숫자 중에서 무작위로 선택
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    # 덧셈 또는 뺄셈 무작위 선택
    operation = random.choice(['+', '-'])
    
    if operation == '+':
        answer = num1 + num2
    else:
        # 뺄셈의 경우 큰 수에서 작은 수를 빼도록 조정
        num1, num2 = max(num1, num2), min(num1, num2)
        answer = num1 - num2
    
    return num1, operation, num2, answer

def main():
    st.title('덧셈과 뺄셈 연습')
    
    # 세션 상태 초기화
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
        st.session_state.problems = []

    # 3문제를 모두 풀었는지 확인
    if st.session_state.current_question >= 3:
        st.success(f'연습이 끝났습니다! {st.session_state.correct_answers}문제를 맞추셨습니다!')
        if st.button('다시 시작하기'):
            st.session_state.current_question = 0
            st.session_state.correct_answers = 0
            st.session_state.problems = []
            st.rerun()
        return

    # 새로운 문제 생성
    if len(st.session_state.problems) <= st.session_state.current_question:
        st.session_state.problems.append(generate_question())

    # 현재 문제 가져오기
    num1, operation, num2, correct_answer = st.session_state.problems[st.session_state.current_question]

    # 문제 표시
    st.write(f"### 문제 {st.session_state.current_question + 1}/3")
    st.write(f"{num1} {operation} {num2} = ?")

    # 사용자 입력
    user_answer = st.number_input('답을 입력하세요:', value=None, placeholder="여기에 답을 입력하세요")
    
    if st.button('제출'):
        if user_answer == correct_answer:
            st.success('정답입니다! 👏')
            st.session_state.correct_answers += 1
        else:
            st.error(f'틀렸습니다. 정답은 {correct_answer}입니다.')
        
        st.session_state.current_question += 1
        st.rerun()

if __name__ == "__main__":
    main()
