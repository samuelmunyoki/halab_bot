import requests
from fingerprint.gen_fingerprint import FingerprintSimulator
from solvers.two_captcha import twocaptcha_g_recaptcha

def site_login(email, password):
    """
    Login function authenticates email and password to support.halabtech.com

    1. Generated a fingerprint
    2. Bypasses Google reCAPTCHA
    3. Authenticates the server

    """
    # Generating fingerprint
    simulator = FingerprintSimulator()
    device_fingerprint = simulator.generate_fingerprint()
    print("Generated Fingerprint:", device_fingerprint)

    g_token = ''

    response = twocaptcha_g_recaptcha()

    if response:
        # Process the response if the CAPTCHA was solved successfully
        print("Captcha solved successfully.\n", response)
        g_token= response.get('code')
    else:
        # Handle the case where the CAPTCHA was not solved
        print("Failed to solve captcha.")
        # return None

    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',        
        'origin': 'https://support.halabtech.com',
        'priority': 'u=0, i',
        'referer': 'https://support.halabtech.com/index.php?a=login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"126.0.2592.113"',
        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Microsoft Edge";v="126.0.2592.113"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"6.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
    }
    PARAMS = {
        'a': 'login',
    }

    DATA = {
        'op': 'login',
        'dfp':device_fingerprint,
        'username': email,
        'password': password,
        'g-recaptcha-response': g_token,
    }

    response = requests.post('https://support.halabtech.com/index.php', params=PARAMS, headers=HEADERS, data=DATA)
    print(response.text)
    
