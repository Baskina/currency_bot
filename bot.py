from .privat_bank_api import main as get_data_api
import asyncio
from .logining import logining

action_map = {
    "exchange": get_data_api,
}


async def get_data(action, args):
    return await action(args)


def get_action(command):
    return action_map[command]


async def main_coroutine(user_command):
    command, *args = user_command.split(' ')
    print(command, args)
    action = get_action(command)
    return await asyncio.gather(get_data(action, args), logining(f'message from client: {user_command}'))


def main(command):
    return asyncio.run(main_coroutine(command))[0]
