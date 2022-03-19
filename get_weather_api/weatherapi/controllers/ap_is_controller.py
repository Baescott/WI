# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from weatherapi.api_helper import APIHelper
from weatherapi.configuration import Configuration
from weatherapi.controllers.base_controller import BaseController
from weatherapi.http.auth.custom_query_auth import CustomQueryAuth
from weatherapi.models.current_json_response import CurrentJsonResponse
from weatherapi.models.forecast_json_response import ForecastJsonResponse
from weatherapi.models.history_json_response import HistoryJsonResponse
from weatherapi.models.search_json_response import SearchJsonResponse
from weatherapi.models.ip_json_response import IpJsonResponse
from weatherapi.models.timezone_json_response import TimezoneJsonResponse
from weatherapi.models.astronomy_json_response import AstronomyJsonResponse
from weatherapi.exceptions.api_exception import APIException

class APIsController(BaseController):

    """A Controller to access Endpoints in the weatherapi API."""


    def get_realtime_weather(self,
                             q,
                             lang=None,
                             aqi=None):
        """Does a GET request to /current.json.

        Current weather or realtime weather API method allows a user to get up
        to date current weather information in json and xml. The data is
        returned as a Current Object.Current object contains current or
        realtime weather information for a given city.

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.
            lang (string, optional): Returns 'condition:text' field in API in
                the desired language. Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                check 'lang-code'.

        Returns:
            CurrentJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/current.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q,
            'lang': lang,
            'aqi': aqi
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        #print(_request.__dict__)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CurrentJsonResponse.from_dictionary)

    def get_forecast_weather(self,
                             q,
                             days,
                             dt=None,
                             unixdt=None,
                             hour=None,
                             lang=None,
                             aqi=None):
        """Does a GET request to /forecast.json.

        Forecast weather API method returns upto next 10 day weather forecast
        and weather alert as json. The data is returned as a Forecast
        Object.<br />Forecast object contains astronomy data, day weather
        forecast and hourly interval weather information for a given city.

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.
            days (int): Number of days of weather forecast. Value ranges from
                1 to 10
            dt (date, optional): Date should be between today and next 10 day
                in yyyy-MM-dd format
            unixdt (int, optional): Please either pass 'dt' or 'unixdt' and
                not both in same request.<br />unixdt should be between today
                and next 10 day in Unix format
            hour (int, optional): Must be in 24 hour. For example 5 pm should
                be hour=17, 6 am as hour=6
            lang (string, optional): Returns 'condition:text' field in API in
                the desired language. Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                check 'lang-code'.

        Returns:
            ForecastJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/forecast.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q,
            'days': days,
            'dt': dt,
            'unixdt': unixdt,
            'hour': hour,
            'lang': lang,
            'aqi': aqi
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ForecastJsonResponse.from_dictionary)

    def get_history_weather(self,
                            q,
                            dt,
                            unixdt=None,
                            end_dt=None,
                            unixend_dt=None,
                            hour=None,
                            lang=None,
                            aqi=None):
        """Does a GET request to /history.json.

        History weather API method returns historical weather for a date on or
        after 1st Jan, 2015 as json. The data is returned as a Forecast
        Object.

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.
            dt (date): Date on or after 1st Jan, 2015 in yyyy-MM-dd format
            unixdt (int, optional): Please either pass 'dt' or 'unixdt' and
                not both in same request.<br />unixdt should be on or after
                1st Jan, 2015 in Unix format
            end_dt (date, optional): Date on or after 1st Jan, 2015 in
                yyyy-MM-dd format'end_dt' should be greater than 'dt'
                parameter and difference should not be more than 30 days
                between the two dates.
            unixend_dt (int, optional): Date on or after 1st Jan, 2015 in Unix
                Timestamp format<br />unixend_dt has same restriction as
                'end_dt' parameter. Please either pass 'end_dt' or
                'unixend_dt' and not both in same request. e.g.:
                unixend_dt=1490227200
            hour (int, optional): Must be in 24 hour. For example 5 pm should
                be hour=17, 6 am as hour=6
            lang (string, optional): Returns 'condition:text' field in API in
                the desired language. Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                check 'lang-code'.

        Returns:
            HistoryJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/history.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q,
            'dt': dt,
            'unixdt': unixdt,
            'end_dt': end_dt,
            'unixend_dt': unixend_dt,
            'hour': hour,
            'lang': lang,
            'aqi': aqi
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, HistoryJsonResponse.from_dictionary)

    def search_autocomplete_weather(self,
                                    q):
        """Does a GET request to /search.json.

        WeatherAPI.com Search or Autocomplete API returns matching cities and
        towns as an array of Location object.

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.

        Returns:
            list of SearchJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/search.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SearchJsonResponse.from_dictionary)

    def get_ip_lookup(self,
                      q):
        """Does a GET request to /ip.json.

        IP Lookup API method allows a user to get up to date information for
        an IP address.

        Args:
            q (string): Pass IP address.

        Returns:
            IpJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ip.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IpJsonResponse.from_dictionary)

    def get_time_zone(self,
                      q):
        """Does a GET request to /timezone.json.

        Return Location Object

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.

        Returns:
            TimezoneJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/timezone.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TimezoneJsonResponse.from_dictionary)

    def get_astronomy(self,
                      q,
                      dt):
        """Does a GET request to /astronomy.json.

        Return Location and Astronomy Object

        Args:
            q (string): Pass US Zipcode, UK Postcode, Canada Postalcode, IP
                address, Latitude/Longitude (decimal degree) or city name.
                Visit [request parameter
                section](https://www.weatherapi.com/docs/#intro-request) to
                learn more.
            dt (date): Date on or after 1st Jan, 2015 in yyyy-MM-dd format

        Returns:
            AstronomyJsonResponse: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/astronomy.json'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'q': q,
            'dt': dt
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Error code 1003: Parameter \'q\' not provided.Error code 1005: API request url is invalid.Error code 1006: No location found matching parameter \'q\'Error code 9999: Internal application error.', _context)
        elif _context.response.status_code == 401:
            raise APIException('Error code 1002: API key not provided.Error code 2006: API key provided is invalid', _context)
        elif _context.response.status_code == 403:
            raise APIException('Error code 2007: API key has exceeded calls per month quota.<br />Error code 2008: API key has been disabled.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AstronomyJsonResponse.from_dictionary)
