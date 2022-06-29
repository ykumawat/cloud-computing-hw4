FROM python:3.7-alpine

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN pip install requests

# Expose port 5000
EXPOSE 5000

# Copy todolist.py, index.html
COPY . ./

# Launch the application
CMD python todolist_api.py
