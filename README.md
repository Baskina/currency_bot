# **Socket Python Application**

This is a Python application that demonstrates socket programming. It consists of a server and a client component. The server is launched first, followed by the client.

## **Features**

* **Bot with "exchange" Command:** The application includes a bot that responds to the "exchange" command. Users can use this command to retrieve currency exchange rates.

* **Currency API Integration:** The application interacts with a currency API to fetch exchange rates.

* **User-Defined Currency and Timeframe:** Users can specify the currency they want to inquire about and the number of days they want to look back in time.

* **Default Currency Support:** By default, the application includes support for EUR and USD currencies.

## **Usage**

* **Launch Server:** Run the server script (server.py) to start the server component of the application.

* **Launch Client:** Run the client script (client.py) to start the client component of the application.

* **Bot Command:** In the client terminal, use the "exchange" command followed by the desired currency and optional number of days. For example:

`exchange 2 PLN
`
This command retrieves the currency exchange rates for PLN for the last 2 days.

* **Output Example:**

`
Date: 21.02.2024
PLN - Sale: 9.6103, Purchase: 9.6103
USD - Sale: 38.4756, Purchase: 38.4756
EUR - Sale: 41.5421, Purchase: 41.5421
Date: 20.02.2024
PLN - Sale: 9.5276, Purchase: 9.5276
USD - Sale: 38.2847, Purchase: 38.2847
EUR - Sale: 41.2403, Purchase: 41.2403`

## Additional Notes

This application is a test implementation to explore and understand the usage of socket programming, asyncio, aiofile, and interaction with external APIs for fetching currency exchange rates.
