import { HTTPMethods } from "../types"

const fetchClientWithoutAuthorization = async (
  url: string,
  httpMethod: HTTPMethods,
  data: object
): Promise<any> => {
  const response = await fetch(`/api${url}`, {
    method: httpMethod,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(data => {
      return data.json();
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  return response;
}

export { fetchClientWithoutAuthorization }