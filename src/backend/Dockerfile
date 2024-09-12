FROM python:3.12

# Set the working directory
WORKDIR /code

# Copy the requirements.txt first, for better cache
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all the current contents (app.py and others) into /code inside the container
COPY . /code

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
