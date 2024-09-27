import argparse

from commands import (
    validate_config,
    run_pipeline,
    generate_config,
    initialize_scheduler
)

def main():
    parser = argparse.ArgumentParser(description="nativeETL, ETL pipeline creator & executor using only Python built-in modules")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    parser_validate = subparsers.add_parser('validate', help="Validate a pipeline's configuration file to ensure it's usable.")
    parser_validate.add_argument('--config', '-c', required=True, help="Path to the configuration file.")

    parser_run = subparsers.add_parser('run', help='Run the pipeline based on the configuration file, irregardles of schedule.')
    parser_run.add_argument('--config', '-c', required=True, help="Path to the configuration file.")

    parser_generate = subparsers.add_parser('generate', help='Creates a dummy pipeline configuration file for the user.')
    parser_generate.add_argument('--config', '-c', required=True, help="Path to the configuration file.")


    parser_schedule = subparsers.add_parser('schedule', help='Initialize the scheduler on this machine to run any pipelines with \
                                       configured schedules.  Pipelines configs without a schedule or tagged as an exclusion \
                                       will not be scheduled to run can only be executed with the nativeETL run command.')

    args = parser.parse_args()

    if args.command == 'validate':
        validate_config(args.config)
    elif args.command == 'run':
        run_pipeline(args.config)
    elif args.command == 'generate':
        generate_config(args.config)
    elif args.command == 'schedule':
        initialize_scheduler()
    else:
        parser.print_help()