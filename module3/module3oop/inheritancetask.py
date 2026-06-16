class bank:
    def getdata(self):
        self.acno = int(input("Enter acno: "))
        self.acnm = input("Enter acc name: ")
        self.actype = input("Enter actype: ")

class deposit(bank):
    def getdeposit(self):
        self.bal = int(input("Enter deposit: "))
        if self.bal < 2000:
            print("Deposit greater than 2000")
        else:
            print("OK")

class withdrawal(deposit):
    def getwithdraw(self):
        x = int(input("Enter withdraw amount: "))
        if x <= self.bal:
            self.bal = self.bal - x
            print("Remaining Balance =", self.bal)
        else:
            print("Insufficient Balance")

class statements(withdrawal):
    def getacinfo(self):
        print("a/c no is",self.acno)
        print("a/c type is ",self.actype)
        print("a/c holder name is ",self.acnm)
        print("a/c balance is ",self.bal)


st=statements()
st.getdata()

st.getdeposit()
st.getwithdraw()
st.getacinfo()

         