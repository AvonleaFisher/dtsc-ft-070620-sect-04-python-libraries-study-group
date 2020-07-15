def convert_c_to_f(temperature_c):
    return (temperature_c * (9/5) + 32) 

def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""

## CREATE THE ADDITIONAL FUNCTIONS BELOW


# convert_c_to_k
def convert_c_to_k(temp_c):
    return temp_c + 273.15


# convert_f_to_k
def convert_f_to_k(temp_f):
    return (temp_f - 32) * (5/9) + 273.15

# convert_k_to_c
def convert_k_to_c(temp_k):
    return temp_k - 273.15

# convert_k_to_f
def convert_k_to_f(temp_k):
    return (temp_k - 273.15) * (9/5) + 32


## LEVEL UP

# convert_f_to_all
def convert_f_to_all(temp_f):
    print("The temperature in {} f is:".format(temp_f))
    print(str(f_to_c(temp_f)) + " " + "in celcius")
    print(str(convert_f_to_k(temp_f)) + " " + "in kelvins")

# convert_f_to_all
