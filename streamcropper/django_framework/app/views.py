from django.http import JsonResponse

from gui.stream_presenter import StreamPresenter
from interactor.use_cases.show_stream_command import ShowStreamCommand
from utils.benchmark.show_all_stream_info_command_benchmark import ShowAllStreamInfoCommandBenchmark


def show_all_stream_info(request):
    command = ShowAllStreamInfoCommandBenchmark(StreamPresenter())
    view_streams = command.execute()
    return JsonResponse(view_streams, safe=False)

def show_stream(request):
    command = ShowStreamCommand(StreamPresenter())
    stream_id = request.GET.get('streamId')
    moment_radius = int(request.GET.get('momentRadius'))

    view_stream = command.execute(stream_id, moment_radius)

    return JsonResponse(view_stream, safe=False)
