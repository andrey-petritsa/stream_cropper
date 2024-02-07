import file_repository.in_file_stream_gateway


class InFileGatewayFactory():
    def create_stream_gateway(self):
        return file_repository.in_file_stream_gateway.InFileStreamGateway()