from django.shortcuts import render
from django.http import HttpResponse
from api.api_helpers import create_json_response
import random
import requests
from bs4 import BeautifulSoup

def index(request):
    # Perform necessary operations

    # Create the JSON response using the helper function
    a = 0
    _from = random.randint(100,99999)
    _to = random.randint(100000,300000)
    for i in range(_from,_to):
        a += i
    response = create_json_response(200, 'Success', {'It\'s': 'Working','Action': 'Sum numbers to test elapsed time.','From': _from,'To': _to,'Result':a})

    return response

def get_salary(request):
    name = request.GET.get('name')
    dni = request.GET.get('dni')
    organism = request.GET.get('organism')
    utf8 = request.GET.get('utf8')
    page = request.GET.get('page')
    
    if name is None:
        name = ''
    if dni is None:
        dni = ''
    if organism is None:
        organism = ''
    if utf8 is None:
        utf8 = '✓'
    if page is None:
        page = '0'
        
    response = scraping_salary(name, dni, organism, utf8, page)

    return response

def scraping_salary(name, dni, organism, utf8, page):
    
    
    url = 'http://www.sistemas.chubut.gov.ar/sueldos/buscar?'
    url += 'listado_dgc[agente]='+name
    url += '&listado_dgc[dni]='+dni
    url += '&listado_dgc[organismo]='+organism
    url += '&utf8='+utf8
    url += '&page='+page
    print(url)
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract information from the parsed HTML
            # For example, find all <a> tags and collect their text and href attributes
            data = []
            table = soup.find('table',{'class':'table table-bordered table-condensed table-striped'})
            cant = 0
            count_rows = 0
            if table:
                data = []
                data_agente = []
                current_job = None
                total_data = []
                rows = table.find_all('tr')
                dni_anterior = ''
                row_num = 0
                for row in rows:
                    row_num += 1
                    if row_num > 1:
                        cells = row.find_all(['td','th'])

                        # Check if it's a new job
                        first_col_value = cells[0].get_text().strip()
                        if first_col_value != '' and first_col_value[:5] != 'Total':
                            dni = first_col_value                            
                            data_agente = {
                                'DNI': first_col_value,
                                'Agente': cells[1].get_text().strip(),
                                'jobs': [],
                                'Total Salary':cells[4].get_text().strip()
                            }
                            
                        if first_col_value == '' or (first_col_value != '' and first_col_value[:5] != 'Total'):
                            current_job = {
                                'Organismo / Convenio': cells[2].get_text().strip(),
                                'Categoría': cells[3].get_text().strip(),
                                'Salario': cells[4].get_text().strip(),
                            }
                            data_agente['jobs'].append(current_job)

                        # Check if it's a total row
                        if first_col_value[:5] == 'Total':
                    
                            total_salary = first_col_value[6:]
                            data_agente['Total Salary'] = total_salary
                            total_salary = ''
                            
                        if dni != dni_anterior:
                            dni_anterior = dni
                            cant += 1
                            data.append(data_agente)

            else:
                data.append({'error': 'Sorry, could´t find person.'})

            # Return the scraped data as JSON response
            data = {'value': 'Personas','Cantidad': cant,'page': page,'data': data}
            response = create_json_response(200, 'Success', data)

        else:
            # Return error response if the request was not successful
            response = create_json_response(500, 'Error', {'error': 'Failed to retrieve website content'})
    except requests.RequestException as e:
        # Return error response if an exception occurred during the request
        response = create_json_response(500, 'Error', {'error': str(e)})
    return response

def get_organisms(request):
    
    url = 'http://www.sistemas.chubut.gov.ar/sueldos/buscar'
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract information from the parsed HTML
            # For example, find all <a> tags and collect their text and href attributes
            data = []
            select_element = soup.find('select', {'id': 'listado_dgc_organismo'})
            cant = 0
            if select_element:
                option_elements = select_element.find_all('option')  # Find all <option> elements within the <select>

                for option_element in option_elements:
                    option_value = option_element.get('value')  # Get the value attribute of the <option>
                    option_text = option_element.get_text()  # Get the text content of the <option>
                    if not (option_value == '' or option_text == ''):
                        cant += 1
                        data.append({'id': option_value,'organismo': str(option_text).strip()})
            else:
                data.append({'error': 'Sorry, could´t find organisms.'})

            # Return the scraped data as JSON response
            data = {'value': 'Organismos','Cantidad': cant,'data': data}
            response = create_json_response(200, 'Success', data)

        else:
            # Return error response if the request was not successful
            response = create_json_response(500, 'Error', {'error': 'Failed to retrieve website content'})
    except requests.RequestException as e:
        # Return error response if an exception occurred during the request
        response = create_json_response(500, 'Error', {'error': str(e)})
    return response