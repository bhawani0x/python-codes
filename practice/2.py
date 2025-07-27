# # list of str, and num 
# # need to print all possible combination of length num

class Pattern:

    _instance = None

    def __new__(cls, *arg):
        if cls._instance is None:
            cls._instance = super(Pattern, cls).__new__(cls)
        return cls._instance


    def __init__(self, li:list[str], num:int)-> None:
        self.li = li
        self.num = num

    def create_pattern(self) -> list[str]:
        tmp_list = self.li
        for i in range(self.num):
            li_2 = []
            for ch in self.li:
                li_2.extend(self.recursive(ch, tmp_list))
            tmp_list = li_2

        return(tmp_list)
    
    def recursive(self, ch, tmp_list):
        new_li = []
        for ch_in_return_list in tmp_list:
            new_li.append(ch + ch_in_return_list)
        return new_li
        
        


li = ['a', 'b', 'c', 'd', 'e']
num = 5
obj = Pattern(li, num)
response  = obj.create_pattern()
print(response)


from itertools import product

class Pattern:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Pattern, cls).__new__(cls)
        return cls._instance

    def __init__(self, li: list[str], num: int) -> None:
        self.li = li
        self.num = num

    def create_pattern(self) -> list[str]:
        return [''.join(p) for p in product(self.li, repeat=self.num)]



li = ['a', 'b', 'c', 'd', 'e']
num = 2
obj = Pattern(li, num)
response = obj.create_pattern()
print(len(response))
# Output: ['aa', 'ab', 'ba', 'bb']
