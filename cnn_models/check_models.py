import os
import sys
import shutil

# Define colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Define the models directory path
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saved_models')

# Ensure the models directory exists
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
    print(f"{Colors.YELLOW}Created models directory: {MODEL_DIR}{Colors.END}")

# Define expected model files
EXPECTED_MODELS = {
    'breast_cancer_model.pkl': "Breast Cancer Model",
    'heart_disease_model.pkl': "Heart Disease Model",
    'Liver_Model.pkl': "Liver Disease Model",
    'hepatitis_model.pkl': "Hepatitis Model",
    'diabetis_model.pkl': "Diabetes Model",
    'kidney_disease_model.h5': "Kidney Disease Model (CNN)",
    'brain_tumor_model.h5': "Brain Tumor Model (CNN)"
}

# Check if each model file exists
missing_models = []
existing_models = []

print(f"\n{Colors.BOLD}Checking model files in: {MODEL_DIR}{Colors.END}\n")

for model_file, model_name in EXPECTED_MODELS.items():
    file_path = os.path.join(MODEL_DIR, model_file)
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
        print(f"{Colors.GREEN}✓ {model_name} found ({file_size:.2f} MB){Colors.END}")
        existing_models.append(model_file)
    else:
        print(f"{Colors.RED}✗ {model_name} missing ({model_file}){Colors.END}")
        missing_models.append(model_file)

# Summary
print(f"\n{Colors.BOLD}Summary:{Colors.END}")
print(f"Total models: {len(EXPECTED_MODELS)}")
print(f"{Colors.GREEN}Found: {len(existing_models)}{Colors.END}")
print(f"{Colors.RED}Missing: {len(missing_models)}{Colors.END}")

# Provide instructions for missing models
if missing_models:
    print(f"\n{Colors.BOLD}Instructions to fix missing models:{Colors.END}")
    
    # Check for the brain_tumor_model specifically
    if 'brain_tumor_model.h5' in missing_models:
        print(f"\n{Colors.YELLOW}To fix the Brain Tumor Model:{Colors.END}")
        print("1. Download a pre-trained brain tumor classification model (brain_tumor_model.h5)")
        print("2. Place it in the following directory:")
        print(f"   {MODEL_DIR}")
        print("\nYou can create your own model using TensorFlow/Keras with code like:")
        print("""
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
    
    # Create a CNN model for brain tumor classification
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    # Train the model...
    model.save('saved_models/brain_tumor_model.h5')
        """)
    
    # Instructions for other models
    print(f"\n{Colors.YELLOW}General instructions for all missing models:{Colors.END}")
    print("1. Train or download the missing model files")
    print("2. Place them in the models directory with the correct filenames:")
    for model in missing_models:
        print(f"   - {model}")
    print(f"3. Restart the model server: python cnn_models/load_models.py")

# Check if load_models.py exists and has been modified
load_models_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'load_models.py')
if os.path.exists(load_models_path):
    print(f"\n{Colors.BOLD}Checking server configuration:{Colors.END}")
    
    # Very basic check - this could be more sophisticated
    with open(load_models_path, 'r') as f:
        content = f.read()
        if 'brain_tumor_model = None' in content and 'if brain_tumor_model is None:' in content:
            print(f"{Colors.GREEN}✓ Server code includes proper error handling{Colors.END}")
        else:
            print(f"{Colors.YELLOW}! Server code may need updating to handle missing models properly{Colors.END}")
            print("  Run: python -m pip install --upgrade .")

# Check server status if port 5002 is in use
import socket
def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if check_port_in_use(5002):
    print(f"{Colors.GREEN}✓ Model server appears to be running on port 5002{Colors.END}")
else:
    print(f"{Colors.YELLOW}! Model server does not appear to be running on port 5002{Colors.END}")
    print("  To start the server: python cnn_models/load_models.py")

print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
print("1. Ensure all model files are in place")
print("2. Start the model server: python cnn_models/load_models.py")
print("3. Test the API: http://localhost:5002/models/status")
print("4. Open the health app in your browser\n") 