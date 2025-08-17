### Learn LLM with Python

#### 1. Basic Python and Streamlit

<details>
<summary>2. Basic IO in python</summary>


- Reading file is easy, opening a file in write mode and write in it using `file.write('The content you wanna write')` will cause overwrite, so be careful

```python
with open('filename.txt','w') as file:
    file.write("Hey, I was the text that overworte Everything!")
```

- to avoid this, write file in 'a' append mode

<details>
<summary>Error Handling try,except,else,finally</summary>

- Give good Errors to the customers, dumb like me who dont know wtf is going on, putting strings in their pincode and shit
- Errors like NameError, ZeroDivisionError classes are used to categorize the errors
```
try:
    file=open('Example.txt','r')
    c=1/0
    a=b
except NameError as err:
    print(err)
except Exception as expMain:
    print(expMain)

## If the try is successful, instead of exception, execute else
else:
    print("No Error Bro😁")

# Finally clock is executed regardless of the error or not
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed")
    print("Execution Complete✅")
```

<details>
<summary>Classes and Objects</summary>
- A bank account system would help us understand that a class is a blueprint to create an object(account1), reduce the redundancy in code , initialise the object creation with a `__init__(self,...)` constructor, takes first argument as `self` which is equivalent to `this` keyword in many languages



```
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        if(self.balance<0):
            print("Can't Deposit! Balance Negative.")
        else:
            self.balance+=amount
            print(f"New Balance is {self.balance}/-")

    def withdraw(self,amount):
        if(self.balance<0):
            print("Can't Withdraw! Balance Negative.")
        else:
            self.balance-=amount
            print(f"{amount}/- deposited✅.\nNew Balance: {self.balance}")
    
    def get_balance(self):
        print(f"Your current balance is: {self.balance}/-")


account1 = BankAccount("Aditya",500)
print(account1.name)
account1.get_balance()
account1.withdraw(50)
account1.get_balance()
account1.deposit(4000)
```
