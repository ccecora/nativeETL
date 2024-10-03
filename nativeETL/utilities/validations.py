def verify_file_type(path: str, accepted_file_suffixes: list[str]) -> None:
    for file_suffix in accepted_file_suffixes:
        if path.endswith(file_suffix):
            return
        
    raise Exception(
        f"""Only file type accepted at the moment must 
        be of the following type(s): {accepted_file_suffixes}.
        """
    )

def verify_yaml_structure(path: str) -> None:
    pass