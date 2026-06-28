import yaml
import difflib

def search(name: str):
    with open("commands.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    command_dict = config["commands"]
    available_keys = list(command_dict.keys())

    matches = difflib.get_close_matches(name, available_keys, n=1, cutoff=0.4)

    if matches:
        matched_key = matches[0]
        return matched_key, command_dict[matched_key]
    else:
        for key, formula in command_dict.items():
            if key in name:
                return key, formula

    return None, None
