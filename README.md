
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

## About startup.sh

The `startup.sh` file is useful for certain Azure deployment scenarios:

- **Azure App Service**: When deploying to Azure App Service (without containers), the platform can use this script to start your application.
- **Custom startup commands**: It allows you to specify how your application should start in environments that support custom startup scripts.
- **Environment-specific configuration**: You could modify the script to include environment variables or other startup configurations.

While Docker deployments use the Dockerfile's CMD instruction instead, keeping `startup.sh` provides flexibility for non-containerized deployments.

## Next Steps

To learn more about FastAPI, see [FastAPI](https://fastapi.tiangolo.com/).
