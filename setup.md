# Setup Instructions

Follow these steps to set up your environment for HOF Cognitive Computing.

## Prerequisites

Ensure you have the following software installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Make

## Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Distillative-AI/HOF-cognition.git
   cd HOF-cognition
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install PyTorch:**

   Follow the instructions on the [PyTorch website](https://pytorch.org/get-started/locally/) to install the appropriate version for your system.

   For example, for CUDA 11.1:
   ```bash
   pip install torch torchvision torchaudio
   ```

5. **Build and compile necessary components:**

   ```bash
   make build
   ```

6. **Set up environment variables:**

   Create a `.env` file in the root directory and add the necessary environment variables. Example:
   ```bash
   export HOF_COGNITION_ENV=development
   ```

7. **Verify the installation:**

   Run the following command to ensure everything is set up correctly:
   ```bash
   python -m unittest discover tests
   ```

Your environment should now be set up and ready to use HOF Cognitive Computing.
