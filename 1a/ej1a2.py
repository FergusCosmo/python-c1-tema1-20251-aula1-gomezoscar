"""
Enunciado:
Continuando con la biblioteca requests de Python.
En este ejercicio, aprenderás a trabajar con respuestas en formato JSON.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato JSON
3. Extraer información específica de un objeto JSON

Tu tarea es completar la función indicada para realizar una consulta a la API
de ipify.org usando el formato JSON, que es más estructurado que el texto plano.
"""

import requests

def get_user_ip_json():
    """
    Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
    en formato JSON.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
    try:
        # 1. Realizar la petición GET con el parámetro format=json
        response = requests.get('https://api.ipify.org?format=json')
        
        # 2. Verificar si la petición fue exitosa (código 200)
        if response.status_code == 200:
            # 3. Convertir la respuesta a formato JSON
            data = response.json()
            
            # 4. Extraer y devolver la IP del campo "ip"
            return data['ip']
        else:
            return None
            
    except (requests.exceptions.RequestException, KeyError, ValueError):
        # 5. Devolver None si hay algún error
        return None

def get_response_info():
    """
    Obtiene información adicional sobre la respuesta HTTP al consultar la API.
    
    Returns:
        dict: Diccionario con información de la respuesta (tipo de contenido,
              tiempo de respuesta, tamaño de la respuesta)
        None: Si ocurre un error en la petición
    """
    try:
        # 1. Realizar la petición GET
        response = requests.get('https://api.ipify.org?format=json')
        
        # 2. Verificar si la petición fue exitosa (código 200)
        if response.status_code == 200:
            # 3. Crear y devolver un diccionario con la información solicitada
            return {
                'content_type': response.headers.get('Content-Type', 'desconocido'),
                'elapsed_time': response.elapsed.total_seconds() * 1000,  # Convertir a ms
                'response_size': len(response.content)  # Tamaño en bytes
            }
        else:
            return None
            
    except requests.exceptions.RequestException:
        # 4. Devolver None si hay algún error
        return None

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    ip = get_user_ip_json()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
        
        # Mostrar información adicional de la respuesta
        info = get_response_info()
        if info:
            print("\nInformación de la respuesta:")
            print(f"Tipo de contenido: {info['content_type']}")
            print(f"Tiempo de respuesta: {info['elapsed_time']:.2f} ms")
            print(f"Tamaño de la respuesta: {info['response_size']} bytes")
    else:
        print("No se pudo obtener la dirección IP")