import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import {
  BrowserRouter as Router,
} from "react-router-dom";
import { DUMMY_USER } from "../setupTests";
import Login from "./Login";
import * as router from "react-router-dom";

describe(("Login page"), () => {
  let mockSetLoginToken: jest.Mock;

  jest.mock("react-router-dom", () => ({
    ...(jest.requireActual("react-router-dom")),
    useNavigate: jest.fn(),
  }));

  beforeEach(() => {
    mockSetLoginToken = jest.fn();
  })

  it("login with proper login data", async () => {
    const { container } = render(
      <Router>
        <Login setLoginToken={mockSetLoginToken} />
      </Router>
    );

    const usernameInput = container.querySelector('input[name="username"]');
    const passwordInput = container.querySelector('input[name="password"]');
    const submitButton = screen.getByRole("button", { name: /login/i });

    expect(usernameInput).toBeInTheDocument();
    expect(passwordInput).toBeInTheDocument();
    expect(submitButton).toBeInTheDocument();

    await userEvent.type(usernameInput as Element, DUMMY_USER.username);
    await userEvent.type(passwordInput as Element, DUMMY_USER.password);
    userEvent.click(submitButton);

    await waitFor(() => {
      expect(mockSetLoginToken).toHaveBeenCalled();
    });
  })
})