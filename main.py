import re

# 下面是我誤會題目意思做出來的廢品QQ
# def t(text):
#     i = []
#     for x in text:
#         if x not in i:
#             i.append(x)
#     ans = ''
#     for j in i:
#         ans += j
#     return ans
#
#
# a = '山外山青龍山'
# print(t(a))
# # ------


def compare(add=[], minus=[], equal=''):
    if type(equal) != type([]):
        raise 'equal need is []'
    left = 0
    right = len(equal)
    for i in add:
        left += int(i)
    for i in minus:
        left -= int(i)
    if left == int(equal[0]):
        return True
    else:
        return False


def renew_map(u_len, unknown, now_tag):
    map_ed = {}
    for i in range(0, u_len):
        map_ed[unknown[i]] = now_tag[i]
    return map_ed


# text_list = equal
# text_list

def fm3294(text_list, map_ed):
    # if text_list == []:
    #     return []
    for i in range(0, len(text_list)):
        # print(text_list[i])
        for k in map_ed:
            # print(k)
            if k in text_list[i]:
                # r = re.compile(f'{k}')
                text_list[i] = re.sub(k, map_ed[k], text_list[i])
                # print(text_list[i])
    return text_list


# 這裡改三個變數內容
add = ['山外山', '青龍山']
minus = []
equal = ['青龍山外']

# add = ['一二三', '三二一']
# minus = []
# equal = ['四四四']


k = add.copy()
k.extend(minus)
k.extend(equal)
unknown = []
for i in k:
    for j in i:
        if j not in unknown:
            unknown.append(j)
        # print(j)
u_len = len(unknown)

# ----
max_m0 = int(u_len * '9')
for i in range(0, max_m0 + 1):
    # for i in range(0, 5):
    #     # print(i)
    s = '{:0>max_m0d}'.replace('max_m0',str(u_len))
    now_tag = list(s.format(i))
    map_ed = renew_map(u_len, unknown, now_tag)
    add_ed = fm3294(add.copy(), map_ed)
    minus_ed = fm3294(minus.copy(), map_ed)
    equal_ed = fm3294(equal.copy(), map_ed)
    # 取代完成後開始排左右--------
    if compare(add_ed, minus_ed, equal_ed):
        print('==============')
        print(f'add = {add_ed}')
        print(f'minus = {minus_ed}')
        print(f'equal = {equal_ed}')
