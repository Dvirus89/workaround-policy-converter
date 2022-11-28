
import os 
import json

def main_procedure():
    json_path = input("Drag and Drop your BIGIP exported policy file here and press ENTER: ")
    json_path = str(json_path.replace("'","").replace('"',''))
    fix_policy_file(json_path)


def fix_policy_file(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        json_parsed = json.loads(f.read())
        sig_sets= json_parsed['policy']['signature-sets']
        
        for obj_sigset_list in sig_sets:
            if 'signatureSet' in obj_sigset_list:
                if 'filter' in obj_sigset_list['signatureSet']:
                    if 'attackTypeReference' in obj_sigset_list['signatureSet']['filter']:
                        obj_sigset_list['signatureSet']['filter']['attackType'] = obj_sigset_list['signatureSet']['filter'].pop('attackTypeReference')
                        del obj_sigset_list['signatureSet']['filter']['attackType']['link']
        
        with open(f"{os.path.split(json_path)[0]}/fixed-{os.path.split(json_path)[1]}", 'w') as w:
            json.dump(json_parsed, w, indent=4)
            input("Done, Press ENTER to continue.")


    


if __name__ == '__main__':
    main_procedure()

