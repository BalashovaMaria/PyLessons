import math
figura=input('krug or treyg or premoug:')
if figura== 'krug':
    rkruga=int(input('radius:'))
    print('ploshad kruga =',round(math.pi * (rkruga**2),2))
elif figura== 'treyg':
    sa=int(input('storona1:'))
    sb=int(input('storona2:'))
    sc=int(input('storona3:'))
    polper=(sa+sb+sc)/2
    print('ploshad treyg = ',round(math.sqrt((polper*(polper-sa)*(polper-sb)*(polper-sc))),2))
elif figura== 'premoug':
    st1=int(input('storona1:'))
    st2=int(input('storona2:'))
    print('ploshad premoug=',st1 * st2)
else:
    print('error')
