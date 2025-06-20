import {
  PUBLIC_APP_LOCAL_STORAGE_TOKEN,
  PUBLIC_APP_LOCAL_STORAGE_EXPIRY,
  PUBLIC_APP_LOCAL_STORAGE_REFRESH
} from '$env/static/public';
import type { AuthToken } from '../types';

const setTokenInMemory = ({ accessToken, refreshToken, expiry }: AuthToken): void => {
  window.localStorage.setItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN, accessToken);
  window.localStorage.setItem(PUBLIC_APP_LOCAL_STORAGE_REFRESH, refreshToken);
  window.localStorage.setItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY, expiry ? expiry.toISOString() : '');
};

const getTokenFromMemory = (): AuthToken => {
  const accessToken = window.localStorage.getItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN) || '';
  const refreshToken = window.localStorage.getItem(PUBLIC_APP_LOCAL_STORAGE_REFRESH) || '';
  const expiry = window.localStorage.getItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY) || '';

  let expiryDate = new Date();

  if (expiry) {
    expiryDate = new Date(expiry);
  }

  return {
    accessToken: accessToken,
    refreshToken: refreshToken,
    expiry: expiryDate,
    tokenType: 'Bearer'
  };
};

const removeTokenInMemory = (): void => {
  window.localStorage.removeItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN);
  window.localStorage.removeItem(PUBLIC_APP_LOCAL_STORAGE_REFRESH);
  window.localStorage.removeItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY);
};

export { setTokenInMemory, getTokenFromMemory, removeTokenInMemory };
