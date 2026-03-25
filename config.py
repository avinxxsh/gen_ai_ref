from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# model params
PARAMETERS = {
    GenParams.DECODING_METHOD: 'greedy',
    GenParams.MAX_NEW_TOKENS: 256,
}

# watsonx creds, ususally an api key
CREDENTIALS = {
    'url': 'https://us-south.ml.cloud.ibm.com',
    'project_id': 'skills-network'
} 

LLAMA_MODEL_ID = 'meta-llama/llama-3-2-11b-vision-instruct'
GRANITE_MODEL_ID = 'ibm/granite-3-3-8b-instruct'
MISTRAL_MODEL_ID = 'mistralai/mistral-small-3-1-24b-instruct-2503'
