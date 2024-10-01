import yaml
from pathlib import Path
import logging

CONFIG_HOME = Path("nativeETL/pipeline_configs")


def generate_config(config_path: str):
    example_config = {
        "pipeline" : "",
        "version": 1.0,
        "fields": {},
    }

    if not config_path.endswith(".yml"):
        raise Exception("Config file specified is not of type yml. \
                        Please specify a yml file when generating a config")
    elif "/" in config_path:
        raise Exception(f"No subdirectories accepted in config_path, \
                        all configs written to CONFIG_HOME: {CONFIG_HOME}")

    dest_path = CONFIG_HOME/Path(config_path)

    if not dest_path.exists():
        dest_path.write_text(yaml.dump(example_config, default_flow_style=False, sort_keys=False))
    else:
        raise Exception(f"File already exists at {dest_path}, config not generated")
