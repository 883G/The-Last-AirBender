from hypothesis import strategies as st

POSITIVE_INTEGERS: st.SearchStrategy[int] = st.integers(min_value=0)

NEGETIVE_INTEGERS: st.SearchStrategy[int] = st.integers(max_value=-1)
