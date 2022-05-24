import { HTTPMethods } from "../types";

const fetchClientWithoutToken = async (
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

const fetchClientGet = async (
  url: string,
  token: string,
): Promise<any> => {
  const response = await fetch(`/api${url}`, {
    method: HTTPMethods.GET,
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
  })
    .then(data => {
      return data.json();
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  return response;
}

export { fetchClientWithoutToken, fetchClientGet }