import { render, screen } from "@testing-library/react";
import {
  BrowserRouter as Router,
} from "react-router-dom";
import { AuthContext } from "../utils/AuthContext";
import Authorization from "./Authorization";

describe(("Login page"), () => {
  const testComponent = (token: string = "") => {
    return (
      <Router>
        <AuthContext.Provider value={token}>
          <Authorization>
            <p>Authorized</p>
          </Authorization>
        </AuthContext.Provider>
      </Router>
    );
  };

  it("shows authorized view if token is provided", async () => {
    render(testComponent("TOKEN"));

    const authorizedComponent = await screen.findByText(/authorized/i);
    expect(authorizedComponent).toBeInTheDocument();
  })

  it("moves to login view if token is NOT provided", async () => {
    render(testComponent());

    expect(window.location.pathname).toEqual("/login");
  })
})