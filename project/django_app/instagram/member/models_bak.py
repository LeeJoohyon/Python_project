# from django.db import models, IntegrityError
#
#
# class User(models.Model):
#     username = models.CharField('유저네임', max_length=200, unique=True)
#     last_name = models.CharField('성', max_length=100)
#     first_name = models.CharField('이름', max_length=100)
#     nickname = models.CharField('닉네임', max_length=200)
#     email = models.EmailField('이메일', blank=True)
#     date_joined = models.DateField(auto_now_add=True)
#     last_modified = models.DateField(auto_now=True)
#     following = models.ManyToManyField("self", symmetrical=False, related_name='follower_set',blank=True)
#
#     def __str__(self):
#         return self.first_name
#
#     def follow(self,user):
#         self.following.add(user)
#
#     def unfollow(self,user):
#         self.follow.remove(user)
#
#     @property
#     def follower(self):
#         return self.follower_set.all()
#
#     def change_nickname(self,new_nickname):
#         self.nickname = new_nickname
#         self.save()
#
#     @staticmethod
#     def create_dummy_user(num):
#         import random
#         last_name_list = ['방', '이', '박', '김']
#         first_name_list = ['민아', '혜리', '소진', '아영']
#         nick_name_list = ['빵', '리헬', '쏘지', '율곰']
#         created_count = 0
#
#         for i in range(num):
#             try:
#                 User.objects.create(
#                     username='User{}'.format(i + 1),
#                     last_name=random.choice(last_name_list),
#                     first_name=random.choice(first_name_list),
#                     nickname=random.choice(nick_name_list),
#                 )
#                 created_count += 1
#
#             except IntegrityError as e:
#                 print(e)
#
#         return created_count
#
#     @staticmethod
#     def assign_global_variables():
#         import sys
#         # __main__모둘을 modul변수에 할당
#         modules = sys.modules['__main__']
#                                     #startswith 로시작하는 것을 가져온다
#         users = User.objects.filter(username__startswith='User')
#         for index,user in enumerate(users):
#             setattr(modules,'u{}'.format(index+1),user)


