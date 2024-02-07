import sys
import utils

import interactor.factories as factories
from file_repository.in_file_gateway_factory import InFileGatewayFactory
from gui import TaskRegistryPresenter
from gui.console_show_streams_moments_command import ConsoleShowStreamsMomentsCommand
from gui.console_view import ConsoleView
from interactor import StartRecordStreamCommand, ShowTaskRegistryCommand, \
    AddStreamWatcherCommand, StopTaskByIdCommand
from interactor.record_stream_task_factory import RecordStreamTaskFactory
from interactor.use_cases.stop_all_tasks_command import StopAllTasksCommand
from utils.logger.file_logger import FileLogger
from utils.logger.time_decorator import TimeDecorator

utils.logger = TimeDecorator(FileLogger('output/log.txt'))

factories.record_stream_task_factory = RecordStreamTaskFactory()
factories.gateway_factory = InFileGatewayFactory()

def get_help():
    use_cases = ["Показать моменты из всех стримов", "Начать запись стрима", "Показать регистр задач", "Добавить вотчера стримеру", "Остановить задачу"]
    i = 1
    help = ""
    for case in use_cases:
        help += f'{i}. {case}\n'
        i = i + 1

    return help

while(True):
    command_index = input(get_help())

    if command_index == "1":
        command = ConsoleShowStreamsMomentsCommand()
        radius = input('Введите радиус\n')
        command.execute(float(radius))

    if command_index == '2':
        platform = 'twith'
        stream_reference = input('Введите имя стрима: ')
        command = StartRecordStreamCommand()
        command.execute(stream_reference, platform)

    if command_index == '3':
        command = ShowTaskRegistryCommand(TaskRegistryPresenter(ConsoleView()))
        command.execute()

    if command_index == '4':
        stream_reference = input('Введите имя стримера: ')
        platform = 'twith'
        command = AddStreamWatcherCommand()
        command.execute(stream_reference, platform)

    if command_index == '5':
        task_id = input('Введите id задачи: ')
        command = StopTaskByIdCommand()
        command.execute(task_id)


    if command_index == "0":
        command = StopAllTasksCommand()
        command.execute()
        sys.exit()
