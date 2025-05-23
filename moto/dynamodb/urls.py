from .responses import DynamoHandler

url_bases = [
    r"https?://dynamodb\.(.+)\.amazonaws\.com",
    r"https?://(.+)\.ddb\.(.+)\.amazonaws\.com",
]

url_paths = {"{0}/": DynamoHandler.dispatch}
