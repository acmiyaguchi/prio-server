# GoogleCloudStorageObjectSensor
# DockerOperator
# GoogleCloudStorageToGoogleCloudStorageOperator

paths = [
    "raw",
    "intermediate/owned/create_verify1",
    "intermediate/owned/create_verify2",
    "intermediate/owned/aggregates",
    "intermediate/shared/create_verify1",
    "intermediate/shared/create_verify2",
    "intermediate/shared/aggregates",
    "proccessed"
]

# TODO: scheduling parameters
dag = None

def declare_subgraph(command):
    file_sensor = FileSensor(
        path="raw/"
    )

    # TODO: generic method
    job_operator = JobOperator(
        image="mozilla/prio-server:latest"
        command="create_verify1",
        arguments={
            "input-owned": "raw/"
            "output-owned": "intermediate/owned/create_verify1",
            "output-shared": "intermediate/shared/create_verify1",
            # etc
        }
    )

    move_operator = MoveOperator(

    )

    file_sensor >> job_operator >> move_operator

    raise NotImplementedError("TODO: subdag operator")


declare_subgraph("create_verify1")
declare_subgraph("create_verify2")
declare_subgraph("aggregate")
declare_subgraph("publish")