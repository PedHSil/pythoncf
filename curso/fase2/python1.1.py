class CallMe:
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self, nome):
        print(nome,'está chamando,', self.phone)
        

call1 = CallMe('1234-5678')
call1('Joaquim')
       
        