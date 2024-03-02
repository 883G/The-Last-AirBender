from hypothesis import strategies as st

POSITIVE_INTEGERS: st.SearchStrategy[int] = st.integers(min_value=0)

NEGETIVE_INTEGERS: st.SearchStrategy[int] = st.integers(max_value=-1)

ENVIRONMENT_VARIABLES: st.SearchStrategy[str] = st.text(
    alphabet=st.characters(
        codec="UTF",
        # Removed wierd categories to avoid wierd errors
        # when patching envs.
        exclude_categories={
            "Cc",
        },
    ),
)
