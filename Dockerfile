# Step 1: Bring in the base "operating system" and Python
FROM python:3.10-slim

# Step 2: Create a workspace folder inside Docker called /app
WORKDIR /app

# Step 3: Copy your requirements list into that workspace
COPY requirements.txt .

# Step 4: Run the installer to download all your libraries (pandas, scikit-learn, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your files (main.py, model.pkl) into the workspace
COPY . .

# Step 6: Open up a communication port so you can view your frontend web app
EXPOSE 8501

# Step 7: The final command that runs automatically when the container starts
CMD ["python", "main.py"]