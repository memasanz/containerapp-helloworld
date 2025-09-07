
### Using Python directly

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Start the application:
   ```
   uvicorn main:app --reload
   ```

3. Access the application:
   ```
   http://127.0.0.1:8000/hello
   ```

### Using Docker

1. Build the Docker image:
   ```
   docker build --tag fastapi-demo .
   ```

2. Run the Docker container:
   ```
   docker run --detach --publish 8000:8000 fastapi-demo
   ```
   
   If port 8000 is already in use, you can use a different port:
   ```
   docker run --detach --publish 8001:8000 fastapi-demo
   ```

3. Access the application:
   ```
   http://localhost:8000/hello
   ```

## Deploy to Azure Container Apps

You can deploy the application to Azure Container Apps using the Azure CLI:

```
az containerapp up \
  --resource-group your-resource-group --name web-aca-app \
  --ingress external --target-port 8000 --source .
```

The URL for the deployed app is in the output of the `az containerapp up` command. Open the URL in your browser to see the web app running in Azure. The form of the URL will look like the following: `https://web-aca-app.<generated-text>.<location-info>.azurecontainerapps.io`, where the `<generated-text>` and `<location-info>` are unique to your deployment.

## Deploy to Azure App Service with Azure CLI

- https://learn.microsoft.com/en-us/azure/app-service/deploy-zip?tabs=cli

You can deploy the application to Azure App Service using the Azure CLI. Below are the typical steps and commands:

1. Create a resource group:
   ```
   az group create --name <your-resource-group> --location eastus
   ```

2. Create an App Service plan and a web app (Linux):
   ```pwsh
   az appservice plan create --name myAppServicePlan --resource-group <your-resource-group> --sku B1 --is-linux
   az webapp create --resource-group <your-resource-group> --plan myAppServicePlan --name <your-app-name> --runtime "PYTHON:3.11"
   ```

3. Deploy your code using Zip Deploy:
   ```pwsh
   # First create a ZIP file of your application
   Compress-Archive -Path * -DestinationPath app.zip
   
4. Enable build during deployment to install dependencies:
   ```pwsh
   az webapp config appsettings set --resource-group <your-resource-group> --name <your-app-name> --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
   ```

5.  Then deploy the ZIP file
   az webapp deploy --resource-group <your-resource-group> --name <your-app-name> --src-path app.zip
   ```

3. Set startup command if needed:
   ```pwsh
   az webapp config set --resource-group <your-resource-group> --name <your-app-name> --startup-file "startup.sh"
   ```

4. Enable Detailed Logging
   ```pwsh
   az webapp log config --resource-group fastapi-test-rg --name fastapi-demo-app-123 --application-logging filesystem --level information --detailed-error-messages true --failed-request-tracing true --web-server-logging filesystem
   ```

Replace `<your-resource-group>` and `<your-app-name>` with your actual resource group and desired app name.

## About startup.sh

The `startup.sh` file is useful for certain Azure deployment scenarios:

- **Azure App Service**: When deploying to Azure App Service (without containers), the platform can use this script to start your application.
- **Custom startup commands**: It allows you to specify how your application should start in environments that support custom startup scripts.
- **Environment-specific configuration**: You could modify the script to include environment variables or other startup configurations.

While Docker deployments use the Dockerfile's CMD instruction instead, keeping `startup.sh` provides flexibility for non-containerized deployments.

## OpenAI API Endpoints

When deployed to Azure Container Apps, the following endpoints are available for interacting with the OpenAI API:


Use these URLs to explore, test, and integrate with the OpenAI API endpoints provided by this application.
 When deployed to Azure Container Apps, use the following general endpoint format (replace `<your-app-url>` with your actual app URL):
 - **Swagger UI:** `https://<your-app-url>/docs`
 - **OpenAPI JSON:** `https://<your-app-url>/openapi.json`
 - **ReDoc:** `https://<your-app-url>/redoc`
 Use these URLs to explore, test, and integrate with the OpenAI API endpoints provided by this application.

## Next Steps

To learn more about FastAPI, see [FastAPI](https://fastapi.tiangolo.com/).


