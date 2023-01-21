casino_blacklist = {'Lydia Stanley', 'Michael Bailey', 'Janet Richardson', 'Mary Curtis', 'Michael Davis',
                    'Harold Johnson', 'Denise Olson'}
poker_blacklist = {'Lydia Stanley', 'Jorge Allen', 'Thomas Wolfe', 'Mary Kennedy', 'Denise Olson'}
alcohol_blacklist = {'Robert Wilson', 'Jeffrey Leonard', 'Pamela Murphy', 'Mark Nelson', 'Sharon Ford',
                     'David Mendoza', 'Lydia Stanley', 'Janet Richardson'}
print("Persona Non-Grata:", casino_blacklist.intersection(poker_blacklist).intersection(alcohol_blacklist))
