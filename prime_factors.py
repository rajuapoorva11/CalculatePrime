'''
Program to find the prime factors for a given number
'''
import time
import os


class PrimeFactor():
    def __init__(self):
        self.database_values = {}
        if os.path.isfile("Database.txt"):
            with open('Database.txt', 'r') as file:
                data = file.read()
            if data:
                self.database_values = eval(data)
        else:
            f = open('Database.txt', 'w')
            f.close()


    def find_prime_factors(self, number):
        '''
        This function is used to find all the prime factors for given number
        This function returns list of prime numbers
        '''
        prime_numbers = []
        # The loop starts from 2 as 1 cannot be considered as prime number
        for num_prime in range(2, number + 1):
            # logic to check if the number is prime
            if (number % num_prime == 0):
                is_prime = 1
                for num_divisble in range(2, (num_prime // 2 + 1)):
                    # logic to Check if the number has divisors if yes then that number is skipped
                    if (num_prime % num_divisble == 0):
                        is_prime = 0
                        break
                if (is_prime == 1):
                    prime_numbers.append(num_prime)
                    self.database_values[number] = prime_numbers
        return prime_numbers

    def fetch_database(self, number):
        '''
        This function is used to check the number is in database first, if not found then we find the prime factors
        '''
        prime_factors = self.database_values.get(number)
        if prime_factors is None:
            prime_factors = self.find_prime_factors(number)
        return prime_factors

    def write_database(self):
        '''
        This function is used to write into database
        '''
        with open('Database.txt', 'w') as file:
            file.write(str(self.database_values))

    def write_output(self):
        '''
        This function is used to write to result file
        '''
        result_file = open('result.txt', 'w')
        result_file.write("Given number: %d" %number +"\n" )
        for i in range(len(prime_number_factors)):
            result_file.write("Prime factor found: %i" % prime_number_factors[i] + "\n")

        result_file.write( time_taken + "\n")
        result_file.close()

if __name__ == '__main__':
    try:
        # instance to the PrimeFactor class
        primefactor_obj = PrimeFactor()
        while True:
            user_input = input("Enter any Number to find prime factors or type exit to exit : ")
            start_time = time.time()
            if "exit" == str(user_input).lower():
                break
            try:
                number = int(user_input)
            except ValueError:
                print("ERROR MESSAGE: The given value %s is not a integer. Please enter valid integer" % str(user_input))
                continue
            # function to fetch prime factors
            prime_number_factors = primefactor_obj.fetch_database(number)
            # Print to console
            time_taken = "Time taken to find prime factors is %s milli seconds" % str(
                int(time.time() * 1000) - int(start_time * 1000))
            print("Given number: %d" %number)
            for i in range(len(prime_number_factors)):
                print("Prime factor found: %s" %prime_number_factors[i],sep='\n')
            print(time_taken)
            primefactor_obj.write_output()
        primefactor_obj.write_database()

    except Exception as e:
        print("ERROR : Unexpected error. Please try again %s" % str(e))
