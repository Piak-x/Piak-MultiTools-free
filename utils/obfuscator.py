import base64
import random
import string
import re
import os

def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def substitute_variables(code):
    variable_pattern = r'\b[A-Za-z_][A-Za-z0-9_]*\b'
    reserved_keywords = set([
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    ])
    
    variables = set(re.findall(variable_pattern, code)) - reserved_keywords
    
    var_map = {var: generate_random_string() for var in variables}
    
    for var, obfuscated_var in var_map.items():
        code = re.sub(rf'\b{var}\b', obfuscated_var, code)
    
    return code

def insert_dummy_code(code):
    dummy_code = '\n'.join([
        'if False: pass', 
        'try: pass\nexcept: pass',
        'for _ in range(1): pass',
        'while False: pass'
    ])
    return f'{dummy_code}\n{code}'

def obfuscate_code(code):
    code = substitute_variables(code)
    code = insert_dummy_code(code)
    encoded_code = base64.b64encode(code.encode('utf-8')).decode('utf-8')
    obfuscated_code = f'''
import base64
exec(base64.b64decode("{encoded_code}").decode('utf-8'))
'''
    return obfuscated_code

def obfuscate_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        obfuscated_code = obfuscate_code(code)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        
        print(f"Le fichier {input_file} a été obfusqué et sauvegardé dans {output_file}")
    
    except Exception as e:
        print(f"Erreur lors de l'obfuscation : {str(e)}")

def main():
    input_file = input("Entrez le chemin du fichier Python à obfusquer: ")
    if not os.path.isfile(input_file):
        print("Le fichier spécifié n'existe pas.")
        return
    
    output_file = input("Entrez le nom du fichier de sortie (par défaut: 'output_obfuscated.py'): ")
    if not output_file:
        output_file = "output_obfuscated.py"
    
    obfuscate_file(input_file, output_file)

if __name__ == "__main__":
    main()
