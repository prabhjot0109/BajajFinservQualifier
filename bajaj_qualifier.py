import requests
import json

def main():
    name = "Prabhjot Singh Assi"
    reg_no = "0827AL221098"
    email = "prabhjotsingh220924@acropolis.in"
    
    print("Start Task")
    
    generate_webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    request_body = {
        "name": name,
        "regNo": reg_no,
        "email": email
    }
    
    try:
        print("Sending POST request to generate webhook")
        response = requests.post(generate_webhook_url, json=request_body)
        response.raise_for_status()
        
        webhook_data = response.json()
        print("Webhook generated successfully!")
        
        webhook_url = webhook_data.get("webhook")
        access_token = webhook_data.get("accessToken")
        
        if not webhook_url or not access_token:
            print("Error: Webhook URL or access token missing from response")
            return
            
        print(f"Webhook URL: {webhook_url}")
        print(f"Access Token: {access_token}")
        
        print("Solving Question 2")
        final_query = """
        SELECT 
            e1.EMP_ID, 
            e1.FIRST_NAME, 
            e1.LAST_NAME, 
            d.DEPARTMENT_NAME, 
            COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
        FROM 
            EMPLOYEE e1
        JOIN 
            DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
        LEFT JOIN 
            EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT 
            AND e1.DOB > e2.DOB
        GROUP BY 
            e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
        ORDER BY 
            e1.EMP_ID DESC
        """
        
        submit_url = webhook_url
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }
        
        submit_body = {
            "finalQuery": final_query.strip()
        }
        
        print("Submit SQL solution")
        submit_response = requests.post(submit_url, headers=headers, json=submit_body)
        submit_response.raise_for_status()
        
        print("Solution submitted!")
        print(f"Response: {submit_response.text}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()