vip_seat_1 = 'Lydia Stanley'
vip_seat_2 = 'Jorge Allen'
vip_seat_3 = 'Thomas Wolfe'
vip_seat_4 = 'Mary Kennedy'
vip_seat_5 = 'Denise Olson'

com_seat_1 = 'Robert Wilson'
com_seat_2 = 'Jeffrey Leonard'
com_seat_3 = 'Pamela Murphy'
com_seat_4 = 'Mark Nelson'
com_seat_5 = 'Sharon Ford'
com_seat_6 = 'David Mendoza'
com_seat_7 = 'Lydia Stanley'
com_seat_8 = ''
com_seat_9 = ''
com_seat_10 = ''

VIP_box = (vip_seat_1, vip_seat_2, vip_seat_3, vip_seat_4, vip_seat_5)
comm_room = (com_seat_1, com_seat_2, com_seat_3, com_seat_4, com_seat_5, com_seat_6, com_seat_7, com_seat_8, com_seat_9,
             com_seat_10)
VIP_guests = set(VIP_box)
Common_guest = set(comm_room)
Common_guest.remove('')

print('VIP Guests:', VIP_guests)
print('Common Guests:', Common_guest)
