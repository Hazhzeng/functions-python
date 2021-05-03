import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "This is private repo awesome",
        status_code=200
    )
