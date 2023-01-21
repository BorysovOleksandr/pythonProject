my_list = ['Thomas Wolfe', 'Jeffrey Leonard', 'Pamela Murphy', 'Mark Nelson', 'Jeffrey Leonard', 'Mary Kennedy',
           'Denise Olson', 'Lydia Stanley', 'Thomas Wolfe', 'Jorge Allen', 'Lydia Stanley']
n_d_l = []
for i in my_list:
    if i not in n_d_l:
        n_d_l.append(i)
print('Non-duplicated list : ', n_d_l)
