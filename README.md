# BRATS Data Retrieval

A simple utility to retrieve Brain Tumor Segmentation (BraTS) data from Synapse platform.

## Setup Instructions

### Virtual Environment

Create and manage a Python virtual environment with these commands (macOS):

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# When finished, deactivate with
deactivate
```

### Install Dependencies

Once your virtual environment is activated:

```bash
pip install synapseclient synapseutils python-dotenv
```

### Synapse Authentication

To access the data, you'll need a Synapse personal access token:

1. Visit [Synapse Personal Access Tokens](https://accounts.synapse.org/authenticated/personalaccesstokens)
2. Log in to your Synapse account
3. Create a new token with appropriate permissions (view, download, modify)
4. Copy the generated token

### Environment Configuration

Create a `.env` file in the root directory with:

```env
SYNAPSE_AUTH_TOKEN=your_token_here
```

## Usage

Run the script to download BraTS data:

```bash
python main.py
```

## Notes

- The script downloads data from Synapse entity ID 'syn53708249' which contains BraTS dataset files
- Never commit your `.env` file to version control
- Add `.env` to your `.gitignore` file
