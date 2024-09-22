import random
import requests
from datetime import datetime, timezone

def Error(e):
    print(f"An error occurred: {e}")

def Title(title):
    print(f"\n{'='*20} {title} {'='*20}\n")

def NumberInfo(phone_number):
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
    except ImportError:
        return "None", "None", "None", "None", "None"
        
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        operator_phone = carrier.name_for_number(parsed_number, "fr")
        type_number_phone = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        country_phone = phonenumbers.region_code_for_number(parsed_number)
        region_phone = geocoder.description_for_number(parsed_number, "fr")
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_phone = timezones[0] if timezones else None
    except Exception as e:
        Error(e)
        operator_phone = "None"
        type_number_phone = "None"
        country_phone = "None"
        region_phone = "None"
        timezone_phone = "None"

    return operator_phone, type_number_phone, country_phone, region_phone, timezone_phone

def IpInfo(ip):
    website = "ipinfo.io"  # Example website
    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip}")
        api = response.json()
    except Exception as e:
        Error(e)
        api = {}

    isp_ip = api.get("isp", "None")
    org_ip = api.get("org", "None")
    as_ip = api.get("as", "None")

    return isp_ip, org_ip, as_ip

def TokenInfo(token):
    try:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
    except Exception as e:
        Error(e)
        user = {}

    username_discord = user.get('username', 'None') + '#' + user.get('discriminator', 'None')
    display_name_discord = user.get('global_name', 'None')
    user_id_discord = user.get('id', 'None')
    avatar_hash = user.get('avatar', None)
    avatar_url_discord = (f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_hash}.gif"
                          if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_hash}.gif").status_code == 200 
                          else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_hash}.png") if avatar_hash else "None"
    created_at_discord = datetime.fromtimestamp(((int(user_id_discord) >> 22) + 1420070400000) / 1000, timezone.utc) if user_id_discord != 'None' else "None"
    email_discord = user.get('email', 'None')
    phone_discord = user.get('phone', 'None')
    
    try:
        friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token}).json()
        friends_discord = '\n' + ' / '.join([f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"
                                             for friend in friends_response if len(friends_response) < 1024]) if friends_response else "None"
    except Exception as e:
        Error(e)
        friends_discord = "None"

    try:
        gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()
        gift_codes_discord = '\n\n'.join([f"Gift: {gift['promotion']['outbound_title']}\nCode: {gift['code']}" for gift in gift_codes_response]) if gift_codes_response else "None"
    except Exception as e:
        Error(e)
        gift_codes_discord = "None"

    mfa_discord = user.get('mfa_enabled', 'None')
    nitro_type = user.get('premium_type', 0)
    nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(nitro_type, 'False')

    return username_discord, display_name_discord, user_id_discord, avatar_url_discord, created_at_discord, email_discord, phone_discord, nitro_discord, friends_discord, gift_codes_discord, mfa_discord

