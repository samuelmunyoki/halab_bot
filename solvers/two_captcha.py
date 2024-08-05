# https://github.com/2captcha/2captcha-python

import sys
import os
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha




def twocaptcha_g_recaptcha():
    """
    Solve a reCAPTCHA using the 2Captcha service.

    This function uses the 2Captcha service to solve a reCAPTCHA challenge on a specified site.
    It retrieves the site key and URL from environment variables and sends a request to 2Captcha.
    If successful, it prints the result. Otherwise, it prints an error message.

    Returns:
        dict: The response from 2Captcha if the CAPTCHA is solved successfully.
        None: If there was an error during the solving process.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the API key and site key from environment variables
    API_KEY = os.getenv('APIKEY_2CAPTCHA')
    SITE_KEY = os.getenv('SITEKEY_HALAB')
    SITE_URL = os.getenv('SITE_URL')

    # Ensure that environment variables are loaded
    if not API_KEY or not SITE_KEY or not SITE_URL:
        print("Error: Missing environment variables. Please check your .env file.")
        sys.exit(1)

    # Initialize the 2Captcha solver with the API key
    SOLVER = TwoCaptcha(API_KEY)


    try:
        print("Solving Google reCAPTCHA ...")
        # Request to solve the reCAPTCHA
        result = SOLVER.recaptcha(
            sitekey=SITE_KEY,
            url=SITE_URL,
            version='v2',
        )
    except Exception as e:
        # Print any error that occurs during the request
        print('Error:', e)
        return None
    else:    
        return result


