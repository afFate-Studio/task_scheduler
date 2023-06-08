import pyinputplus as pyip

# function used to check the response from the user to make sure it is a valid response
def check_response(response):
    while True:
        try:
            for i in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
                if response == i:   # if valid response, ends loop and returns response
                    return response
            raise ValueError        
        except ValueError:
            response = pyip.inputStr("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response