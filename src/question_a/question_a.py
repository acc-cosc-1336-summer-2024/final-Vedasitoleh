#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table(num):
    final_table = []
    num = 1
   
    while num <= 5:
        table = [ int(num) * i for i in range(1,11)]
        num += 1
        final_table = final_table + table

    return final_table

def display_multiplication_table(final_table):
    
    print(final_table)

display_multiplication_table(create_multiplication_table(1))
