# How to use

## Clone the repository
```
git clone git@github.com:DD-rasmus/Company-search-API.git
cd Company-search-API
```

## Fill the details in the api.py file
In api.py fill the following details:

SEARCH_ENGINE_ID:
1. Go to: https://programmablesearchengine.google.com/controlpanel/create
2. Add a name to your search engine (choose freely).
3. Choose "Search the entire web"
4. Click "Create"
5. You should now see "Success" and the following code:
```
<script async src="https://cse.google.com/cse.js?cx=mkdasjk1232sa">
</script>
<div class="gcse-search"></div>
```
6. Copy the value after the "?cx=" in the first line and add it to the api.py file as a value for SEARCH_ENGINE_ID

API_KEY:
1. Go to https://developers.google.com/custom-search/v1/introduction#identify_your_application_to_google_with_api_key
2. Press blue "Get a Key" button
3. Choose "+ Create a new project"
4. Choose a name
5. Press "Show key"
6. Copy the key and add it to the api.py file as a value for API_KEY

2. Add companies to the companies.xlsx file under the title "Companies" (max 100 companies can be added)

## Run the environment
1. `python3 -m venv .`
2. `source env/activate`
3. `pip install -r requirements.txt`

## Run the app
`python api.py`

Results outputted to `results.xlsx` file.
