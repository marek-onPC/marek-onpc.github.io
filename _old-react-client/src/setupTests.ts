// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
import { server } from './mocks/server';
import { AuthCredentials, NoteType } from './types';

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

const DUMMY_USER: AuthCredentials = {
  username: "username",
  password: "password",
};
const DUMMY_TOKEN = "TOKEN_STRING_1234567890";
const DUMMY_NOTES: Array<NoteType> = [
  {
    id: "id1",
    title: "Post one",
    categories: ["categoryOne, categoryTwo"],
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
  },
  {
    id: "id2",
    title: "Note two",
    categories: ["categoryTwo, categoryThree"],
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
  },
  {
    id: "id3",
    title: "Entry three",
    categories: ["categoryOne, categoryThree"],
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
  },
]

export { DUMMY_USER, DUMMY_TOKEN, DUMMY_NOTES };