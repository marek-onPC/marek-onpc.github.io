import { rest } from 'msw';
import { DUMMY_NOTES, DUMMY_TOKEN } from '../setupTests';
import { AuthCredentials, NoteType } from '../types';

const authorizedCallHandler = (dummyToken: string) => {
  return rest.get("/api/authtest", (req, res, ctx) => {
    if (JSON.stringify(req.headers).includes(`"authorization":"Bearer ${dummyToken}"`)) {
      return res(
        ctx.status(200),
        ctx.json({
          token: dummyToken,
        }),
      )
    };

    return res(
      ctx.status(401),
      ctx.json({
        statusText: "Invalid token",
      }),
    );
  });
}

const _loginHandler = rest.post("/api/login", (req, res, ctx) => {
  const { username, password } = req.body as AuthCredentials;

  if (username === "username" && password === "password") {
    return res(
      ctx.status(200),
      ctx.json({
        token: DUMMY_TOKEN,
      }),
    )
  }

  return res(
    ctx.status(400),
  )
});

const _notesHandler = rest.get("/api/notes", (req, res, ctx) => {
  return res(
    ctx.status(200),
    ctx.json(JSON.stringify(DUMMY_NOTES)),
  )
});

export const handlers = [_loginHandler, _notesHandler];

export { authorizedCallHandler };
