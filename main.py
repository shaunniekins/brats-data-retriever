import synapseclient
import synapseutils
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Synapse client
syn = synapseclient.Synapse()

try:
    # Get token from environment variables
    auth_token = os.getenv("SYNAPSE_AUTH_TOKEN")

    if not auth_token:
        raise ValueError("SYNAPSE_AUTH_TOKEN not found in .env file")

    # Login to Synapse
    syn.login(authToken=auth_token)

    # Download files from Synapse (syn53708249 is the BraTS dataset ID)
    files = synapseutils.syncFromSynapse(syn, 'syn53708249')

    print(f"Successfully downloaded {len(files)} files")

except Exception as e:
    print(f"An error occurred: {e}")