def main():
    Title("Dox Create")

    by = input("\nDoxed By      : ")
    reason = input("Reason        : ")
    pseudo1 = input("First Pseudo  : ")
    pseudo2 = input("Second Pseudo : ")

    print("\nDiscord Information:")
    token_input = input("Token ? (y/n) -> ")
    if token_input.lower() in ["y", "yes"]:
        token = input("Token: ")
        discord_info = TokenInfo(token)
    else:
        discord_info = (
            input("Username      : "),
            input("Display Name  : "),
            input("Id            : "),
            input("Avatar        : "),
            input("Created At    : "),
            input("Email         : "),
            input("Phone         : "),
            input("Nitro         : "),
            input("Friends       : "),
            input("Gift Code     : "),
            input("Mfa           : ")
        )

    print("\nIP Information:")
    ip_public = input("Ip Publique   : ")
    ip_local = input("Ip Local      : ")
    ipv6 = input("Ipv6          : ")
    vpn_pc = input("VPN           : ")
    isp_ip, org_ip, as_ip = IpInfo(ip_public)

    print("\nPC Information:")
    pc_info = (
        input("Name          : "),
        input("Username      : "),
        input("Display Name  : "),
        input("Platform      : "),
        input("Exploitation  : "),
        input("Windows Key   : "),
        input("MAC Address   : "),
        input("HWID Address  : "),
        input("CPU           : "),
        input("GPU           : "),
        input("RAM           : "),
        input("Disk          : "),
        input("Screen Main   : "),
        input("Screen Sec    : ")
    )

    print("\nNumber Information:")
    phone_number = input("Phone Number  : ")
    brand_phone = input("Brand         : ")
    operator_phone, type_number_phone, country_phone, region_phone, timezone_phone = NumberInfo(phone_number)

    print("\nPersonal Information:")
    personal_info = (
        input("Gender        : "),
        input("Last Name     : "),
        input("First Name    : "),
        input("Age           : "),
        input("Mother        : "),
        input("Father        : "),
        input("Brother       : "),
        input("Sister        : ")
    )

    print("\nLocation Information:")
    location_info = (
        input("Continent     : "),
        input("Country       : "),
        input("Region        : "),
        input("Postal Code   : "),
        input("City          : "),
        input("Address       : "),
        input("Timezone      : "),
        input("Longitude     : "),
        input("Latitude      : ")
    )

    print("\nSocial Information:")
    password = input("Password      : ")
    email = input("Email         : ")

    print("\nOther:")
    other = input("Other         : ")
    database = input("DataBase      : ")
    logs = input("Logs          : ")

    name_file = input(f"Choose the file name -> ")
    if not name_file.strip():
        name_file = f'No Name {random.randint(1, 999)}'

    path = f"./DoxCreate/Dox - {name_file}.txt"

    with open(path, 'w', encoding='utf-8') as file:
        file.write(f'''
        Doxed By : {by}
        Reason   : {reason}
        Pseudo   : "{pseudo1}", "{pseudo2}"

        DISCORD INFORMATION:
        Username     : {discord_info[0]}
        Display Name : {discord_info[1]}
        ID           : {discord_info[2]}
        Avatar       : {discord_info[3]}
        Created At   : {discord_info[4]}
        Token        : {discord_info[5]}
        E-Mail       : {discord_info[6]}
        Phone        : {discord_info[7]}
        Nitro        : {discord_info[8]}
        Friends      : {discord_info[9]}
        Gift Code    : {discord_info[10]}
        MFA          : {discord_info[11]}

        IP INFORMATION:
        IP Publique  : {ip_public}
        Ip Local     : {ip_local}
        Ipv6         : {ipv6}
        Isp          : {isp_ip}
        Org          : {org_ip}
        As           : {as_ip}
        VPN Y/N      : {vpn_pc}

        PC INFORMATION:
        Name         : {pc_info[0]}
        Username     : {pc_info[1]}
        Display Name : {pc_info[2]}
        Platform     : {pc_info[3]}
        Exploitation : {pc_info[4]}
        Windows Key  : {pc_info[5]}
        Mac Address  : {pc_info[6]}
        Hwid Address : {pc_info[7]}
        CPU          : {pc_info[8]}
        GPU          : {pc_info[9]}
        RAM          : {pc_info[10]}
        Disk         : {pc_info[11]}
        Screen Main  : {pc_info[12]}
        Screen Sec   : {pc_info[13]}

        NUMBER INFORMATION:
        Phone Number : {phone_number}
        Brand        : {brand_phone}
        Operator     : {operator_phone}
        Type         : {type_number_phone}
        Country      : {country_phone}
        Region       : {region_phone}
        Timezone     : {timezone_phone}

        PERSONAL INFORMATION:
        Gender       : {personal_info[0]}
        Last Name    : {personal_info[1]}
        First Name   : {personal_info[2]}
        Age          : {personal_info[3]}
        Mother       : {personal_info[4]}
        Father       : {personal_info[5]}
        Brother      : {personal_info[6]}
        Sister       : {personal_info[7]}

        LOCATION INFORMATION:
        Continent    : {location_info[0]}
        Country      : {location_info[1]}
        Region       : {location_info[2]}
        Postal Code  : {location_info[3]}
        City         : {location_info[4]}
        Address      : {location_info[5]}
        Timezone     : {location_info[6]}
        Longitude    : {location_info[7]}
        Latitude     : {location_info[8]}

        SOCIAL INFORMATION:
        Password     : {password}
        E-Mail       : {email}

        OTHER:
        Other        : {other}
        DataBase     : {database}
        Logs         : {logs}
        ''')

    print(f"All information saved to {path}.")

if __name__ == "__main__":
    main()
