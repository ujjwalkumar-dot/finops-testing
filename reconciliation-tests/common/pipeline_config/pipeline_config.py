def pipeline_config(pytestconfig):
    return (
        pytestconfig.getoption("--pipeline_name"),
        pytestconfig.getoption("--pipeline_code"),
    )