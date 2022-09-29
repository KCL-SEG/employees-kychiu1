"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class ContractPay:
    def get_pay(self) -> int:
        raise NotImplementedError("This method has not been implemented")


class HourlyContract(ContractPay):
    def __init__(self, hours: int, hourly_rate: int):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def get_pay(self) -> int:
        return self.hours * self.hourly_rate

    def __str__(self):
        return f"a contract of {self.hours} hours at {self.hourly_rate}/hour"


class SalaryContract(ContractPay):
    def __init__(self, salary: int):
        self.salary = salary

    def get_pay(self) -> int:
        return self.salary

    def __str__(self):
        return f"a monthly salary of {self.salary}"


class Commission:
    def get_pay(self) -> int:
        raise NotImplementedError("This method has not been implemented")


class BonusCommission(Commission):
    def __init__(self, bonus: int):
        self.bonus = bonus

    def get_pay(self) -> int:
        return self.bonus

    def __str__(self):
        return f"receives a bonus commission of {self.bonus}"


class ContractCommission(Commission):
    def __init__(self, number_contracts: int, contract_pay_rate: int):
        self.number_contracts = number_contracts
        self.contract_pay_rate = contract_pay_rate

    def get_pay(self) -> int:
        return self.number_contracts * self.contract_pay_rate

    def __str__(self):
        return f"receives a commission for {self.number_contracts} contract(s) at {self.contract_pay_rate}/contract"


class Employee:
    def __init__(self, name, contractPay: ContractPay, commission: Commission = None):
        self.name = name
        self.contractPay = contractPay
        self.commission = commission

    def get_pay(self) -> int:
        total = 0
        if self.contractPay:
            total += self.contractPay.get_pay()
        if self.commission:
            total += self.commission.get_pay()
        return total

    def __str__(self):
        res = f"{self.name} works on {str(self.contractPay)}"
        if self.commission:
            res += f" and {str(self.commission)}"
        res += ". "
        res += f" Their total pay is {self.get_pay()}."
        return res


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120, 30), BonusCommission(600))
