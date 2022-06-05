// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
import { server } from './mocks/server';
import { AuthCredentials } from './types';

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

const DUMMY_USER: AuthCredentials = {
  username: "username",
  password: "password",
};
const DUMMY_TOKEN = "TOKEN_STRING_1234567890";

export { DUMMY_USER, DUMMY_TOKEN };