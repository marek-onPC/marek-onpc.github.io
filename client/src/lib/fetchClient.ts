import {
  HTTPMethods,
  type GetFilters,
  type SavedCheatSheetResponseType,
  type UnsavedCheatSheetType,
  type UpdateCheatSheetType
} from '../types';
import { PUBLIC_APP_SERVER } from '$env/static/public';

const _filter_serializer = (filters: GetFilters): URLSearchParams => {
  let serialized: Record<string, string> = {};

  if (filters.is_published__list) {
    serialized = {
      ...serialized,
      is_published__list: filters.is_published__list.join(',')
    };
  }

  return new URLSearchParams(serialized);
};

const fetchClientPostWithoutToken = async (url: string, data: object): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}`, {
    method: HTTPMethods.POST,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = await data.json();

    return {
      status: responseStatus,
      data: responseData
    };
  });

  return response;
};

const fetchClientGetWithoutToken = async (url: string): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}`, {
    method: HTTPMethods.GET,
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = await data.json();

    return {
      status: responseStatus,
      data: responseData
    };
  });

  return response;
};

const fetchClientGet = async (
  url: string,
  token: string,
  filters?: GetFilters,
  queryParams?: Record<string, string | number>
): Promise<any> => {
  const queryString =
    queryParams !== undefined
      ? new URLSearchParams(
          Object.fromEntries(
            Object.entries(queryParams).map(([k, v]) => [k, String(v)])
          )
        ).toString()
      : filters
        ? _filter_serializer(filters).toString()
        : '';
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}?${queryString}`, {
    method: HTTPMethods.GET,
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = await data.json();

    return {
      status: responseStatus,
      data: responseData
    };
  });

  return response;
};

const fetchClientPost = async (
  url: string,
  token: string,
  payload: UnsavedCheatSheetType
): Promise<{ status: number; id: string }> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}`, {
    method: HTTPMethods.POST,
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = (await data.json()) as SavedCheatSheetResponseType;

    return {
      status: responseStatus,
      id: responseData.id
    };
  });

  return response;
};

const fetchClientPatch = async (
  url: string,
  token: string,
  payload: UpdateCheatSheetType
): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}`, {
    method: HTTPMethods.PATCH,
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;

    return {
      status: responseStatus
    };
  });

  return response;
};

const fetchClientDelete = async (url: string, token: string): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}/api${url}`, {
    method: HTTPMethods.DELETE,
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;

    return {
      status: responseStatus
    };
  });

  return response;
};

export {
  fetchClientPostWithoutToken,
  fetchClientGetWithoutToken,
  fetchClientGet,
  fetchClientPost,
  fetchClientPatch,
  fetchClientDelete
};
