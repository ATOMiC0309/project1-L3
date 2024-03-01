#1-topshiriq

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     """Bu Animal klasi 8-dars uyga vazifaning 1-topshirig'i"""
#     def __init__(self, nomi, kengligi, ogirligi, tezligi):
#         self.nomi = nomi
#         self.kengligi = kengligi
#         self.ogirligi = ogirligi
#         self.tezligi = tezligi
#
#     @abstractmethod
#     def animal_nomi(self):
#         return self.nomi
#
#     @abstractmethod
#     def animal_kenligi(self):
#         return self.kengligi
#
#     @abstractmethod
#     def animal_ogirligi(self):
#         return self.ogirligi
#
#     @abstractmethod
#     def animal_tezligi(self):
#         return self.tezligi
#
# class Dog(Animal):
#     """Bu Dog klasi Animal klasidning vorisi"""
#     def __init__(self, nomi, kengligi, ogirligi, tezligi):
#         super().__init__(nomi, kengligi, ogirligi, tezligi)
#
#     def animal_nomi(self):
#         return f"Dog nomi: {self.nomi}"
#
#     def animal_kenligi(self):
#         return f"Dog kengligi: {self.kengligi}"
#
#     def animal_ogirligi(self):
#         return f"Dog ogirligi: {self.ogirligi}"
#
#     def animal_tezligi(self):
#         return f"Dog tezligi: {self.tezligi}"
#
# class Cat(Animal):
#     """Bu Cat klasi Animal klasidning vorisi"""
#
#     def __init__(self, nomi, kengligi, ogirligi, tezligi):
#         super().__init__(nomi, kengligi, ogirligi, tezligi)
#
#     def animal_nomi(self):
#         return f"Cat nomi: {self.nomi}"
#
#     def animal_kenligi(self):
#         return f"Cat kengligi: {self.kengligi}"
#
#     def animal_ogirligi(self):
#         return f"Cat ogirligi: {self.ogirligi}"
#
#     def animal_tezligi(self):
#         return f"Cat tezligi: {self.tezligi}"
#
# class Elephant(Animal):
#     """Bu Elephant klasi Animal klasidning vorisi"""
#
#     def __init__(self, nomi, kengligi, ogirligi, tezligi):
#         super().__init__(nomi, kengligi, ogirligi, tezligi)
#
#     def animal_nomi(self):
#         return f"Elephant nomi: {self.nomi}"
#
#     def animal_kenligi(self):
#         return f"Elephant kengligi: {self.kengligi}"
#
#     def animal_ogirligi(self):
#         return f"Elephant ogirligi: {self.ogirligi}"
#
#     def animal_tezligi(self):
#         return f"Elephant tezligi: {self.tezligi}"
#
#
# dog1 = Dog("Rex", 70, 25, 40)
# print(dog1.animal_nomi())
# print(dog1.animal_kenligi())
# print(dog1.animal_ogirligi())
# print(dog1.animal_tezligi(), "\n", "*"*40)
#
# cat1 = Cat("Cat1", 40, 15, 45)
# print(cat1.animal_nomi())
# print(cat1.animal_kenligi())
# print(cat1.animal_ogirligi())
# print(cat1.animal_tezligi(), "\n", "*"*40)
#
# el1 = Elephant("Elephant1", 200, 400, 20)
# print(el1.animal_nomi())
# print(el1.animal_kenligi())
# print(el1.animal_ogirligi())
# print(el1.animal_tezligi())


# 2-topshiriq

# from abc import ABC, abstractmethod
# class Anketa(ABC):
#     """Bu Anketa klassi"""
#     def __init__(self, full_name, birth_year, address, phone_num, passport):
#         self.full_name = full_name
#         self.birth_year = birth_year
#         self.address = address
#         self.phone_num = phone_num
#         self.passport = passport
#
#     @abstractmethod
#     def get_full_name(self):
#         pass
#
#     @abstractmethod
#     def get_birth_year(self):
#         pass
#
#     @abstractmethod
#     def get_address(self):
#         pass
#
#     @abstractmethod
#     def get_phone_num(self):
#         pass
#
#     @abstractmethod
#     def get_passport(self):
#         pass
#
# import csv
# class Questionnaire(Anketa):
#     """Bu Questionnaire klasi"""
#     def __init__(self, full_name, birth_year, address, phone_num, passport):
#         super().__init__(full_name, birth_year, address, phone_num, passport)
#
#     def get_full_name(self):
#         pass
#
#     def get_birth_year(self):
#         pass
#
#     def get_address(self):
#         pass
#
#     def get_phone_num(self):
#         pass
#
#     def get_passport(self):
#         pass
#
#     def __check_full_name(self):
#         for i in (self.full_name).lower():
#             if i not in "abcdefghijklmnopqrstuvwxyz ":
#                 return False
#         return True
#
#     def __check_passport(self):
#         if str(self.passport).isalnum() and len(self.passport) == 9:
#             if not self.passport[0].isdigit() and not self.passport[1].isdigit():
#                 return True
#         return False
#
#     def write_file(self):
#
#         if self.__check_passport() and self.__check_full_name():
#             with open("anketa.csv", "w") as file:
#                 writer = csv.writer(file, lineterminator="\n")
#                 writer.writerow(
#                     [self.full_name.title(), self.birth_year, self.address.title(), self.phone_num, self.passport.upper()]
#                 )
#             return f"Ma'lumot faylga yozildi."
#         else :
#             return f"Ma'lumot faylga yozilmadi!\nSababi ma'lumotlar xato kiritildi."
#
# anketa1 = Questionnaire("Jamshidbek Mamajonov", 2003, "Namangan", "+998949862666", "AB1234567")
# print(anketa1.write_file())
# anketa1 = Questionnaire("Jamsh1dbek Mamajonov", 2003, "Namangan", "+998949862666", "A1234567")
# print(anketa1.write_file())

