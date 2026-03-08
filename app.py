"""Streamlit 웹페이지 테스트용 간단한 숫자 덧셈 앱."""

import streamlit as st


def main() -> None:
    """숫자 입력과 덧셈 결과를 보여주는 메인 앱."""
    st.title("숫자 덧셈 테스트")
    st.write("웹페이지가 정상적으로 보이는지 확인해보세요.")

    col1, col2 = st.columns(2)
    with col1:
        num1: float = st.number_input(
            "첫 번째 숫자",
            value=0.0,
            step=1.0,
            key="num1",
        )
    with col2:
        num2: float = st.number_input(
            "두 번째 숫자",
            value=0.0,
            step=1.0,
            key="num2",
        )

    if st.button("덧셈 결과 보기"):
        result: float = num1 + num2
        st.success(f"결과: **{num1} + {num2} = {result}**")


if __name__ == "__main__":
    main()
