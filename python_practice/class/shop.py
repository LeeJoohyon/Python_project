
class Shop:
    description = 'python Shop class'
    def __init__(self,name,shop_type,address):
        self._name = name
        self._shop_type = shop_type
        self._address = address

    def get_info(self):
        return print('상점정보(%s)' % self.__name)
        print('유형:%s' % self.__shop_type)
        print('주소:%s' % self.__address)


    def show_info(self):
        print('상점정보(%s)'% self._name)
        print('유형:%s' % self._shop_type)
        print('주소:%s' % self._address)

    #def change_type(self,market_type):
    #   self.__shop_type = market_type

    @classmethod
    def change_descrption(cls, new_description):
        cls.description = new_description

    @staticmethod
    def print_test():
        print('staticmetod test!')


    @property #property 가 메서드를 변수로 바꿔주어서 ('')형태가아니라 변수값대입하듯이 넣으면된다.
    def name(self):

         return self._name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        print('Set new name({})'.format(self._name))

    # def get_name(self):
    #     return self.__name
    # def set_name(self,new_name):
    #     self.__name = new_name

class Restaurant(Shop):

   @staticmethod
   def show_info(self):
       print('식당정보(%s)' % self._name)
       print('유형:%s' % self._shop_type)
       print('주소:%s' % self._address)



# print(shop1.description)
# print(Shop.description)
#shop1.change_descrption('changed description')
#print(shop1.description)
#Shop.change_descrption('cbanged descpription')
#print(Shop.description)


r1 = Restaurant('minaury','seoul','sinsa')
r1.show_info()