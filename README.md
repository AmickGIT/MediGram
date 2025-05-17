# MediGram

A comprehensive platform for mental health support and medical image analysis, featuring chatbots, report analysis, prescription reading, and brain tumor detection using deep learning.

## Features
- **Mental Health Chatbot:** Chat with an AI-powered mental health assistant.
- **Report Analysis:** Upload and analyze medical reports.
- **Prescription Reader:** Extract information from prescription images.
- **Brain Tumor Detection:** Upload brain scans for AI-based tumor detection.
- **Role-based Dashboards:** Separate dashboards for patients and doctors.

## Getting Started

### Prerequisites
- Python 3.x
- Node.js & npm (for frontend)
- (Optional) Virtual environment for Python
- All required Python and Node.js packages (see requirements.txt/package.json if available)

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd MediGram
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Node.js dependencies (if applicable):**
   ```bash
   cd <frontend-folder>
   npm install
   ```

## Usage Guide

### Step 1: Start Backend Services
- In the `chatbot_models` folder, run the following scripts in dedicated terminals:
  - `main.py`
  - `main1.py`
  - `prescription_reader.py`
- In the `cnn_models` folder, run:
  - `load_models.py`

### Step 2: User Signup & Login
- Run `signup.js` and enter a real email address.
- A confirmation email will be sent; click the link (it may show an error, but proceed).
- Go to `login.js` and log in with your credentials.
- Choose to access either the patient or doctor dashboard.

### Step 3: Platform Usage
- **Patient Dashboard:**
  - Chat with the mental health bot.
  - Use report analysis and prescription reader (upload sample reports in `chatbot_models/uploads`).
- **Doctor Dashboard:**
  - Select the Brain Tumor model from the dropdown.
  - Add test images from `cnn_models/Sample_Pictures/Brain_Tumor`.
  - Upload images (Tumor/No Tumor) to test the model's accuracy.

## Folder Structure
```
MediGram/
├── chatbot_models/
│   ├── main.py
│   ├── main1.py
│   ├── prescription_reader.py
│   └── uploads/
├── cnn_models/
│   ├── load_models.py
│   └── Sample_Pictures/
├── <frontend-folder>/
│   ├── signup.js
│   └── login.js
└── README.md
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.



