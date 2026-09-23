from prefect import flow, task


attempt = 0


@task(
    retries=2,
    retry_delay_seconds=2
)
def connect_database():

    global attempt

    attempt += 1

    print("Connection Attempt:", attempt)

    if attempt == 1:
        raise Exception(
            "Database temporarily unavailable"
        )

    print("Database connected")

    return "Hospital Data"


@task
def preprocess_data(data):

    print("Preprocessing:", data)


@flow
def hospital_workflow():

    data = connect_database()

    preprocess_data(data)


if __name__ == "__main__":
    hospital_workflow()