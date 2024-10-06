import { fetchClientGet, fetchClientPostWithoutToken } from '../helpers/fetchClient';
import { DUMMY_TOKEN, DUMMY_USER } from '../setupTests';
import { server } from '../mocks/server';
import { authorizedCallHandler } from '../mocks/handlers';

describe('api calls test case', () => {
  describe('nonauthorized calls test case', () => {
    it('receive 200 status on correct call', async () => {
      const response = await fetchClientPostWithoutToken('/login', DUMMY_USER);

      expect(response.status).toEqual(200);
      expect(response.data).toEqual({ token: DUMMY_TOKEN });
    });
  });

  describe('authorized calls test case', () => {
    beforeEach(() => {
      server.use(authorizedCallHandler(DUMMY_TOKEN));
    });

    it('returns 200 status on correct call - with correct token', async () => {
      const response = await fetchClientGet('/authtest', DUMMY_TOKEN);

      expect(response.status).toEqual(200);
    });

    it('returns unauthorized error on invalid call - without token', async () => {
      const expectedError = new Error('Unauthorized');

      try {
        const response = await fetchClientGet('/authtest', '');
      } catch (error) {
        expect(error).toEqual(expectedError);
      }
    });
  });
});
