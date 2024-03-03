"""
------Intuitions
->Try to use stack (using a list and only using append and pop methods).
->Instead Running into 2 loops, one for traversing and one for looking ahead.
->Put indices in the stack.
"""


def daily_temperatures(self, temperatures):
    st = []
    res = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while st and temperatures[st[-1]] < temp:
            index = st.pop()
            res[index] = i - index
        st.append(i)

    return res
