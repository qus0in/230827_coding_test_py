T = int(input())
# print(T)

for tc in range(1, T+1):
    # print('tc', tc)
    text = input()
    st = []
    for t in text:
        if len(st) and st[-1] == '(' and t == ')':
            st.pop()
        else:
            st.append(t)
        # print(st)
    print('NO' if st else 'YES')
