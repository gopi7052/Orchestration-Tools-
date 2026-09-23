from prefect import flow, task


@task
def train_model():

    print("Training model")

    return "Model"


@task
def evaluate_model(model):

    print("Evaluating model")

    return 0.80


@task
def save_model(model):

    print("Model saved")


@flow
def ml_workflow():

    model = train_model()

    accuracy = evaluate_model(model)

    if accuracy >= 0.85:

        save_model(model)

        print("Model accepted")

    else:

        print("Model rejected")


if __name__ == "__main__":
    ml_workflow()