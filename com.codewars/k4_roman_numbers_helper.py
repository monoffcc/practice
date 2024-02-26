dic = {
    'M' : 1000,
    'CM' : 900,
    'D' : 500,
    'CD' : 400,
    'C' : 100,
    'XC' : 90,
    'L' : 50,
    'XL' : 40,
    'X' : 10,
    'IX' : 9,
    'V' : 5,
    'IV' : 4,
    'I' : 1
}
rdic={v:k for k,v in dic.items()}

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        result=''
            
        for n,v in rdic.items():
            
            while val>=n:
                result+=v
                val-=n
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        print(f'from roman : {roman_num}, {type(roman_num)}')
        result=0
        ln=''
        
        for c,v in dic.items():
            while roman_num.startswith(c):
                result+=v
                roman_num=roman_num[len(c):]            
        return result
    