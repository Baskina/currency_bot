import aiohttp
import asyncio
import platform
from datetime import datetime, timedelta
from .logining import logining

default_days = 1
default_currency = ['USD', 'EUR']
default_args = default_currency + [default_days]


class HttpError(Exception):
    pass


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as err:
            raise HttpError(f'Connection error: {url}', str(err))


async def get_exchange_rate(day):
    return await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={day}')


async def get_whole_currency_data(index_day):
    requests_array = []
    for index_day in range(1, index_day + 1):
        day = datetime.now() - timedelta(days=index_day)
        requests_array.append(get_exchange_rate(day.strftime("%d.%m.%Y")))

    try:
        return await asyncio.gather(*requests_array)
    except HttpError as err:
        print(err)


def get_chosen_currency_data(whole_currency_data, currency_names):
    currency = currency_names

    data = []
    for item in whole_currency_data:
        date = item["date"]
        for currency_item in currency:
            currency_data = next((x for x in item["exchangeRate"] if x["currency"] == currency_item), None)
            data_index = next((i for i, obj in enumerate(data) if date in obj), None)
            if data_index is not None:
                data[data_index][f"{date}"].update(
                    {currency_item: {"sale": currency_data["saleRateNB"], "purchase": currency_data["purchaseRateNB"]}})
            else:
                data.append({item["date"]: {f'{currency_item}': {"sale": currency_data["saleRateNB"],
                                                                 "purchase": currency_data["purchaseRateNB"]}}})
    return data


async def get_data(args):
    if len(args) > 1:
        args.extend(default_currency)
    else:
        args = default_args
    index_day = get_days_amount(args[0])
    whole_currency_data = await get_whole_currency_data(index_day)
    chosen_currency_data = get_chosen_currency_data(whole_currency_data, args[1:])
    return format_currency_data(chosen_currency_data)



def format_currency_data(currency_data):
    result = ""
    for item in currency_data:
        for date, currencies in item.items():
            result += f"Date: {date}\n"
            for currency, values in currencies.items():
                result += f"{currency} - Sale: {values['sale']}, Purchase: {values['purchase']}\n"
    return result


def get_days_amount(days_amount):
    try:
        days_amount = int(days_amount)
    except IndexError:
        days_amount = 1
    days_amount = 10 if int(days_amount) > 10 else int(days_amount)
    return days_amount


async def main_coroutine(args):
    return await asyncio.gather(get_data(args), logining(args))


async def main(args):
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    return await get_data(args)


if __name__ == '__main__':
    main([1, 'USD', 'EUR'])
