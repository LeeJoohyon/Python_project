champion = 'Lux'

def local1():
     champion = 'Ahri'
     print('local1 local() : {}'.format(locals()))

    def local2():
        champion = 'Ezreal'
        print('local2 local() : {}'.format(locals()))
       
       local2()

print('global locals() : {}'.format(locals()))
local1()

