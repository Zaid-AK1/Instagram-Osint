import requests
import base64
import binascii
import time
import random
import os
import sys
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if sys.platform.startswith('win') else 'clear')

def instagram_osint():
    while True:
        clear_screen()
        print('=================================================')
        print('              Zaid AK Instagram Osint                ')
        print('=================================================')
        username = input(Fore.RED + "Target Username : " + Fore.WHITE + "@")
        if not username:
            print(Fore.RED + "Username cannot be empty!")
            time.sleep(1)
            continue
        headers = {
            'accept-language': 'en-US;q=1.0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
        }
        data = {"q": username}
        def unhex(hexstr):
            return binascii.unhexlify(hexstr)
        hexstr = ''.join([
            '61','48','52','30','63','48','4D','36','4C','79','39','70','4C','6D','6C','75','63','33','52','68',
            '5A','33','4A','68','62','53','35','6A','62','32','30','76','59','58','42','70','4C','33','59','78',
            '4C','33','56','7A','5A','58','4A','7A','4C','32','78','76','62','32','74','31','63','43','38','3D'
        ])
        url = base64.b64decode(unhex(hexstr)).decode('utf-8')
        def try_post(url, headers, data, retries=3):
            for attempt in range(retries):
                try:
                    response = requests.post(url, headers=headers, data=data)
                    response.raise_for_status()
                    return response
                except requests.RequestException as err:
                    print(Fore.RED + f"Attempt {attempt + 1} failed: {err}")
                    time.sleep(random.uniform(1, 3))
            print(Fore.RED + "All attempts failed.")
            return None
        response = try_post(url, headers, data)
        if response:
            try:
                result = response.json()
                if result:
                    print(Fore.WHITE + "Response Details:")
                    print(Fore.RED + "Multiple Users Found: " + Fore.WHITE + str(result.get('multiple_users_found', 'N/A')))
                    print(Fore.RED + "Email Sent: " + Fore.WHITE + str(result.get('email_sent', 'N/A')))
                    print(Fore.RED + "SMS Sent: " + Fore.WHITE + str(result.get('sms_sent', 'N/A')))
                    print(Fore.RED + "WA Sent: " + Fore.WHITE + str(result.get('wa_sent', 'N/A')))
                    print(Fore.RED + "Lookup Source: " + Fore.WHITE + result.get('lookup_source', 'N/A'))
                    print(Fore.RED + "Corrected Input: " + Fore.WHITE + result.get('corrected_input', 'N/A'))
                    print(Fore.RED + "Show UHL Entry in Verification Steps: " + Fore.WHITE + str(result.get('show_uhl_entry_in_verification_steps', 'N/A')))
                    print(Fore.RED + "UHL Entry Eligible CPS: " + Fore.WHITE + str(result.get('uhl_entry_eligible_cps', 'N/A')))
                    # هنا أهم نقطة: يطبع أي معلومة عن الرقم إذا وجدت
                    phone = result.get('phone_number', None)
                    obf_phone = result.get('obfuscated_phone', None)
                    print(Fore.RED + "Phone Number (Full): " + Fore.WHITE + (phone if phone else 'N/A'))
                    print(Fore.RED + "Phone Number (Obfuscated): " + Fore.WHITE + (obf_phone if obf_phone else 'N/A'))
                    user_info = result.get('user', {})
                    print(Fore.RED + "User Information:")
                    print(Fore.RED + "  Full Name: " + Fore.WHITE + user_info.get('full_name', 'N/A'))
                    print(Fore.RED + "  Username: " + Fore.WHITE + user_info.get('username', 'N/A'))
                    print(Fore.RED + "  Profile Pic URL: " + Fore.WHITE + user_info.get('profile_pic_url', 'N/A'))
                    print(Fore.RED + "  Verified: " + Fore.WHITE + str(user_info.get('is_verified', 'N/A')))
                    print(Fore.RED + "Has Valid Phone: " + Fore.WHITE + str(result.get('has_valid_phone', 'N/A')))
                    print(Fore.RED + "Can Email Reset: " + Fore.WHITE + str(result.get('can_email_reset', 'N/A')))
                    print(Fore.RED + "Can SMS Reset: " + Fore.WHITE + str(result.get('can_sms_reset', 'N/A')))
                    print(Fore.RED + "Can WA Reset: " + Fore.WHITE + str(result.get('can_wa_reset', 'N/A')))
                    print(Fore.RED + "Is WA Timing Signal: " + Fore.WHITE + str(result.get('is_wa_timing_signal', 'N/A')))
                    print(Fore.RED + "WA Account Recovery Type: " + Fore.WHITE + result.get('wa_account_recovery_type', 'N/A'))
                    print(Fore.RED + "Can P2S Reset: " + Fore.WHITE + str(result.get('can_p2s_reset', 'N/A')))
                    print(Fore.RED + "Can Flashcall Reset: " + Fore.WHITE + str(result.get('can_flashcall_reset', 'N/A')))
                    print(Fore.RED + "Email: " + Fore.WHITE + str(result.get('email', 'N/A')))
                    print(Fore.RED + "FB Login Option: " + Fore.WHITE + str(result.get('fb_login_option', 'N/A')))
                    print(Fore.RED + "P2S Option Position: " + Fore.WHITE + result.get('p2s_option_position', 'N/A'))
                    print(Fore.RED + "Autosend Disabled: " + Fore.WHITE + str(result.get('autosend_disabled', 'N/A')))
                    print(Fore.RED + "Toast Message: " + Fore.WHITE + result.get('toast_message', 'N/A'))
                    print(Fore.RED + "Toast Title: " + Fore.WHITE + result.get('toast_title', 'N/A'))
                    print(Fore.RED + "Toast Type: " + Fore.WHITE + result.get('toast_type', 'N/A'))
                    print(Fore.RED + "Login Flow Ready to Continue: " + Fore.WHITE + str(result.get('login_flow_ready_to_continue', 'N/A')))
            except Exception as err:
                print(Fore.RED + "Error in parsing response or invalid response format.")
        print('\n[1] Search new username')
        print('[2] Exit')
        again = input('Choose an option: ')
        if again.strip() != '1':
            print("Exiting...")
            break

if __name__ == "__main__":
    instagram_osint()
