import yaml
from pathlib import Path

example_config = {
    "pipeline" : "",
    "version": 1.0,
    "fields": {},
}

def generate_config(config_path: str):
    if not config_path.endswith(".yml"):
        raise OSError("Config file specified is not of type yml. \
                       Please specify a yml file when generating a config")

    config_path = Path(config_path).resolve()

    config_home = Path("nativeETL/pipeline_configs").parent()
    
    if config_path.parent() == config_home:
        example_config = yaml.dump(data, default_flow_style=False, sort_keys=False)
        config_path.write_text(example_config)
