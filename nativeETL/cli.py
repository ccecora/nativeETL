import argparse

#from helpers import existing_configs

from .commands import (
    validate_config,
    run_pipeline,
    generate_config,
    initialize_scheduler
)

def main():
    parser = argparse.ArgumentParser(description="nativeETL, ETL pipeline creator & executor using only Python built-in modules")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    parser_validate = subparsers.add_parser('validate', help="Validate a pipeline's configuration file to ensure it's usable. \
                                            Note that this command will be run for config-dependent CLI commands")
    parser_validate.add_argument('--config', '-c', required=True, help="Path to the configuration file.")

    parser_run = subparsers.add_parser('run', help='Run the pipeline based on the configuration file, irregardles of schedule.')
    parser_run.add_argument('--config', '-c', required=True, help="Path to the configuration file.")

    parser_generate = subparsers.add_parser('generate', help='Creates a dummy pipeline configuration file for the user.')
    parser_generate.add_argument('--config', '-c', required=True, help="Path to the configuration file.")


    parser_schedule = subparsers.add_parser('schedule', help='Initialize the scheduler on this machine to run any pipelines with \
                                       configured schedules.  Pipelines configs without a schedule or tagged as an exclusion \
                                       will not be scheduled to run can only be executed with the nativeETL run command.')
    parser_generate.add_argument('--safe', '-s', required=False, default=True, help="If True, will ensure the project is 'safe' \
                                  before the scheduler is initialized by validating every existing config.")

    args = parser.parse_args()

    if args.command == 'validate':
        validate_config(args.config)
    elif args.command == 'run':
        validate_config(args.config)
        run_pipeline(args.config)
    elif args.command == 'generate':
        generate_config(args.config)
    elif args.command == 'schedule':
        # TODO: implement --safe if the schedule command becomes usable
        #
        # Would be something like the following:
        #
        # if args.safe:
        #    for config in existing_configs():
        #       validate_config(config)
        initialize_scheduler()

    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()