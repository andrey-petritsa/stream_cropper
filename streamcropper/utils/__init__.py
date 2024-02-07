from file_repository.stream_dir import StreamDir
from utils.logger.stdout_logger import StdoutLogger
from utils.logger.time_decorator import TimeDecorator
from utils.requests_client import RequestsClient
from utils.stream_id_generator import StreamIdGenerator
from utils.uuid_generator import UuidGenerator

web_client = RequestsClient()
id_generator = UuidGenerator()
stream_id_generator = StreamIdGenerator()
logger = TimeDecorator(StdoutLogger())
stream_dir_path = "./output"
stream_dir = StreamDir(stream_dir_path)