from table_build import TableBuild
from logsetup import get_module_logger

def main():
    logger = get_module_logger()
    build = TableBuild(logger).build_table()
    return build

if __name__ == "__main__":
    main()