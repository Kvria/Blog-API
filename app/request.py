import urllib.request,json
from .models import Quote

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['QUOTES_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quotes_results = process_results(quotes_results_list)


    return quote_results

def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        quote = quote_item,get('quote')
        author = quote_item.get('author')

        quote_results.append(quote_object)

    return quote_results

def get_quote(id):
    get_quote_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:
            id = quote_details_response.get('id')
            quote = quote_details_response.get('quote')
            author = quote_details_response.get('author')
            
            quote_object = Quote(id,quote,author)

    return quote_object
