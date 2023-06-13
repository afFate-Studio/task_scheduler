import pyinputplus as pyip

# function used to check the response from the user to make sure it is a valid response
def check_response(response):
    RESPONSES = ['Y','y','Yes','yes','N','n','No','no']
    while True:
        try:
            for i in RESPONSES:
                if response == i:   # if valid response, ends loop and returns response
                    if response in RESPONSES[0:3]:
                        response = 'Y'
                    else:
                        response = 'N'
                    return response
            raise ValueError        
        except ValueError:
            response = pyip.inputStr("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response