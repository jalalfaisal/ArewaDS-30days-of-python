# level 1
import statistics
class Statistics:
    def _init_( self, sample):
        self.sample = sample
    def mean(self):
        return statistics.mean(self.sample)
    def meadian(self):
        return statistics.median(self.sample)
    def mode(self):
        return statistics.mode(self.sample)
    def range(self):
        try:
           return statistics.range(self.sample)
        except statistics.Statisticserror:
           return None
    def variance(self):
        return statistics.variance(self.sample)
    
    def stdev(self):
        return statistics.stdev(self.sample)
    
    def min(self):
        return min(self.sample)
    
    def max(self):
        return max(self.sample)
    
    def count(self):
        return len(self.sample)
    
    def percentile(self, p):
        return statistics.quantiles(self.sample, n=100)[p]
    
    def freq_distribution(self):
        freq = {}
        for x in self.sample:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        return freq
sample = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(sample)

print(stats.mean())
print(stats.median())
print(stats.mode())
print(stats.range())
print(stats.variance())
print(stats.stdev())
print(stats.min())
print(stats.max())
print(stats.count())
print(stats.percentile(50))
print(stats.freq_distribution())(sample)

# level 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        return sum(income["amount"] for income in self.incomes)

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print("Name:", self.firstname, self.lastname)
        print("Total Income:", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Account Balance:", self.account_balance())


# initiation
person = PersonAccount("John", "Doe")
person.add_income(5000, "Salary")
person.add_income(2000, "Freelance")
person.add_expense(1000, "Rent")
person.add_expense(500, "Groceries")
person.account_info()       
        
