# API Usage

This section describes how the code interacts with the Banco Central API to retrieve money circulation data.

**API Endpoint:**

* https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias

**Function:** `make_api_request(skip, start_date, end_date)`

* This function constructs an API request URL and retrieves data for a specific date range and skip index.
* The URL includes filters based on the provided `start_date` and `end_date`.
* The `skip` parameter is used for pagination when dealing with large datasets.
* The function returns a dictionary containing the retrieved data and any relevant metadata.

**Example Usage:**

```python
data = make_api_request(0, "2023-01-01", "2023-02-28")

print(data)
